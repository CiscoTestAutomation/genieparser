expected_output = {
    "tag": {
        "64512": {
            "level": {
                1: {
                    "hosts": {
                        "R1": {}
                    }
                },
                2: {
                    "hosts": {
                        "R2": {
                            "metric": 20,
                            "interface": {
                                "TenGigabitEthernet0/0/0.10": {
                                    "next_hop": "R3",
                                    "snpa": "ccb6.c8f6.e904"
                                },
                                "TenGigabitEthernet0/0/0.20": {
                                    "next_hop": "R6",
                                    "snpa": "04bd.97d1.2e24"
                                }
                            }
                        },
                        "R3": {
                            "metric": 10,
                            "interface": {
                                "TenGigabitEthernet0/0/0.10": {
                                    "next_hop": "R3",
                                    "snpa": "ccb6.c8f6.e904"
                                }
                            }
                        },
                        "R4": {
                            "metric": 20,
                            "interface": {
                                "TenGigabitEthernet0/0/0.20": {
                                    "next_hop": "R6",
                                    "snpa": "04bd.97d1.2e24"
                                }
                            }
                        },
                        "R5": {
                            "metric": 30,
                            "interface": {
                                "TenGigabitEthernet0/0/0.10": {
                                    "next_hop": "R3",
                                    "snpa": "ccb6.c8f6.e904"
                                },
                                "TenGigabitEthernet0/0/0.20": {
                                    "next_hop": "R6",
                                    "snpa": "04bd.97d1.2e24"
                                }
                            }
                        },
                        "R1": {},
                        "R6": {
                            "metric": 10,
                            "interface": {
                                "TenGigabitEthernet0/0/0.20": {
                                    "next_hop": "R6",
                                    "snpa": "04bd.97d1.2e24"
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
