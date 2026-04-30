expected_output = {
    'name': {
        'grpc-tcp': {
            'type': 'protocol',
            'profile': '',
            'state': 'Valid',
            'explanation': 'Receiver validated'
        },
        'grpc-tls': {
            'type': 'protocol',
            'profile': '',
            'state': 'Invalid',
            'explanation': "Value 'unspecified' not supported for parameter 'protocol'."},
        'pullrecv': {
            'type': 'pull mode',
            'profile': '',
            'state': 'Valid',
            'explanation': 'Receiver validated'
        }
    }
}
