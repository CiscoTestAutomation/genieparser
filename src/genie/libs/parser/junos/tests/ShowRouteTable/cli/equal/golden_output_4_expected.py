expected_output = {
    "table_name": {
        "inet.3": {
            "active_route_count": 5,
            "destination_count": 5,
            "hidden_route_count": 0,
            "holddown_route_count": 0,
            "routes": {
                "10.0.0.5/32": {
                    "active_tag": "*",
                    "age": "00:25:43",
                    "metric": "10",
                    "next_hop": {
                        "next_hop_list": {
                            1: {"to": "10.2.94.2", "via": "lt-1/2/0.49"},
                            2: {
                                "best_route": ">",
                                "to": "10.2.3.2",
                                "via": "lt-1/2/0.23",
                            },
                        }
                    },
                    "preference": "9",
                    "protocol_name": "LDP",
                }
            },
            "total_route_count": 5,
        }
    }
}
