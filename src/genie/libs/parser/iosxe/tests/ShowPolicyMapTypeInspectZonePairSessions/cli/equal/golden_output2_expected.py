expected_output= {
    "zone_pair": {
        "super-zp": {
            "service_policy_inspect": {
                "super-pmap": {
                    "class_map": {
                        "match-acl-141": {
                            "class_map_type": "match-all",
                            "class_map_match": [
                                "access-group 141"
                            ],
                            "class_map_action": "Inspect",
                        },
                        "match-acl-132": {
                            "class_map_type": "match-all",
                            "class_map_match": [
                                "access-group 132"
                            ],
                            "class_map_action": "Pass",
                            "packets": 0,
                            "bytes": 0
                        },
                        "match-acl-131": {
                            "class_map_type": "match-all",
                            "class_map_match": [
                                "access-group 131"
                            ],
                            "class_map_action": "Inspect",
                            "established_sessions": {
                                "0x00000001": {
                                    "initiator_ip":"12.1.0.1",
                                    "initiator_port": "38012",
                                    "last_heard": "00",
                                    "protocol": "telnet",
                                    "responder_ip": "33.3.3.1",
                                    "responder_port": "23",
                                    "state": "SIS_OPEN",
                                    "created": "00",
                                    "bytes_sent": {
                                        "initiator": "21",
                                        "responder": 31
                                     }
                                }
                            }
                        },
                        "match-ftp": {
                            "class_map_type": "match-any",
                            "class_map_match": [
                                "protocol ftp"
                            ],
                            "class_map_action": "Inspect"
                        },
                        "match-h323": {
                            "class_map_type": "match-any",
                            "class_map_match": [
                                "protocol h323"
                            ],
                            "class_map_action": "Inspect"
                        },
                        "match-rtsp": {
                            "class_map_type": "match-any",
                            "class_map_match": [
                                "protocol rtsp"
                            ],
                            "class_map_action": "Inspect"
                        },
                        "match-sip": {
                            "class_map_type": "match-any",
                            "class_map_match": [
                                "protocol sip"
                            ],
                            "class_map_action": "Inspect"
                        },
                        "match-skinny": {
                            "class_map_type": "match-any",
                            "class_map_match": [
                                "protocol skinny"
                            ],
                            "class_map_action": "Inspect"
                        },
                        "match-tftp": {
                            "class_map_type": "match-any",
                            "class_map_match": [
                                "protocol tftp"
                            ],
                            "class_map_action": "Inspect"
                        },
                        "match-icmp": {
                            "class_map_type": "match-any",
                            "class_map_match": [
                                "protocol icmp"
                            ],
                            "class_map_action": "Inspect",
                            "established_sessions": {
                                "0x00000000": {
                                    "initiator_ip":"11.11.11.11",
                                    "initiator_port": "8",
                                    "last_heard": "00:00:03",
                                    "protocol": "icmp",
                                    "responder_ip": "33.33.33.33",
                                    "responder_port": "45",
                                    "state": "SIS_OPEN",
                                    "created": "00:00:03",
                                    "bytes_sent": {
                                        "initiator": "360",
                                        "responder": 360
                                     }
                                }
                            }
                        },
                        "match-udp": {
                            "class_map_type": "match-any",
                            "class_map_match": [
                                "protocol udp"
                            ],
                            "class_map_action": "Inspect"
                        },
                        "match-tcp": {
                            "class_map_type": "match-any",
                            "class_map_match": [
                                "protocol tcp"
                            ],
                            "class_map_action": "Inspect"
                        },
                        "match-dns": {
                            "class_map_type": "match-any",
                            "class_map_match": [
                                "protocol dns"
                            ],
                            "class_map_action": "Inspect"
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
