expected_output = {
    "protocols": {
        "ospf": {
            "vrf": {
                "default": {
                    "address_family": {
                        "ipv4": {
                            "instance": {
                                "1": {
                                    "router_id": "10.36.3.3",
                                    "preference": {
                                        "single_value": {
                                            "all": 110
                                        },
                                        "multi_values": {
                                            "granularity": {
                                                "detail": {
                                                    "intra_area": 112,
                                                    "inter_area": 113
                                                }
                                            },
                                            "external": 114
                                        }
                                    },
                                    "nsf": False,
                                    "redistribution": {
                                        "connected": {
                                            "enabled": True
                                        },
                                        "static": {
                                            "enabled": True,
                                            "metric": 10
                                        },
                                        "bgp": {
                                            "bgp_id": 100,
                                            "metric": 111
                                        },
                                        "isis": {
                                            "isis_id": 10,
                                            "metric": 3333
                                        }
                                    },
                                    "areas": {
                                        "0": {
                                            "interfaces": [
                                                "Loopback0",
                                                "GigabitEthernet0/0/0/0",
                                                "GigabitEthernet0/0/0/2"
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