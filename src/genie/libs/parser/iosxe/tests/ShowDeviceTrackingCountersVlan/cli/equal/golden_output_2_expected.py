expected_output = {
    "vlanid":{
        20:{
            "received":{
                "ndp":{
                    "REDIR": 1,
                },
            },
            "received_broadcast_multicast":{
                "ndp":{
                    "REDIR":1,
                },
            },
            "bridged":{

            },
            "broadcast_multicast_to_unicast":{

            },
            "probe":{

            },
            "limited_broadcast_to_local":{

            },
            "dropped":{
                "Routing Proxy": {
                    "protocol": "ndp",
                    "message": "redir",
                    "dropped": 1,
                    "reason": {
                        1: {
                            "reason": "Stop other ND"
                        }
                    }
                }
            },
            "faults":[

            ],
        }
    }
}
