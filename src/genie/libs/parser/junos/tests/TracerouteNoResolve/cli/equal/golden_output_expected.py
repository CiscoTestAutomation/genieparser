expected_output = {
    "traceroute": {
        "to": {"domain": "example.local", "address": "10.135.0.2"},
        "max-hops": "30",
        "packet-size": "52",
        "hops": [
            {
                "hop-number": "1",
                "router-name": "r1",
                "address": "10.145.0.2",
                "round-trip-time": "1.792 ms  1.142 ms  0.831 ms",
            },
            {
                "hop-number": "2",
                "address": "10.135.0.2",
                "round-trip-time": "1.734 ms  1.234 ms  0.855 ms",
            },
        ],
    }
}
