expected_output = {
    'lisp_id': {
        0: {
            'home_instance': 101,
            'total': 5,
            'eid_prefix': {
                '88.88.88.0/24': {
                    'type': 'Provider',
                    'source': 'Dynamic',
                    'iid': 103,
                    'eid': '88.88.88.0',
                    'mask': 24
                    },
                '100.100.100.0/24': {
                    'type': 'Provider',
                    'source': 'Dynamic',
                    'iid': 103,
                    'eid': '100.100.100.0',
                    'mask': 24
                    },
                '200.200.200.0/24': {
                    'type': 'Provider',
                    'source': 'Dynamic',
                    'iid': 103,
                    'eid': '200.200.200.0',
                    'mask': 24
                    },
                '192.168.0.1/32': {
                    'type': 'Subscriber',
                    'source': 'Dynamic',
                    'iid': 101,
                    'eid': '192.168.0.1',
                    'mask': 32
                    },
                '192.168.9.1/32': {
                    'type': 'Subscriber',
                    'source': 'Dynamic',
                    'iid': 101,
                    'eid': '192.168.9.1',
                    'mask': 32
                    }
                }
            }
        }
    }