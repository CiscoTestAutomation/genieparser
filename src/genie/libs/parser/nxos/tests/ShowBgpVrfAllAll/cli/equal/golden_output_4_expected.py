expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv6 unicast": {
                    "bgp_table_version": 177,
                    "local_router_id": "1.1.1.1",
                    "prefixes": {
                        "110:110:110::110/128": {
                            "index": {
                                1: {
                                    "status_codes": "*>",
                                    "path_type": "r",
                                    "next_hop": "0::",
                                    "origin_codes": "?",
                                    "metric": 0,
                                    "localprf": 100,
                                    "weight": 32768,
                                }
                            }
                        },
                        "122:122::122:122/128": {
                            "index": {
                                1: {
                                    "status_codes": "*>",
                                    "path_type": "e",
                                    "next_hop": "99:99:99::99",
                                    "origin_codes": "i",
                                    "weight": 30,
                                    "path": "2",
                                }
                            }
                        },
                        "123:123::123:123/128": {
                            "index": {
                                1: {
                                    "next_hop": "98:98:98::98",
                                    "origin_codes": "i",
                                    "status_codes": "*>",
                                    "path_type": "i",
                                    "weight": 20,
                                    "localprf": 100,
                                    "path": "3 2",
                                },
                                2: {
                                    "next_hop": "99:99:99::99",
                                    "origin_codes": "i",
                                    "status_codes": "None",
                                    "path_type": "e",
                                    "weight": 10,
                                    "path": "2",
                                },
                            }
                        },
                    },
                }
            }
        }
    }
}

