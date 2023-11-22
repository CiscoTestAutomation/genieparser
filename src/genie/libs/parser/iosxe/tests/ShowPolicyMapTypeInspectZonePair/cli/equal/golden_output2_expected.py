expected_output= {
    "zone_pair": {
        "DEFAULT->RED": {
            "service_policy_inspect": {
                "TEST": {
                    "class_map": {
                        "TEST": {
                            "class_map_type": "match-any",
                            "class_map_match": [
                                "access-group name HBN2"
                            ],
                            "class_map_action": {
                                "Inspect": {
                                    "sessions_since_startup_or_reset": 0,
                                    "current_session_counts_estab": 0,
                                    "current_session_counts_half_open": 0,
                                    "current_session_counts_terminating": 0,
                                    "maxever_session_counts_estab": 0,
                                    "maxever_session_counts_half_open": 0,
                                    "maxever_session_counts_terminating": 0,
                                    "last_session_created": "never",
                                    "last_statistic_reset": "never",
                                    "last_session_creation_rate": 0,
                                    "last_half_open_session_total": 0
                                }
                            }
                        },
                        "ICMP": {
                            "class_map_type": "match-all",
                            "class_map_match": [
                                "protocol icmp"
                            ],
                            "class_map_action": {
                                "Pass": {
                                    "total_packets": 0,
                                    "total_bytes": 0
                                }
                            }
                        },
                        "class-default": {
                            "class_map_type": "match-any",
                            "class_map_match": [
                                "any "
                            ],
                            "class_map_action": {
                                "Drop": {
                                    "total_packets": 0,
                                    "total_bytes": 0
                                }
                            }
                        }
                    }
                }
            }
        },
        "DEFAULT2GREEN": {
            "service_policy_inspect": {
                "TEST": {
                    "class_map": {
                        "TEST": {
                            "class_map_type": "match-any",
                            "class_map_match": [
                                "access-group name HBN2"
                            ],
                            "class_map_action": {
                                "Inspect": {
                                    "sessions_since_startup_or_reset": 0,
                                    "current_session_counts_estab": 0,
                                    "current_session_counts_half_open": 0,
                                    "current_session_counts_terminating": 0,
                                    "maxever_session_counts_estab": 0,
                                    "maxever_session_counts_half_open": 0,
                                    "maxever_session_counts_terminating": 0,
                                    "last_session_created": "never",
                                    "last_statistic_reset": "never",
                                    "last_session_creation_rate": 0,
                                    "last_half_open_session_total": 0
                                }
                            }
                        },
                        "ICMP": {
                            "class_map_type": "match-all",
                            "class_map_match": [
                                "protocol icmp"
                            ],
                            "class_map_action": {
                                "Pass": {
                                    "total_packets": 0,
                                    "total_bytes": 0
                                }
                            }
                        },
                        "class-default": {
                            "class_map_type": "match-any",
                            "class_map_match": [
                                "any "
                            ],
                            "class_map_action": {
                                "Drop": {
                                    "total_packets": 0,
                                    "total_bytes": 0
                                }
                            }
                        }
                    }
                }
            }
        },
        "GREEN->DEFAULT": {
            "service_policy_inspect": {
                "TEST": {
                    "class_map": {
                        "TEST": {
                            "class_map_type": "match-any",
                            "class_map_match": [
                                "access-group name HBN2"
                            ],
                            "class_map_action": {
                                "Inspect": {
                                    "sessions_since_startup_or_reset": 0,
                                    "current_session_counts_estab": 0,
                                    "current_session_counts_half_open": 0,
                                    "current_session_counts_terminating": 0,
                                    "maxever_session_counts_estab": 0,
                                    "maxever_session_counts_half_open": 0,
                                    "maxever_session_counts_terminating": 0,
                                    "last_session_created": "never",
                                    "last_statistic_reset": "never",
                                    "last_session_creation_rate": 0,
                                    "last_half_open_session_total": 0
                                }
                            }
                        },
                        "ICMP": {
                            "class_map_type": "match-all",
                            "class_map_match": [
                                "protocol icmp"
                            ],
                            "class_map_action": {
                                "Pass": {
                                    "total_packets": 0,
                                    "total_bytes": 0
                                }
                            }
                        },
                        "class-default": {
                            "class_map_type": "match-any",
                            "class_map_match": [
                                "any "
                            ],
                            "class_map_action": {
                                "Drop": {
                                    "total_packets": 0,
                                    "total_bytes": 0
                                }
                            }
                        }
                    }
                }
            }
        },
        "GREEN->RED": {
            "service_policy_inspect": {
                "TEST": {
                    "class_map": {
                        "TEST": {
                            "class_map_type": "match-any",
                            "class_map_match": [
                                "access-group name HBN2"
                            ],
                            "class_map_action": {
                                "Inspect": {
                                    "sessions_since_startup_or_reset": 0,
                                    "current_session_counts_estab": 0,
                                    "current_session_counts_half_open": 0,
                                    "current_session_counts_terminating": 0,
                                    "maxever_session_counts_estab": 0,
                                    "maxever_session_counts_half_open": 0,
                                    "maxever_session_counts_terminating": 0,
                                    "last_session_created": "never",
                                    "last_statistic_reset": "never",
                                    "last_session_creation_rate": 0,
                                    "last_half_open_session_total": 0
                                }
                            }
                        },
                        "ICMP": {
                            "class_map_type": "match-all",
                            "class_map_match": [
                                "protocol icmp"
                            ],
                            "class_map_action": {
                                "Pass": {
                                    "total_packets": 0,
                                    "total_bytes": 0
                                }
                            }
                        },
                        "class-default": {
                            "class_map_type": "match-any",
                            "class_map_match": [
                                "any "
                            ],
                            "class_map_action": {
                                "Drop": {
                                    "total_packets": 0,
                                    "total_bytes": 0
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}