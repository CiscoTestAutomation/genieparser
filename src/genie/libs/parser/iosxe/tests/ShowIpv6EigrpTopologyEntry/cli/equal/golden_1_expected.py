expected_output = {
    '5001::/64': {
        'autonomous_system_number': 101,
        'descriptor_blocks': {
            'FE80::20C:29FF:FED4:B578': {
                'composite_metric': '3072/2816',
                'from': 'FE80::20C:29FF:FED4:B578',
                'interface': 'vmi1',
                'route': 'Internal',
                'send_flag': '0x0',
                'vector_metrics': {
                    'hop_count': 1,
                    'load': '2/255',
                    'minimum_bandwidth': 1000000,
                    'minimum_mtu': 1492,
                    'originating_router': '10.10.1.1',
                    'reliability': '255/255',
                    'total_delay': 20
                }
            }
        },
        'feasible_distance': 3072,
        'num_successors': 1,
        'query_origin_flag': 1,
        'router_id': '10.9.1.1',
        'state': 'Passive'
    }
}