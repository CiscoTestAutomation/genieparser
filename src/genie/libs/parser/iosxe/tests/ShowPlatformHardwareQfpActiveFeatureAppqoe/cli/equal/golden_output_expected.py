expected_output = {
    'feature': {
    'appqoe': {
        'global': {
        'ip_non_tcp_pkts': 0,
        'not_enabled': 0,
        'cft_handle_pkt': 0,
        'sdvt_divert_req_fail': 139,
        'sn_data_pkts_processed': 0,
        'sdvt_global_stats': {
            'appnav_registration': 64,
            'control_decaps_could_not_find_flow_from_tuple': 2,
            'within_sdvt_syn_policer_limit': 33131
                }
            },
        'sn_index': {
        '0 (Green)': {
            'ip': '10.136.2.250',
            'oce_id': 1092284384,
            'del': 0,
            'key': '0x0301',
            'id': 1,
            'ver': 1,
            'status': 1,
            'type': 3,
            'sng': 0,
            'appnav_stats': {
            'to_sn': {
                'packets': 23357718,
                'bytes': 18288051565
                },
            'from_sn': {
                'packets': 21249179,
                'bytes': 18466919498
                }
            },
            'sdvt_count_stats': {
            'active_connections': 1328,
            'decaps': 21222127,
            'encaps': 23357729,
            'expired_connections': 28546,
            'idle_timed_out_persistent_connections': 1603,
            'decap_messages': {
                'processed_control_messages': 26991,
                'delete_requests_recieved': 26991,
                'deleted_protocol_decision': 26991
                }
            },
            'sdvt_packet_stats': {
            'divert': {
                'packets': 23357734,
                'bytes': 17166890183
                },
            'reinject': {
                'packets': 21221637,
                'bytes': 17063783593
                }
            },
            'sdvt_drop_cause_stats': {},
            'sdvt_errors_stats': {}
        },
        'Default': {
            'sdvt_count_stats': {
            'decaps': 27,
            'packets_unmarked_in_ingress': 139
            },
            'sdvt_packet_stats': {},
            'sdvt_drop_cause_stats': {},
            'sdvt_errors_stats': {}
                }
            }
        }
    }
}
