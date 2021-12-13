expected_output = {
    "instance": {
        "default": {
            "vrf": {
                "VRF1": {
                    "address_family": {
                        "vpnv4": {
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
                                            "route_info": "Local",
                                            "ext_community": "Cost:pre-bestpath:128:1280 0x8800:32768:0 0x8801:100:32 0x8802:65280:256 0x8803:65281:1514 0x8806:0:16843009",
                                            "recipient_pathid": "0",
                                            "transfer_pathid": "0x0",
                                        }
                                    },
                                }
                            },
                            "route_distinguisher": "65000:1",
                            "default_vrf": "VRF1",
                        }
                    }
                }
            }
        }
    }
}
