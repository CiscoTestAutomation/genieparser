expected_output = {
    "prefix_set_name": {
        "test6": {
            "sequences": "5 - 20",
            "prefixes": {
                "2001:DB8:2::/64 65..128 permit": {
                    "refcount": 1,
                    "prefix": "2001:DB8:2::/64",
                    "sequence": 10,
                    "hit_count": 0,
                    "action": "permit",
                    "masklength_range": "65..128",
                },
                "2001:DB8:3::/64 64..128 permit": {
                    "refcount": 3,
                    "prefix": "2001:DB8:3::/64",
                    "sequence": 15,
                    "hit_count": 0,
                    "action": "permit",
                    "masklength_range": "64..128",
                },
                "2001:DB8:1::/64 64..64 permit": {
                    "refcount": 1,
                    "prefix": "2001:DB8:1::/64",
                    "sequence": 5,
                    "hit_count": 0,
                    "action": "permit",
                    "masklength_range": "64..64",
                },
            },
            "protocol": "ipv6",
            "refcount": 2,
            "range_entries": 3,
            "count": 4,
            "prefix_set_name": "test6",
        }
    }
}
