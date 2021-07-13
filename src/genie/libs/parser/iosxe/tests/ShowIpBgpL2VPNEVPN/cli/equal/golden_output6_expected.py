expected_output = {
    "instance": {
        "default": {
            "vrf": {
                "EVPN-BGP-Table": {
                    "address_family": {
                        "l2vpn evpn": {
                            "prefixes": {
                                "[2][2.2.2.2:1000][0][48][022651BDC820][32][192.168.19.2]/24": {
                                    "table_version": "229",
                                    "nlri_data": {
                                        "route-type": "2",
                                        "rd": "2.2.2.2:1000",
                                        "eti": "0",
                                        "mac_len": "48",
                                        "mac": "022651BDC820",
                                        "ip_len": "32",
                                        "ip_prefix": "192.168.19.2",
                                        "subnet": "24"
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
                                            "ext_community": "RT:100:100 RT:100:200 EVPN DEF GW:0:0",
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