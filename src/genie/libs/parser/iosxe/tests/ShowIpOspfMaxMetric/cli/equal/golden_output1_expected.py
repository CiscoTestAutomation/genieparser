expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "instance": {
                        "1": {
                            "router_id": "10.4.1.1",
                            "base_topology_mtid": {
                                "0": {
                                    "router_lsa_max_metric": {False: {}},
                                    "start_time": "00:01:58.313",
                                    "time_elapsed": "00:54:43.859",
                                }
                            },
                        },
                        "65109": {
                            "router_id": "10.0.187.164",
                            "base_topology_mtid": {
                                "0": {
                                    "router_lsa_max_metric": {
                                        True: {
                                            "advertise_lsa_metric": 16711680,
                                            "condition": "on startup for 5 seconds",
                                            "state": "inactive",
                                            "unset_reason": "timer expired, Originated for 5 seconds",
                                            "unset_time": "00:02:03.314",
                                            "unset_time_elapsed": "00:54:38.858",
                                        }
                                    },
                                    "start_time": "00:01:58.314",
                                    "time_elapsed": "00:54:43.858",
                                }
                            },
                        },
                    }
                }
            }
        }
    }
}
