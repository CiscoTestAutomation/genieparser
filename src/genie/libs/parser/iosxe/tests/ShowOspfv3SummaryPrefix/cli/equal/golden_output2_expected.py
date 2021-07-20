expected_output = {
    "process_id": {
        "65001": {
            "address_family": "ipv6",
            "router_id": "1.1.1.1",
            "null_route": {
                "5005:0:1::/48": {
                    "null_metric": "<unreachable>"
                },
                "6006:0:1::/48": {
                    "null_metric": "<unreachable>"
                },
            },
            "summary": {
                "2003:0:1::/48": {
                    "sum_tag": 0,
                    "sum_type": "2",
                    "sum_metric": 20,
                },
                "4004:0:1::/48": {
                    "sum_tag": 0,
                    "sum_type": "2",
                    "sum_metric": 20,
                },
            },
        },
    }
}
