
expected_output = {
    'total_interfaces': 5,
    'total_sr_policies': 3,
    'total_endpoints': 2,
    'maximum_pps': 2000,
    'dual_color_gre': {
        'bit_pos': 11,
    },
    'interface_delay_measurement': {
        'total_sessions': 2,
        'counters': {
            'packets': {
                'sent': 288628,
                'received': 0,
            },
            'errors': {
                'sent_errors': 14,
                'received_errors': 0,
            },
            'probes': {
                'started': 28866,
                'completed': 0,
                'incomplete': 28864,
                'advertisements': 0,
            },
        },
    },
    'sr_policy_delay_measurement': {
        'total_sessions': 7,
        'counters': {
            'packets': {
                'sent': 3030386,
                'received': 3030374,
            },
            'errors': {
                'sent_errors': 0,
                'received_errors': 3,
            },
            'probes': {
                'started': 101024,
                'completed': 101017,
                'incomplete': 7,
                'advertisements': 688,
            },
        },
    },
    'endpoint_delay_measurement': {
        'total_sessions': 2,
        'counters': {
            'packets': {
                'sent': 288630,
                'received': 288630,
            },
            'errors': {
                'sent_errors': 14,
                'received_errors': 4,
            },
            'probes': {
                'started': 28866,
                'completed': 28859,
                'incomplete': 5,
                'advertisements': 421,
            },
        },
    },
    'interface_loss_measurement': {
        'total_sessions': 1,
        'counters': {
            'packets': {
                'sent': 14,
                'received': 13,
            },
            'errors': {
                'sent_errors': 0,
                'received_errors': 0,
            },
            'probes': {
                'started': 8,
                'completed': 7,
                'incomplete': 0,
                'advertisements': 1,
            },
        },
    },
    'global_counters': {
        'packets_sent': 3607644,
        'query_packets_received': 3319004,
        'invalid_session_id': 0,
        'no_session': 0,
    },
    'hw_support_mpls_gal_timestamp': 'Yes',
    'hw_support_ipv4_twamp_timestamp': 'Yes',
    'hw_support_ipv6_twamp_timestamp': 'No',
    'hw_support_64_bit_timestamp': 'Yes',
    'hw_support_ipv4_udp_checksum': 'Yes',
}