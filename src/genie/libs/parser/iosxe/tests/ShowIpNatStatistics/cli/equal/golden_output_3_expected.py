expected_output = {
    "active_translations": {"dynamic": 1, "extended": 1, "static": 0, "total": 1},
    "cef_punted_pkts": 0,
    "cef_translated_pkts": 4,
    "dynamic_mappings": {
        "inside_source": {
            "id": {
                3: {
                    "access_list": "99",
                    "interface": "Serial0/0",
                    "match": "access-list 99 interface Serial0/0",
                    "refcount": 1,
                }
            }
        }
    },
    "expired_translations": 0,
    "hits": 3,
    "interfaces": {"inside": ["FastEthernet0/0"], "outside": ["Serial0/0"]},
    "misses": 1,
    "queued_pkts": 0,
}
