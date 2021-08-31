expected_output = {
    "tag": {
        "1": {
            "state": {
                "enabled": {
                    "init_nbr": 2,
                    "max_nbr": 64,
                    "full_exp_nbr": 2,
                    "syncing_nbr": 0
                }
            }
        },
        "2": {
            "state": {
                "disabled": {}
            }
        },
        "null": {
            "state": {
                "enabled": {
                    "init_nbr": 2,
                    "max_nbr": 64,
                    "full_exp_nbr": 653,
                    "syncing_nbr": 3,
                    "host": {
                        "VM1_5": {
                            "level": {
                                "L2": {
                                    "interface": {
                                        "Tu26": {
                                            "state": "Syncing",
                                            "timer": "Expired",
                                            "csnp_rcvd": "no",
                                            "init_flood": "no",
                                            "req_size": 0
                                        }
                                    }
                                }
                            }
                        },
                        "VM1_6": {
                            "level": {
                                "L2": {
                                    "interface": {
                                        "Tu32": {
                                            "state": "Syncing",
                                            "timer": "Expired",
                                            "csnp_rcvd": "no",
                                            "init_flood": "no",
                                            "req_size": 0
                                        },
                                        "Tu34": {
                                            "state": "Syncing",
                                            "timer": "Expired",
                                            "csnp_rcvd": "no",
                                            "init_flood": "no",
                                            "req_size": 0
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
