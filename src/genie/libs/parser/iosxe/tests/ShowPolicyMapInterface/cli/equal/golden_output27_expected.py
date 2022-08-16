expected_output = {
    "FiveGigabitEthernet1/0/48": {
        "service_policy": {
            "output": {
                "policy_name": {
                    "PWRED-CHILD": {
                        "class_map": {
                            "CWRED": {
                                "bandwidth_kbps": 200000,
                                "bandwidth_percent": 20,
                                "match": [
                                    "dscp ef (46)", 
                                    "dscp af11 (10)", 
                                    "dscp 1"
                                ],
                                "match_evaluation": "match-any",
                                "packets": 0,
                                "queueing": True,
                                "total_drops": 0,
                                "bytes_output": 197438313055,
                                "afd_wred_stats": {
                                    "total_drops_bytes": 0,
                                    "total_drops_packets": 0,
                                    "virtual_class": {
                                        0: {
                                            "afd_weight": 12,
                                            "dscp": 1,
                                            "max": 20,
                                            "min": 10,
                                            "random_drop_bytes": 0,
                                            "random_drop_packets": 0,
                                            "transmit_bytes": 65284071936,
                                            "transmit_packets": 68692637637
                                        },
                                        1: {
                                            "afd_weight": 21,
                                            "dscp": 10,
                                            "max": 30,
                                            "min": 20,
                                            "random_drop_bytes": 0,
                                            "random_drop_packets": 0,
                                            "transmit_bytes": 65807437056,
                                            "transmit_packets": 68696726426
                                        },
                                        2: {
                                            "afd_weight": 29,
                                            "dscp": 46,
                                            "max": 40,
                                            "min": 30,
                                            "random_drop_bytes": 0,
                                            "random_drop_packets": 0,
                                            "transmit_bytes": 66346804063,
                                            "transmit_packets": 68700945419
                                        }
                                    }
                                },
                            },
                            "class-default": {
                                "match": [
                                    "any"
                                ],
                                "match_evaluation": "match-any",
                                "packets": 0,
                                "total_drops": 0,
                                "bytes_output": 3392,
                            }
                        }
                    }
                }
            }
        }
    }
}
