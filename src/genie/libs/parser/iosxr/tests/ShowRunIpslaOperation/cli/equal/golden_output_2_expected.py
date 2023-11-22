expected_output = {
    'ipsla': {
        'operations': {
            100: {
                'type': {
                    'udp jitter': {
                        'vrf': 'VRF-1',
                        'src_addr': '1.1.1.1',
                        'dest_addr': '2.2.2.2',
                        'packet': {'count': 1000, 'interval': 20},
                        'time_out': 3000,
                        'data_size_req': 500,
                        'dest_port': 15000,
                        'frequency': 60,
                        'verify-data': True
                    }
                }
            },
            200: {
                'type': {
                    'udp jitter': {
                        'vrf': 'VRF-2',
                        'src_addr': '3.3.3.3',
                        'dest_addr': '4.4.4.4',
                        'packet': {'count': 1500, 'interval': 20},
                        'time_out': 4000,
                        'data_size_req': 500,
                        'dest_port': 10000,
                        'frequency': 60,
                        'verify-data': True
                    }
                }
            }
        }
    }
}