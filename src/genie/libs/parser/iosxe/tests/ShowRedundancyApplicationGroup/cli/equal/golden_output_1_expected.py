expected_output = {
    "group_id": {
        "1": {
            "fault_states_group": {
                "1": {
                    "runtime_priority": 200,
                    "rg_faults_rg_state": "Up",
                    "total_switchovers_due_to_faults": 0,
                    "total_down_or_up_state_changes_due_to_faults": 0,
                }
            },
            "group_name": "group1",
            "administrative_state": "No Shutdown",
            "aggregate_operational_state": "Up",
            "my_role": "STANDBY",
            "peer_role": "ACTIVE",
            "peer_presence": "Yes",
            "peer_comm": "Yes",
            "peer_progression_started": "Yes",
            "rf_domain": {
                "btob-one": {"rf_state": "STANDBY HOT", "peer_rf_state": "ACTIVE"}
            },
            "rg_protocol": {
                1: {
                    "role": "Standby",
                    "negotiation": "Enabled",
                    "priority": 200,
                    "protocol_state": "Standby-hot",
                    "ctrl_interfaces_state": "Up",
                    "active_peer": {
                        "address": "9.1.1.1",
                        "priority": 200,
                        "interface": "Po10.100",
                    },
                    "standby_peer": {"address": "Local"},
                    "log_counters": {
                        "role_change_to_active": 0,
                        "role_change_to_standby": 1,
                        "disable_events": {"rg_down_state": 0, "rg_shut": 0},
                        "ctrl_interface_events": {"up": 1, "down": 1, "admin_down": 0},
                        "reload_events": {"local_request": 0, "peer_request": 0},
                    },
                }
            },
            "rg_media_context": {
                1: {
                    "ctx_state": "Standby",
                    "protocol_id": 1,
                    "media_type": "Default",
                    "ctrl_interface": "Port-channel10.100",
                    "timers": {
                        "current_hello_timer": 3000,
                        "configured_hello_timer": 3000,
                        "hold_timer": 9000,
                        "peer_hello_timer": 3000,
                        "peer_hold_timer": 9000,
                    },
                    "stats": {
                        "pkts": 144780,
                        "bytes": 8976360,
                        "ha_seq": 0,
                        "seq_number": 144780,
                        "pkt_loss": 0,
                        "authentication": "not configured",
                        "authentication_failures": 0,
                        "reload_peer": {"tx": 0, "rx": 0},
                        "resign": {"tx": 0, "rx": 0},
                    },
                    "active_peer": {
                        "status": "Present",
                        "hold_timer": 9000,
                        "pkts": 144772,
                        "bytes": 4922248,
                        "ha_seq": 0,
                        "seq_number": 145489,
                        "pkt_loss": 0,
                    },
                }
            },
        },
        "2": {
            "fault_states_group": {
                "2": {
                    "runtime_priority": 175,
                    "rg_faults_rg_state": "Up",
                    "total_switchovers_due_to_faults": 0,
                    "total_down_or_up_state_changes_due_to_faults": 0,
                }
            },
            "group_name": "group2",
            "administrative_state": "No Shutdown",
            "aggregate_operational_state": "Up",
            "my_role": "STANDBY",
            "peer_role": "ACTIVE",
            "peer_presence": "Yes",
            "peer_comm": "Yes",
            "peer_progression_started": "Yes",
            "rf_domain": {
                "btob-two": {"rf_state": "STANDBY HOT", "peer_rf_state": "ACTIVE"}
            },
            "rg_protocol": {
                2: {
                    "role": "Standby",
                    "negotiation": "Enabled",
                    "priority": 175,
                    "protocol_state": "Standby-hot",
                    "ctrl_interfaces_state": "Up",
                    "active_peer": {
                        "address": "9.1.1.1",
                        "priority": 175,
                        "interface": "Po10.100",
                    },
                    "standby_peer": {"address": "Local"},
                    "log_counters": {
                        "role_change_to_active": 0,
                        "role_change_to_standby": 1,
                        "disable_events": {"rg_down_state": 0, "rg_shut": 0},
                        "ctrl_interface_events": {"up": 1, "down": 1, "admin_down": 0},
                        "reload_events": {"local_request": 0, "peer_request": 0},
                    },
                }
            },
            "rg_media_context": {
                2: {
                    "ctx_state": "Standby",
                    "protocol_id": 1,
                    "media_type": "Default",
                    "ctrl_interface": "Port-channel10.100",
                    "timers": {
                        "current_hello_timer": 3000,
                        "configured_hello_timer": 3000,
                        "hold_timer": 9000,
                        "peer_hello_timer": 3000,
                        "peer_hold_timer": 9000,
                    },
                    "stats": {
                        "pkts": 144780,
                        "bytes": 8976360,
                        "ha_seq": 0,
                        "seq_number": 144780,
                        "pkt_loss": 0,
                        "authentication": "not configured",
                        "authentication_failures": 0,
                        "reload_peer": {"tx": 0, "rx": 0},
                        "resign": {"tx": 0, "rx": 0},
                    },
                    "active_peer": {
                        "status": "Present",
                        "hold_timer": 9000,
                        "pkts": 144772,
                        "bytes": 4922248,
                        "ha_seq": 0,
                        "seq_number": 145489,
                        "pkt_loss": 0,
                    },
                }
            },
        },
    }
}
