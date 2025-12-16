expected_output = {
    'zonepair': {
        'class_group': {
            'id': 14841376,
            'name': 'policy1',
        },
        'classes': [
            {
                'name': 'c-ftp-tcp',
                'id': 13549553,
                'number_of_protocols': 4,
                'protocols': [1, 2, 4, 18],
                'maxever_number_of_packet_per_flow': 25,
                'addresses': {
                    'filler_block': '0x8967f400',
                    'action_block': '0x8d70f400',
                    'stats_table': '0x898d7400',
                    'stats_blocks': ['0x8d716c00', '0x8d716c40', '0x8d716c80', '0x8d716cc0']
                },
                'result': ['0x08000000', '0x8967f400'],
                'filler_block': {
                    'sw': '0x8d70f400898d7400',
                    'hw': '0x0000000c00000000'
                }
            },
            {
                'name': 'class-default',
                'id': 1593,
                'number_of_protocols': 0,
                'maxever_number_of_packet_per_flow': 0,
                'addresses': {
                    'filler_block': '0x8967f400',
                    'action_block': '0x8d70f400',
                    'stats_table': '0x898d7400',
                    'stats_blocks': ['0x8d716c00', '0x8d716c40', '0x8d716c80', '0x8d716cc0']
                },
                'result': ['0x08000000', '0x8967f400'],
                'filler_block': {
                    'sw': '0x8d70f400898d7400',
                    'hw': '0x0000000c00000000'
                }
            },
            {
                'name': 'class-default',
                'id': 1593,
                'number_of_protocols': 0,
                'maxever_number_of_packet_per_flow': 0,
                'addresses': {
                    'filler_block': '0x8967f408',
                    'action_block': '0x8d70f4f0',
                    'stats_table': '0x898d7520'
                },
                'result': ['0x81000000', '0x8967f408'],
                'filler_block': {
                    'sw': '0x8d70f4f0898d7520',
                    'hw': '000000000000000000'
                }
            }
        ],
        'destination_zone': {
            'id': 1,
            'name': 'ge0-0-3',
        },
        'id': 1,
        'lookup_data': {
            'hw': ['0x00010003', '0x00084441'],
            'sw': ['0x00010003', '0x00084441'],
        },
        'name': 'zp-ge000-ge003',
        'source_zone': {
            'id': 2,
            'name': 'ge0-0-0',
        },
    }
}
