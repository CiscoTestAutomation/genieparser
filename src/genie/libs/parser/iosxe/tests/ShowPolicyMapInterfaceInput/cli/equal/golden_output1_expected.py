expected_output = {
    "FiveGigabitEthernet1/0/36": {
        "service_policy": {
            "input": {
                "policy_name": {
                    "AutoQos-4.0-CiscoPhone-Input-Policy": {
                        "class_map": {
                            "AutoQos-4.0-Default-Class": {
                                "match": [
                                    "access-group name AutoQos-4.0-Acl-Default"
                                ],
                                "match_evaluation": "match-any",
                                "packets": 3035984544,
                                "qos_set": {
                                    "dscp": {
                                        "default": {}
                                    }
                                }
                            },
                            "AutoQos-4.0-Voip-Data-CiscoPhone-Class": {
                                "match": [
                                    "cos  5"
                                ],
                                "match_evaluation": "match-any",
                                "packets": 0,
                                "police": {
                                    "cir_bc_bytes": 8000,
                                    "cir_bps": 128000,
                                    "conformed": {
                                        "actions": {
                                            "transmit": True
                                        },
                                        "bps": 0,
                                        "bytes": 0
                                    },
                                    "exceeded": {
                                        "actions": {
                                            "set_dscp_transmit": "dscp table policed-dscp"
                                        },
                                        "bps": 0,
                                        "bytes": 0
                                    }
                                },
                                "qos_set": {
                                    "dscp": {
                                        "ef": {}
                                    }
                                }
                            },
                            "AutoQos-4.0-Voip-Signal-CiscoPhone-Class": {
                                "match": [
                                    "cos  3"
                                ],
                                "match_evaluation": "match-any",
                                "packets": 0,
                                "police": {
                                    "cir_bc_bytes": 8000,
                                    "cir_bps": 32000,
                                    "conformed": {
                                        "actions": {
                                            "transmit": True
                                        },
                                        "bps": 0,
                                        "bytes": 0
                                    },
                                    "exceeded": {
                                        "actions": {
                                            "set_dscp_transmit": "dscp table policed-dscp"
                                        },
                                        "bps": 0,
                                        "bytes": 0
                                    }
                                },
                                "qos_set": {
                                    "dscp": {
                                        "cs3": {}
                                    }
                                }
                            },
                            "class-default": {
                                "match": [
                                    "any"
                                ],
                                "match_evaluation": "match-any",
                                "packets": 4312
                            }
                        }
                    }
                }
            }
        }
    }
}