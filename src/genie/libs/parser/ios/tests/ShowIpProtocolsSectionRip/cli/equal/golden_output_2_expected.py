expected_output = {
    "protocols": {
        "rip": {
            "vrf": {
                "VRF1": {
                    "address_family": {
                        "ipv4": {
                            "instance": {
                                "rip": {
                                    "distance": 120,
                                    "network": ["10.0.0.0"],
                                    "maximum_paths": 4,
                                    "timers": {
                                        "holddown_interval": 180,
                                        "update_interval": 30,
                                        "next_update": 2,
                                        "invalid_interval": 180,
                                        "flush_interval": 240,
                                    },
                                    "redistribute": {
                                        "static": {},
                                        "rip": {},
                                        "connected": {},
                                    },
                                    "output_delay": 50,
                                    "neighbors": {
                                        "10.1.3.3": {
                                            "last_update": "20:33:00",
                                            "distance": 120,
                                        },
                                        "10.1.2.2": {
                                            "last_update": "00:00:21",
                                            "distance": 120,
                                        },
                                    },
                                    "receive_version": 2,
                                    "interfaces": {
                                        "GigabitEthernet2.200": {
                                            "key_chain": "none",
                                            "triggered_rip": "no",
                                            "send_version": "2",
                                            "receive_version": "2",
                                        },
                                        "GigabitEthernet3.200": {
                                            "key_chain": "none",
                                            "triggered_rip": "no",
                                            "send_version": "1 2",
                                            "receive_version": "2",
                                        },
                                    },
                                    "outgoing_update_filterlist": {
                                        "outgoing_update_filterlist": "150",
                                        "interfaces": {
                                            "GigabitEthernet2.100": {
                                                "per_user": True,
                                                "filter": "150",
                                                "default": "not set",
                                            },
                                            "GigabitEthernet3.100": {
                                                "per_user": True,
                                                "filter": "130",
                                                "default": "not set",
                                            },
                                        },
                                    },
                                    "incoming_update_filterlist": {
                                        "incoming_update_filterlist": "100",
                                        "interfaces": {
                                            "GigabitEthernet2.100": {
                                                "per_user": True,
                                                "filter": "13",
                                                "default": "not set",
                                            }
                                        },
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
