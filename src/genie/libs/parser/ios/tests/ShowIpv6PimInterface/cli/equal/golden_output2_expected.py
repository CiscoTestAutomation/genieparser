expected_output = {
    "vrf": {
        "VRF1": {
            "interface": {
                "Loopback1": {
                    "dr_priority": 1,
                    "neighbor_count": 0,
                    "address": ["FE80::21E:F6FF:FEAC:A600"],
                    "pim_enabled": True,
                    "hello_interval": 30,
                },
                "Tunnel6": {
                    "dr_priority": 1,
                    "neighbor_count": 0,
                    "pim_enabled": False,
                    "hello_interval": 30,
                },
                "Tunnel5": {
                    "dr_priority": 1,
                    "neighbor_count": 0,
                    "address": ["FE80::21E:F6FF:FEAC:A600"],
                    "pim_enabled": False,
                    "hello_interval": 30,
                },
                "Tunnel7": {
                    "dr_priority": 1,
                    "neighbor_count": 0,
                    "pim_enabled": False,
                    "hello_interval": 30,
                },
                "GigabitEthernet3": {
                    "dr_priority": 1,
                    "neighbor_count": 0,
                    "address": ["FE80::5054:FF:FE84:F097"],
                    "pim_enabled": True,
                    "hello_interval": 30,
                },
            }
        }
    }
}
