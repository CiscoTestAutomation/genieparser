expected_output = {
    "policy_map": {
        "child-policy": {
            "class": {
                "band-policy": {"bandwidth_kbps": 150000},
                "class-default": {
                    "queue_limit_packets": 100,
                    "random_detect": {
                        "class_val": {
                            "0": {
                                "mark_probability": "1/10",
                                "max_threshold": "50",
                                "min_threshold": "25",
                            },
                            "1": {
                                "mark_probability": "1/10",
                                "max_threshold": "70",
                                "min_threshold": "50",
                            },
                            "2": {
                                "mark_probability": "1/10",
                                "max_threshold": "100",
                                "min_threshold": "80",
                            },
                            "3": {
                                "mark_probability": "1/10",
                                "max_threshold": "100",
                                "min_threshold": "80",
                            },
                            "4": {
                                "mark_probability": "1/10",
                                "max_threshold": "100",
                                "min_threshold": "80",
                            },
                            "5": {
                                "mark_probability": "1/10",
                                "max_threshold": "100",
                                "min_threshold": "80",
                            },
                            "6": {
                                "mark_probability": "1/10",
                                "max_threshold": "100",
                                "min_threshold": "80",
                            },
                            "7": {
                                "mark_probability": "1/10",
                                "max_threshold": "50",
                                "min_threshold": "25",
                            },
                        },
                        "exponential_weight": 4,
                        "wred_type": "packet-based",
                    },
                },
                "high-priority": {"priority": True, "priority_kbps": 2000000},
                "low-priority": {"priority": True, "priority_kbps": 2000000},
                "test-cir": {"bandwidth_kbps": 800000},
            }
        }
    }
}
