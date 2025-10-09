expected_output = {
    "radius_server": {
        "radius1.com": {
            "acct_port": 1813,
            "auth_port": 1812,
            "host": "radius1.com",
            "hostname": "rad-test-1",
            "priority": 1,
            "id": 1,
            "platform_state_type": {
                "state": {
                    "current": "DEAD",
                    "duration": "0s",
                    "previous_duration": "0s"
                },
                "platform_state_smd": {
                    "current": "DEAD",
                    "duration": "0s",
                    "previous_duration": "0s"
                },
                "platform_state_wncd_0": {
                    "current": "DEAD",
                    "duration": "433s",
                    "previous_duration": "0s"
                },
                "platform_state_wncd_1": {
                    "current": "DEAD",
                    "duration": "433s",
                    "previous_duration": "0s"
                },
                "platform_state_wncd_2": {
                    "current": "DEAD",
                    "duration": "433s",
                    "previous_duration": "0s"
                },
                "platform_state_wncd_3": {
                    "current": "DEAD",
                    "duration": "433s",
                    "previous_duration": "0s"
                },
                "platform_state_wncd_4": {
                    "current": "DEAD",
                    "duration": "433s",
                    "previous_duration": "0s"
                },
                "platform_state_wncd_5": {
                    "current": "DEAD",
                    "duration": "433s",
                    "previous_duration": "0s"
                },
                "platform_state_wncd_6": {
                    "current": "DEAD",
                    "duration": "433s",
                    "previous_duration": "0s"
                },
                "platform_state_wncd_7": {
                    "current": "DEAD",
                    "duration": "433s",
                    "previous_duration": "0s"
                }
            },
            "dead_type": {
                "dead": {
                    "total_time": "0s",
                    "count": "0"
                },
                "smd_platform_dead": {
                    "total_time": "0s",
                    "count": "0"
                },
                "wncd_platform_dead": {
                    "total_time": "0s",
                    "count": "0DEADDEAD"
                }
            },
            "quarantined": "No",
            "aaatype": {
                "authen": {
                    "request": 0,
                    "timeout": 0,
                    "failover": 0,
                    "retransmission": 0,
                    "response": {
                        "accept": 0,
                        "reject": 0,
                        "challenge": 0,
                        "unexpected": 0,
                        "server_error": 0,
                        "incorrect": 0,
                        "time": "0ms"
                    },
                    "transaction": {
                        "success": 0,
                        "failure": 0
                    },
                    "throttled": {
                        "transaction": 0,
                        "timeout": 0,
                        "failure": 0
                    },
                    "malformed_responses": "0",
                    "bad_authenticators": "0",
                    "transaction_type": {
                        "dot1xtransactions": {
                            "response": {
                                "total_responses": "0",
                                "avg_response_time": "0ms"
                            },
                            "transaction": {
                                "timeouts": 0,
                                "failover": 0,
                                "total": 0,
                                "success": 0,
                                "failure": 0
                            }
                        },
                        "mac_authtransactions": {
                            "response": {
                                "total_responses": "0",
                                "avg_response_time": "0ms"
                            },
                            "transaction": {
                                "timeouts": 0,
                                "failover": 0,
                                "total": 0,
                                "success": 0,
                                "failure": 0
                            }
                        }
                    }
                },
                "author": {
                    "request": 0,
                    "timeout": 0,
                    "failover": 0,
                    "retransmission": 0,
                    "response": {
                        "accept": 0,
                        "reject": 0,
                        "challenge": 0,
                        "unexpected": 0,
                        "server_error": 0,
                        "incorrect": 0,
                        "time": "0ms"
                    },
                    "transaction": {
                        "success": 0,
                        "failure": 0
                    },
                    "throttled": {
                        "transaction": 0,
                        "timeout": 0,
                        "failure": 0
                    },
                    "malformed_responses": "0",
                    "bad_authenticators": "0",
                    "transaction_type": {
                        "mac_authortransactions": {
                            "response": {
                                "total_responses": "0",
                                "avg_response_time": "0ms"
                            },
                            "transaction": {
                                "timeouts": 0,
                                "failover": 0,
                                "total": 0,
                                "success": 0,
                                "failure": 0
                            }
                        }
                    }
                }
            },
            "account": {
                "request": 0,
                "timeout": 0,
                "failover": 0,
                "retransmission": 0,
                "requests": {
                    "start": 0,
                    "interim": 0,
                    "stop": 0
                },
                "responses": {
                    "start": 0,
                    "interim": 0,
                    "stop": 0
                },
                "response": {
                    "unexpected": 0,
                    "server_error": 0,
                    "incorrect": 0,
                    "time": "0ms"
                },
                "transaction": {
                    "success": 0,
                    "failure": 0
                },
                "throttled": {
                    "transaction": 0,
                    "timeout": 0,
                    "failure": 0
                },
                "malformed_responses": "0",
                "bad_authenticators": "0"
            },
            "elapsed_time": "0m",
            "estimated_outstanding_access_transactions": 0,
            "estimated_outstanding_accounting_transactions": 0,
            "estimated_throttled_access_transactions": 0,
            "estimated_throttled_accounting_transactions": 0,
            "maximum_throttled_transactions": {
                "access": 0,
                "accounting": 0
            },
            "consecutive_response_failures": {
                "total": 0,
                "platform_type": {
                    "smd_platform": {
                        "max": 0,
                        "current": 0,
                        "total": 0
                    },
                    "wncd_platform": {
                        "max": 0,
                        "current": 0,
                        "total": 0
                    },
                    "iosd_platform": {
                        "max": 0,
                        "current": 0,
                        "total": 0
                    }
                }
            },
            "consecutive_timeouts": {
                "total": 0,
                "platform_type": {
                    "smd_platform": {
                        "max": 0,
                        "current": 0,
                        "total": 0
                    },
                    "wncd_platform": {
                        "max": 0,
                        "current": 0,
                        "total": 0
                    },
                    "iosd_platform": {
                        "max": 0,
                        "current": 0,
                        "total": 0
                    }
                }
            }
        },
        "radius2.com": {
            "acct_port": 1813,
            "auth_port": 1812,
            "host": "radius2.com",
            "hostname": "rad-test-2",
            "priority": 2,
            "id": 2,
            "platform_state_type": {
                "state": {
                    "current": "DEAD",
                    "duration": "0s",
                    "previous_duration": "0s"
                },
                "platform_state_smd": {
                    "current": "DEAD",
                    "duration": "0s",
                    "previous_duration": "0s"
                },
                "platform_state_wncd_0": {
                    "current": "DEAD",
                    "duration": "433s",
                    "previous_duration": "0s"
                },
                "platform_state_wncd_1": {
                    "current": "DEAD",
                    "duration": "433s",
                    "previous_duration": "0s"
                },
                "platform_state_wncd_2": {
                    "current": "DEAD",
                    "duration": "433s",
                    "previous_duration": "0s"
                },
                "platform_state_wncd_3": {
                    "current": "DEAD",
                    "duration": "433s",
                    "previous_duration": "0s"
                },
                "platform_state_wncd_4": {
                    "current": "DEAD",
                    "duration": "433s",
                    "previous_duration": "0s"
                },
                "platform_state_wncd_5": {
                    "current": "DEAD",
                    "duration": "433s",
                    "previous_duration": "0s"
                },
                "platform_state_wncd_6": {
                    "current": "DEAD",
                    "duration": "433s",
                    "previous_duration": "0s"
                },
                "platform_state_wncd_7": {
                    "current": "DEAD",
                    "duration": "433s",
                    "previous_duration": "0s"
                }
            },
            "dead_type": {
                "dead": {
                    "total_time": "0s",
                    "count": "0"
                },
                "smd_platform_dead": {
                    "total_time": "0s",
                    "count": "0"
                },
                "wncd_platform_dead": {
                    "total_time": "0s",
                    "count": "0DEADDEAD"
                }
            },
            "quarantined": "No",
            "aaatype": {
                "authen": {
                    "request": 0,
                    "timeout": 0,
                    "failover": 0,
                    "retransmission": 0,
                    "response": {
                        "accept": 0,
                        "reject": 0,
                        "challenge": 0,
                        "unexpected": 0,
                        "server_error": 0,
                        "incorrect": 0,
                        "time": "0ms"
                    },
                    "transaction": {
                        "success": 0,
                        "failure": 0
                    },
                    "throttled": {
                        "transaction": 0,
                        "timeout": 0,
                        "failure": 0
                    },
                    "malformed_responses": "0",
                    "bad_authenticators": "0",
                    "transaction_type": {
                        "dot1xtransactions": {
                            "response": {
                                "total_responses": "0",
                                "avg_response_time": "0ms"
                            },
                            "transaction": {
                                "timeouts": 0,
                                "failover": 0,
                                "total": 0,
                                "success": 0,
                                "failure": 0
                            }
                        },
                        "mac_authtransactions": {
                            "response": {
                                "total_responses": "0",
                                "avg_response_time": "0ms"
                            },
                            "transaction": {
                                "timeouts": 0,
                                "failover": 0,
                                "total": 0,
                                "success": 0,
                                "failure": 0
                            }
                        }
                    }
                },
                "author": {
                    "request": 0,
                    "timeout": 0,
                    "failover": 0,
                    "retransmission": 0,
                    "response": {
                        "accept": 0,
                        "reject": 0,
                        "challenge": 0,
                        "unexpected": 0,
                        "server_error": 0,
                        "incorrect": 0,
                        "time": "0ms"
                    },
                    "transaction": {
                        "success": 0,
                        "failure": 0
                    },
                    "throttled": {
                        "transaction": 0,
                        "timeout": 0,
                        "failure": 0
                    },
                    "malformed_responses": "0",
                    "bad_authenticators": "0",
                    "transaction_type": {
                        "mac_authortransactions": {
                            "response": {
                                "total_responses": "0",
                                "avg_response_time": "0ms"
                            },
                            "transaction": {
                                "timeouts": 0,
                                "failover": 0,
                                "total": 0,
                                "success": 0,
                                "failure": 0
                            }
                        }
                    }
                }
            },
            "account": {
                "request": 0,
                "timeout": 0,
                "failover": 0,
                "retransmission": 0,
                "requests": {
                    "start": 0,
                    "interim": 0,
                    "stop": 0
                },
                "responses": {
                    "start": 0,
                    "interim": 0,
                    "stop": 0
                },
                "response": {
                    "unexpected": 0,
                    "server_error": 0,
                    "incorrect": 0,
                    "time": "0ms"
                },
                "transaction": {
                    "success": 0,
                    "failure": 0
                },
                "throttled": {
                    "transaction": 0,
                    "timeout": 0,
                    "failure": 0
                },
                "malformed_responses": "0",
                "bad_authenticators": "0"
            },
            "elapsed_time": "0m",
            "estimated_outstanding_access_transactions": 0,
            "estimated_outstanding_accounting_transactions": 0,
            "estimated_throttled_access_transactions": 0,
            "estimated_throttled_accounting_transactions": 0,
            "maximum_throttled_transactions": {
                "access": 0,
                "accounting": 0
            },
            "consecutive_response_failures": {
                "total": 0,
                "platform_type": {
                    "smd_platform": {
                        "max": 0,
                        "current": 0,
                        "total": 0
                    },
                    "wncd_platform": {
                        "max": 0,
                        "current": 0,
                        "total": 0
                    },
                    "iosd_platform": {
                        "max": 0,
                        "current": 0,
                        "total": 0
                    }
                }
            },
            "consecutive_timeouts": {
                "total": 0,
                "platform_type": {
                    "smd_platform": {
                        "max": 0,
                        "current": 0,
                        "total": 0
                    },
                    "wncd_platform": {
                        "max": 0,
                        "current": 0,
                        "total": 0
                    },
                    "iosd_platform": {
                        "max": 0,
                        "current": 0,
                        "total": 0
                    }
                }
            }
        }
    }
}