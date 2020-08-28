expected_output = {
    "bridge_domain": {
        2051: {
            "state": "UP",
            "member_ports": [
                "vfi VPLS-2051 neighbor 10.120.202.64 2051",
                "Port-channel1 service instance 2051",
            ],
            "bd_domain_id": 2051,
            "aging_timer": 3600,
            "mac_table": {
                "VPLS-2051.10200e6": {
                    "pseudoport": "VPLS-2051.10200e6",
                    "mac_address": {
                        "0000.57FF.6D9E": {
                            "tag": "dynamic",
                            "mac_address": "0000.57FF.6D9E",
                            "age": 3153,
                            "policy": "forward",
                            "aed": 0,
                        }
                    },
                },
                "Port-channel1.EFP2051": {
                    "pseudoport": "Port-channel1.EFP2051",
                    "mac_address": {
                        "0000.A0FF.0027": {
                            "tag": "dynamic",
                            "mac_address": "0000.A0FF.0027",
                            "age": 3142,
                            "policy": "forward",
                            "aed": 0,
                        },
                        "0000.A0FF.0097": {
                            "tag": "dynamic",
                            "mac_address": "0000.A0FF.0097",
                            "age": 3153,
                            "policy": "forward",
                            "aed": 0,
                        },
                        "0000.A0FF.013A": {
                            "tag": "dynamic",
                            "mac_address": "0000.A0FF.013A",
                            "age": 3137,
                            "policy": "forward",
                            "aed": 0,
                        },
                        "0000.A0FF.00BF": {
                            "tag": "dynamic",
                            "mac_address": "0000.A0FF.00BF",
                            "age": 3125,
                            "policy": "forward",
                            "aed": 0,
                        },
                        "0000.A0FF.010C": {
                            "tag": "dynamic",
                            "mac_address": "0000.A0FF.010C",
                            "age": 3133,
                            "policy": "forward",
                            "aed": 0,
                        },
                        "0000.A0FF.010F": {
                            "tag": "dynamic",
                            "mac_address": "0000.A0FF.010F",
                            "age": 3133,
                            "policy": "forward",
                            "aed": 0,
                        },
                    },
                },
            },
            "mac_learning_state": "Enabled",
            "split-horizon_group": {
                "0": {
                    "interfaces": ["Port-channel1 service instance 2051"],
                    "num_of_ports": "1",
                }
            },
            "number_of_ports_in_all": 2,
        },
        2052: {
            "state": "UP",
            "member_ports": [
                "vfi VPLS-2052 neighbor 10.120.202.64 2052",
                "Port-channel1 service instance 2052",
            ],
            "bd_domain_id": 2052,
            "aging_timer": 3600,
            "mac_table": {
                "Port-channel1.EFP2052": {
                    "pseudoport": "Port-channel1.EFP2052",
                    "mac_address": {
                        "0000.A0FF.002C": {
                            "tag": "dynamic",
                            "mac_address": "0000.A0FF.002C",
                            "age": 3143,
                            "policy": "forward",
                            "aed": 0,
                        },
                        "0000.A0FF.0015": {
                            "tag": "dynamic",
                            "mac_address": "0000.A0FF.0015",
                            "age": 3141,
                            "policy": "forward",
                            "aed": 0,
                        },
                    },
                }
            },
            "mac_learning_state": "Enabled",
            "split-horizon_group": {
                "0": {
                    "interfaces": ["Port-channel1 service instance 2052"],
                    "num_of_ports": "1",
                }
            },
            "number_of_ports_in_all": 2,
        },
    }
}
