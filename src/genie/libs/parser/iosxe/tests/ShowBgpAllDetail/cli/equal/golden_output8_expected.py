expected_output = {
    "instance": {
        "default": {
            "vrf": {
                "one": {
                    "address_family": {
                        "": {
                            "prefixes": {
                                "11.5.0.0/24": {
                                    "table_version": "102",
                                    "available_path": "1",
                                    "best_path": "1",
                                    "paths": "1 available, best #1, table one",
                                    "index": {
                                        1: {
                                            "next_hop": "20.0.101.1",
                                            "gateway": "20.0.101.1",
                                            "originator": "20.0.101.1",
                                            "next_hop_via": "vrf one",
                                            "update_group": [1, 2, 3],
                                            "localpref": 100,
                                            "origin_codes": "i",
                                            "status_codes": "*>",
                                            "refresh_epoch": 1,
                                            "route_info": "3",
                                            "community": "65537",
                                            "ext_community": "RT:1:100",
                                            "mpls_labels": {
                                                "in": "16",
                                                "out": "nolabel"
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0x0"
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
}
