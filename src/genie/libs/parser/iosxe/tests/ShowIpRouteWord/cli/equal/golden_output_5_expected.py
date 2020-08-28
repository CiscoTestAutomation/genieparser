expected_output = {
    "entry": {
        "192.168.4.0/25": {
            "distance": "1",
            "advertised_by": "eigrp 10 route-map GENIE_INTO_EIGRP",
            "ip": "192.168.4.0",
            "known_via": "static",
            "mask": "25",
            "metric": "0",
            "paths": {
                1: {
                    "merge_labels": False,
                    "metric": "0",
                    "nexthop": "10.1.11.9",
                    "prefer_non_rib_labels": False,
                    "route_tag": "113",
                    "share_count": "1",
                }
            },
            "redist_via": "eigrp",
            "redist_via_tag": "10",
        }
    },
    "total_prefixes": 1,
}
