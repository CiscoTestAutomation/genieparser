expected_output = {
        "vrf": {
            "Default-IP-Routing-Table": {
                "vrf_id": "0",
                "route_source": {
                    "connected": {
                        "networks": 2,
                        "subnets": 43,
                        "overhead": 9260,
                        "memory_bytes": 6480
                    },
                    "static": {
                        "networks": 6,
                        "subnets": 58,
                        "overhead": 19508,
                        "memory_bytes": 9216
                    },
                    "eigrp": {
                        "1": {
                            "networks": 0,
                            "subnets": 0,
                            "overhead": 0,
                            "memory_bytes": 0
                        }
                    },
                    "internal": {
                        "memory_bytes": 210048,
                        "networks": 96,
                    },
                    "ospf": {
                        "100": {
                            "networks": 101,
                            "subnets": 4344,
                            "overhead": 352008,
                            "memory_bytes": 642124,
                            "intra_area": 80,
                            "inter_area": 638,
                            "external_1": 3148,
                            "external_2": 578,
                            "nssa_external_1": 1,
                            "nssa_external_2": 0
                        }
                    },
                    "bgp": {
                        "65448": {
                            "networks": 133,
                            "subnets": 72,
                            "overhead": 43092,
                            "memory_bytes": 31564,
                            "external": 0,
                            "internal": 197,
                            "local": 8
                        }
                    }
                },
                "maximum_paths": 32,
                "removing_queue_size": 0,
                "total_route_source": {
                    "networks": 338,
                    "subnets": 4517,
                    "overhead": 423868,
                    "memory_bytes": 899432
                }
            }
        }
    }
