expected_output = {
    'vpls_name': {
        'CAMPUS_E_O1': {
            'interface': {
                'Gi0/0/0': {
                    'encapsulation': 'Gi0/0/0:8(Ethernet)',
                    'priority': 0,
                    'state': 'UP',
                    'state_in_l2vpn_service': 'UP',
                },
                'pw100011': {
                    'encapsulation': '10.201.99.82:16(MPLS)',
                    'priority': 0,
                    'state': 'UP',
                    'state_in_l2vpn_service': 'UP',
                },
            },
            'state': 'UP',
        },
        'EVPL-1900-MPLS-to-ASR-BKB-O1': {
            'interface': {
                'Te0/1/3': {
                    'encapsulation': 'Te0/1/3:1900(Eth VLAN)',
                    'priority': 0,
                    'state': 'UP',
                    'state_in_l2vpn_service': 'UP',
                },
                'pw1900': {
                    'encapsulation': '10.201.99.82:1900(MPLS)',
                    'priority': 0,
                    'state': 'UP',
                    'state_in_l2vpn_service': 'UP',
                },
            },
            'state': 'UP',
        },
        'EVPL-ALLVLANBMEDNAStoASR-BKB-O1': {
            'interface': {
                'Gi1/0/0': {
                    'encapsulation': 'Gi1/0/0:1(Ethernet)',
                    'priority': 0,
                    'state': 'UP',
                    'state_in_l2vpn_service': 'UP',
                },
                'pw9001': {
                    'encapsulation': '10.201.99.82:9001(MPLS)',
                    'priority': 0,
                    'state': 'UP',
                    'state_in_l2vpn_service': 'UP',
                },
            },
            'state': 'UP',
        },
        'RMA-VPLS': {
            'interface': {
                '-': {
                    'encapsulation': 'RMA-VPLS(VFI)',
                    'priority': 0,
                    'state': 'UP',
                    'state_in_l2vpn_service': 'UP',
                },
                'pw100028': {
                    'encapsulation': 'RMA-VPLS(VFI)',
                    'priority': 0,
                    'state': 'UP',
                    'state_in_l2vpn_service': 'UP',
                },
                'pw100031': {
                    'encapsulation': '5004:5000(MPLS)',
                    'group': 'core_pw',
                    'priority': 0,
                    'state': 'UP',
                    'state_in_l2vpn_service': 'UP',
                },
            },
            'state': 'UP',
        },
    },
}
