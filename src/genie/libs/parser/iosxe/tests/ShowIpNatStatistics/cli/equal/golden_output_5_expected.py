expected_output = {
    "active_translations": {"dynamic": 5, "extended": 5, "static": 0, "total": 5},
    "dynamic_mappings": {
        "inside_source": {
            "id": {
                1: {
                    "match": "route-map NAT-MAP pool inside-pool",
                    "pool": {
                        "inside-pool": {
                            "allocated": 1,
                            "allocated_percentage": 100,
                            "end": "10.49.1.1",
                            "id": 1,
                            "misses": 0,
                            "netmask": "255.255.255.0",
                            "start": "10.49.1.1",
                            "total_addresses": 1,
                            "type": "generic",
                        }
                    },
                    "refcount": 6,
                    "route_map": "NAT-MAP",
                }
            }
        }
    },
    "expired_translations": 0,
    "hits": 11178,
    "in_to_out_drops": 0,
    "interfaces": {
        "inside": ["GigabitEthernet0/0/0"],
        "outside": ["GigabitEthernet0/0/1"],
    },
    "ip_alias_add_fail": 0,
    "limit_entry_add_fail": 0,
    "mapping_stats_drop": 0,
    "misses": 8,
    "nat_limit_statistics": {"max_entry": {"max_allowed": 0, "missed": 0, "used": 0}},
    "out_to_in_drops": 0,
    "pool_stats_drop": 0,
    "port_block_alloc_fail": 0,
}
