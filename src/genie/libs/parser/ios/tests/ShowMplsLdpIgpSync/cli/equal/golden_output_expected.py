expected_output = {
    "vrf": {
        "default": {
            "interface": {
                "FastEthernet0/0/0": {
                    "sync": {
                        "status": {
                            "enabled": True,
                            "sync_achieved": False,
                            "peer_reachable": True,
                        }
                    },
                    "ldp": {"configured": True, "igp_synchronization_enabled": False},
                    "igp": {"enabled": "ospf 1", "holddown_time": "infinite"},
                    "peer_ldp_ident": "10.0.0.1:0",
                }
            }
        }
    }
}
