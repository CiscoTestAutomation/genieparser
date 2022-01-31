expected_output = {
    "r5-15-s": {
        "name": "r5-15-s",
        "color": 115,
        "end_point": "15.0.0.15",
        "owners": "CLI",
        "status": {
            "admin": "up",
            "operational": {
                "state": "up",
                "time_for_state": "00:03:41",
                "since": "09-21 14:13:15.629"
            }
        },
        "candidate_paths": {
            "preference": {
                1: {
                    "path_type": {
                        "explicit": {
                            "segment_list": {
                                "to-R5-15-s": {
                                    "status": "active",
                                    "weight": 1,
                                    "metric_type": "TE",
                                    "hops": {
                                        1: {
                                            "sid": 16505,
                                            "sid_type": "Prefix-SID",
                                            "local_address": "15.0.0.15"
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "type": "CLI",
                }
            }
        },
        "attributes": {
            "binding_sid": {
                17: {
                    "allocation_mode": "dynamic",
                    "state": "programmed"
                }
            },
            "auto_route": "Include all (Strict)",
            "auto_route_mode": "relative",
            "auto_route_value": -3
        },
        "tunnel_id": "65756",
        "interface_handle": "0x83",
        "stats": {
            "packets": 0,
            "bytes": 0
        },
        "event_history": {
            1: {
                "timestamp": "09-21 14:13:15.629",
                "client": "CLI",
                "event_type": "Policy created",
                "context": {
                    "Name": "CLI"
                }
            },
            2: {
                "timestamp": "09-21 14:13:15.812",
                "client": "CLI",
                "event_type": "Set colour",
                "context": {
                    "Colour": "115"
                }
            },
            3: {
                "timestamp": "09-21 14:13:15.812",
                "client": "CLI",
                "event_type": "Set end point",
                "context": {
                    "End-point": "15.0.0.15"
                }
            },
            4: {
                "timestamp": "09-21 14:13:16.754",
                "client": "CLI",
                "event_type": "Set explicit path",
                "context": {
                    "Path option": "to-R5-15-s"
                }
            },
            5: {
                "timestamp": "09-21 14:13:16.759",
                "client": "CLI",
                "event_type": "BSID allocated",
                "context": {
                    "FWD": "label 17"
                }
            },
            6: {
                "timestamp": "09-21 14:13:19.815",
                "client": "FH Resolution",
                "event_type": "Policy state UP",
                "context": {
                    "Status": "PATH RESOLVED CP: 1"
                }
            },
            7: {
                "timestamp": "09-21 14:13:19.883",
                "client": "FH Resolution",
                "event_type": "REOPT triggered",
                "context": {
                    "Status": "REOPTIMIZED CP: 1"
                }
            },
            8: {
                "timestamp": "09-21 14:13:28.082",
                "client": "FH Resolution",
                "event_type": "REOPT triggered",
                "context": {
                    "Status": "REOPTIMIZED CP: 1"
                }
            },
            9: {
                "timestamp": "09-21 14:14:31.562",
                "client": "FH Resolution",
                "event_type": "REOPT triggered",
                "context": {
                    "Status": "REOPTIMIZED CP: 1"
                }
            },
            10: {
                "timestamp": "09-21 14:14:31.626",
                "client": "FH Resolution",
                "event_type": "REOPT triggered",
                "context": {
                    "Status": "REOPTIMIZED CP: 1"
                }
            },
            11: {
                "timestamp": "09-21 14:15:36.795",
                "client": "FH Resolution",
                "event_type": "REOPT triggered",
                "context": {
                    "Status": "REOPTIMIZED CP: 1"
                }
            },
            12: {
                "timestamp": "09-21 14:15:44.974",
                "client": "FH Resolution",
                "event_type": "REOPT triggered",
                "context": {
                    "Status": "REOPTIMIZED CP: 1"
                }
            },
            13: {
                "timestamp": "09-21 14:15:52.763",
                "client": "FH Resolution",
                "event_type": "REOPT triggered",
                "context": {
                    "Status": "REOPTIMIZED CP: 1"
                }
            },
            14: {
                "timestamp": "09-21 14:15:53.570",
                "client": "FH Resolution",
                "event_type": "REOPT triggered",
                "context": {
                    "Status": "REOPTIMIZED CP: 1"
                }
            }
        }
    }
}