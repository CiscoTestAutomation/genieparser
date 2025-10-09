expected_output = {
    'eigrp_instance': { 
        '100': { 
            'hello_process': { 
                'expiration': [ 
                    '1.724',
                    '1.724',
                    '2.294',
                    '2.923'
                ],
                'type': [ 
                    '(parent)',
                    'Hello (Te0/0/6.20)',
                    'Hello (Te0/0/4)',
                    'Hello (Te0/0/10)'
                ]
            },
            'sia_process': { 
                'expiration': [
                    '0.000'
                    ],
                'type': [
                    '(parent)'
                ]
            },
            'update_process': {
                'expiration': [
                    '4.780',
                    '4.780',
                    '4.780',
                    '4.780',
                    '10.457',
                    '10.457',
                    '11.220',
                    '11.220',
                    '12.303',
                    '12.303'
                ],
                'type': [
                    '(parent)',
                    '(parent)',
                    '(parent)',
                    'Peer transmission',
                    '(parent)',
                    'Peer holding',
                    '(parent)',
                    'Peer holding',
                    '(parent)',
                    'Peer holding'
                ]
            }
        }
    }
}