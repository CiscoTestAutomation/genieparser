expected_output = {
    "protocols": {
        "rip": {
            "vrf": {
                "default": {
                    "address_family": {
                        "ipv4": {
                            "instance": {
                                "rip": {
                                    "outgoing_update_filterlist": {
                                        "outgoing_update_filterlist": "not set"
                                    },
                                    "automatic_network_summarization_in_effect": False,
                                    "output_delay": 50,
                                    "maximum_paths": 4,
                                    "neighbors": {
                                        "10.1.2.2": {
                                            "distance": 120,
                                            "last_update": "00:00:04",
                                        },
                                        "10.1.3.3": {
                                            "distance": 120,
                                            "last_update": "00:00:00",
                                        },
                                    },
                                    "redistribute": {
                                        "rip": {},
                                        "static": {},
                                        "connected": {},
                                    },
                                    "distance": 120,
                                    "incoming_update_filterlist": {
                                        "incoming_update_filterlist": "not set"
                                    },
                                    "default_redistribution_metric": 3,
                                    "network": ["10.0.0.0"],
                                    "interfaces": {
                                        "GigabitEthernet3.100": {
                                            "triggered_rip": "no",
                                            "summary_address": {"172.16.0.0/17": {}},
                                            "key_chain": "1",
                                            "send_version": "2",
                                            "receive_version": "2",
                                            "passive": True,
                                        }
                                    },
                                    "send_version": 2,
                                    "receive_version": 2,
                                    "timers": {
                                        "update_interval": 10,
                                        "next_update": 8,
                                        "holddown_interval": 22,
                                        "flush_interval": 23,
                                        "invalid_interval": 21,
                                    },
                                    "incoming_route_metric": {
                                        "list": "21",
                                        "added": "10",
                                    },
                                }
                            }
                        }
                    }
                }
            }
        },
        "application": {
            "holddown": 0,
            "flushed": 0,
            "preference": {"single_value": {"all": 4}},
            "incoming_filter_list": "not set",
            "outgoing_filter_list": "not set",
            "update_frequency": 0,
            "maximum_path": 32,
            "invalid": 0,
        },
    }
}
