expected_output = {
    "maxsid": {
        "name": "maxsid",
        "color": 100,
        "end_point": "10.169.196.241",
        "status": {
            "admin": "up",
            "operational": {
                "state": "up",
                "time_for_state": "06:35:58",
                "since": "09-09 20:19:30.195"
            }
        },
        "candidate_paths": {
            "preference": {
                200: {
                    "path_type": {
                        "explicit": {
                            "segment_list": {
                                "maxsid": {
                                    "status": "active",
                                    "weight": 0,
                                    "metric_type": "TE",
                                    "hops": {
                                        1: {
                                            "sid": 16071,
                                            "sid_type": "Prefix-SID",
                                            "local_address": "10.189.5.252"
                                        },
                                        2: {
                                            "sid": 16072,
                                            "sid_type": "Prefix-SID",
                                            "local_address": "10.189.5.253"
                                        },
                                        3: {
                                            "sid": 16071,
                                            "sid_type": "Prefix-SID",
                                            "local_address": "10.189.5.252"
                                        },
                                        4: {
                                            "sid": 16072,
                                            "sid_type": "Prefix-SID",
                                            "local_address": "10.189.5.253"
                                        },
                                        5: {
                                            "sid": 16071,
                                            "sid_type": "Prefix-SID",
                                            "local_address": "10.189.5.252"
                                        },
                                        6: {
                                            "sid": 16072,
                                            "sid_type": "Prefix-SID",
                                            "local_address": "10.189.5.253"
                                        },
                                        7: {
                                            "sid": 16071,
                                            "sid_type": "Prefix-SID",
                                            "local_address": "10.189.5.252"
                                        },
                                        8: {
                                            "sid": 16072,
                                            "sid_type": "Prefix-SID",
                                            "local_address": "10.189.5.253"
                                        },
                                        9: {
                                            "sid": 16071,
                                            "sid_type": "Prefix-SID",
                                            "local_address": "10.189.5.252"
                                        },
                                        10: {
                                            "sid": 16072,
                                            "sid_type": "Prefix-SID",
                                            "local_address": "10.189.5.253"
                                        },
                                        11: {
                                            "sid": 16071,
                                            "sid_type": "Prefix-SID",
                                            "local_address": "10.189.5.252"
                                        },
                                        12: {
                                            "sid": 16072,
                                            "sid_type": "Prefix-SID",
                                            "local_address": "10.189.5.253"
                                        },
                                        13: {
                                            "sid": 16063,
                                            "sid_type": "Prefix-SID",
                                            "local_address": "10.169.196.241"
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                100: {
                    "path_type": {
                        "explicit": {
                            "segment_list": {
                                "test1": {
                                    "status": "inactive",
                                    "weight": 0,
                                    "metric_type": "TE",
                                    "hops": {
                                        1: {
                                            "sid": 16072,
                                            "sid_type": "Prefix-SID",
                                            "local_address": "10.189.5.253"
                                        },
                                        2: {
                                            "sid": 16052,
                                            "sid_type": "Prefix-SID",
                                            "local_address": "10.169.14.241"
                                        },
                                        3: {
                                            "sid": 16062,
                                            "sid_type": "Prefix-SID",
                                            "local_address": "10.34.2.251"
                                        },
                                        4: {
                                            "sid": 16063,
                                            "sid_type": "Prefix-SID",
                                            "local_address": "10.169.196.241"
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "attributes": {
            "binding_sid": {
                15001: {
                    "allocation_mode": "explicit",
                    "state": "programmed"
                }
            }
        },
        "forwarding_id": "65537",
        "stats": {
            "packets": 2520,
            "bytes": 397042
        },
        "event_history": {
            1: {
                "timestamp": "09-09 20:15:58.969",
                "client": "CLI AGENT",
                "event_type": "Policy created",
                "context": {
                    "Name": "maxsid"
                }
            },
            2: {
                "timestamp": "09-09 20:16:09.573",
                "client": "CLI AGENT",
                "event_type": "Set colour",
                "context": {
                    "Colour": "100"
                }
            },
            3: {
                "timestamp": "09-09 20:16:09.573",
                "client": "CLI AGENT",
                "event_type": "Set end point",
                "context": {
                    "End-point": "10.169.196.241"
                }
            },
            4: {
                "timestamp": "09-09 20:16:23.728",
                "client": "CLI AGENT",
                "event_type": "Set explicit path",
                "context": {
                    "Path option": "maxsid"
                }
            },
            5: {
                "timestamp": "09-09 20:19:30.195",
                "client": "FH Resolution",
                "event_type": "Policy state UP",
                "context": {
                    "Status": "PATH RESOLVED"
                }
            },
            6: {
                "timestamp": "09-09 20:19:30.202",
                "client": "FH Resolution",
                "event_type": "REOPT triggered",
                "context": {
                    "Status": "REOPTIMIZED"
                }
            },
            7: {
                "timestamp": "09-09 20:56:19.877",
                "client": "FH Resolution",
                "event_type": "REOPT triggered",
                "context": {
                    "Status": "REOPTIMIZED"
                }
            },
            8: {
                "timestamp": "09-09 20:57:51.007",
                "client": "CLI AGENT",
                "event_type": "Set binding SID",
                "context": {
                    "BSID": "Binding SID set"
                }
            },
            9: {
                "timestamp": "09-09 21:15:51.840",
                "client": "CLI AGENT",
                "event_type": "Set explicit path",
                "context": {
                    "Path option": "test1"
                }
            },
            10: {
                "timestamp": "09-09 21:19:04.452",
                "client": "CLI AGENT",
                "event_type": "Set explicit path",
                "context": {
                    "Path option": "test1"
                }
            },
            11: {
                "timestamp": "09-09 21:19:04.454",
                "client": "FH Resolution",
                "event_type": "Policy state UP",
                "context": {
                    "Status": "PATH RESOLVED"
                }
            },
            12: {
                "timestamp": "09-09 21:19:04.458",
                "client": "FH Resolution",
                "event_type": "REOPT triggered",
                "context": {
                    "Status": "REOPTIMIZED"
                }
            },
            13: {
                "timestamp": "09-09 21:20:20.811",
                "client": "CLI AGENT",
                "event_type": "Remove path option",
                "context": {
                    "Path option": "300"
                }
            },
            14: {
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