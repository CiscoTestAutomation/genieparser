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
                "since": "08-28 20:56:55.275",
            },
        },
        "candidate_paths": {
            "preference": {
                100: {
                    "constraints": {"affinity": {"include-all": ["green", "blue"]}},
                    "path_type": {
                        "dynamic": {
                            "status": "inactive",
                            "weight": 0,
                            "metric_type": "IGP",
                            "path_accumulated_metric": 2200,
                            "hops": {
                                1: {
                                    "sid": 16063,
                                    "sid_type": "Prefix-SID",
                                    "local_address": "10.169.196.241",
                                }
                            },
                        }
                    },
                }
            }
        },
        "attributes": {
            "binding_sid": {
                15000: {"allocation_mode": "explicit", "state": "programmed"}
            }
        },
    }
}
