expected_output = {
    "clock_state": {"system_status": {"clock_state": "unsynchronized"}},
    "peer": {
        "10.16.2.2": {
            "local_mode": {
                "client": {
                    "delay": 0.0,
                    "jitter": 15937.0,
                    "local_mode": "client",
                    "mode": "unsynchronized",
                    "offset": 0.0,
                    "poll": 64,
                    "reach": 0,
                    "receive_time": 41,
                    "refid": "127.127.1.1",
                    "remote": "10.16.2.2",
                    "configured": True,
                    "stratum": 3,
                }
            }
        },
        "10.36.3.3": {
            "local_mode": {
                "client": {
                    "delay": 0.0,
                    "jitter": 15937.0,
                    "local_mode": "client",
                    "mode": "unsynchronized",
                    "offset": 0.0,
                    "poll": 64,
                    "reach": 0,
                    "receive_time": "-",
                    "refid": ".INIT.",
                    "remote": "10.36.3.3",
                    "configured": True,
                    "stratum": 16,
                }
            }
        },
    },
}
