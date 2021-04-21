expected_output = {
    "interfaces": {
        "Vlan6000": {
            "interface_state": False,
            "config_status": True,
            "name": "pod555",
            "link_status": False,
            "line_protocol": False,
            "mac_address": "aa11.bbff.ee55",
            "mtu": 1500,
            "ipv4": {"10.10.1.1": {"ip": "10.10.1.1"}},
            "subnet": "255.255.255.0",
            "traffic_statistics": {
                "packets_input": 0,
                "bytes_input": 0,
                "packets_output": 0,
                "bytes_output": 0,
                "packets_dropped": 0,
            },
            "control_point_states": {
                "interface": {
                    "interface_number": 612,
                    "interface_config_status": "active",
                    "interface_state": "not active",
                },
                "Vlan6000": {
                    "interface_vlan_config_status": "not active",
                    "interface_vlan_state": "DOWN",
                },
            },
        }
    }
}
