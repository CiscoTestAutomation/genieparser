expected_output = {
    "interfaces": {
        "GigabitEthernet1": {
            "line_protocol": "up",
            "status": "up",
            "clns_protocol_processing": False,
        },
        "GigabitEthernet2": {
            "line_protocol": "up",
            "status": "up",
            "checksum_enabled": True,
            "mtu": 1497,
            "encapsulation": "SAP",
            "erpdus_enabled": True,
            "min_interval_msec": 10,
            "clns_fast_switching": True,
            "clns_sse_switching": False,
            "dec_compatibility_mode": "OFF",
            "next_esh_ish_in": 55,
            "routing_protocol": {
                "IS-IS": {
                    "process_id": {
                        "test": {
                            "level_type": "level-1-2",
                            "interface_number": "0x1",
                            "local_circuit_id": "0x1",
                            "neighbor_extended_local_circuit_id": "0x0",
                            "level-1": {
                                "metric": 10,
                                "circuit_id": "R2.01",
                                "dr_id": "R2.01",
                                "ipv6_metric": 10,
                            },
                            "priority": {
                                "level-1": {"priority": 64},
                                "level-2": {"priority": 64},
                            },
                            "adjacencies": {
                                "level-1": {"number_of_active_adjancies": 1},
                                "level-2": {"number_of_active_adjancies": 0},
                            },
                            "level-2": {
                                "metric": 10,
                                "circuit_id": "R2.01",
                                "dr_id": "0000.0000.0000.00",
                                "ipv6_metric": 10,
                            },
                            "hello_interval": {
                                "level-1": {"next_is_is_lan_hello_in_ms": 432},
                                "level-2": {"next_is_is_lan_hello_in": 4},
                            },
                        }
                    }
                }
            },
        },
        "GigabitEthernet3": {
            "line_protocol": "up",
            "status": "up",
            "checksum_enabled": True,
            "mtu": 1497,
            "encapsulation": "SAP",
            "erpdus_enabled": True,
            "min_interval_msec": 10,
            "clns_fast_switching": True,
            "clns_sse_switching": False,
            "dec_compatibility_mode": "OFF",
            "next_esh_ish_in": 15,
            "routing_protocol": {
                "IS-IS": {
                    "process_id": {
                        "test": {
                            "level_type": "level-1-2",
                            "interface_number": "0x2",
                            "local_circuit_id": "0x2",
                            "neighbor_extended_local_circuit_id": "0x0",
                            "level-1": {
                                "metric": 10,
                                "circuit_id": "R2.02",
                                "dr_id": "0000.0000.0000.00",
                                "ipv6_metric": 10,
                            },
                            "priority": {
                                "level-1": {"priority": 64},
                                "level-2": {"priority": 64},
                            },
                            "adjacencies": {
                                "level-1": {"number_of_active_adjancies": 0},
                                "level-2": {"number_of_active_adjancies": 0},
                            },
                            "level-2": {
                                "metric": 10,
                                "circuit_id": "R2.02",
                                "dr_id": "0000.0000.0000.00",
                                "ipv6_metric": 10,
                            },
                            "hello_interval": {
                                "level-1": {"next_is_is_lan_hello_in": 5},
                                "level-2": {"next_is_is_lan_hello_in": 6},
                            },
                        }
                    }
                }
            },
        },
        "GigabitEthernet4": {
            "line_protocol": "up",
            "status": "up",
            "checksum_enabled": True,
            "mtu": 1497,
            "encapsulation": "SAP",
            "erpdus_enabled": True,
            "min_interval_msec": 10,
            "clns_fast_switching": True,
            "clns_sse_switching": False,
            "dec_compatibility_mode": "OFF",
            "next_esh_ish_in": 32,
            "routing_protocol": {
                "IS-IS": {
                    "process_id": {
                        "VRF1": {
                            "level_type": "level-1-2",
                            "interface_number": "0x1",
                            "local_circuit_id": "0x1",
                            "neighbor_extended_local_circuit_id": "0x0",
                            "level-1": {
                                "metric": 10,
                                "circuit_id": "R2.01",
                                "dr_id": "0000.0000.0000.00",
                                "ipv6_metric": 10,
                            },
                            "priority": {
                                "level-1": {"priority": 64},
                                "level-2": {"priority": 64},
                            },
                            "adjacencies": {
                                "level-1": {"number_of_active_adjancies": 0},
                                "level-2": {"number_of_active_adjancies": 0},
                            },
                            "level-2": {
                                "metric": 10,
                                "circuit_id": "R2.01",
                                "dr_id": "0000.0000.0000.00",
                                "ipv6_metric": 10,
                            },
                            "hello_interval": {
                                "level-1": {"next_is_is_lan_hello_in": 2},
                                "level-2": {"next_is_is_lan_hello_in": 7},
                            },
                        }
                    }
                }
            },
        },
        "Loopback0": {
            "line_protocol": "up",
            "status": "up",
            "checksum_enabled": True,
            "mtu": 1514,
            "encapsulation": "LOOPBACK",
            "erpdus_enabled": True,
            "min_interval_msec": 10,
            "clns_fast_switching": False,
            "clns_sse_switching": False,
            "dec_compatibility_mode": "OFF",
            "next_esh_ish_in": 36,
            "routing_protocol": {
                "IS-IS": {
                    "process_id": {
                        "test": {
                            "level_type": "level-1-2",
                            "interface_number": "0x0",
                            "local_circuit_id": "0x7",
                            "neighbor_extended_local_circuit_id": "0x0",
                            "level-1": {
                                "metric": 10,
                                "circuit_id": "R2.07",
                                "ipv6_metric": 10,
                            },
                            "priority": {
                                "level-1": {"priority": 64},
                                "level-2": {"priority": 64},
                            },
                            "adjacencies": {
                                "level-1": {"number_of_active_adjancies": 0},
                                "level-2": {"number_of_active_adjancies": 0},
                            },
                            "level-2": {
                                "metric": 10,
                                "circuit_id": "R2.07",
                                "ipv6_metric": 10,
                            },
                            "hello_interval": {"next_is_is_hello_in": 0},
                            "if_state": "Down",
                        }
                    }
                }
            },
        },
        "Loopback1": {
            "line_protocol": "up",
            "status": "up",
            "checksum_enabled": True,
            "mtu": 1514,
            "encapsulation": "LOOPBACK",
            "erpdus_enabled": True,
            "min_interval_msec": 10,
            "clns_fast_switching": False,
            "clns_sse_switching": False,
            "dec_compatibility_mode": "OFF",
            "next_esh_ish_in": 49,
            "routing_protocol": {
                "IS-IS": {
                    "process_id": {
                        "VRF1": {
                            "level_type": "level-1-2",
                            "interface_number": "0x0",
                            "local_circuit_id": "0x8",
                            "neighbor_extended_local_circuit_id": "0x0",
                            "level-1": {
                                "metric": 10,
                                "circuit_id": "R2.08",
                                "ipv6_metric": 10,
                            },
                            "priority": {
                                "level-1": {"priority": 64},
                                "level-2": {"priority": 64},
                            },
                            "adjacencies": {
                                "level-1": {"number_of_active_adjancies": 0},
                                "level-2": {"number_of_active_adjancies": 0},
                            },
                            "level-2": {
                                "metric": 10,
                                "circuit_id": "R2.08",
                                "ipv6_metric": 10,
                            },
                            "hello_interval": {"next_is_is_hello_in": 0},
                            "if_state": "Down",
                        }
                    }
                }
            },
        },
    }
}
