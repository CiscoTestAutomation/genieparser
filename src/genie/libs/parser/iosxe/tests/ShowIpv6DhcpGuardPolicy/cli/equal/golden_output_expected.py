expected_output = { 
   "dhcp_guard_policy_config":{
      "policy_name":"pol1",
      "trusted_port":True,
      "device_role":"dhcp server",
      "max_preference":255,
      "min_preference":0,
      "access_list":"acl2",
      "prefix_list":"abc",
      "targets":{
          "vlan 2":{
            "target":"vlan 2",
            "type":"VLAN",
            "feature":"DHCP Guard",
            "target_range":"vlan all"
            },
            "vlan 3":{
                "target":"vlan 3",
                "type":"VLAN",
                "feature":"DHCP Guard",
                "target_range":"vlan all"
            },
            "vlan 4":{
                "target":"vlan 4",
                "type":"VLAN",
                "feature":"DHCP Guard",
                "target_range":"vlan all"
            },
            "vlan 5":{
                "target":"vlan 5",
                "type":"VLAN",
                "feature":"DHCP Guard",
                "target_range":"vlan all"
            },
            "vlan 6":{
                "target":"vlan 6",
                "type":"VLAN",
                "feature":"DHCP Guard",
                "target_range":"vlan all"
            },
            "vlan 7":{
                "target":"vlan 7",
                "type":"VLAN",
                "feature":"DHCP Guard",
                "target_range":"vlan all"
            },
            "vlan 8":{
                "target":"vlan 8",
                "type":"VLAN",
                "feature":"DHCP Guard",
                "target_range":"vlan all"
            },
            "vlan 9":{
                "target":"vlan 9",
                "type":"VLAN",
                "feature":"DHCP Guard",
                "target_range":"vlan all"
            },
            "vlan 10":{
                "target":"vlan 10",
                "type":"VLAN",
                "feature":"DHCP Guard",
                "target_range":"vlan all"
            }
        }
    }
}