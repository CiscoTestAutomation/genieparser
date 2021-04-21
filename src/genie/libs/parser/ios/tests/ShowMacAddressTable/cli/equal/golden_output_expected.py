expected_output = {
    "mac_table": {
        "vlans": {
            "100": {
                "mac_addresses": {
                    "ecbd.1dff.5f92": {
                        "drop": {"drop": True, "entry_type": "dynamic"},
                        "mac_address": "ecbd.1dff.5f92",
                    },
                    "3820.56ff.6f75": {
                        "interfaces": {
                            "Port-channel12": {
                                "interface": "Port-channel12",
                                "entry_type": "dynamic",
                            }
                        },
                        "mac_address": "3820.56ff.6f75",
                    },
                    "58bf.eaff.e508": {
                        "interfaces": {
                            "Vlan100": {"interface": "Vlan100", "entry_type": "static"}
                        },
                        "mac_address": "58bf.eaff.e508",
                    },
                },
                "vlan": 100,
            },
            "all": {
                "mac_addresses": {
                    "0100.0cff.9999": {
                        "interfaces": {
                            "CPU": {"interface": "CPU", "entry_type": "static"}
                        },
                        "mac_address": "0100.0cff.9999",
                    },
                    "0100.0cff.999a": {
                        "interfaces": {
                            "CPU": {"interface": "CPU", "entry_type": "static"}
                        },
                        "mac_address": "0100.0cff.999a",
                    },
                },
                "vlan": "all",
            },
            "20": {
                "mac_addresses": {
                    "aaaa.bbff.8888": {
                        "drop": {"drop": True, "entry_type": "static"},
                        "mac_address": "aaaa.bbff.8888",
                    }
                },
                "vlan": 20,
            },
            "10": {
                "mac_addresses": {
                    "aaaa.bbff.8888": {
                        "interfaces": {
                            "GigabitEthernet1/0/8": {
                                "entry": "*",
                                "interface": "GigabitEthernet1/0/8",
                                "entry_type": "static",
                            },
                            "GigabitEthernet1/0/9": {
                                "entry": "*",
                                "interface": "GigabitEthernet1/0/9",
                                "entry_type": "static",
                            },
                            "Vlan101": {
                                "entry": "*",
                                "interface": "Vlan101",
                                "entry_type": "static",
                            },
                        },
                        "mac_address": "aaaa.bbff.8888",
                    }
                },
                "vlan": 10,
            },
            "101": {
                "mac_addresses": {
                    "58bf.eaff.e5f7": {
                        "interfaces": {
                            "Vlan101": {"interface": "Vlan101", "entry_type": "static"}
                        },
                        "mac_address": "58bf.eaff.e5f7",
                    },
                    "3820.56ff.6fb3": {
                        "interfaces": {
                            "Port-channel12": {
                                "interface": "Port-channel12",
                                "entry_type": "dynamic",
                            }
                        },
                        "mac_address": "3820.56ff.6fb3",
                    },
                    "3820.56ff.6f75": {
                        "interfaces": {
                            "Port-channel12": {
                                "interface": "Port-channel12",
                                "entry_type": "dynamic",
                            }
                        },
                        "mac_address": "3820.56ff.6f75",
                    },
                },
                "vlan": 101,
            },
        }
    },
    "total_mac_addresses": 10,
}
