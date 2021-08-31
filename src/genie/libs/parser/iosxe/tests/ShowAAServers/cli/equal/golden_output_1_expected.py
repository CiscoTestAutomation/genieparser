expected_output = {
   "radius_server": {
        "11.15.24.213": {
            "aaatype": {
                "authen": {
                    "bad_authenticators": "0",
                    "failover": 0,
                    "malformed_responses": "0",
                    "request": 49,
                    "response": {
                        "accept": 8,
                        "challenge": 16,
                        "incorrect": 0,
                        "reject": 0,
                        "server_error": 0,
                        "time": "94ms",
                        "unexpected": 2,
                    },
                    "retransmission": 19,
                    "throttled": {"failure": 0, "timeout": 0, "transaction": 0},
                    "timeout": 25,
                    "transaction": {"failure": 6, "success": 24},
                    "transaction_type": {
                        "dot1xtransactions": {
                            "response": {
                                "avg_response_time": "94ms",
                                "total_responses": "24",
                            },
                            "transaction": {
                                "failover": 0,
                                "failure": 4,
                                "success": 8,
                                "timeouts": 4,
                                "total": 12,
                            },
                        },
                        "mac_authtransactions": {
                            "response": {
                                "avg_response_time": "0ms",
                                "total_responses": "0",
                            },
                            "transaction": {
                                "failover": 0,
                                "failure": 0,
                                "success": 0,
                                "timeouts": 0,
                                "total": 0,
                            },
                        },
                    },
                },
                "author": {
                    "bad_authenticators": "0",
                    "failover": 0,
                    "malformed_responses": "0",
                    "request": 0,
                    "response": {
                        "accept": 0,
                        "challenge": 0,
                        "incorrect": 0,
                        "reject": 0,
                        "server_error": 0,
                        "time": "0ms",
                        "unexpected": 0,
                    },
                    "retransmission": 0,
                    "throttled": {"failure": 0, "timeout": 0, "transaction": 0},
                    "timeout": 0,
                    "transaction": {"failure": 0, "success": 0},
                    "transaction_type": {
                        "mac_authortransactions": {
                            "response": {
                                "avg_response_time": "0ms",
                                "total_responses": "0",
                            },
                            "transaction": {
                                "failover": 0,
                                "failure": 0,
                                "success": 0,
                                "timeouts": 0,
                                "total": 0,
                            },
                        }
                    },
                },
            },
            "account": {
                "bad_authenticators": "0",
                "failover": 0,
                "malformed_responses": "0",
                "request": 21,
                "requests": {"interim": 0, "start": 8, "stop": 7},
                "response": {
                    "incorrect": 0,
                    "server_error": 0,
                    "time": "3ms",
                    "unexpected": 0,
                },
                "responses": {"interim": 0, "start": 8, "stop": 5},
                "retransmission": 6,
                "throttled": {"failure": 0, "timeout": 0, "transaction": 0},
                "timeout": 8,
                "transaction": {"failure": 2, "success": 13},
            },
            "acct_port": 1813,
            "auth_port": 1812,
            "consecutive_response_failures": {
                "platform_type": {
                    "iosd_platform": {"current": 0, "max": 0, "total": 0},
                    "smd_platform": {"current": 0, "max": 3, "total": 5},
                    "wncd_platform": {"current": 0, "max": 0, "total": 0},
                },
                "total": 5,
            },
            "consecutive_timeouts": {
                "platform_type": {
                    "iosd_platform": {"current": 3, "max": 3, "total": 3},
                    "smd_platform": {"current": 0, "max": 15, "total": 26},
                    "wncd_platform": {"current": 0, "max": 0, "total": 0},
                },
                "total": 29,
            },
            "dead_type": {
                "dead": {"count": "0", "total_time": "0s"},
                "platform_dead": {"count": "0UP", "total_time": "0s"},
                "smd_platform_dead": {"count": "2", "total_time": "0s"},
            },
            "elapsed_time": "2h9m",
            "estimated_outstanding_access_transactions": 0,
            "estimated_outstanding_accounting_transactions": 0,
            "estimated_throttled_access_transactions": 0,
            "estimated_throttled_accounting_transactions": 0,
            "host": "11.15.24.213",
            "hostname": "mgmt-rad",
            "id": 1,
            "maximum_throttled_transactions": {"access": 0, "accounting": 0},
            "platform_state_type": {
                "platform_state_smd": {
                    "current": "UP",
                    "duration": "5646s",
                    "previous_duration": "0s",
                },
                "platform_state_wncd_8": {
                    "current": "UP",
                    "duration": "0s",
                    "previous_duration": "0s",
                },
                "state": {
                    "current": "UP",
                    "duration": "7787s",
                    "previous_duration": "0s",
                },
                "state_wncd_1": {"current": "UP"},
                "state_wncd_2": {"current": "UP"},
                "state_wncd_3": {"current": "UP"},
                "state_wncd_4": {"current": "UP"},
                "state_wncd_5": {"current": "UP"},
                "state_wncd_6": {"current": "UP"},
                "state_wncd_7": {"current": "UP"},
            },
            "priority": 1,
            "quarantined": "No",
            "requests_per_minute_past_24_hours": {
                "average": 0,
                "level_type": {
                    "high": {"ago": 4, "hours": 1, "minutes": 37},
                    "low ": {"ago": 0, "hours": 2, "minutes": 9},
                },
            },
        }
    }
}
