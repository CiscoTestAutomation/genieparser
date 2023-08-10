expected_output = {
    "instance": {
        "default": {
            "vrf": {
                "EVPN-BGP-Table": {
                    "address_family": {
                        "l2vpn evpn": {
                            "prefixes": {
                                "101.102.0.0/17": {
                                    "table_version": "5923",
                                    "available_path": "2",
                                    "best_path": "2",
                                    "paths": "2 available, best #2, table EVPN-BGP-Table",
                                    "index": {
                                        1: {
                                            "next_hop": "20.0.101.1",
                                            "gateway": "20.1.150.3",
                                            "originator": "20.1.150.3",
                                            "next_hop_via": "default",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "ext_community": "RT:20.1.101.1:101 ENCAP:8 Router MAC:5C71.0DCD.F0E0",
                                            "origin_codes": "?",
                                            "status_codes": "* ",
                                            "refresh_epoch": 1,
                                            "route_info": "150",
                                            "route_status": "received & used",
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0"
                                        },
                                        2: {
                                            "next_hop": "20.0.101.1",
                                            "gateway": "20.1.150.4",
                                            "originator": "20.1.150.4",
                                            "next_hop_via": "default",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "ext_community": "RT:20.1.101.1:101 ENCAP:8 Router MAC:5C71.0DCD.F0E0",
                                            "origin_codes": "?",
                                            "status_codes": "*>",
                                            "refresh_epoch": 1,
                                            "route_info": "150",
                                            "route_status": "received & used",
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0x0"
                                        }
                                    }
                                },
                                "101.103.0.0/17": {
                                    "table_version": "5924",
                                    "available_path": "2",
                                    "best_path": "2",
                                    "paths": "2 available, best #2, table EVPN-BGP-Table",
                                    "index": {
                                        1: {
                                            "next_hop": "20.0.101.1",
                                            "gateway": "20.1.150.3",
                                            "originator": "20.1.150.3",
                                            "next_hop_via": "default",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "ext_community": "RT:20.1.101.1:101 ENCAP:8 Router MAC:5C71.0DCD.F0E0",
                                            "origin_codes": "?",
                                            "status_codes": "* ",
                                            "refresh_epoch": 1,
                                            "route_info": "150",
                                            "route_status": "received & used",
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0"
                                        },
                                        2: {
                                            "next_hop": "20.0.101.1",
                                            "gateway": "20.1.150.4",
                                            "originator": "20.1.150.4",
                                            "next_hop_via": "default",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "ext_community": "RT:20.1.101.1:101 ENCAP:8 Router MAC:5C71.0DCD.F0E0",
                                            "origin_codes": "?",
                                            "status_codes": "*>",
                                            "refresh_epoch": 1,
                                            "route_info": "150",
                                            "route_status": "received & used",
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0x0"
                                        }
                                    }
                                },
                                "101.104.0.0/17": {
                                    "table_version": "5925",
                                    "available_path": "2",
                                    "best_path": "2",
                                    "paths": "2 available, best #2, table EVPN-BGP-Table",
                                    "index": {
                                        1: {
                                            "next_hop": "20.0.101.1",
                                            "gateway": "20.1.150.3",
                                            "originator": "20.1.150.3",
                                            "next_hop_via": "default",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "ext_community": "RT:20.1.101.1:101 ENCAP:8 Router MAC:5C71.0DCD.F0E0",
                                            "origin_codes": "?",
                                            "status_codes": "* ",
                                            "refresh_epoch": 1,
                                            "route_info": "150",
                                            "route_status": "received & used",
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0"
                                        },
                                        2: {
                                            "next_hop": "20.0.101.1",
                                            "gateway": "20.1.150.4",
                                            "originator": "20.1.150.4",
                                            "next_hop_via": "default",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "ext_community": "RT:20.1.101.1:101 ENCAP:8 Router MAC:5C71.0DCD.F0E0",
                                            "origin_codes": "?",
                                            "status_codes": "*>",
                                            "refresh_epoch": 1,
                                            "route_info": "150",
                                            "route_status": "received & used",
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0x0"
                                        }
                                    }
                                },
                                "101.69.0.0/17": {
                                    "table_version": "2096",
                                    "available_path": "1",
                                    "best_path": "1",
                                    "paths": "1 available, best #1, table EVPN-BGP-Table",
                                    "index": {
                                        1: {
                                            "next_hop": "0.0.0.0",
                                            "gateway": "0.0.0.0",
                                            "originator": "30.1.107.78",
                                            "next_hop_via": "vrf vrf100",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "ext_community": "RT:30.1.107.78:100 ENCAP:8",
                                            "metric": 0,
                                            "weight": "32768",
                                            "origin_codes": "?",
                                            "status_codes": "*>",
                                            "refresh_epoch": 1,
                                            "route_info": "Local",
                                            "imported_path_from": "base",
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0x0"
                                        }
                                    }
                                },
                                "101.70.0.0/17": {
                                    "table_version": "2097",
                                    "available_path": "1",
                                    "best_path": "1",
                                    "paths": "1 available, best #1, table EVPN-BGP-Table",
                                    "index": {
                                        1: {
                                            "next_hop": "0.0.0.0",
                                            "gateway": "0.0.0.0",
                                            "originator": "30.1.107.78",
                                            "next_hop_via": "vrf vrf100",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "ext_community": "RT:30.1.107.78:100 ENCAP:8",
                                            "metric": 0,
                                            "weight": "32768",
                                            "origin_codes": "?",
                                            "status_codes": "*>",
                                            "refresh_epoch": 1,
                                            "route_info": "Local",
                                            "imported_path_from": "base",
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0x0"
                                        }
                                    }
                                },
                                "101.71.0.0/17": {
                                    "table_version": "2098",
                                    "available_path": "1",
                                    "best_path": "1",
                                    "paths": "1 available, best #1, table EVPN-BGP-Table",
                                    "index": {
                                        1: {
                                            "next_hop": "0.0.0.0",
                                            "gateway": "0.0.0.0",
                                            "originator": "30.1.107.78",
                                            "next_hop_via": "vrf vrf100",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "ext_community": "RT:30.1.107.78:100 ENCAP:8",
                                            "metric": 0,
                                            "weight": "32768",
                                            "origin_codes": "?",
                                            "status_codes": "*>",
                                            "refresh_epoch": 1,
                                            "route_info": "Local",
                                            "imported_path_from": "base",
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0x0"
                                        }
                                    }
                                },
                                "101.72.0.0/17": {
                                    "table_version": "2099",
                                    "available_path": "1",
                                    "best_path": "1",
                                    "paths": "1 available, best #1, table EVPN-BGP-Table",
                                    "index": {
                                        1: {
                                            "next_hop": "0.0.0.0",
                                            "gateway": "0.0.0.0",
                                            "originator": "30.1.107.78",
                                            "next_hop_via": "vrf vrf100",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "ext_community": "RT:30.1.107.78:100 ENCAP:8",
                                            "metric": 0,
                                            "weight": "32768",
                                            "origin_codes": "?",
                                            "status_codes": "*>",
                                            "refresh_epoch": 1,
                                            "route_info": "Local",
                                            "imported_path_from": "base",
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0x0"
                                        }
                                    }
                                },
                                "101.73.0.0/17": {
                                    "table_version": "2100",
                                    "available_path": "1",
                                    "best_path": "1",
                                    "paths": "1 available, best #1, table EVPN-BGP-Table",
                                    "index": {
                                        1: {
                                            "next_hop": "0.0.0.0",
                                            "gateway": "0.0.0.0",
                                            "originator": "30.1.107.78",
                                            "next_hop_via": "vrf vrf100",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "ext_community": "RT:30.1.107.78:100 ENCAP:8",
                                            "metric": 0,
                                            "weight": "32768",
                                            "origin_codes": "?",
                                            "status_codes": "*>",
                                            "refresh_epoch": 1,
                                            "route_info": "Local",
                                            "imported_path_from": "base",
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0x0"
                                        }
                                    }
                                },
                                "101.74.0.0/17": {
                                    "table_version": "2101",
                                    "available_path": "1",
                                    "best_path": "1",
                                    "paths": "1 available, best #1, table EVPN-BGP-Table",
                                    "index": {
                                        1: {
                                            "next_hop": "0.0.0.0",
                                            "gateway": "0.0.0.0",
                                            "originator": "30.1.107.78",
                                            "next_hop_via": "vrf vrf100",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "ext_community": "RT:30.1.107.78:100 ENCAP:8",
                                            "metric": 0,
                                            "weight": "32768",
                                            "origin_codes": "?",
                                            "status_codes": "*>",
                                            "refresh_epoch": 1,
                                            "route_info": "Local",
                                            "imported_path_from": "base",
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0x0"
                                        }
                                    }
                                },
                                "101.170.0.0/17": {
                                    "table_version": "2150",
                                    "available_path": "1",
                                    "best_path": "1",
                                    "paths": "1 available, best #1, table EVPN-BGP-Table",
                                    "index": {
                                        1: {
                                            "next_hop": "0.0.0.0",
                                            "gateway": "0.0.0.0",
                                            "originator": "30.1.107.78",
                                            "next_hop_via": "vrf vrf102",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "ext_community": "RT:30.1.107.78:102 ENCAP:8",
                                            "metric": 0,
                                            "weight": "32768",
                                            "origin_codes": "?",
                                            "status_codes": "*>",
                                            "refresh_epoch": 1,
                                            "route_info": "Local",
                                            "imported_path_from": "base",
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0x0"
                                        }
                                    }
                                },
                                "10.101.101.101/17": {
                                    "table_version": "2225",
                                    "available_path": "1",
                                    "best_path": "1",
                                    "paths": "1 available, best #1, table EVPN-BGP-Table",
                                    "index": {
                                        1: {
                                            "next_hop": "0.0.0.0",
                                            "gateway": "0.0.0.0",
                                            "originator": "30.1.107.78",
                                            "next_hop_via": "vrf vrf224",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "metric": 0,
                                            "ext_community": "RT:30.1.107.78:224 ENCAP:8",
                                            "weight": "32768",
                                            "origin_codes": "i",
                                            "status_codes": "*>",
                                            "refresh_epoch": 1,
                                            "route_info": "Local",
                                            "imported_path_from": "base",
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0x0"
                                        }
                                    }
                                },
                                "101.225.0.0/17": {
                                    "table_version": "2229",
                                    "available_path": "1",
                                    "best_path": "1",
                                    "paths": "1 available, best #1, table EVPN-BGP-Table",
                                    "index": {
                                        1: {
                                            "next_hop": "0.0.0.0",
                                            "gateway": "0.0.0.0",
                                            "originator": "30.1.107.78",
                                            "next_hop_via": "vrf vrf225",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "ext_community": "RT:30.1.107.78:225 ENCAP:8",
                                            "metric": 0,
                                            "weight": "32768",
                                            "origin_codes": "?",
                                            "status_codes": "*>",
                                            "refresh_epoch": 1,
                                            "route_info": "Local",
                                            "imported_path_from": "base",
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