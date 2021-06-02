expected_output = {
    "fault_state_group_id": {
        "1": {
            "runtime_priority": {
                "200": {
                    "rg_faults_rg_state": {
                        "Up": {
                            "total_switchovers_due_to_faults": "0",
                            "total_down_or_up_state_changes_due_to_faults": "0"
                        }
                    }
                }
            }
        },
        "2": {
            "runtime_priority": {
                "175": {
                    "rg_faults_rg_state": {
                        "Up": {
                            "total_switchovers_due_to_faults": "0",
                            "total_down_or_up_state_changes_due_to_faults": "0"
                        }
                    }
                }
            }
        }
    },
    "group_id": {
        "1": {
            "group_name": "group1",
            "administrative_state": "No Shutdown",
            "aggregate_oper_state": "Up",
            "my_role": "STANDBY",
            "peer_role": "ACTIVE",
            "peer_presence": "Yes",
            "peer_comm": "Yes",
            "peer_progression_started": "Yes",
            "rf_domain": {
                "btob-one": {
                    "rf_state": "STANDBY HOT",
                    "peer_rf_state": "ACTIVE"
                }
            }
        },
        "2": {
            "group_name": "group2",
            "administrative_state": "No Shutdown",
            "aggregate_oper_state": "Up",
            "my_role": "STANDBY",
            "peer_role": "ACTIVE",
            "peer_presence": "Yes",
            "peer_comm": "Yes",
            "peer_progression_started": "Yes",
            "rf_domain": {
                "btob-two": {
                    "rf_state": "STANDBY HOT",
                    "peer_rf_state": "ACTIVE"
                }
            }
        }
    },
    "rg_protocol_for_rg": {
        "1": {
            "role": "Standby",
            "negotiation": "Enabled",
            "priority": "200",
            "protocol_state": "Standby-hot",
            "ctrl_intf_state": "Up",
            "active_peer_address": "9.1.1.1",
            "active_peer_priority": "200",
            "active_peer_intf": "Po10.100",
            "standby_peer": "Local",
            "log_counters": {
                "1": {
                    "role_change_to_active": "0",
                    "role_change_to_standby": "1",
                    "disable_events": "rg down state 0, rg shut 0",
                    "ctrl_intf_events": "up 1, down 1, admin_down 0",
                    "reload_events": "local request 0, peer request 0"
                }
            }
        },
        "2": {
            "role": "Standby",
            "negotiation": "Enabled",
            "priority": "175",
            "protocol_state": "Standby-hot",
            "ctrl_intf_state": "Up",
            "active_peer_address": "9.1.1.1",
            "active_peer_priority": "175",
            "active_peer_intf": "Po10.100",
            "standby_peer": "Local",
            "log_counters": {
                "1": {
                    "role_change_to_active": "0",
                    "role_change_to_standby": "1",
                    "disable_events": "rg down state 0, rg shut 0",
                    "ctrl_intf_events": "up 1, down 1, admin_down 0",
                    "reload_events": "local request 0, peer request 0"
                }
            }
        }
    },
    "rg_media_context_for_rg": {
        "1": {
            "ctx_state": "Standby",
            "protocol_id": "1",
            "media_type": "Default",
            "control_interface": "Port-channel10.100",
            "current_hello_timer": "3000",
            "configured_hello_timer": "3000",
            "hold_timer": "9000",
            "peer_hello_timer": "3000",
            "peer_hold_timer": "9000",
            "stats": {
                "1": {
                    "pkts": "144780",
                    "bytes": "8976360",
                    "ha_seq": "0",
                    "seq_number": "144780",
                    "pkt_loss": "0",
                    "authentication_status": "not configured",
                    "authentication_failure": "0",
                    "reload_peer": "TX 0, RX 0",
                    "resign": "TX 0, RX 0"
                }
            },
            "active_peer_status": "Present",
            "active_peer_hold_timer": "9000",
            "active_peer_stats": {
                "1": {
                    "pkts": "144772",
                    "bytes": "4922248",
                    "ha_seq": "0",
                    "seq_number": "145489",
                    "pkt_loss": "0"
                }
            }
        },
        "2": {
            "ctx_state": "Standby",
            "protocol_id": "1",
            "media_type": "Default",
            "control_interface": "Port-channel10.100",
            "current_hello_timer": "3000",
            "configured_hello_timer": "3000",
            "hold_timer": "9000",
            "peer_hello_timer": "3000",
            "peer_hold_timer": "9000",
            "stats": {
                "1": {
                    "pkts": "144780",
                    "bytes": "8976360",
                    "ha_seq": "0",
                    "seq_number": "144780",
                    "pkt_loss": "0",
                    "authentication_status": "not configured",
                    "authentication_failure": "0",
                    "reload_peer": "TX 0, RX 0",
                    "resign": "TX 0, RX 0"
                }
            },
            "active_peer_status": "Present",
            "active_peer_hold_timer": "9000",
            "active_peer_stats": {
                "1": {
                    "pkts": "144772",
                    "bytes": "4922248",
                    "ha_seq": "0",
                    "seq_number": "145489",
                    "pkt_loss": "0"
                }
            }
        }
    }
}
