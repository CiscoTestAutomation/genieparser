expected_output = {
    'tunnel_prot_stats': {
        'message_stats': {
            'sent': {
                'listen_start': 1,
                'listen_stop': 0,
                'socket_open': 0,
                'socket_close': 0
            },
            'recieved': {
                'general_error': 0,
                'socket_error': 0,
                'socket_ready': 0,
                'socket_up': 0,
                'socket_down': 0,
                'mtu_changed': 0,
                'listen_ready': 1,
                'other': 0
            },
        },
        'error_stats': {
            'recieved': {
                'listen_start': 0,
                'listen_stop': 0,
                'socket_open': 0,
                'socket_close': 0,
                'connection_timeout': 0
            },
        },
        'data_stats': {
            'sent': {
                'cef_packet_drop': 0,
                'ps_packet_drop': 0
            },
            'recieved': {
                'ps_packet_drop': 0,
                'clear_packet_drop': 0
            }
        }
    }
}