

expected_output = {
    'vrf': {
        'VRF1': {
            'interfaces': {
                'Loopback0': {
                    'interface_status': 'up',
                    'igmp_activity': {
                        'joins': 6,
                        'leaves': 0
                    },
                    'igmp_max_query_response_time': 10,
                    'igmp_querier_timeout': 125,
                    'igmp_query_interval': 60,
                    'last_member_query_response_interval': 1,
                    'igmp_querying_router': '10.16.2.2',
                    'igmp_querying_router_info': 'this system',
                    'igmp_state': 'enabled',
                    'time_elapsed_since_last_query_sent': '00:00:53',
                    'time_elapsed_since_last_report_received': '00:00:51',
                    'time_elapsed_since_router_enabled': '02:46:41',
                    'igmp_version': 3,
                    'ip_address': '10.16.2.2/32',
                    'line_protocol': 'up',
                    'oper_status': 'up'
                }
            }
        }
    }
}
