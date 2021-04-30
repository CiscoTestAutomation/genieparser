expected_output = {
    'power-usage-information': {
        'power-usage-item': [
            {
                'name': 'PSM 0',
                'state': 'Online',
                'dc-input-detail2': {
                    'dc-input-status':
                    'OK (INP0 feed expected, INP0 feed connected)'
                },
                'pem-capacity-detail': {
                    'capacity-actual': '2100',
                    'capacity-max': '2500'
                },
                'dc-output-detail2': {
                    'str-dc-power': '489.25',
                    'str-zone': 'Lower',
                    'str-dc-current': '9.50',
                    'str-dc-voltage': '51.50',
                    'str-dc-load': '23.30'
                }
            },  
            {
                'name': 'PSM 1',
                'state': 'Empty',
                'input': 'Absent'
            },
            {
                'name': 'PSM 2',
                'state': 'Online',
                'dc-input-detail2': {
                    'dc-input-status':
                    'OK (INP0 feed expected, INP0 feed connected)'
                },
                'pem-capacity-detail': {
                    'capacity-actual': '2100',
                    'capacity-max': '2500'
                },
                'dc-output-detail2': {
                    'str-dc-power': '504.56',
                    'str-zone': 'Lower',
                    'str-dc-current': '9.75',
                    'str-dc-voltage': '51.75',
                    'str-dc-load': '24.03'
                }
            } 
        ],
        'power-usage-system': {
            'power-usage-zone-information': [{
                'str-zone': 'Upper',
                'capacity-actual': '6300',
                'capacity-max': '7500',
                'capacity-allocated': '3332',
                'capacity-remaining': '2968',
                'capacity-actual-usage': '925.50'
            }, {
                'str-zone': 'Lower',
                'capacity-actual': '8400',
                'capacity-max': '10000',
                'capacity-allocated': '6294',
                'capacity-remaining': '2106',
                'capacity-actual-usage': '1974.69'
            }],
            'capacity-sys-actual':
            '14700',
            'capacity-sys-max':
            '17500',
            'capacity-sys-remaining':
            '5074'
        }
    }
}
