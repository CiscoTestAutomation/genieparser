expected_output = {
    "total_peers": 1,
    "vrf": {
        "management": {
            "peer": {
                "1.1.1.1": {
                    "mode": "synchronized",
                    "remote": "1.1.1.1",
                    "local": "2.2.2.2",
                    "stratum": 1,
                    "poll": 64,
                    "reach": 377,
                    "delay": 0.0271,
                    "vrf": "management"
                }
            }
        }
    },
    "clock_state": {
        "system_status": {
            "clock_state": "synchronized",
            "clock_stratum": 1,
            "associations_address": "1.1.1.1",
            "root_delay": 0.0271
        }
    }
}
