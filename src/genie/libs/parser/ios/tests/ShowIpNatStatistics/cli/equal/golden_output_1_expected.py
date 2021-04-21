expected_output = {
    "active_translations": {"dynamic": 2, "extended": 0, "static": 0, "total": 2},
    "dynamic_mappings": {
        "inside_source": {
            "id": {
                1: {
                    "access_list": "1",
                    "match": "access-list 1 pool net-208",
                    "pool": {
                        "net-208": {
                            "allocated": 2,
                            "allocated_percentage": 14,
                            "end": "172.16.233.221",
                            "misses": 0,
                            "netmask": "255.255.255.240",
                            "start": "172.16.233.208",
                            "total_addresses": 14,
                            "type": "generic",
                        }
                    },
                    "refcount": 2,
                }
            }
        }
    },
    "expired_translations": 2,
    "hits": 135,
    "interfaces": {"inside": ["Ethernet1"], "outside": ["Serial0"]},
    "misses": 5,
}
