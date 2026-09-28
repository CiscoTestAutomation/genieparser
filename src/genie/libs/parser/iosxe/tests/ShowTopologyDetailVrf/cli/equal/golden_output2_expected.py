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
                            "is_replicated": True,
                            "rpl_routes": [
                                {
                                    "source_vrf": "",
                                    "safi": "unicast",
                                    "rpl_topo": "",
                                    "protocol": "static",
                                    "router_id": "",
                                    "route_map_name": "",
                                    "src_topo_fwdref": False
                                },
                                {
                                    "source_vrf": "",
                                    "safi": "unicast",
                                    "rpl_topo": "",
                                    "protocol": "ospf",
                                    "router_id": "11",
                                    "route_map_name": "",
                                    "src_topo_fwdref": False
                                },
                                {
                                    "source_vrf": "",
                                    "safi": "unicast",
                                    "rpl_topo": "test",
                                    "protocol": "static",
                                    "router_id": "",
                                    "route_map_name": "",
                                    "src_topo_fwdref": False
                                },
                                {
                                    "source_vrf": "foo",
                                    "safi": "unicast",
                                    "rpl_topo": "",
                                    "protocol": "connected",
                                    "router_id": "",
                                    "route_map_name": "",
                                    "src_topo_fwdref": True
                                },
                                {
                                    "source_vrf": "global",
                                    "safi": "unicast",
                                    "rpl_topo": "",
                                    "protocol": "connected",
                                    "router_id": "",
                                    "route_map_name": "rm1",
                                    "src_topo_fwdref": False
                                },
                                {
                                    "source_vrf": "v1",
                                    "safi": "unicast",
                                    "rpl_topo": "t1",
                                    "protocol": "bgp",
                                    "router_id": "65001",
                                    "route_map_name": "",
                                    "src_topo_fwdref": False
                                },
                                {
                                    "source_vrf": "bar",
                                    "safi": "unicast",
                                    "rpl_topo": "",
                                    "protocol": "bgp",
                                    "router_id": "11.12",
                                    "route_map_name": "",
                                    "src_topo_fwdref": False
                                },
                                {
                                    "source_vrf": "vrf-a",
                                    "safi": "unicast",
                                    "rpl_topo": "",
                                    "protocol": "isis",
                                    "router_id": "tag123",
                                    "route_map_name": "",
                                    "src_topo_fwdref": True
                                },
                                {
                                    "source_vrf": "global",
                                    "safi": "unicast",
                                    "rpl_topo": "",
                                    "protocol": "ospf",
                                    "router_id": "777",
                                    "route_map_name": "",
                                    "src_topo_fwdref": False
                                }
                            ],
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
                                    "if_name": "Ethernet1/0.77",
                                    "oper_state": "DOWN",
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
