expected_output = {
    "topologies": {
        "t1": {
            "address_families": {
                "ipv4": {
                    "vrfs": {
                        "default": {
                            "state": "UP",
                            "cef_forwarding": "enabled",
                            "fallback": True,
                            "lock_count": 1,
                            "used_by": [
                                {
                                    "used_by_topo_afi": "ipv4 multicast",
                                    "used_by_topo_name": "base"
                                },
                                {
                                    "used_by_topo_afi": "ipv4 multicast",
                                    "used_by_topo_name": "test"
                                },
                                {
                                    "used_by_topo_afi": "ipv4 multicast",
                                    "used_by_topo_name": "bar"
                                }
                            ],
                            "user_lock_count": 0
                        }
                    }
                }
            }
        }
    }
}
