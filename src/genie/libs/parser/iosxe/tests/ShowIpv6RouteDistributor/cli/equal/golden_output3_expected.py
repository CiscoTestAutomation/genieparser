expected_output = {
    "vrf": {
        "VRF1": {
            "address_family": {
                "ipv6": {
                    "routes": {
                        "2001:1:1:1::1/128": {
                            "route": "2001:1:1:1::1/128",
                            "active": True,
                            "metric": 0,
                            "route_preference": 0,
                            "source_protocol_codes": "LC",
                            "source_protocol": "local_connected",
                            "next_hop": {
                                "outgoing_interface": {
                                    "Loopback300": {
                                        "outgoing_interface": "Loopback300"
                                    }
                                }
                            }
                        },
                        "2001:2:2:2::2/128": {
                            "route": "2001:2:2:2::2/128",
                            "active": True,
                            "metric": 10752,
                            "route_preference": 90,
                            "source_protocol_codes": "D",
                            "source_protocol": "eigrp",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "FE80::F816:3EFF:FE21:73F6",
                                        "outgoing_interface": "GigabitEthernet2.390"
                                    }
                                }
                            }
                        },
                        "2001:3:3:3::3/128": {
                            "route": "2001:3:3:3::3/128",
                            "active": True,
                            "metric": 2570240,
                            "route_preference": 90,
                            "source_protocol_codes": "D",
                            "source_protocol": "eigrp",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "FE80::5C00:80FF:FE02:7",
                                        "outgoing_interface": "GigabitEthernet3.390"
                                    }
                                }
                            }
                        },
                        "2001:10:12:90::/64": {
                            "route": "2001:10:12:90::/64",
                            "active": True,
                            "metric": 0,
                            "route_preference": 0,
                            "source_protocol_codes": "C",
                            "source_protocol": "connected",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet2.390": {
                                        "outgoing_interface": "GigabitEthernet2.390"
                                    }
                                }
                            }
                        },
                        "2001:10:12:90::1/128": {
                            "route": "2001:10:12:90::1/128",
                            "active": True,
                            "metric": 0,
                            "route_preference": 0,
                            "source_protocol_codes": "L",
                            "source_protocol": "local",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet2.390": {
                                        "outgoing_interface": "GigabitEthernet2.390"
                                    }
                                }
                            }
                        },
                        "2001:10:12:110::/64": {
                            "route": "2001:10:12:110::/64",
                            "active": True,
                            "metric": 0,
                            "route_preference": 0,
                            "source_protocol_codes": "C",
                            "source_protocol": "connected",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet2.410": {
                                        "outgoing_interface": "GigabitEthernet2.410"
                                    }
                                }
                            }
                        },
                        "2001:10:12:110::1/128": {
                            "route": "2001:10:12:110::1/128",
                            "active": True,
                            "metric": 0,
                            "route_preference": 0,
                            "source_protocol_codes": "L",
                            "source_protocol": "local",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet2.410": {
                                        "outgoing_interface": "GigabitEthernet2.410"
                                    }
                                }
                            }
                        },
                        "2001:10:12:115::/64": {
                            "route": "2001:10:12:115::/64",
                            "active": True,
                            "metric": 0,
                            "route_preference": 0,
                            "source_protocol_codes": "C",
                            "source_protocol": "connected",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet2.415": {
                                        "outgoing_interface": "GigabitEthernet2.415"
                                    }
                                }
                            }
                        },
                        "2001:10:12:115::1/128": {
                            "route": "2001:10:12:115::1/128",
                            "active": True,
                            "metric": 0,
                            "route_preference": 0,
                            "source_protocol_codes": "L",
                            "source_protocol": "local",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet2.415": {
                                        "outgoing_interface": "GigabitEthernet2.415"
                                    }
                                }
                            }
                        },
                        "2001:10:12:120::/64": {
                            "route": "2001:10:12:120::/64",
                            "active": True,
                            "metric": 0,
                            "route_preference": 0,
                            "source_protocol_codes": "C",
                            "source_protocol": "connected",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet2.420": {
                                        "outgoing_interface": "GigabitEthernet2.420"
                                    }
                                }
                            }
                        },
                        "2001:10:12:120::1/128": {
                            "route": "2001:10:12:120::1/128",
                            "active": True,
                            "metric": 0,
                            "route_preference": 0,
                            "source_protocol_codes": "L",
                            "source_protocol": "local",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet2.420": {
                                        "outgoing_interface": "GigabitEthernet2.420"
                                    }
                                }
                            }
                        },
                        "2001:10:13:90::/64": {
                            "route": "2001:10:13:90::/64",
                            "active": True,
                            "metric": 0,
                            "route_preference": 0,
                            "source_protocol_codes": "C",
                            "source_protocol": "connected",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet3.390": {
                                        "outgoing_interface": "GigabitEthernet3.390"
                                    }
                                }
                            }
                        },
                        "2001:10:13:90::1/128": {
                            "route": "2001:10:13:90::1/128",
                            "active": True,
                            "metric": 0,
                            "route_preference": 0,
                            "source_protocol_codes": "L",
                            "source_protocol": "local",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet3.390": {
                                        "outgoing_interface": "GigabitEthernet3.390"
                                    }
                                }
                            }
                        },
                        "2001:10:13:110::/64": {
                            "route": "2001:10:13:110::/64",
                            "active": True,
                            "metric": 0,
                            "route_preference": 0,
                            "source_protocol_codes": "C",
                            "source_protocol": "connected",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet3.410": {
                                        "outgoing_interface": "GigabitEthernet3.410"
                                    }
                                }
                            }
                        },
                        "2001:10:13:110::1/128": {
                            "route": "2001:10:13:110::1/128",
                            "active": True,
                            "metric": 0,
                            "route_preference": 0,
                            "source_protocol_codes": "L",
                            "source_protocol": "local",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet3.410": {
                                        "outgoing_interface": "GigabitEthernet3.410"
                                    }
                                }
                            }
                        },
                        "2001:10:13:115::/64": {
                            "route": "2001:10:13:115::/64",
                            "active": True,
                            "metric": 0,
                            "route_preference": 0,
                            "source_protocol_codes": "C",
                            "source_protocol": "connected",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet3.415": {
                                        "outgoing_interface": "GigabitEthernet3.415"
                                    }
                                }
                            }
                        },
                        "2001:10:13:115::1/128": {
                            "route": "2001:10:13:115::1/128",
                            "active": True,
                            "metric": 0,
                            "route_preference": 0,
                            "source_protocol_codes": "L",
                            "source_protocol": "local",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet3.415": {
                                        "outgoing_interface": "GigabitEthernet3.415"
                                    }
                                }
                            }
                        },
                        "2001:10:13:120::/64": {
                            "route": "2001:10:13:120::/64",
                            "active": True,
                            "metric": 0,
                            "route_preference": 0,
                            "source_protocol_codes": "C",
                            "source_protocol": "connected",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet3.420": {
                                        "outgoing_interface": "GigabitEthernet3.420"
                                    }
                                }
                            }
                        },
                        "2001:10:13:120::1/128": {
                            "route": "2001:10:13:120::1/128",
                            "active": True,
                            "metric": 0,
                            "route_preference": 0,
                            "source_protocol_codes": "L",
                            "source_protocol": "local",
                            "next_hop": {
                                "outgoing_interface": {
                                    "GigabitEthernet3.420": {
                                        "outgoing_interface": "GigabitEthernet3.420"
                                    }
                                }
                            }
                        },
                        "2001:10:23:90::/64": {
                            "route": "2001:10:23:90::/64",
                            "active": True,
                            "metric": 15360,
                            "route_preference": 90,
                            "source_protocol_codes": "D",
                            "source_protocol": "eigrp",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "FE80::F816:3EFF:FE21:73F6",
                                        "outgoing_interface": "GigabitEthernet2.390"
                                    },
                                    2: {
                                        "index": 2,
                                        "next_hop": "FE80::5C00:80FF:FE02:7",
                                        "outgoing_interface": "GigabitEthernet3.390"
                                    }
                                }
                            }
                        },
                        "2001:10:23:115::/64": {
                            "route": "2001:10:23:115::/64",
                            "active": True,
                            "metric": 50,
                            "route_preference": 115,
                            "source_protocol_codes": "I1",
                            "source_protocol": "isis",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "FE80::5C00:80FF:FE02:7",
                                        "outgoing_interface": "GigabitEthernet3.415"
                                    }
                                }
                            }
                        },
                        "2001:10:23:120::/64": {
                            "route": "2001:10:23:120::/64",
                            "active": True,
                            "metric": 2,
                            "route_preference": 120,
                            "source_protocol_codes": "R",
                            "source_protocol": "rip",
                            "next_hop": {
                                "next_hop_list": {
                                    1: {
                                        "index": 1,
                                        "next_hop": "FE80::5C00:80FF:FE02:7",
                                        "outgoing_interface": "GigabitEthernet3.420"
                                    }
                                }
                            }
                        },
                        "FF00::/8": {
                            "route": "FF00::/8",
                            "active": True,
                            "metric": 0,
                            "route_preference": 0,
                            "source_protocol_codes": "L",
                            "source_protocol": "local",
                            "next_hop": {
                                "outgoing_interface": {
                                    "Null0": {
                                        "outgoing_interface": "Null0"
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