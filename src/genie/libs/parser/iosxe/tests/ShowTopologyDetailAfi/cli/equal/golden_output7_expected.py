expected_output = {
    "topologies": {
        "base": {
            "address_families": {
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
                        },
                        "vrf-a": {
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
                        "vrf-b": {
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
                                },
                                {
                                    "source_vrf": "vrf-a",
                                    "safi": "unicast",
                                    "rpl_topo": "",
                                    "protocol": "ospf",
                                    "router_id": "1",
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
