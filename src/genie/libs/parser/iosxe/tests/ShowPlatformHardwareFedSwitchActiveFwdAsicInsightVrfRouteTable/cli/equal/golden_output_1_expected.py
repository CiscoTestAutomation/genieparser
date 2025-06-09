expected_output = {
    'vrf_route_table': {
        2: {
            'ip_version': 4,
            'routes': [
                {
                    'ip_prefix': '14.1.0.255/32',
                    'dest_type': 'for_us',
                    'dest_id': 0,
                    'dest_info': 'N/A',
                    'class_id': 0,
                    'drop': False,
                    'route_user_data': '104865530382056'
                },
                {
                    'ip_prefix': '14.1.0.0/24',
                    'dest_type': 'host',
                    'dest_id': 0,
                    'dest_info': 'N/A',
                    'class_id': 0,
                    'drop': False,
                    'route_user_data': '0'
                },
                {
                    'ip_prefix': '14.1.0.0/32',
                    'dest_type': 'for_us',
                    'dest_id': 0,
                    'dest_info': 'N/A',
                    'class_id': 0,
                    'drop': False,
                    'route_user_data': '104865571485592'
                }
            ]
        }
    }
}