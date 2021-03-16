expected_output = {
    "ping": {
        "address": "10.1.1.1",
        "data_bytes": 101,
        "ip": "10.1.1.1",
        "repeat": 11,
        "result_per_line": [
            "109 bytes from 10.1.1.1: icmp_seq=0 ttl=254 time=5.575 ms",
            "109 bytes from 10.1.1.1: icmp_seq=1 ttl=254 time=4.419 ms",
            "109 bytes from 10.1.1.1: icmp_seq=2 ttl=254 time=3.946 ms",
            "109 bytes from 10.1.1.1: icmp_seq=3 ttl=254 time=4.827 ms",
            "109 bytes from 10.1.1.1: icmp_seq=4 ttl=254 time=4.048 ms",
            "109 bytes from 10.1.1.1: icmp_seq=5 ttl=254 time=4.281 ms",
            "109 bytes from 10.1.1.1: icmp_seq=6 ttl=254 time=2.578 ms",
            "109 bytes from 10.1.1.1: icmp_seq=7 ttl=254 time=3.366 ms",
            "109 bytes from 10.1.1.1: icmp_seq=8 ttl=254 time=4.238 ms",
            "109 bytes from 10.1.1.1: icmp_seq=9 ttl=254 time=3.383 ms",
            "109 bytes from 10.1.1.1: icmp_seq=10 ttl=254 time=2.543 ms"
        ],
        "source": "10.3.3.3",
        "statistics": {
            "received": 11,
            "round_trip": {
                "avg_ms": 3.927,
                "max_ms": 5.575,
                "min_ms": 2.543
            },
            "send": 11,
            "success_rate_percent": 100.0
        },
    }
} 