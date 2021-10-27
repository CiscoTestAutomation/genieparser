expected_output = {
    "tag": {
        "2": {
            "flex_algo": {
                "global": {
                    "level": {
                        "1": {
                            "delay_metric": True
                        }
                    }
                },
                "128": {
                    "level": {
                        "1": {
                            "def_priority": 128,
                            "def_source": "R1-1.00",
                            "def_equal_to_local": True,
                            "def_metric_type": "IGP",
                            "def_prefix_metric": False,
                            "disabled": False,
                            "microloop_avoidance_timer_running": False
                        }
                    },
                    "local_priority": 128,
                    "frr_disabled": False,
                    "microloop_avoidance_disabled": False
                }
            },
            "flex_algo_count": 4,
            "use_delay_metric_advertisement": [
                "Application",
                "Legacy"
            ]
        },
        "1": {
            "flex_algo": {
                "global": {
                    "level": {
                        "1": {
                            "delay_metric": True
                        }
                    }
                },
                "128": {
                    "level": {
                        "1": {
                            "def_priority": 128,
                            "def_source": "R5.00",
                            "def_equal_to_local": True,
                            "def_metric_type": "IGP",
                            "def_prefix_metric": False,
                            "disabled": False,
                            "microloop_avoidance_timer_running": False
                        }
                    },
                    "local_priority": 128,
                    "frr_disabled": False,
                    "microloop_avoidance_disabled": False
                }
            },
            "flex_algo_count": 3,
            "use_delay_metric_advertisement": [
                "Application",
                "Legacy"
            ]
        }
    }
}