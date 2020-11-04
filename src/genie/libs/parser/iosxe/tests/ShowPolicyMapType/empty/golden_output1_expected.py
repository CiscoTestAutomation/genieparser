expected_output = {
    "Control Plane": {
        "service_policy": {
            "input": {
                "policy_name": {
                    "Control_Plane_In": {
                        "class_map": {
                            "Ping_Class": {
                                "match_evaluation": "match-all",
                                "packets": 0,
                                "bytes": 0,
                                "rate": {
                                    "interval": 300,
                                    "offered_rate_bps": 0,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["access-group name Ping_Option"],
                                "police": {
                                    "cir_bps": 8000,
                                    "cir_bc_bytes": 1500,
                                    "conformed": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {"drop": True},
                                        "bps": 0,
                                    },
                                    "exceeded": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {"drop": True},
                                        "bps": 0,
                                    },
                                },
                            },
                            "TELNET_Class": {
                                "match_evaluation": "match-all",
                                "packets": 0,
                                "bytes": 0,
                                "rate": {
                                    "interval": 300,
                                    "offered_rate_bps": 0,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["access-group name TELNET_Permit"],
                                "police": {
                                    "cir_bps": 8000,
                                    "cir_bc_bytes": 1500,
                                    "conformed": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {"drop": True},
                                        "bps": 0,
                                    },
                                    "exceeded": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {"drop": True},
                                        "bps": 0,
                                    },
                                },
                            },
                            "TACACS_Class": {
                                "match_evaluation": "match-all",
                                "packets": 0,
                                "bytes": 0,
                                "rate": {
                                    "interval": 300,
                                    "offered_rate_bps": 0,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["access-group name TACACS_Permit"],
                                "police": {
                                    "cir_bps": 8000,
                                    "cir_bc_bytes": 1500,
                                    "conformed": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {"drop": True},
                                        "bps": 0,
                                    },
                                    "exceeded": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {"drop": True},
                                        "bps": 0,
                                    },
                                },
                            },
                            "SNMP_Class": {
                                "match_evaluation": "match-all",
                                "packets": 0,
                                "bytes": 0,
                                "rate": {
                                    "interval": 300,
                                    "offered_rate_bps": 0,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["access-group name SNMP_Permit"],
                                "police": {
                                    "cir_bps": 8000,
                                    "cir_bc_bytes": 1500,
                                    "conformed": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {"drop": True},
                                        "bps": 0,
                                    },
                                    "exceeded": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {"drop": True},
                                        "bps": 0,
                                    },
                                },
                            },
                            "FTP_Class": {
                                "match_evaluation": "match-all",
                                "packets": 0,
                                "bytes": 0,
                                "rate": {
                                    "interval": 300,
                                    "offered_rate_bps": 0,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["access-group name FTP_Permit"],
                                "police": {
                                    "cir_bps": 8000,
                                    "cir_bc_bytes": 1500,
                                    "conformed": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {"drop": True},
                                        "bps": 0,
                                    },
                                    "exceeded": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {"drop": True},
                                        "bps": 0,
                                    },
                                },
                            },
                            "BGP_Class": {
                                "match_evaluation": "match-all",
                                "packets": 32,
                                "bytes": 2032,
                                "rate": {
                                    "interval": 300,
                                    "offered_rate_bps": 0,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["access-group name BGP_Permit"],
                                "qos_set": {
                                    "ip precedence": {
                                        "6": {"marker_statistics": "Disabled"}
                                    }
                                },
                            },
                            "OSPF_Class": {
                                "match_evaluation": "match-all",
                                "packets": 58,
                                "bytes": 11788,
                                "rate": {
                                    "interval": 300,
                                    "offered_rate_bps": 0,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["access-group name OSPF_Permit"],
                                "qos_set": {
                                    "ip precedence": {
                                        "6": {"marker_statistics": "Disabled"}
                                    }
                                },
                            },
                            "LDP_Class": {
                                "match_evaluation": "match-all",
                                "packets": 128,
                                "bytes": 9552,
                                "rate": {
                                    "interval": 300,
                                    "offered_rate_bps": 0,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["access-group name LDP_Permit"],
                                "qos_set": {
                                    "ip precedence": {
                                        "6": {"marker_statistics": "Disabled"}
                                    }
                                },
                            },
                            "ICMP_Class1": {
                                "match_evaluation": "match-all",
                                "packets": 0,
                                "bytes": 0,
                                "rate": {
                                    "interval": 300,
                                    "offered_rate_bps": 0,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["access-group name ICMP_Permit1"],
                                "police": {
                                    "cir_bps": 8000,
                                    "cir_bc_bytes": 1500,
                                    "conformed": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {"drop": True},
                                        "bps": 0,
                                    },
                                    "exceeded": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {"drop": True},
                                        "bps": 0,
                                    },
                                },
                            },
                            "ICMP_Class2": {
                                "match_evaluation": "match-all",
                                "packets": 4,
                                "bytes": 482,
                                "rate": {
                                    "interval": 300,
                                    "offered_rate_bps": 0,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["access-group name ICMP_Permit2"],
                                "police": {
                                    "cir_bps": 12000000,
                                    "cir_bc_bytes": 150000,
                                    "conformed": {
                                        "packets": 4,
                                        "bytes": 482,
                                        "actions": {"transmit": True},
                                        "bps": 0,
                                    },
                                    "exceeded": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {"drop": True},
                                        "bps": 0,
                                    },
                                },
                            },
                            "NTP_Class": {
                                "match_evaluation": "match-all",
                                "packets": 3,
                                "bytes": 330,
                                "rate": {
                                    "interval": 300,
                                    "offered_rate_bps": 0,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["access-group name NTP_Permit"],
                                "police": {
                                    "cir_bps": 8000,
                                    "cir_bc_bytes": 1500,
                                    "conformed": {
                                        "packets": 3,
                                        "bytes": 330,
                                        "actions": {"drop": True},
                                        "bps": 0,
                                    },
                                    "exceeded": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {"drop": True},
                                        "bps": 0,
                                    },
                                },
                            },
                            "ALL_Class": {
                                "match_evaluation": "match-all",
                                "packets": 23,
                                "bytes": 1548,
                                "rate": {
                                    "interval": 300,
                                    "offered_rate_bps": 0,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["access-group name ALL_Permit"],
                                "police": {
                                    "cir_bps": 200000,
                                    "cir_bc_bytes": 15000,
                                    "conformed": {
                                        "packets": 23,
                                        "bytes": 1548,
                                        "actions": {"transmit": True},
                                        "bps": 0,
                                    },
                                    "exceeded": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {"drop": True},
                                        "bps": 0,
                                    },
                                },
                            },
                            "class-default": {
                                "match_evaluation": "match-any",
                                "packets": 276,
                                "bytes": 16554,
                                "rate": {
                                    "interval": 300,
                                    "offered_rate_bps": 0,
                                    "drop_rate_bps": 0,
                                },
                                "match": ["any"],
                            },
                        }
                    }
                }
            }
        }
    }
}
