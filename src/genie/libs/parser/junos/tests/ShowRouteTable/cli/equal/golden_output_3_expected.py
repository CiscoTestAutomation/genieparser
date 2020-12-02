expected_output = {
    "table_name": {
        "inet.3": {
            "active_route_count": 3,
            "destination_count": 3,
            "hidden_route_count": 0,
            "holddown_route_count": 0,
            "routes": {
                "10.169.197.254/32": {
                    "active_tag": "*",
                    "age": "02:14:05",
                    "metric": "1001",
                    "next_hop": {
                        "next_hop_list": {
                            1: {
                                "best_route": ">",
                                "to": "10.49.0.1",
                                "via": "ge-0/0/2.0",
                            }
                        }
                    },
                    "preference": "9",
                    "protocol_name": "LDP",
                },
                "192.168.36.220/32": {
                    "active_tag": "*",
                    "age": "02:03:22",
                    "metric": "1111",
                    "next_hop": {
                        "next_hop_list": {
                            1: {
                                "best_route": ">",
                                "mpls_label": "Push 307742",
                                "to": "192.168.220.6",
                                "via": "ge-0/0/1.0",
                            }
                        }
                    },
                    "preference": "9",
                    "protocol_name": "LDP",
                },
                "10.64.4.4/32": {
                    "active_tag": "*",
                    "age": "02:30:55",
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
                    "preference2": "4",
                    "protocol_name": "LDP",
                },
            },
            "total_route_count": 3,
        }
    }
}
