expected_output = {
    "index": {
        1: {
            "source": "TRAP",
            "name": "RACL Drop(punt to cpu for icmp    ",
            "asic": 0,
            "priority": 1,
            "tc": 2,
            "policy": "system-cpp-default",
            "cir_sw": 2000,
            "cir_hw": 1907,
            "packets_a": 0,
            "bytes_a": 0,
            "packets_d": 0,
            "bytes_d": 0,
        },
        2: {
            "source": "LPTSv4",
            "name": "ICMP IPv4                         ",
            "asic": 0,
            "priority": 1,
            "tc": 3,
            "policy": "system-cpp-police-icmp-v4",
            "cir_sw": 2500,
            "cir_hw": 2384,
            "packets_a": 18260,
            "bytes_a": 3652000,
            "packets_d": 0,
            "bytes_d": 0,
        },
    }
}
