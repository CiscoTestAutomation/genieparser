expected_output = {
    "instance": {
        "default": {
            "vrf": {
                "EVPN-BGP-Table": {
                    "address_family": {
                        "l2vpn evpn": {
                            "prefixes": {
                                "[4][3.3.3.3:1][03AABB00000002000001][32][3.3.3.3]/23": {
                                    "table_version": "135",
                                    "nlri_data": {
                                        "route-type": "4",
                                        "rd": "3.3.3.3:1",
                                        "esi": "03AABB00000002000001",
                                        "ip_len": "32",
                                        "orig_rtr_id": "3.3.3.3",
                                        "subnet": "23"
                                    },
                                    "available_path": "1",
                                    "best_path": "1",
                                    "paths": "1 available, best #1, table EVPN-BGP-Table",
                                    "index": {
                                        1: {
                                            "next_hop": "::",
                                            "gateway": "0.0.0.0",
                                            "originator": "3.3.3.3",
                                            "next_hop_via": "default",
                                            "update_group": 1,
                                            "localpref": 100,
                                            "weight": "32768",
                                            "origin_codes": "?",
                                            "status_codes": "*>",
                                            "refresh_epoch": 1,
                                            "route_info": "Local",
                                            "ext_community": "EVPN ES-IMPORT:0xAABB:0x0:0x2",
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