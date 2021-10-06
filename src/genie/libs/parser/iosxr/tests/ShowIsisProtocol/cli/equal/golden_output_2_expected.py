

expected_output = {
    "instance": {
        "test": {
            "process_id": "test",
            "instance": "0",
            "vrf": {
                "default": {
                    "system_id": "2222.22ff.4444",
                    "is_levels": "level-1-2",
                    "manual_area_address": ["49.0001"],
                    "routing_area_address": ["49.0001"],
                    "non_stop_forwarding": "Disabled",
                    "most_recent_startup_mode": "Cold Restart",
                    "te_connection_status": "Down",
                    "topology": {
                        "IPv4 Unicast": {
                            "vrf": {
                                "default": {
                                    "level": {
                                        1: {
                                            "generate_style": "Wide",
                                            "accept_style": "Wide",
                                            "metric": 10,
                                            "ispf_status": "Disabled",
                                        },
                                        2: {
                                            "generate_style": "Wide",
                                            "accept_style": "Wide",
                                            "metric": 10,
                                            "ispf_status": "Disabled",
                                        },
                                    },
                                    "protocols_redistributed": False,
                                    "distance": 115,
                                    "adv_passive_only": False,
                                }
                            }
                        },
                        "IPv6 Unicast": {
                            "vrf": {
                                "default": {
                                    "level": {
                                        1: {
                                            "metric": 10,
                                            "ispf_status": "Disabled"},
                                        2: {
                                            "metric": 10,
                                            "ispf_status": "Disabled"},
                                    },
                                    "protocols_redistributed": False,
                                    "distance": 115,
                                    "adv_passive_only": False,
                                }
                            }
                        },
                    },
                    "interfaces": {
                        "Loopback0": {
                            "running_state": "running actively",
                            "configuration_state": "active in configuration",
                        },
                        "GigabitEthernet0/0/0/0.115": {
                            "running_state": "running actively",
                            "configuration_state": "active in configuration",
                        },
                        "GigabitEthernet0/0/0/1.115": {
                            "running_state": "running actively",
                            "configuration_state": "active in configuration",
                        },
                    },
                }
            },
        },
        "test1": {
            "process_id": "test1",
            "instance": "0",
            "vrf": {
                "VRF1": {
                    "system_id": "2222.22ff.4444",
                    "is_levels": "level-1-2",
                    "manual_area_address": ["49.0001"],
                    "routing_area_address": ["49.0001"],
                    "non_stop_forwarding": "Disabled",
                    "most_recent_startup_mode": "Cold Restart",
                    "te_connection_status": "Down",
                    "topology": {
                        "IPv4 Unicast": {
                            "vrf": {
                                "VRF1": {
                                    "level": {
                                        1: {
                                            "generate_style": "Wide",
                                            "accept_style": "Wide",
                                            "metric": 10,
                                            "ispf_status": "Disabled",
                                        },
                                        2: {
                                            "generate_style": "Wide",
                                            "accept_style": "Wide",
                                            "metric": 10,
                                            "ispf_status": "Disabled",
                                        },
                                    },
                                    "protocols_redistributed": False,
                                    "distance": 115,
                                    "adv_passive_only": False,
                                }
                            }
                        },
                        "IPv6 Unicast": {
                            "vrf": {
                                "VRF1": {
                                    "level": {
                                        1: {
                                            "metric": 10,
                                            "ispf_status": "Disabled"},
                                        2: {
                                            "metric": 10,
                                            "ispf_status": "Disabled"},
                                    },
                                    "protocols_redistributed": False,
                                    "distance": 115,
                                    "adv_passive_only": False,
                                }
                            }
                        },
                    },
                    "interfaces": {
                        "Loopback300": {
                            "running_state": "running actively",
                            "configuration_state": "active in configuration",
                        },
                        "GigabitEthernet0/0/0/0.415": {
                            "running_state": "running actively",
                            "configuration_state": "active in configuration",
                        },
                        "GigabitEthernet0/0/0/1.415": {
                            "running_state": "running actively",
                            "configuration_state": "active in configuration",
                        },
                    },
                }
            },
        },
        "test2": {
            "process_id": "test2",
            "instance": "0",
            "vrf": {
                "VRF1": {
                    "system_id": "0000.0000.0000",
                    "is_levels": "level-1-2",
                    "non_stop_forwarding": "Disabled",
                    "most_recent_startup_mode": "Cold Restart",
                    "te_connection_status": "Down",
                }
            },
        },
    }
}
