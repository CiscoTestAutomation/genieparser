expected_output = {
    "FastEthernet4/1/1": {
        "service_policy": {
            "input": {
                "policy_name": {
                    "mypolicy": {
                        "class_map": {
                            "class1": {
                                "match_evaluation": "match-all",
                                "packets": 500,
                                "bytes": 125000,
                                "rate": {
                                    "interval": 300,
                                    "offered_rate_bps": 4000,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["packet length min 100 max 300"],
                                "qos_set": {
                                    "qos-group": {"20": {"packets_marked": 500}}
                                },
                            }
                        }
                    }
                }
            }
        }
    }
}
