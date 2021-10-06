expected_output = {
    "maxsid": {
        "name": "maxsid",
        "color": 100,
        "end_point": "10.169.196.241",
        "status": {
            "admin": "up",
            "operational": {
                "state": "up",
                "time_for_state": "04:54:31",
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
            "packets": 1878,
            "bytes": 295606
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
    },
    "test1": {
        "name": "test1",
        "color": 100,
        "end_point": "10.169.196.241",
        "status": {
            "admin": "up",
            "operational": {
                "state": "up",
                "time_for_state": "03:48:03",
                "since": "09-09 21:25:58.933"
            }
        },
        "candidate_paths": {
            "preference": {
                400: {
                    "path_type": {
                        "dynamic": {
                            "status": "inactive",
                            "pce": True,
                            "weight": 0,
                            "metric_type": "TE"
                        }
                    }
                },
                300: {
                    "path_type": {
                        "dynamic": {
                            "status": "active",
                            "weight": 0,
                            "metric_type": "TE",
                            "path_accumulated_metric": 2115,
                            "hops": {
                                1: {
                                    "sid": 16052,
                                    "sid_type": "Prefix-SID",
                                    "local_address": "10.169.14.241"
                                },
                                2: {
                                    "sid": 24,
                                    "sid_type": "Adjacency-SID",
                                    "local_address": "10.169.14.33",
                                    "remote_address": "10.169.14.34"
                                },
                                3: {
                                    "sid": 16063,
                                    "sid_type": "Prefix-SID",
                                    "local_address": "10.169.196.241"
                                }
                            }
                        }
                    }
                },
                200: {
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
                },
                100: {
                    "path_type": {
                        "dynamic": {
                            "status": "inactive",
                            "weight": 0,
                            "metric_type": "TE",
                            "path_accumulated_metric": 2115,
                            "hops": {
                                1: {
                                    "sid": 16052,
                                    "sid_type": "Prefix-SID",
                                    "local_address": "10.169.14.241"
                                },
                                2: {
                                    "sid": 24,
                                    "sid_type": "Adjacency-SID",
                                    "local_address": "10.169.14.33",
                                    "remote_address": "10.169.14.34"
                                },
                                3: {
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
        "attributes": {
            "binding_sid": {
                15000: {
                    "allocation_mode": "explicit",
                    "state": "programmed"
                }
            }
        },
        "forwarding_id": "65536",
        "stats": {
            "packets": 44,
            "bytes": 1748
        },
        "event_history": {
            1: {
                "timestamp": "08-29 14:51:29.074",
                "client": "FH Resolution",
                "event_type": "REOPT triggered",
                "context": {
                    "Status": "REOPTIMIZED"
                }
            },
            2: {
                "timestamp": "08-29 14:51:29.099",
                "client": "FH Resolution",
                "event_type": "REOPT triggered",
                "context": {
                    "Status": "REOPTIMIZED"
                }
            },
            3: {
                "timestamp": "08-29 14:51:29.114",
                "client": "FH Resolution",
                "event_type": "REOPT triggered",
                "context": {
                    "Status": "REOPTIMIZED"
                }
            },
            4: {
                "timestamp": "08-29 14:51:29.150",
                "client": "FH Resolution",
                "event_type": "REOPT triggered",
                "context": {
                    "Status": "REOPTIMIZED"
                }
            },
            5: {
                "timestamp": "08-29 14:51:29.199",
                "client": "FH Resolution",
                "event_type": "REOPT triggered",
                "context": {
                    "Status": "REOPTIMIZED"
                }
            },
            6: {
                "timestamp": "09-09 20:50:52.378",
                "client": "CLI AGENT",
                "event_type": "Set colour",
                "context": {
                    "Colour": "200"
                }
            },
            7: {
                "timestamp": "09-09 20:52:04.236",
                "client": "CLI AGENT",
                "event_type": "Policy ADMIN DOWN",
                "context": {
                    "shutdown": "test1"
                }
            },
            8: {
                "timestamp": "09-09 20:59:06.432",
                "client": "CLI AGENT",
                "event_type": "Policy state DOWN",
                "context": {
                    "no shutdown": "test1"
                }
            },
            9: {
                "timestamp": "09-09 20:59:06.434",
                "client": "FH Resolution",
                "event_type": "Policy state UP",
                "context": {
                    "Status": "PATH RESOLVED"
                }
            },
            10: {
                "timestamp": "09-09 20:59:06.442",
                "client": "FH Resolution",
                "event_type": "REOPT triggered",
                "context": {
                    "Status": "REOPTIMIZED"
                }
            },
            11: {
                "timestamp": "09-09 21:17:36.909",
                "client": "CLI AGENT",
                "event_type": "Set colour",
                "context": {
                    "Colour": "100"
                }
            },
            12: {
                "timestamp": "09-09 21:18:39.057",
                "client": "CLI AGENT",
                "event_type": "Policy ADMIN DOWN",
                "context": {
                    "shutdown": "test1"
                }
            },
            13: {
                "timestamp": "09-09 21:25:58.931",
                "client": "CLI AGENT",
                "event_type": "Policy state DOWN",
                "context": {
                    "no shutdown": "test1"
                }
            },
            14: {
                "timestamp": "09-09 21:25:58.933",
                "client": "FH Resolution",
                "event_type": "Policy state UP",
                "context": {
                    "Status": "PATH RESOLVED"
                }
            },
            15: {
                "timestamp": "09-09 21:25:58.945",
                "client": "FH Resolution",
                "event_type": "REOPT triggered",
                "context": {
                    "Status": "REOPTIMIZED"
                }
            }
        }
    }
}