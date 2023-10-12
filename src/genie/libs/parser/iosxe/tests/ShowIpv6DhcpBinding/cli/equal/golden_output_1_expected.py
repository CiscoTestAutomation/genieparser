expected_output = {
    "client": {
        "FE80::8715:A9FF:FEBE:B6FA": {
            "duid": "00030001A85E45C5D933",
            "username": "unassigned",
            "vrf": "OPER_VRF",
            "interface": "relayed",
            "ia_pd": {
                "0x00000001": {
                    "ia_id": "0x00000001",
                    "t1": 302400,
                    "t2": 483840,
                    "prefix": {
                        "2001:DB8::/48": {
                            "preferred_lifetime": 604800,
                            "valid_lifetime": 2592000,
                            "expires": {
                                "month": "Oct",
                                "day": 11,
                                "year": 2023,
                                "time": "03:26 AM",
                                "remaining_seconds": 2506862
                            }
                        }
                    }
                }
            },
            "ia_na": {
                "0x00000000": {
                    "ia_id": "0x00000000",
                    "t1": 43200,
                    "t2": 69120,
                    "address": {
                        "2001::514B:882E:78AF:9593": {
                            "preferred_lifetime": 86400,
                            "valid_lifetime": 172800,
                            "expires": {
                                "month": "Sep",
                                "day": 13,
                                "year": 2023,
                                "time": "03:26 AM",
                                "remaining_seconds": 87662
                            }
                        },
                        "2002::24A4:79EA:58FB:6A6D": {
                            "preferred_lifetime": 86400,
                            "valid_lifetime": 172800,
                            "expires": {
                                "month": "Sep",
                                "day": 13,
                                "year": 2023,
                                "time": "03:26 AM",
                                "remaining_seconds": 87662
                            }
                        },
                        "2003::B987:FD2C:CB89:9583": {
                            "preferred_lifetime": "INFINITY",
                            "valid_lifetime": "INFINITY"
                        }
                    }
                }
            }
        }
    }
}