expected_output = {
    "test_genie_1": {
        "color": 0,
        "name": "test_genie_1",
        "status": {
            "admin": "down",
            "operational": {
                "since": "05-18 03:50:08.958",
                "state": "down",
                "time_for_state": "00:00:01",
            },
        },
    },
    "test_genie_2": {
        "attributes": {
            "binding_sid": {257: {"allocation_mode": "dynamic", "state": "programmed"}}
        },
        "candidate_paths": {
            "preference": {
                100: {
                    "path_type": {
                        "dynamic": {
                            "metric_type": "TE",
                            "status": "inactive",
                            "weight": 0,
                        }
                    }
                }
            }
        },
        "color": 100,
        "end_point": "10.19.198.239",
        "name": "test_genie_2",
        "status": {
            "admin": "down",
            "operational": {
                "since": "05-18 03:50:09.080",
                "state": "down",
                "time_for_state": "00:00:00",
            },
        },
    },
}
