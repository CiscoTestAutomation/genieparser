

expected_output = {
    'groups': {
        'pe1-to-pe2': {
            'name': {
                'vpws_bl1_pe2': {
                    'segment1': {
                        'TenGigabitEthernet0/0/0/3/1.200': {
                            'segment2': {
                                'EVPN 12222,32222,10.4.1.1': {
                                    'status': 'UP'}
                            },
                            'status': 'UP'}
                    },
                    'status': 'UP'},
                'vpws_pe1_pe1': {
                    'segment1': {
                        'TenGigabitEthernet0/0/0/3/1.100': {
                            'segment2': {
                                'EVPN 11111,31111,10.4.1.1': {
                                    'status': 'UP'}
                            },
                            'status': 'UP'}
                        },
                    'status': 'UP'}
                }
            }
        }
    }
