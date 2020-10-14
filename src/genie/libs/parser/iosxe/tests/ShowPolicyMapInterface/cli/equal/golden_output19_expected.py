expected_output = {
    "TenGigabitEthernet0/0/0.101": {
        "service_policy": {
            "input": {
                "policy_name": {
                    "L3VPNin": {
                        "class_map": {
                            "ARP_in": {
                                "bytes": 0,
                                "match": ["protocol arp"],
                                "match_evaluation": "match-all",
                                "packets": 0,
                                "police": {
                                    "cir_bc_bytes": 125,
                                    "cir_bps": 100,
                                    "conformed": {
                                        "actions": {"transmit": True},
                                        "bps": 0,
                                        "bytes": 0,
                                        "packets": 0,
                                    },
                                    "exceeded": {
                                        "actions": {"drop": True},
                                        "bps": 0,
                                        "bytes": 0,
                                        "packets": 0,
                                    },
                                    "pir_be_bytes": 658,
                                    "pir_bps": 20000,
                                    "violated": {
                                        "actions": {"drop": True},
                                        "bps": 0,
                                        "bytes": 0,
                                        "packets": 0,
                                    },
                                },
                                "rate": {
                                    "drop_rate_bps": 0,
                                    "interval": 300,
                                    "offered_rate_bps": 0,
                                },
                            }
                        }
                    }
                }
            }
        }
    }
}
