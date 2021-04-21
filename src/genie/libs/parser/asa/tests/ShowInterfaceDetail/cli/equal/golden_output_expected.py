expected_output = {
    "interfaces": {
        "Vlan5000": {
            "interface_state": True,
            "config_status": True,
            "name": "pod248",
            "link_status": True,
            "line_protocol": True,
            "mac_address": "aa11.bbff.ee55",
            "mtu": 1500,
            "ipv4": {"10.10.1.1": {"ip": "10.10.1.1"}},
            "subnet": "255.255.255.0",
            "traffic_statistics": {
                "packets_input": 34354322,
                "bytes_input": 32443242111,
                "packets_output": 92739172,
                "bytes_output": 4309803982,
                "packets_dropped": 2551519,
            },
            "control_point_states": {
                "interface": {
                    "interface_number": 899,
                    "interface_config_status": "active",
                    "interface_state": "active",
                },
                "Vlan5000": {
                    "interface_vlan_config_status": "active",
                    "interface_vlan_state": "UP",
                },
            },
        }
    }
}
