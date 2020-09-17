expected_output = {
    "vrf": {
        "VRF1": {
            "vrf_id": "0x2",
            "maximum_paths": 32,
            "total_route_source": {
                "networks": 4,
                "subnets": 23,
                "replicates": 0,
                "overhead": 2688,
                "memory_bytes": 9932,
            },
            "route_source": {
                "connected": {
                    "networks": 0,
                    "subnets": 17,
                    "replicates": 0,
                    "overhead": 1632,
                    "memory_bytes": 5168,
                },
                "static": {
                    "networks": 0,
                    "subnets": 0,
                    "replicates": 0,
                    "overhead": 0,
                    "memory_bytes": 0,
                },
                "internal": {"networks": 4, "memory_bytes": 2936},
                "application": {
                    "networks": 0,
                    "subnets": 0,
                    "replicates": 0,
                    "overhead": 0,
                    "memory_bytes": 0,
                },
                "ospf": {
                    "2": {
                        "networks": 0,
                        "subnets": 1,
                        "replicates": 0,
                        "overhead": 96,
                        "memory_bytes": 308,
                        "intra_area": 1,
                        "inter_area": 0,
                        "external_1": 0,
                        "external_2": 0,
                        "nssa_external_1": 0,
                        "nssa_external_2": 0,
                    }
                },
                "isis": {
                    "test1": {
                        "networks": 0,
                        "subnets": 1,
                        "replicates": 0,
                        "overhead": 96,
                        "memory_bytes": 304,
                        "level_1": 1,
                        "level_2": 0,
                        "inter_area": 0,
                    }
                },
                "eigrp": {
                    "100": {
                        "networks": 0,
                        "subnets": 3,
                        "replicates": 0,
                        "overhead": 672,
                        "memory_bytes": 912,
                    }
                },
                "rip": {
                    "networks": 0,
                    "subnets": 1,
                    "replicates": 0,
                    "overhead": 192,
                    "memory_bytes": 304,
                },
                "bgp": {
                    "65000": {
                        "networks": 0,
                        "subnets": 0,
                        "replicates": 0,
                        "overhead": 0,
                        "memory_bytes": 0,
                        "external": 0,
                        "internal": 0,
                        "local": 0,
                    }
                },
            },
        }
    }
}
