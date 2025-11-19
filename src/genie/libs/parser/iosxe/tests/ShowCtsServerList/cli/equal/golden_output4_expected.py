expected_output = {
    'global_server_liveness_automated_test': {
        'dead_time': 20,
        'dead_time_unit': 'secs',
        'idle_time': 60,
        'idle_time_unit': 'mins',
        'status': 'ENABLED (default)',
    },
    'installed_list': {
        'CTSServerList1-0006': {
            '172.23.27.221': {
                'a_id': '361CB222CFE7E875B7293A50834CC2A4',
                'auto_test_status': False,
                'dead_time': 20,
                'dead_time_unit': 'secs',
                'idle_time': 60,
                'idle_time_unit': 'mins',
                'keywrap_enable': False,
                'port_number': 1812,
                'server_ip': '172.23.27.221',
                'status': 'ALIVE',
            },
        },
    },
    'load_balance_status': 'DISABLED',
    'server_group_dead_time': 20,
    'server_group_dead_time_unit': 'secs',
}
