expected_output = {
    "evi" : {
        "2": {
            "producer" : {
                "L2VPN": {
                    "originator" : {
                        "1.1.1.2": {
                            "etag": "0",
                            "evi": "2",
                            "label": "20012",
                            "mcast_proxy": "IGMP",
                            "producer": "L2VPN",
                            "router_ip": "1.1.1.2",
                            "tunnel_id": "1.1.1.2",
                            "type": "6"
                        }
                    }
                },
                "BGP": {
                    "originator" : {
                        "2.2.2.2": {
                            "etag": "0",
                            "evi": "2",
                            "label": "20012",
                            "mcast_proxy": "IGMP",
                            "producer": "BGP",
                            "router_ip": "2.2.2.2",
                            "tunnel_id": "2.2.2.2",
                            "type": "6"
                        },
                        "3.3.3.2": {
                            "etag": "0",
                            "evi": "2",
                            "label": "20012",
                            "mcast_proxy": "IGMP",
                            "producer": "BGP",
                            "router_ip": "3.3.3.2",
                            "tunnel_id": "3.3.3.2",
                            "type": "6"
                        }
                    }
                }
            }
        }
    }
}
