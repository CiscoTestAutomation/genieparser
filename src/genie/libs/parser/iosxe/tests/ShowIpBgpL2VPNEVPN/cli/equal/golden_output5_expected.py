expected_output = {
    "instance": {
        "default": {
            "vrf": {
                "evi_2": {
                    "address_family": {
                        "l2vpn evpn": {
                            "prefixes": {
                                "[1][3.3.3.3:2][03AABB00000002000001][0]/23": {
                                    "table_version": "140",
                                    "nlri_data": {
                                        "route-type": "1",
                                        "rd": "3.3.3.3:2",
                                        "esi": "03AABB00000002000001",
                                        "eti": "0",
                                        "subnet": "23"
                                    },
                                    "available_path": "2",
                                    "best_path": "1",
                                    "paths": "2 available, best #1, table evi_2",
                                    "index": {
                                        1: {
                                            "next_hop": "::",
                                            "gateway": "0.0.0.0",
                                            "originator": "3.3.3.3",
                                            "next_hop_via": "default",
                                            "update_group": 1,
                                            "ext_community": "RT:100:2",
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0x0"
                                        },
                                        2: {
                                            "next_hop": "4.4.4.1",
                                            "gateway": "99.99.99.99",
                                            "originator": "99.99.99.99",
                                            "next_hop_igp_metric": "3",
                                            "next_hop_via": "default",
                                            "update_group": 1,
                                            "ext_community": "RT:100:2",
                                            "cluster_list": "99.99.99.99",
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0"
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                "EVPN-BGP-Table": {
                    "address_family": {
                        "l2vpn evpn": {
                            "prefixes": {
                                "[1][4.4.4.3:2][03AABB00000002000001][0]/23": {
                                    "table_version": "101",
                                    "nlri_data": {
                                        "route-type": "1",
                                        "rd": "4.4.4.3:2",
                                        "esi": "03AABB00000002000001",
                                        "eti": "0",
                                        "subnet": "23"
                                    },
                                    "available_path": "2",
                                    "best_path": "1",
                                    "paths": "2 available, best #1, table EVPN-BGP-Table",
                                    "index": {
                                        1: {
                                            "next_hop": "4.4.4.1",
                                            "gateway": "99.99.99.99",
                                            "originator": "99.99.99.99",
                                            "next_hop_igp_metric": "3",
                                            "next_hop_via": "default",
                                            "localpref": 100,
                                            "metric": 0,
                                            "origin_codes": "?",
                                            "status_codes": "*>",
                                            "refresh_epoch": 46,
                                            "route_info": "Local",
                                            "imported_path_from": "[1][4.4.4.3:2][03AABB00000002000001][0]/23 (global)",
                                            "ext_community": "RT:100:2",
                                            "cluster_list": "99.99.99.99",
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0x0"
                                        },
                                        2: {
                                            "next_hop": "4.4.4.1",
                                            "gateway": "98.98.98.98",
                                            "originator": "98.98.98.98",
                                            "next_hop_igp_metric": "3",
                                            "next_hop_via": "default",
                                            "localpref": 100,
                                            "metric": 0,
                                            "origin_codes": "?",
                                            "status_codes": "* i",
                                            "refresh_epoch": 46,
                                            "route_info": "Local",
                                            "imported_path_from": "[1][4.4.4.3:2][03AABB00000002000001][0]/23 (global)",
                                            "ext_community": "RT:100:2",
                                            "cluster_list": "98.98.98.98",
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0"
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