expected_output ={
    "DENY_ALL": {
        "statements": {
            10: {
                "actions": {
                    "actions": "drop"
                },
                "conditions": {}
            }
        }
    },
    "PASS_ALL": {
        "statements": {
            10: {
                "actions": {
                    "actions": "pass"
                },
                "conditions": {}
            }
        }
    },
    "V002:EXPORT": {
        "statements": {
            10: {
                "actions": {
                    "actions": "drop"
                },
                "conditions": {}
            },
            20: {
                "actions": {
                    "set_ext_community_rt": [
                        "64911:303712001"
                    ],
                    "set_ext_community_rt_additive": True
                },
                "conditions": {}
            }
        }
    }
}

