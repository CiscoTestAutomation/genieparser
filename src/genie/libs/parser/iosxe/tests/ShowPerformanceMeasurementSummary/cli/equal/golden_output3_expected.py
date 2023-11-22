
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
                'sent': 516,
                'received': 0,
            },
            'errors': {
                'sent_errors': 14,
                'received_errors': 0,
            },
            'probes': {
                'started': 54,
                'completed': 0,
                'incomplete': 52,
                'advertisements': 0,
            },
        },
    },
    'sr_policy_delay_measurement': {
        'total_sessions': 7,
        'counters': {
            'packets': {
                'sent': 5344,
                'received': 5344,
            },
            'errors': {
                'sent_errors': 0,
                'received_errors': 0,
            },
            'probes': {
                'started': 175,
                'completed': 175,
                'incomplete': 0,
                'advertisements': 21,
            },
        },
    },
    'endpoint_delay_measurement': {
        'total_sessions': 2,
        'counters': {
            'packets': {
                'sent': 516,
                'received': 516,
            },
            'errors': {
                'sent_errors': 14,
                'received_errors': 0,
            },
            'probes': {
                'started': 54,
                'completed': 50,
                'incomplete': 2,
                'advertisements': 2,
            },
        },
    },
    'interface_loss_measurement': {
        'total_sessions': 1,
        'counters': {
            'packets': {
                'sent': 7229,
                'received': 7228,
            },
            'errors': {
                'sent_errors': 0,
                'received_errors': 0,
            },
            'probes': {
                'started': 3615,
                'completed': 3614,
                'incomplete': 0,
                'advertisements': 1,
            },
        },
    },
    'global_counters': {
        'packets_sent': 6376,
        'query_packets_received': 5860,
        'invalid_session_id': 0,
        'no_session': 0,
    },
    'hw_support_mpls_gal_timestamp': 'Yes',
    'hw_support_ipv4_twamp_timestamp': 'Yes',
    'hw_support_ipv6_twamp_timestamp': 'No',
    'hw_support_64_bit_timestamp': 'Yes',
    'hw_support_ipv4_udp_checksum': 'Yes',
    'max_packets_per_burst': 2000,
    'querier_rx_queue': {
        'size': 0,
        'enqueues': 5860,
        'high_water_mark': 7,
        'high_water_mark_time': '19 1970 09:42:09.484',
    },
    'responder_rx_queue': {
        'size': 0,
        'enqueues': 0,
        'high_water_mark': 0,
        'high_water_mark_time': 'N/A',
    },
    'querier_im_queue': {
        'size': 0,
        'enqueues': 1,
        'high_water_mark': 1,
        'high_water_mark_time': '19 1970 09:42:09.038',
    },
    'querier_cfg_queue': {
        'size': 0,
        'enqueues': 1793,
        'high_water_mark': 58,
        'high_water_mark_time': '19 1970 09:42:09.039',
    },
    'querier_chkpt_queue': {
        'size': 0,
        'enqueues': 0,
        'high_water_mark': 0,
        'high_water_mark_time': 'N/A',
    },
    'udp_port_gal_oob_ipv4': 63426,
    'udp_port_gal_oob_ipv6': 59792,
    'udp_port_twamp_query_ipv4': 862,
    'udp_port_twamp_query_ipv6': 862,
    'udp_port_twamp_reply_ipv4': 49963,
    'udp_port_twamp_reply_ipv6': 65299,
    'udp_port_sdlm_query_ipv4': 6634,
    'udp_port_sdlm_query_ipv6': 6634,
    'udp_port_sdlm_reply_ipv4': 50119,
    'udp_port_sdlm_reply_ipv6': 57446,
    'last_error_querier': {
        'info': 'Unknown destination address type 0.',
        'timestamp': '06:30:28  20 2021',
        'session_id': 2,
    },
    'last_error_receive': {
        'info': 'Failed to enqueue CFG',
        'timestamp': '06:30:10  20 2021',
    },
    'pm_runtime': {
        0: {
            'name': 'CP PROBE START',
            'last': 34000,
            'avg': 341861,
            'total': 44442000,
            'cnt': 130,
            'wrapped': 0,
        },
        1: {
            'name': 'CP BURST TIMER',
            'last': 263000,
            'avg': 307949,
            'total': 1150808000,
            'cnt': 3737,
            'wrapped': 0,
        },
        2: {
            'name': 'CFG GET INFO',
            'last': 23000,
            'avg': 51676,
            'total': 302825000,
            'cnt': 5860,
            'wrapped': 0,
        },
        3: {
            'name': 'FIB_FWD',
            'last': 12000,
            'avg': 46990,
            'total': 275367000,
            'cnt': 5860,
            'wrapped': 0,
        },
    },
}