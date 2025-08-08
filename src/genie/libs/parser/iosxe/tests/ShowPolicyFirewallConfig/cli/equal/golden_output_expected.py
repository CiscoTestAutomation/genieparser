expected_output = {
    "zone_pair": {
        "in-out": {
            "source_zone": "inside",
            "source_interfaces": [
                "GigabitEthernet0/1/3"
            ],
            "destination_zone": "outside",
            "destination_interfaces": [
                "GigabitEthernet0/1/0"
            ],
            "service_policy": {
                "name": "pmap",
                "class_map": {
                    "nested_cmap": {
                        "match_type": "match-any",
                        "match_criteria": [
                            "match class-map cmap",
                            "match protocol tcp"
                        ],
                        "action": "inspect",
                        "parameter_map": "param"
                    },
                    "class-default": {
                        "match_type": "match-any",
                        "match_criteria": [
                            "match any"
                        ],
                        "action": "drop log",
                        "parameter_map": "Default"
                    }
                }
            }
        }
    },
    "parameter_map_configuration": {
        "parameter_map_type_inspect": "param",
        "alert_messages": "on",
        "all_application_inspection": "on",
        "audit_trailing": "off",
        "logging_dropped_packets": "off",
        "logging_flow": "off",
        "utd_context_id": 0,
        "icmp_session_idle_time": {
            "idle": "60 sec",
            "ageout": "60 sec"
        },
        "dns_session_idle_time": "5 sec",
        "tcp_session_half_open": {
            "half_open": "on",
            "half_close": "on",
            "idle": "on"
        },
        "tcp_session_idle_time": {
            "idle": "80 sec",
            "ageout": "80 sec"
        },
        "tcp_session_fin_wait_time": {
            "wait": "1 sec",
            "ageout": "1 sec"
        },
        "tcp_session_syn_wait_time": {
            "wait": "30 sec",
            "ageout": "30 sec"
        },
        "tcp_loose_window_scaling_enforcement": "off",
        "tcp_max_half_open_connections": {
            "value": "unlimited",
            "block_time": "0 min"
        },
        "udp_half_open_session_idle_time": {
            "idle": "30000 ms",
            "ageout": "30000 ms"
        },
        "udp_session_idle_time": {
            "idle": "60 sec",
            "ageout": "60 sec"
        },
        "sessions_connections_threshold_low": "unlimited",
        "sessions_connection_threshold_high": "unlimited",
        "sessions_connection_rate_threshold_low": "unlimited",
        "sessions_connection_rate_threshold_high": "unlimited",
        "sessions_max_incomplete_threshold_low": "unlimited",
        "sessions_max_incomplete_threshold_high": "unlimited",
        "sessions_max_inspect_sessions": "unlimited",
        "total_packets_per_flow": "default",
        "zone_mismatch_drop_option": "off"
    }
}
