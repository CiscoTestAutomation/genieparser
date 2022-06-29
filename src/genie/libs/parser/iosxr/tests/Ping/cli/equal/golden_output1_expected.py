expected_output = {
    "ping": {
        "address": "10.4.1.1",
        "data_bytes": 100,
        "repeat": 100,
        "result_per_line": [
            "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!",
            "!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!"
        ],
        "statistics": {
            "received": 100,
            "round_trip": {
                "avg_ms": 2.0,
                "max_ms": 14.0,
                "min_ms": 1.0
            },
            "send": 100,
            "success_rate_percent": 100.0
        },
        "timeout_secs": 2
    }
}