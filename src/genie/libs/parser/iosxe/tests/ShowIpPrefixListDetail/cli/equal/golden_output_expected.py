expected_output = {
    "prefix_set_name": {
        "test": {
            "sequences": "5 - 25",
            "prefixes": {
                "10.205.0.0/8 8..16 permit": {
                    "refcount": 0,
                    "prefix": "10.205.0.0/8",
                    "sequence": 10,
                    "hit_count": 0,
                    "masklength_range": "8..16",
                    "action": "permit",
                },
                "10.21.0.0/8 8..16 permit": {
                    "refcount": 1,
                    "prefix": "10.21.0.0/8",
                    "sequence": 15,
                    "hit_count": 0,
                    "masklength_range": "8..16",
                    "action": "permit",
                },
                "10.169.0.0/8 16..24 permit": {
                    "refcount": 3,
                    "prefix": "10.169.0.0/8",
                    "sequence": 25,
                    "hit_count": 0,
                    "masklength_range": "16..24",
                    "action": "permit",
                },
                "10.94.0.0/8 24..32 permit": {
                    "refcount": 2,
                    "prefix": "10.94.0.0/8",
                    "sequence": 20,
                    "hit_count": 0,
                    "masklength_range": "24..32",
                    "action": "permit",
                },
                "10.205.0.0/8 8..8 permit": {
                    "refcount": 1,
                    "prefix": "10.205.0.0/8",
                    "sequence": 5,
                    "hit_count": 0,
                    "masklength_range": "8..8",
                    "action": "permit",
                },
            },
            "protocol": "ipv4",
            "refcount": 2,
            "range_entries": 4,
            "count": 5,
            "prefix_set_name": "test",
        }
    }
}
