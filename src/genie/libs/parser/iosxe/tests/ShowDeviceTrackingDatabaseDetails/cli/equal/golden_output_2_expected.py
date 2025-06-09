expected_output = {
        'portdb': {
            'interface': 'Gi2/0/46',
            'total_entries': 1,
            'dynamic_entries': 1
        },
        'binding_table_configuration': {
            'max/box': 'no limit',
            'max/vlan': 'no limit',
            'max/port': 'no limit',
            'max/mac': 'no limit'
        },
        'binding_table_count': {
            'dynamic': 9,
            'local': 0,
            'total': 9
        },
        'binding_table_state_count': {
            'verify': 2,
            'reachable': 6,
            'stale': 1,
            'total': 9
        },
        'device': {
            1: {
            'dev_code': 'DH4',
            'network_layer_address': '100.70.0.49',
            'link_layer_address': '1caa.07e2.959a(S)',
            'interface': 'Gi2/0/46',
            'mode': 'access',
            'vlan_id': 70,
            'pref_level_code': 24,
            'age': '61s',
            'state': 'VERIFY',
            'time_left': '8 s try 2(150 s)',
            'filter': 'no',
            'in_crimson': 'yes',
            'client_id': '1caa.07e2.959a',
            'policy': '(unspecified)              DT-PROGRAMMATIC (Device-tracking)'
            }
        }
        }
