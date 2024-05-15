expected_output = {
    'global_igmp': {
        'admin_state': 'Enabled',
        'admin_version': 2,
        'max_response_time': 10,
        'querier_timeout': 120,
        'query_interval': 100,
        'source_ip_address': '0.0.0.0',
        'tcn_query_count': 10,
        'tcn_query_interval': 10,
    },
    'vlan': {
        '10': {
            'admin_state': 'Enabled',
            'admin_version': 2,
            'max_response_time': 10,
            'operational_state': 'Non-Querier',
            'operational_version': 2,
            'querier_timeout': 120,
            'query_interval': 100,
            'source_ip_address': '10.1.1.1',
            'tcn_query_count': 10,
            'tcn_query_interval': 10,
            'tcn_query_pending_count': 0,
        },
    },
}