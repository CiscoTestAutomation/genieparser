expected_output = {
    "interfaces": {
        "FiveGigabitEthernet1/0/35": {
            "switchport_access_vlan": "19",
            "switchport_mode": "access",
            "load_interval": "30",
            "authentication_host_mode": "multi-domain",
            "authentication_priority": "mab",
            "authentication_port_control": "auto",
            "authentication_periodic": True,
            "mab": True,
            "spanning_tree_portfast": True,
            "input_policy": "AutoQos-4.0-CiscoPhone-Input-Policy",
            "output_policy": "AutoQos-4.0-Output-Policy",
            'trust_device': 'cisco-phone',
        }
    }
}
