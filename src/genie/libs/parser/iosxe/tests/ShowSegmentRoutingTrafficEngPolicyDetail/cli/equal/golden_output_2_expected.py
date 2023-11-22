expected_output = {
    "r5-s": {
        "name": "r5-s",
        "color": 102,
        "end_point": "5.5.5.5",
        "owners": "CLI",
        "status": {
            "admin": "up",
            "operational": {
                "state": "up",
                "time_for_state": "20:10:54",
                "since": "08-25 10:31:14.279"
            }
        },
        "candidate_paths": {
            "preference": {
                1: {
                    "path_type": {
                        "explicit": {
                            "segment_list": {
                                "to-R5-s": {
                                    "status": "active",
                                    "weight": 1,
                                    "metric_type": "TE",
                                    "hops": {
                                        1: {
                                            "sid": 16052,
                                            "sid_type": "Prefix-SID",
                                            "local_address": "5.5.5.5"
                                        }
                                    }
                                }
                            }
                        }
                    },
                    "type": "CLI"
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
            "auto_route": "Include all (Strict)"
        },
        "tunnel_id": "65537",
        "interface_handle": "0x81",
        "stats": {
            "packets": 32,
            "bytes": 2680
        },
        "event_history": {
            1: {
                "timestamp": "08-20 14:31:31.046",
                "client": "FH Resolution",
                "event_type": "REOPT triggered",
                "context": {
                    "Status": "REOPTIMIZED CP: 1"
                }
            },
            2: {
                "timestamp": "08-20 14:31:31.090",
                "client": "FH Resolution",
                "event_type": "REOPT triggered",
                "context": {
                    "Status": "REOPTIMIZED CP: 1"
                }
            },
            3: {
                "timestamp": "08-20 14:31:43.795",
                "client": "FH Resolution",
                "event_type": "REOPT triggered",
                "context": {
                    "Status": "REOPTIMIZED CP: 1"
                }
            },
            4: {
                "timestamp": "08-24 11:22:13.235",
                "client": "CLI",
                "event_type": "Policy ADMIN DOWN",
                "context": {
                    "shutdown": "r5-s"
                }
            },
            5: {
                "timestamp": "08-24 11:22:15.369",
                "client": "CLI",
                "event_type": "Policy state DOWN",
                "context": {
                    "no shutdown": "r5-s"
                }
            },
            6: {
                "timestamp": "09-09 20:15:58.969",
                "client": "CLI AGENT",
                "event_type": "Policy created",
                "context": {
                    "Name": "maxsid"
                }
            },
            7: {
                "timestamp": "09-09 20:16:09.573",
                "client": "CLI AGENT",
                "event_type": "Set colour",
                "context": {
                    "Colour": "100"
                }
            },
            8: {
                "timestamp": "09-09 20:16:09.573",
                "client": "CLI AGENT",
                "event_type": "Set end point",
                "context": {
                    "End-point": "10.169.196.241"
                }
            },
            9: {
                "timestamp": "09-09 20:16:23.728",
                "client": "CLI AGENT",
                "event_type": "Set explicit path",
                "context": {
                    "Path option": "maxsid"
                }
            },
            10: {
                "timestamp": "09-09 20:19:30.195",
                "client": "FH Resolution",
                "event_type": "Policy state UP",
                "context": {
                    "Status": "PATH RESOLVED"
                }
            },
            11: {
                "timestamp": "09-09 20:19:30.202",
                "client": "FH Resolution",
                "event_type": "REOPT triggered",
                "context": {
                    "Status": "REOPTIMIZED"
                }
            },
            12: {
                "timestamp": "09-09 20:56:19.877",
                "client": "FH Resolution",
                "event_type": "REOPT triggered",
                "context": {
                    "Status": "REOPTIMIZED"
                }
            },
            13: {
                "timestamp": "09-09 20:57:51.007",
                "client": "CLI AGENT",
                "event_type": "Set binding SID",
                "context": {
                    "BSID": "Binding SID set"
                }
            },
            14: {
                "timestamp": "09-09 21:15:51.840",
                "client": "CLI AGENT",
                "event_type": "Set explicit path",
                "context": {
                    "Path option": "test1"
                }
            },
            15: {
                "timestamp": "09-09 21:19:04.452",
                "client": "CLI AGENT",
                "event_type": "Set explicit path",
                "context": {
                    "Path option": "test1"
                }
            },
            16: {
                "timestamp": "09-09 21:19:04.454",
                "client": "FH Resolution",
                "event_type": "Policy state UP",
                "context": {
                    "Status": "PATH RESOLVED"
                }
            },
            17: {
                "timestamp": "09-09 21:19:04.458",
                "client": "FH Resolution",
                "event_type": "REOPT triggered",
                "context": {
                    "Status": "REOPTIMIZED"
                }
            },
            18: {
                "timestamp": "09-09 21:20:20.811",
                "client": "CLI AGENT",
                "event_type": "Remove path option",
                "context": {
                    "Path option": "300"
                }
            },
            19: {
                "timestamp": "09-09 21:20:20.812",
                "client": "FH Resolution",
                "event_type": "Policy state UP",
                "context": {
                    "Status": "PATH RESOLVED"
                }
            }
        }
    }
}