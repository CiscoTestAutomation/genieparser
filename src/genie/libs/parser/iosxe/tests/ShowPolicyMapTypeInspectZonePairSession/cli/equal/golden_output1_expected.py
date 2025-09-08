expected_output= {
    "zone_pair": {
        "z1z2": {
            "service_policy_inspect": {
                "pmap": {
                    "class_map": {
                        "cmap": {
                            "class_map_type": "match-any",
                            "class_map_match": [
                                "protocol udp"
                            ],
                            "class_map_action": "Inspect",
                            "established_sessions": {
                                "0x00000000": {
                                    "initiator_ip":"10.1.1.1",
                                    "initiator_port": "10001",
                                    "last_heard": "00:00:13",
                                    "protocol": "udp",
                                    "responder_ip": "20.1.1.1",
                                    "responder_port": "20001",
                                    "state": "SIS_OPEN",
                                    "created": "00:00:22",
                                    "bytes_sent": {
                                        "initiator": "10000",
                                        "responder": 0
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
