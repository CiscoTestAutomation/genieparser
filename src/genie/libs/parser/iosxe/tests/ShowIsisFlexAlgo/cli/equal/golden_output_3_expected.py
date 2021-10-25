expected_output = {
    "tag": {
        "1": {
            "flex_algo_count": 3,
            "flex_algo": {
                "128": {
                    "level": {
                        "2": {
                            "def_priority": 131,
                            "def_source": "asr1k-25.00",
                            "def_equal_to_local": False,
                            "def_metric_type": "IGP",
                            "def_exclude_any_affinity": [
                                "0x00000000",
                                "0x00000000",
                                "0x00000000",
                                "0x00000000",
                                "0x00000000",
                                "0x00000000",
                                "0x00000200"
                            ],
                            "disabled": False,
                            "microloop_avoidance_timer_running": False
                        }
                    },
                    "local_priority": 128,
                    "frr_disabled": False,
                    "microloop_avoidance_disabled": False
                },
                "129": {
                    "level": {
                        "2": {
                            "def_priority": 132,
                            "def_source": "asr1k-25.00",
                            "def_equal_to_local": False,
                            "def_metric_type": "Delay",
                            "def_include_all_affinity": [
                                "0x00000001",
                                "0x00800000",
                                "0x00000000",
                                "0x00000000",
                                "0x00000000",
                                "0x00000000",
                                "0x00000000",
                                "0x40000000"
                            ],
                            "def_prefix_metric": True,
                            "disabled": False,
                            "microloop_avoidance_timer_running": False
                        }
                    },
                    "local_priority": 128,
                    "frr_disabled": False,
                    "microloop_avoidance_disabled": False
                },
                "130": {
                    "level": {
                        "2": {
                            "def_priority": 133,
                            "def_source": "asr1k-25.00",
                            "def_equal_to_local": False,
                            "def_metric_type": "IGP",
                            "def_include_any_affinity": [
                                "0x00000002"
                            ],
                            "def_prefix_metric": False,
                            "disabled": False,
                            "microloop_avoidance_timer_running": False
                        }
                    },
                    "local_priority": 128,
                    "frr_disabled": False,
                    "microloop_avoidance_disabled": False
                }
            }
        }
    }
}