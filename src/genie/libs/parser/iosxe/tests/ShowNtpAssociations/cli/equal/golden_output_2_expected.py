expected_output = {
    "peer": {
        "2001:DB8::EEE8": {
            "local_mode": {
                "client": {
                    "remote": "2001:DB8::EEE8",
                    "configured": True,
                    "refid": "2001:DB8::EEE8",
                    "local_mode": "client",
                    "mode": "synchronized",
                    "stratum": 2,
                    "receive_time": 337,
                    "poll": 512,
                    "reach": 377,
                    "delay": 1.957,
                    "offset": -2.107,
                    "jitter": 1.078
                }
            }
        },
        "2001:DB8::EEE7": {
            "local_mode": {
                "client": {
                    "remote": "2001:DB8::EEE7",
                    "configured": True,
                    "refid": "2001:DB8::EEE7",
                    "local_mode": "client",
                    "mode": "candidate",
                    "stratum": 2,
                    "receive_time": 358,
                    "poll": 512,
                    "reach": 377,
                    "delay": 1.955,
                    "offset": -2.214,
                    "jitter": 1.059
                }
            }
        }
    },
    "clock_state": {
        "system_status": {
            "clock_state": "unsynchronized",
            "clock_stratum": 2,
            "associations_address": "2001:DB8::EEE8",
            "root_delay": 1.957,
            "clock_offset": -2.107,
            "clock_refid": "2001:DB8::EEE8",
            "associations_local_mode": "client"
        }
    }
}
