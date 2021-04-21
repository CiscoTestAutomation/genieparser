expected_output = {
    "ping": {
        "address": "10.4.1.1",
        "data-bytes": 1400,
        "result": [
            {
                "bytes": 1408,
                "from": "10.4.1.1",
                "icmp-seq": 0,
                "time": "2.246",
                "ttl": 64,
            },
            {
                "bytes": 1408,
                "from": "10.4.1.1",
                "icmp-seq": 1,
                "time": "1.251",
                "ttl": 64,
            },
            {
                "bytes": 1408,
                "from": "10.4.1.1",
                "icmp-seq": 2,
                "time": "22.375",
                "ttl": 64,
            },
            {
                "bytes": 1408,
                "from": "10.4.1.1",
                "icmp-seq": 3,
                "time": "1.078",
                "ttl": 64,
            },
            {
                "bytes": 1408,
                "from": "10.4.1.1",
                "icmp-seq": 4,
                "time": "1.167",
                "ttl": 64,
            },
        ],
        "source": "10.4.1.1",
        "statistics": {
            "loss-rate": 0,
            "received": 5,
            "round-trip": {
                "avg": "5.623",
                "max": "22.375",
                "min": "1.078",
                "stddev": "8.386",
            },
            "send": 5,
        },
    }
}
