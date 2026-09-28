expected_output = {
    "topologies": {
        "base": {
            "address_families": {
                "ipv4": {
                    "vrfs": {
                        "v1": {
                            "state": "UP",
                            "cef_forwarding": "enabled",
                            "lock_count": 2,
                            "user_lock_count": 0
                        }
                    }
                },
                "ipv6": {
                    "vrfs": {
                        "v1": {
                            "state": "DOWN",
                            "cef_forwarding": "enabled",
                            "lock_count": 2,
                            "user_lock_count": 0
                        }
                    }
                },
                "ipv4 multicast": {
                    "vrfs": {
                        "v1": {
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
                        "v1": {
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
