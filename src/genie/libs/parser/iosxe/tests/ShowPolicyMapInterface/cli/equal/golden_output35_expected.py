expected_output = {
    "GigabitEthernet1/0/1": {
        "service_policy": {
            "input": {
                "policy_name": {
                    "parent_set_dscp_child_policer": {
                        "class_map": {
                            "class-default": {
                                "match_evaluation": "match-any",
                                "packets": 18068758,
                                "match": ["any"],
                                "qos_set": {"dscp": {"cs6": {}}},
                                "child_policy_name": {
                                    "child_ace_policer": {
                                        "class_map": {
                                            "cm-acl100": {
                                                "match_evaluation": "match-all",
                                                "packets": 18068758,
                                                "match": ["access-group 100"],
                                                "police": {
                                                    "rate_bps": 500000000,
                                                    "burst_bytes": 15625000,
                                                    "conformed": {
                                                        "bytes": 1987633400,
                                                        "actions": {
                                                            "transmit": True
                                                        },
                                                        "bps": 50875000,
                                                    },
                                                    "exceeded": {
                                                        "bytes": 1626118200,
                                                        "actions": {
                                                            "drop": True
                                                        },
                                                        "bps": 41622000,
                                                    },
                                                },
                                            },
                                            "class-default": {
                                                "match_evaluation": "match-any",
                                                "packets": 0,
                                                "match": ["any"],
                                            },
                                        }
                                    }
                                },
                            }
                        }
                    }
                }
            }
        }
    }
}