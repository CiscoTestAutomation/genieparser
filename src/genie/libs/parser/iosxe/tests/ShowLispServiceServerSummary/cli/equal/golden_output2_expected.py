expected_output = {
    "lisp_router_instances": {
        0: {
            "lisp_router_instance_id": 0,
            "service": {
                "ipv6": {
                    "instance_id": {
                        "101": {
                            "map_server": {
                                "summary": {
                                    "number_configured_sites": 2,
                                    "number_registered_sites": 2,
                                    "af_datum": {
                                        "ipv6-afi": {
                                            "address_type": "ipv6-afi",
                                            "number_configured_eids": 2,
                                            "number_registered_eids": 2,
                                        }
                                    },
                                    "sites_with_inconsistent_registrations": 0,
                                },
                                "sites": {
                                    "xtr1_1": {
                                        "configured": 1,
                                        "inconsistent": 0,
                                        "registered": 1,
                                        "site_id": "xtr1_1",
                                    },
                                    "xtr2": {
                                        "configured": 1,
                                        "inconsistent": 0,
                                        "registered": 1,
                                        "site_id": "xtr2",
                                    },
                                },
                            }
                        }
                    }
                }
            },
        }
    }
}
