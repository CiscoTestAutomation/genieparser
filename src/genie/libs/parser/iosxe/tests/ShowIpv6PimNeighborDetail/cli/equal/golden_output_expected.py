expected_output = {
    "vrf": {
        "default": {
            "interfaces": {
                "Port-channel1.100": {
                    "address_family": {
                        "ipv6": {
                            "neighbors": {
                                "secondary_address": ["2001::1:1"],
                                "FE80::21A:30FF:FE47:6EC0": {
                                    "up_time": "3w3d",
                                    "dr_priority": 1,
                                    "expiration": "00:01:37",
                                    "interface": "Port-channel1.100",
                                    "genid_capable": True,
                                    "bidir_capable": True,
                                },
                            }
                        }
                    }
                },
                "Port-channel1.101": {
                    "address_family": {
                        "ipv6": {
                            "neighbors": {
                                "secondary_address": ["2001:1::1:1"],
                                "FE80::21A:30FF:FE47:6EC0": {
                                    "up_time": "3w3d",
                                    "dr_priority": 1,
                                    "expiration": "00:01:38",
                                    "interface": "Port-channel1.101",
                                    "genid_capable": True,
                                    "bidir_capable": True,
                                },
                            }
                        }
                    }
                },
                "GigabitEthernet0/2/3.100": {
                    "address_family": {
                        "ipv6": {
                            "neighbors": {
                                "secondary_address": ["2001::4:2"],
                                "FE80::2D7:8FFF:FECB:8602": {
                                    "up_time": "3w3d",
                                    "designated_router": True,
                                    "dr_priority": 1,
                                    "expiration": "00:01:25",
                                    "interface": "GigabitEthernet0/2/3.100",
                                    "genid_capable": True,
                                    "bidir_capable": True,
                                },
                            }
                        }
                    }
                },
                "GigabitEthernet0/2/0.101": {
                    "address_family": {
                        "ipv6": {
                            "neighbors": {
                                "FE80::21A:30FF:FE47:6E01": {
                                    "up_time": "3w3d",
                                    "dr_priority": 1,
                                    "expiration": "00:01:24",
                                    "interface": "GigabitEthernet0/2/0.101",
                                    "genid_capable": True,
                                    "bidir_capable": True,
                                },
                                "secondary_address": ["2001:1::1"],
                            }
                        }
                    }
                },
                "GigabitEthernet0/2/3.101": {
                    "address_family": {
                        "ipv6": {
                            "neighbors": {
                                "secondary_address": ["2001:1::4:2"],
                                "FE80::2D7:8FFF:FECB:8602": {
                                    "up_time": "3w3d",
                                    "designated_router": True,
                                    "dr_priority": 1,
                                    "expiration": "00:01:42",
                                    "interface": "GigabitEthernet0/2/3.101",
                                    "genid_capable": True,
                                    "bidir_capable": True,
                                },
                            }
                        }
                    }
                },
                "GigabitEthernet0/2/0.100": {
                    "address_family": {
                        "ipv6": {
                            "neighbors": {
                                "FE80::21A:30FF:FE47:6E01": {
                                    "up_time": "3w3d",
                                    "dr_priority": 1,
                                    "expiration": "00:01:33",
                                    "interface": "GigabitEthernet0/2/0.100",
                                    "genid_capable": True,
                                    "bidir_capable": True,
                                },
                                "secondary_address": ["2001::1"],
                            }
                        }
                    }
                },
            }
        }
    }
}
