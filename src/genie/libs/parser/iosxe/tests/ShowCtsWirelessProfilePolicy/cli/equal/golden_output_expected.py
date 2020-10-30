expected_output = {
    "policy_name": {
        "xyz-policy": {
            "role_based_enforcement": "ENABLED",
            "inline_tagging": "ENABLED",
            "default_sgt": "100"
        },
        "foo2": {
            "role_based_enforcement": "DISABLED",
            "inline_tagging": "ENABLED",
            "default_sgt": "NOT-DEFINED"
        },
        "foo3": {
            "role_based_enforcement": "DISABLED",
            "inline_tagging": "DISABLED",
            "default_sgt": "65001"
        }
    }
}