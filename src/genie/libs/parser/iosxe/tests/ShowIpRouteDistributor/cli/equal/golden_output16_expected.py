expected_output = {
    "entry": {
        "10.0.0.0/8": {
            "ip": "10.0.0.0",
            "mask": "8",
            "known_via": "static",
            "distance": "1",
            "metric": "0",
            "paths": {
                1: {
                    "nexthop": "192.0.2.1",
                    "prefer_non_rib_labels": False,
                    "merge_labels": False,
                    "metric": "0",
                    "share_count": "1",
                },
            },
        },
    },
    "total_prefixes": 1,
}
