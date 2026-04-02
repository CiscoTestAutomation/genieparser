expected_output = {
    "HundredGigE1/0/0": {
        "input": {
            "free_count": 494,
            "mac_entries": {
                "0000.0c5d.92f9": {
                    "index": 58,
                    "packets": 1,
                    "bytes": 106,
                    "last_ms": 4038,
                },
                "0004.c059.c060": {
                    "index": 61,
                    "packets": 0,
                    "bytes": 0,
                    "last_ms": 2493135,
                },
                "00b0.64bc.4860": {
                    "index": 64,
                    "packets": 1,
                    "bytes": 106,
                    "last_ms": 20165,
                },
                "0090.f2c9.cc00": {
                    "index": 103,
                    "packets": 12,
                    "bytes": 720,
                    "last_ms": 3117,
                },
            },
            "total_packets": 14,
            "total_bytes": 932,
        },
        "output": {
            "free_count": 511,
            "mac_entries": {
                "0090.f2c9.cc00": {
                    "index": 103,
                    "packets": 8,
                    "bytes": 504,
                    "last_ms": 4311,
                },
            },
            "total_packets": 8,
            "total_bytes": 504,
        },
    }
}
