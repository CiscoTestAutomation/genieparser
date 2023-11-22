expected_output = {
    "SRTE_POL_1": {
        "name": "SRTE_POL_1",
        "color": 1,
        "end_point": "4.4.4.4",
        "owners": "CLI",
        "status": {
            "admin": "up",
            "operational": {
                "state": "up",
                "time_for_state": "00:01:41",
                "since": "10-21 07:10:38.262"
            }
        },
        "candidate_paths": {
            "preference": {
                1 : {
                        "type": "CLI",
                        "path_type": {
                            "dynamic": {
                                "status": "active",
                                "metric_type": "TE",
                                "path_accumulated_metric": 30,
                                "hops": {
                                        1: {
                                            "sid": 24321,
                                            "sid_type": "Prefix-SID",
                                            "local_address": "4.4.4.4",
                                }
                            }
                        }
                    }
                }
            },
        },

        "attributes": {
            "binding_sid": {
                18: {
                    "allocation_mode": "dynamic",
                    "state": "programmed"
                }
            }
        }
    },
}
