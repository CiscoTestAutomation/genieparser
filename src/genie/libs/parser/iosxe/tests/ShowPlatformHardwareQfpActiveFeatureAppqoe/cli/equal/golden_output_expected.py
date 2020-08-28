expected_output = {
    "feature": {
        "appqoe": {
            "global": {
                "cft_handle_pkt": 0,
                "ip_non_tcp_pkts": 0,
                "not_enabled": 0,
                "sdvt_divert_req_fail": 0,
                "sdvt_global_stats": {
                    "appnav_registration": 1,
                    "within_sdvt_syn_policer_limit": 266004,
                },
                "syn_policer_rate": 800,
            },
            "sn_index": {
                "0 (Green)": {
                    "sdvt_count_stats": {
                        "decap_messages": {
                            "delete_requests_recieved": 14200,
                            "deleted_protocol_decision": 14200,
                            "processed_control_messages": 14200,
                        },
                        "decaps": 679143,
                        "encaps": 743013,
                        "expired_connections": 64609,
                        "idle_timed_out_persistent_connections": 50409,
                        "packets_unmarked_in_ingress": 502868,
                    },
                    "sdvt_drop_cause_stats": {},
                    "sdvt_errors_stats": {},
                    "sdvt_packet_stats": {
                        "divert": {"bytes": 43313261, "packets": 743013},
                        "reinject": {"bytes": 503129551, "packets": 679010},
                    },
                },
                "Default": {
                    "sdvt_count_stats": {},
                    "sdvt_drop_cause_stats": {},
                    "sdvt_errors_stats": {},
                    "sdvt_packet_stats": {},
                },
            },
        }
    }
}
