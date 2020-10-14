expected_output = {
    "instance": {
        "default": {
            "vrf": {
                "blue": {
                    "address_family": {
                        "vpnv4": {
                            "prefixes": {
                                "10.144.0.0/24": {
                                    "table_version": "88",
                                    "available_path": "4",
                                    "best_path": "1",
                                    "paths": "4 available, best #1, table blue",
                                    "index": {
                                        1: {
                                            "next_hop": "10.3.3.3",
                                            "gateway": "10.6.6.6",
                                            "imported_path_from": "12:23:10.144.0.0/24",
                                            "originator": "10.6.6.6",
                                            "route_info": "1",
                                            "next_hop_igp_metric": "21",
                                            "localpref": 200,
                                            "metric": 0,
                                            "mpls_labels": {
                                                "in": "nolabel",
                                                "out": "37",
                                            },
                                            "origin_codes": "?",
                                            "status_codes": "*>",
                                            "ext_community": "RT:12:23",
                                            "update_group": 6,
                                        },
                                        2: {
                                            "next_hop": "10.13.13.13",
                                            "gateway": "10.13.13.13",
                                            "imported_path_from": "12:23:10.144.0.0/24",
                                            "originator": "10.0.0.2",
                                            "route_info": "1",
                                            "next_hop_via": "green",
                                            "localpref": 100,
                                            "metric": 0,
                                            "origin_codes": "?",
                                            "status_codes": "* ",
                                            "ext_community": "RT:12:23 ",
                                            "recursive_via_connected": True,
                                            "update_group": 6,
                                        },
                                        3: {
                                            "next_hop": "10.3.3.3",
                                            "gateway": "10.7.7.7",
                                            "imported_path_from": "12:23:10.144.0.0/24",
                                            "originator": "10.7.7.7",
                                            "next_hop_igp_metric": "21",
                                            "localpref": 200,
                                            "metric": 0,
                                            "mpls_labels": {
                                                "in": "nolabel",
                                                "out": "37",
                                            },
                                            "origin_codes": "?",
                                            "route_info": "1",
                                            "status_codes": "* i",
                                            "ext_community": "RT:12:23",
                                            "update_group": 6,
                                        },
                                        4: {
                                            "next_hop": "10.11.11.11",
                                            "gateway": "10.11.11.11",
                                            "originator": "10.1.0.1",
                                            "ext_community": "RT:11:12 ",
                                            "recursive_via_connected": True,
                                            "update_group": 6,
                                        },
                                    },
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
