expected_output = {
        'record_name': {
            'group-udp-tcp-10001': {
                'endpoint': 'tcp-10002 OR udp-10002',
                'endpoint_type': 'N/A',
                'threshold': 'N/A',
                'multiplier': 'N/A',
                'interval': 'N/A',
                'tracker_type': 'tracker-group'
            },
            'nat-dia-tracker-4351': {
                'endpoint': '151.151.151.1',
                'endpoint_type': 'IP',
                'threshold': '300',
                'multiplier': '3',
                'interval': '60',
                'tracker_type': 'interface'
            },
            'tcp-10001': {
                'endpoint': '10.157.10.2',
                'endpoint_type': 'TCP',
                'threshold': '100',
                'multiplier': '1',
                'interval': '20',
                'tracker_type': 'static-route'
            },
            'tcp-10002': {
                'endpoint': '10.160.10.2',
                'endpoint_type': 'UDP',
                'threshold': '100',
                'multiplier': '1',
                'interval': '20',
                'tracker_type': 'static-route'
            },
            'udp-10001': {
                'endpoint': '10.157.10.2',
                'endpoint_type': 'UDP',
                'threshold': '100',
                'multiplier': '1',
                'interval': '20',
                'tracker_type': 'static-route'
            },
            'udp-10002': {
                'endpoint': '10.160.10.2',
                'endpoint_type': 'UDP',
                'threshold': '100',
                'multiplier': '1',
                'interval': '20',
                'tracker_type': 'static-route'
            },
            'track1': {
                'endpoint': '198.168.20.2',
                'endpoint_type': 'IP',
                'threshold': '300',
                'multiplier': '3',
                'interval': '60',
                'tracker_type': 'interface'
            },
            'track3': {
                'endpoint': 'www.diatracker.com',
                'endpoint_type': 'DNS_NAME',
                'threshold': '300',
                'multiplier': '3',
                'interval': '60',
                'tracker_type': 'interface'
            }
        }
    }
