expected_output = {
    "entry": {
        "0.0.0.0/0": {
            "distance": "20",
            "ip": "0.0.0.0",
            "known_via": "bgp 65161",
            "mask": "0",
            "metric": "0",
            "net": "supernet",
            "paths": {
                1: {
                    "age": "2d07h",
                    "as_hops": "9",
                    "from": "10.101.146.10",
                    "merge_labels": False,
                    "metric": "0",
                    "mpls_label": "none",
                    "nexthop": "10.101.146.10",
                    "prefer_non_rib_labels": False,
                    "route_tag": "65161",
                    "share_count": "1",
                }
            },
            "redist_via": "ospf",
            "redist_via_tag": "1",
            "tag_name": "65161",
            "tag_type": "external",
            "type": "default path",
            "update": {"age": "2d07h", "from": "10.101.146.10"},
        }
    },
    "total_prefixes": 1,
}
