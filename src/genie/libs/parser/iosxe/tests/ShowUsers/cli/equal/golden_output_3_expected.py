expected_output = {
    "line": {
        "0 con 0": {
            "user": "admin",
            "host": "idle",
            "idle": "00:01:30",
            "active": False,
        },
        "2 vty 0": {
            "user": "admin",
            "host": "idle",
            "idle": "00:00:00",
            "active": True,
            "location": "foo-bar.cisco.com",
        },
        "3 vty 1": {
            "user": "admin",
            "host": "idle",
            "idle": "00:01:25",
            "location": "xxx-xxxxxxx-nitro1.cisco.com",
            "active": False,
        },
        "4 vty 2": {
            "user": "admin",
            "host": "idle",
            "idle": "00:12:34",
            "active": False,
            "location": "xxx-xxxxxxx-nitro2.cisco.com",
        },
    },
    "interface": {
        "unknown": {
            "user": {
                "NETCONF(ONEP)": {
                    "mode": "com.cisco.ne",
                    "idle": "00:00:49",
                    "peer_address": "foo-int.cisco.com",
                }
            }
        }
    },
}
