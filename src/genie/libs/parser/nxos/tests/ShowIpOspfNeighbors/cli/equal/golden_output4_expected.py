expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "instance": {
                        "10": {
                            "total_neighbors": 2,
                            "interfaces": {
                                "Ethernet1/1": {
                                    "neighbors": {
                                        "192.0.2.1": {
                                            "neighbor_router_id": "192.0.2.1",
                                            "priority": 1,
                                            "state": "full",
                                            "neighbor_role": "dr",
                                            "up_time": "1d02h",
                                            "address": "192.0.2.1"
                                        }
                                    }
                                },
                                "Ethernet1/2": {
                                    "neighbors": {
                                        "192.0.2.1": {
                                            "neighbor_router_id": "192.0.2.1",
                                            "priority": 0,
                                            "state": "2way",
                                            "neighbor_role": "drother",
                                            "up_time": "00:00:03",
                                            "address": "192.0.2.5"
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
