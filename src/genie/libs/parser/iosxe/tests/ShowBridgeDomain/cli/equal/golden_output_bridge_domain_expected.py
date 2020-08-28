expected_output = {
    "bridge_domain": {
        3051: {
            "number_of_ports_in_all": 2,
            "state": "UP",
            "member_ports": [
                "vfi VPLS-3051 neighbor 192.168.36.220 3051",
                "GigabitEthernet0/0/3 service instance 3051",
            ],
            "mac_table": {
                "GigabitEthernet0/0/3.EFP3051": {
                    "pseudoport": "GigabitEthernet0/0/3.EFP3051",
                    "mac_address": {
                        "0000.A0FF.0118": {
                            "tag": "dynamic",
                            "age": 3441,
                            "aed": 0,
                            "mac_address": "0000.A0FF.0118",
                            "policy": "forward",
                        },
                        "0000.A0FF.0077": {
                            "tag": "dynamic",
                            "age": 3426,
                            "aed": 0,
                            "mac_address": "0000.A0FF.0077",
                            "policy": "forward",
                        },
                        "0000.A0FF.011C": {
                            "tag": "dynamic",
                            "age": 3442,
                            "aed": 0,
                            "mac_address": "0000.A0FF.011C",
                            "policy": "forward",
                        },
                        "0000.A0FF.001F": {
                            "tag": "dynamic",
                            "age": 3416,
                            "aed": 0,
                            "mac_address": "0000.A0FF.001F",
                            "policy": "forward",
                        },
                        "0000.A0FF.0068": {
                            "tag": "dynamic",
                            "age": 3424,
                            "aed": 0,
                            "mac_address": "0000.A0FF.0068",
                            "policy": "forward",
                        },
                        "0000.A0FF.00C5": {
                            "tag": "dynamic",
                            "age": 3433,
                            "aed": 0,
                            "mac_address": "0000.A0FF.00C5",
                            "policy": "forward",
                        },
                        "0000.A0FF.0108": {
                            "tag": "dynamic",
                            "age": 3440,
                            "aed": 0,
                            "mac_address": "0000.A0FF.0108",
                            "policy": "forward",
                        },
                        "0000.A0FF.0010": {
                            "tag": "dynamic",
                            "age": 3415,
                            "aed": 0,
                            "mac_address": "0000.A0FF.0010",
                            "policy": "forward",
                        },
                        "0000.A0FF.000F": {
                            "tag": "dynamic",
                            "age": 3415,
                            "aed": 0,
                            "mac_address": "0000.A0FF.000F",
                            "policy": "forward",
                        },
                        "0000.A0FF.007F": {
                            "tag": "dynamic",
                            "age": 3426,
                            "aed": 0,
                            "mac_address": "0000.A0FF.007F",
                            "policy": "forward",
                        },
                        "0000.A0FF.007B": {
                            "tag": "dynamic",
                            "age": 3426,
                            "aed": 0,
                            "mac_address": "0000.A0FF.007B",
                            "policy": "forward",
                        },
                        "0000.A0FF.0087": {
                            "tag": "dynamic",
                            "age": 3427,
                            "aed": 0,
                            "mac_address": "0000.A0FF.0087",
                            "policy": "forward",
                        },
                        "0000.A0FF.00AA": {
                            "tag": "dynamic",
                            "age": 3430,
                            "aed": 0,
                            "mac_address": "0000.A0FF.00AA",
                            "policy": "forward",
                        },
                        "0000.A0FF.012C": {
                            "tag": "dynamic",
                            "age": 3443,
                            "aed": 0,
                            "mac_address": "0000.A0FF.012C",
                            "policy": "forward",
                        },
                        "0000.A0FF.00D0": {
                            "tag": "dynamic",
                            "age": 3434,
                            "aed": 0,
                            "mac_address": "0000.A0FF.00D0",
                            "policy": "forward",
                        },
                        "0000.A0FF.00F6": {
                            "tag": "dynamic",
                            "age": 3438,
                            "aed": 0,
                            "mac_address": "0000.A0FF.00F6",
                            "policy": "forward",
                        },
                        "0000.A0FF.00F7": {
                            "tag": "dynamic",
                            "age": 3438,
                            "aed": 0,
                            "mac_address": "0000.A0FF.00F7",
                            "policy": "forward",
                        },
                        "0000.A0FF.00F2": {
                            "tag": "dynamic",
                            "age": 3438,
                            "aed": 0,
                            "mac_address": "0000.A0FF.00F2",
                            "policy": "forward",
                        },
                        "0000.A0FF.0129": {
                            "tag": "dynamic",
                            "age": 3443,
                            "aed": 0,
                            "mac_address": "0000.A0FF.0129",
                            "policy": "forward",
                        },
                    },
                }
            },
            "aging_timer": 3600,
            "bd_domain_id": 3051,
            "split-horizon_group": {
                "0": {
                    "num_of_ports": "1",
                    "interfaces": ["GigabitEthernet0/0/3 service instance 3051"],
                }
            },
            "mac_learning_state": "Enabled",
        }
    }
}
