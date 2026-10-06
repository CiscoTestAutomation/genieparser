expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "instance": {
                        "UNDERLAY": {
                            "total_neighbors": 3,
                            "interfaces": {
                                "Ethernet1/1": {
                                    "neighbors": {
                                        "20.2.0.1": {
                                            "neighbor_router_id": "20.2.0.1",
                                            "priority": 1,
                                            "state": "full",
                                            "neighbor_role": "-",
                                            "up_time": "01:51:30",
                                            "address": "20.4.0.2"
                                        }
                                    }
                                },
                                "Ethernet1/2": {
                                    "neighbors": {
                                        "20.2.0.2": {
                                            "neighbor_router_id": "20.2.0.2",
                                            "priority": 1,
                                            "state": "full",
                                            "neighbor_role": "-",
                                            "up_time": "01:59:59",
                                            "address": "20.4.0.6"
                                        }
                                    }
                                },
                                "Ethernet1/3": {
                                    "neighbors": {
                                        "20.2.0.3": {
                                            "neighbor_router_id": "20.2.0.3",
                                            "priority": 1,
                                            "state": "full",
                                            "neighbor_role": "-",
                                            "up_time": "01:59:57",
                                            "address": "20.4.0.10"
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
