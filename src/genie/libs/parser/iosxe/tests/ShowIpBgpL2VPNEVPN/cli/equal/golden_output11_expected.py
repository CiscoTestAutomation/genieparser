expected_output = {
    "instance": {
        "default": {
            "vrf": {
                "evi_5": {
                    "address_family": {
                        "l2vpn evpn": {
                            "prefixes": {
                                "[6][2.2.2.2:5][0][0][*][32][239.1.105.1][32][1.1.1.3]/23": {
                                    "table_version": "20",
                                    "nlri_data": {
                                        "route-type": "6",
                                        "rd": "2.2.2.2:5",
                                        "eti": "0",
                                        "mcast_src_len": "0",
                                        "mcast_src": "*",
                                        "mcast_group_len": "32",
                                        "mcast_group_addr": "239.1.105.1",
                                        "orig_rtr_len": "32",
                                        "orig_rtr_id": "1.1.1.3",
                                        "subnet": "23"
                                    },
                                    "available_path": "1",
                                    "best_path": "1",
                                    "paths": "1 available, best #1, table evi_5",
                                    "index": {
                                        1: {
                                            "next_hop": "1.1.1.3",
                                            "gateway": "98.98.98.98",
                                            "originator": "98.98.98.98",
                                            "next_hop_igp_metric": "21",
                                            "next_hop_via": "default",
                                            "localpref": 100,
                                            "metric": 0,
                                            "origin_codes": "?",
                                            "status_codes": "*>",
                                            "refresh_epoch": 1,
                                            "route_info": "show ip bgp l2vpn evpn evi 5 route-type 6",
                                            "igmpmld": {
                                                "version": "v2"
                                            },
                                            "ext_community": "RT:1:5 ENCAP:8",
                                            "cluster_list": "98.98.98.98",
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0x0"
                                        }
                                    }
                                },
                                "[6][2.2.2.2:5][0][32][192.168.105.111][32][239.1.105.1][32][2.2.2.3]/27": {
                                    "table_version": "15",
                                    "nlri_data": {
                                        "route-type": "6",
                                        "rd": "2.2.2.2:5",
                                        "eti": "0",
                                        "mcast_src_len": "32",
                                        "mcast_src": "192.168.105.111",
                                        "mcast_group_len": "32",
                                        "mcast_group_addr": "239.1.105.1",
                                        "orig_rtr_len": "32",
                                        "orig_rtr_id": "2.2.2.3",
                                        "subnet": "27"
                                    },
                                    "available_path": "1",
                                    "best_path": "1",
                                    "paths": "1 available, best #1, table evi_5",
                                    "index": {
                                        1: {
                                            "next_hop": "::",
                                            "gateway": "0.0.0.0",
                                            "originator": "2.2.2.3",
                                            "next_hop_via": "default",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "weight": "32768",
                                            "origin_codes": "?",
                                            "status_codes": "*>",
                                            "refresh_epoch": 1,
                                            "route_info": "Local",
                                            "igmpmld": {
                                                "version": "v3"
                                            },
                                            "ext_community": "RT:1:5 ENCAP:8",
                                            "local_vxlan_vtep": {
                                                "local_router_mac": "0000.0000.0000",
                                                "vtep_ip": "2.2.2.3"
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
                "default": {
                    "address_family": {
                        "l2vpn evpn": {
                            "prefixes": {
                                "[6][2.2.2.2:5][0][32][192.168.105.111][32][239.1.105.1][32][1.1.1.3]/27": {
                                    "table_version": "26",
                                    "nlri_data": {
                                        "route-type": "6",
                                        "rd": "2.2.2.2:5",
                                        "eti": "0",
                                        "mcast_src_len": "32",
                                        "mcast_src": "192.168.105.111",
                                        "mcast_group_len": "32",
                                        "mcast_group_addr": "239.1.105.1",
                                        "orig_rtr_len": "32",
                                        "orig_rtr_id": "1.1.1.3",
                                        "subnet": "27"
                                    },
                                    "available_path": "0",
                                    "best_path": "",
                                    "paths": "0 available, no best path"
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}