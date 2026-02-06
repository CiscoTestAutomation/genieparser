expected_output = {
    "static_nexthop_ip_fastreroute": {
        "flags": {
            "primary": "*",
            "no_adjacency": "-",
            "incomplete_adjacency": "=",
            "adjacency": "+",
            "adjacency_downloaded": "DL",
            "adjacency_resolution": "Res",
            "ipfrr_adjacency_index": "Idx"
        },
        "nexthops": [
            {
                "protocol": "IP",
                "primary": True,
                "adj_id": 23,
                "ifnum": 20,
                "address": "100.5.0.2+",
                "idx": 1,
                "dl": 3,
                "res": 0,
                "interface": "Gi0/0/6"
            },
            {
                "protocol": "IP",
                "primary": False,
                "adj_id": 85,
                "ifnum": 21,
                "address": "100.6.0.2+",
                "idx": 1,
                "dl": 3,
                "res": 2,
                "interface": "Gi0/0/7"
            },
            {
                "protocol": "IPv6",
                "primary": True,
                "adj_id": 56,
                "ifnum": 20,
                "address": "2FF:100::2+",
                "idx": 2,
                "dl": 3,
                "res": 0,
                "interface": "Gi0/0/6"
            },
            {
                "protocol": "IPv6",
                "primary": False,
                "adj_id": 82,
                "ifnum": 21,
                "address": "3FF:100::2+",
                "idx": 2,
                "dl": 3,
                "res": 2,
                "interface": "Gi0/0/7"
            }
        ],
        "static_nexthop_resolution_timer_sec": 255,
        "total_nexthop_adjacency_triggered": 8
    }
}