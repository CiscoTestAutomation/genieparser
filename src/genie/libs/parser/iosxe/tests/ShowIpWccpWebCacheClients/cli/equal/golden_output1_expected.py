expected_output = {
    'wccp_client_information': {
        '10.1.100.10': {
            'client_id': '10.1.100.10',
            'protocol_version': '2.0',
            'state': 'Usable',
            'redirection': 'GRE',
            'packet_return': 'GRE',
            'assignment': 'HASH',
            'packets_redirected': 1234567,
            'connect_time': '01:12:45',
        },
        '10.1.100.11': {
            'client_id': '10.1.100.11',
            'protocol_version': '2.0',
            'state': 'Usable',
            'redirection': 'L2',
            'packet_return': 'L2',
            'assignment': 'MASK',
            'packets_redirected': 987654,
            'connect_time': '00:45:12',
        }
    }
}
