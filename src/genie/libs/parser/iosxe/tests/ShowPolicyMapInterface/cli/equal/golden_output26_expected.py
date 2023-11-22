expected_output = {
    "TenGigabitEthernet2/0/11": {
        "service_policy": {
            "input": {
                "policy_name": {
                    "set-exp": {
                        "class_map": {
                            "class-default": {
                                "match": [
                                    "any"
                                ],
                                "match_evaluation": "match-any",
                                "packets": 32589133
                            },
                            "dscp-cs1": {
                                "match": [
                                    "dscp cs1 (8)"
                                ],
                                "match_evaluation": "match-all",
                                "packets": 0,
                                "qos_set": {"mpls_experimental_imposition": 1},
                            }
                        }
                    }
                }
            }
        }
    }
}
