expected_output = {
    "instance": {
        "default": {
            "vrf": {
                "default": {
                    "address_family": {
                        "vpnv4": {
                            "prefixes": {
                                "10.229.11.11/32": {
                                    "table_version": "6195",
                                    "available_path": "1",
                                    "best_path": "1",
                                    "paths": "1 available, best #1, no table",
                                    "index": {
                                        1: {
                                            "next_hop": "10.169.197.254",
                                            "gateway": "10.169.197.254",
                                            "originator": "10.169.197.254",
                                            "next_hop_igp_metric": "1002",
                                            "next_hop_via": "default",
                                            "localpref": 100,
                                            "metric": 0,
                                            "mpls_labels": {
                                                "in": "nolabel",
                                                "out": "584",
                                            },
                                            "origin_codes": "?",
                                            "status_codes": "*>",
                                            "refresh_epoch": 9,
                                            "route_info": "65555",
                                            "route_status": "Received from a RR-client",
                                            "community": "62000:1",
                                            "ext_community": "RT:65109:4093",
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0x0",
                                            "update_group": [17, 18]
                                        }
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
