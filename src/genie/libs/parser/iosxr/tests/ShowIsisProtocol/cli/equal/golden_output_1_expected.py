

expected_output = {
    "instance": {
        "TEST": {
            "process_id": "TEST",
            "instance": "0",
            "vrf": {
                "default": {
                    "system_id": "0123.45ff.f077",
                    "is_levels": "level-2-only",
                    "manual_area_address": ["90.0000"],
                    "routing_area_address": ["90.0000"],
                    "non_stop_forwarding": "Disabled",
                    "most_recent_startup_mode": "Cold Restart",
                    "te_connection_status": "Up",
                    "topology": {
                        "IPv4 Unicast": {
                            'vrf': {
                                'default': {
                                    "level": {
                                        2: {
                                            "generate_style": "Wide",
                                            "accept_style": "Wide",
                                            "metric": 100000,
                                            "ispf_status": "Disabled",
                                        }
                                    },
                                    "protocols_redistributed": False,
                                    "distance": 115,
                                    "adv_passive_only": True,
                                }
                            }
                        }
                    },
                    "srlb": {
                        "start": 15000,
                        "end": 15999},
                    "srgb": {
                        "start": 16000,
                        "end": 81534},
                    "interfaces": {
                        "GigabitEthernet0/0/0/1": {
                            "running_state": "running suppressed",
                            "configuration_state": "active in configuration",
                        },
                        "GigabitEthernet0/0/0/2": {
                            "running_state": "running suppressed",
                            "configuration_state": "active in configuration",
                        },
                        "GigabitEthernet0/0/0/3": {
                            "running_state": "running suppressed",
                            "configuration_state": "active in configuration",
                        },
                        "Loopback0": {
                            "running_state": "running passively",
                            "configuration_state": "passive in configuration",
                        },
                        "GigabitEthernet0/0/0/4": {
                            "running_state": "running suppressed",
                            "configuration_state": "active in configuration",
                        },
                        "GigabitEthernet0/0/0/5": {
                            "running_state": "running suppressed",
                            "configuration_state": "active in configuration",
                        },
                        "GigabitEthernet0/0/0/6": {
                            "running_state": "disabled",
                            "configuration_state": "active in configuration",
                        },
                        "GigabitEthernet0/0/0/7": {
                            "running_state": "disabled",
                            "configuration_state": "active in configuration",
                        },
                    },
                }
            },
        }
    }
}
