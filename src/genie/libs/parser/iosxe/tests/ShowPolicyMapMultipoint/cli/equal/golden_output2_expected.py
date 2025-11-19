expected_output = {
    "interfaces": {
        "Tunnel1": {
            "2001:DB8:1201::122": {
                "service_policy": {
                    "output": {
                        "policy_name": {
                            "spoke1_group": {
                                "class_map": {
                                    "abc": {
                                        "match_evaluation": "match-any",
                                        "match": [
                                            "protocol icmp"
                                        ],
                                        "packets": 215,
                                        "bytes": 31820,
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
                                        "packets": 118,
                                        "bytes": 12949,
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
            "2001:DB8:1202::123": {
                "service_policy": {
                    "output": {
                        "policy_name": {
                            "spoke2_group": {
                                "class_map": {
                                    "abc": {
                                        "match_evaluation": "match-any",
                                        "match": [
                                            "protocol icmp"
                                        ],
                                        "packets": 215,
                                        "bytes": 31820,
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
                                        "packets": 111,
                                        "bytes": 12211,
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