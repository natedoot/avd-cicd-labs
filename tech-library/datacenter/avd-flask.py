from flask import Flask, render_template, request, redirect, url_for, flash
import yaml
import os
import subprocess
import datetime

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Needed for flash messages

MASTER_YAML_FILE = "tech-library/datacenter/group_vars/NETWORK_SERVICES.yml"
CONNECTED_ENDPOINTS_FILE = "tech-library/datacenter/group_vars/CONNECTED_ENDPOINTS.yml"
REPO_PATH = "/workspaces/avd-cicd-labs"

def load_yaml(file_path):
    """Loads YAML data from a file."""
    if not os.path.exists(file_path):
        return {}  # Return empty dict if file doesn't exist
    with open(file_path, "r") as f:
        return yaml.safe_load(f) or {}

def save_yaml(file_path, data):
    """Ensures the directory exists and saves YAML data to the file."""
    os.makedirs(os.path.dirname(file_path), exist_ok=True)  # Create the directory if it doesn't exist
    with open(file_path, "w") as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=False)
    commit_changes(file_path)  # Automatically commit changes

def commit_changes(file_path):
    """Commits changes to the local Git repository."""
    try:
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        commit_message = f"Auto-commit: Updated {os.path.basename(file_path)} at {timestamp}"

        subprocess.run(["git", "-C", REPO_PATH, "add", file_path], check=True)
        subprocess.run(["git", "-C", REPO_PATH, "commit", "-m", commit_message], check=True)
        flash(f"Changes to {os.path.basename(file_path)} committed successfully.", "success")

    except subprocess.CalledProcessError as e:
        flash(f"Git commit failed: {str(e)}", "danger")

def push_to_remote():
    """Creates a new branch and pushes committed changes to the remote repository."""
    try:
        # Generate a unique branch name based on timestamp
        timestamp = datetime.datetime.now().strftime("%Y%m%d-%H%M%S")
        branch_name = f"changes-{timestamp}"

        # Create a new branch
        subprocess.run(["git", "-C", REPO_PATH, "checkout", "-b", branch_name], check=True)
        
        # Push the new branch to GitHub
        subprocess.run(["git", "-C", REPO_PATH, "push", "origin", branch_name], check=True)

        flash(f"Changes pushed to remote branch {branch_name}.", "success")
    
    except subprocess.CalledProcessError as e:
        flash(f"Git push failed: {str(e)}", "danger")

def append_to_yaml(master_file, network_services_key, vrf_name, new_svi):
    """Appends SVI data to the specified tenant and VRF in the master YAML file,
    ensuring VRF VNI consistency across all tenants, and creating a new tenant if needed."""

    master_yaml = load_yaml(master_file)

    # Step 1: If tenant does not exist, create it
    if network_services_key not in master_yaml:
        master_yaml[network_services_key] = [
            {
                "name": network_services_key,
                "mac_vrf_vni_base": 10000,  # Default base value for new tenants
                "vrfs": []
            }
        ]
        flash(f"New tenant {network_services_key} created.", "info")

    # Step 2: Find if the VRF already exists in ANY tenant and reuse its vrf_vni
    existing_vrf_vni = None
    last_used_vrf_vni = 0  # Track highest VNI used

    for tenant_name, tenant_list in master_yaml.items():
        if isinstance(tenant_list, list) and len(tenant_list) > 0:
            tenant = tenant_list[0]  # Get the first tenant entry

            if "vrfs" in tenant and isinstance(tenant["vrfs"], list):
                for vrf in tenant["vrfs"]:
                    if isinstance(vrf, dict):
                        last_used_vrf_vni = max(last_used_vrf_vni, vrf.get("vrf_vni", 0))
                        if vrf.get("name") == vrf_name:
                            existing_vrf_vni = vrf["vrf_vni"]

    # If VRF does not exist anywhere, assign a new vrf_vni
    if existing_vrf_vni is None:
        existing_vrf_vni = last_used_vrf_vni + 1

    # Step 3: Ensure the current tenant exists (this should always be true now)
    tenant_list = master_yaml[network_services_key]
    if not isinstance(tenant_list, list) or len(tenant_list) == 0:
        flash(f"Invalid structure for {network_services_key} in NETWORK_SERVICES.yml.", "danger")
        return

    tenant = tenant_list[0]

    # Ensure VRFs exist in this tenant
    if "vrfs" not in tenant or not isinstance(tenant["vrfs"], list):
        tenant["vrfs"] = []

    vrf_list = tenant["vrfs"]

    # Step 4: Find or create the VRF within this tenant
    vrf = next((v for v in vrf_list if isinstance(v, dict) and v.get("name") == vrf_name), None)

    if not vrf:
        vrf = {"name": vrf_name, "vrf_vni": existing_vrf_vni, "svis": []}
        vrf_list.append(vrf)
        flash(f"New VRF {vrf_name} created in {network_services_key} with vrf_vni {existing_vrf_vni}.", "info")

    # Ensure "svis" exists in the VRF and is a list
    if "svis" not in vrf or not isinstance(vrf["svis"], list):
        vrf["svis"] = []

    # Step 5: Check if VLAN ID already exists
    if any(svi["id"] == new_svi["id"] for svi in vrf["svis"] if isinstance(svi, dict)):
        flash(f"SVI with VLAN ID {new_svi['id']} already exists in VRF {vrf_name}.", "danger")
        return

    # Step 6: Append the new SVI
    vrf["svis"].append(new_svi)
    save_yaml(master_file, master_yaml)
    flash("SVI successfully added!", "success")

def append_to_connected_endpoints(file_path, server_name, endpoint_ports, switch_ports, switches, vlans, native_vlan, mode, portfast, port_channel_desc, port_channel_mode):
    """Appends a new connected endpoint to CONNECTED_ENDPOINTS.yml."""
    data = load_yaml(file_path)

    # Ensure "servers" exists in the YAML structure
    if "servers" not in data:
        data["servers"] = []

    # Check if server already exists
    existing_server = next((s for s in data["servers"] if s["name"] == server_name), None)

    new_adapter = {
        "endpoint_ports": endpoint_ports.split(","),  # Convert comma-separated input into a list
        "switch_ports": switch_ports.split(","),  # Convert comma-separated input into a list
        "switches": switches.split(","),  # Convert comma-separated input into a list
        "vlans": vlans,  # Keep as a string (since ranges are allowed)
        "native_vlan": int(native_vlan),
        "mode": mode,
        "spanning_tree_portfast": portfast
    }

    # Add port-channel details if provided
    if port_channel_desc or port_channel_mode:
        new_adapter["port_channel"] = {}
        if port_channel_desc:
            new_adapter["port_channel"]["description"] = port_channel_desc
        if port_channel_mode:
            new_adapter["port_channel"]["mode"] = port_channel_mode

    if existing_server:
        # Append to existing server's adapters
        existing_server["adapters"].append(new_adapter)
    else:
        # Create a new server entry
        data["servers"].append({
            "name": server_name,
            "adapters": [new_adapter]
        })

    save_yaml(file_path, data)
    flash(f"Connected endpoint {server_name} added successfully!", "success")

@app.route("/")
def landing_page():
    """Landing page that links to different forms."""
    return render_template("landing_page.html")

@app.route("/network-services", methods=["GET", "POST"])
def network_services():
    master_yaml = load_yaml(MASTER_YAML_FILE)

    # Step 1: Extract list of tenants (top-level keys)
    tenants = sorted(master_yaml.keys())

    # Step 2: Extract all VRFs from all tenants
    all_vrfs = set()
    for tenant_name, tenant_list in master_yaml.items():
        if isinstance(tenant_list, list) and len(tenant_list) > 0:
            tenant = tenant_list[0]  # Assuming first element contains VRFs
            if "vrfs" in tenant and isinstance(tenant["vrfs"], list):
                for vrf in tenant["vrfs"]:
                    if isinstance(vrf, dict) and "name" in vrf:
                        all_vrfs.add(vrf["name"])

    if request.method == "POST":
        network_services_key = request.form.get("business_unit")  # Tenant Key
        custom_tenant = request.form.get("custom_tenant")  # If new tenant is provided
        vrf_name = request.form.get("vrf_name")
        custom_vrf = request.form.get("custom_vrf")  # If new VRF is provided
        vlan_id = request.form.get("vlan_id")
        svi_name = request.form.get("svi_name")
        ip_address = request.form.get("ip_address")
        enabled = request.form.get("enabled")

        # Use custom tenant if provided
        if network_services_key == "custom" and custom_tenant:
            network_services_key = custom_tenant

        # Use custom VRF if provided
        if vrf_name == "custom" and custom_vrf:
            vrf_name = custom_vrf

        if not (network_services_key and vrf_name and vlan_id and svi_name and ip_address and enabled):
            flash("All fields are required!", "danger")
            return redirect(url_for("network_services"))

        try:
            vlan_id = int(vlan_id)
        except ValueError:
            flash("VLAN ID must be an integer.", "danger")
            return redirect(url_for("network_services"))

        # Convert enabled from string to boolean
        enabled = True if enabled.lower() == "true" else False

        new_svi = {
            "id": vlan_id,
            "name": svi_name,
            "ip_address": ip_address,
            "enabled": enabled
        }

        append_to_yaml(MASTER_YAML_FILE, network_services_key, vrf_name, new_svi)
        return redirect(url_for("landing_page"))

    return render_template("network_services_form.html", tenants=tenants, all_vrfs=sorted(all_vrfs))


@app.route("/connected-endpoints", methods=["GET", "POST"])
def connected_endpoints():
    if request.method == "POST":
        server_name = request.form.get("server_name")
        endpoint_ports = request.form.get("endpoint_ports")
        switch_ports = request.form.get("switch_ports")
        switches = request.form.get("switches")
        vlans = request.form.get("vlans")
        native_vlan = request.form.get("native_vlan")
        mode = request.form.get("mode")
        portfast = request.form.get("portfast")
        port_channel_desc = request.form.get("port_channel_desc")
        port_channel_mode = request.form.get("port_channel_mode")

        if not all([server_name, endpoint_ports, switch_ports, switches, vlans, native_vlan, mode, portfast]):
            flash("All fields (except port-channel) are required!", "danger")
            return redirect(url_for("connected_endpoints"))

        append_to_connected_endpoints(CONNECTED_ENDPOINTS_FILE, server_name, endpoint_ports, switch_ports, switches, vlans, native_vlan, mode, portfast, port_channel_desc, port_channel_mode)
        return redirect(url_for("landing_page"))

    return render_template("connected_endpoints_form.html")

@app.route("/push-to-remote", methods=["POST"])
def push_remote():
    push_to_remote()
    return redirect(url_for("landing_page"))

if __name__ == "__main__":
    app.run(debug=True)
