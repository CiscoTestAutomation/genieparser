expected_output = {
    "vrf": {
        "Default-IP-Routing-Table": {
            "vrf_id": "0",
            "route_source": {
                "application": {
                    "networks": 0,
                    "subnets": 0,
                    "replicates": 0,
                    "overhead": 0,
                    "memory_bytes": 0,
                },
                "connected": {
                    "networks": 0,
                    "subnets": 2,
                    "replicates": 0,
                    "overhead": 192,
                    "memory_bytes": 624,
                },
                "static": {
                    "networks": 0,
                    "subnets": 0,
                    "replicates": 0,
                    "overhead": 0,
                    "memory_bytes": 0,
                },
                "bgp": {
                    "65000": {
                        "networks": 1,
                        "subnets": 0,
                        "replicates": 0,
                        "overhead": 96,
                        "memory_bytes": 312,
                        "external": 0,
                        "internal": 1,
                        "local": 0,
                    }
                },
                "internal": {"networks": 1, "memory_bytes": 712},
            },
            "maximum_paths": 32,
            "total_route_source": {
                "networks": 2,
                "subnets": 2,
                "replicates": 0,
                "overhead": 288,
                "memory_bytes": 1648,
            },
        }
    }
}
