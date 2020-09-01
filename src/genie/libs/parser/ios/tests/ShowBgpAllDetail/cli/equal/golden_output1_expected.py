expected_output = {
    "instance": {
        "default": {
            "vrf": {
                "VRF1": {
                    "address_family": {
                        "vpnv4 unicast RD 100:100": {
                            "default_vrf": "VRF1",
                            "prefixes": {
                                "10.229.11.11/32": {
                                    "available_path": "1",
                                    "best_path": "1",
                                    "index": {
                                        1: {
                                            "gateway": "0.0.0.0",
                                            "inaccessible": False,
                                            "localpref": 100,
                                            "metric": 0,
                                            "next_hop": "0.0.0.0",
                                            "next_hop_via": "vrf VRF1",
                                            "origin_codes": "?",
                                            "originator": "10.1.1.1",
                                            "recipient_pathid": "0",
                                            "refresh_epoch": 1,
                                            "route_info": "Local",
                                            "status_codes": "*>",
                                            "transfer_pathid": "0x0",
                                            "weight": "32768",
                                        }
                                    },
                                    "paths": "1 available, best #1, table VRF1",
                                    "table_version": "2",
                                }
                            },
                            "route_distinguisher": "100:100",
                        },
                        "vpnv6 unicast RD 100:100": {
                            "default_vrf": "VRF1",
                            "prefixes": {
                                "2001:11:11::11/128": {
                                    "available_path": "1",
                                    "best_path": "1",
                                    "index": {
                                        1: {
                                            "gateway": "0.0.0.0",
                                            "inaccessible": False,
                                            "localpref": 100,
                                            "metric": 0,
                                            "next_hop": "::",
                                            "next_hop_via": "vrf VRF1",
                                            "origin_codes": "?",
                                            "originator": "10.1.1.1",
                                            "recipient_pathid": "0",
                                            "refresh_epoch": 1,
                                            "route_info": "Local",
                                            "status_codes": "*>",
                                            "transfer_pathid": "0x0",
                                            "weight": "32768",
                                        }
                                    },
                                    "paths": "1 available, best #1, table VRF1",
                                    "table_version": "2",
                                }
                            },
                            "route_distinguisher": "100:100",
                        },
                    }
                },
                "default": {
                    "address_family": {
                        "ipv4 unicast": {
                            "prefixes": {
                                "10.4.1.1/32": {
                                    "available_path": "1",
                                    "best_path": "1",
                                    "index": {
                                        1: {
                                            "gateway": "0.0.0.0",
                                            "localpref": 100,
                                            "metric": 0,
                                            "next_hop": "0.0.0.0",
                                            "origin_codes": "?",
                                            "originator": "10.1.1.1",
                                            "recipient_pathid": "0",
                                            "refresh_epoch": 1,
                                            "route_info": "Local",
                                            "status_codes": "*>",
                                            "transfer_pathid": "0x0",
                                            "update_group": 3,
                                            "weight": "32768",
                                        }
                                    },
                                    "paths": "1 available, best #1, table default, RIB-failure(17)",
                                    "table_version": "4",
                                },
                                "10.1.1.0/24": {
                                    "available_path": "2",
                                    "best_path": "1",
                                    "index": {
                                        1: {
                                            "gateway": "0.0.0.0",
                                            "localpref": 100,
                                            "metric": 0,
                                            "next_hop": "0.0.0.0",
                                            "origin_codes": "?",
                                            "originator": "10.1.1.1",
                                            "recipient_pathid": "0",
                                            "refresh_epoch": 1,
                                            "route_info": "Local",
                                            "status_codes": "*>",
                                            "transfer_pathid": "0x0",
                                            "update_group": 3,
                                            "weight": "32768",
                                        },
                                        2: {
                                            "gateway": "10.1.1.2",
                                            "localpref": 100,
                                            "metric": 0,
                                            "next_hop": "10.1.1.2",
                                            "origin_codes": "?",
                                            "originator": "10.1.1.2",
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0",
                                            "refresh_epoch": 1,
                                            "route_info": "Local",
                                            "status_codes": "* i",
                                            "update_group": 3,
                                        },
                                    },
                                    "paths": "2 available, best #1, table default",
                                    "table_version": "5",
                                },
                                "10.16.2.2/32": {
                                    "available_path": "1",
                                    "best_path": "1",
                                    "index": {
                                        1: {
                                            "gateway": "10.1.1.2",
                                            "localpref": 100,
                                            "metric": 0,
                                            "next_hop": "10.1.1.2",
                                            "origin_codes": "?",
                                            "originator": "10.1.1.2",
                                            "recipient_pathid": "0",
                                            "refresh_epoch": 1,
                                            "route_info": "Local",
                                            "status_codes": "*>",
                                            "transfer_pathid": "0x0",
                                        }
                                    },
                                    "paths": "1 available, best #1, table default",
                                    "table_version": "2",
                                },
                            }
                        },
                        "ipv6 unicast": {
                            "prefixes": {
                                "2001:1:1:1::1/128": {
                                    "available_path": "1",
                                    "best_path": "1",
                                    "index": {
                                        1: {
                                            "gateway": "0.0.0.0",
                                            "localpref": 100,
                                            "metric": 0,
                                            "next_hop": "::",
                                            "origin_codes": "?",
                                            "originator": "10.1.1.1",
                                            "recipient_pathid": "0",
                                            "refresh_epoch": 1,
                                            "route_info": "Local",
                                            "status_codes": "*>",
                                            "transfer_pathid": "0x0",
                                            "update_group": 1,
                                            "weight": "32768",
                                        }
                                    },
                                    "paths": "1 available, best #1, table default",
                                    "table_version": "4",
                                },
                                "2001:2:2:2::2/128": {
                                    "available_path": "2",
                                    "best_path": "1",
                                    "index": {
                                        1: {
                                            "gateway": "2001:DB8:1:1::2",
                                            "localpref": 100,
                                            "metric": 0,
                                            "next_hop": "2001:DB8:1:1::2",
                                            "origin_codes": "?",
                                            "originator": "10.1.1.2",
                                            "recipient_pathid": "0",
                                            "refresh_epoch": 1,
                                            "route_info": "Local",
                                            "status_codes": "*>",
                                            "transfer_pathid": "0x0",
                                        },
                                        2: {
                                            "gateway": "10.1.1.2",
                                            "localpref": 100,
                                            "metric": 0,
                                            "next_hop": "::FFFF:10.1.1.2",
                                            "origin_codes": "?",
                                            "originator": "10.1.1.2",
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0",
                                            "refresh_epoch": 1,
                                            "route_info": "Local",
                                            "status_codes": "* i",
                                        },
                                    },
                                    "paths": "2 available, best #1, table default",
                                    "table_version": "2",
                                },
                                "2001:DB8:1:1::/64": {
                                    "available_path": "3",
                                    "best_path": "1",
                                    "index": {
                                        1: {
                                            "gateway": "0.0.0.0",
                                            "localpref": 100,
                                            "metric": 0,
                                            "next_hop": "::",
                                            "origin_codes": "?",
                                            "originator": "10.1.1.1",
                                            "recipient_pathid": "0",
                                            "refresh_epoch": 1,
                                            "route_info": "Local",
                                            "status_codes": "*>",
                                            "transfer_pathid": "0x0",
                                            "update_group": 1,
                                            "weight": "32768",
                                        },
                                        2: {
                                            "gateway": "2001:DB8:1:1::2",
                                            "localpref": 100,
                                            "metric": 0,
                                            "next_hop": "2001:DB8:1:1::2",
                                            "origin_codes": "?",
                                            "originator": "10.1.1.2",
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0",
                                            "refresh_epoch": 1,
                                            "route_info": "Local",
                                            "status_codes": "* i",
                                            "update_group": 1,
                                        },
                                        3: {
                                            "gateway": "10.1.1.2",
                                            "localpref": 100,
                                            "metric": 0,
                                            "next_hop": "::FFFF:10.1.1.2",
                                            "origin_codes": "?",
                                            "originator": "10.1.1.2",
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0",
                                            "refresh_epoch": 1,
                                            "route_info": "Local",
                                            "status_codes": "* i",
                                            "update_group": 1,
                                        },
                                    },
                                    "paths": "3 available, best #1, table default",
                                    "table_version": "5",
                                },
                            }
                        },
                    }
                },
            }
        }
    }
}
