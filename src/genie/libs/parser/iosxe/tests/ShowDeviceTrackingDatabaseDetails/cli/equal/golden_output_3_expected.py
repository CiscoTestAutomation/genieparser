expected_output = {
        'vlandb': {
            'vlan_id': 70,
            'total_entries': 5,
            'dynamic_entries': 5
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
            'reachable': 7,
            'total': 9
        },
        'device': {
            1: {
            'dev_code': 'DH4',
            'network_layer_address': '100.70.0.42',
            'link_layer_address': 'f8a5.c5eb.44ab(S)',
            'interface': 'Gi3/0/46',
            'mode': 'access',
            'vlan_id': 70,
            'pref_level_code': 24,
            'age': '95s',
            'state': 'VERIFY',
            'time_left': '38 s try 3(204 s)',
            'filter': 'no',
            'in_crimson': 'yes',
            'client_id': 'f8a5.c5eb.44ab',
            'policy': '(unspecified)              DT-PROGRAMMATIC (Device-tracking)'
            },
            2: {
            'dev_code': 'DH4',
            'network_layer_address': '100.70.0.49',
            'link_layer_address': '1caa.07e2.959a(R)',
            'interface': 'Gi2/0/46',
            'mode': 'access',
            'vlan_id': 70,
            'pref_level_code': 24,
            'age': '34s',
            'state': 'REACHABLE',
            'time_left': '26 s(177 s)',
            'filter': 'no',
            'in_crimson': 'yes',
            'client_id': '1caa.07e2.959a',
            'policy': '(unspecified)              DT-PROGRAMMATIC (Device-tracking)'
            },
            3: {
            'dev_code': 'ARP',
            'network_layer_address': '100.70.2.2',
            'link_layer_address': '5061.bfc0.4c73(R)',
            'interface': 'Po126',
            'mode': 'trunk',
            'vlan_id': 70,
            'pref_level_code': 5,
            'age': '34s',
            'state': 'REACHABLE',
            'time_left': '26 s',
            'filter': 'no',
            'in_crimson': 'yes',
            'client_id': '0000.0000.0000',
            'policy': '(unspecified)              DT-PROGRAMMATIC (Device-tracking)'
            },
            4: {
            'dev_code': 'ND',
            'network_layer_address': 'FE80::5261:BFFF:FEC0:4C73',
            'link_layer_address': '5061.bfc0.4c73(R)',
            'interface': 'Po126',
            'mode': 'trunk',
            'vlan_id': 70,
            'pref_level_code': 5,
            'age': '19s',
            'state': 'REACHABLE',
            'time_left': '41 s',
            'filter': 'no',
            'in_crimson': 'yes',
            'client_id': '0000.0000.0000',
            'policy': '(unspecified)              DT-PROGRAMMATIC (Device-tracking)'
            }
        }
        }
