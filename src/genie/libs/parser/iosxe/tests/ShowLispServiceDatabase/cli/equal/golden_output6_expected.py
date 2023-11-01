expected_output = {
    "lisp_id": {
        "default": {
            "instance_id": {
                4097: {
                    "eid_table": "default",
                    "lsb": "0x1",
                    "entries": {
                        "total": 2,
                        "no_route": 0,
                        "inactive": 0,
                        'do_not_register': 2,
                        "eids": {
                            "100.64.232.1/32": {
                                "eid": "100.64.232.1",
                                "mask": 32,
                                "dynamic_eid": "CIP_INFRA_VN_AP_POOL-IPV4",
                                "locator_set": "rloc_b2f5589b-a3ac-4dcb-a816-7f421e0a683e",
                                "uptime": "7w3d",
                                "last_change": "7w3d",
                                "domain_id": "unset",
                                "service_insertion": "N/A",
                                "service_insertion_id": 0,
                                'do_not_register': True,
                                "locators": {
                                    "100.64.245.5": {
                                        "priority": 10,
                                        "weight": 10,
                                        "source": "cfg-intf",
                                        "location": "site-self",
                                        "state": "reachable",
                                        "affinity_id_x": 20,
                                        "affinity_id_y": 20
                                    }
                                }
                            },
                            "100.66.249.1/32": {
                                "eid": "100.66.249.1",
                                "mask": 32,
                                "dynamic_eid": "EXTENDED_NODES-IPV4",
                                "locator_set": "rloc_b2f5589b-a3ac-4dcb-a816-7f421e0a683e",
                                "uptime": "7w1d",
                                "last_change": "7w1d",
                                "domain_id": "unset",
                                "service_insertion": "N/A",
                                "service_insertion_id": 0,
                                'do_not_register': True,
                                "locators": {
                                    "100.64.245.5": {
                                        "priority": 10,
                                        "weight": 10,
                                        "source": "cfg-intf",
                                        "location": "site-self",
                                        "state": "reachable",
                                        "affinity_id_x": 101
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
