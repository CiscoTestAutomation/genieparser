expected_output = {
    'crypto_gdoi_group_name': {
        'bw600-IPV6_eft': {
            'group_handle': 1073741871,
            'local_key_server_handle': 1073741919,
            'local_address': '15.15.15.1',
            'local_priority': 245,
            'local_ks_role': 'Primary',
            'local_ks_status': 'Alive',
            'local_ks_version': '1.0.27',
            'local_coop_version': '1.0.8',
            'primary_timers': {
                'primary_refresh_policy_time': 20,
                'remaining_time': 11,
                'per_user_timer_remaining_time': 0,
                'antireplay_sequence_number': 124,
            },
            '1': {
                'server_handle': 1073741917,
                'peer_address': '16.16.16.1',
                'peer_version': '1.0.27',
                'peer_coop_version': '1.0.8',
                'coop_protocol': 'base',
                'peer_priority': 200,
                'peer_ks_role': 'Secondary',
                'peer_ks_status': 'Alive',
                'antireplay_sequence_number': 5,
                'ike_status': 'Established',
                'counters': {
                    'ann_msgs_sent': 122,
                    'ann_msgs_sent_with_reply_request': 1,
                    'ann_msgs_recv': 4,
                    'ann_msgs_recv_with_reply_request': 1,
                    'packet_sent_drops': 1,
                    'packet_recv_drops': 0,
                    'total_bytes_sent': 104495,
                    'total_bytes_recv': 2130
                }
            }
        }    
    }
}
