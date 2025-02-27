# D-SPINE1

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
- [MAC Address Table](#mac-address-table)
  - [MAC Address Table Summary](#mac-address-table-summary)
  - [MAC Address Table Device Configuration](#mac-address-table-device-configuration)
- [Interfaces](#interfaces)
  - [Switchport Default](#switchport-default)
  - [Ethernet Interfaces](#ethernet-interfaces)
  - [Loopback Interfaces](#loopback-interfaces)
- [Routing](#routing)
  - [Service Routing Protocols Model](#service-routing-protocols-model)
  - [IP Routing](#ip-routing)
  - [IPv6 Routing](#ipv6-routing)
  - [ARP](#arp)
  - [Router BGP](#router-bgp)
- [BFD](#bfd)
  - [Router BFD](#router-bfd)
- [Filters](#filters)
  - [Peer Filters](#peer-filters)
  - [Prefix-lists](#prefix-lists)
  - [IPv6 Prefix-lists](#ipv6-prefix-lists)
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
| Management1 | OOB_MANAGEMENT | oob | default | 192.168.0.21/24 | - |

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
   ip address 192.168.0.21/24
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

STP mode: **none**

### Spanning Tree Device Configuration

```eos
!
spanning-tree mode none
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

## MAC Address Table

### MAC Address Table Summary

- MAC address table entry maximum age: 1800 seconds

### MAC Address Table Device Configuration

```eos
!
mac address-table aging-time 1800
```

## Interfaces

### Switchport Default

#### Switchport Defaults Summary

- Default Switchport Mode: routed

#### Switchport Default Device Configuration

```eos
!
switchport default mode routed
```

### Ethernet Interfaces

#### Ethernet Interfaces Summary

##### L2

| Interface | Description | Mode | VLANs | Native VLAN | Trunk Group | Channel-Group |
| --------- | ----------- | ---- | ----- | ----------- | ----------- | ------------- |

*Inherited from Port-Channel Interface

##### IPv4

| Interface | Description | Channel Group | IP Address | VRF |  MTU | Shutdown | ACL In | ACL Out |
| --------- | ----------- | ------------- | ---------- | ----| ---- | -------- | ------ | ------- |
| Ethernet7 | P2P_D-LEAF7_Ethernet1 | - | 192.168.1.48/31 | default | 9214 | False | - | - |
| Ethernet8 | P2P_D-LEAF8_Ethernet1 | - | 192.168.1.56/31 | default | 9214 | False | - | - |

##### IPv6

| Interface | Description | Channel Group | IPv6 Address | VRF | MTU | Shutdown | ND RA Disabled | Managed Config Flag | IPv6 ACL In | IPv6 ACL Out |
| --------- | ----------- | --------------| ------------ | --- | --- | -------- | -------------- | -------------------| ----------- | ------------ |
| Ethernet1 | P2P_D-LEAF1_Ethernet1 | - | - | default | 9214 | False | - | - | - | - |
| Ethernet2 | P2P_D-LEAF2_Ethernet1 | - | - | default | 9214 | False | - | - | - | - |
| Ethernet3 | P2P_D-LEAF3_Ethernet1 | - | - | default | 9214 | False | - | - | - | - |
| Ethernet4 | P2P_D-LEAF4_Ethernet1 | - | - | default | 9214 | False | - | - | - | - |
| Ethernet5 | P2P_D-LEAF5_Ethernet1 | - | - | default | 9214 | False | - | - | - | - |
| Ethernet6 | P2P_D-LEAF6_Ethernet1 | - | - | default | 9214 | False | - | - | - | - |

#### Ethernet Interfaces Device Configuration

```eos
!
interface Ethernet1
   description P2P_D-LEAF1_Ethernet1
   no shutdown
   mtu 9214
   no switchport
   ipv6 enable
!
interface Ethernet2
   description P2P_D-LEAF2_Ethernet1
   no shutdown
   mtu 9214
   no switchport
   ipv6 enable
!
interface Ethernet3
   description P2P_D-LEAF3_Ethernet1
   no shutdown
   mtu 9214
   no switchport
   ipv6 enable
!
interface Ethernet4
   description P2P_D-LEAF4_Ethernet1
   no shutdown
   mtu 9214
   no switchport
   ipv6 enable
!
interface Ethernet5
   description P2P_D-LEAF5_Ethernet1
   no shutdown
   mtu 9214
   no switchport
   ipv6 enable
!
interface Ethernet6
   description P2P_D-LEAF6_Ethernet1
   no shutdown
   mtu 9214
   no switchport
   ipv6 enable
!
interface Ethernet7
   description P2P_D-LEAF7_Ethernet1
   no shutdown
   mtu 9214
   no switchport
   ip address 192.168.1.48/31
!
interface Ethernet8
   description P2P_D-LEAF8_Ethernet1
   no shutdown
   mtu 9214
   no switchport
   ip address 192.168.1.56/31
```

### Loopback Interfaces

#### Loopback Interfaces Summary

##### IPv4

| Interface | Description | VRF | IP Address |
| --------- | ----------- | --- | ---------- |
| Loopback0 | ROUTER_ID | default | 1.1.4.201/32 |

##### IPv6

| Interface | Description | VRF | IPv6 Address |
| --------- | ----------- | --- | ------------ |
| Loopback0 | ROUTER_ID | default | 2001:db8:d:1::c9/128 |

#### Loopback Interfaces Device Configuration

```eos
!
interface Loopback0
   description ROUTER_ID
   no shutdown
   ip address 1.1.4.201/32
   ipv6 address 2001:db8:d:1::c9/128
```

## Routing

### Service Routing Protocols Model

Multi agent routing protocol model enabled

```eos
!
service routing protocols model multi-agent
```

### IP Routing

#### IP Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | True (ipv6 interfaces) |

#### IP Routing Device Configuration

```eos
!
ip routing ipv6 interfaces
```

### IPv6 Routing

#### IPv6 Routing Summary

| VRF | Routing Enabled |
| --- | --------------- |
| default | True |
| default | false |

#### IPv6 Routing Device Configuration

```eos
!
ipv6 unicast-routing
```

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
| 65400 | 1.1.4.201 |

| BGP Tuning |
| ---------- |
| graceful-restart restart-time 300 |
| graceful-restart |
| no bgp default ipv4-unicast |
| distance bgp 20 200 200 |
| maximum-paths 4 ecmp 4 |

#### Router BGP Peer Groups

##### EVPN-OVERLAY-PEERS

| Settings | Value |
| -------- | ----- |
| Address Family | evpn |
| Next-hop unchanged | True |
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
| 1.1.4.7 | 65478 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 1.1.4.8 | 65478 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 2001:db8:d:1::1 | 65412 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 2001:db8:d:1::2 | 65412 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 2001:db8:d:1::3 | 65434 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 2001:db8:d:1::4 | 65434 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 2001:db8:d:1::5 | 65456 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |
| 2001:db8:d:1::6 | 65456 | default | - | Inherited from peer group EVPN-OVERLAY-PEERS | Inherited from peer group EVPN-OVERLAY-PEERS | - | Inherited from peer group EVPN-OVERLAY-PEERS | - | - | - | - |

#### BGP Neighbor Interfaces

| Neighbor Interface | VRF | Peer Group | Remote AS | Peer Filter |
| ------------------ | --- | ---------- | --------- | ----------- |
| Ethernet1 | default | LOCAL-UNDERLAY-PEERS | 65412 | - |
| Ethernet2 | default | LOCAL-UNDERLAY-PEERS | 65412 | - |
| Ethernet3 | default | LOCAL-UNDERLAY-PEERS | 65434 | - |
| Ethernet4 | default | LOCAL-UNDERLAY-PEERS | 65434 | - |
| Ethernet5 | default | LOCAL-UNDERLAY-PEERS | 65456 | - |
| Ethernet6 | default | LOCAL-UNDERLAY-PEERS | 65456 | - |
| Ethernet7 | default | LOCAL-UNDERLAY-PEERS | 65478 | - |
| Ethernet8 | default | LOCAL-UNDERLAY-PEERS | 65478 | - |

#### Router BGP EVPN Address Family

##### EVPN Peer Groups

| Peer Group | Activate | Route-map In | Route-map Out | Encapsulation |
| ---------- | -------- | ------------ | ------------- | ------------- |
| EVPN-OVERLAY-PEERS | True |  - | - | default |

#### Router BGP Device Configuration

```eos
!
router bgp 65400
   router-id 1.1.4.201
   no bgp default ipv4-unicast
   distance bgp 20 200 200
   graceful-restart restart-time 300
   graceful-restart
   maximum-paths 4 ecmp 4
   neighbor EVPN-OVERLAY-PEERS peer group
   neighbor EVPN-OVERLAY-PEERS next-hop-unchanged
   neighbor EVPN-OVERLAY-PEERS update-source Loopback0
   neighbor EVPN-OVERLAY-PEERS bfd
   neighbor EVPN-OVERLAY-PEERS ebgp-multihop 3
   neighbor EVPN-OVERLAY-PEERS send-community
   neighbor EVPN-OVERLAY-PEERS maximum-routes 0
   neighbor LOCAL-UNDERLAY-PEERS peer group
   neighbor LOCAL-UNDERLAY-PEERS send-community
   neighbor LOCAL-UNDERLAY-PEERS maximum-routes 12000
   neighbor 1.1.4.7 peer group EVPN-OVERLAY-PEERS
   neighbor 1.1.4.7 remote-as 65478
   neighbor 1.1.4.7 description D-LEAF7_Loopback0
   neighbor 1.1.4.8 peer group EVPN-OVERLAY-PEERS
   neighbor 1.1.4.8 remote-as 65478
   neighbor 1.1.4.8 description D-LEAF8_Loopback0
   neighbor 2001:db8:d:1::1 peer group EVPN-OVERLAY-PEERS
   neighbor 2001:db8:d:1::1 remote-as 65412
   neighbor 2001:db8:d:1::1 description D-LEAF1_Loopback0
   neighbor 2001:db8:d:1::2 peer group EVPN-OVERLAY-PEERS
   neighbor 2001:db8:d:1::2 remote-as 65412
   neighbor 2001:db8:d:1::2 description D-LEAF2_Loopback0
   neighbor 2001:db8:d:1::3 peer group EVPN-OVERLAY-PEERS
   neighbor 2001:db8:d:1::3 remote-as 65434
   neighbor 2001:db8:d:1::3 description D-LEAF3_Loopback0
   neighbor 2001:db8:d:1::4 peer group EVPN-OVERLAY-PEERS
   neighbor 2001:db8:d:1::4 remote-as 65434
   neighbor 2001:db8:d:1::4 description D-LEAF4_Loopback0
   neighbor 2001:db8:d:1::5 peer group EVPN-OVERLAY-PEERS
   neighbor 2001:db8:d:1::5 remote-as 65456
   neighbor 2001:db8:d:1::5 description D-LEAF5_Loopback0
   neighbor 2001:db8:d:1::6 peer group EVPN-OVERLAY-PEERS
   neighbor 2001:db8:d:1::6 remote-as 65456
   neighbor 2001:db8:d:1::6 description D-LEAF6_Loopback0
   redistribute connected route-map RM-CONN-2-BGP
   neighbor interface Ethernet1 peer-group LOCAL-UNDERLAY-PEERS remote-as 65412
   neighbor interface Ethernet2 peer-group LOCAL-UNDERLAY-PEERS remote-as 65412
   neighbor interface Ethernet3 peer-group LOCAL-UNDERLAY-PEERS remote-as 65434
   neighbor interface Ethernet4 peer-group LOCAL-UNDERLAY-PEERS remote-as 65434
   neighbor interface Ethernet5 peer-group LOCAL-UNDERLAY-PEERS remote-as 65456
   neighbor interface Ethernet6 peer-group LOCAL-UNDERLAY-PEERS remote-as 65456
   neighbor interface Ethernet7 peer-group LOCAL-UNDERLAY-PEERS remote-as 65478
   neighbor interface Ethernet8 peer-group LOCAL-UNDERLAY-PEERS remote-as 65478
   !
   address-family evpn
      neighbor EVPN-OVERLAY-PEERS activate
   !
   address-family ipv4
      no neighbor EVPN-OVERLAY-PEERS activate
      neighbor LOCAL-UNDERLAY-PEERS activate
      neighbor LOCAL-UNDERLAY-PEERS next-hop address-family ipv6 originate
   !
   address-family ipv6
      neighbor LOCAL-UNDERLAY-PEERS activate
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

## Filters

### Peer Filters

#### Peer Filters Summary

##### LEAF-AS-RANGE

| Sequence | Match |
| -------- | ----- |
| 10 | as-range 65401-65499 result accept |

#### Peer Filters Device Configuration

```eos
!
peer-filter LEAF-AS-RANGE
   10 match as-range 65401-65499 result accept
```

### Prefix-lists

#### Prefix-lists Summary

##### PL-LOOPBACKS-EVPN-OVERLAY

| Sequence | Action |
| -------- | ------ |
| 10 | permit 1.1.4.0/24 eq 32 |

#### Prefix-lists Device Configuration

```eos
!
ip prefix-list PL-LOOPBACKS-EVPN-OVERLAY
   seq 10 permit 1.1.4.0/24 eq 32
```

### IPv6 Prefix-lists

#### IPv6 Prefix-lists Summary

##### PL-LOOPBACKS-EVPN-OVERLAY-V6

| Sequence | Action |
| -------- | ------ |
| 10 | permit 2001:db8:d:1::0/64 eq 128 |

#### IPv6 Prefix-lists Device Configuration

```eos
!
ipv6 prefix-list PL-LOOPBACKS-EVPN-OVERLAY-V6
   seq 10 permit 2001:db8:d:1::0/64 eq 128
```

### Route-maps

#### Route-maps Summary

##### RM-CONN-2-BGP

| Sequence | Type | Match | Set | Sub-Route-Map | Continue |
| -------- | ---- | ----- | --- | ------------- | -------- |
| 10 | permit | ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY | - | - | - |
| 30 | permit | ipv6 address prefix-list PL-LOOPBACKS-EVPN-OVERLAY-V6 | - | - | - |

#### Route-maps Device Configuration

```eos
!
route-map RM-CONN-2-BGP permit 10
   match ip address prefix-list PL-LOOPBACKS-EVPN-OVERLAY
!
route-map RM-CONN-2-BGP permit 30
   match ipv6 address prefix-list PL-LOOPBACKS-EVPN-OVERLAY-V6
```

## VRF Instances

### VRF Instances Summary

| VRF Name | IP Routing |
| -------- | ---------- |

### VRF Instances Device Configuration

```eos
```
