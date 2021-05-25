expected_output = {
    "protocols": {
        "ospf": {
            "vrf": {
                "default": {
                    "address_family": {
                        "ipv4": {
                            "instance": {
                                "mpls1": {
                                    "router_id": "10.94.1.1",
                                    "preference": {
                                        "single_value": {
                                            "all": 110
                                        }
                                    },
                                    "nsf": True,
                                    "redistribution": {
                                        "static": {
                                            "enabled": True,
                                            "metric": 100
                                        }
                                    },
                                    "areas": {
                                        "0": {
                                            "interfaces": [
                                                "Loopback0",
                                                "GigabitEthernet0/0/0/0",
                                                "GigabitEthernet0/0/0/1"
                                            ],
                                            "mpls": {
                                                "te": {
                                                    "enabled": True
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