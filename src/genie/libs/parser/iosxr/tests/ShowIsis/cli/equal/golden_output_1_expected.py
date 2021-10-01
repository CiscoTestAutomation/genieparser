

expected_output = {
    "instance": {
        "test": {
            "process_id": "test",
            "instance": "0",
            "vrf": {
                "default": {
                    "system_id": "3333.33ff.6666",
                    "is_levels": "level-1-2",
                    "manual_area_address": ["49.0002"],
                    "routing_area_address": ["49.0002", "49.0001"],
                    "non_stop_forwarding": "Disabled",
                    "most_recent_startup_mode": "Cold Restart",
                    "te_connection_status": "Down",
                    "topology": {
                        "IPv4 Unicast": {
                            'vrf': {
                                'default': {
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
                                },
                            },
                        },
                        "IPv6 Unicast": {
                            'vrf': {
                                'default': {
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
                        "GigabitEthernet0/0/0/0": {
                            "running_state": "running actively",
                            "configuration_state": "active in configuration",
                        },
                        "GigabitEthernet0/0/0/1": {
                            "running_state": "running actively",
                            "configuration_state": "active in configuration",
                        },
                        "GigabitEthernet0/0/0/2": {
                            "running_state": "running actively",
                            "configuration_state": "active in configuration",
                        },
                        "GigabitEthernet0/0/0/3": {
                            "running_state": "running actively",
                            "configuration_state": "active in configuration",
                        },
                    },
                }
            },
        }
    }
}
