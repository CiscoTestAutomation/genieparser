expected_output = {
    "instance": {
        "default": {
            "vrf": {
                "EVPN-BGP-Table": {
                    "address_family": {
                        "l2vpn evpn": {
                            "prefixes": {
                                "[2][20.0.101.1:10][0][48][188B9D501231][0][*]/20": {
                                    "table_version": "6086",
                                    "nlri_data": {
                                        "route-type": "2",
                                        "rd": "20.0.101.1:10",
                                        "eti": "0",
                                        "mac_len": "48",
                                        "mac": "188B9D501231",
                                        "ip_len": "0",
                                        "subnet": "20"
                                    },
                                    "available_path": "4",
                                    "best_path": "3",
                                    "paths": "4 available, best #3, table EVPN-BGP-Table",
                                    "index": {
                                        1: {
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
                                            "evpn": {
                                                "evpn_esi": "00000000000000000000",
                                                "label": 210010,
                                                "ext_community": "RT:23456:210010 ENCAP:8"
                                            },
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
                                            "origin_codes": "?",
                                            "status_codes": "* ",
                                            "refresh_epoch": 1,
                                            "route_info": "150",
                                            "route_status": "received-only",
                                            "evpn": {
                                                "evpn_esi": "00000000000000000000",
                                                "label": 0,
                                                "ext_community": "RT:150:210010 ENCAP:8"
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0"
                                        },
                                        3: {
                                            "next_hop": "20.0.101.1",
                                            "gateway": "20.1.150.3",
                                            "originator": "20.1.150.3",
                                            "next_hop_via": "default",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "origin_codes": "?",
                                            "status_codes": "*>",
                                            "refresh_epoch": 1,
                                            "route_info": "150",
                                            "route_status": "received-only",
                                            "evpn": {
                                                "evpn_esi": "00000000000000000000",
                                                "label": 210010,
                                                "ext_community": "RT:23456:210010 ENCAP:8"
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0x0"
                                        },
                                        4: {
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
                                            "evpn": {
                                                "evpn_esi": "00000000000000000000",
                                                "label": 0,
                                                "ext_community": "RT:150:210010 ENCAP:8"
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0"
                                        }
                                    }
                                },
                                "[2][20.0.101.1:10][0][48][188B9D508D17][0][*]/20": {
                                    "table_version": "6087",
                                    "nlri_data": {
                                        "route-type": "2",
                                        "rd": "20.0.101.1:10",
                                        "eti": "0",
                                        "mac_len": "48",
                                        "mac": "188B9D508D17",
                                        "ip_len": "0",
                                        "subnet": "20"
                                    },
                                    "available_path": "4",
                                    "best_path": "3",
                                    "paths": "4 available, best #3, table EVPN-BGP-Table",
                                    "index": {
                                        1: {
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
                                            "evpn": {
                                                "evpn_esi": "00000000000000000000",
                                                "label": 210010,
                                                "ext_community": "RT:23456:210010 ENCAP:8"
                                            },
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
                                            "origin_codes": "?",
                                            "status_codes": "* ",
                                            "refresh_epoch": 1,
                                            "route_info": "150",
                                            "route_status": "received-only",
                                            "evpn": {
                                                "evpn_esi": "00000000000000000000",
                                                "label": 0,
                                                "ext_community": "RT:150:210010 ENCAP:8"
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0"
                                        },
                                        3: {
                                            "next_hop": "20.0.101.1",
                                            "gateway": "20.1.150.3",
                                            "originator": "20.1.150.3",
                                            "next_hop_via": "default",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "origin_codes": "?",
                                            "status_codes": "*>",
                                            "refresh_epoch": 1,
                                            "route_info": "150",
                                            "route_status": "received-only",
                                            "evpn": {
                                                "evpn_esi": "00000000000000000000",
                                                "label": 210010,
                                                "ext_community": "RT:23456:210010 ENCAP:8"
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0x0"
                                        },
                                        4: {
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
                                            "evpn": {
                                                "evpn_esi": "00000000000000000000",
                                                "label": 0,
                                                "ext_community": "RT:150:210010 ENCAP:8"
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0"
                                        }
                                    }
                                },
                                "[2][20.0.101.1:51][0][48][001201000001][0][*]/20": {
                                    "table_version": "652422",
                                    "nlri_data": {
                                        "route-type": "2",
                                        "rd": "20.0.101.1:51",
                                        "eti": "0",
                                        "mac_len": "48",
                                        "mac": "001201000001",
                                        "ip_len": "0",
                                        "subnet": "20"
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
                                            "evpn": {
                                                "evpn_esi": "00000000000000000000",
                                                "label": 200051,
                                                "ext_community": "RT:23456:200051 ENCAP:8"
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
                                            "evpn": {
                                                "evpn_esi": "00000000000000000000",
                                                "label": 0,
                                                "ext_community": "RT:150:200051 ENCAP:8"
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
                                            "evpn": {
                                                "evpn_esi": "00000000000000000000",
                                                "label": 200051,
                                                "ext_community": "RT:23456:200051 ENCAP:8"
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
                                            "evpn": {
                                                "evpn_esi": "00000000000000000000",
                                                "label": 0,
                                                "ext_community": "RT:150:200051 ENCAP:8"
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0"
                                        }
                                    }
                                },
                                "[2][20.0.101.1:51][0][48][001201000001][32][101.51.1.102]/24": {
                                    "table_version": "652845",
                                    "nlri_data": {
                                        "route-type": "2",
                                        "rd": "20.0.101.1:51",
                                        "eti": "0",
                                        "mac_len": "48",
                                        "mac": "001201000001",
                                        "ip_len": "32",
                                        "ip_prefix": "101.51.1.102",
                                        "subnet": "24"
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
                                            "evpn": {
                                                "evpn_esi": "00000000000000000000",
                                                "label": 200051,
                                                "ext_community": "RT:23456:200051 ENCAP:8"
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
                                            "evpn": {
                                                "evpn_esi": "00000000000000000000",
                                                "label": 0,
                                                "ext_community": "RT:150:200051 ENCAP:8"
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
                                            "evpn": {
                                                "evpn_esi": "00000000000000000000",
                                                "label": 200051,
                                                "ext_community": "RT:23456:200051 ENCAP:8"
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
                                            "evpn": {
                                                "evpn_esi": "00000000000000000000",
                                                "label": 0,
                                                "ext_community": "RT:150:200051 ENCAP:8"
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0"
                                        }
                                    }
                                },
                                "[2][20.0.101.1:51][0][48][001701000001][0][*]/20": {
                                    "table_version": "651919",
                                    "nlri_data": {
                                        "route-type": "2",
                                        "rd": "20.0.101.1:51",
                                        "eti": "0",
                                        "mac_len": "48",
                                        "mac": "001701000001",
                                        "ip_len": "0",
                                        "subnet": "20"
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
                                            "evpn": {
                                                "evpn_esi": "00000000000000000000",
                                                "label": 200051,
                                                "ext_community": "RT:23456:200051 ENCAP:8"
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
                                            "evpn": {
                                                "evpn_esi": "00000000000000000000",
                                                "label": 0,
                                                "ext_community": "RT:150:200051 ENCAP:8"
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
                                            "evpn": {
                                                "evpn_esi": "00000000000000000000",
                                                "label": 200051,
                                                "ext_community": "RT:23456:200051 ENCAP:8"
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
                                            "evpn": {
                                                "evpn_esi": "00000000000000000000",
                                                "label": 0,
                                                "ext_community": "RT:150:200051 ENCAP:8"
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0"
                                        }
                                    }
                                },
                                "[2][20.0.101.1:53][0][48][001201000003][32][101.53.1.102]/24": {
                                    "table_version": "652847",
                                    "nlri_data": {
                                        "route-type": "2",
                                        "rd": "20.0.101.1:53",
                                        "eti": "0",
                                        "mac_len": "48",
                                        "mac": "001201000003",
                                        "ip_len": "32",
                                        "ip_prefix": "101.53.1.102",
                                        "subnet": "24"
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
                                            "evpn": {
                                                "evpn_esi": "00000000000000000000",
                                                "label": 200053,
                                                "ext_community": "RT:23456:200053 ENCAP:8"
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
                                            "evpn": {
                                                "evpn_esi": "00000000000000000000",
                                                "label": 0,
                                                "ext_community": "RT:150:200053 ENCAP:8"
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
                                            "evpn": {
                                                "evpn_esi": "00000000000000000000",
                                                "label": 200053,
                                                "ext_community": "RT:23456:200053 ENCAP:8"
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
                                            "evpn": {
                                                "evpn_esi": "00000000000000000000",
                                                "label": 0,
                                                "ext_community": "RT:150:200053 ENCAP:8"
                                            },
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