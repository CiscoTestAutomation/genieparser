expected_output = {
    "active_translations": {"dynamic": 3, "extended": 3, "static": 0, "total": 3},
    "cef_punted_pkts": 0,
    "cef_translated_pkts": 0,
    "dynamic_mappings": {
        "inside_source": {
            "id": {
                1: {
                    "access_list": "1",
                    "match": "access-list 1 pool pool1",
                    "pool": {
                        "pool1": {
                            "addr_hash": 0,
                            "allocated": 0,
                            "allocated_percentage": 0,
                            "average_len": 0,
                            "chains": "0/256",
                            "end": "192.168.115.254",
                            "misses": 0,
                            "netmask": "255.255.255.0",
                            "start": "192.168.49.1",
                            "total_addresses": 254,
                            "type": "generic",
                        }
                    },
                    "refcount": 3,
                }
            }
        }
    },
    "expired_translations": 0,
    "hits": 3228980,
    "interfaces": {
        "inside": ["GigabitEthernet0/3/1"],
        "outside": ["GigabitEthernet0/3/0"],
    },
    "ip_alias_add_fail": 0,
    "limit_entry_add_fail": 0,
    "mapping_stats_drop": 0,
    "misses": 3,
    "pool_stats_drop": 0,
    "port_block_alloc_fail": 0,
}
