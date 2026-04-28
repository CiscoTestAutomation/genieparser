expected_output = {
    101: {
        'grpc-tcp': {
            'connection': 65535,
            'explanation': 'Receiver active',
            'state': 'Timeout backoff'},
        'grpc-tls': {
            'connection': 65535,
            'explanation': 'Receiver invalid',
            'state': 'Disconnected'
        }
    },
    102: {
        'grpc-tcp': {
            'connection': 65535,
            'explanation': 'Subscription invalid',
            'state': 'Disconnected'
        },
        'grpc-tls': {
            'connection': 65535,
            'explanation': 'Subscription invalid',
            'state': 'Disconnected'
        }
    }
}
