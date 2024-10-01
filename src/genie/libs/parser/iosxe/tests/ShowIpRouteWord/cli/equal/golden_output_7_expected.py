expected_output = {
    "entry": {
        "0.0.0.0/0": {
            "ip": "0.0.0.0",
            "mask": "0",
            "net": "supernet",
            "known_via": "bgp 100.1",
            "distance": "20",
            "metric": "0",
            "type": "default path",
            "tag_name": "65637",
            "tag_type": "external",
            "update": {
                "from": "100.101.0.12",
                "age": "00:16:36"
            },
            "paths": {
                1: {
                    "nexthop": "100.101.0.12",
                    "from": "100.101.0.12",
                    "age": "00:16:36",
                    "prefer_non_rib_labels": False,
                    "merge_labels": False,
                    "metric": "0",
                    "share_count": "1",
                    "as_hops": "5",
                    "route_tag": "65637",
                    "mpls_label": "none",
                    "mpls_flags": "NSF"
                },
                2: {
                    "nexthop": "100.101.0.8",
                    "from": "100.101.0.8",
                    "age": "00:16:36",
                    "prefer_non_rib_labels": False,
                    "merge_labels": False,
                    "metric": "0",
                    "share_count": "1",
                    "as_hops": "5",
                    "route_tag": "65637",
                    "mpls_label": "none",
                    "mpls_flags": "NSF"
                },
                3: {
                    "nexthop": "100.101.0.4",
                    "from": "100.101.0.4",
                    "age": "00:16:36",
                    "prefer_non_rib_labels": False,
                    "merge_labels": False,
                    "metric": "0",
                    "share_count": "1",
                    "as_hops": "5",
                    "route_tag": "65637",
                    "mpls_label": "none",
                    "mpls_flags": "NSF"
                }
            }
        }
    },
    "total_prefixes": 3
}
