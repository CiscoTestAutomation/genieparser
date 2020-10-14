expected_output = {
    "protocols": {
        "rip": {
            "vrf": {
                "VRF1": {
                    "address_family": {
                        "ipv4": {
                            "instance": {
                                "rip": {
                                    "maximum_paths": 4,
                                    "incoming_update_filterlist": {
                                        "interfaces": {
                                            "GigabitEthernet2.100": {
                                                "per_user": True,
                                                "default": "not set",
                                                "filter": "13",
                                            }
                                        },
                                        "incoming_update_filterlist": "100",
                                    },
                                    "network": ["10.0.0.0"],
                                    "distance": 120,
                                    "receive_version": 2,
                                    "interfaces": {
                                        "GigabitEthernet2.200": {
                                            "triggered_rip": "no",
                                            "key_chain": "none",
                                            "receive_version": "2",
                                            "send_version": "2",
                                        },
                                        "GigabitEthernet3.200": {
                                            "triggered_rip": "no",
                                            "key_chain": "none",
                                            "receive_version": "2",
                                            "send_version": "1 2",
                                        },
                                    },
                                    "outgoing_update_filterlist": {
                                        "interfaces": {
                                            "GigabitEthernet3.100": {
                                                "per_user": True,
                                                "default": "not set",
                                                "filter": "130",
                                            },
                                            "GigabitEthernet2.100": {
                                                "per_user": True,
                                                "default": "not set",
                                                "filter": "150",
                                            },
                                        },
                                        "outgoing_update_filterlist": "150",
                                    },
                                    "output_delay": 50,
                                    "timers": {
                                        "flush_interval": 240,
                                        "next_update": 2,
                                        "update_interval": 30,
                                        "invalid_interval": 180,
                                        "holddown_interval": 180,
                                    },
                                    "neighbors": {
                                        "10.1.2.2": {
                                            "last_update": "00:00:21",
                                            "distance": 120,
                                        },
                                        "10.1.3.3": {
                                            "last_update": "20:33:00",
                                            "distance": 120,
                                        },
                                    },
                                    "redistribute": {
                                        "rip": {},
                                        "static": {},
                                        "connected": {},
                                    },
                                    "send_version": 2,
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
