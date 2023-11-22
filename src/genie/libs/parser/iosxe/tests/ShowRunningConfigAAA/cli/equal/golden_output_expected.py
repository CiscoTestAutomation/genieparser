expected_output = {
    'group_server': {
        'radius': {
            'RADIUS_GROUP': {
                'server_name': 'RADIUS_1',
                'source_interface': 'TenGigabitEthernet1/0/13',
                'vrf': 'newVRF2'
            },
            'sr1': {
                'server_name': 'r1',
                'source_interface': 'GigabitEthernet0/0',
                'vrf': 'Mgmt-vrf'
            }
        },
        'tacacs+': {
            'tacacs_1': {
                'server_name': 'tacas_1',
                'source_interface': 'GigabitEthernet0/0',
                'vrf': 'Mgmt-vrf'
            },
            'tacas_1': {
                'source_interface': 'GigabitEthernet0/0'
            }
        }
    },
    'new_model': True,
    'radius': {
        'server': {
            'RADIUS_1': {
                'acct_port': 1813,
                'address': '11.15.24.213',
                'address_type': 'ipv4',
                'auth_port': 1812,
                'key': 'Cisco123'
            },
            'RADIUS_GROUP': {},
            'r1': {
                'acct_port': 1813,
                'address': '1.1.1.1',
                'address_type': 'ipv4',
                'auth_port': 1812,
                'key': 'Cisco123'
            }
        }
    },
    'session_id': 'common',
    'tacacs': {
        'server': {
            'tacas_1': {
                'address': 'AAAA::BBBB',
                'address_type': 'ipv6',
                'key': 'cisco345'
            }
        }
    }
}

