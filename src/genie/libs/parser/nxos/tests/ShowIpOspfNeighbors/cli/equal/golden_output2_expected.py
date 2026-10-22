expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "instance": {
                        "UNDERLAY": {
                            "total_neighbors": 2,
                            "interfaces": {
                                "Ethernet1/1": {
                                    "neighbors": {
                                        "10.2.0.2": {
                                            "neighbor_router_id": "10.2.0.2",
                                            "priority": 1,
                                            "state": "full",
                                            "neighbor_role": "-",
                                            "up_time": "02:00:19",
                                            "address": "10.4.0.1"
                                        }
                                    }
                                },
                                "Ethernet1/2": {
                                    "neighbors": {
                                        "10.2.0.1": {
                                            "neighbor_router_id": "10.2.0.1",
                                            "priority": 1,
                                            "state": "full",
                                            "neighbor_role": "-",
                                            "up_time": "01:51:38",
                                            "address": "10.4.0.6"
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
