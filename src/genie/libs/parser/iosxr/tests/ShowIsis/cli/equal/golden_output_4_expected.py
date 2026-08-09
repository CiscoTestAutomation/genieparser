expected_output = {
     "instance": {
        "1": {
            "process_id": "1",
            "vrf": {
                "default": {
                    "system_id": "fc20.2400.06fd",
                    "is_levels": "level-2-only",
                    "manual_area_address": [
                        "49.0000"
                    ],
                    "routing_area_address": [
                        "49.0000"
                    ],
                    "non_stop_forwarding": "Disabled",
                    "most_recent_startup_mode": "Cold Restart",
                    "te_connection_status": "Up",
                    "topology": {
                        "IPv4 Unicast": {
                            "vrf": {
                                "default": {
                                    "level": {
                                        2: {
                                            "generate_style": "Wide",
                                            "accept_style": "Wide",
                                            "metric": 10
                                        }
                                    },
                                    "redistributing": [
                                        "Connected"
                                    ],
                                    "protocols_redistributed": True,
                                    "distance": 115,
                                    "adv_passive_only": False
                                }
                            }
                        },
                        "IPv6 Unicast": {
                            "vrf": {
                                "default": {
                                    "level": {
                                        2: {
                                            "metric": 10
                                        }
                                    },
                                    "protocols_redistributed": False,
                                    "distance": 115,
                                    "adv_passive_only": False
                                }
                            }
                        }
                    },
                    "interfaces": {
                        "Loopback0": {
                            "running_state": "running passively",
                            "configuration_state": "passive in configuration"
                        },
                        "GigabitEthernet0/0/0/0": {
                            "running_state": "running actively",
                            "configuration_state": "active in configuration"
                        },
                        "TenGigE0/0/0/14": {
                            "running_state": "running actively",
                            "configuration_state": "active in configuration"
                        },
                        "TenGigE0/0/0/15": {
                            "running_state": "disabled",
                            "configuration_state": "active in configuration"
                        },
                        "TenGigE0/0/0/16": {
                            "running_state": "disabled",
                            "configuration_state": "active in configuration"
                        },
                        "TenGigE0/0/0/17": {
                            "running_state": "disabled",
                            "configuration_state": "active in configuration"
                        }
                    }
                }
            }
        }
    }
}