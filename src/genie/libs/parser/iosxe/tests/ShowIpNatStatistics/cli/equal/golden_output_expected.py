expected_output = {
    "active_translations": {"dynamic": 3, "extended": 3, "static": 0, "total": 3},
    "cef_punted_pkts": 0,
    "cef_translated_pkts": 0,
    "dynamic_mappings": {
        "inside_source": {
            "id": {
                1: {
                    "access_list": "102",
                    "match": "access-list 102 pool mypool",
                    "pool": {
                        "mypool": {
                            "allocated": 1,
                            "allocated_percentage": 20,
                            "end": "10.5.5.5",
                            "misses": 0,
                            "netmask": "255.255.255.0",
                            "start": "10.5.5.1",
                            "total_addresses": 5,
                            "type": "generic",
                        }
                    },
                    "refcount": 3,
                }
            }
        }
    },
    "expired_translations": 0,
    "hits": 59230465,
    "interfaces": {
        "inside": [
            "TenGigabitEthernet1/0/0,",
            "TenGigabitEthernet1/1/0,",
            "TenGigabitEthernet1/2/0",
            "TenGigabitEthernet1/3/0",
        ],
        "outside": [
            "TenGigabitEthernet2/0/0,",
            "TenGigabitEthernet2/1/0,",
            "TenGigabitEthernet2/2/0",
            "TenGigabitEthernet2/3/0",
        ],
    },
    "ip_alias_add_fail": 0,
    "limit_entry_add_fail": 0,
    "mapping_stats_drop": 0,
    "misses": 3,
    "nat_limit_statistics": {
        "max_entry": {"max_allowed": 2147483647, "missed": 0, "used": 3}
    },
    "pool_stats_drop": 0,
    "port_block_alloc_fail": 0,
}
