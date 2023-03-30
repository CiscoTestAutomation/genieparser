expected_output = {
    'vpls_name': {
        'TEST': {
            'interface': {
                'Te0/3/0': {
                    'encapsulation': 'Te0/3/0:5516(Eth VLAN)',
                    'priority': 0,
                    'state': 'UP',
                    'state_in_l2vpn_service': 'UP',
                },
                'pw100039': {
                    'encapsulation': '10.67.120.222:670055516(MPLS)',
                    'group': 'CA',
                    'priority': 1,
                    'state': 'UP',
                    'state_in_l2vpn_service': 'UP',
                },
                'pw100040': {
                    'encapsulation': '10.68.120.222:670055516(MPLS)',
                    'group': 'CA',
                    'priority': 2,
                    'state': 'SB',
                    'state_in_l2vpn_service': 'IA',
                },
            },
            'state': 'UP',
        },
        'Test_incomplete': {
            'state': 'Incomplete',
        },
    },
}
