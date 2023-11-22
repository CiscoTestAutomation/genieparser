expected_output = {
    "FiftyGigE6/0/11": {
        "service_policy": {
            "output": {
                "policy_name": {
                    "parent": {
                        "class_map": {
                            "tc7": {
                                "bytes_output": 0,
                                "match": ["traffic-class " '7'],
                                "match_evaluation": "match-all",
                                "packets": 0,
                                "queue_limit_bytes": 7500000,
                                "queueing": True,
                                "total_drops": 0
                            }
                        }
                    }
                }
            }
        }
    }
}
