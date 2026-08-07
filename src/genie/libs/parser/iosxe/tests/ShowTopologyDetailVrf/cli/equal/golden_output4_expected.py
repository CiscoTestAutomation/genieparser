expected_output = {
    "topologies": {
        "base": {
            "address_families": {
                "ipv4 multicast": {
                    "vrfs": {
                        "v2": {
                            "state": "DOWN",
                            "cef_forwarding": "disabled",
                            "lock_count": 4,
                            "mcast_multitopology": True,
                            "user_lock_count": 0
                        }
                    }
                }
            }
        },
        "foo": {
            "address_families": {
                "ipv4 multicast": {
                    "vrfs": {
                        "v2": {
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
        },
        "test_topo": {
            "address_families": {
                "ipv4 multicast": {
                    "vrfs": {
                        "v2": {
                            "state": "DOWN",
                            "cef_forwarding": "disabled",
                            "lock_count": 2,
                            "user_lock_count": 0
                        }
                    }
                }
            }
        }
    }
}
