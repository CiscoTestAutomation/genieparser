expected_output = {
    "topologies": {
        "base": {
            "address_families": {
                "ipv4 multicast": {
                    "vrfs": {
                        "v1": {
                            "state": "UP",
                            "cef_forwarding": "disabled",
                            "lock_count": 1,
                            "mcast_multitopology": True,
                            "is_replicated": True,
                            "rpl_routes": [
                                {
                                    "source_vrf": "v2",
                                    "safi": "unicast",
                                    "rpl_topo": "",
                                    "protocol": "all",
                                    "router_id": "",
                                    "route_map_name": "",
                                    "src_topo_fwdref": False
                                }
                            ],
                            "assoc_interfaces": [
                                {
                                    "if_name": "Loopback10",
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
