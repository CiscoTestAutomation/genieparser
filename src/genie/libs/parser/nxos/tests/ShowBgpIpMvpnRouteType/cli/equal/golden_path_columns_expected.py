expected_output = {
    "instance": {
        "default": {
            "vrf": {
                "default": {
                    "vrf_name_out": "default",
                    "address_family": {
                        "ipv4 mvpn": {
                            "af_name": "ipv4 mvpn",
                            "table_version": "26",
                            "router_id": "10.2.0.1",
                            "rd": {
                                "65002:30001": {
                                    "rd_val": "65002:30001",
                                    "prefix": {
                                    "[5][10.111.1.3][238.8.4.101]/64": {
                                        "nonipprefix": "[5][10.111.1.3][238.8.4.101]/64",
                                            "path": {
                                                1: {
                                                    "pathnr": 0,
                                                    "typecode": "e",
                                                    "bestcode": ">",
                                                    "statuscode": "*",
                                                    "ipnexthop": "10.10.0.1",
                                                    "weight": "0",
                                                    "path": "65003 65002",
                                                    "origin": "i"
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
    }
}
