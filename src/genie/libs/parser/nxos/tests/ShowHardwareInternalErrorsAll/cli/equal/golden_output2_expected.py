expected_output = {
    'slot': {
        1: {
            'device_records': [
                {
                    'device': 'Sacramento Xbar ASIC',
                    'role': 'MAC',
                    'mod': 1,
                    'last_cleared': 'Thu Oct  1 14:59:35 2026',
                    'category': 'ERROR',
                    'instance': {
                        0: {
                            'counter': {
                                196616: {
                                    'name': 'Interface Inbound Errors '
                                            '(CRC,len,Algn Err)',
                                    'value': 30003,
                                    'ports': '1-48 I1',
                                },
                            },
                        },
                    },
                },
                {
                    'device': 'Clipper XBAR',
                    'role': 'MAC',
                    'mod': 1,
                    'last_cleared': 'Thu Oct  1 14:59:35 2026',
                    'category': 'ERROR',
                    'instance': {
                        0: {
                            'counter': {
                                196616: {
                                    'name': 'Interface Inbound Errors '
                                            '(CRC,len,Algn Err)',
                                    'value': 13,
                                    'ports': '5-8 -',
                                },
                            },
                        },
                    },
                },
            ],
        },
    },
}
