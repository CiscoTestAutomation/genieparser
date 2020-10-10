expected_output = {
    "GigabitEthernet0/0/1": {
        "service_policy": {
            "input": {"policy_name": {"TEST": {}}},
            "output": {"policy_name": {"TEST2": {}}},
        }
    },
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
                            }
                        }
                    }
                }
            }
        }
    },
}
