expected_output= {
    "zone_pair": {
        "zone1-zone2": {
            "service_policy_inspect": {
                "pm": {
                    "class_map": {
                        "cm": {
                            "class_map_type": "match-any",
                            "class_map_match": [
                                "protocol icmp"
                            ],
                            "class_map_action": "Inspect",
                            "established_sessions": {
                                "0x000000EC": {
                                    "initiator_ip":"2002::1",
                                    "initiator_port": "128",
                                    "last_heard": "00",
                                    "protocol": "icmp",
                                    "responder_ip": "3002::1",
                                    "responder_port": "4033",
                                    "state": "SIS_OPEN",
                                    "created": "00",
                                    "bytes_sent": {
                                        "initiator": "1520",
                                        "responder": 1520
                                     }
                                }
                            }
                        },
                        "class-default": {
                            "class_map_type": "match-any",
                            "class_map_match": [
                                "any"
                            ],
                            "class_map_action": "Drop",
                            "packets": 0,
                            "bytes": 0
                        }
                    }
                }
            }
        }
    }
}
