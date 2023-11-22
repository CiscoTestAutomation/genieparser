expected_output = {
    'vrf': {
        'default': {
            'interfaces': {
                'Bundle-Ether40051': {
                    'sync': {
                        'delay': 5,
                        'status': 'Not ready (No peer session)',
                    },
                },
                'Bundle-Ether40055': {
                    'sync': {
                        'delay': 5,
                        'peers': {
                            '10.120.0.10:0': {
                                'graceful_restart': False,
                            },
                        },
                        'status': 'Ready',
                    },
                },
            },
            'vrf_index': '0x60000000',
        },
    },
}
