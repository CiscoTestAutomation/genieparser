expected_output = {
    "bridge_domain": {
        10: {
            "number_of_ports_in_all": 3,
            "bd_domain_id": 10,
            "state": "UP",
            "mac_learning_state": "Enabled",
            "aging_timer": 30,
            "member_ports": [
                "GigabitEthernet6 service instance 10",
                "GigabitEthernet7 service instance 10",
                "EVPN Instance 10",
            ],
            "mac_table": {
                "OCE_PTR:0xe8eb04a0": {
                    "mac_address": {
                        "000C.29FF.EEC6": {
                            "mac_address": "000C.29FF.EEC6",
                            "aed": 0,
                            "policy": "forward",
                            "tag": "static_r",
                            "age": 0,
                        }
                    },
                    "pseudoport": "OCE_PTR:0xe8eb04a0",
                },
                "GigabitEthernet6.EFP10": {
                    "mac_address": {
                        "000C.29FF.A9B3": {
                            "mac_address": "000C.29FF.A9B3",
                            "aed": 0,
                            "policy": "forward",
                            "tag": "dynamic_c",
                            "age": 29,
                        }
                    },
                    "pseudoport": "GigabitEthernet6.EFP10",
                },
                "GigabitEthernet7.EFP10": {
                    "mac_address": {
                        "000C.29FF.A6A1": {
                            "mac_address": "000C.29FF.A6A1",
                            "aed": 0,
                            "policy": "forward",
                            "tag": "dynamic_c",
                            "age": 26,
                        }
                    },
                    "pseudoport": "GigabitEthernet7.EFP10",
                },
                "OCE_PTR:0xe8eb0500": {
                    "mac_address": {
                        "000C.29FF.DBFB": {
                            "mac_address": "000C.29FF.DBFB",
                            "aed": 0,
                            "policy": "forward",
                            "tag": "static_r",
                            "age": 0,
                        }
                    },
                    "pseudoport": "OCE_PTR:0xe8eb0500",
                },
            },
        }
    }
}
