expected_output = {
    "isis": {
        "test_0": {
            "neighbors": {
                "R1_xe": {
                    "type": {
                        "L2": {
                            "interfaces": {
                                "GigabitEthernet1": {
                                    "ip_address": "172.16.10.1",
                                    "state": "UP",
                                    "holdtime": "21",
                                    "circuit_id": "C_ID.00"
                                },
                                "GigabitEthernet2": {
                                    "ip_address": "172.16.20.1",
                                    "state": "DOWN",
                                    "holdtime": "25",
                                    "circuit_id": "C_ID.01"
                                },
                                "GigabitEthernet3": {
                                    "ip_address": "172.16.30.1",
                                    "state": "INIT",
                                    "holdtime": "21",
                                    "circuit_id": "C_ID.02"
                                }
                            }
                        }
                    }
                },
                "R2_xr": {
                    "type": {
                        "L1": {
                            "interfaces": {
                                "GigabitEthernet4": {
                                    "ip_address": "172.16.40.1",
                                    "state": "NONE",
                                    "holdtime": "25",
                                    "circuit_id": "C_ID.03"
                                }
                            }
                        }
                    }
                }
            }
        },
        "test_1": {
            "neighbors": {
                "R3_xe": {
                    "type": {
                        "L1": {
                            "interfaces": {
                                "GigabitEthernet6": {
                                    "ip_address": "172.16.50.1",
                                    "state": "NONE",
                                    "holdtime": "21",
                                    "circuit_id": "C_ID.05"
                                },
                                "GigabitEthernet5": {
                                    "ip_address": "172.16.60.1",
                                    "state": "UP",
                                    "holdtime": "25",
                                    "circuit_id": "C_ID.07"
                                }
                            }
                        }
                    }
                },
                "R4_xr": {
                    "type": {
                        "L2": {
                            "interfaces": {
                                "GigabitEthernet8": {
                                    "ip_address": "172.16.70.1",
                                    "state": "INIT",
                                    "holdtime": "21",
                                    "circuit_id": "C_ID.06"
                                },
                                "GigabitEthernet7": {
                                    "ip_address": "172.16.80.1",
                                    "state": "DOWN",
                                    "holdtime": "25",
                                    "circuit_id": "C_ID.04"
                                }
                            }
                        }
                    }
                }
            }
        },
        "test_2": {
            "neighbors": {
                "R7_xe": {
                    "type": {
                        "L1": {
                            "interfaces": {
                                "GigabitEthernet10.104": {
                                    "ip_address": "172.17.10.1",
                                    "state": "NONE",
                                    "holdtime": "21",
                                    "circuit_id": "C_ID.10"
                                }
                            }
                        }
                    }
                },
                "R8_xe": {
                    "type": {
                        "L1": {
                            "interfaces": {
                                "GigabitEthernet10.103": {
                                    "ip_address": "172.17.20.1",
                                    "state": "UP",
                                    "holdtime": "25",
                                    "circuit_id": "C_ID.08"
                                }
                            }
                        }
                    }
                },
                "R9_xr": {
                    "type": {
                        "L2": {
                            "interfaces": {
                                "GigabitEthernet13.102": {
                                    "ip_address": "172.17.30.1",
                                    "state": "INIT",
                                    "holdtime": "21",
                                    "circuit_id": "C_ID.11"
                                },
                                "GigabitEthernet13.101": {
                                    "ip_address": "172.17.40.1",
                                    "state": "DOWN",
                                    "holdtime": "25",
                                    "circuit_id": "C_ID.13"
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}