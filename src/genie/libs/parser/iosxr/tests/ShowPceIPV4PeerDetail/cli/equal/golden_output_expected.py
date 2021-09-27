

expected_output = {
    'pce_peer_database': {
        '192.168.0.1': {
            'state': 'Up',
            'capabilities': {
                'stateful': True,
                'segment-routing': True,
                'update': True
            },
            'pcep': {
                'uptime': '00:01:50',
                'session_id_local': 0,
                'session_id_remote': 0
            },
            'ka': {
                'sending_intervals': 30,
                'minimum_acceptable_inteval': 20
            },
            'peer_timeout': 120,
            'statistics': {
                'rx': {
                    'keepalive_messages': 4,
                    'request_messages': 3,
                    'reply_messages': 0,
                    'error_messages': 0,
                    'open_messages': 1,
                    'report_messages': 4,
                    'update_messages': 0,
                    'initiate_messages': 0
                },
                'tx': {
                    'keepalive_messages': 4,
                    'request_messages': 0,
                    'reply_messages': 3,
                    'error_messages': 0,
                    'open_messages': 1,
                    'report_messages': 0,
                    'update_messages': 2,
                    'initiate_messages': 0
                }
            }
        }
    }
}
