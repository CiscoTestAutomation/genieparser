expected_output = {
    "topologies": {
        "base": {
            "address_families": {
                "ipv6": {
                    "vrfs": {
                        "v1": {
                            "state": "UP",
                            "cef_forwarding": "enabled",
                            "lock_count": 1,
                            "assoc_interfaces": [
                                {
                                    "if_name": "Tunnel1",
                                    "oper_state": "DOWN",
                                    "upstream": False
                                },
                                {
                                    "if_name": "Ethernet0/0",
                                    "oper_state": "DOWN",
                                    "upstream": False
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
