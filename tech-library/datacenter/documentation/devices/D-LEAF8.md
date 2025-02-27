# D-LEAF8

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
  - [Router BGP](#router-bgp)
- [BFD](#bfd)
  - [Router BFD](#router-bfd)
- [Multicast](#multicast)
  - [IP IGMP Snooping](#ip-igmp-snooping)
- [Filters](#filters)
  - [Prefix-lists](#prefix-lists)
  - [Route-maps](#route-maps)
- [VRF Instances](#vrf-instances)
  - [VRF Instances Summary](#vrf-instances-summary)
  - [VRF Instances Device Configuration](#vrf-instances-device-configuration)

## Management

### Management Interfaces

#### Management Interfaces Summary

##### IPv4

| Management Interface | Description | Type | VRF | IP Address | Gateway |
| -------------------- | ----------- | ---- | --- | ---------- | ------- |
| Management1 | OOB_MANAGEMENT | oob | default | 192.168.0.136/24 | - |

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
   ip address 192.168.0.136/24
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
| 50 | Yellow | - |
| 70 | Brown | - |
| 90 | Pink | - |

### VLANs Device Configuration

```eos
!
vlan 10
   name Blue
!
vlan 50
   name Yellow
!
vlan 70
   name Brown
!
vlan 90
   name Pink
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

##### IPv4

| Interface | Description | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet1 | P2P_D-SPINE1_Ethernet8 | - | 192.168.1.57/31 | default | 9214 | False | - | - |
| Ethernet2 | P2P_D-SPINE2_Ethernet8 | - | 192.168.1.59/31 | default | 9214 | False | - | - |
| Ethernet3 | P2P_D-SPINE3_Ethernet8 | - | 192.168.1.61/31 | default | 9214 | False | - | - |
| Ethernet4 | P2P_D-SPINE4_Ethernet8 | - | 192.168.1.63/31 | default | 9214 | False | - | - |
| Ethernet7 | P2P_BB1_Ethernet8 | - | 172.16.4.4/31 | default | 9214 | False | - | - |
| Ethernet8 | P2P_BB2_Ethernet8 | - | 172.16.4.6/31 | default | 9214 | False | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_D-SPINE1_Ethernet8
   no shutdown
   mtu 9214
   no switchport
   ip address 192.168.1.57/31
!
interface Ethernet2
   description P2P_D-SPINE2_Ethernet8
   no shutdown
   mtu 9214
   no switchport
   ip address 192.168.1.59/31
!
interface Ethernet3
   description P2P_D-SPINE3_Ethernet8
   no shutdown
   mtu 9214
   no switchport
   ip address 192.168.1.61/31
!
interface Ethernet4
   description P2P_D-SPINE4_Ethernet8
   no shutdown
   mtu 9214
   no switchport
   ip address 192.168.1.63/31
!
interface Ethernet7
   description P2P_BB1_Ethernet8
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.4.4/31
!
interface Ethernet8
   description P2P_BB2_Ethernet8
   no shutdown
   mtu 9214
   no switchport
   ip address 172.16.4.6/31
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | ROUTER_ID | default | 1.1.4.8/32 |
| Loopback1 | VXLAN_TUNNEL_SOURCE | default | 2.2.4.8/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | ROUTER_ID | default | - |
| Loopback1 | VXLAN_TUNNEL_SOURCE | default | - |

#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description ROUTER_ID
   no shutdown
   ip address 1.1.4.8/32
!
interface Loopback1
   description VXLAN_TUNNEL_SOURCE
   no shutdown
   ip address 2.2.4.8/32
```

### VLAN Interfaces

#### VLAN Interfaces Summary

| Interface | Description | VRF |  MTU | Shutdown |
| --------- | ----------- | --- | ---- | -------- |
| Vlan10 | Blue | Prod | 9014 | False |
| Vlan50 | Yellow | Dev | 9014 | False |
| Vlan70 | Brown | Dev | 9014 | False |
| Vlan90 | Pink | Dev | 9014 | False |

##### IPv4

| Interface | VRF | IP Address | IP Address Virtual | IP Router Virtual Address | ACL In | ACL Out |
| --------- | --- | ---------- | ------------------ | ------------------------- | ------ | ------- |
| Vlan10 |  Prod  |  -  |  10.10.10.1/24  |  -  |  -  |  -  |
| Vlan50 |  Dev  |  -  |  10.50.50.1/24  |  -  |  -  |  -  |
| Vlan70 |  Dev  |  -  |  10.70.70.1/24  |  -  |  -  |  -  |
| Vlan90 |  Dev  |  -  |  10.90.90.1/24  |  -  |  -  |  -  |

##### IPv6

| Interface | VRF | IPv6 Address | IPv6 Virtual Addresses | Virtual Router Addresses | ND RA Disabled | Managed Config Flag | Other Config Flag | IPv6 ACL In | IPv6 ACL Out |
| --------- | --- | ------------ | ---------------------- | ------------------------ | -------------- | ------------------- | ----------------- | ----------- | ------------ |
| Vlan10 | Prod | - | 2001:db8:10:10::1/64 | - | - | - | - | - | - |
| Vlan50 | Dev | - | 2001:db8:50:50::1/64 | - | - | - | - | - | - |
| Vlan70 | Dev | - | 2001:db8:70:70::1/64 | - | - | - | - | - | - |
| Vlan90 | Dev | - | 2001:db8:90:90::1/64 | - | - | - | - | - | - |

#### VLAN Interfaces Device Configuration

```eos
!
interface Vlan10
   description Blue
   no shutdown
   mtu 9014
   vrf Prod
   ipv6 enable
   ip address virtual 10.10.10.1/24
   ipv6 address virtual 2001:db8:10:10::1/64
!
interface Vlan50
   description Yellow
   no shutdown
   mtu 9014
   vrf Dev
   ipv6 enable
   ip address virtual 10.50.50.1/24
   ipv6 address virtual 2001:db8:50:50::1/64
!
interface Vlan70
   description Brown
   no shutdown
   mtu 9014
   vrf Dev
   ipv6 enable
   ip address virtual 10.70.70.1/24
   ipv6 address virtual 2001:db8:70:70::1/64
!
interface Vlan90
   description Pink
   no shutdown
   mtu 9014
   vrf Dev
   ipv6 enable
   ip address virtual 10.90.90.1/24
   ipv6 address virtual 2001:db8:90:90::1/64
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
| 50 | 10050 | - | - |
| 70 | 10070 | - | - |
| 90 | 10090 | - | - |

##### VRF to VNI and Multicast Group Mappings

| VRF | VNI | Multicast Group |
| ---- | --- | --------------- |
| Dev | 50002 | - |
| Prod | 50001 | - |

#### VXLAN Interface Device Configuration

```eos
!
interface Vxlan1
   description D-LEAF8_VTEP
   vxlan source-interface Loopback1
   vxlan udp-port 4789
   vxlan vlan 10 vni 10010
   vxlan vlan 50 vni 10050
   vxlan vlan 70 vni 10070
   vxlan vlan 90 vni 10090
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
| Dev | true |
| Prod | true |

### ARP

Global ARP timeout: 1500

#### ARP Device Configuration

```eos
!
arp aging timeout default 1500
```

### Router BGP

ASN Notation: asplain

#### Router BGP Summary

| BGP AS | Router ID |
| ------ | --------- |
| 65478 | 1.1.4.8 |

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
| Address Family | evpn |
| Local AS | 65500 |
| Source | Loopback0 |
| Ebgp multihop | 15 |
| Send community | all |
| Maximum routes | 0 (no limit) |

##### EVPN-OVERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | evpn |
| Source | Loopback0 |
| BFD | True |
| Ebgp multihop | 3 |
| Send community | all |
| Maximum routes | 0 (no limit) |

##### LOCAL-UNDERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | ipv4 |
| Send community | all |
| Maximum routes | 12000 |

#### BGP Neighbors

| Neighbor | Remote AS | VRF | Shutdown | Send-community | Maximum-routes | Allowas-in | BFD | RIB Pre-Policy Retain | Route-Reflector Client | Passive | TTL Max Hops |
| -------- | --------- | --- | -------- | -------------- | -------------- | ---------- | --- | --------------------- | ---------------------- | ------- | ------------ |
| 1.1.0.1 | 65500 | default | - | Inherited from peer group EVPN-OVERLAY-CORE | Inherited from peer group EVPN-OVERLAY-CORE | - | - | - | - | - | - |
| 1.1.0.2 | 65500 | default | - | Inherited from peer group EVPN-OVERLAY-CORE | Inherited from peer group EVPN-OVERLAY-CORE | - | - | - | - | - | - |
| 172.16.4.5 | 65500 | default | - | Inherited from peer group LOCAL-UNDERLAY-PEERS | Inherited from peer group LOCAL-UNDERLAY-PEERS | - | - | - | - | - | - |
| 172.16.4.7 | 65500 | default | - | Inherited from peer group LOCAL-UNDERLAY-PEERS | Inherited from peer group LOCAL-UNDERLAY-PEERS | - | - | - | - | - | - |
| 192.168.1.56 | 65400 | default | - | Inherited from peer group LOCAL-UNDERLAY-PEERS | Inherited from peer group LOCAL-UNDERLAY-PEERS | - | - | - | - | - | - |
| 192.168.1.58 | 65400 | default | - | Inherited from peer group LOCAL-UNDERLAY-PEERS | Inherited from peer group LOCAL-UNDERLAY-PEERS | - | - | - | - | - | - |
| 192.168.1.60 | 65400 | default | - | Inherited from peer group LOCAL-UNDERLAY-PEERS | Inherited from peer group LOCAL-UNDERLAY-PEERS | - | - | - | - | - | - |
| 192.168.1.62 | 65400 | default | - | Inherited from peer group LOCAL-UNDERLAY-PEERS | Inherited from peer group LOCAL-UNDERLAY-PEERS | - | - | - | - | - | - |
| 2001:db8:d:1::c9 | 65400 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 2001:db8:d:1::ca | 65400 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 2001:db8:d:1::cb | 65400 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 2001:db8:d:1::cc | 65400 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |

#### Router BGP EVPN Address Family

- VPN import pruning is **enabled**

##### EVPN Peer Groups

| Peer Group | Activate | Route-map In | Route-map Out | Encapsulation |
| ---------- | -------- | ------------ | ------------- | ------------- |
| EVPN-OVERLAY-CORE | True |  - | - | default |
| EVPN-OVERLAY-PEERS | True |  - | - | default |

##### EVPN DCI Gateway Summary

| Settings | Value |
| -------- | ----- |
| Remote Domain Peer Groups | EVPN-OVERLAY-CORE |
| L3 Gateway Configured | True |
| L3 Gateway Inter-domain | True |

#### Router BGP VLANs

| VLAN | Route-Distinguisher | Both Route-Target | Import Route Target | Export Route-Target | Redistribute |
| ---- | ------------------- | ----------------- | ------------------- | ------------------- | ------------ |
| 10 | 1.1.4.8:10010 | 10010:10010<br>remote 10010:10010 | - | - | learned |
| 50 | 1.1.4.8:10050 | 10050:10050<br>remote 10050:10050 | - | - | learned |
| 70 | 1.1.4.8:10070 | 10070:10070<br>remote 10070:10070 | - | - | learned |
| 90 | 1.1.4.8:10090 | 10090:10090<br>remote 10090:10090 | - | - | learned |

#### Router BGP VRFs

| VRF | Route-Distinguisher | Redistribute |
| --- | ------------------- | ------------ |
| Dev | 1.1.4.8:50002 | connected |
| Prod | 1.1.4.8:50001 | connected |

#### Router BGP Device Configuration

```eos
!
router bgp 65478
   router-id 1.1.4.8
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   graceful-restart restart-time 300
   graceful-restart
   maximum-paths 4 ecmp 4
   neighbor EVPN-OVERLAY-CORE peer group
   neighbor EVPN-OVERLAY-CORE local-as 65500 no-prepend replace-as
   neighbor EVPN-OVERLAY-CORE update-source Loopback0
   neighbor EVPN-OVERLAY-CORE ebgp-multihop 15
   neighbor EVPN-OVERLAY-CORE send-community
   neighbor EVPN-OVERLAY-CORE maximum-routes 0
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-PEERS bfd
   neighbor EVPN-OVERLAY-PEERS ebgp-multihop 3
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor LOCAL-UNDERLAY-PEERS peer group
   neighbor LOCAL-UNDERLAY-PEERS send-community
   neighbor LOCAL-UNDERLAY-PEERS maximum-routes 12000
   neighbor 1.1.0.1 peer group EVPN-OVERLAY-CORE
   neighbor 1.1.0.1 remote-as 65500
   neighbor 1.1.0.1 description BB1_Loopback0
   neighbor 1.1.0.2 peer group EVPN-OVERLAY-CORE
   neighbor 1.1.0.2 remote-as 65500
   neighbor 1.1.0.2 description BB2_Loopback0
   neighbor 172.16.4.5 peer group LOCAL-UNDERLAY-PEERS
   neighbor 172.16.4.5 remote-as 65500
   neighbor 172.16.4.5 description BB1
   neighbor 172.16.4.7 peer group LOCAL-UNDERLAY-PEERS
   neighbor 172.16.4.7 remote-as 65500
   neighbor 172.16.4.7 description BB2
   neighbor 192.168.1.56 peer group LOCAL-UNDERLAY-PEERS
   neighbor 192.168.1.56 remote-as 65400
   neighbor 192.168.1.56 description D-SPINE1_Ethernet8
   neighbor 192.168.1.58 peer group LOCAL-UNDERLAY-PEERS
   neighbor 192.168.1.58 remote-as 65400
   neighbor 192.168.1.58 description D-SPINE2_Ethernet8
   neighbor 192.168.1.60 peer group LOCAL-UNDERLAY-PEERS
   neighbor 192.168.1.60 remote-as 65400
   neighbor 192.168.1.60 description D-SPINE3_Ethernet8
   neighbor 192.168.1.62 peer group LOCAL-UNDERLAY-PEERS
   neighbor 192.168.1.62 remote-as 65400
   neighbor 192.168.1.62 description D-SPINE4_Ethernet8
   neighbor 2001:db8:d:1::c9 peer group EVPN-OVERLAY-PEERS
   neighbor 2001:db8:d:1::c9 remote-as 65400
   neighbor 2001:db8:d:1::c9 description D-SPINE1_Loopback0
   neighbor 2001:db8:d:1::ca peer group EVPN-OVERLAY-PEERS
   neighbor 2001:db8:d:1::ca remote-as 65400
   neighbor 2001:db8:d:1::ca description D-SPINE2_Loopback0
   neighbor 2001:db8:d:1::cb peer group EVPN-OVERLAY-PEERS
   neighbor 2001:db8:d:1::cb remote-as 65400
   neighbor 2001:db8:d:1::cb description D-SPINE3_Loopback0
   neighbor 2001:db8:d:1::cc peer group EVPN-OVERLAY-PEERS
   neighbor 2001:db8:d:1::cc remote-as 65400
   neighbor 2001:db8:d:1::cc description D-SPINE4_Loopback0
   redistribute connected route-map RM-CONN-2-BGP
   !
   vlan 10
      rd 1.1.4.8:10010
      rd evpn domain remote 1.1.4.8:10010
      route-target both 10010:10010
      route-target import export evpn domain remote 10010:10010
      redistribute learned
   !
   vlan 50
      rd 1.1.4.8:10050
      rd evpn domain remote 1.1.4.8:10050
      route-target both 10050:10050
      route-target import export evpn domain remote 10050:10050
      redistribute learned
   !
   vlan 70
      rd 1.1.4.8:10070
      rd evpn domain remote 1.1.4.8:10070
      route-target both 10070:10070
      route-target import export evpn domain remote 10070:10070
      redistribute learned
   !
   vlan 90
      rd 1.1.4.8:10090
      rd evpn domain remote 1.1.4.8:10090
      route-target both 10090:10090
      route-target import export evpn domain remote 10090:10090
      redistribute learned
   !
   address-family evpn
      neighbor EVPN-OVERLAY-CORE activate
      neighbor EVPN-OVERLAY-CORE domain remote
      neighbor EVPN-OVERLAY-PEERS activate
      route import match-failure action discard
      neighbor default next-hop-self received-evpn-routes route-type ip-prefix inter-domain
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-CORE activate
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor LOCAL-UNDERLAY-PEERS activate
   !
   vrf Dev
      rd 1.1.4.8:50002
      route-target import evpn 50002:50002
      route-target export evpn 50002:50002
      router-id 1.1.4.8
      redistribute connected
   !
   vrf Prod
      rd 1.1.4.8:50001
      route-target import evpn 50001:50001
      route-target export evpn 50001:50001
      router-id 1.1.4.8
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

### Prefix-lists

#### Prefix-lists Summary

##### PL-LOOPBACKS-EVPN-OVERLAY

| Sequence | Action |
| -------- | ------ |
| 10 | permit 1.1.4.0/24 eq 32 |
| 20 | permit 2.2.4.0/24 eq 32 |

#### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 1.1.4.0/24 eq 32
   seq 20 permit 2.2.4.0/24 eq 32
```

### Route-maps

#### Route-maps Summary

##### RM-CONN-2-BGP

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY | - | - | - |

#### Route-maps Device Configuration

```eos
!
route-map RM-CONN-2-BGP permit 10
   match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY
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
