

expected_output = {
        "vrf": {
            "VRF1": {
                "peer": {
                    "10.94.44.44": {
                        "sa_limit": "44",
                        "description": "R4",
                        "elapsed_time": "01:03:22",
                        "connect_source_address": "10.21.33.34",
                        "authentication": {
                            "password": {
                                "set": False
                            },
                        },
                        "connect_source": "loopback3",
                        "peer_as": "200",
                        "mesh_group": "2",
                        "session_state": "inactive",
                        "statistics": {
                            "established_transitions": 0,
                            "last_message_received": "never",
                            "discontinuity_time": "00:00:20",
                            "port": {
                                "remote": 0,
                                "local": 0
                            },
                            "received": {
                                "notification": 0,
                                "data_message": 0,
                                "sa_response": 0,
                                "sa_request": 0,
                                "keepalive": 0,
                                "total": 0,
                                "ctrl_message": 0
                            },
                            "cache_lifetime": "00:03:30",
                            "sent": {
                                "notification": 0,
                                "data_message": 0,
                                "sa_response": 0,
                                "sa_request": 0,
                                "keepalive": 0,
                                "total": 0,
                                "ctrl_message": 0
                            },
                            "connection_attempts": 88,
                            "error": {
                                "rpf_failure": "0"
                            }
                        },
                        "enable": False,
                        "timer": {
                            "keepalive_interval": 60,
                            "connect_retry_interval": 44,
                            "holdtime_interval": 90
                        }
                    }
                }
            },
            "default": {
                "peer": {
                    "10.4.1.1": {
                        "sa_limit": "111",
                        "description": "R1",
                        "elapsed_time": "01:27:25",
                        "connect_source_address": "10.36.3.3",
                        "reset_reason": 'Keepalive timer expired',
                        "authentication": {
                            "password": {
                                "set": False
                            },
                        },
                        "connect_source": "loopback0",
                        "peer_as": "100",
                        "mesh_group": "1",
                        "session_state": "established",
                        "statistics": {
                            "established_transitions": 6,
                            "last_message_received": "00:00:22",
                            "discontinuity_time": "01:27:25",
                            "port": {
                                "remote": 26743,
                                "local": 639
                            },
                            "received": {
                                "notification": 0,
                                "data_message": 0,
                                "sa_response": 0,
                                "sa_request": 0,
                                "keepalive": 92,
                                "total": 0,
                                "ctrl_message": 0
                            },
                            "cache_lifetime": "00:03:30",
                            "sent": {
                                "notification": 6,
                                "data_message": 0,
                                "sa_response": 0,
                                "sa_request": 0,
                                "keepalive": 119,
                                "total": 0,
                                "ctrl_message": 0
                            },
                            "connection_attempts": 0,
                            "error": {
                                "rpf_failure": "0"
                            }
                        },
                        "enable": True,
                        "timer": {
                            "keepalive_interval": 60,
                            "connect_retry_interval": 33,
                            "holdtime_interval": 90
                        }
                    }
                }
            }
        }
    }
