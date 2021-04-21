expected_output = {
    "vrf": {
        "VRF-1": {
            "maximum_paths": 32,
            "route_source": {
                "application": {
                    "memory_bytes": 0,
                    "networks": 0,
                    "overhead": 0,
                    "replicates": 0,
                    "subnets": 0,
                },
                "bgp": {
                    "65000": {
                        "external": 0,
                        "internal": 1,
                        "local": 0,
                        "memory_bytes": 312,
                        "networks": 1,
                        "overhead": 96,
                        "replicates": 0,
                        "subnets": 0,
                    }
                },
                "connected": {
                    "memory_bytes": 624,
                    "networks": 0,
                    "overhead": 192,
                    "replicates": 0,
                    "subnets": 2,
                },
                "internal": {"memory_bytes": 712, "networks": 1},
                "static": {
                    "memory_bytes": 0,
                    "networks": 0,
                    "overhead": 0,
                    "replicates": 0,
                    "subnets": 0,
                },
            },
            "total_route_source": {
                "memory_bytes": 1648,
                "networks": 2,
                "overhead": 288,
                "replicates": 0,
                "subnets": 2,
            },
            "vrf_id": "0x27",
        }
    }
}
