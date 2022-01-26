expected_output = {
    "testing123456789_987654321_123456789_987654321": {
        "name": "testing123456789_987654321_123456789_987654321",
        "color": 80001,
        "end_point": "1.1.1.1",
        "owners": "CLI",
        "status": {
            "admin": "up",
            "operational": {
                "state": "up",
                "time_for_state": "00:02:46",
                "since": "08-24 20:20:28.539"
            }
        },
        "candidate_paths": {
            "preference": {
                2: {
                    "path_type": {
                        "explicit": {
                            "segment_list": {
                                "R1_2000": {
                                    "status": "inactive",
                                    "weight": 1,
                                    "metric_type": "TE"
                                },
                                "R1_20001": {
                                    "status": "active",
                                    "weight": 1,
                                    "metric_type": "TE",
                                    "hops": {
                                        1: {
                                            "sid": 100071,
                                            "sid_type": "Prefix-SID",
                                            "local_address": "7.7.7.7"
                                        },
                                        2: {
                                            "sid": 100041,
                                            "sid_type": "Prefix-SID",
                                            "local_address": "4.4.4.4"
                                        },
                                        3: {
                                            "sid": 100021,
                                            "sid_type": "Prefix-SID",
                                            "local_address": "2.2.2.2"
                                        },
                                        4: {
                                            "sid": 100011,
                                            "sid_type": "Prefix-SID",
                                            "local_address": "1.1.1.1"
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
                957: {
                    "allocation_mode": "dynamic",
                    "state": "programmed"
                }
            },
            "auto_route": "Include all"
        }
    }
}
