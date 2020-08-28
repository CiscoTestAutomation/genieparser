expected_output = {
    "vrf": {
        "default": {
            "interface": {
                "GigabitEthernet0/0/0": {
                    "ldp": {"configured": False, "igp_synchronization_enabled": True},
                    "sync": {
                        "status": {"sync_achieved": False, "peer_reachable": False},
                        "delay_time": 0,
                        "left_time": 0,
                    },
                    "igp": {"holddown_time": "infinite", "enabled": "ospf 88"},
                },
                "TenGigabitEthernet0/1/0": {
                    "ldp": {"configured": True, "igp_synchronization_enabled": True},
                    "sync": {
                        "status": {"sync_achieved": True, "peer_reachable": True},
                        "delay_time": 0,
                        "left_time": 0,
                    },
                    "igp": {"holddown_time": "1 milliseconds", "enabled": "ospf 88"},
                    "peer_ldp_ident": "10.169.197.252:0",
                },
                "TenGigabitEthernet0/2/0": {
                    "ldp": {"configured": True, "igp_synchronization_enabled": True},
                    "sync": {
                        "status": {"sync_achieved": True, "peer_reachable": True},
                        "delay_time": 0,
                        "left_time": 0,
                    },
                    "igp": {"holddown_time": "infinite", "enabled": "ospf 88"},
                    "peer_ldp_ident": "192.168.36.220:0",
                },
            }
        }
    }
}
