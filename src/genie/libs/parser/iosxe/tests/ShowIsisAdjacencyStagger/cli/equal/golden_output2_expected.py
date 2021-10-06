expected_output = {
    "tag": {
        "1": {
            "state": {
                "enabled": {
                    "init_nbr": 2,
                    "max_nbr": 64,
                    "full_exp_nbr": 2,
                    "syncing_nbr": 0,
                    "host": {
                        "R2": {
                            "level": {
                                "L1L2": {
                                    "interface": {
                                        "Et0/0": {
                                            "state": "Full",
                                            "timer": "NewCfg",
                                            "csnp_rcvd": "yes",
                                            "init_flood": "yes",
                                            "req_size": 0
                                        }
                                    }
                                }
                            }
                        },
                        "R3": {
                            "level": {
                                "L1L2": {
                                    "interface": {
                                        "Et1/0": {
                                            "state": "Full",
                                            "timer": "NewCfg",
                                            "csnp_rcvd": "yes",
                                            "init_flood": "yes",
                                            "req_size": 0
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        },
        "null": {}
    }
}
