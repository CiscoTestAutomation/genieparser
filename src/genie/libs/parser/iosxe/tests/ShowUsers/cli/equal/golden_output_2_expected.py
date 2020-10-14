expected_output = {
    "interface": {
        "unknown": {
            "user": {
                "NETCONF(ONEP)": {"idle": "00:00:49", "mode": "com.cisco.ne"},
                "a(ONEP)": {"idle": "00:00:49", "mode": "com.cisco.sy"},
            }
        }
    },
    "line": {
        "1 vty 0": {
            "active": True,
            "host": "idle",
            "idle": "00:00:00",
            "location": "10.24.17.55",
            "user": "developer",
        }
    },
}
