
expected_output = {
    'total_interfaces': 5,
    'total_sr_policies': 3,
    'total_endpoints': 2,
    'maximum_pps': 2000,
    'dual_color_gre': {
        'bit_pos': 9,
        'info': 'Failed, last success 0',
    },
    'interface_delay_measurement': {
        'total_sessions': 2,
        'counters': {
            'packets': {
                'sent': 100,
                'received': 0,
            },
            'errors': {
                    'tx': {
                        'interface_down': 0,
                        'no_mpls_caps': 0,
                        'no_ip_address': 0,
                        'other': 14,
                    },
                    'rx': {
                        'negative_delay': 0,
                        'delay_threshold_exceeded': 0,
                        'missing_tx_timestamp': 0,
                        'missing_rx_timestamp': 0,
                        'probe_full': 0,
                        'probe_not_started': 0,
                        'control_code_error': 0,
                        'control_code_notif': 0,
                    },
            },
            'probes': {
                'started': 12,
                'completed': 0,
                'incomplete': 10,
                'advertisements': 0,
            },
        },
    },
    'sr_policy_delay_measurement': {
        'total_sessions': 7,
        'counters': {
            'packets': {
                'sent': 980,
                'received': 980,
            },
            'errors': {
                    'tx': {
                        'no_ip_address': 0,
                        'other': 0,
                    },
                    'rx': {
                        'negative_delay': 0,
                        'delay_threshold_exceeded': 0,
                        'missing_tx_timestamp': 0,
                        'missing_rx_timestamp': 0,
                        'probe_full': 0,
                        'probe_not_started': 0,
                        'control_code_error': 0,
                        'control_code_notif': 0,
                    },
            },
            'probes': {
                'started': 28,
                'completed': 28,
                'incomplete': 0,
                'advertisements': 7,
            },
        },
    },
    'endpoint_delay_measurement': {
        'total_sessions': 2,
        'counters': {
            'packets': {
                'sent': 100,
                'received': 100,
            },
            'errors': {
                    'tx': {
                        'interface_down': 0,
                        'no_mpls_caps': 0,
                        'no_ip_address': 0,
                        'other': 14,
                    },
                    'rx': {
                        'negative_delay': 0,
                        'delay_threshold_exceeded': 0,
                        'missing_tx_timestamp': 0,
                        'missing_rx_timestamp': 0,
                        'probe_full': 0,
                        'probe_not_started': 0,
                        'control_code_error': 0,
                        'control_code_notif': 0,
                    },
            },
            'probes': {
                'started': 12,
                'completed': 8,
                'incomplete': 2,
                'advertisements': 2,
            },
        },
    },
    'interface_loss_measurement': {
        'total_sessions': 1,
        'counters': {
            'packets': {
                'sent': 7159,
                'received': 7158,
            },
            'errors': {
                    'tx': {
                        'interface_down': 0,
                        'no_mpls_caps': 0,
                        'no_ip_address': 0,
                        'other': 0,
                    },
                    'rx': {
                        'negative_delay': 0,
                        'delay_threshold_exceeded': 0,
                        'missing_tx_timestamp': 0,
                        'missing_rx_timestamp': 0,
                        'probe_full': 0,
                        'probe_not_started': 0,
                        'control_code_error': 0,
                        'control_code_notif': 0,
                    },
            },
            'probes': {
                'started': 3580,
                'completed': 3579,
                'incomplete': 0,
                'advertisements': 1,
            },
        },
    },
    'global_counters': {
        'packets_sent': 7159,
        'query_packets_received': 7158,
        'invalid_session_id': 0,
        'no_session': 0,
    },
    'hw_support_mpls_gal_timestamp': 'Yes',
    'hw_support_ipv4_twamp_timestamp': 'Yes',
    'hw_support_ipv6_twamp_timestamp': 'No',
    'hw_support_64_bit_timestamp': 'Yes',
    'hw_support_ipv4_udp_checksum': 'Yes',
}