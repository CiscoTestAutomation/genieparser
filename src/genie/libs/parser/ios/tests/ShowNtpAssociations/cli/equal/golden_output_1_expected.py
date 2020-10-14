expected_output = {
    "clock_state": {
        "system_status": {
            "associations_address": "10.16.2.2",
            "associations_local_mode": "client",
            "clock_offset": 27.027,
            "clock_refid": "127.127.1.1",
            "clock_state": "synchronized",
            "clock_stratum": 3,
            "root_delay": 5.61,
        }
    },
    "peer": {
        "10.16.2.2": {
            "local_mode": {
                "client": {
                    "delay": 5.61,
                    "jitter": 3.342,
                    "mode": "synchronized",
                    "offset": 27.027,
                    "poll": 64,
                    "reach": 7,
                    "receive_time": 25,
                    "refid": "127.127.1.1",
                    "remote": "10.16.2.2",
                    "stratum": 3,
                    "configured": True,
                    "local_mode": "client",
                }
            }
        },
        "10.36.3.3": {
            "local_mode": {
                "client": {
                    "delay": 0.0,
                    "jitter": 15937.0,
                    "mode": "unsynchronized",
                    "offset": 0.0,
                    "poll": 512,
                    "reach": 0,
                    "receive_time": "-",
                    "refid": ".STEP.",
                    "remote": "10.36.3.3",
                    "stratum": 16,
                    "configured": True,
                    "local_mode": "client",
                }
            }
        },
    },
}
