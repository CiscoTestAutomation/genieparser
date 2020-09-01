expected_output = {
    "TenGigabitEthernet0/0/0.101": {
        "service_policy": {
            "input": {
                "policy_name": {
                    "L3VPNin": {
                        "class_map": {
                            "IPP11111": {
                                "match_evaluation": "match-all",
                                "bandwidth_percent": 4,
                                "bandwidth_kbps": 536,
                                "packets": 253,
                                "bytes": 5656,
                                "rate": {
                                    "interval": 300,
                                    "offered_rate_bps": 0,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["ip precedence 6  7"],
                                "queueing": True,
                                "queue_limit_packets": "32",
                                "queue_depth": 98,
                                "total_drops": 666,
                                "no_buffer_drops": 0,
                                "pkts_output": 125,
                                "bytes_output": 253654,
                            }
                        }
                    }
                }
            }
        }
    }
}
