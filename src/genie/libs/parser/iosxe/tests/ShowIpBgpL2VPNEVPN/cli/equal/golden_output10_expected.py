expected_output = {
    "instance": {
        "default": {
            "vrf": {
                "evi_101": {
                    "address_family": {
                        "l2vpn evpn": {
                            "prefixes": {
                                "[2][20.0.1.1:101][0][48][000011112222][32][20.101.1.254]/24": {
                                    "table_version": "13",
                                    "nlri_data": {
                                        "route-type": "2",
                                        "rd": "20.0.1.1:101",
                                        "eti": "0",
                                        "mac_len": "48",
                                        "mac": "000011112222",
                                        "ip_len": "32",
                                        "ip_prefix": "20.101.1.254",
                                        "subnet": "24"
                                    },
                                    "available_path": "1",
                                    "best_path": "1",
                                    "paths": "1 available, best #1, table evi_101",
                                    "index": {
                                        1: {
                                            "next_hop": "30.0.1.11",
                                            "gateway": "20.1.1.112",
                                            "originator": "20.1.1.112",
                                            "next_hop_via": "default",
                                            "localpref": 100,
                                            "origin_codes": "?",
                                            "status_codes": "*>",
                                            "refresh_epoch": 1,
                                            "route_info": "300",
                                            "imported_path_from": "[2][30.0.1.11:101][0][48][000011112222][32][20.101.1.254]/24 (global)",
                                            "evpn": {
                                                "evpn_esi": "00000000000000000000",
                                                "label": 2000101,
                                                "ext_community": "RT:100:2000101 RT:100:3000101 ENCAP:8"
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