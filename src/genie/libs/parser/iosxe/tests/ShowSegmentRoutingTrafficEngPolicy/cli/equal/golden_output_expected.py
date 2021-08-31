expected_output = {
    "test1": {
        "name": "test1",
        "color": 100,
        "end_point": "10.169.196.241",
        "status": {
            "admin": "up",
            "operational": {
                "state": "up",
                "time_for_state": "09:38:18",
                "since": "08-28 20:56:55.275"
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
                            "metric_type": "IGP",
                            "path_accumulated_metric": 2200,
                            "hops": {
                                1: {
                                    "sid": 16063,
                                    "sid_type": "Prefix-SID",
                                    "local_address": "10.169.196.241"
                                },
                                2: {
                                    "sid": 16072,
                                    "sid_type": "Prefix-SID",
                                    "local_address": "10.189.5.253",
                                    "remote_address": "10.189.6.253"
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
                                            "local_address": "10.189.5.253",
                                            "remote_address": "10.189.6.253"
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
                            "metric_type": "IGP",
                            "path_accumulated_metric": 2200,
                            "hops": {
                                1: {
                                    "sid": 16063
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
        }
    }
}