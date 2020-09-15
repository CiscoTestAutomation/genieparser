expected_output = {
    "protocols": {
        "rip": {
            "vrf": {
                "default": {
                    "address_family": {
                        "ipv4": {
                            "instance": {
                                "rip": {
                                    "maximum_paths": 4,
                                    "distance": 120,
                                    "incoming_route_metric": {
                                        "list": "21",
                                        "added": "10",
                                    },
                                    "neighbors": {
                                        "10.1.3.3": {
                                            "distance": 120,
                                            "last_update": "00:00:00",
                                        },
                                        "10.1.2.2": {
                                            "distance": 120,
                                            "last_update": "00:00:04",
                                        },
                                    },
                                    "interfaces": {
                                        "GigabitEthernet3.100": {
                                            "summary_address": {"172.16.0.0/17": {}},
                                            "triggered_rip": "no",
                                            "passive": True,
                                            "send_version": "2",
                                            "receive_version": "2",
                                            "key_chain": "1",
                                        }
                                    },
                                    "receive_version": 2,
                                    "outgoing_update_filterlist": {
                                        "outgoing_update_filterlist": "not set"
                                    },
                                    "default_redistribution_metric": 3,
                                    "incoming_update_filterlist": {
                                        "incoming_update_filterlist": "not set"
                                    },
                                    "automatic_network_summarization_in_effect": False,
                                    "output_delay": 50,
                                    "send_version": 2,
                                    "timers": {
                                        "update_interval": 10,
                                        "flush_interval": 23,
                                        "invalid_interval": 21,
                                        "next_update": 8,
                                        "holddown_interval": 22,
                                    },
                                    "network": ["10.0.0.0"],
                                    "redistribute": {
                                        "connected": {},
                                        "rip": {},
                                        "static": {},
                                    },
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
