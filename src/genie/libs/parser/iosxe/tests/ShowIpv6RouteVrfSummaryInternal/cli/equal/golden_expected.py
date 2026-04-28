expected_output = {
    "vrf": {
        "demo2": {
            "ipv6_routing_table_name": "demo2",
            "table_id": "1E000004",
            "global_scope": "global",
            "total_entries": 3,
            "default_maximum_paths": 16,
            "route_sources": {
                "connected": {
                    "networks": 0,
                    "overhead": 0,
                    "memory_bytes": 0
                },
                "local": {
                    "networks": 3,
                    "overhead": 600,
                    "memory_bytes": 648
                }
            },
            "total": {
                "networks": 3,
                "overhead": 600,
                "memory_bytes": 648
            },
            "prefix_counts": {
                "/8": 1,
                "/10": 1,
                "/127": 1
            }
        },
        "demo3": {
            "ipv6_routing_table_name": "demo3",
            "table_id": "1E000005",
            "global_scope": "global",
            "total_entries": 3,
            "default_maximum_paths": 16,
            "route_sources": {
                "connected": {
                    "networks": 0,
                    "overhead": 0,
                    "memory_bytes": 0
                },
                "local": {
                    "networks": 3,
                    "overhead": 600,
                    "memory_bytes": 648
                }
            },
            "total": {
                "networks": 3,
                "overhead": 600,
                "memory_bytes": 648
            },
            "prefix_counts": {
                "/8": 1,
                "/10": 1,
                "/127": 1
            }
        },
        "Mgmt-vrf": {
            "ipv6_routing_table_name": "Mgmt-vrf",
            "table_id": "1E000001",
            "global_scope": "global",
            "total_entries": 3,
            "default_maximum_paths": 16,
            "route_sources": {
                "connected": {
                    "networks": 0,
                    "overhead": 0,
                    "memory_bytes": 0
                },
                "local": {
                    "networks": 3,
                    "overhead": 600,
                    "memory_bytes": 648
                }
            },
            "total": {
                "networks": 3,
                "overhead": 600,
                "memory_bytes": 648
            },
            "prefix_counts": {
                "/8": 1,
                "/10": 1,
                "/127": 1
            }
        }
    }
}