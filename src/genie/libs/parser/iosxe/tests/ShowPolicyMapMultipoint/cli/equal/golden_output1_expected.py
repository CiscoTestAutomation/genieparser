expected_output = {
    "interfaces": {
        "Tunnel1": {
            "21.50.50.122": {
                "service_policy": {
                    "output": {
                        "policy_name": {
                            "spoke1_group": {
                                "class_map": {
                                    "abc": {
                                        "match_evaluation": "match-any",
                                        "match": [
                                            "protocol ipv6-icmp"
                                        ],
                                        "packets": 215,
                                        "bytes": 27520,
                                        "rate": {
                                            "interval": 5,
                                            "offered_rate_bps": 0,
                                            "drop_rate_bps": 0
                                        },
                                        "qos_set": {
                                            "dscp": {
                                                "af43": {
                                                    "marker_statistics": "Disabled"
                                                }
                                            }
                                        }
                                    },
                                    "class-default": {
                                        "match_evaluation": "match-any",
                                        "match": [
                                            "any"
                                        ],
                                        "packets": 138,
                                        "bytes": 16129,
                                        "rate": {
                                            "interval": 5,
                                            "offered_rate_bps": 0,
                                            "drop_rate_bps": 0
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            },
            "22.51.51.123": {
                "service_policy": {
                    "output": {
                        "policy_name": {
                            "spoke2_group": {
                                "class_map": {
                                    "abc": {
                                        "match_evaluation": "match-any",
                                        "match": [
                                            "protocol ipv6-icmp"
                                        ],
                                        "packets": 215,
                                        "bytes": 27520,
                                        "rate": {
                                            "interval": 5,
                                            "offered_rate_bps": 0,
                                            "drop_rate_bps": 0
                                        },
                                        "qos_set": {
                                            "dscp": {
                                                "af11": {
                                                    "marker_statistics": "Disabled"
                                                }
                                            }
                                        }
                                    },
                                    "class-default": {
                                        "match_evaluation": "match-any",
                                        "match": [
                                            "any"
                                        ],
                                        "packets": 131,
                                        "bytes": 15309,
                                        "rate": {
                                            "interval": 5,
                                            "offered_rate_bps": 0,
                                            "drop_rate_bps": 0
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