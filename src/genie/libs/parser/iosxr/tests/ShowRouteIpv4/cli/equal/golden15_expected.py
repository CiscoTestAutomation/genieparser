expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "routes": {
                        "0.0.0.0/0": {
                            "active": True,
                            "next_hop": {
                                "outgoing_interface": {
                                    "Null0": {
                                        "outgoing_interface": "Null0",
                                        "updated": "3y15w"
                                    }
                                }
                            },
                            "route": "0.0.0.0/0",
                            "source_protocol": "static",
                            "source_protocol_codes": "S *"
                        },
                        "10.0.0.0/8": {
                            "active": True,
                            "metric": 0,
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "172.16.254.189",
                                        "updated": "4d11h"
                                    },
                                    2: {
                                        "index": 2,
                                        "next_hop": "172.17.254.254",
                                        "updated": "4d11h"
                                    }
                                }
                            },
                            "route": "10.0.0.0/8",
                            "route_preference": 20,
                            "source_protocol": "bgp",
                            "source_protocol_codes": "B"
                        }
                    }
                }
            },
            "last_resort": {
                "gateway": "0.0.0.0",
                "to_network": "0.0.0.0"
            }
        }
    }
}
