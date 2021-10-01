expected_output = {
    "instance": {
        "default": {
            "vrf": {
                "EVPN-BGP-Table": {
                    "address_family": {
                        "l2vpn evpn": {
                            "prefixes": {
                                "[6][20.0.101.1:51][0][32][15.10.10.1][32][225.0.0.51][32][20.0.101.1]/27": {
                                    "table_version": "652975",
                                    "nlri_data": {
                                        "route-type": "6",
                                        "rd": "20.0.101.1:51",
                                        "eti": "0",
                                        "mcast_src_len": "32",
                                        "mcast_src": "15.10.10.1",
                                        "mcast_group_len": "32",
                                        "mcast_group_addr": "225.0.0.51",
                                        "orig_rtr_len": "32",
                                        "orig_rtr_id": "20.0.101.1",
                                        "subnet": "27"
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
                                            "igmpmld": {
                                                "version": "v3",
                                                "filter_mode": "exclude"
                                            },
                                            "ext_community": "RT:23456:200051 ENCAP:8",
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
                                            "ext_community": "RT:150:200051 ENCAP:8",
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
                                            "igmpmld": {
                                                "version": "v3",
                                                "filter_mode": "exclude"
                                            },
                                            "ext_community": "RT:23456:200051 ENCAP:8",
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
                                            "ext_community": "RT:150:200051 ENCAP:8",
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0"
                                        }
                                    }
                                },
                                "[6][20.0.101.1:76][0][32][15.10.10.26][32][225.0.0.76][32][20.0.101.1]/27": {
                                    "table_version": "652976",
                                    "nlri_data": {
                                        "route-type": "6",
                                        "rd": "20.0.101.1:76",
                                        "eti": "0",
                                        "mcast_src_len": "32",
                                        "mcast_src": "15.10.10.26",
                                        "mcast_group_len": "32",
                                        "mcast_group_addr": "225.0.0.76",
                                        "orig_rtr_len": "32",
                                        "orig_rtr_id": "20.0.101.1",
                                        "subnet": "27"
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
                                            "igmpmld": {
                                                "version": "v3",
                                                "filter_mode": "exclude"
                                            },
                                            "ext_community": "RT:23456:200076 ENCAP:8",
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
                                            "ext_community": "RT:150:200076 ENCAP:8",
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
                                            "igmpmld": {
                                                "version": "v3",
                                                "filter_mode": "exclude"
                                            },
                                            "ext_community": "RT:23456:200076 ENCAP:8",
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
                                            "ext_community": "RT:150:200076 ENCAP:8",
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0"
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                "evi_60": {
                    "address_family": {
                        "l2vpn evpn": {
                            "prefixes": {
                                "[6][30.0.107.78:60][0][0][*][0][*][32][30.0.107.78]/19": {
                                    "table_version": "1515",
                                    "nlri_data": {
                                        "route-type": "6",
                                        "rd": "30.0.107.78:60",
                                        "eti": "0",
                                        "mcast_src_len": "0",
                                        "mcast_src": "*",
                                        "mcast_group_len": "0",
                                        "mcast_group_addr": "*",
                                        "orig_rtr_len": "32",
                                        "orig_rtr_id": "30.0.107.78",
                                        "subnet": "19"
                                    },
                                    "available_path": "1",
                                    "best_path": "1",
                                    "paths": "1 available, best #1, table evi_60",
                                    "index": {
                                        1: {
                                            "next_hop": "::",
                                            "gateway": "0.0.0.0",
                                            "originator": "30.1.107.78",
                                            "next_hop_via": "default",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "weight": "32768",
                                            "origin_codes": "?",
                                            "status_codes": "*>",
                                            "refresh_epoch": 1,
                                            "route_info": "Local",
                                            "route_status": "received-only",
                                            "ext_community": "RT:23456:200060 ENCAP:8",
                                            "local_vxlan_vtep": {
                                                "vrf": "vrf100",
                                                "vni": "3000100",
                                                "local_router_mac": "AC3A.6767.049F",
                                                "vtep_ip": "30.0.107.78"
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0x0"
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                "evi_61": {
                    "address_family": {
                        "l2vpn evpn": {
                            "prefixes": {
                                "[6][30.0.107.78:61][0][0][*][0][*][32][30.0.107.78]/19": {
                                    "table_version": "1573",
                                    "nlri_data": {
                                        "route-type": "6",
                                        "rd": "30.0.107.78:61",
                                        "eti": "0",
                                        "mcast_src_len": "0",
                                        "mcast_src": "*",
                                        "mcast_group_len": "0",
                                        "mcast_group_addr": "*",
                                        "orig_rtr_len": "32",
                                        "orig_rtr_id": "30.0.107.78",
                                        "subnet": "19"
                                    },
                                    "available_path": "1",
                                    "best_path": "1",
                                    "paths": "1 available, best #1, table evi_61",
                                    "index": {
                                        1: {
                                            "next_hop": "::",
                                            "gateway": "0.0.0.0",
                                            "originator": "30.1.107.78",
                                            "next_hop_via": "default",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "weight": "32768",
                                            "origin_codes": "?",
                                            "status_codes": "*>",
                                            "refresh_epoch": 1,
                                            "route_info": "Local",
                                            "route_status": "received-only",
                                            "ext_community": "RT:23456:200061 ENCAP:8",
                                            "local_vxlan_vtep": {
                                                "vrf": "vrf100",
                                                "vni": "3000100",
                                                "local_router_mac": "AC3A.6767.049F",
                                                "vtep_ip": "30.0.107.78"
                                            },
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0x0"
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                "evi_78": {
                    "address_family": {
                        "l2vpn evpn": {
                            "prefixes": {
                                "[6][30.0.107.78:78][0][32][15.10.10.28][32][225.0.0.78][32][20.0.101.1]/27": {
                                    "table_version": "655375",
                                    "nlri_data": {
                                        "route-type": "6",
                                        "rd": "30.0.107.78:78",
                                        "eti": "0",
                                        "mcast_src_len": "32",
                                        "mcast_src": "15.10.10.28",
                                        "mcast_group_len": "32",
                                        "mcast_group_addr": "225.0.0.78",
                                        "orig_rtr_len": "32",
                                        "orig_rtr_id": "20.0.101.1",
                                        "subnet": "27"
                                    },
                                    "available_path": "1",
                                    "best_path": "1",
                                    "paths": "1 available, best #1, table evi_78",
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
                                            "imported_path_from": "[6][20.0.101.1:78][0][32][15.10.10.28][32][225.0.0.78][32][20.0.101.1]/27 (global)",
                                            "igmpmld": {
                                                "version": "v3",
                                                "filter_mode": "exclude"
                                            },
                                            "ext_community": "RT:23456:200078 ENCAP:8",
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0x0"
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                "evi_79": {
                    "address_family": {
                        "l2vpn evpn": {
                            "prefixes": {
                                "[6][30.0.107.78:79][0][0][*][32][225.0.0.79][32][20.0.101.2]/23": {
                                    "table_version": "655452",
                                    "nlri_data": {
                                        "route-type": "6",
                                        "rd": "30.0.107.78:79",
                                        "eti": "0",
                                        "mcast_src_len": "0",
                                        "mcast_src": "*",
                                        "mcast_group_len": "32",
                                        "mcast_group_addr": "225.0.0.79",
                                        "orig_rtr_len": "32",
                                        "orig_rtr_id": "20.0.101.2",
                                        "subnet": "23"
                                    },
                                    "available_path": "1",
                                    "best_path": "1",
                                    "paths": "1 available, best #1, table evi_79",
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
                                            "route_info": "Updated on Jun 7 2021 16:17:01 UTC",
                                            "imported_path_from": "[6][20.0.101.1:78][0][32][15.10.10.28][32][225.0.0.78][32][20.0.101.1]/27 (global)",
                                            "igmpmld": {
                                                "version": "v2"
                                            },
                                            "ext_community": "RT:23456:200079 ENCAP:8",
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0x0"
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                "evi_93": {
                    "address_family": {
                        "l2vpn evpn": {
                            "prefixes": {
                                "[6][30.0.107.78:93][0][0][*][32][225.0.0.93][32][20.0.101.2]/23": {
                                    "table_version": "655466",
                                    "nlri_data": {
                                        "route-type": "6",
                                        "rd": "30.0.107.78:93",
                                        "eti": "0",
                                        "mcast_src_len": "0",
                                        "mcast_src": "*",
                                        "mcast_group_len": "32",
                                        "mcast_group_addr": "225.0.0.93",
                                        "orig_rtr_len": "32",
                                        "orig_rtr_id": "20.0.101.2",
                                        "subnet": "23"
                                    },
                                    "available_path": "1",
                                    "best_path": "1",
                                    "paths": "1 available, best #1, table evi_93",
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
                                            "route_info": "Updated on Jun 7 2021 16:17:01 UTC",
                                            "imported_path_from": "[6][20.0.101.1:78][0][32][15.10.10.28][32][225.0.0.78][32][20.0.101.1]/27 (global)",
                                            "igmpmld": {
                                                "version": "v2"
                                            },
                                            "ext_community": "RT:23456:200093 ENCAP:8",
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