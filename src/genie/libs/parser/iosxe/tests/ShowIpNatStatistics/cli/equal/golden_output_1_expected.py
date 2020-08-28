expected_output = {
    "active_translations": {"dynamic": 0, "extended": 0, "static": 0, "total": 0},
    "cef_punted_pkts": 0,
    "cef_translated_pkts": 0,
    "dynamic_mappings": {
        "inside_source": {
            "id": {
                1: {
                    "access_list": "test-robot",
                    "match": "access-list test-robot pool test-robot",
                    "pool": {
                        "test-robot": {
                            "allocated": 0,
                            "allocated_percentage": 0,
                            "end": "10.1.1.1",
                            "misses": 0,
                            "netmask": "255.255.255.252",
                            "start": "10.1.1.1",
                            "total_addresses": 1,
                            "type": "generic",
                        }
                    },
                    "refcount": 0,
                }
            }
        }
    },
    "expired_translations": 11013,
    "hits": 3358708,
    "interfaces": {
        "inside": ["TenGigabitEthernet0/1/0"],
        "outside": ["TenGigabitEthernet0/2/0"],
    },
    "ip_alias_add_fail": 0,
    "limit_entry_add_fail": 0,
    "mapping_stats_drop": 0,
    "misses": 11050,
    "pool_stats_drop": 0,
    "port_block_alloc_fail": 0,
}
