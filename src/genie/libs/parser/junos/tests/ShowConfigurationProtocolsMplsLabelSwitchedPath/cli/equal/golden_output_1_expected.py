expected_output = {
    "configuration": {
        "protocols": {
            "mpls": {
                "label-switched-path": {
                    "to": "10.0.0.1",
                    "revert-timer": "0",
                    "no-cspf": True,
                    "setup-priority": "3",
                    "reservation-priority": "3",
                    "record": True,
                    "inter-domain": True,
                    "primary": {"name": "test_data"},
                }
            }
        }
    }
}
