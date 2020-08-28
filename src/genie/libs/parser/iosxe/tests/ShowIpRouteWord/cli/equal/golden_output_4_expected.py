expected_output = {
    "entry": {
        "0.0.0.0/0": {
            "distance": "1",
            "ip": "0.0.0.0",
            "known_via": "static",
            "mask": "0",
            "metric": "0",
            "net": "supernet",
            "paths": {
                1: {
                    "merge_labels": False,
                    "metric": "0",
                    "nexthop": "10.255.207.129",
                    "prefer_non_rib_labels": False,
                    "share_count": "1",
                }
            },
            "type": "default path",
        }
    },
    "total_prefixes": 1,
}
