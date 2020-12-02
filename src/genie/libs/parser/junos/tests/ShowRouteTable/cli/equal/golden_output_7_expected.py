expected_output = {
    "table_name": {
        "mpls.0": {
            "active_route_count": 11,
            "destination_count": 11,
            "hidden_route_count": 0,
            "holddown_route_count": 0,
            "routes": {
                "592383": {
                    "active_tag": "*",
                    "age": "00:02:52",
                    "metric": "2",
                    "next_hop": {
                        "next_hop_list": {
                            1: {
                                "best_route": ">",
                                "mpls_label": "Swap 517890",
                                "to": "10.169.14.158",
                                "via": "et-0/0/0.0",
                            }
                        }
                    },
                    "preference": "9",
                    "protocol_name": "LDP",
                    "rt-tag": "0",
                }
            },
            "total_route_count": 11,
        }
    }
}
