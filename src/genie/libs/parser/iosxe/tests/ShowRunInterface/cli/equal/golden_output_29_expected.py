expected_output =  {
    'interfaces': {
        'FiftyGigE1/1/2': {
            'storm_control': {
                'action': 'trap',
                'broadcast': {
                    'level': '100m',
                    'low_level': '50m',
                },
                'multicast': {
                    'level': '100m',
                    'low_level': '50m',
                },
                'unicast': {
                    'level': '20k',
                },
                'unknown-unicast': {
                    'level': '20k',
                },
            },
            'switchport_access_vlan': '100',
            'switchport_mode': 'access',
        },
    },
}
