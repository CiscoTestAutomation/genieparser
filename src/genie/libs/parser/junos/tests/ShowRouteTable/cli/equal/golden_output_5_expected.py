expected_output = {
    "table_name": {
        "mpls.0": {
            "destination_count": 54,
            "total_route_count": 54,
            "active_route_count": 54,
            "holddown_route_count": 0,
            "hidden_route_count": 0,
            "routes": {
                "118420": {
                    "active_tag": "*",
                    "protocol_name": "VPN",
                    "preference": "170",
                    "age": "31w3d 20:13:54",
                    "next_hop": {
                        "next_hop_list": {
                            1: {
                                "to": "10.19.198.66",
                                "via": "ge-0/0/3.0",
                                "best_route": ">",
                                "mpls_label": "Swap 78",
                            }
                        }
                    },
                }
            },
        }
    }
}
