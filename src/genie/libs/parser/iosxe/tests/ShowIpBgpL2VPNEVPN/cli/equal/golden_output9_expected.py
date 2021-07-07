expected_output = {
    "instance": {
        "default": {
            "vrf": {
                "EVPN-BGP-Table": {
                    "address_family": {
                        "l2vpn evpn": {
                            "prefixes": {
                                "[5][20.0.0.1:31000][0][32][250.250.250.23]/17": {
                                    "table_version": "241",
                                    "nlri_data": {
                                        "route-type": "5",
                                        "rd": "20.0.0.1:31000",
                                        "eti": "0",
                                        "ip_len": "32",
                                        "ip_prefix": "250.250.250.23",
                                        "subnet": "17"
                                    },
                                    "available_path": "1",
                                    "best_path": "1",
                                    "paths": "1 available, best #1, table EVPN-BGP-Table",
                                    "index": {
                                        1: {
                                            "next_hop": "20.0.102.3",
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
                                            "evpn": {
                                                "ext_community": "RT:1000:31000",
                                                "encap": "8",
                                                "router_mac": "MAC:6056.0001.1101"
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