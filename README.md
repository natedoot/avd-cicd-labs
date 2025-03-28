# AVD Connected Endpoints Port-Channel Behavior Demo

## Overview

This demo highlights a key behavioral difference between two AVD data models: `connected_endpoints` and `network_ports`, specifically when defining **Port-Channels** across a fabric.

The goal is to demonstrate how `connected_endpoints` can simplify configuration and enforce validation, and how `network_ports` can be enhanced using profiles to achieve safe, repeatable port-channel definitions.

## AVD Data Model Context

From the AVD documentation:

- `connected_endpoints`: Endpoint-centric model, ideal for servers or ports with unique configs.
- `network_ports`: Compact, port-centric model, ideal for large-scale generic configurations.

Key behaviors:
- **Both models can coexist**, with `connected_endpoints` taking precedence if a port is defined in both.
- Both models **support inheritance** from `port_profiles`, allowing shared configuration.
- `network_ports` requires manual `channel_id` for multi-port Port-Channels, or uses a 1:1 auto-generated mapping.
- `connected_endpoints` supports automatic `channel_id` assignment and includes built-in duplicate detection.

---

## ✅ Working Example: `connected_endpoints` with automatic Port-Channel creation

### CONNECTED_ENDPOINTS.yml
```yaml
- name: Test-Port-Channel
  adapters:
    - endpoint_ports: [Ethernet9, Ethernet10]
      switch_ports: [Ethernet9, Ethernet10]
      switches: [A-LEAF5, A-LEAF6]
      profile: DEFAULT
      port_channel:
        mode: active
```

### Ansible Playbook Output (summary)
```
changed: [A-LEAF5 -> localhost]
changed: [A-LEAF6 -> localhost]
```

### Generated EOS CLI Config
```eos
interface Port-Channel9
   description SERVER_Test-Port-Channel
   no shutdown
   switchport mode access
   switchport
   mlag 9
   spanning-tree portfast
   spanning-tree bpduguard enable
```

> ✅ AVD auto-assigned `channel_id` 9 and created the port-channel cleanly.

---

## ❌ Duplication Protection: Manually setting conflicting `channel_id`

### Modified CONNECTED_ENDPOINTS.yml
```yaml
- name: Test-Port-Channel
  adapters:
    - endpoint_ports: [Ethernet9, Ethernet10]
      switch_ports: [Ethernet9, Ethernet10]
      switches: [A-LEAF5, A-LEAF6]
      profile: DEFAULT
      port_channel:
        mode: active

- name: Test-Port-Channel-Failboat
  adapters:
    - endpoint_ports: [Ethernet11, Ethernet12]
      switch_ports: [Ethernet11, Ethernet12]
      switches: [A-LEAF5, A-LEAF6]
      profile: DEFAULT
      port_channel:
        mode: active
        channel_id: 9
```

### Build Output
```
AristaAvdDuplicateDataError: Found duplicate objects with conflicting data while generating configuration for Port-channel Interfaces defined under connected_endpoints.
{'name': 'Port-Channel9', 'description': 'SERVER_Test-Port-Channel-Failboat'} conflicts with {'name': 'Port-Channel9', 'description': 'SERVER_Test-Port-Channel'}.
```

> ❌ AVD detects the duplication and halts the build. This protection is built into `connected_endpoints`.

---

## ✅ Safer `network_ports` using `port_profiles` with defined `channel_id`

By leveraging `port_profiles`, you can safely define port-channels using the `network_ports` model without risking accidental ID duplication.

### CONNECTED_ENDPOINTS.yml (using `network_ports`)
```yaml
port_profiles:
  - profile: PC-PROFILE-A
    port_channel:
      channel_id: 100
  - profile: PC-PROFILE-B
    port_channel:
      channel_id: 200

network_ports:
  - switches:
      - A-LEAF5
      - A-LEAF6
    switch_ports:
      - Ethernet9
      - Ethernet10
    description: Multiple interfaces in the same port-channel
    port_channel:
      mode: active
    profile: PC-PROFILE-A

  - switches:
      - A-LEAF5
      - A-LEAF6
    switch_ports:
      - Ethernet13
      - Ethernet14
    port_channel:
      mode: active
    profile: PC-PROFILE-B
```

### Ansible Playbook Output
```
changed: [A-LEAF5 -> localhost]
changed: [A-LEAF6 -> localhost]
```

### Generated EOS CLI Config
```eos
interface Port-Channel100
   no shutdown
   switchport
   mlag 100
!
interface Port-Channel200
   no shutdown
   switchport
   mlag 200
!
interface Ethernet9
   description Multiple interfaces in the same port-channel
   no shutdown
   channel-group 100 mode active
!
interface Ethernet10
   description Multiple interfaces in the same port-channel
   no shutdown
   channel-group 100 mode active
!
interface Ethernet13
   no shutdown
   channel-group 200 mode active
!
interface Ethernet14
   no shutdown
   channel-group 200 mode active
```

> ✅ By placing `channel_id` in the profile, you avoid accidental reuse while keeping the config DRY and scalable.

---

## Recommendation

- Use `connected_endpoints` when:
  - You want per-endpoint clarity and AVD-managed `channel_id`s.
  - You want built-in duplication detection and simplified modeling.

- Use `network_ports` when:
  - You need to apply generic, large-scale port templates.
  - Combine with `port_profiles` to safely control `channel_id` values.

Both models are powerful and interoperable — the right choice depends on your use case. For most port-channel use cases with varying configurations, `connected_endpoints` offers more guardrails and ease of use.

---

## Appendix

- AVD Version: `5.1.0`
- Devices: `A-LEAF5`, `A-LEAF6`
- Ansible version: Use `ansible-playbook -v` for full debug if needed

