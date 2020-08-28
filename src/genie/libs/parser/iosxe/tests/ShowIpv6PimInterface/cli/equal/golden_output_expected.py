expected_output = {
    "vrf": {
        "default": {
            "interface": {
                "Tunnel4": {
                    "dr_priority": 1,
                    "neighbor_count": 0,
                    "hello_interval": 30,
                    "pim_enabled": False,
                },
                "Null0": {
                    "address": ["FE80::1"],
                    "dr_priority": 1,
                    "neighbor_count": 0,
                    "hello_interval": 30,
                    "pim_enabled": False,
                },
                "Loopback0": {
                    "address": ["FE80::21E:F6FF:FEAC:A600"],
                    "dr_priority": 1,
                    "neighbor_count": 0,
                    "hello_interval": 30,
                    "pim_enabled": True,
                },
                "Tunnel3": {
                    "dr_priority": 1,
                    "neighbor_count": 0,
                    "hello_interval": 30,
                    "pim_enabled": False,
                },
                "Tunnel1": {
                    "address": ["FE80::21E:F6FF:FEAC:A600"],
                    "dr_priority": 1,
                    "neighbor_count": 0,
                    "hello_interval": 30,
                    "pim_enabled": False,
                },
                "GigabitEthernet1": {
                    "address": ["FE80::5054:FF:FE2C:6CDF"],
                    "dr_address": "FE80::5054:FF:FEAC:64B3",
                    "pim_enabled": True,
                    "dr_priority": 1,
                    "neighbor_count": 1,
                    "hello_interval": 30,
                },
                "Tunnel2": {
                    "dr_priority": 1,
                    "neighbor_count": 0,
                    "hello_interval": 30,
                    "pim_enabled": False,
                },
                "GigabitEthernet2": {
                    "address": ["FE80::5054:FF:FEBE:8787"],
                    "dr_priority": 1,
                    "neighbor_count": 0,
                    "hello_interval": 30,
                    "pim_enabled": True,
                },
                "Tunnel0": {
                    "address": ["FE80::21E:F6FF:FEAC:A600"],
                    "dr_priority": 1,
                    "neighbor_count": 0,
                    "hello_interval": 30,
                    "pim_enabled": False,
                },
            }
        }
    }
}
