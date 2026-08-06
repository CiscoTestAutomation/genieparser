expected_output = {
    "topologies": {
        "Foo": {
            "address_families": {
                "ipv6": {
                    "vrfs": {
                        "Foo-VRF-123": {
                            "state": "DOWN",
                            "cef_forwarding": "enabled",
                            "topo_events": "0xab",
                            "lock_count": 2,
                            "assoc_interfaces": [
                                {
                                    "if_name": "GigabitEthernet1",
                                    "oper_state": "DOWN",
                                    "upstream": False
                                },
                                {
                                    "if_name": "GigabitEthernet2",
                                    "oper_state": "UP",
                                    "upstream": False
                                },
                                {
                                    "if_name": "Loopback20",
                                    "oper_state": "UP",
                                    "upstream": False
                                }
                            ],
                            "user_lock_count": 55
                        }
                    }
                }
            }
        }
    }
}
