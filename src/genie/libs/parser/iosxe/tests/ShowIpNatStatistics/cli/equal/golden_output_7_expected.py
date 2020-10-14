expected_output = {
    "active_translations": {
        "dynamic": 3000,
        "extended": 1500,
        "static": 1,
        "total": 3001,
    },
    "cef_punted_pkts": 0,
    "cef_translated_pkts": 0,
    "dynamic_mappings": {
        "inside_source": {
            "id": {
                1: {
                    "access_list": "test",
                    "match": "access-list test pool net-208",
                    "pool": {
                        "net-208": {
                            "addr_hash": 6,
                            "allocated": 1500,
                            "allocated_percentage": 5,
                            "average_len": 5,
                            "chains": "256/256",
                            "end": "10.55.100.254",
                            "id": 1,
                            "misses": 0,
                            "netmask": "255.255.0.0",
                            "start": "10.55.0.1",
                            "total_addresses": 25854,
                            "type": "generic",
                        }
                    },
                    "refcount": 3000,
                }
            }
        }
    },
    "expired_translations": 1,
    "hits": 45392,
    "interfaces": {"inside": ["Vlan88"], "outside": ["Vlan89"]},
    "misses": 0,
}
