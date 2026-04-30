expected_output = {
    'id': {
        101: {
            'state': 'Invalid',
            'stream': 'NETCONF',
            'filter': {
                'filter_type': 'not specified'
            }, 'update_policy': {
                'update_trigger': 'not specified'
            },
            'encoding': 'encode-xml',
            'receivers': {
                'grpc-tcp://169.254.0.1:20006': {
                    'last_update': '04/22/26 12:09:14',
                    'state': 'Disconnected',
                    'notes': 'Subscription invalid'
                }
            }
        }
    }
}
