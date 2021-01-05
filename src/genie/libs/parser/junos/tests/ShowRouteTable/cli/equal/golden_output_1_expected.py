expected_output = {
    "table_name": {
        "inet.3": {
            "active_route_count": 3,
            "destination_count": 3,
            "hidden_route_count": 0,
            "holddown_route_count": 0,
            "routes": {
                "10.64.4.4/32": {
                    "active_tag": "*",
                    "age": "03:40:50",
                    "metric": "110",
                    "next_hop": {
                        "next_hop_list": {
                            1: {
                                "best_route": ">",
                                "to": "192.168.220.6",
                                "via": "ge-0/0/1.0",
                            }
                        }
                    },
                    "preference": "9",
                    "protocol_name": "LDP",
                }
            },
            "total_route_count": 3,
        }
    }
}
