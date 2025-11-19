expected_output = {
    'parameter_maps': {
        'global': {
            'name': 'global',
            'index': 1,
            'type': 'Parameter-Map',
            'global_parameter_map': True,
            'alerts': 'On',
            'audits': 'Off',
            'drop_log': 'Off',
            'hsl_mode': 'V9',
            'host': '10.1.1.1:9000',
            'port': 54174,
            'template': '300 sec',
            'session_rate_high': 2147483647,
            'session_rate_low': 2147483647,
            'time_duration': '60 sec',
            'half_open': {
                'high': 2147483647,
                'low': 2147483647,
                'host': 4294967295,
                'host_block_time': 0,
            },
            'inactivity_times': {
                'dns': 5,
                'icmp': 10,
                'tcp': 3600,
                'udp': 30,
            },
            'tcp_timeouts': {
                'syn_wait_time': 30,
                'fin_wait_time': 1,
            },
            'tcp_rst_pkt_control': {
                'half_open': 'On',
                'half_close': 'On',
                'idle': 'On',
            },
            'udp_timeout': {
                'udp_half_open_time': 30000,
            },
            'max_sessions': 'Unlimited',
            'number_of_simultaneous_packet_per_sessions': 0,
            'syn_cookie_and_resource_management': {
                'global_syn_flood_limit': 4294967295,
                'global_total_session': 4294967295,
            },
        }
    }
}