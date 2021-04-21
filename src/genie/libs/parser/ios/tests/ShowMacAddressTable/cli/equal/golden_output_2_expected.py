expected_output = {
    "mac_table": {
        "vlans": {
            "100": {
                "mac_addresses": {
                    "11aa.22ff.ee88": {
                        "interfaces": {
                            "Router": {
                                "entry": "*",
                                "interface": "Router",
                                "entry_type": "static",
                                "learn": "No",
                            }
                        },
                        "mac_address": "11aa.22ff.ee88",
                    }
                },
                "vlan": 100,
            },
            "101": {
                "mac_addresses": {
                    "44dd.eeff.55bb": {
                        "interfaces": {
                            "GigabitEthernet1/40": {
                                "entry": "*",
                                "interface": "GigabitEthernet1/40",
                                "entry_type": "dynamic",
                                "learn": "Yes",
                                "age": 10,
                            }
                        },
                        "mac_address": "44dd.eeff.55bb",
                    }
                },
                "vlan": 101,
            },
            "102": {
                "mac_addresses": {
                    "aa11.bbff.ee55": {
                        "interfaces": {
                            "GigabitEthernet1/2": {
                                "entry": "*",
                                "interface": "GigabitEthernet1/2",
                                "entry_type": "static",
                                "learn": "Yes",
                            },
                            "GigabitEthernet1/4": {
                                "entry": "*",
                                "interface": "GigabitEthernet1/4",
                                "entry_type": "static",
                                "learn": "Yes",
                            },
                            "GigabitEthernet1/5": {
                                "entry": "*",
                                "interface": "GigabitEthernet1/5",
                                "entry_type": "static",
                                "learn": "Yes",
                            },
                            "GigabitEthernet1/6": {
                                "entry": "*",
                                "interface": "GigabitEthernet1/6",
                                "entry_type": "static",
                                "learn": "Yes",
                            },
                            "GigabitEthernet1/9": {
                                "entry": "*",
                                "interface": "GigabitEthernet1/9",
                                "entry_type": "static",
                                "learn": "Yes",
                            },
                            "GigabitEthernet1/10": {
                                "entry": "*",
                                "interface": "GigabitEthernet1/10",
                                "entry_type": "static",
                                "learn": "Yes",
                            },
                            "GigabitEthernet1/11": {
                                "entry": "*",
                                "interface": "GigabitEthernet1/11",
                                "entry_type": "static",
                                "learn": "Yes",
                            },
                            "GigabitEthernet1/12": {
                                "entry": "*",
                                "interface": "GigabitEthernet1/12",
                                "entry_type": "static",
                                "learn": "Yes",
                            },
                            "Router": {
                                "entry": "*",
                                "interface": "Router",
                                "entry_type": "static",
                                "learn": "Yes",
                            },
                            "Switch": {
                                "entry": "*",
                                "interface": "Switch",
                                "entry_type": "static",
                                "learn": "Yes",
                            },
                        },
                        "mac_address": "aa11.bbff.ee55",
                    }
                },
                "vlan": 102,
            },
            "200": {
                "mac_addresses": {
                    "dd44.55ff.55ee": {
                        "interfaces": {
                            "TenGigabitEthernet1/1": {
                                "entry": "*",
                                "interface": "TenGigabitEthernet1/1",
                                "entry_type": "static",
                                "learn": "Yes",
                            },
                            "TenGigabitEthernet1/2": {
                                "entry": "*",
                                "interface": "TenGigabitEthernet1/2",
                                "entry_type": "static",
                                "learn": "Yes",
                            },
                            "TenGigabitEthernet1/4": {
                                "entry": "*",
                                "interface": "TenGigabitEthernet1/4",
                                "entry_type": "static",
                                "learn": "Yes",
                            },
                            "TenGigabitEthernet1/8": {
                                "entry": "*",
                                "interface": "TenGigabitEthernet1/8",
                                "entry_type": "static",
                                "learn": "Yes",
                            },
                        },
                        "mac_address": "dd44.55ff.55ee",
                    }
                },
                "vlan": 200,
            },
            "300": {
                "mac_addresses": {
                    "11aa.22ff.ee88": {
                        "interfaces": {
                            "Router": {
                                "interface": "Router",
                                "entry_type": "static",
                                "learn": "No",
                            }
                        },
                        "mac_address": "11aa.22ff.ee88",
                    }
                },
                "vlan": 300,
            },
            "301": {
                "mac_addresses": {
                    "11aa.22ff.ee88": {
                        "drop": {"drop": True, "entry_type": "static"},
                        "mac_address": "11aa.22ff.ee88",
                    }
                },
                "vlan": 301,
            },
            "---": {
                "mac_addresses": {
                    "0000.0000.0000": {
                        "interfaces": {
                            "Router": {
                                "entry": "*",
                                "interface": "Router",
                                "entry_type": "static",
                                "learn": "No",
                            }
                        },
                        "mac_address": "0000.0000.0000",
                    }
                },
                "vlan": "---",
            },
            "400": {
                "mac_addresses": {
                    "0000.0000.0000": {
                        "interfaces": {
                            "vPC Peer-Link": {
                                "entry": "*",
                                "interface": "vPC Peer-Link",
                                "entry_type": "static",
                                "learn": "No",
                            },
                            "Router": {
                                "entry": "*",
                                "interface": "Router",
                                "entry_type": "static",
                                "learn": "No",
                            },
                        },
                        "mac_address": "0000.0000.0000",
                    }
                },
                "vlan": 400,
            },
        }
    },
    "total_mac_addresses": 8,
}
