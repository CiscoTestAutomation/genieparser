expected_output = {
    "GigabitEthernet5": {
        "service_policy": {
            "input": {
                "policy_name": {
                    "check_exp": {
                        "class_map": {
                            "check_exp": {
                                "match_evaluation": "match-all",
                                "match": [
                                    "ip precedence 2"
                                ],
                                "packets": 792268,
                                "bytes": 87149480,
                                "rate": {
                                    "interval": 300,
                                    "offered_rate_bps": 2298000,
                                    "drop_rate_bps": 0
                                },
                                "qos_set": {
                                    "mpls_experimental_imposition": 1,
                                    "mpls experimental imposition 1": {
                                        "stats": {
                                            "packets_marked": 792268
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
