expected_output= {
    "zone_pair": {
        "in-out": {
            "service_policy_inspect": {
                "in-out": {
                    "class_map": {
                        "FOO": {
                            "class_map_type": "match-any",
                            "class_map_match": [
                                "protocol icmp",
                                "protocol udp",
                                "protocol tcp"
                            ],
                            "class_map_action": "Inspect",
                            "half_open_sessions": {
                                "0x00000603": {
                                    "initiator_ip":"1.1.1.1",
                                    "initiator_port": "5633",
                                    "last_heard": "00:01:48",
                                    "protocol": "udp",
                                    "responder_ip": "2.2.2.1",
                                    "responder_port": "12609",
                                    "state": "SIS_OPENING",
                                    "created": "00:01:48",
                                    "bytes_sent": {
                                        "initiator": "0",
                                        "responder": 0
                                     }
                                },
                                "0x00000608": {
                                    "initiator_ip":"1.1.1.1",
                                    "initiator_port": "5638",
                                    "last_heard": "00:01:47",
                                    "protocol": "udp",
                                    "responder_ip": "2.2.2.1",
                                    "responder_port": "12614",
                                    "state": "SIS_OPENING",
                                    "created": "00:01:47",
                                    "bytes_sent": {
                                        "initiator": "0",
                                        "responder": 0
                                     }
                                },
                                "0x00000609": {
                                    "initiator_ip":"1.1.1.1",
                                    "initiator_port": "8",
                                    "last_heard": "00:00:15",
                                    "protocol": "icmp",
                                    "responder_ip": "3.3.3.10",
                                    "responder_port": "0",
                                    "state": "SIS_OPENING",
                                    "created": "00:01:11",
                                    "bytes_sent": {
                                        "initiator": "0",
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
