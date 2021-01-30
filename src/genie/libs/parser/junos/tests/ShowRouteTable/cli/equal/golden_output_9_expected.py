expected_output = {
    "table_name": {
        "TESTVPN.inet.0": {
            "active_route_count": 3,
            "destination_count": 3,
            "hidden_route_count": 0,
            "holddown_route_count": 0,
            "routes": {
                "192.168.51.0/30": {
                    "active_tag": "*",
                    "age": "00:41:59",
                    "next_hop": {
                        "next_hop_list": {
                            1: {
                                "to": ">",
                                "via": "xe-1/0/0.0"
                            }
                        }
                    },
                    "preference": "0",
                    "protocol_name": "Direct"
                },
                "192.168.51.1/32": {
                    "active_tag": "*",
                    "age": "00:41:59",
                    "next_hop": {
                        "next_hop_list": {
                            1: {
                                "to": "Local",
                                "via": "xe-1/0/0.0"
                            }
                        }
                    },
                    "preference": "0",
                    "protocol_name": "Local"
                },
                "192.168.61.0/30": {
                    "active_tag": "*",
                    "age": "00:25:19",
                    "learned_from": "27.93.202.40",
                    "local_preference": "100",
                    "next_hop": {
                        "next_hop_list": {
                            1: {
                                "best_route": ">",
                                "mpls_label": "Push 16, Push 299792(top)",
                                "to": "27.93.202.49",
                                "via": "xe-2/0/0.0"
                            }
                        }
                    },
                    "preference": "170",
                    "protocol_name": "BGP"
                }
            },
            "total_route_count": 3
        }
    }
}