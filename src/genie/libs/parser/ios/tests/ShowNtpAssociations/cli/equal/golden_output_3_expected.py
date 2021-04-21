expected_output = {
    "clock_state": {
        "system_status": {
            "associations_address": "192.168.13.57",
            "associations_local_mode": "client",
            "clock_offset": 11.18,
            "clock_refid": "192.168.1.111",
            "clock_state": "synchronized",
            "clock_stratum": 3,
            "root_delay": 7.9,
        }
    },
    "peer": {
        "172.31.32.2": {
            "local_mode": {
                "client": {
                    "configured": True,
                    "delay": 4.2,
                    "jitter": 1.6,
                    "local_mode": "client",
                    "mode": "None",
                    "offset": -8.59,
                    "poll": 1024,
                    "reach": 377,
                    "receive_time": 29,
                    "refid": "172.31.32.1",
                    "remote": "172.31.32.2",
                    "stratum": 5,
                }
            }
        },
        "192.168.13.33": {
            "local_mode": {
                "client": {
                    "configured": True,
                    "delay": 4.1,
                    "jitter": 2.3,
                    "local_mode": "client",
                    "mode": "selected",
                    "offset": 3.48,
                    "poll": 128,
                    "reach": 377,
                    "receive_time": 69,
                    "refid": "192.168.1.111",
                    "remote": "192.168.13.33",
                    "stratum": 3,
                }
            }
        },
        "192.168.13.57": {
            "local_mode": {
                "client": {
                    "configured": True,
                    "delay": 7.9,
                    "jitter": 3.6,
                    "local_mode": "client",
                    "mode": "synchronized",
                    "offset": 11.18,
                    "poll": 128,
                    "reach": 377,
                    "receive_time": 32,
                    "refid": "192.168.1.111",
                    "remote": "192.168.13.57",
                    "stratum": 3,
                }
            }
        },
    },
}
