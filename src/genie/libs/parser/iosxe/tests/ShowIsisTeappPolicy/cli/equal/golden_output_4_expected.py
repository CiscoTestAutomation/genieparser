expected_output = {
    "tag": {
        "null": {
            "endpoints": {}
        },
        "1": {
            "endpoints": {
                "5.5.5.5": {
                    "interfaces": {
                        "no interface": {
                            "flag": 1,
                            "metric_mode": "none",
                            "last_updated": "1w2d",
                            "sid_type": "strict-spf"
                        },
                        "Tunnel67531": {
                            "flag": 1,
                            "metric_mode": "none",
                            "last_updated": "20:48:22",
                            "sid_type": "strict-spf"
                        },
                        "Tunnel66562": {
                            "flag": 0,
                            "metric_mode": "none",
                            "last_updated": "20:48:30",
                            "sid_type": "spf"
                        }
                    },
                    "level": "L1",
                    "host": "R5.00"
                }
            }
        }
    }
}
