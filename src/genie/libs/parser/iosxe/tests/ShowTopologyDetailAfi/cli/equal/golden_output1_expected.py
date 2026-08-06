expected_output = {
    "topologies": {
        "base": {
            "address_families": {
                "ipv6": {
                    "vrfs": {
                        "default": {
                            "state": "UP",
                            "cef_forwarding": "enabled",
                            "lock_count": 2,
                            "assoc_interfaces": [
                                {
                                    "if_name": "Ethernet0/2",
                                    "oper_state": "DOWN",
                                    "upstream": False
                                },
                                {
                                    "if_name": "Ethernet0/3",
                                    "oper_state": "DOWN",
                                    "upstream": False
                                },
                                {
                                    "if_name": "Ethernet1/0",
                                    "oper_state": "DOWN",
                                    "upstream": False
                                },
                                {
                                    "if_name": "Ethernet1/1",
                                    "oper_state": "DOWN",
                                    "upstream": False
                                },
                                {
                                    "if_name": "Ethernet1/2",
                                    "oper_state": "DOWN",
                                    "upstream": False
                                },
                                {
                                    "if_name": "Ethernet1/3",
                                    "oper_state": "DOWN",
                                    "upstream": False
                                },
                                {
                                    "if_name": "Serial2/0",
                                    "oper_state": "DOWN",
                                    "upstream": False
                                },
                                {
                                    "if_name": "Serial2/1",
                                    "oper_state": "DOWN",
                                    "upstream": False
                                },
                                {
                                    "if_name": "Serial2/2",
                                    "oper_state": "DOWN",
                                    "upstream": False
                                },
                                {
                                    "if_name": "Serial2/3",
                                    "oper_state": "DOWN",
                                    "upstream": False
                                },
                                {
                                    "if_name": "Serial3/0",
                                    "oper_state": "DOWN",
                                    "upstream": False
                                },
                                {
                                    "if_name": "Serial3/1",
                                    "oper_state": "DOWN",
                                    "upstream": False
                                },
                                {
                                    "if_name": "Serial3/2",
                                    "oper_state": "DOWN",
                                    "upstream": False
                                },
                                {
                                    "if_name": "Serial3/3",
                                    "oper_state": "DOWN",
                                    "upstream": False
                                },
                                {
                                    "if_name": "Ethernet1/0.77",
                                    "oper_state": "DOWN",
                                    "upstream": False
                                }
                            ],
                            "user_lock_count": 0
                        },
                        "vrf-a": {
                            "state": "UP",
                            "cef_forwarding": "enabled",
                            "lock_count": 2,
                            "assoc_interfaces": [
                                {
                                    "if_name": "Ethernet0/0",
                                    "oper_state": "UP",
                                    "upstream": False
                                }
                            ],
                            "user_lock_count": 0
                        },
                        "vrf-b": {
                            "state": "UP",
                            "cef_forwarding": "enabled",
                            "lock_count": 2,
                            "is_replicated": True,
                            "rpl_routes": [
                                {
                                    "source_vrf": "vrf-a",
                                    "safi": "unicast",
                                    "rpl_topo": "",
                                    "protocol": "ospf",
                                    "router_id": "1",
                                    "route_map_name": "",
                                    "src_topo_fwdref": True
                                }
                            ],
                            "assoc_interfaces": [
                                {
                                    "if_name": "Ethernet0/1",
                                    "oper_state": "UP",
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
