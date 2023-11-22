expected_output = {
    'static_mappings': {
        'index': {
            1: {
                'address': '2001:1::2',
                'direction': 'v6v4',
                'is_valid': 'FALSE',
                'mapping_id': 0,
                'non_key_address': '1.1.1.2',
                'protocol': '---',
                'rg_id': 0
            },
            2: {
                'address': '2001:1::2 (1234)',
                'direction': 'v6v4',
                'is_valid': 'FALSE',
                'mapping_id': 0,
                'non_key_address': '1.1.1.2 (100)',
                'protocol': 'TCP',
                'rg_id': 0
            },
            3: {
                'address': '2002:1::2',
                'direction': 'v6v4',
                'is_valid': 'FALSE',
                'mapping_id': 1,
                'non_key_address': '2.2.2.1',
                'protocol': '---',
                'rg_id': 16
            },
            4: {
                'address': '2009:1::2',
                'direction': 'v6v4',
                'is_valid': 'FALSE',
                'mapping_id': 0,
                'non_key_address': '10.10.10.2',
                'protocol': '---',
                'rg_id': 0
            }
        },
        'no_of_mappings': 4
    }
}
