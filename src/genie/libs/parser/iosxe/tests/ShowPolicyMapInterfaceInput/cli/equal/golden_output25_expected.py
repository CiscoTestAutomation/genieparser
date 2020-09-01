expected_output = {
    "CUST123-PIN-T5/0/0.20": {
        "service_policy": {
            "input": {
                "policy_name": {
                    "CUST123-PIN-T5/0/0.20": {
                        "class_map": {
                            "class-default": {
                                "match_evaluation": "match-any",
                                "packets": 21211,
                                "bytes": 1442291,
                                "rate": {
                                    "interval": 30,
                                    "offered_rate_bps": 0,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["any"],
                                "police": {
                                    "conformed": {
                                        "packets": 21211,
                                        "bytes": 1442291,
                                        "actions": {
                                            "transmit": True,
                                            "set_mpls_exp_imposition_transmit": "5",
                                        },
                                        "bps": 0,
                                    },
                                    "exceeded": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {
                                            "drop": True,
                                            "set_mpls_exp_imposition_transmit": "5",
                                        },
                                        "bps": 0,
                                    },
                                    "violated": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {
                                            "drop": True,
                                            "set_mpls_exp_imposition_transmit": "5",
                                        },
                                        "bps": 0,
                                    },
                                },
                            },
                            "pe_mgmt_bun_input": {
                                "match_evaluation": "match-any",
                                "packets": 0,
                                "bytes": 0,
                                "rate": {
                                    "interval": 30,
                                    "offered_rate_bps": 0,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["access-group 122"],
                                "police": {
                                    "conformed": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {
                                            "set_mpls_exp_imposition_transmit": "6"
                                        },
                                        "bps": 0,
                                    },
                                    "exceeded": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {
                                            "set_mpls_exp_imposition_transmit": "2"
                                        },
                                        "bps": 0,
                                    },
                                    "violated": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {
                                            "set_mpls_exp_imposition_transmit": "2"
                                        },
                                        "bps": 0,
                                    },
                                },
                            },
                            "pe_mgmt_unb_input": {
                                "match_evaluation": "match-any",
                                "packets": 0,
                                "bytes": 0,
                                "rate": {
                                    "interval": 30,
                                    "offered_rate_bps": 0,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["ip dscp 63"],
                                "police": {
                                    "conformed": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {
                                            "set_mpls_exp_imposition_transmit": "6"
                                        },
                                        "bps": 0,
                                    },
                                    "exceeded": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {
                                            "set_mpls_exp_imposition_transmit": "2"
                                        },
                                        "bps": 0,
                                    },
                                    "violated": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {
                                            "set_mpls_exp_imposition_transmit": "2"
                                        },
                                        "bps": 0,
                                    },
                                },
                            },
                            "pe_ef_input": {
                                "match_evaluation": "match-any",
                                "packets": 0,
                                "bytes": 0,
                                "rate": {
                                    "interval": 30,
                                    "offered_rate_bps": 0,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["dscp cs5 (40) ef (46)"],
                                "police": {
                                    "conformed": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {
                                            "set_mpls_exp_imposition_transmit": "4"
                                        },
                                        "bps": 0,
                                    },
                                    "exceeded": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {"drop": True},
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
                            "pe_af4_in_input": {
                                "match_evaluation": "match-any",
                                "packets": 0,
                                "bytes": 0,
                                "rate": {
                                    "interval": 30,
                                    "offered_rate_bps": 0,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["dscp cs4 (32) af41 (34)"],
                                "police": {
                                    "conformed": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {
                                            "set_mpls_exp_imposition_transmit": "6"
                                        },
                                        "bps": 0,
                                    },
                                    "exceeded": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {
                                            "set_mpls_exp_imposition_transmit": "2"
                                        },
                                        "bps": 0,
                                    },
                                    "violated": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {
                                            "set_mpls_exp_imposition_transmit": "2"
                                        },
                                        "bps": 0,
                                    },
                                },
                            },
                            "pe_af4_out_input": {
                                "match_evaluation": "match-any",
                                "packets": 0,
                                "bytes": 0,
                                "rate": {
                                    "interval": 30,
                                    "offered_rate_bps": 0,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["dscp af42 (36) af43 (38)"],
                                "police": {
                                    "conformed": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {
                                            "set_mpls_exp_imposition_transmit": "2"
                                        },
                                        "bps": 0,
                                    },
                                    "exceeded": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {
                                            "set_mpls_exp_imposition_transmit": "2"
                                        },
                                        "bps": 0,
                                    },
                                    "violated": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {
                                            "set_mpls_exp_imposition_transmit": "2"
                                        },
                                        "bps": 0,
                                    },
                                },
                            },
                            "pe_af3_in_input": {
                                "match_evaluation": "match-any",
                                "packets": 0,
                                "bytes": 0,
                                "rate": {
                                    "interval": 30,
                                    "offered_rate_bps": 0,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["dscp cs3 (24) af31 (26)"],
                                "police": {
                                    "conformed": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {
                                            "set_mpls_exp_imposition_transmit": "6"
                                        },
                                        "bps": 0,
                                    },
                                    "exceeded": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {
                                            "set_mpls_exp_imposition_transmit": "2"
                                        },
                                        "bps": 0,
                                    },
                                    "violated": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {
                                            "set_mpls_exp_imposition_transmit": "2"
                                        },
                                        "bps": 0,
                                    },
                                },
                            },
                            "pe_af3_out_input": {
                                "match_evaluation": "match-any",
                                "packets": 0,
                                "bytes": 0,
                                "rate": {
                                    "interval": 30,
                                    "offered_rate_bps": 0,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["dscp af32 (28) af33 (30)"],
                                "police": {
                                    "conformed": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {
                                            "set_mpls_exp_imposition_transmit": "2"
                                        },
                                        "bps": 0,
                                    },
                                    "exceeded": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {
                                            "set_mpls_exp_imposition_transmit": "2"
                                        },
                                        "bps": 0,
                                    },
                                    "violated": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {
                                            "set_mpls_exp_imposition_transmit": "2"
                                        },
                                        "bps": 0,
                                    },
                                },
                            },
                            "pe_af2_in_input": {
                                "match_evaluation": "match-any",
                                "packets": 3157930,
                                "bytes": 391583320,
                                "rate": {
                                    "interval": 30,
                                    "offered_rate_bps": 0,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["dscp cs2 (16) af21 (18)"],
                                "police": {
                                    "conformed": {
                                        "packets": 171102,
                                        "bytes": 21216648,
                                        "actions": {
                                            "set_mpls_exp_imposition_transmit": "6"
                                        },
                                        "bps": 0,
                                    },
                                    "exceeded": {
                                        "packets": 941,
                                        "bytes": 116684,
                                        "actions": {
                                            "set_mpls_exp_imposition_transmit": "2"
                                        },
                                        "bps": 0,
                                    },
                                    "violated": {
                                        "packets": 2985887,
                                        "bytes": 370249988,
                                        "actions": {
                                            "set_mpls_exp_imposition_transmit": "2"
                                        },
                                        "bps": 0,
                                    },
                                },
                            },
                            "pe_af2_out_input": {
                                "match_evaluation": "match-any",
                                "packets": 0,
                                "bytes": 0,
                                "rate": {
                                    "interval": 30,
                                    "offered_rate_bps": 0,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["dscp af22 (20) af23 (22)"],
                                "police": {
                                    "conformed": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {
                                            "set_mpls_exp_imposition_transmit": "2"
                                        },
                                        "bps": 0,
                                    },
                                    "exceeded": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {
                                            "set_mpls_exp_imposition_transmit": "2"
                                        },
                                        "bps": 0,
                                    },
                                    "violated": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {
                                            "set_mpls_exp_imposition_transmit": "2"
                                        },
                                        "bps": 0,
                                    },
                                },
                            },
                            "pe_af1_in_input": {
                                "match_evaluation": "match-any",
                                "packets": 3157934,
                                "bytes": 391583816,
                                "rate": {
                                    "interval": 30,
                                    "offered_rate_bps": 0,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["dscp cs1 (8) af11 (10)"],
                                "police": {
                                    "conformed": {
                                        "packets": 171176,
                                        "bytes": 21225824,
                                        "actions": {
                                            "set_mpls_exp_imposition_transmit": "6"
                                        },
                                        "bps": 0,
                                    },
                                    "exceeded": {
                                        "packets": 1090,
                                        "bytes": 135160,
                                        "actions": {
                                            "set_mpls_exp_imposition_transmit": "2"
                                        },
                                        "bps": 0,
                                    },
                                    "violated": {
                                        "packets": 2985668,
                                        "bytes": 370222832,
                                        "actions": {
                                            "set_mpls_exp_imposition_transmit": "2"
                                        },
                                        "bps": 0,
                                    },
                                },
                            },
                            "pe_af1_out_input": {
                                "match_evaluation": "match-any",
                                "packets": 0,
                                "bytes": 0,
                                "rate": {
                                    "interval": 30,
                                    "offered_rate_bps": 0,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["dscp af12 (12) af13 (14)"],
                                "police": {
                                    "conformed": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {
                                            "set_mpls_exp_imposition_transmit": "2"
                                        },
                                        "bps": 0,
                                    },
                                    "exceeded": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {
                                            "set_mpls_exp_imposition_transmit": "2"
                                        },
                                        "bps": 0,
                                    },
                                    "violated": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {
                                            "set_mpls_exp_imposition_transmit": "2"
                                        },
                                        "bps": 0,
                                    },
                                },
                            },
                        }
                    }
                }
            }
        }
    }
}
