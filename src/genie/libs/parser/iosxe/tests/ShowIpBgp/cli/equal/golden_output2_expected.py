expected_output = {
    "vrf": {
        "internal": {
            "address_family": {
                "vpnv4 RD 65026:3601": {
                    "bgp_table_version": 88855359,
                    "route_identifier": "10.90.2.45",
                    "route_distinguisher": "65026:3601",
                    "default_vrf": "internal",
                    "routes": {
                        "10.0.0.0": {
                            "index": {
                                1: {
                                    "status_codes": "*>",
                                    "path": "65002 65000",
                                    "next_hop": "10.10.10.10",
                                    "weight": 0,
                                    "origin_codes": "i"
                                }
                            }
                        },
                        "172.16.0.0/12": {
                            "index": {
                                1: {
                                    "status_codes": "*>",
                                    "path": "65002 65000",
                                    "next_hop": "10.10.10.10",
                                    "weight": 0,
                                    "origin_codes": "i"
                                }
                            }
                        },
                        "192.168.0.0/16": {
                            "index": {
                                1: {
                                    "status_codes": "*>",
                                    "path": "65002 65000",
                                    "next_hop": "10.10.10.10",
                                    "weight": 0,
                                    "origin_codes": "i"
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
