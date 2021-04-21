expected_output = {
    "GigabitEthernet0/1/1": {
        "service_policy": {
            "output": {
                "policy_name": {
                    "shape-out": {
                        "class_map": {
                            "class-default": {
                                "bytes": 0,
                                "bytes_output": 0,
                                "match": ["any"],
                                "match_evaluation": "match-any",
                                "no_buffer_drops": 0,
                                "packets": 0,
                                "pkts_output": 0,
                                "queue_depth": 0,
                                "queue_limit_packets": "64",
                                "queueing": True,
                                "rate": {
                                    "drop_rate_bps": 0,
                                    "interval": 300,
                                    "offered_rate_bps": 0,
                                },
                                "shape_bc_bps": 2000,
                                "shape_be_bps": 2000,
                                "shape_cir_bps": 500000,
                                "shape_type": "average",
                                "target_shape_rate": 500000,
                                "total_drops": 0,
                            }
                        }
                    }
                }
            }
        }
    }
}
