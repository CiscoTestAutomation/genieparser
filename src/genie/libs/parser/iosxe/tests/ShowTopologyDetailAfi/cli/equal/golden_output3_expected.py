expected_output = {
    "topologies": {
        "t1": {
            "address_families": {
                "ipv4": {
                    "vrfs": {
                        "default": {
                            "state": "UP",
                            "cef_forwarding": "enabled",
                            "lock_count": 2,
                            "all_interfaces": True,
                            "assoc_interfaces": [
                                {
                                    "if_name": "GigabitEthernet1",
                                    "oper_state": "UP",
                                    "upstream": False
                                },
                                {
                                    "if_name": "GigabitEthernet2",
                                    "oper_state": "UP",
                                    "upstream": False
                                }
                            ],
                            "user_lock_count": 0,
                            "topo_deleted": True
                        }
                    }
                }
            }
        }
    }
}
