expected_output = {
    "SRTE_POL_1": {
        "name": "SRTE_POL_1",
        "color": 1,
        "end_point": "4.4.4.4",
        "owners": "CLI",
        "status": {
            "admin": "down",
            "operational": {
                "state": "down",
                "time_for_state": "00:00:06",
                "since": "10-21 07:10:38.262"
            }
        },
        "candidate_paths": {
            "preference": {
                1 : {
                    "type": "CLI",
                        "path_type": {
                            "dynamic": {
                                "status": "inactive",
                                "metric_type": "TE",
                            }
                       }
                },
            },
        },

        "attributes": {
            "binding_sid": {
                18: {
                    "allocation_mode": "dynamic",
                    "state": "programmed"
                }
            },
        }
    }
}
