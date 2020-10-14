expected_output = {
    "instance": {
        "default": {
            "vrf": {
                "default": {
                    "address_family": {
                        "": {
                            "prefixes": {
                                "0.0.0.0/0": {
                                    "available_path": "2",
                                    "best_path": "1",
                                    "index": {
                                        1: {
                                            "community": "65100:106 65100:500 65100:601 65351:1 no-export",
                                            "gateway": "10.4.1.1",
                                            "localpref": 150,
                                            "next_hop": "10.4.1.1",
                                            "origin_codes": "i",
                                            "originator": "10.16.2.2",
                                            "route_info": "65000 65191 1111111002 1111111502 1111111001 1111111505 1111111005 1111111504 222222 333",
                                            "status_codes": "*>",
                                            "update_group": 8,
                                        },
                                        2: {
                                            "community": "65100:106 65100:500 65100:601 65351:1",
                                            "gateway": "10.4.1.1",
                                            "localpref": 100,
                                            "next_hop": "10.4.1.1",
                                            "origin_codes": "i",
                                            "originator": "10.16.2.2",
                                            "route_info": "65000 65191 1111111002 1111111502 1111111001 1111111505 1111111005 1111111504 222222 333",
                                            "route_status": "received-only",
                                            "status_codes": "* ",
                                            "update_group": 8,
                                        },
                                    },
                                    "paths": "2 available, best #1, table default, not advertised to EBGP peer",
                                    "table_version": "791832",
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
