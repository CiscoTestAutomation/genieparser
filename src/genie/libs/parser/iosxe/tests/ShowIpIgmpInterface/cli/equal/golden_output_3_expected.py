expected_output = {
    'vrf': {
        'default': {
            'interface': {
                'GigabitEthernet0/0/4': {
                    'configured_querier_timeout': 120,
                    'configured_query_interval': 60,
                    'counters': {
                        'joins': 1,
                        'leaves': 0,
                    },
                    'enable': True,
                    'host_version': 2,
                    'interface_address': '200.1.1.1/24',
                    'interface_status': 'up',
                    'last_member_query_count': 2,
                    'last_member_query_interval': 1000,
                    'multicast': {
                        'designated_router': '200.1.1.1',
                        'dr_this_system': True,
                        'routing_enable': True,
                        'ttl_threshold': 0,
                    },
                    'oper_status': 'up',
                    'querier': '200.1.1.1',
                    'querier_timeout': 120,
                    'query_interval': 60,
                    'query_max_response_time': 10,
                    'query_this_system': True,
                    'router_version': 2,
                },
            },
        },
    },
}
