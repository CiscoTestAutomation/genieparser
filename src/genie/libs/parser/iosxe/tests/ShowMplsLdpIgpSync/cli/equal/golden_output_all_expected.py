expected_output = {
    "vrf": {
        "default": {
            "interface": {
                "GigabitEthernet0/0/0": {
                    "ldp": {"configured": True, "igp_synchronization_enabled": True},
                    "sync": {
                        "status": {"sync_achieved": True, "peer_reachable": True},
                        "delay_time": 0,
                        "left_time": 0,
                    },
                    "igp": {"holddown_time": "infinite", "enabled": "ospf 65109"},
                    "peer_ldp_ident": "10.169.197.252:0",
                },
                "GigabitEthernet0/0/2": {
                    "ldp": {"configured": True, "igp_synchronization_enabled": False}
                },
            }
        }
    }
}
