expected_output = {
    "isis": {
        "1": {
            "neighbors": {
                "spine2-ott-lisp-c9k-127": {
                    "type": {
                        "L1L2": {
                            "interfaces": {
                                "GigabitEthernet1/0/2": {
                                    "ip_address": "10.10.12.2",
                                    "state": "UP",
                                    "holdtime": "24",
                                    "circuit_id": "0A"
                                }
                            }
                        }
                    }
                },
                "spine1-c9k-100": {
                    "type": {
                        "L1": {
                            "interfaces": {
                                "GigabitEthernet1/0/1": {
                                    "ip_address": "10.10.11.2",
                                    "state": "UP",
                                    "holdtime": "26",
                                    "circuit_id": "0A"
                                }
                            }
                        }
                    }
                }
            }
        },
        "2": {
            "neighbors": {
                "ott-lisp-c9k-127": {
                    "type": {
                        "L1L2": {
                            "interfaces": {
                                "TwentyFiveGigE1/0/2": {
                                    "ip_address": "20.20.22.2",
                                    "state": "UP",
                                    "holdtime": "24",
                                    "circuit_id": "0B"
                                }
                            }
                        }
                    }
                },
                "ott-lisp-c9k-100": {
                    "type": {
                        "L2": {
                            "interfaces": {
                                "TwentyFiveGigE1/0/1": {
                                    "ip_address": "20.20.21.2",
                                    "state": "UP",
                                    "holdtime": "22",
                                    "circuit_id": "0B"
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
