expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "instance": {
                        "1111": {
                            "base_topology_mtid": {
                                "0": {
                                    "router_lsa_max_metric": {
                                        True: {
                                            "condition": "on startup for 300 seconds",
                                            "state": "active",
                                            "time_remaining": "00:03:55",
                                        }
                                    },
                                    "start_time": "00:02:24.554",
                                    "time_elapsed": "00:01:04.061",
                                }
                            },
                            "router_id": "10.4.1.1",
                        }
                    }
                }
            }
        }
    }
}
