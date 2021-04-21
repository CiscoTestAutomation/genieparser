expected_output = {
    "instance": {
        "default": {
            "vrf": {
                "L2VPN-VPLS-BGP-Table": {
                    "address_family": {
                        "l2vpn vpls": {
                            "prefixes": {
                                "VEID-1:Blk-1/136,": {
                                    "available_path": "2",
                                    "best_path": "1",
                                    "index": {
                                        1: {
                                            "agi_version": 0,
                                            "cluster_list": "0.0.0.61",
                                            "ext_community": "RT:0:3051 RT:5918:3051 L2VPN L2:0x0:MTU-1500",
                                            "gateway": "192.168.165.119",
                                            "label_base": 16,
                                            "localpref": 100,
                                            "metric": 0,
                                            "next_hop": "192.168.165.220",
                                            "next_hop_igp_metric": "66536",
                                            "origin_codes": "?",
                                            "originator": "192.168.165.119",
                                            "recipient_pathid": "0",
                                            "refresh_epoch": 7,
                                            "route_info": "Local",
                                            "status_codes": "*>",
                                            "transfer_pathid": "0x0",
                                            "ve_block_size": 10,
                                        },
                                        2: {
                                            "agi_version": 0,
                                            "cluster_list": "0.0.0.61",
                                            "ext_community": "RT:0:3051 RT:5918:3051 L2VPN L2:0x0:MTU-1500",
                                            "gateway": "192.168.165.120",
                                            "label_base": 16,
                                            "localpref": 100,
                                            "metric": 0,
                                            "next_hop": "192.168.165.220",
                                            "next_hop_igp_metric": "66536",
                                            "origin_codes": "?",
                                            "originator": "192.168.165.120",
                                            "recipient_pathid": "0",
                                            "refresh_epoch": 9,
                                            "route_info": "Local",
                                            "status_codes": "* i",
                                            "transfer_pathid": "0",
                                            "ve_block_size": 10,
                                        },
                                    },
                                    "paths": "2 available, best #1, table L2VPN-VPLS-BGP-Table",
                                    "table_version": "2",
                                },
                                "VEID-2:Blk-1/136,": {
                                    "available_path": "1",
                                    "best_path": "1",
                                    "index": {
                                        1: {
                                            "agi_version": 0,
                                            "ext_community": "RT:0:3051 RT:5918:3051 L2VPN L2:0x0:MTU-1500",
                                            "gateway": "0.0.0.0",
                                            "label_base": 1026,
                                            "localpref": 100,
                                            "next_hop": "0.0.0.0",
                                            "origin_codes": "?",
                                            "originator": "10.169.197.254",
                                            "recipient_pathid": "0",
                                            "refresh_epoch": 1,
                                            "route_info": "Local",
                                            "status_codes": "*>",
                                            "transfer_pathid": "0x0",
                                            "update_group": 4,
                                            "weight": "32768",
                                            "ve_block_size": 10,
                                        }
                                    },
                                    "paths": "1 available, best #1, table L2VPN-VPLS-BGP-Table",
                                    "table_version": "304",
                                },
                            },
                            "route_distinguisher": "5918:3051",
                        }
                    }
                }
            }
        }
    }
}
