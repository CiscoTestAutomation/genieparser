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
                "time_for_state": "02:07:25",
                "since": "08-20 06:52:36.113"
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
            "auto_route": "Include all (Strict)"
        }
    }
}
