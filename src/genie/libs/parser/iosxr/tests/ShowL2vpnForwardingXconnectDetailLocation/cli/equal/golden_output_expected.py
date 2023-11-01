expected_output = {
    'local_interface': 'Bundle-Ether5.1001',
    'xconnect_id': '0xc0000002',
    'status': 'up',
    'segment': {
        '1': {
            'segment_type': 'AC',
            'ac_interface': 'Bundle-Ether5.1001',
            'status': 'Bound',
            'statistics': {
                'packets': {
                    'received': 2497,
                    'sent': 2462
                },
                'bytes': {
                    'received': 282604,
                    'sent': 277640
                }
            }
        },
        '2': {
            'segment_type': 'SRv6 EVPN',
            'internal_id': '::ffff:10.0.0.1',
            'evi': 1001,
            'ac_id': 10001,
            'status': 'Bound',
            'control_word': 'disabled',
            'statistics': {
                'packets': {
                    'received': 2462,
                    'sent': 2497
                },
                'bytes': {
                    'received': 277640,
                    'sent': 282604
                }
            }
        }
    }
}
