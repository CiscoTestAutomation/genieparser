expected_output = {
    "TenGigabitEthernet0/3/0.41": {
        "service_policy": {
            "output": {
                "policy_name": {
                    "VLAN51_QoS": {
                        "class_map": {
                            "VLAN51_QoS": {
                                "match_evaluation": "match-all",
                                "packets": 0,
                                "bytes": 0,
                                "rate": {
                                    "interval": 300,
                                    "offered_rate_bps": 0,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["access-group name VLAN51_QoS"],
                                "queueing": True,
                                "queue_limit_packets": "64",
                                "queue_depth": 0,
                                "total_drops": 0,
                                "no_buffer_drops": 0,
                                "pkts_output": 0,
                                "bytes_output": 0,
                                "shape_type": "average",
                                "shape_cir_bps": 80000,
                                "shape_bc_bps": 320,
                                "shape_be_bps": 0,
                                "target_shape_rate": 80000,
                                "police": {
                                    "cir_bps": 8000000,
                                    "pir_bc_bytes": 4000,
                                    "cir_be_bytes": 1000,
                                    "conformed": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {"transmit": True},
                                        "bps": 0,
                                    },
                                    "exceeded": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {"transmit": True},
                                        "bps": 0,
                                    },
                                    "violated": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {"drop": True},
                                        "bps": 0,
                                    },
                                },
                            },
                            "class-default": {
                                "match_evaluation": "match-any",
                                "packets": 0,
                                "bytes": 0,
                                "rate": {
                                    "interval": 300,
                                    "offered_rate_bps": 0,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["any"],
                                "queue_limit_packets": "41666",
                                "queue_depth": 0,
                                "total_drops": 0,
                                "no_buffer_drops": 0,
                                "pkts_output": 0,
                                "bytes_output": 0,
                            },
                        }
                    }
                }
            }
        }
    }
}
