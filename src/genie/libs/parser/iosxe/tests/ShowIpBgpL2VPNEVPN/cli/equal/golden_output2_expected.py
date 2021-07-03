expected_output = {
    "instance": {
        "default": {
            "vrf": {
                "EVPN-BGP-Table": {
                    "address_family": {
                        "l2vpn evpn": {
                            "prefixes": {
                                "[3][20.0.101.1:10][0][32][20.0.101.1]/17": {
                                    "table_version": "3830",
                                    "nlri_data": {
                                        "route-type": "3",
                                        "rd": "20.0.101.1:10",
                                        "eti": "0",
                                        "ip_len": "32",
                                        "orig_rtr_id": "20.0.101.1",
                                        "subnet": "17"
                                    },
                                    "available_path": "4",
                                    "best_path": "3",
                                    "paths": "4 available, best #3, table EVPN-BGP-Table",
                                    "index": {
                                        1: {
                                            "next_hop": "20.0.101.1",
                                            "gateway": "20.1.150.3",
                                            "originator": "20.1.150.3",
                                            "next_hop_via": "default",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "origin_codes": "?",
                                            "status_codes": "* ",
                                            "refresh_epoch": 1,
                                            "route_info": "150",
                                            "ext_community": "RT:23456:210010 ENCAP:8 EVPN Mcast Flags:1",
                                            "pmsi": {
                                                "tun_type": "IR",
                                                "vni": "210010",
                                                "tun_id": {
                                                    "tun_endpoint": "20.0.101.1"
                                                }
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0"
                                        },
                                        2: {
                                            "next_hop": "20.0.101.1",
                                            "gateway": "20.1.150.3",
                                            "originator": "20.1.150.3",
                                            "next_hop_via": "default",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "origin_codes": "?",
                                            "status_codes": "* ",
                                            "refresh_epoch": 1,
                                            "route_info": "150",
                                            "route_status": "received-only",
                                            "ext_community": "RT:150:210010 ENCAP:8 EVPN Mcast Flags:1",
                                            "pmsi": {
                                                "tun_type": "IR",
                                                "vni": "210010",
                                                "tun_id": {
                                                    "tun_endpoint": "20.0.101.1"
                                                }
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0"
                                        },
                                        3: {
                                            "next_hop": "20.0.101.1",
                                            "gateway": "20.1.150.4",
                                            "originator": "20.1.150.4",
                                            "next_hop_via": "default",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "origin_codes": "?",
                                            "status_codes": "*>",
                                            "refresh_epoch": 1,
                                            "route_info": "150",
                                            "route_status": "received-only",
                                            "ext_community": "RT:23456:210010 ENCAP:8 EVPN Mcast Flags:1",
                                            "pmsi": {
                                                "tun_type": "IR",
                                                "vni": "210010",
                                                "tun_id": {
                                                    "tun_endpoint": "20.0.101.1"
                                                }
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0x0"
                                        },
                                        4: {
                                            "next_hop": "20.0.101.1",
                                            "gateway": "20.1.150.4",
                                            "originator": "20.1.150.4",
                                            "next_hop_via": "default",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "origin_codes": "?",
                                            "status_codes": "* ",
                                            "refresh_epoch": 1,
                                            "route_info": "150",
                                            "route_status": "received-only",
                                            "ext_community": "RT:150:210010 ENCAP:8 EVPN Mcast Flags:1",
                                            "pmsi": {
                                                "tun_type": "IR",
                                                "vni": "210010",
                                                "tun_id": {
                                                    "tun_endpoint": "20.0.101.1"
                                                }
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0"
                                        }
                                    }
                                },
                                "[3][20.0.101.1:51][0][32][20.0.101.1]/17": {
                                    "table_version": "4074",
                                    "nlri_data": {
                                        "route-type": "3",
                                        "rd": "20.0.101.1:51",
                                        "eti": "0",
                                        "ip_len": "32",
                                        "orig_rtr_id": "20.0.101.1",
                                        "subnet": "17"
                                    },
                                    "available_path": "4",
                                    "best_path": "3",
                                    "paths": "4 available, best #3, table EVPN-BGP-Table",
                                    "index": {
                                        1: {
                                            "next_hop": "20.0.101.1",
                                            "gateway": "20.1.150.3",
                                            "originator": "20.1.150.3",
                                            "next_hop_via": "default",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "origin_codes": "?",
                                            "status_codes": "* ",
                                            "refresh_epoch": 1,
                                            "route_info": "150",
                                            "route_status": "received-only",
                                            "ext_community": "RT:23456:200051 ENCAP:8 EVPN Mcast Flags:1",
                                            "pmsi": {
                                                "tun_type": "IR",
                                                "vni": "200051",
                                                "tun_id": {
                                                    "tun_endpoint": "20.0.101.1"
                                                }
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0"
                                        },
                                        2: {
                                            "next_hop": "20.0.101.1",
                                            "gateway": "20.1.150.3",
                                            "originator": "20.1.150.3",
                                            "next_hop_via": "default",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "origin_codes": "?",
                                            "status_codes": "* ",
                                            "refresh_epoch": 1,
                                            "route_info": "150",
                                            "route_status": "received-only",
                                            "ext_community": "RT:150:200051 ENCAP:8 EVPN Mcast Flags:1",
                                            "pmsi": {
                                                "tun_type": "IR",
                                                "vni": "200051",
                                                "tun_id": {
                                                    "tun_endpoint": "20.0.101.1"
                                                }
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0"
                                        },
                                        3: {
                                            "next_hop": "20.0.101.1",
                                            "gateway": "20.1.150.4",
                                            "originator": "20.1.150.4",
                                            "next_hop_via": "default",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "origin_codes": "?",
                                            "status_codes": "*>",
                                            "refresh_epoch": 1,
                                            "route_info": "150",
                                            "route_status": "received-only",
                                            "ext_community": "RT:23456:200051 ENCAP:8 EVPN Mcast Flags:1",
                                            "pmsi": {
                                                "tun_type": "IR",
                                                "vni": "200051",
                                                "tun_id": {
                                                    "tun_endpoint": "20.0.101.1"
                                                }
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0x0"
                                        },
                                        4: {
                                            "next_hop": "20.0.101.1",
                                            "gateway": "20.1.150.4",
                                            "originator": "20.1.150.4",
                                            "next_hop_via": "default",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "origin_codes": "?",
                                            "status_codes": "* ",
                                            "refresh_epoch": 1,
                                            "route_info": "150",
                                            "route_status": "received-only",
                                            "ext_community": "RT:150:200051 ENCAP:8 EVPN Mcast Flags:1",
                                            "pmsi": {
                                                "tun_type": "IR",
                                                "vni": "200051",
                                                "tun_id": {
                                                    "tun_endpoint": "20.0.101.1"
                                                }
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0"
                                        }
                                    }
                                },
                                "[3][20.0.101.1:52][0][32][20.0.101.1]/17": {
                                    "table_version": "4075",
                                    "nlri_data": {
                                        "route-type": "3",
                                        "rd": "20.0.101.1:52",
                                        "eti": "0",
                                        "ip_len": "32",
                                        "orig_rtr_id": "20.0.101.1",
                                        "subnet": "17"
                                    },
                                    "available_path": "4",
                                    "best_path": "3",
                                    "paths": "4 available, best #3, table EVPN-BGP-Table",
                                    "index": {
                                        1: {
                                            "next_hop": "20.0.101.1",
                                            "gateway": "20.1.150.3",
                                            "originator": "20.1.150.3",
                                            "next_hop_via": "default",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "origin_codes": "?",
                                            "status_codes": "* ",
                                            "refresh_epoch": 1,
                                            "route_info": "150",
                                            "route_status": "received-only",
                                            "ext_community": "RT:23456:200052 ENCAP:8 EVPN Mcast Flags:1",
                                            "pmsi": {
                                                "tun_type": "IR",
                                                "vni": "200052",
                                                "tun_id": {
                                                    "tun_endpoint": "20.0.101.1"
                                                }
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0"
                                        },
                                        2: {
                                            "next_hop": "20.0.101.1",
                                            "gateway": "20.1.150.3",
                                            "originator": "20.1.150.3",
                                            "next_hop_via": "default",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "origin_codes": "?",
                                            "status_codes": "* ",
                                            "refresh_epoch": 1,
                                            "route_info": "150",
                                            "route_status": "received-only",
                                            "ext_community": "RT:150:200052 ENCAP:8 EVPN Mcast Flags:1",
                                            "pmsi": {
                                                "tun_type": "IR",
                                                "vni": "200052",
                                                "tun_id": {
                                                    "tun_endpoint": "20.0.101.1"
                                                }
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0"
                                        },
                                        3: {
                                            "next_hop": "20.0.101.1",
                                            "gateway": "20.1.150.4",
                                            "originator": "20.1.150.4",
                                            "next_hop_via": "default",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "origin_codes": "?",
                                            "status_codes": "*>",
                                            "refresh_epoch": 1,
                                            "route_info": "150",
                                            "route_status": "received-only",
                                            "ext_community": "RT:23456:200052 ENCAP:8 EVPN Mcast Flags:1",
                                            "pmsi": {
                                                "tun_type": "IR",
                                                "vni": "200052",
                                                "tun_id": {
                                                    "tun_endpoint": "20.0.101.1"
                                                }
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0x0"
                                        },
                                        4: {
                                            "next_hop": "20.0.101.1",
                                            "gateway": "20.1.150.4",
                                            "originator": "20.1.150.4",
                                            "next_hop_via": "default",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "origin_codes": "?",
                                            "status_codes": "* ",
                                            "refresh_epoch": 1,
                                            "route_info": "150",
                                            "route_status": "received-only",
                                            "ext_community": "RT:150:200052 ENCAP:8 EVPN Mcast Flags:1",
                                            "pmsi": {
                                                "tun_type": "IR",
                                                "vni": "200052",
                                                "tun_id": {
                                                    "tun_endpoint": "20.0.101.1"
                                                }
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0"
                                        }
                                    }
                                },
                                "[3][20.0.101.1:53][0][32][20.0.101.1]/17": {
                                    "table_version": "4076",
                                    "nlri_data": {
                                        "route-type": "3",
                                        "rd": "20.0.101.1:53",
                                        "eti": "0",
                                        "ip_len": "32",
                                        "orig_rtr_id": "20.0.101.1",
                                        "subnet": "17"
                                    },
                                    "available_path": "4",
                                    "best_path": "3",
                                    "paths": "4 available, best #3, table EVPN-BGP-Table",
                                    "index": {
                                        1: {
                                            "next_hop": "20.0.101.1",
                                            "gateway": "20.1.150.3",
                                            "originator": "20.1.150.3",
                                            "next_hop_via": "default",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "origin_codes": "?",
                                            "status_codes": "* ",
                                            "refresh_epoch": 1,
                                            "route_info": "150",
                                            "route_status": "received-only",
                                            "ext_community": "RT:23456:200053 ENCAP:8 EVPN Mcast Flags:1",
                                            "pmsi": {
                                                "tun_type": "IR",
                                                "vni": "200053",
                                                "tun_id": {
                                                    "tun_endpoint": "20.0.101.1"
                                                }
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0"
                                        },
                                        2: {
                                            "next_hop": "20.0.101.1",
                                            "gateway": "20.1.150.3",
                                            "originator": "20.1.150.3",
                                            "next_hop_via": "default",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "origin_codes": "?",
                                            "status_codes": "* ",
                                            "refresh_epoch": 1,
                                            "route_info": "150",
                                            "route_status": "received-only",
                                            "ext_community": "RT:150:200053 ENCAP:8 EVPN Mcast Flags:1",
                                            "pmsi": {
                                                "tun_type": "IR",
                                                "vni": "200053",
                                                "tun_id": {
                                                    "tun_endpoint": "20.0.101.1"
                                                }
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0"
                                        },
                                        3: {
                                            "next_hop": "20.0.101.1",
                                            "gateway": "20.1.150.4",
                                            "originator": "20.1.150.4",
                                            "next_hop_via": "default",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "origin_codes": "?",
                                            "status_codes": "*>",
                                            "refresh_epoch": 1,
                                            "route_info": "150",
                                            "route_status": "received-only",
                                            "ext_community": "RT:23456:200053 ENCAP:8 EVPN Mcast Flags:1",
                                            "pmsi": {
                                                "tun_type": "IR",
                                                "vni": "200053",
                                                "tun_id": {
                                                    "tun_endpoint": "20.0.101.1"
                                                }
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0x0"
                                        },
                                        4: {
                                            "next_hop": "20.0.101.1",
                                            "gateway": "20.1.150.4",
                                            "originator": "20.1.150.4",
                                            "next_hop_via": "default",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "origin_codes": "?",
                                            "status_codes": "* ",
                                            "refresh_epoch": 1,
                                            "route_info": "150",
                                            "route_status": "received-only",
                                            "ext_community": "RT:150:200053 ENCAP:8 EVPN Mcast Flags:1",
                                            "pmsi": {
                                                "tun_type": "IR",
                                                "vni": "200053",
                                                "tun_id": {
                                                    "tun_endpoint": "20.0.101.1"
                                                }
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0"
                                        }
                                    }
                                },
                                "[3][20.0.101.1:54][0][32][20.0.101.1]/17": {
                                    "table_version": "4077",
                                    "nlri_data": {
                                        "route-type": "3",
                                        "rd": "20.0.101.1:54",
                                        "eti": "0",
                                        "ip_len": "32",
                                        "orig_rtr_id": "20.0.101.1",
                                        "subnet": "17"
                                    },
                                    "available_path": "4",
                                    "best_path": "3",
                                    "paths": "4 available, best #3, table EVPN-BGP-Table",
                                    "index": {
                                        1: {
                                            "next_hop": "20.0.101.1",
                                            "gateway": "20.1.150.3",
                                            "originator": "20.1.150.3",
                                            "next_hop_via": "default",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "origin_codes": "?",
                                            "status_codes": "* ",
                                            "refresh_epoch": 1,
                                            "route_info": "150",
                                            "route_status": "received-only",
                                            "ext_community": "RT:23456:200054 ENCAP:8 EVPN Mcast Flags:1",
                                            "pmsi": {
                                                "tun_type": "IR",
                                                "vni": "200054",
                                                "tun_id": {
                                                    "tun_endpoint": "20.0.101.1"
                                                }
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0"
                                        },
                                        2: {
                                            "next_hop": "20.0.101.1",
                                            "gateway": "20.1.150.3",
                                            "originator": "20.1.150.3",
                                            "next_hop_via": "default",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "origin_codes": "?",
                                            "status_codes": "* ",
                                            "refresh_epoch": 1,
                                            "route_info": "150",
                                            "route_status": "received-only",
                                            "ext_community": "RT:150:200054 ENCAP:8 EVPN Mcast Flags:1",
                                            "pmsi": {
                                                "tun_type": "IR",
                                                "vni": "200054",
                                                "tun_id": {
                                                    "tun_endpoint": "20.0.101.1"
                                                }
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0"
                                        },
                                        3: {
                                            "next_hop": "20.0.101.1",
                                            "gateway": "20.1.150.4",
                                            "originator": "20.1.150.4",
                                            "next_hop_via": "default",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "origin_codes": "?",
                                            "status_codes": "*>",
                                            "refresh_epoch": 1,
                                            "route_info": "150",
                                            "route_status": "received-only",
                                            "ext_community": "RT:23456:200054 ENCAP:8 EVPN Mcast Flags:1",
                                            "pmsi": {
                                                "tun_type": "IR",
                                                "vni": "200054",
                                                "tun_id": {
                                                    "tun_endpoint": "20.0.101.1"
                                                }
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0x0"
                                        },
                                        4: {
                                            "next_hop": "20.0.101.1",
                                            "gateway": "20.1.150.4",
                                            "originator": "20.1.150.4",
                                            "next_hop_via": "default",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "origin_codes": "?",
                                            "status_codes": "* ",
                                            "refresh_epoch": 1,
                                            "route_info": "150",
                                            "route_status": "received-only",
                                            "ext_community": "RT:150:200054 ENCAP:8 EVPN Mcast Flags:1",
                                            "pmsi": {
                                                "tun_type": "IR",
                                                "vni": "200054",
                                                "tun_id": {
                                                    "tun_endpoint": "20.0.101.1"
                                                }
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0"
                                        }
                                    }
                                },
                                "[3][20.0.101.1:64][0][32][20.0.101.1]/17": {
                                    "table_version": "4087",
                                    "nlri_data": {
                                        "route-type": "3",
                                        "rd": "20.0.101.1:64",
                                        "eti": "0",
                                        "ip_len": "32",
                                        "orig_rtr_id": "20.0.101.1",
                                        "subnet": "17"
                                    },
                                    "available_path": "4",
                                    "best_path": "3",
                                    "paths": "4 available, best #3, table EVPN-BGP-Table",
                                    "index": {
                                        1: {
                                            "next_hop": "20.0.101.1",
                                            "gateway": "20.1.150.3",
                                            "originator": "20.1.150.3",
                                            "next_hop_via": "default",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "origin_codes": "?",
                                            "status_codes": "* ",
                                            "refresh_epoch": 1,
                                            "route_info": "150",
                                            "route_status": "received-only",
                                            "ext_community": "RT:23456:200064 ENCAP:8 EVPN Mcast Flags:1",
                                            "pmsi": {
                                                "tun_type": "IR",
                                                "vni": "200064",
                                                "tun_id": {
                                                    "tun_endpoint": "20.0.101.1"
                                                }
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0"
                                        },
                                        2: {
                                            "next_hop": "20.0.101.1",
                                            "gateway": "20.1.150.3",
                                            "originator": "20.1.150.3",
                                            "next_hop_via": "default",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "origin_codes": "?",
                                            "status_codes": "* ",
                                            "refresh_epoch": 1,
                                            "route_info": "150",
                                            "route_status": "received-only",
                                            "ext_community": "RT:150:200064 ENCAP:8 EVPN Mcast Flags:1",
                                            "pmsi": {
                                                "tun_type": "IR",
                                                "vni": "200064",
                                                "tun_id": {
                                                    "tun_endpoint": "20.0.101.1"
                                                }
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0"
                                        },
                                        3: {
                                            "next_hop": "20.0.101.1",
                                            "gateway": "20.1.150.4",
                                            "originator": "20.1.150.4",
                                            "next_hop_via": "default",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "origin_codes": "?",
                                            "status_codes": "*>",
                                            "refresh_epoch": 1,
                                            "route_info": "150",
                                            "route_status": "received-only",
                                            "ext_community": "RT:23456:200064 ENCAP:8 EVPN Mcast Flags:1",
                                            "pmsi": {
                                                "tun_type": "IR",
                                                "vni": "200064",
                                                "tun_id": {
                                                    "tun_endpoint": "20.0.101.1"
                                                }
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0x0"
                                        },
                                        4: {
                                            "next_hop": "20.0.101.1",
                                            "gateway": "20.1.150.4",
                                            "originator": "20.1.150.4",
                                            "next_hop_via": "default",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "origin_codes": "?",
                                            "status_codes": "* ",
                                            "refresh_epoch": 1,
                                            "route_info": "150",
                                            "route_status": "received-only",
                                            "ext_community": "RT:150:200064 ENCAP:8 EVPN Mcast Flags:1",
                                            "pmsi": {
                                                "tun_type": "IR",
                                                "vni": "200064",
                                                "tun_id": {
                                                    "tun_endpoint": "20.0.101.1"
                                                }
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0"
                                        }
                                    }
                                },
                                "[3][20.0.101.1:69][0][32][20.0.101.1]/17": {
                                    "table_version": "4092",
                                    "nlri_data": {
                                        "route-type": "3",
                                        "rd": "20.0.101.1:69",
                                        "eti": "0",
                                        "ip_len": "32",
                                        "orig_rtr_id": "20.0.101.1",
                                        "subnet": "17"
                                    },
                                    "available_path": "4",
                                    "best_path": "3",
                                    "paths": "4 available, best #3, table EVPN-BGP-Table",
                                    "index": {
                                        1: {
                                            "next_hop": "20.0.101.1",
                                            "gateway": "20.1.150.3",
                                            "originator": "20.1.150.3",
                                            "next_hop_via": "default",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "origin_codes": "?",
                                            "status_codes": "* ",
                                            "refresh_epoch": 1,
                                            "route_info": "150",
                                            "route_status": "received-only",
                                            "ext_community": "RT:23456:200069 ENCAP:8 EVPN Mcast Flags:1",
                                            "pmsi": {
                                                "tun_type": "IR",
                                                "vni": "200069",
                                                "tun_id": {
                                                    "tun_endpoint": "20.0.101.1"
                                                }
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0"
                                        },
                                        2: {
                                            "next_hop": "20.0.101.1",
                                            "gateway": "20.1.150.3",
                                            "originator": "20.1.150.3",
                                            "next_hop_via": "default",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "origin_codes": "?",
                                            "status_codes": "* ",
                                            "refresh_epoch": 1,
                                            "route_info": "150",
                                            "route_status": "received-only",
                                            "ext_community": "RT:150:200069 ENCAP:8 EVPN Mcast Flags:1",
                                            "pmsi": {
                                                "tun_type": "IR",
                                                "vni": "200069",
                                                "tun_id": {
                                                    "tun_endpoint": "20.0.101.1"
                                                }
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0"
                                        },
                                        3: {
                                            "next_hop": "20.0.101.1",
                                            "gateway": "20.1.150.4",
                                            "originator": "20.1.150.4",
                                            "next_hop_via": "default",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "origin_codes": "?",
                                            "status_codes": "*>",
                                            "refresh_epoch": 1,
                                            "route_info": "150",
                                            "route_status": "received-only",
                                            "ext_community": "RT:23456:200069 ENCAP:8 EVPN Mcast Flags:1",
                                            "pmsi": {
                                                "tun_type": "IR",
                                                "vni": "200069",
                                                "tun_id": {
                                                    "tun_endpoint": "20.0.101.1"
                                                }
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0x0"
                                        },
                                        4: {
                                            "next_hop": "20.0.101.1",
                                            "gateway": "20.1.150.4",
                                            "originator": "20.1.150.4",
                                            "next_hop_via": "default",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "origin_codes": "?",
                                            "status_codes": "* ",
                                            "refresh_epoch": 1,
                                            "route_info": "150",
                                            "route_status": "received-only",
                                            "ext_community": "RT:150:200069 ENCAP:8 EVPN Mcast Flags:1",
                                            "pmsi": {
                                                "tun_type": "IR",
                                                "vni": "200069",
                                                "tun_id": {
                                                    "tun_endpoint": "20.0.101.1"
                                                }
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0"
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                "evi_184": {
                    "address_family": {
                        "l2vpn evpn": {
                            "prefixes": {
                                "[3][30.0.107.78:184][0][32][20.0.101.1]/17": {
                                    "table_version": "4420",
                                    "nlri_data": {
                                        "route-type": "3",
                                        "rd": "30.0.107.78:184",
                                        "eti": "0",
                                        "ip_len": "32",
                                        "orig_rtr_id": "20.0.101.1",
                                        "subnet": "17"
                                    },
                                    "available_path": "1",
                                    "best_path": "1",
                                    "paths": "1 available, best #1, table evi_184",
                                    "index": {
                                        1: {
                                            "next_hop": "20.0.101.1",
                                            "gateway": "20.1.150.4",
                                            "originator": "20.1.150.4",
                                            "next_hop_via": "default",
                                            "localpref": 100,
                                            "origin_codes": "?",
                                            "status_codes": "*>",
                                            "refresh_epoch": 1,
                                            "route_info": "150",
                                            "imported_path_from": "[3][20.0.101.1:184][0][32][20.0.101.1]/17 (global)",
                                            "ext_community": "RT:23456:2000184 ENCAP:8 EVPN Mcast Flags:1",
                                            "pmsi": {
                                                "tun_type": "IR",
                                                "vni": "2000184",
                                                "tun_id": {
                                                    "tun_endpoint": "20.0.101.1"
                                                }
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0x0"
                                        }
                                    }
                                },
                                "[3][30.0.107.78:184][0][32][20.0.101.2]/17": {
                                    "table_version": "3510",
                                    "nlri_data": {
                                        "route-type": "3",
                                        "rd": "30.0.107.78:184",
                                        "eti": "0",
                                        "ip_len": "32",
                                        "orig_rtr_id": "20.0.101.2",
                                        "subnet": "17"
                                    },
                                    "available_path": "1",
                                    "best_path": "1",
                                    "paths": "1 available, best #1, table evi_184",
                                    "index": {
                                        1: {
                                            "next_hop": "20.0.101.2",
                                            "gateway": "20.1.150.4",
                                            "originator": "20.1.150.4",
                                            "next_hop_via": "default",
                                            "localpref": 100,
                                            "origin_codes": "?",
                                            "status_codes": "*>",
                                            "refresh_epoch": 1,
                                            "route_info": "150",
                                            "imported_path_from": "[3][20.0.101.2:184][0][32][20.0.101.2]/17 (global)",
                                            "ext_community": "RT:23456:2000184 ENCAP:8 EVPN Mcast Flags:1",
                                            "pmsi": {
                                                "tun_type": "IR",
                                                "vni": "2000184",
                                                "tun_id": {
                                                    "tun_endpoint": "20.0.101.2"
                                                }
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0x0"
                                        }
                                    }
                                },
                                "[3][30.0.107.78:184][0][32][20.0.101.3]/17": {
                                    "table_version": "2825",
                                    "nlri_data": {
                                        "route-type": "3",
                                        "rd": "30.0.107.78:184",
                                        "eti": "0",
                                        "ip_len": "32",
                                        "orig_rtr_id": "20.0.101.3",
                                        "subnet": "17"
                                    },
                                    "available_path": "1",
                                    "best_path": "1",
                                    "paths": "1 available, best #1, table evi_184",
                                    "index": {
                                        1: {
                                            "next_hop": "20.0.101.3",
                                            "gateway": "20.1.150.4",
                                            "originator": "20.1.150.4",
                                            "next_hop_via": "default",
                                            "localpref": 100,
                                            "origin_codes": "?",
                                            "status_codes": "*>",
                                            "refresh_epoch": 1,
                                            "route_info": "150",
                                            "imported_path_from": "[3][20.0.101.3:184][0][32][20.0.101.3]/17 (global)",
                                            "ext_community": "RT:23456:2000184 ENCAP:8 EVPN Mcast Flags:1",
                                            "pmsi": {
                                                "tun_type": "IR",
                                                "vni": "2000184",
                                                "tun_id": {
                                                    "tun_endpoint": "20.0.101.3"
                                                }
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0x0"
                                        }
                                    }
                                },
                                "[3][30.0.107.78:184][0][32][20.0.101.4]/17": {
                                    "table_version": "5600",
                                    "nlri_data": {
                                        "route-type": "3",
                                        "rd": "30.0.107.78:184",
                                        "eti": "0",
                                        "ip_len": "32",
                                        "orig_rtr_id": "20.0.101.4",
                                        "subnet": "17"
                                    },
                                    "available_path": "1",
                                    "best_path": "1",
                                    "paths": "1 available, best #1, table evi_184",
                                    "index": {
                                        1: {
                                            "next_hop": "20.0.101.4",
                                            "gateway": "20.1.150.4",
                                            "originator": "20.1.150.4",
                                            "next_hop_via": "default",
                                            "localpref": 100,
                                            "origin_codes": "?",
                                            "status_codes": "*>",
                                            "refresh_epoch": 1,
                                            "route_info": "150",
                                            "imported_path_from": "[3][20.0.101.4:184][0][32][20.0.101.4]/17 (global)",
                                            "ext_community": "RT:23456:2000184 ENCAP:8 EVPN Mcast Flags:1",
                                            "pmsi": {
                                                "tun_type": "IR",
                                                "vni": "2000184",
                                                "tun_id": {
                                                    "tun_endpoint": "20.0.101.4"
                                                }
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