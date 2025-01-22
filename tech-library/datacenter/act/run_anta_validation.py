import os
from anta import ANTAInventory, TestSuite
from anta.result_manager import ResultManager
import json

def load_inventory(file_path):
    """Load device inventory from a file."""
    with open(file_path, "r") as f:
        return json.load(f)

def run_anta_tests(inventory_file):
    """Run NRFU tests using ANTA."""
    # Retrieve credentials from environment variables
    username = os.getenv("ANTA_USERNAME")
    password = os.getenv("ANTA_PASSWORD")
    
    if not username or not password:
        raise ValueError("Missing ANTA_USERNAME or ANTA_PASSWORD environment variables.")

    # Load inventory
    inventory_data = load_inventory(inventory_file)
    inventory = ANTAInventory()
    inventory.add_devices_from_inventory(inventory_data, username=username, password=password)
    
    # Initialize test suite
    suite = TestSuite(inventory)

    # Add desired tests to the suite
    suite.add_testcase("TestNTPSynchronization")  # Example test case
    suite.add_testcase("TestLLDPNeighbors")  # Example test case

    # Run the tests
    suite.run()
    
    # Manage and return the results
    result_manager = ResultManager(suite)
    result_manager.render_results()
    return result_manager

if __name__ == "__main__":
    # Replace with your inventory file path
    inventory_file = "./inventory.json"
    
    results = run_anta_tests(inventory_file)
    
    # Optionally, exit with non-zero code if there are failures
    if results.failed_tests:
        print("Some tests failed.")
        exit(1)
    else:
        print("All tests passed.")
