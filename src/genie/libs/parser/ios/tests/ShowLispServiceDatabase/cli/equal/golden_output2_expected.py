expected_output = {
    "lisp_router_instances": {
        0: {
            "lisp_router_instance_id": 0,
            "locator_sets": {"RLOC": {"locator_set_name": "RLOC"}},
            "service": {
                "ipv6": {
                    "etr": {
                        "local_eids": {
                            "101": {
                                "vni": "101",
                                "total_eid_entries": 1,
                                "no_route_eid_entries": 0,
                                "inactive_eid_entries": 0,
                                "eids": {
                                    "2001:192:168::/64": {
                                        "eid_address": {
                                            "address_type": "ipv6",
                                            "vrf": "red",
                                        },
                                        "id": "2001:192:168::/64",
                                        "loopback_address": "10.16.2.2",
                                        "priority": 50,
                                        "rlocs": "RLOC",
                                        "source": "cfg-intf",
                                        "state": "site-self, reachable",
                                        "weight": 50,
                                    }
                                },
                            }
                        }
                    }
                }
            },
        }
    }
}
