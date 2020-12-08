expected_output = {
    "clock_state": {
        "system_status": {
            "associations_address": "172.16.229.65",
            "associations_local_mode": "active",
            "clock_offset": 73.819,
            "clock_refid": ".GNSS.",
            "clock_state": "synchronized",
            "clock_stratum": 1,
            "root_delay": 1.436,
        }
    },
    "peer": {
        "10.2.2.2": {
            "local_mode": {
                "active": {
                    "delay": 1.47,
                    "jitter": 52.506,
                    "mode": "falseticker",
                    "offset": -46.76,
                    "poll": 128,
                    "reach": 271,
                    "receive_time": 84,
                    "refid": "172.16.229.65",
                    "remote": "10.2.2.2",
                    "stratum": 2,
                    "type": "active",
                }
            }
        },
        "172.16.229.65": {
            "local_mode": {
                "active": {
                    "delay": 1.436,
                    "jitter": 10.905,
                    "mode": "synchronized",
                    "offset": 73.819,
                    "poll": 64,
                    "reach": 377,
                    "receive_time": 59,
                    "refid": ".GNSS.",
                    "remote": "172.16.229.65",
                    "stratum": 1,
                    "type": "active",
                }
            }
        },
        "172.16.229.66": {
            "local_mode": {
                "active": {
                    "delay": 0.969,
                    "jitter": 8.964,
                    "mode": "final selection set",
                    "offset": 59.428,
                    "poll": 64,
                    "reach": 377,
                    "receive_time": 63,
                    "refid": ".GNSS.",
                    "remote": "172.16.229.66",
                    "stratum": 1,
                    "type": "active",
                }
            }
        },
        "10.145.32.44": {
            "local_mode": {
                "active": {
                    "delay": 42.72,
                    "jitter": 6.228,
                    "mode": "final selection set",
                    "offset": 64.267,
                    "poll": 64,
                    "reach": 377,
                    "receive_time": 61,
                    "refid": ".GNSS.",
                    "remote": "10.145.32.44",
                    "stratum": 1,
                    "type": "active",
                }
            }
        },
    },
}
