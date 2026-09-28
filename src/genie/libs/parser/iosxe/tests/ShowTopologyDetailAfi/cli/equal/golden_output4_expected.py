expected_output = {
    "topologies": {
        "test": {
            "address_families": {
                "ipv4": {
                    "vrfs": {
                        "default": {
                            "state": "UP",
                            "cef_forwarding": "enabled",
                            "lock_count": 1,
                            "max_route_limit": 100,
                            "warn_limit_percent": 7,
                            "warn_limit": 7,
                            "assoc_interfaces": [
                                {
                                    "if_name": "Ethernet0/0",
                                    "oper_state": "DOWN",
                                    "upstream": True
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
