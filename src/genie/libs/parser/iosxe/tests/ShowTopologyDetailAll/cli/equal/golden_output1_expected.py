expected_output = {
    "topologies": {
        "base": {
            "address_families": {
                "ipv4": {
                    "vrfs": {
                        "default": {
                            "state": "UP",
                            "cef_forwarding": "enabled",
                            "lock_count": 2,
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
                                },
                                {
                                    "if_name": "Loopback20",
                                    "oper_state": "DOWN",
                                    "upstream": False
                                }
                            ],
                            "user_lock_count": 0
                        },
                        "foo": {
                            "state": "UP",
                            "cef_forwarding": "enabled",
                            "lock_count": 2,
                            "user_lock_count": 0
                        },
                        "__Platform_iVRF:_ID00_": {
                            "is_ivrf": True,
                            "state": "UP",
                            "cef_forwarding": "disabled",
                            "lock_count": 2,
                            "user_lock_count": 0
                        }
                    }
                },
                "ipv6": {
                    "vrfs": {
                        "default": {
                            "state": "DOWN",
                            "cef_forwarding": "enabled",
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
                            "user_lock_count": 0
                        }
                    }
                },
                "ipv4 multicast": {
                    "vrfs": {
                        "default": {
                            "state": "DOWN",
                            "cef_forwarding": "disabled",
                            "lock_count": 2,
                            "is_replicated": True,
                            "rpl_routes": [
                                {
                                    "source_vrf": "",
                                    "safi": "unicast",
                                    "rpl_topo": "",
                                    "protocol": "all",
                                    "router_id": "",
                                    "route_map_name": "",
                                    "src_topo_fwdref": False
                                }
                            ],
                            "user_lock_count": 0
                        },
                        "foo": {
                            "state": "DOWN",
                            "cef_forwarding": "disabled",
                            "lock_count": 2,
                            "is_replicated": True,
                            "rpl_routes": [
                                {
                                    "source_vrf": "",
                                    "safi": "unicast",
                                    "rpl_topo": "",
                                    "protocol": "all",
                                    "router_id": "",
                                    "route_map_name": "",
                                    "src_topo_fwdref": False
                                }
                            ],
                            "user_lock_count": 0
                        }
                    }
                },
                "ipv6 multicast": {
                    "vrfs": {
                        "default": {
                            "state": "DOWN",
                            "cef_forwarding": "disabled",
                            "lock_count": 2,
                            "is_replicated": True,
                            "rpl_routes": [
                                {
                                    "source_vrf": "",
                                    "safi": "unicast",
                                    "rpl_topo": "",
                                    "protocol": "all",
                                    "router_id": "",
                                    "route_map_name": "",
                                    "src_topo_fwdref": False
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
