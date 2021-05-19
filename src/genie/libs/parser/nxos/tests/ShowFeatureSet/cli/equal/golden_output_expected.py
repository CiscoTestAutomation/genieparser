expected_output = {
    "feature": {
        "bash-shell": {"instance": {"1": {"state": "disabled"}}},
        "bgp": {"instance": {"1": {"state": "enabled"}}},
        "eigrp": {
            "instance": {
                "1": {"state": "enabled"},
                "2": {"state": "enabled", "running": "no"},
                "3": {"state": "enabled", "running": "no"},
                "4": {"state": "enabled", "running": "no"},
            }
        },
    }
}
