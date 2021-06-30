expected_output = {
    "instance": {
        "default": {
            "vrf": {
                "EVPN-BGP-Table": {
                    "address_family": {
                        "l2vpn evpn": {
                            "prefixes": {
                                "[3][40.0.0.3:164][0][32][40.0.0.7]/17": {
                                    "table_version": "234",
                                    "nlri_data": {
                                        "route-type": "3",
                                        "rd": "40.0.0.3:164",
                                        "eti": "0",
                                        "ip_len": "32",
                                        "orig_rtr_id": "40.0.0.7",
                                        "subnet": "17"
                                    },
                                    "available_path": "1",
                                    "best_path": "1",
                                    "paths": "1 available, best #1, table EVPN-BGP-Table",
                                    "index": {
                                        1: {
                                            "next_hop": "40.0.0.3",
                                            "gateway": "20.0.102.3",
                                            "originator": "20.0.102.3",
                                            "next_hop_via": "default",
                                            "update_group": 13,
                                            "localpref": 100,
                                            "origin_codes": "i",
                                            "status_codes": "*>",
                                            "refresh_epoch": 1,
                                            "route_info": "Local",
                                            "route_status": "Received from a RR-client",
                                            "ext_community": "RT:10:23000 ENCAP:8",
                                            "pmsi": {
                                                "tun_type": "IR",
                                                "vni": "22993",
                                                "tun_id": {
                                                    "tun_endpoint": "40.0.0.3"
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