expected_output = {
    "instance": {
        "default": {
            "vrf": {
                "default": {
                    "vrf_name_out": "default",
                    "address_family": {
                        "l2vpn evpn": {
                            "af_name": "l2vpn evpn",
                            "table_version": "26",
                            "router_id": "10.2.0.1",
                            "rd": {
                                "65002:30001": {
                                    "rd_val": "65002:30001",
                                    "prefix": {
                                        "[2]:[0]:[0]:[48]:[0050.0000.0e00]:[0]:[0.0.0.0]/216": {
                                            "nonipprefix": "[2]:[0]:[0]:[48]:[0050.0000.0e00]:[0]:[0.0.0.0]/216",
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
