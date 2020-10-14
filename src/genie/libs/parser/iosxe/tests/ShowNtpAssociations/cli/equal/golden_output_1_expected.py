expected_output = {
    "clock_state": {
        "system_status": {
            "associations_address": "127.127.1.1",
            "associations_local_mode": "client",
            "clock_offset": 0.0,
            "clock_refid": ".LOCL.",
            "clock_state": "synchronized",
            "clock_stratum": 0,
            "root_delay": 0.0,
        }
    },
    "peer": {
        "10.4.1.1": {
            "local_mode": {
                "client": {
                    "delay": 0.0,
                    "jitter": 15937.0,
                    "mode": "unsynchronized",
                    "offset": 0.0,
                    "poll": 1024,
                    "reach": 0,
                    "receive_time": "-",
                    "refid": ".INIT.",
                    "remote": "10.4.1.1",
                    "stratum": 16,
                    "configured": True,
                    "local_mode": "client",
                }
            }
        },
        "127.127.1.1": {
            "local_mode": {
                "client": {
                    "delay": 0.0,
                    "jitter": 1.204,
                    "mode": "synchronized",
                    "offset": 0.0,
                    "poll": 16,
                    "reach": 377,
                    "receive_time": 6,
                    "refid": ".LOCL.",
                    "remote": "127.127.1.1",
                    "stratum": 0,
                    "configured": True,
                    "local_mode": "client",
                }
            }
        },
        "10.16.2.2": {
            "local_mode": {
                "client": {
                    "delay": 0.0,
                    "jitter": 15937.0,
                    "mode": "unsynchronized",
                    "offset": 0.0,
                    "poll": 1024,
                    "reach": 0,
                    "receive_time": "-",
                    "refid": ".INIT.",
                    "remote": "10.16.2.2",
                    "stratum": 16,
                    "configured": True,
                    "local_mode": "client",
                }
            }
        },
    },
}
