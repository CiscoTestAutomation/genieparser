expected_output = {
    "instance": {
        "default": {
            "vrf": {
                "VRF1": {
                    "address_family": {
                        "vpnv4 unicast": {
                            "prefixes": {
                                "10.4.1.1/32": {
                                    "table_version": "2",
                                    "available_path": "1",
                                    "best_path": "1",
                                    "paths": "1 available, best #1, table VRF1",
                                    "index": {
                                        1: {
                                            "next_hop": "0.0.0.0",
                                            "gateway": "0.0.0.0",
                                            "originator": "10.4.1.1",
                                            "next_hop_via": "vrf VRF1",
                                            "localpref": 100,
                                            "metric": 0,
                                            "weight": "32768",
                                            "origin_codes": "i",
                                            "status_codes": "*>",
                                            "refresh_epoch": 1,
                                            "ext_community": "Cost:pre-bestpath:128:1280 0x8800:32768:0",
                                            "route_info": "Local",
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0x0",
                                            "update_group": 1,
                                        }
                                    },
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
