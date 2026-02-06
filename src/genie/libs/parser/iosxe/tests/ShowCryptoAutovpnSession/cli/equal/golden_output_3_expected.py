expected_output = {
    'local': {
        'device_id': '20030000000000000000000000000000',
        'device_number': '2003',
        'local_wan': {
            'wan_1': {
                'interface': 'TenGigabitEthernet0/0/9',
                'nat_type': 'Friendly',
                'private_ip': '21.21.21.2',
                'private_port': '4500',
            },
        },
        'registry_1': {
            'ip': '10.124.22.98',
            'port': '9350',
            'wan_1': {
                'ip': '10.74.9.192',
                'port': '5065',
                'status': 'Connected',
            },
        },
        'registry_2': {
            'ip': '10.124.22.98',
            'port': '9351',
            'wan_1': {
                'ip': '10.74.9.192',
                'port': '5065',
                'status': 'Connected',
            },
        },
        'role': 'Spoke',
    },
    'peer': {
        0: {
            'peer_id': '20090000000000000000000000000000',
            'peer_number': '2009',
            'role': 'Hub',
            'wan_1': {
                'registry_1': {
                    'private_ip': '23.23.23.2',
                    'private_port': '4500',
                    'public_ip': '10.74.9.192',
                    'public_port': '5440',
                },
                'registry_2': {
                    'private_ip': '23.23.23.2',
                    'private_port': '4500',
                    'public_ip': '10.74.9.192',
                    'public_port': '5440',
                },
            },
        },
    },
    'session': {
        0: {
            'initiator': 'Yes',
            'interface': 'Vi1',
            'local_ip': '21.21.21.2',
            'local_port': '4500',
            'local_wan': 1,
            'peer_ip': '23.23.23.2',
            'peer_number': '2009',
            'peer_port': '4500',
            'peer_wan': 1,
            'session_type': 'Private',
            'status': 'Connected',
        },
        1: {
            'initiator': 'Yes',
            'interface': 'Vi2',
            'local_ip': '21.21.21.2',
            'local_port': '4500',
            'local_wan': 1,
            'peer_ip': '24.24.24.2',
            'peer_number': '2009',
            'peer_port': '4500',
            'peer_wan': 2,
            'session_type': 'Private',
            'status': 'Connected',
        }
    }
}