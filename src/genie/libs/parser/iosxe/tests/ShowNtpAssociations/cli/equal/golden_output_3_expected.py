expected_output = {
    "peer": {
        "192.0.2.1": {
            "local_mode": {
                "client": {
                    "remote": "192.0.2.1",
                    "configured": True,
                    "refid": "192.0.2.2",
                    "local_mode": "client",
                    "mode": "synchronized",
                    "stratum": 2,
                    "receive_time": 676,
                    "poll": 1024,
                    "reach": 377,
                    "delay": 0.117,
                    "offset": -3.705,
                    "jitter": 1.09
                }
            }
        },
        "192.0.2.10": {
            "local_mode": {
                "client": {
                    "remote": "192.0.2.10",
                    "configured": True,
                    "refid": ".GNSS.",
                    "local_mode": "client",
                    "mode": "candidate",
                    "stratum": 1,
                    "receive_time": 811,
                    "poll": 1024,
                    "reach": 377,
                    "delay": 0.319,
                    "offset": -3.649,
                    "jitter": 1.053
                }
            }
        },
        "192.0.2.20": {
            "local_mode": {
                "client": {
                    "remote": "192.0.2.20",
                    "configured": True,
                    "refid": "127.0.0.1",
                    "local_mode": "client",
                    "mode": "unsynchronized",
                    "stratum": 16,
                    "receive_time": 375,
                    "poll": 1024,
                    "reach": 0,
                    "delay": 0.0,
                    "offset": 0.0,
                    "jitter": 15937.0
                }
            }
        }
    },
    "clock_state": {
        "system_status": {
            "clock_state": "synchronized",
            "clock_stratum": 2,
            "associations_address": "192.0.2.1",
            "root_delay": 0.117,
            "clock_offset": -3.705,
            "clock_refid": "192.0.2.2",
            "associations_local_mode": "client"
        }
    }
}

