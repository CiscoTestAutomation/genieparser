expected_output = {
    "instance": {
        "default": {
            "vrf": {
                "vrf1": {
                    "address_family": {
                        "": {
                            "default_vrf": "vrf1",
                            "prefixes": {
                                "0.0.0.0/0": {
                                    "available_path": "2",
                                    "best_path": "1",
                                    "index": {
                                        1: {
                                            "community": "163:43242 2002:8 2002:35 2002:53 2002:100 2002:1000",
                                            "ext_community": "RT:65002:3014",
                                            "gateway": "10.121.2.2",
                                            "localpref": 950,
                                            "next_hop": "10.121.2.2",
                                            "next_hop_via": "vrf vrf1",
                                            "origin_codes": "i",
                                            "originator": "10.246.128.21",
                                            "recipient_pathid": "0",
                                            "refresh_epoch": 2,
                                            "route_info": "64624",
                                            "status_codes": "*>",
                                            "transfer_pathid": "0x0",
                                            "update_group": [13, 304],
                                        },
                                        2: {
                                            "community": "163:43242 2002:8 2002:35 2002:53 2002:100 2002:1000",
                                            "ext_community": "RT:65002:3014",
                                            "gateway": "10.55.117.38",
                                            "imported_path_from": "10.55.117.38:3014:0.0.0.0/0 (global)",
                                            "localpref": 950,
                                            "metric": 0,
                                            "next_hop": "10.55.117.38",
                                            "next_hop_igp_metric": "11",
                                            "next_hop_via": "default",
                                            "origin_codes": "i",
                                            "originator": "10.55.117.38",
                                            "recipient_pathid": "0",
                                            "refresh_epoch": 17,
                                            "route_info": "64624",
                                            "status_codes": "* i",
                                            "transfer_pathid": "0",
                                            "update_group": [13, 304],
                                        },
                                    },
                                    "paths": "2 available, best #1, table vrf1",
                                    "table_version": "74438",
                                }
                            },
                            "route_distinguisher": "10.100.1.1:3014",
                        }
                    }
                }
            }
        }
    }
}
