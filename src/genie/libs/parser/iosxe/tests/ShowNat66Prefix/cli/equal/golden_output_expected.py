expected_output = {
    'nat66_prefix': {
        'prefixes_configured': 3,
        'ra_prefixes_configured': 0,
        'nat66_prefixes': {
            '1': {
                'id': 1,
                'inside': 'FD62:1B53:AFFB:1201::/112',
                'outside': '2001:4888:AFFB:1201::/112',
            },
            '2': {
                'id': 2,
                'inside': 'FD62:1B53:AFFB:1202::/112',
                'outside': '2001:4888:AFFB:1202::/112',
                'vrf': 'MPN1202',
            },
            '3': {
                'id': 3,
                'inside': 'FD62:1B53:AFFB:1203::/112',
                'outside': '2001:4888:AFFB:1203::/112',
                'vrf': 'MPN1203',
            },
        },
    },
}