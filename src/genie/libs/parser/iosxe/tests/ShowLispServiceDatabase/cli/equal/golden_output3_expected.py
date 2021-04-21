expected_output = {
    "lisp_router_instances": {
        0: {
            "lisp_router_instance_id": 0,
            "locator_sets": {"RLOC": {"locator_set_name": "RLOC"}},
            "service": {
                "ethernet": {
                    "etr": {
                        "local_eids": {
                            "1": {
                                "vni": "1",
                                "total_eid_entries": 2,
                                "no_route_eid_entries": 0,
                                "inactive_eid_entries": 0,
                                "dynamic_eids": {
                                    "0050.56ff.1bbe/48": {
                                        "dynamic_eid": "Auto-L2-group-1",
                                        "eid_address": {
                                            "address_type": "ethernet",
                                            "vrf": "101",
                                        },
                                        "id": "0050.56ff.1bbe/48",
                                        "loopback_address": "10.229.11.1",
                                        "priority": 1,
                                        "rlocs": "RLOC",
                                        "source": "cfg-intf",
                                        "state": "site-self, reachable",
                                        "weight": 100,
                                    },
                                    "cafe.caff.c9fd/48": {
                                        "dynamic_eid": "Auto-L2-group-1",
                                        "eid_address": {
                                            "address_type": "ethernet",
                                            "vrf": "101",
                                        },
                                        "id": "cafe.caff.c9fd/48",
                                        "loopback_address": "10.229.11.1",
                                        "priority": 1,
                                        "rlocs": "RLOC",
                                        "source": "cfg-intf",
                                        "state": "site-self, reachable",
                                        "weight": 100,
                                    },
                                },
                            },
                            "2": {
                                "vni": "2",
                                "total_eid_entries": 2,
                                "no_route_eid_entries": 0,
                                "inactive_eid_entries": 0,
                                "dynamic_eids": {
                                    "0050.56ff.118f/48": {
                                        "dynamic_eid": "Auto-L2-group-2",
                                        "eid_address": {
                                            "address_type": "ethernet",
                                            "vrf": "102",
                                        },
                                        "id": "0050.56ff.118f/48",
                                        "loopback_address": "10.229.11.1",
                                        "priority": 1,
                                        "rlocs": "RLOC",
                                        "source": "cfg-intf",
                                        "state": "site-self, reachable",
                                        "weight": 100,
                                    },
                                    "face.01ff.7172/48": {
                                        "dynamic_eid": "Auto-L2-group-2",
                                        "eid_address": {
                                            "address_type": "ethernet",
                                            "vrf": "102",
                                        },
                                        "id": "face.01ff.7172/48",
                                        "loopback_address": "10.229.11.1",
                                        "priority": 1,
                                        "rlocs": "RLOC",
                                        "source": "cfg-intf",
                                        "state": "site-self, reachable",
                                        "weight": 100,
                                    },
                                },
                            },
                        }
                    }
                }
            },
        }
    }
}
