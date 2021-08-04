expected_output = {
    "interface": {
        "TenGigE0/2/0/3": {
            "service_policy": {
                "input": {"policy_status": "Service Policy not installed"},
                "output": {
                    "policy_name": {
                        "cap": {
                            "class": {
                                "cap": {
                                    "classification_statistics": {
                                        "matched": {
                                            "packets/bytes": "638/42108",
                                            "rate/kbps": 10,
                                        },
                                        "transmitted": "N/A",
                                        "total_dropped": "N/A",
                                    },
                                    "queueing_statistics": {
                                        "queue_id": 44,
                                        "high_watermark": "0/0",
                                        "inst_queue_len": "0/0",
                                        "avg_queue_len": "0/0",
                                        "taildropped": "0/0",
                                    },
                                },
                                "class-default": {
                                    "classification_statistics": {
                                        "matched": {
                                            "packets/bytes": "0/0",
                                            "rate/kbps": 0,
                                        },
                                        "transmitted": "N/A",
                                        "total_dropped": "N/A",
                                    }
                                },
                            }
                        }
                    }
                },
            }
        }
    }
}
