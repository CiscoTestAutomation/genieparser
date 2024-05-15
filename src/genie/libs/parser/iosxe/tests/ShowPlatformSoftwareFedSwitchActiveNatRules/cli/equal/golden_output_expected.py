expected_output = {
    'rules': {
        'dynamic': {
            'index': {
                1: {
                    'acl': 'test_out',
                    'overload': 'No',
                    'pool_interface_ip': 'outside_pool',
                    'rule_id': '0x80000002',
                    'type': 'Outside',
                    'vrf': 0
                },
                2: {
                    'acl': 'test_in',
                    'overload': 'No',
                    'pool_interface_ip': 'inside_pool',
                    'rule_id': '0x80000004',
                    'type': 'Inside',
                    'vrf': 0
                }
            },
            'number_of_rules': 2
        },
        'static': {
            'number_of_rules': 0
        }
    }
}