expected_output = {
    "isis": {
        "test": {
            "neighbors": {
                "R2_xr": {
                    "type": {
                        "L1": {
                            "interfaces": {
                                "GigabitEthernet2.115": {
                                    "ip_address": "10.12.115.2",
                                    "state": "UP",
                                    "holdtime": "7",
                                    "circuit_id": "R2_xr.01",
                                }
                            }
                        },
                        "L2": {
                            "interfaces": {
                                "GigabitEthernet2.115": {
                                    "ip_address": "10.12.115.2",
                                    "state": "UP",
                                    "holdtime": "7",
                                    "circuit_id": "R2_xr.01",
                                }
                            }
                        },
                    }
                },
                "R3_nx": {
                    "type": {
                        "L1": {
                            "interfaces": {
                                "GigabitEthernet3.115": {
                                    "ip_address": "10.13.115.3",
                                    "state": "UP",
                                    "holdtime": "28",
                                    "circuit_id": "R1_xe.02",
                                }
                            }
                        },
                        "L2": {
                            "interfaces": {
                                "GigabitEthernet3.115": {
                                    "ip_address": "10.13.115.3",
                                    "state": "UP",
                                    "holdtime": "23",
                                    "circuit_id": "R1_xe.02",
                                }
                            }
                        },
                    }
                },
            }
        },
        "test1": {
            "neighbors": {
                "2222.22ff.4444": {
                    "type": {
                        "L1": {
                            "interfaces": {
                                "GigabitEthernet2.415": {
                                    "ip_address": "10.12.115.2",
                                    "state": "INIT",
                                    "holdtime": "21",
                                    "circuit_id": "2222.22ff.4444.01",
                                }
                            }
                        },
                        "L2": {
                            "interfaces": {
                                "GigabitEthernet2.415": {
                                    "ip_address": "10.12.115.2",
                                    "state": "INIT",
                                    "holdtime": "20",
                                    "circuit_id": "2222.22ff.4444.01",
                                }
                            }
                        },
                    }
                },
                "R3_nx": {
                    "type": {
                        "L1": {
                            "interfaces": {
                                "GigabitEthernet3.415": {
                                    "ip_address": "10.13.115.3",
                                    "state": "UP",
                                    "holdtime": "21",
                                    "circuit_id": "R1_xe.02",
                                }
                            }
                        },
                        "L2": {
                            "interfaces": {
                                "GigabitEthernet3.415": {
                                    "ip_address": "10.13.115.3",
                                    "state": "UP",
                                    "holdtime": "27",
                                    "circuit_id": "R1_xe.02",
                                }
                            }
                        },
                    }
                },
            }
        },
    }
}
