expected_output = {
    "instance": {
        "default": {
            "vrf": {
                "sample_vrf": {
                    "address_family": {
                        "vpnv4": {
                            "default_vrf": "sample_vrf",
                            "prefixes": {
                                "0.0.0.0/0": {
                                    "available_path": "4",
                                    "best_path": "1",
                                    "index": {
                                        1: {
                                            "community": "65300:106 65300:500 65300:601 65351:1",
                                            "gateway": "10.220.100.80",
                                            "imported_path_from": "50000:2:172.17.0.0/16",
                                            "imported_safety_path": True,
                                            "localpref": 100,
                                            "next_hop": "10.220.100.80",
                                            "next_hop_via": "vrf sample_vrf",
                                            "origin_codes": "i",
                                            "originator": "10.115.10.40",
                                            "recipient_pathid": "0",
                                            "refresh_epoch": 1,
                                            "route_info": "2",
                                            "status_codes": "*>",
                                            "transfer_pathid": "0x0",
                                            "update_group": [1, 29, 35],
                                        },
                                        2: {
                                            "community": "65300:106 65300:500 65300:601 65351:1",
                                            "gateway": "10.115.10.1",
                                            "imported_path_from": "base",
                                            "localpref": 100,
                                            "metric": 0,
                                            "next_hop": "10.115.10.1",
                                            "next_hop_igp_metric": "2",
                                            "next_hop_via": "vrf sample_vrf",
                                            "origin_codes": "i",
                                            "originator": "10.115.10.1",
                                            "recipient_pathid": "0",
                                            "refresh_epoch": 3,
                                            "route_info": "Local",
                                            "status_codes": "* i",
                                            "transfer_pathid": "0",
                                            "update_group": [1, 29, 35],
                                        },
                                    },
                                    "paths": "4 available, best #1, table sample_vrf",
                                    "table_version": "1559863",
                                }
                            },
                            "route_distinguisher": "102:102",
                        }
                    }
                }
            }
        }
    }
}
