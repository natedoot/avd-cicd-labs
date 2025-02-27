# FABRIC

## Table of Contents

- [Fabric Switches and Management IP](#fabric-switches-and-management-ip)
  - [Fabric Switches with inband Management IP](#fabric-switches-with-inband-management-ip)
- [Fabric Topology](#fabric-topology)
- [Fabric IP Allocation](#fabric-ip-allocation)
  - [Fabric Point-To-Point Links](#fabric-point-to-point-links)
  - [Point-To-Point Links Node Allocation](#point-to-point-links-node-allocation)
  - [Loopback Interfaces (BGP EVPN Peering)](#loopback-interfaces-bgp-evpn-peering)
  - [Loopback0 Interfaces Node Allocation](#loopback0-interfaces-node-allocation)
  - [ISIS CLNS interfaces](#isis-clns-interfaces)
  - [VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)](#vtep-loopback-vxlan-tunnel-source-interfaces-vteps-only)
  - [VTEP Loopback Node allocation](#vtep-loopback-node-allocation)

## Fabric Switches and Management IP

| POD | Type | Node | Management IP | Platform | Provisioned in CloudVision | Serial Number |
| --- | ---- | ---- | ------------- | -------- | -------------------------- | ------------- |
| pod-a | l3leaf | A-LEAF1 | 192.168.0.101/24 | vEOS-lab | Provisioned | - |
| pod-a | l3leaf | A-LEAF2 | 192.168.0.102/24 | vEOS-lab | Provisioned | - |
| pod-a | l3leaf | A-LEAF3 | 192.168.0.103/24 | vEOS-lab | Provisioned | - |
| pod-a | l3leaf | A-LEAF4 | 192.168.0.104/24 | vEOS-lab | Provisioned | - |
| pod-a | l3leaf | A-LEAF5 | 192.168.0.105/24 | vEOS-lab | Provisioned | - |
| pod-a | l3leaf | A-LEAF6 | 192.168.0.106/24 | vEOS-lab | Provisioned | - |
| pod-a | l3leaf | A-LEAF7 | 192.168.0.107/24 | vEOS-lab | Provisioned | - |
| pod-a | l3leaf | A-LEAF8 | 192.168.0.108/24 | vEOS-lab | Provisioned | - |
| pod-a | spine | A-SPINE1 | 192.168.0.11/24 | vEOS-lab | Provisioned | - |
| pod-a | spine | A-SPINE2 | 192.168.0.12/24 | vEOS-lab | Provisioned | - |
| pod-a | spine | A-SPINE3 | 192.168.0.13/24 | vEOS-lab | Provisioned | - |
| pod-a | spine | A-SPINE4 | 192.168.0.14/24 | vEOS-lab | Provisioned | - |
| pod-b | l3leaf | B-LEAF1 | 192.168.0.111/24 | vEOS-lab | Provisioned | - |
| pod-b | l3leaf | B-LEAF2 | 192.168.0.112/24 | vEOS-lab | Provisioned | - |
| pod-b | l3leaf | B-LEAF3 | 192.168.0.113/24 | vEOS-lab | Provisioned | - |
| pod-b | l3leaf | B-LEAF4 | 192.168.0.114/24 | vEOS-lab | Provisioned | - |
| pod-b | l3leaf | B-LEAF5 | 192.168.0.115/24 | vEOS-lab | Provisioned | - |
| pod-b | l3leaf | B-LEAF6 | 192.168.0.116/24 | vEOS-lab | Provisioned | - |
| pod-b | l3leaf | B-LEAF7 | 192.168.0.117/24 | vEOS-lab | Provisioned | - |
| pod-b | l3leaf | B-LEAF8 | 192.168.0.118/24 | vEOS-lab | Provisioned | - |
| pod-b | spine | B-SPINE1 | 192.168.0.15/24 | vEOS-lab | Provisioned | - |
| pod-b | spine | B-SPINE2 | 192.168.0.16/24 | vEOS-lab | Provisioned | - |
| pod-b | spine | B-SPINE3 | 192.168.0.17/24 | vEOS-lab | Provisioned | - |
| pod-b | spine | B-SPINE4 | 192.168.0.18/24 | vEOS-lab | Provisioned | - |
| pod-b | l2leaf | B-SW1 | 192.168.0.119/24 | vEOS-lab | Provisioned | - |
| pod-backbone | backbone | BB1 | 192.168.0.9/24 | vEOS-lab | Provisioned | - |
| pod-backbone | backbone | BB2 | 192.168.0.10/24 | vEOS-lab | Provisioned | - |
| pod-c | l3leaf | C-LEAF1 | 192.168.0.121/24 | vEOS-lab | Provisioned | - |
| pod-c | l3leaf | C-LEAF2 | 192.168.0.122/24 | vEOS-lab | Provisioned | - |
| pod-c | l3leaf | C-LEAF3 | 192.168.0.123/24 | vEOS-lab | Provisioned | - |
| pod-c | l3leaf | C-LEAF4 | 192.168.0.124/24 | vEOS-lab | Provisioned | - |
| pod-c | l3leaf | C-LEAF5 | 192.168.0.125/24 | vEOS-lab | Provisioned | - |
| pod-c | l3leaf | C-LEAF6 | 192.168.0.126/24 | vEOS-lab | Provisioned | - |
| pod-c | l3leaf | C-LEAF7 | 192.168.0.127/24 | vEOS-lab | Provisioned | - |
| pod-c | l3leaf | C-LEAF8 | 192.168.0.128/24 | vEOS-lab | Provisioned | - |
| pod-c | spine | C-SPINE1 | 192.168.0.19/24 | vEOS-lab | Provisioned | - |
| pod-c | spine | C-SPINE2 | 192.168.0.20/24 | vEOS-lab | Provisioned | - |
| pod-d | l3leaf | D-LEAF1 | 192.168.0.129/24 | vEOS-lab | Provisioned | - |
| pod-d | l3leaf | D-LEAF2 | 192.168.0.130/24 | vEOS-lab | Provisioned | - |
| pod-d | l3leaf | D-LEAF3 | 192.168.0.131/24 | vEOS-lab | Provisioned | - |
| pod-d | l3leaf | D-LEAF4 | 192.168.0.132/24 | vEOS-lab | Provisioned | - |
| pod-d | l3leaf | D-LEAF5 | 192.168.0.133/24 | vEOS-lab | Provisioned | - |
| pod-d | l3leaf | D-LEAF6 | 192.168.0.134/24 | vEOS-lab | Provisioned | - |
| pod-d | l3leaf | D-LEAF7 | 192.168.0.135/24 | vEOS-lab | Provisioned | - |
| pod-d | l3leaf | D-LEAF8 | 192.168.0.136/24 | vEOS-lab | Provisioned | - |
| pod-d | spine | D-SPINE1 | 192.168.0.21/24 | vEOS-lab | Provisioned | - |
| pod-d | spine | D-SPINE2 | 192.168.0.22/24 | vEOS-lab | Provisioned | - |
| pod-d | spine | D-SPINE3 | 192.168.0.23/24 | vEOS-lab | Provisioned | - |
| pod-d | spine | D-SPINE4 | 192.168.0.24/24 | vEOS-lab | Provisioned | - |

> Provision status is based on Ansible inventory declaration and do not represent real status from CloudVision.

### Fabric Switches with inband Management IP

| POD | Type | Node | Management IP | Inband Interface |
| --- | ---- | ---- | ------------- | ---------------- |

## Fabric Topology

| Type | Node | Node Interface | Peer Type | Peer Node | Peer Interface |
| ---- | ---- | -------------- | --------- | ----------| -------------- |
| l3leaf | A-LEAF1 | Ethernet1 | spine | A-SPINE1 | Ethernet1 |
| l3leaf | A-LEAF1 | Ethernet2 | spine | A-SPINE2 | Ethernet1 |
| l3leaf | A-LEAF1 | Ethernet3 | spine | A-SPINE3 | Ethernet1 |
| l3leaf | A-LEAF1 | Ethernet4 | spine | A-SPINE4 | Ethernet1 |
| l3leaf | A-LEAF1 | Ethernet5 | mlag_peer | A-LEAF2 | Ethernet5 |
| l3leaf | A-LEAF1 | Ethernet6 | mlag_peer | A-LEAF2 | Ethernet6 |
| l3leaf | A-LEAF2 | Ethernet1 | spine | A-SPINE1 | Ethernet2 |
| l3leaf | A-LEAF2 | Ethernet2 | spine | A-SPINE2 | Ethernet2 |
| l3leaf | A-LEAF2 | Ethernet3 | spine | A-SPINE3 | Ethernet2 |
| l3leaf | A-LEAF2 | Ethernet4 | spine | A-SPINE4 | Ethernet2 |
| l3leaf | A-LEAF3 | Ethernet1 | spine | A-SPINE1 | Ethernet3 |
| l3leaf | A-LEAF3 | Ethernet2 | spine | A-SPINE2 | Ethernet3 |
| l3leaf | A-LEAF3 | Ethernet3 | spine | A-SPINE3 | Ethernet3 |
| l3leaf | A-LEAF3 | Ethernet4 | spine | A-SPINE4 | Ethernet3 |
| l3leaf | A-LEAF3 | Ethernet5 | mlag_peer | A-LEAF4 | Ethernet5 |
| l3leaf | A-LEAF3 | Ethernet6 | mlag_peer | A-LEAF4 | Ethernet6 |
| l3leaf | A-LEAF4 | Ethernet1 | spine | A-SPINE1 | Ethernet4 |
| l3leaf | A-LEAF4 | Ethernet2 | spine | A-SPINE2 | Ethernet4 |
| l3leaf | A-LEAF4 | Ethernet3 | spine | A-SPINE3 | Ethernet4 |
| l3leaf | A-LEAF4 | Ethernet4 | spine | A-SPINE4 | Ethernet4 |
| l3leaf | A-LEAF5 | Ethernet1 | spine | A-SPINE1 | Ethernet5 |
| l3leaf | A-LEAF5 | Ethernet2 | spine | A-SPINE2 | Ethernet5 |
| l3leaf | A-LEAF5 | Ethernet3 | spine | A-SPINE3 | Ethernet5 |
| l3leaf | A-LEAF5 | Ethernet4 | spine | A-SPINE4 | Ethernet5 |
| l3leaf | A-LEAF5 | Ethernet5 | mlag_peer | A-LEAF6 | Ethernet5 |
| l3leaf | A-LEAF5 | Ethernet6 | mlag_peer | A-LEAF6 | Ethernet6 |
| l3leaf | A-LEAF6 | Ethernet1 | spine | A-SPINE1 | Ethernet6 |
| l3leaf | A-LEAF6 | Ethernet2 | spine | A-SPINE2 | Ethernet6 |
| l3leaf | A-LEAF6 | Ethernet3 | spine | A-SPINE3 | Ethernet6 |
| l3leaf | A-LEAF6 | Ethernet4 | spine | A-SPINE4 | Ethernet6 |
| l3leaf | A-LEAF7 | Ethernet1 | spine | A-SPINE1 | Ethernet7 |
| l3leaf | A-LEAF7 | Ethernet2 | spine | A-SPINE2 | Ethernet7 |
| l3leaf | A-LEAF7 | Ethernet3 | spine | A-SPINE3 | Ethernet7 |
| l3leaf | A-LEAF7 | Ethernet4 | spine | A-SPINE4 | Ethernet7 |
| l3leaf | A-LEAF7 | Ethernet5 | mlag_peer | A-LEAF8 | Ethernet5 |
| l3leaf | A-LEAF7 | Ethernet6 | mlag_peer | A-LEAF8 | Ethernet6 |
| l3leaf | A-LEAF7 | Ethernet7 | backbone | BB1 | Ethernet1 |
| l3leaf | A-LEAF7 | Ethernet8 | backbone | BB2 | Ethernet1 |
| l3leaf | A-LEAF8 | Ethernet1 | spine | A-SPINE1 | Ethernet8 |
| l3leaf | A-LEAF8 | Ethernet2 | spine | A-SPINE2 | Ethernet8 |
| l3leaf | A-LEAF8 | Ethernet3 | spine | A-SPINE3 | Ethernet8 |
| l3leaf | A-LEAF8 | Ethernet4 | spine | A-SPINE4 | Ethernet8 |
| l3leaf | A-LEAF8 | Ethernet7 | backbone | BB1 | Ethernet2 |
| l3leaf | A-LEAF8 | Ethernet8 | backbone | BB2 | Ethernet2 |
| l3leaf | B-LEAF1 | Ethernet1 | spine | B-SPINE1 | Ethernet1 |
| l3leaf | B-LEAF1 | Ethernet2 | spine | B-SPINE2 | Ethernet1 |
| l3leaf | B-LEAF1 | Ethernet3 | spine | B-SPINE3 | Ethernet1 |
| l3leaf | B-LEAF1 | Ethernet4 | spine | B-SPINE4 | Ethernet1 |
| l3leaf | B-LEAF2 | Ethernet1 | spine | B-SPINE1 | Ethernet2 |
| l3leaf | B-LEAF2 | Ethernet2 | spine | B-SPINE2 | Ethernet2 |
| l3leaf | B-LEAF2 | Ethernet3 | spine | B-SPINE3 | Ethernet2 |
| l3leaf | B-LEAF2 | Ethernet4 | spine | B-SPINE4 | Ethernet2 |
| l3leaf | B-LEAF3 | Ethernet1 | spine | B-SPINE1 | Ethernet3 |
| l3leaf | B-LEAF3 | Ethernet2 | spine | B-SPINE2 | Ethernet3 |
| l3leaf | B-LEAF3 | Ethernet3 | spine | B-SPINE3 | Ethernet3 |
| l3leaf | B-LEAF3 | Ethernet4 | spine | B-SPINE4 | Ethernet3 |
| l3leaf | B-LEAF4 | Ethernet1 | spine | B-SPINE1 | Ethernet4 |
| l3leaf | B-LEAF4 | Ethernet2 | spine | B-SPINE2 | Ethernet4 |
| l3leaf | B-LEAF4 | Ethernet3 | spine | B-SPINE3 | Ethernet4 |
| l3leaf | B-LEAF4 | Ethernet4 | spine | B-SPINE4 | Ethernet4 |
| l3leaf | B-LEAF5 | Ethernet1 | spine | B-SPINE1 | Ethernet5 |
| l3leaf | B-LEAF5 | Ethernet2 | spine | B-SPINE2 | Ethernet5 |
| l3leaf | B-LEAF5 | Ethernet3 | spine | B-SPINE3 | Ethernet5 |
| l3leaf | B-LEAF5 | Ethernet4 | spine | B-SPINE4 | Ethernet5 |
| l3leaf | B-LEAF5 | Ethernet7 | l2leaf | B-SW1 | Ethernet1 |
| l3leaf | B-LEAF6 | Ethernet1 | spine | B-SPINE1 | Ethernet6 |
| l3leaf | B-LEAF6 | Ethernet2 | spine | B-SPINE2 | Ethernet6 |
| l3leaf | B-LEAF6 | Ethernet3 | spine | B-SPINE3 | Ethernet6 |
| l3leaf | B-LEAF6 | Ethernet4 | spine | B-SPINE4 | Ethernet6 |
| l3leaf | B-LEAF6 | Ethernet7 | l2leaf | B-SW1 | Ethernet2 |
| l3leaf | B-LEAF7 | Ethernet1 | spine | B-SPINE1 | Ethernet7 |
| l3leaf | B-LEAF7 | Ethernet2 | spine | B-SPINE2 | Ethernet7 |
| l3leaf | B-LEAF7 | Ethernet3 | spine | B-SPINE3 | Ethernet7 |
| l3leaf | B-LEAF7 | Ethernet4 | spine | B-SPINE4 | Ethernet7 |
| l3leaf | B-LEAF7 | Ethernet7 | backbone | BB1 | Ethernet3 |
| l3leaf | B-LEAF7 | Ethernet8 | backbone | BB2 | Ethernet3 |
| l3leaf | B-LEAF8 | Ethernet1 | spine | B-SPINE1 | Ethernet8 |
| l3leaf | B-LEAF8 | Ethernet2 | spine | B-SPINE2 | Ethernet8 |
| l3leaf | B-LEAF8 | Ethernet3 | spine | B-SPINE3 | Ethernet8 |
| l3leaf | B-LEAF8 | Ethernet4 | spine | B-SPINE4 | Ethernet8 |
| l3leaf | B-LEAF8 | Ethernet7 | backbone | BB1 | Ethernet4 |
| l3leaf | B-LEAF8 | Ethernet8 | backbone | BB2 | Ethernet4 |
| backbone | BB1 | Ethernet5 | l3leaf | C-LEAF7 | Ethernet7 |
| backbone | BB1 | Ethernet6 | l3leaf | C-LEAF8 | Ethernet7 |
| backbone | BB1 | Ethernet7 | l3leaf | D-LEAF7 | Ethernet7 |
| backbone | BB1 | Ethernet8 | l3leaf | D-LEAF8 | Ethernet7 |
| backbone | BB2 | Ethernet5 | l3leaf | C-LEAF7 | Ethernet8 |
| backbone | BB2 | Ethernet6 | l3leaf | C-LEAF8 | Ethernet8 |
| backbone | BB2 | Ethernet7 | l3leaf | D-LEAF7 | Ethernet8 |
| backbone | BB2 | Ethernet8 | l3leaf | D-LEAF8 | Ethernet8 |
| l3leaf | C-LEAF1 | Ethernet1 | spine | C-SPINE1 | Ethernet1 |
| l3leaf | C-LEAF1 | Ethernet2 | spine | C-SPINE2 | Ethernet1 |
| l3leaf | C-LEAF1 | Ethernet5 | mlag_peer | C-LEAF2 | Ethernet5 |
| l3leaf | C-LEAF1 | Ethernet6 | mlag_peer | C-LEAF2 | Ethernet6 |
| l3leaf | C-LEAF2 | Ethernet1 | spine | C-SPINE1 | Ethernet2 |
| l3leaf | C-LEAF2 | Ethernet2 | spine | C-SPINE2 | Ethernet2 |
| l3leaf | C-LEAF3 | Ethernet1 | spine | C-SPINE1 | Ethernet3 |
| l3leaf | C-LEAF3 | Ethernet2 | spine | C-SPINE2 | Ethernet3 |
| l3leaf | C-LEAF3 | Ethernet5 | mlag_peer | C-LEAF4 | Ethernet5 |
| l3leaf | C-LEAF3 | Ethernet6 | mlag_peer | C-LEAF4 | Ethernet6 |
| l3leaf | C-LEAF4 | Ethernet1 | spine | C-SPINE1 | Ethernet4 |
| l3leaf | C-LEAF4 | Ethernet2 | spine | C-SPINE2 | Ethernet4 |
| l3leaf | C-LEAF5 | Ethernet1 | spine | C-SPINE1 | Ethernet5 |
| l3leaf | C-LEAF5 | Ethernet2 | spine | C-SPINE2 | Ethernet5 |
| l3leaf | C-LEAF5 | Ethernet5 | mlag_peer | C-LEAF6 | Ethernet5 |
| l3leaf | C-LEAF5 | Ethernet6 | mlag_peer | C-LEAF6 | Ethernet6 |
| l3leaf | C-LEAF6 | Ethernet1 | spine | C-SPINE1 | Ethernet6 |
| l3leaf | C-LEAF6 | Ethernet2 | spine | C-SPINE2 | Ethernet6 |
| l3leaf | C-LEAF7 | Ethernet1 | spine | C-SPINE1 | Ethernet7 |
| l3leaf | C-LEAF7 | Ethernet2 | spine | C-SPINE2 | Ethernet7 |
| l3leaf | C-LEAF7 | Ethernet5 | mlag_peer | C-LEAF8 | Ethernet5 |
| l3leaf | C-LEAF7 | Ethernet6 | mlag_peer | C-LEAF8 | Ethernet6 |
| l3leaf | C-LEAF8 | Ethernet1 | spine | C-SPINE1 | Ethernet8 |
| l3leaf | C-LEAF8 | Ethernet2 | spine | C-SPINE2 | Ethernet8 |
| l3leaf | D-LEAF1 | Ethernet1 | spine | D-SPINE1 | Ethernet1 |
| l3leaf | D-LEAF1 | Ethernet2 | spine | D-SPINE2 | Ethernet1 |
| l3leaf | D-LEAF1 | Ethernet3 | spine | D-SPINE3 | Ethernet1 |
| l3leaf | D-LEAF1 | Ethernet4 | spine | D-SPINE4 | Ethernet1 |
| l3leaf | D-LEAF1 | Ethernet5 | mlag_peer | D-LEAF2 | Ethernet5 |
| l3leaf | D-LEAF1 | Ethernet6 | mlag_peer | D-LEAF2 | Ethernet6 |
| l3leaf | D-LEAF2 | Ethernet1 | spine | D-SPINE1 | Ethernet2 |
| l3leaf | D-LEAF2 | Ethernet2 | spine | D-SPINE2 | Ethernet2 |
| l3leaf | D-LEAF2 | Ethernet3 | spine | D-SPINE3 | Ethernet2 |
| l3leaf | D-LEAF2 | Ethernet4 | spine | D-SPINE4 | Ethernet2 |
| l3leaf | D-LEAF3 | Ethernet1 | spine | D-SPINE1 | Ethernet3 |
| l3leaf | D-LEAF3 | Ethernet2 | spine | D-SPINE2 | Ethernet3 |
| l3leaf | D-LEAF3 | Ethernet3 | spine | D-SPINE3 | Ethernet3 |
| l3leaf | D-LEAF3 | Ethernet4 | spine | D-SPINE4 | Ethernet3 |
| l3leaf | D-LEAF3 | Ethernet5 | mlag_peer | D-LEAF4 | Ethernet5 |
| l3leaf | D-LEAF3 | Ethernet6 | mlag_peer | D-LEAF4 | Ethernet6 |
| l3leaf | D-LEAF4 | Ethernet1 | spine | D-SPINE1 | Ethernet4 |
| l3leaf | D-LEAF4 | Ethernet2 | spine | D-SPINE2 | Ethernet4 |
| l3leaf | D-LEAF4 | Ethernet3 | spine | D-SPINE3 | Ethernet4 |
| l3leaf | D-LEAF4 | Ethernet4 | spine | D-SPINE4 | Ethernet4 |
| l3leaf | D-LEAF5 | Ethernet1 | spine | D-SPINE1 | Ethernet5 |
| l3leaf | D-LEAF5 | Ethernet2 | spine | D-SPINE2 | Ethernet5 |
| l3leaf | D-LEAF5 | Ethernet3 | spine | D-SPINE3 | Ethernet5 |
| l3leaf | D-LEAF5 | Ethernet4 | spine | D-SPINE4 | Ethernet5 |
| l3leaf | D-LEAF5 | Ethernet5 | mlag_peer | D-LEAF6 | Ethernet5 |
| l3leaf | D-LEAF5 | Ethernet6 | mlag_peer | D-LEAF6 | Ethernet6 |
| l3leaf | D-LEAF6 | Ethernet1 | spine | D-SPINE1 | Ethernet6 |
| l3leaf | D-LEAF6 | Ethernet2 | spine | D-SPINE2 | Ethernet6 |
| l3leaf | D-LEAF6 | Ethernet3 | spine | D-SPINE3 | Ethernet6 |
| l3leaf | D-LEAF6 | Ethernet4 | spine | D-SPINE4 | Ethernet6 |
| l3leaf | D-LEAF7 | Ethernet1 | spine | D-SPINE1 | Ethernet7 |
| l3leaf | D-LEAF7 | Ethernet2 | spine | D-SPINE2 | Ethernet7 |
| l3leaf | D-LEAF7 | Ethernet3 | spine | D-SPINE3 | Ethernet7 |
| l3leaf | D-LEAF7 | Ethernet4 | spine | D-SPINE4 | Ethernet7 |
| l3leaf | D-LEAF8 | Ethernet1 | spine | D-SPINE1 | Ethernet8 |
| l3leaf | D-LEAF8 | Ethernet2 | spine | D-SPINE2 | Ethernet8 |
| l3leaf | D-LEAF8 | Ethernet3 | spine | D-SPINE3 | Ethernet8 |
| l3leaf | D-LEAF8 | Ethernet4 | spine | D-SPINE4 | Ethernet8 |

## Fabric IP Allocation

### Fabric Point-To-Point Links

| Uplink IPv4 Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ---------------- | ------------------- | ------------------ | ------------------ |
| 192.168.1.0/24 | 256 | 176 | 68.75 % |

### Point-To-Point Links Node Allocation

| Node | Node Interface | Node IP Address | Peer Node | Peer Interface | Peer IP Address |
| ---- | -------------- | --------------- | --------- | -------------- | --------------- |
| A-LEAF1 | Ethernet1 | 192.168.1.1/31 | A-SPINE1 | Ethernet1 | 192.168.1.0/31 |
| A-LEAF1 | Ethernet2 | 192.168.1.3/31 | A-SPINE2 | Ethernet1 | 192.168.1.2/31 |
| A-LEAF1 | Ethernet3 | 192.168.1.5/31 | A-SPINE3 | Ethernet1 | 192.168.1.4/31 |
| A-LEAF1 | Ethernet4 | 192.168.1.7/31 | A-SPINE4 | Ethernet1 | 192.168.1.6/31 |
| A-LEAF2 | Ethernet1 | 192.168.1.9/31 | A-SPINE1 | Ethernet2 | 192.168.1.8/31 |
| A-LEAF2 | Ethernet2 | 192.168.1.11/31 | A-SPINE2 | Ethernet2 | 192.168.1.10/31 |
| A-LEAF2 | Ethernet3 | 192.168.1.13/31 | A-SPINE3 | Ethernet2 | 192.168.1.12/31 |
| A-LEAF2 | Ethernet4 | 192.168.1.15/31 | A-SPINE4 | Ethernet2 | 192.168.1.14/31 |
| A-LEAF3 | Ethernet1 | 192.168.1.17/31 | A-SPINE1 | Ethernet3 | 192.168.1.16/31 |
| A-LEAF3 | Ethernet2 | 192.168.1.19/31 | A-SPINE2 | Ethernet3 | 192.168.1.18/31 |
| A-LEAF3 | Ethernet3 | 192.168.1.21/31 | A-SPINE3 | Ethernet3 | 192.168.1.20/31 |
| A-LEAF3 | Ethernet4 | 192.168.1.23/31 | A-SPINE4 | Ethernet3 | 192.168.1.22/31 |
| A-LEAF4 | Ethernet1 | 192.168.1.25/31 | A-SPINE1 | Ethernet4 | 192.168.1.24/31 |
| A-LEAF4 | Ethernet2 | 192.168.1.27/31 | A-SPINE2 | Ethernet4 | 192.168.1.26/31 |
| A-LEAF4 | Ethernet3 | 192.168.1.29/31 | A-SPINE3 | Ethernet4 | 192.168.1.28/31 |
| A-LEAF4 | Ethernet4 | 192.168.1.31/31 | A-SPINE4 | Ethernet4 | 192.168.1.30/31 |
| A-LEAF5 | Ethernet1 | 192.168.1.33/31 | A-SPINE1 | Ethernet5 | 192.168.1.32/31 |
| A-LEAF5 | Ethernet2 | 192.168.1.35/31 | A-SPINE2 | Ethernet5 | 192.168.1.34/31 |
| A-LEAF5 | Ethernet3 | 192.168.1.37/31 | A-SPINE3 | Ethernet5 | 192.168.1.36/31 |
| A-LEAF5 | Ethernet4 | 192.168.1.39/31 | A-SPINE4 | Ethernet5 | 192.168.1.38/31 |
| A-LEAF6 | Ethernet1 | 192.168.1.41/31 | A-SPINE1 | Ethernet6 | 192.168.1.40/31 |
| A-LEAF6 | Ethernet2 | 192.168.1.43/31 | A-SPINE2 | Ethernet6 | 192.168.1.42/31 |
| A-LEAF6 | Ethernet3 | 192.168.1.45/31 | A-SPINE3 | Ethernet6 | 192.168.1.44/31 |
| A-LEAF6 | Ethernet4 | 192.168.1.47/31 | A-SPINE4 | Ethernet6 | 192.168.1.46/31 |
| A-LEAF7 | Ethernet1 | 192.168.1.49/31 | A-SPINE1 | Ethernet7 | 192.168.1.48/31 |
| A-LEAF7 | Ethernet2 | 192.168.1.51/31 | A-SPINE2 | Ethernet7 | 192.168.1.50/31 |
| A-LEAF7 | Ethernet3 | 192.168.1.53/31 | A-SPINE3 | Ethernet7 | 192.168.1.52/31 |
| A-LEAF7 | Ethernet4 | 192.168.1.55/31 | A-SPINE4 | Ethernet7 | 192.168.1.54/31 |
| A-LEAF7 | Ethernet7 | 172.16.1.0/31 | BB1 | Ethernet1 | 172.16.1.1/31 |
| A-LEAF7 | Ethernet8 | 172.16.1.2/31 | BB2 | Ethernet1 | 172.16.1.3/31 |
| A-LEAF8 | Ethernet1 | 192.168.1.57/31 | A-SPINE1 | Ethernet8 | 192.168.1.56/31 |
| A-LEAF8 | Ethernet2 | 192.168.1.59/31 | A-SPINE2 | Ethernet8 | 192.168.1.58/31 |
| A-LEAF8 | Ethernet3 | 192.168.1.61/31 | A-SPINE3 | Ethernet8 | 192.168.1.60/31 |
| A-LEAF8 | Ethernet4 | 192.168.1.63/31 | A-SPINE4 | Ethernet8 | 192.168.1.62/31 |
| A-LEAF8 | Ethernet7 | 172.16.1.4/31 | BB1 | Ethernet2 | 172.16.1.5/31 |
| A-LEAF8 | Ethernet8 | 172.16.1.6/31 | BB2 | Ethernet2 | 172.16.1.7/31 |
| B-LEAF1 | Ethernet1 | 192.168.1.1/31 | B-SPINE1 | Ethernet1 | 192.168.1.0/31 |
| B-LEAF1 | Ethernet2 | 192.168.1.3/31 | B-SPINE2 | Ethernet1 | 192.168.1.2/31 |
| B-LEAF1 | Ethernet3 | 192.168.1.5/31 | B-SPINE3 | Ethernet1 | 192.168.1.4/31 |
| B-LEAF1 | Ethernet4 | 192.168.1.7/31 | B-SPINE4 | Ethernet1 | 192.168.1.6/31 |
| B-LEAF2 | Ethernet1 | 192.168.1.9/31 | B-SPINE1 | Ethernet2 | 192.168.1.8/31 |
| B-LEAF2 | Ethernet2 | 192.168.1.11/31 | B-SPINE2 | Ethernet2 | 192.168.1.10/31 |
| B-LEAF2 | Ethernet3 | 192.168.1.13/31 | B-SPINE3 | Ethernet2 | 192.168.1.12/31 |
| B-LEAF2 | Ethernet4 | 192.168.1.15/31 | B-SPINE4 | Ethernet2 | 192.168.1.14/31 |
| B-LEAF3 | Ethernet1 | 192.168.1.17/31 | B-SPINE1 | Ethernet3 | 192.168.1.16/31 |
| B-LEAF3 | Ethernet2 | 192.168.1.19/31 | B-SPINE2 | Ethernet3 | 192.168.1.18/31 |
| B-LEAF3 | Ethernet3 | 192.168.1.21/31 | B-SPINE3 | Ethernet3 | 192.168.1.20/31 |
| B-LEAF3 | Ethernet4 | 192.168.1.23/31 | B-SPINE4 | Ethernet3 | 192.168.1.22/31 |
| B-LEAF4 | Ethernet1 | 192.168.1.25/31 | B-SPINE1 | Ethernet4 | 192.168.1.24/31 |
| B-LEAF4 | Ethernet2 | 192.168.1.27/31 | B-SPINE2 | Ethernet4 | 192.168.1.26/31 |
| B-LEAF4 | Ethernet3 | 192.168.1.29/31 | B-SPINE3 | Ethernet4 | 192.168.1.28/31 |
| B-LEAF4 | Ethernet4 | 192.168.1.31/31 | B-SPINE4 | Ethernet4 | 192.168.1.30/31 |
| B-LEAF5 | Ethernet1 | 192.168.1.33/31 | B-SPINE1 | Ethernet5 | 192.168.1.32/31 |
| B-LEAF5 | Ethernet2 | 192.168.1.35/31 | B-SPINE2 | Ethernet5 | 192.168.1.34/31 |
| B-LEAF5 | Ethernet3 | 192.168.1.37/31 | B-SPINE3 | Ethernet5 | 192.168.1.36/31 |
| B-LEAF5 | Ethernet4 | 192.168.1.39/31 | B-SPINE4 | Ethernet5 | 192.168.1.38/31 |
| B-LEAF6 | Ethernet1 | 192.168.1.41/31 | B-SPINE1 | Ethernet6 | 192.168.1.40/31 |
| B-LEAF6 | Ethernet2 | 192.168.1.43/31 | B-SPINE2 | Ethernet6 | 192.168.1.42/31 |
| B-LEAF6 | Ethernet3 | 192.168.1.45/31 | B-SPINE3 | Ethernet6 | 192.168.1.44/31 |
| B-LEAF6 | Ethernet4 | 192.168.1.47/31 | B-SPINE4 | Ethernet6 | 192.168.1.46/31 |
| B-LEAF7 | Ethernet1 | 192.168.1.49/31 | B-SPINE1 | Ethernet7 | 192.168.1.48/31 |
| B-LEAF7 | Ethernet2 | 192.168.1.51/31 | B-SPINE2 | Ethernet7 | 192.168.1.50/31 |
| B-LEAF7 | Ethernet3 | 192.168.1.53/31 | B-SPINE3 | Ethernet7 | 192.168.1.52/31 |
| B-LEAF7 | Ethernet4 | 192.168.1.55/31 | B-SPINE4 | Ethernet7 | 192.168.1.54/31 |
| B-LEAF7 | Ethernet7 | 172.16.2.0/31 | BB1 | Ethernet3 | 172.16.2.1/31 |
| B-LEAF7 | Ethernet8 | 172.16.2.2/31 | BB2 | Ethernet3 | 172.16.2.3/31 |
| B-LEAF8 | Ethernet1 | 192.168.1.57/31 | B-SPINE1 | Ethernet8 | 192.168.1.56/31 |
| B-LEAF8 | Ethernet2 | 192.168.1.59/31 | B-SPINE2 | Ethernet8 | 192.168.1.58/31 |
| B-LEAF8 | Ethernet3 | 192.168.1.61/31 | B-SPINE3 | Ethernet8 | 192.168.1.60/31 |
| B-LEAF8 | Ethernet4 | 192.168.1.63/31 | B-SPINE4 | Ethernet8 | 192.168.1.62/31 |
| B-LEAF8 | Ethernet7 | 172.16.2.4/31 | BB1 | Ethernet4 | 172.16.2.5/31 |
| B-LEAF8 | Ethernet8 | 172.16.2.6/31 | BB2 | Ethernet4 | 172.16.2.7/31 |
| BB1 | Ethernet5 | 172.16.3.1/31 | C-LEAF7 | Ethernet7 | 172.16.3.0/31 |
| BB1 | Ethernet6 | 172.16.3.5/31 | C-LEAF8 | Ethernet7 | 172.16.3.4/31 |
| BB1 | Ethernet7 | 172.16.4.1/31 | D-LEAF7 | Ethernet7 | 172.16.4.0/31 |
| BB1 | Ethernet8 | 172.16.4.5/31 | D-LEAF8 | Ethernet7 | 172.16.4.4/31 |
| BB2 | Ethernet5 | 172.16.3.3/31 | C-LEAF7 | Ethernet8 | 172.16.3.2/31 |
| BB2 | Ethernet6 | 172.16.3.7/31 | C-LEAF8 | Ethernet8 | 172.16.3.6/31 |
| BB2 | Ethernet7 | 172.16.4.3/31 | D-LEAF7 | Ethernet8 | 172.16.4.2/31 |
| BB2 | Ethernet8 | 172.16.4.7/31 | D-LEAF8 | Ethernet8 | 172.16.4.6/31 |
| C-LEAF1 | Ethernet1 | 192.168.1.1/31 | C-SPINE1 | Ethernet1 | 192.168.1.0/31 |
| C-LEAF1 | Ethernet2 | 192.168.1.3/31 | C-SPINE2 | Ethernet1 | 192.168.1.2/31 |
| C-LEAF2 | Ethernet1 | 192.168.1.5/31 | C-SPINE1 | Ethernet2 | 192.168.1.4/31 |
| C-LEAF2 | Ethernet2 | 192.168.1.7/31 | C-SPINE2 | Ethernet2 | 192.168.1.6/31 |
| C-LEAF3 | Ethernet1 | 192.168.1.9/31 | C-SPINE1 | Ethernet3 | 192.168.1.8/31 |
| C-LEAF3 | Ethernet2 | 192.168.1.11/31 | C-SPINE2 | Ethernet3 | 192.168.1.10/31 |
| C-LEAF4 | Ethernet1 | 192.168.1.13/31 | C-SPINE1 | Ethernet4 | 192.168.1.12/31 |
| C-LEAF4 | Ethernet2 | 192.168.1.15/31 | C-SPINE2 | Ethernet4 | 192.168.1.14/31 |
| C-LEAF5 | Ethernet1 | 192.168.1.17/31 | C-SPINE1 | Ethernet5 | 192.168.1.16/31 |
| C-LEAF5 | Ethernet2 | 192.168.1.19/31 | C-SPINE2 | Ethernet5 | 192.168.1.18/31 |
| C-LEAF6 | Ethernet1 | 192.168.1.21/31 | C-SPINE1 | Ethernet6 | 192.168.1.20/31 |
| C-LEAF6 | Ethernet2 | 192.168.1.23/31 | C-SPINE2 | Ethernet6 | 192.168.1.22/31 |
| C-LEAF7 | Ethernet1 | 192.168.1.25/31 | C-SPINE1 | Ethernet7 | 192.168.1.24/31 |
| C-LEAF7 | Ethernet2 | 192.168.1.27/31 | C-SPINE2 | Ethernet7 | 192.168.1.26/31 |
| C-LEAF8 | Ethernet1 | 192.168.1.29/31 | C-SPINE1 | Ethernet8 | 192.168.1.28/31 |
| C-LEAF8 | Ethernet2 | 192.168.1.31/31 | C-SPINE2 | Ethernet8 | 192.168.1.30/31 |
| D-LEAF7 | Ethernet1 | 192.168.1.49/31 | D-SPINE1 | Ethernet7 | 192.168.1.48/31 |
| D-LEAF7 | Ethernet2 | 192.168.1.51/31 | D-SPINE2 | Ethernet7 | 192.168.1.50/31 |
| D-LEAF7 | Ethernet3 | 192.168.1.53/31 | D-SPINE3 | Ethernet7 | 192.168.1.52/31 |
| D-LEAF7 | Ethernet4 | 192.168.1.55/31 | D-SPINE4 | Ethernet7 | 192.168.1.54/31 |
| D-LEAF8 | Ethernet1 | 192.168.1.57/31 | D-SPINE1 | Ethernet8 | 192.168.1.56/31 |
| D-LEAF8 | Ethernet2 | 192.168.1.59/31 | D-SPINE2 | Ethernet8 | 192.168.1.58/31 |
| D-LEAF8 | Ethernet3 | 192.168.1.61/31 | D-SPINE3 | Ethernet8 | 192.168.1.60/31 |
| D-LEAF8 | Ethernet4 | 192.168.1.63/31 | D-SPINE4 | Ethernet8 | 192.168.1.62/31 |

### Loopback Interfaces (BGP EVPN Peering)

| Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------- | ------------------- | ------------------ | ------------------ |
| 1.1.0.0/24 | 256 | 2 | 0.79 % |
| 1.1.1.0/24 | 256 | 12 | 4.69 % |
| 1.1.2.0/24 | 256 | 12 | 4.69 % |
| 1.1.3.0/24 | 256 | 10 | 3.91 % |
| 1.1.4.0/24 | 256 | 12 | 4.69 % |

### Loopback0 Interfaces Node Allocation

| POD | Node | Loopback0 |
| --- | ---- | --------- |
| pod-a | A-LEAF1 | 1.1.1.1/32 |
| pod-a | A-LEAF2 | 1.1.1.2/32 |
| pod-a | A-LEAF3 | 1.1.1.3/32 |
| pod-a | A-LEAF4 | 1.1.1.4/32 |
| pod-a | A-LEAF5 | 1.1.1.5/32 |
| pod-a | A-LEAF6 | 1.1.1.6/32 |
| pod-a | A-LEAF7 | 1.1.1.7/32 |
| pod-a | A-LEAF8 | 1.1.1.8/32 |
| pod-a | A-SPINE1 | 1.1.1.201/32 |
| pod-a | A-SPINE2 | 1.1.1.202/32 |
| pod-a | A-SPINE3 | 1.1.1.203/32 |
| pod-a | A-SPINE4 | 1.1.1.204/32 |
| pod-b | B-LEAF1 | 1.1.2.1/32 |
| pod-b | B-LEAF2 | 1.1.2.2/32 |
| pod-b | B-LEAF3 | 1.1.2.3/32 |
| pod-b | B-LEAF4 | 1.1.2.4/32 |
| pod-b | B-LEAF5 | 1.1.2.5/32 |
| pod-b | B-LEAF6 | 1.1.2.6/32 |
| pod-b | B-LEAF7 | 1.1.2.7/32 |
| pod-b | B-LEAF8 | 1.1.2.8/32 |
| pod-b | B-SPINE1 | 1.1.2.201/32 |
| pod-b | B-SPINE2 | 1.1.2.202/32 |
| pod-b | B-SPINE3 | 1.1.2.203/32 |
| pod-b | B-SPINE4 | 1.1.2.204/32 |
| pod-backbone | BB1 | 1.1.0.1/32 |
| pod-backbone | BB2 | 1.1.0.2/32 |
| pod-c | C-LEAF1 | 1.1.3.1/32 |
| pod-c | C-LEAF2 | 1.1.3.2/32 |
| pod-c | C-LEAF3 | 1.1.3.3/32 |
| pod-c | C-LEAF4 | 1.1.3.4/32 |
| pod-c | C-LEAF5 | 1.1.3.5/32 |
| pod-c | C-LEAF6 | 1.1.3.6/32 |
| pod-c | C-LEAF7 | 1.1.3.7/32 |
| pod-c | C-LEAF8 | 1.1.3.8/32 |
| pod-c | C-SPINE1 | 1.1.3.201/32 |
| pod-c | C-SPINE2 | 1.1.3.202/32 |
| pod-d | D-LEAF1 | 1.1.4.1/32 |
| pod-d | D-LEAF2 | 1.1.4.2/32 |
| pod-d | D-LEAF3 | 1.1.4.3/32 |
| pod-d | D-LEAF4 | 1.1.4.4/32 |
| pod-d | D-LEAF5 | 1.1.4.5/32 |
| pod-d | D-LEAF6 | 1.1.4.6/32 |
| pod-d | D-LEAF7 | 1.1.4.7/32 |
| pod-d | D-LEAF8 | 1.1.4.8/32 |
| pod-d | D-SPINE1 | 1.1.4.201/32 |
| pod-d | D-SPINE2 | 1.1.4.202/32 |
| pod-d | D-SPINE3 | 1.1.4.203/32 |
| pod-d | D-SPINE4 | 1.1.4.204/32 |

### ISIS CLNS interfaces

| POD | Node | CLNS Address |
| --- | ---- | ------------ |
| pod-b | B-LEAF1 | 49.1111.0010.0100.2001.00 |
| pod-b | B-LEAF2 | 49.1111.0010.0100.2002.00 |
| pod-b | B-LEAF3 | 49.1111.0010.0100.2003.00 |
| pod-b | B-LEAF4 | 49.1111.0010.0100.2004.00 |
| pod-b | B-LEAF5 | 49.1111.0010.0100.2005.00 |
| pod-b | B-LEAF6 | 49.1111.0010.0100.2006.00 |
| pod-b | B-LEAF7 | 49.1111.0010.0100.2007.00 |
| pod-b | B-LEAF8 | 49.1111.0010.0100.2008.00 |
| pod-b | B-SPINE1 | 49.1111.0010.0100.2201.00 |
| pod-b | B-SPINE2 | 49.1111.0010.0100.2202.00 |
| pod-b | B-SPINE3 | 49.1111.0010.0100.2203.00 |
| pod-b | B-SPINE4 | 49.1111.0010.0100.2204.00 |

### VTEP Loopback VXLAN Tunnel Source Interfaces (VTEPs Only)

| VTEP Loopback Pool | Available Addresses | Assigned addresses | Assigned Address % |
| ------------------ | ------------------- | ------------------ | ------------------ |
| 2.2.1.0/24 | 256 | 8 | 3.13 % |
| 2.2.2.0/24 | 256 | 8 | 3.13 % |
| 2.2.3.0/24 | 256 | 8 | 3.13 % |
| 2.2.4.0/24 | 256 | 8 | 3.13 % |

### VTEP Loopback Node allocation

| POD | Node | Loopback1 |
| --- | ---- | --------- |
| pod-a | A-LEAF1 | 2.2.1.1/32 |
| pod-a | A-LEAF2 | 2.2.1.1/32 |
| pod-a | A-LEAF3 | 2.2.1.3/32 |
| pod-a | A-LEAF4 | 2.2.1.3/32 |
| pod-a | A-LEAF5 | 2.2.1.5/32 |
| pod-a | A-LEAF6 | 2.2.1.5/32 |
| pod-a | A-LEAF7 | 2.2.1.7/32 |
| pod-a | A-LEAF8 | 2.2.1.7/32 |
| pod-b | B-LEAF1 | 2.2.2.1/32 |
| pod-b | B-LEAF2 | 2.2.2.2/32 |
| pod-b | B-LEAF3 | 2.2.2.3/32 |
| pod-b | B-LEAF4 | 2.2.2.4/32 |
| pod-b | B-LEAF5 | 2.2.2.5/32 |
| pod-b | B-LEAF6 | 2.2.2.6/32 |
| pod-b | B-LEAF7 | 2.2.2.7/32 |
| pod-b | B-LEAF8 | 2.2.2.8/32 |
| pod-c | C-LEAF1 | 2.2.3.1/32 |
| pod-c | C-LEAF2 | 2.2.3.1/32 |
| pod-c | C-LEAF3 | 2.2.3.3/32 |
| pod-c | C-LEAF4 | 2.2.3.3/32 |
| pod-c | C-LEAF5 | 2.2.3.5/32 |
| pod-c | C-LEAF6 | 2.2.3.5/32 |
| pod-c | C-LEAF7 | 2.2.3.7/32 |
| pod-c | C-LEAF8 | 2.2.3.7/32 |
| pod-d | D-LEAF1 | 2.2.4.1/32 |
| pod-d | D-LEAF2 | 2.2.4.1/32 |
| pod-d | D-LEAF3 | 2.2.4.3/32 |
| pod-d | D-LEAF4 | 2.2.4.3/32 |
| pod-d | D-LEAF5 | 2.2.4.5/32 |
| pod-d | D-LEAF6 | 2.2.4.5/32 |
| pod-d | D-LEAF7 | 2.2.4.7/32 |
| pod-d | D-LEAF8 | 2.2.4.8/32 |
