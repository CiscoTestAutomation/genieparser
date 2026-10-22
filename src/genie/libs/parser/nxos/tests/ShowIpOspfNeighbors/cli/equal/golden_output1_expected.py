expected_output = {
    "vrf": {
        "default": {
            "address_family": {
                "ipv4": {
                    "instance": {
                        "UNDERLAY": {
                            "total_neighbors": 1,
                            "interfaces": {
                                "Ethernet1/2": {
                                    "neighbors": {
                                        "10.2.0.3": {
                                            "neighbor_router_id": "10.2.0.3",
                                            "priority": 1,
                                            "state": "full",
                                            "neighbor_role": "-",
                                            "up_time": "01:51:39",
                                            "address": "10.4.0.5"
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
