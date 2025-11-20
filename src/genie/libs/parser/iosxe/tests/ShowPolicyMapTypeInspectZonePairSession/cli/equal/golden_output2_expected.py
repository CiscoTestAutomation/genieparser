expected_output= {
    "zone_pair": {
        "in-to-out": {
            "service_policy_inspect": {
                "pl4": {
                    "class_map": {
                        "cl4": {
                            "class_map_type": "match-all",
                            "class_map_match": [
                                "protocol msrpc",
                                "protocol tcp"
                            ],
                            "class_map_action": "Inspect",
                            "terminating_sessions": {
                                "0x00000001": {
                                    "initiator_ip":"61.0.0.10",
                                    "initiator_port": "35176",
                                    "last_heard": "00",
                                    "protocol": "msrpc",
                                    "responder_ip": "170.100.1.3",
                                    "responder_port": "135",
                                    "state": "SIS_CLOSED",
                                    "created": "00",
                                    "bytes_sent": {
                                        "initiator": "72",
                                        "responder": 1
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
