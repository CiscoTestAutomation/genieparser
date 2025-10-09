expected_output = {
    "class_map": {
        "system-cpp-police-forus": {
            "match_evaluation": "match-any",
            "packets": 0,
            "bytes": 0,
            "rate": {"interval": 300, "offered_rate_bps": 0, "drop_rate_bps": 0},
            "match": ["none"],
            "police": {
                "rate_pps": 1000,
                "burst_pkt": 244,
                "conformed": {"bytes": 2371810, "actions": {"transmit": True}},
                "exceeded": {"bytes": 9136400, "actions": {"drop": True}},
            },
        },
        "system-cpp-police-forus-addr-resolution": {
            "match_evaluation": "match-any",
            "packets": 0,
            "bytes": 0,
            "rate": {"interval": 300, "offered_rate_bps": 0, "drop_rate_bps": 0},
            "match": ["none"],
            "police": {
                "rate_pps": 3000,
                "burst_pkt": 732,
                "conformed": {"bytes": 256, "actions": {"transmit": True}},
                "exceeded": {"bytes": 0, "actions": {"drop": True}},
            },
        },
    }
}