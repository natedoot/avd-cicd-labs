# B-LEAF8

## Table of Contents

- [Management](#management)
  - [Management Interfaces](#management-interfaces)
  - [IP Name Servers](#ip-name-servers)
  - [NTP](#ntp)
  - [Management API HTTP](#management-api-http)
- [Authentication](#authentication)
  - [Local Users](#local-users)
  - [Enable Password](#enable-password)
  - [AAA Authorization](#aaa-authorization)
- [Monitoring](#monitoring)
  - [TerminAttr Daemon](#terminattr-daemon)
- [Monitor Connectivity](#monitor-connectivity)
  - [Global Configuration](#global-configuration)
  - [VRF Configuration](#vrf-configuration)
  - [Monitor Connectivity Device Configuration](#monitor-connectivity-device-configuration)
  - [Link Tracking](#link-tracking)
- [Spanning Tree](#spanning-tree)
  - [Spanning Tree Summary](#spanning-tree-summary)
  - [Spanning Tree Device Configuration](#spanning-tree-device-configuration)
- [Internal VLAN Allocation Policy](#internal-vlan-allocation-policy)
  - [Internal VLAN Allocation Policy Summary](#internal-vlan-allocation-policy-summary)
  - [Internal VLAN Allocation Policy Device Configuration](#internal-vlan-allocation-policy-device-configuration)
- [VLANs](#vlans)
  - [VLANs Summary](#vlans-summary)
  - [VLANs Device Configuration](#vlans-device-configuration)
- [MAC Address Table](#mac-address-table)
  - [MAC Address Table Summary](#mac-address-table-summary)
  - [MAC Address Table Device Configuration](#mac-address-table-device-configuration)
- [Interfaces](#interfaces)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
  - [VLAN Interfaces](#vlan-interfaces)
  - [VXLAN Interface](#vxlan-interface)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [Virtual Router MAC Address](#virtual-router-mac-address)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [ARP](#arp)
  - [Router ISIS](#router-isis)
  - [Router BGP](#router-bgp)
- [BFD](#bfd)
  - [Router BFD](#router-bfd)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
- [Filters](#filters)
  - [Community-lists](#community-lists)
  - [Prefix-lists](#prefix-lists)
  - [Route-maps](#route-maps)
  - [IP Extended Community Lists](#ip-extended-community-lists)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)
- [Virtual Source NAT](#virtual-source-nat)
  - [Virtual Source NAT Summary](#virtual-source-nat-summary)
  - [Virtual Source NAT Configuration](#virtual-source-nat-configuration)
- [EOS CLI Device Configuration](#eos-cli-device-configuration)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | OOB_MANAGEMENT | oob | default | 192.168.0.118/24 | - |

##### IPv6

| Management Interface | Description | Type | VRF | IPv6 Address | IPv6 Gateway |
| -------------------- | ----------- | ---- | --- | ------------ | ------------ |
| Management1 | OOB_MANAGEMENT | oob | default | - | - |

#### Management Interfaces Device Configuration

```eos
!
interface Management1
   description OOB_MANAGEMENT
   no shutdown
   ip address 192.168.0.118/24
```

### IP Name Servers

#### IP Name Servers Summary

| Name Server | VRF | Priority |
| ----------- | --- | -------- |
| 10.255.0.2 | default | - |

#### IP Name Servers Device Configuration

```eos
ip name-server vrf default 10.255.0.2
```

### NTP

#### NTP Summary

##### NTP Servers

| Server | VRF | Preferred | Burst | iBurst | Version | Min Poll | Max Poll | Local-interface | Key |
| ------ | --- | --------- | ----- | ------ | ------- | -------- | -------- | --------------- | --- |
| 0.pool.ntp.org | - | - | - | - | - | - | - | - | - |

#### NTP Device Configuration

```eos
!
ntp server 0.pool.ntp.org
```

### Management API HTTP

#### Management API HTTP Summary

| HTTP | HTTPS | Default Services |
| ---- | ----- | ---------------- |
| False | True | - |

#### Management API VRF Access

| VRF Name | IPv4 ACL | IPv6 ACL |
| -------- | -------- | -------- |
| default | - | - |

#### Management API HTTP Device Configuration

```eos
!
management api http-commands
   protocol https
   no shutdown
   !
   vrf default
      no shutdown
```

## Authentication

### Local Users

#### Local Users Summary

| User | Privilege | Role | Disabled | Shell |
| ---- | --------- | ---- | -------- | ----- |
| admin | 15 | network-admin | False | - |
| cvpadmin | 15 | network-admin | False | - |

#### Local Users Device Configuration

```eos
!
username admin privilege 15 role network-admin nopassword
username cvpadmin privilege 15 role network-admin secret sha512 <removed>
```

### Enable Password

Enable password has been disabled

### AAA Authorization

#### AAA Authorization Summary

| Type | User Stores |
| ---- | ----------- |
| Exec | local |

Authorization for configuration commands is disabled.

#### AAA Authorization Device Configuration

```eos
aaa authorization exec default local
!
```

## Monitoring

### TerminAttr Daemon

#### TerminAttr Daemon Summary

| CV Compression | CloudVision Servers | VRF | Authentication | Smash Excludes | Ingest Exclude | Bypass AAA |
| -------------- | ------------------- | --- | -------------- | -------------- | -------------- | ---------- |
| gzip | 192.168.0.5:9910 | default | token,/tmp/token | ale,flexCounter,hardware,kni,pulse,strata | /Sysdb/cell/1/agent,/Sysdb/cell/2/agent | True |

#### TerminAttr Daemon Device Configuration

```eos
!
daemon TerminAttr
   exec /usr/bin/TerminAttr -cvaddr=192.168.0.5:9910 -cvauth=token,/tmp/token -cvvrf=default -disableaaa -smashexcludes=ale,flexCounter,hardware,kni,pulse,strata -ingestexclude=/Sysdb/cell/1/agent,/Sysdb/cell/2/agent -taillogs
   no shutdown
```

## Monitor Connectivity

### Global Configuration

#### Probing Configuration

| Enabled | Interval | Default Interface Set | Address Only |
| ------- | -------- | --------------------- | ------------ |
| True | - | - | True |

### VRF Configuration

| Name | Description | Default Interface Set | Address Only |
| ---- | ----------- | --------------------- | ------------ |
| Dev | - | - | True |
| Prod | - | - | True |

#### Vrf Dev Configuration

##### Interface Sets

| Name | Interfaces |
| ---- | ---------- |
| Dev-Vtep-Diag | Loopback102 |

##### Host Parameters

| Host Name | Description | IPv4 Address | Probing Interface Set | Address Only | URL |
| --------- | ----------- | ------------ | --------------------- | ------------ | --- |
| A-LEAF7-DiagVtep-Dev | - | 10.102.101.7 | Dev-Vtep-Diag | True | - |
| C-LEAF7-DiagVtep-Dev | - | 10.102.103.7 | Dev-Vtep-Diag | True | - |

#### Vrf Prod Configuration

##### Interface Sets

| Name | Interfaces |
| ---- | ---------- |
| Prod-Vtep-Diag | Loopback101 |

##### Host Parameters

| Host Name | Description | IPv4 Address | Probing Interface Set | Address Only | URL |
| --------- | ----------- | ------------ | --------------------- | ------------ | --- |
| A-LEAF7-DiagVtep-Prod | - | 10.101.101.7 | Prod-Vtep-Diag | True | - |
| C-LEAF7-DiagVtep-Prod | - | 10.101.103.7 | Prod-Vtep-Diag | True | - |

### Monitor Connectivity Device Configuration

```eos
!
monitor connectivity
   vrf Dev
      interface set Dev-Vtep-Diag Loopback102
      !
      host A-LEAF7-DiagVtep-Dev
         local-interfaces Dev-Vtep-Diag address-only
         ip 10.102.101.7
      !
      host C-LEAF7-DiagVtep-Dev
         local-interfaces Dev-Vtep-Diag address-only
         ip 10.102.103.7
   !
   vrf Prod
      interface set Prod-Vtep-Diag Loopback101
      !
      host A-LEAF7-DiagVtep-Prod
         local-interfaces Prod-Vtep-Diag address-only
         ip 10.101.101.7
      !
      host C-LEAF7-DiagVtep-Prod
         local-interfaces Prod-Vtep-Diag address-only
         ip 10.101.103.7
   no shutdown
```

### Link Tracking

#### Link Tracking Groups Summary

| Group Name | Minimum Links | Recovery Delay |
| ---------- | ------------- | -------------- |
| CORE-LINKS | - | 300 |

#### Link Tracking Groups Device Configuration

```eos
!
link tracking group CORE-LINKS
   recovery delay 300
```

## Spanning Tree

### Spanning Tree Summary

STP mode: **mstp**

#### MSTP Instance and Priority

| Instance(s) | Priority |
| -------- | -------- |
| 0 | 0 |

#### Global Spanning-Tree Settings

- Global BPDU Guard for Edge ports is enabled.

### Spanning Tree Device Configuration

```eos
!
spanning-tree mode mstp
spanning-tree edge-port bpduguard default
spanning-tree mst 0 priority 0
```

## Internal VLAN Allocation Policy

### Internal VLAN Allocation Policy Summary

| Policy Allocation | Range Beginning | Range Ending |
| ------------------| --------------- | ------------ |
| ascending | 1006 | 1199 |

### Internal VLAN Allocation Policy Device Configuration

```eos
!
vlan internal order ascending range 1006 1199
```

## VLANs

### VLANs Summary

| VLAN ID | Name | Trunk Groups |
| ------- | ---- | ------------ |
| 10 | Blue | - |
| 20 | Green | - |
| 30 | Orange | - |
| 40 | Purple | - |
| 50 | Yellow | - |
| 60 | Red | - |
| 70 | Brown | - |
| 80 | Black | - |

### VLANs Device Configuration

```eos
!
vlan 10
   name Blue
!
vlan 20
   name Green
!
vlan 30
   name Orange
!
vlan 40
   name Purple
!
vlan 50
   name Yellow
!
vlan 60
   name Red
!
vlan 70
   name Brown
!
vlan 80
   name Black
```

## MAC Address Table

### MAC Address Table Summary

- MAC address table entry maximum age: 1800 seconds

### MAC Address Table Device Configuration

```eos
!
mac address-table aging-time 1800
```

## Interfaces

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |

*Inherited from Port-Channel Interface

##### Link Tracking Groups

| Interface | Group Name | Direction |
| --------- | ---------- | --------- |
| Ethernet1 | CORE-LINKS | upstream |
| Ethernet2 | CORE-LINKS | upstream |
| Ethernet3 | CORE-LINKS | upstream |
| Ethernet4 | CORE-LINKS | upstream |

##### IPv4

| Interface | Description | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1 | P2P_B-SPINE1_Ethernet8 | - | 192.168.1.57/31 | default | 1500 | False | - | - |
| Ethernet2 | P2P_B-SPINE2_Ethernet8 | - | 192.168.1.59/31 | default | 1500 | False | - | - |
| Ethernet3 | P2P_B-SPINE3_Ethernet8 | - | 192.168.1.61/31 | default | 1500 | False | - | - |
| Ethernet4 | P2P_B-SPINE4_Ethernet8 | - | 192.168.1.63/31 | default | 1500 | False | - | - |
| Ethernet7 | P2P_BB1_Ethernet4 | - | 172.16.2.4/31 | default | 9214 | False | - | - |
| Ethernet8 | P2P_BB2_Ethernet4 | - | 172.16.2.6/31 | default | 9214 | False | - | - |

##### ISIS

| Interface | Channel Group | ISIS Instance | ISIS BFD | ISIS Metric | Mode | ISIS Circuit Type | Hello Padding | ISIS Authentication Mode |
| --------- | ------------- | ------------- | -------- | ----------- | ---- | ----------------- | ------------- | ------------------------ |
| Ethernet1 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet2 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet3 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet4 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | - | - |
| Ethernet7 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | True | - |
| Ethernet8 | - | EVPN_UNDERLAY | - | 50 | point-to-point | level-2 | True | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_B-SPINE1_Ethernet8
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.57/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
   link tracking group CORE-LINKS upstream
!
interface Ethernet2
   description P2P_B-SPINE2_Ethernet8
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.59/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
   link tracking group CORE-LINKS upstream
!
interface Ethernet3
   description P2P_B-SPINE3_Ethernet8
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.61/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
   link tracking group CORE-LINKS upstream
!
interface Ethernet4
   description P2P_B-SPINE4_Ethernet8
   no shutdown
   mtu 1500
   no switchport
   ip address 192.168.1.63/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis network point-to-point
   link tracking group CORE-LINKS upstream
!
interface Ethernet7
   description P2P_BB1_Ethernet4
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.2.4/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis hello padding
   isis network point-to-point
!
interface Ethernet8
   description P2P_BB2_Ethernet4
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.2.6/31
   isis enable EVPN_UNDERLAY
   isis circuit-type level-2
   isis metric 50
   isis hello padding
   isis network point-to-point
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | ROUTER_ID | default | 1.1.2.8/32 |
| Loopback1 | VXLAN_TUNNEL_SOURCE | default | 2.2.2.8/32 |
| Loopback101 | DIAG_VRF_Prod | Prod | 10.101.102.8/32 |
| Loopback102 | DIAG_VRF_Dev | Dev | 10.102.102.8/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | ROUTER_ID | default | - |
| Loopback1 | VXLAN_TUNNEL_SOURCE | default | - |
| Loopback101 | DIAG_VRF_Prod | Prod | - |
| Loopback102 | DIAG_VRF_Dev | Dev | - |

##### ISIS

| Interface | ISIS instance | ISIS metric | Interface mode |
| --------- | ------------- | ----------- | -------------- |
| Loopback0 | EVPN_UNDERLAY | - | passive |
| Loopback1 | EVPN_UNDERLAY | - | passive |

#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description ROUTER_ID
   no shutdown
   ip address 1.1.2.8/32
   isis enable EVPN_UNDERLAY
   isis passive
!
interface Loopback1
   description VXLAN_TUNNEL_SOURCE
   no shutdown
   ip address 2.2.2.8/32
   isis enable EVPN_UNDERLAY
   isis passive
!
interface Loopback101
   description DIAG_VRF_Prod
   no shutdown
   vrf Prod
   ip address 10.101.102.8/32
!
interface Loopback102
   description DIAG_VRF_Dev
   no shutdown
   vrf Dev
   ip address 10.102.102.8/32
```

### VLAN Interfaces

#### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan10 | Blue | Prod | 9014 | False |
| Vlan20 | Green | Prod | 9014 | False |
| Vlan30 | Orange | Prod | 9014 | False |
| Vlan40 | Purple | Prod | 9014 | False |
| Vlan50 | Yellow | Dev | 9014 | False |
| Vlan60 | Red | Dev | 9014 | False |
| Vlan70 | Brown | Dev | 9014 | False |
| Vlan80 | Black | Dev | 9014 | False |

##### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ------ | ------- |
| Vlan10 |  Prod  |  -  |  10.10.10.1/24  |  -  |  -  |  -  |
| Vlan20 |  Prod  |  -  |  10.20.20.1/24  |  -  |  -  |  -  |
| Vlan30 |  Prod  |  -  |  10.30.30.1/24  |  -  |  -  |  -  |
| Vlan40 |  Prod  |  -  |  10.40.40.1/24  |  -  |  -  |  -  |
| Vlan50 |  Dev  |  -  |  10.50.50.1/24  |  -  |  -  |  -  |
| Vlan60 |  Dev  |  -  |  10.60.60.1/24  |  -  |  -  |  -  |
| Vlan70 |  Dev  |  -  |  10.70.70.1/24  |  -  |  -  |  -  |
| Vlan80 |  Dev  |  -  |  10.80.80.1/24  |  -  |  -  |  -  |

#### VLAN Interfaces Device Configuration

```eos
!
interface Vlan10
   description Blue
   no shutdown
   mtu 9014
   vrf Prod
   ip address virtual 10.10.10.1/24
!
interface Vlan20
   description Green
   no shutdown
   mtu 9014
   vrf Prod
   ip address virtual 10.20.20.1/24
!
interface Vlan30
   description Orange
   no shutdown
   mtu 9014
   vrf Prod
   ip address virtual 10.30.30.1/24
!
interface Vlan40
   description Purple
   no shutdown
   mtu 9014
   vrf Prod
   ip address virtual 10.40.40.1/24
!
interface Vlan50
   description Yellow
   no shutdown
   mtu 9014
   vrf Dev
   ip address virtual 10.50.50.1/24
!
interface Vlan60
   description Red
   no shutdown
   mtu 9014
   vrf Dev
   ip address virtual 10.60.60.1/24
!
interface Vlan70
   description Brown
   no shutdown
   mtu 9014
   vrf Dev
   ip address virtual 10.70.70.1/24
!
interface Vlan80
   description Black
   no shutdown
   mtu 9014
   vrf Dev
   ip address virtual 10.80.80.1/24
```

### VXLAN Interface

#### VXLAN Interface Summary

| Setting | Value |
| ------- | ----- |
| Source Interface | Loopback1 |
| UDP port | 4789 |

##### VLAN to VNI, Flood List and Multicast Group Mappings

| VLAN | VNI | Flood List | Multicast Group |
| ---- | --- | ---------- | --------------- |
| 10 | 10010 | - | - |
| 20 | 10020 | - | - |
| 30 | 10030 | - | - |
| 40 | 10040 | - | - |
| 50 | 10050 | - | - |
| 60 | 10060 | - | - |
| 70 | 10070 | - | - |
| 80 | 10080 | - | - |

##### VRF to VNI and Multicast Group Mappings

| VRF | VNI | Multicast Group |
| ---- | --- | --------------- |
| Dev | 50002 | - |
| Prod | 50001 | - |

#### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   description B-LEAF8_VTEP
   vxlan source-interface Loopback1
   vxlan udp-port 4789
   vxlan vlan 10 vni 10010
   vxlan vlan 20 vni 10020
   vxlan vlan 30 vni 10030
   vxlan vlan 40 vni 10040
   vxlan vlan 50 vni 10050
   vxlan vlan 60 vni 10060
   vxlan vlan 70 vni 10070
   vxlan vlan 80 vni 10080
   vxlan vrf Dev vni 50002
   vxlan vrf Prod vni 50001
```

## Routing

### Service Routing Protocols Model

Multi agent routing protocol model enabled

```eos
!
service routing protocols model multi-agent
```

### Virtual Router MAC Address

#### Virtual Router MAC Address Summary

Virtual Router MAC Address: 00:1c:73:00:00:01

#### Virtual Router MAC Address Device Configuration

```eos
!
ip virtual-router mac-address 00:1c:73:00:00:01
```

### IP Routing

#### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | True |
| Dev | True |
| Prod | True |

#### IP Routing Device Configuration

```eos
!
ip routing
ip routing vrf Dev
ip routing vrf Prod
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | False |
| default | false |
| Dev | false |
| Prod | false |

### ARP

Global ARP timeout: 1500

#### ARP Device Configuration

```eos
!
arp aging timeout default 1500
```

### Router ISIS

#### Router ISIS Summary

| Settings | Value |
| -------- | ----- |
| Instance | EVPN_UNDERLAY |
| Net-ID | 49.1111.0010.0100.2008.00 |
| Type | level-2 |
| Router-ID | 1.1.2.8 |
| Log Adjacency Changes | True |

#### ISIS Interfaces Summary

| Interface | ISIS Instance | ISIS Metric | Interface Mode |
| --------- | ------------- | ----------- | -------------- |
| Ethernet1 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet2 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet3 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet4 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet7 | EVPN_UNDERLAY | 50 | point-to-point |
| Ethernet8 | EVPN_UNDERLAY | 50 | point-to-point |
| Loopback0 | EVPN_UNDERLAY | - | passive |
| Loopback1 | EVPN_UNDERLAY | - | passive |

#### ISIS IPv4 Address Family Summary

| Settings | Value |
| -------- | ----- |
| IPv4 Address-family Enabled | True |
| Maximum-paths | 4 |

#### Router ISIS Device Configuration

```eos
!
router isis EVPN_UNDERLAY
   net 49.1111.0010.0100.2008.00
   router-id ipv4 1.1.2.8
   is-type level-2
   log-adjacency-changes
   !
   address-family ipv4 unicast
      maximum-paths 4
   !
```

### Router BGP

ASN Notation: asplain

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65200 | 1.1.2.8 |

| BGP Tuning |
| ---------- |
| graceful-restart restart-time 300 |
| graceful-restart |
| no bgp default ipv4-unicast |
| distance bgp 20 200 200 |
| maximum-paths 4 ecmp 4 |

#### Router BGP Peer Groups

##### EVPN-OVERLAY-CORE

| Settings | Value |
| -------- | ----- |
| Remote AS | 65500 |
| Local AS | 65500 |
| Route Reflector Client | Yes |
| Source | Loopback0 |
| BFD | True |
| Ebgp multihop | 15 |
| Send community | all |

##### EVPN-OVERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | evpn |
| Remote AS | 65200 |
| Route Reflector Client | Yes |
| Source | Loopback0 |
| BFD | True |
| Send community | all |
| Maximum routes | 0 (no limit) |

##### IPv4-REMOTE-UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Remote AS | 65500 |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 1.1.0.1 | Inherited from peer group EVPN-OVERLAY-CORE | default | - | Inherited from peer group EVPN-OVERLAY-CORE | - | - | Inherited from peer group EVPN-OVERLAY-CORE | - | Inherited from peer group EVPN-OVERLAY-CORE | - | - |
| 1.1.0.2 | Inherited from peer group EVPN-OVERLAY-CORE | default | - | Inherited from peer group EVPN-OVERLAY-CORE | - | - | Inherited from peer group EVPN-OVERLAY-CORE | - | Inherited from peer group EVPN-OVERLAY-CORE | - | - |
| 1.1.2.201 | Inherited from peer group EVPN-OVERLAY-PEERS | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - |
| 1.1.2.202 | Inherited from peer group EVPN-OVERLAY-PEERS | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - |
| 1.1.2.203 | Inherited from peer group EVPN-OVERLAY-PEERS | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - |
| 1.1.2.204 | Inherited from peer group EVPN-OVERLAY-PEERS | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - |
| 172.16.2.5 | Inherited from peer group IPv4-REMOTE-UNDERLAY-PEERS | default | - | - | - | - | - | - | - | - | - |
| 172.16.2.7 | Inherited from peer group IPv4-REMOTE-UNDERLAY-PEERS | default | - | - | - | - | - | - | - | - | - |

#### Router BGP EVPN Address Family

- VPN import pruning is **enabled**

##### EVPN Peer Groups

| Peer Group | Activate | Route-map In | Route-map Out | Encapsulation |
| ---------- | -------- | ------------ | ------------- | ------------- |
| EVPN-OVERLAY-CORE | True |  - | - | default |
| EVPN-OVERLAY-PEERS | True |  RM-EVPN-SOO-IN | RM-EVPN-SOO-OUT | default |

##### EVPN DCI Gateway Summary

| Settings | Value |
| -------- | ----- |
| Remote Domain Peer Groups | EVPN-OVERLAY-CORE |

#### Router BGP VLANs

| VLAN | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute |
| ---- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ |
| 10 | 1.1.2.8:10010 | 10010:10010<br>remote 10010:10010 | - | - | learned |
| 20 | 1.1.2.8:10020 | 10020:10020<br>remote 10020:10020 | - | - | learned |
| 30 | 1.1.2.8:10030 | 10030:10030<br>remote 10030:10030 | - | - | learned |
| 40 | 1.1.2.8:10040 | 10040:10040<br>remote 10040:10040 | - | - | learned |
| 50 | 1.1.2.8:10050 | 10050:10050<br>remote 10050:10050 | - | - | learned |
| 60 | 1.1.2.8:10060 | 10060:10060<br>remote 10060:10060 | - | - | learned |
| 70 | 1.1.2.8:10070 | 10070:10070<br>remote 10070:10070 | - | - | learned |
| 80 | 1.1.2.8:10080 | 10080:10080<br>remote 10080:10080 | - | - | learned |

#### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| Dev | 1.1.2.8:50002 | connected |
| Prod | 1.1.2.8:50001 | connected |

#### Router BGP Device Configuration

```eos
!
router bgp 65200
   router-id 1.1.2.8
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   graceful-restart restart-time 300
   graceful-restart
   maximum-paths 4 ecmp 4
   neighbor EVPN-OVERLAY-CORE peer group
   neighbor EVPN-OVERLAY-CORE remote-as 65500
   neighbor EVPN-OVERLAY-CORE local-as 65500 no-prepend replace-as
   neighbor EVPN-OVERLAY-CORE update-source Loopback0
   neighbor EVPN-OVERLAY-CORE bfd
   neighbor EVPN-OVERLAY-CORE ebgp-multihop 15
   neighbor EVPN-OVERLAY-CORE route-reflector-client
   neighbor EVPN-OVERLAY-CORE route-map RM-AS65000-EVPN-IN in
   neighbor EVPN-OVERLAY-CORE route-map RM-AS65000-EVPN-OUT out
   neighbor EVPN-OVERLAY-CORE send-community
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS remote-as 65200
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-PEERS bfd
   neighbor EVPN-OVERLAY-PEERS route-reflector-client
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor IPv4-REMOTE-UNDERLAY-PEERS peer group
   neighbor IPv4-REMOTE-UNDERLAY-PEERS remote-as 65500
   neighbor IPv4-REMOTE-UNDERLAY-PEERS route-map RM-AS65000-IPV4-OUT out
   neighbor 1.1.0.1 peer group EVPN-OVERLAY-CORE
   neighbor 1.1.0.1 description BB1_OVERLAY
   neighbor 1.1.0.2 peer group EVPN-OVERLAY-CORE
   neighbor 1.1.0.2 description BB2_OVERLAY
   neighbor 1.1.2.201 peer group EVPN-OVERLAY-PEERS
   neighbor 1.1.2.201 description B-SPINE1_Loopback0
   neighbor 1.1.2.202 peer group EVPN-OVERLAY-PEERS
   neighbor 1.1.2.202 description B-SPINE2_Loopback0
   neighbor 1.1.2.203 peer group EVPN-OVERLAY-PEERS
   neighbor 1.1.2.203 description B-SPINE3_Loopback0
   neighbor 1.1.2.204 peer group EVPN-OVERLAY-PEERS
   neighbor 1.1.2.204 description B-SPINE4_Loopback0
   neighbor 172.16.2.5 peer group IPv4-REMOTE-UNDERLAY-PEERS
   neighbor 172.16.2.5 description BB1_UNDERLAY
   neighbor 172.16.2.7 peer group IPv4-REMOTE-UNDERLAY-PEERS
   neighbor 172.16.2.7 description BB2_UNDERLAY
   !
   vlan 10
      rd 1.1.2.8:10010
      rd evpn domain remote 1.1.2.8:10010
      route-target both 10010:10010
      route-target import export evpn domain remote 10010:10010
      redistribute learned
   !
   vlan 20
      rd 1.1.2.8:10020
      rd evpn domain remote 1.1.2.8:10020
      route-target both 10020:10020
      route-target import export evpn domain remote 10020:10020
      redistribute learned
   !
   vlan 30
      rd 1.1.2.8:10030
      rd evpn domain remote 1.1.2.8:10030
      route-target both 10030:10030
      route-target import export evpn domain remote 10030:10030
      redistribute learned
   !
   vlan 40
      rd 1.1.2.8:10040
      rd evpn domain remote 1.1.2.8:10040
      route-target both 10040:10040
      route-target import export evpn domain remote 10040:10040
      redistribute learned
   !
   vlan 50
      rd 1.1.2.8:10050
      rd evpn domain remote 1.1.2.8:10050
      route-target both 10050:10050
      route-target import export evpn domain remote 10050:10050
      redistribute learned
   !
   vlan 60
      rd 1.1.2.8:10060
      rd evpn domain remote 1.1.2.8:10060
      route-target both 10060:10060
      route-target import export evpn domain remote 10060:10060
      redistribute learned
   !
   vlan 70
      rd 1.1.2.8:10070
      rd evpn domain remote 1.1.2.8:10070
      route-target both 10070:10070
      route-target import export evpn domain remote 10070:10070
      redistribute learned
   !
   vlan 80
      rd 1.1.2.8:10080
      rd evpn domain remote 1.1.2.8:10080
      route-target both 10080:10080
      route-target import export evpn domain remote 10080:10080
      redistribute learned
   !
   address-family evpn
      neighbor EVPN-OVERLAY-CORE activate
      neighbor EVPN-OVERLAY-CORE domain remote
      neighbor EVPN-OVERLAY-PEERS activate
      neighbor EVPN-OVERLAY-PEERS route-map RM-EVPN-SOO-IN in
      neighbor EVPN-OVERLAY-PEERS route-map RM-EVPN-SOO-OUT out
      route import match-failure action discard
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-CORE activate
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor IPv4-REMOTE-UNDERLAY-PEERS activate
      network 1.1.2.7/32
      network 1.1.2.8/32
      network 2.2.2.8/32
   !
   vrf Dev
      rd 1.1.2.8:50002
      route-target import evpn 50002:50002
      route-target export evpn 50002:50002
      router-id 1.1.2.8
      redistribute connected
   !
   vrf Prod
      rd 1.1.2.8:50001
      route-target import evpn 50001:50001
      route-target export evpn 50001:50001
      router-id 1.1.2.8
      redistribute connected
```

## BFD

### Router BFD

#### Router BFD Multihop Summary

| Interval | Minimum RX | Multiplier |
| -------- | ---------- | ---------- |
| 300 | 300 | 3 |

#### Router BFD Device Configuration

```eos
!
router bfd
   multihop interval 300 min-rx 300 multiplier 3
```

## Multicast

### IP IGMP Snooping

#### IP IGMP Snooping Summary

| IGMP Snooping | Fast Leave | Interface Restart Query | Proxy | Restart Query Interval | Robustness Variable |
| ------------- | ---------- | ----------------------- | ----- | ---------------------- | ------------------- |
| Enabled | - | - | - | - | - |

#### IP IGMP Snooping Device Configuration

```eos
```

## Filters

### Community-lists

#### Community-lists Summary

| Name | Action |
| -------- | ------ |
| CL-LOCAL-DOMAIN-ORIGINATED | permit 65200:65200 |
| CL-REMOTE-DOMAIN-ORIGINATED | permit 65000:65000 |

#### Community-lists Device Configuration

```eos
!
ip community-list CL-LOCAL-DOMAIN-ORIGINATED permit 65200:65200
ip community-list CL-REMOTE-DOMAIN-ORIGINATED permit 65000:65000
```

### Prefix-lists

#### Prefix-lists Summary

##### PL-GATEWAY-LOOP

| Sequence | Action |
| -------- | ------ |
| 10 | permit 2.2.2.8/32 |
| 20 | permit 1.1.2.7/32 |
| 30 | permit 1.1.2.8/32 |

#### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-GATEWAY-LOOP
   seq 10 permit 2.2.2.8/32
   seq 20 permit 1.1.2.7/32
   seq 30 permit 1.1.2.8/32
```

### Route-maps

#### Route-maps Summary

##### RM-AS65000-EVPN-IN

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | - | community 65000:65000 additive | - | - |

##### RM-AS65000-EVPN-OUT

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 5 | deny | community CL-REMOTE-DOMAIN-ORIGINATED | - | - | - |
| 10 | permit | - | - | - | - |

##### RM-AS65000-IPV4-OUT

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | ip address prefix-list PL-GATEWAY-LOOP | - | - | - |

##### RM-AS65200-EVPN-IN

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | community CL-REMOTE-DOMAIN-ORIGINATED | local-preference 0 | - | - |
| 20 | permit | - | community 65200:65200 additive | - | - |

##### RM-AS65200-EVPN-OUT

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 5 | deny | community CL-LOCAL-DOMAIN-ORIGINATED | - | - | - |
| 10 | permit | - | - | - | - |

##### RM-EVPN-SOO-IN

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | deny | extcommunity ECL-EVPN-SOO | - | - | - |
| 20 | permit | - | - | - | - |

##### RM-EVPN-SOO-OUT

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | - | extcommunity soo 2.2.2.8:1 additive | - | - |

#### Route-maps Device Configuration

```eos
!
route-map RM-AS65000-EVPN-IN permit 10
   set community 65000:65000 additive
!
route-map RM-AS65000-EVPN-OUT deny 5
   match community CL-REMOTE-DOMAIN-ORIGINATED
!
route-map RM-AS65000-EVPN-OUT permit 10
!
route-map RM-AS65000-IPV4-OUT permit 10
   match ip address prefix-list PL-GATEWAY-LOOP
!
route-map RM-AS65200-EVPN-IN permit 10
   match community CL-REMOTE-DOMAIN-ORIGINATED
   set local-preference 0
!
route-map RM-AS65200-EVPN-IN permit 20
   set community 65200:65200 additive
!
route-map RM-AS65200-EVPN-OUT deny 5
   match community CL-LOCAL-DOMAIN-ORIGINATED
!
route-map RM-AS65200-EVPN-OUT permit 10
!
route-map RM-EVPN-SOO-IN deny 10
   match extcommunity ECL-EVPN-SOO
!
route-map RM-EVPN-SOO-IN permit 20
!
route-map RM-EVPN-SOO-OUT permit 10
   set extcommunity soo 2.2.2.8:1 additive
```

### IP Extended Community Lists

#### IP Extended Community Lists Summary

| List Name | Type | Extended Communities |
| --------- | ---- | -------------------- |
| ECL-EVPN-SOO | permit | soo 2.2.2.8:1 |

#### IP Extended Community Lists Device Configuration

```eos
!
ip extcommunity-list ECL-EVPN-SOO permit soo 2.2.2.8:1
```

## VRF Instances

### VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |
| Dev | enabled |
| Prod | enabled |

### VRF Instances Device Configuration

```eos
!
vrf instance Dev
!
vrf instance Prod
```

## Virtual Source NAT

### Virtual Source NAT Summary

| Source NAT VRF | Source NAT IPv4 Address | Source NAT IPv6 Address |
| -------------- | ----------------------- | ----------------------- |
| Dev | 10.102.102.8 | - |
| Prod | 10.101.102.8 | - |

### Virtual Source NAT Configuration

```eos
!
ip address virtual source-nat vrf Dev address 10.102.102.8
ip address virtual source-nat vrf Prod address 10.101.102.8
```

## EOS CLI Device Configuration

```eos
!
dhcp relay
  mlag peer-link requests disabled
agent KernelFib environment KERNELFIB_PROGRAM_ALL_ECMP='true'

```
