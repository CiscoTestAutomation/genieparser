expected_output = {
    'rules': {
        'dynamic': {
            'index': {
                2: {
                     'acl': 'acl_1',
                     'overload': 'Yes',
                     'pool_interface_ip': 'pool_1',
                     'rule_id': '0x80000001',
                     'type': 'Inside',
                     'vrf': 0
                },
                3: {
                    'acl': 'nat_acl_1',
                    'overload': 'No',
                    'pool_interface_ip': 'pool_in_1',
                    'rule_id': '0x80000002',
                    'type': 'Inside',
                    'vrf': 0
                }
            },
            'number_of_rules': 2
        },
        'static': {
            'index': {
                1: {
                    'domain': 'outside',
                    'global_ip': '35.0.0.2',
                    'global_port': 0,
                    'local_ip': '102.0.0.2',
                    'local_port': 0,
                    'network': 32,
                    'protocol': 'any',
                    'rule_id': '0x1',
                    'type': ' ',
                    'vrf': 0
                }
            },
            'number_of_rules': 1
        }
    }
}