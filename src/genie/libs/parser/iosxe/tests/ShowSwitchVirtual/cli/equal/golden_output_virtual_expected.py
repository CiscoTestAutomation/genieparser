
expected_output = {
    'vss_member_id': {
        1: {
            'role': "VSS Active",
            'mode': "Virtual Switch",
            'domain_number': 123,
            'local_switch': {
                'switch_number': 1,
                'operational_role': 'Virtual Switch Active'
            },
            'peer_switch': {
                'switch_number': 2,
                'operational_role': 'Virtual Switch Standby'
            }
        },
        2: {
            'role': "VSS Standby",
            'mode': "Virtual Switch",
            'domain_number': 123,
            'local_switch': {
                'switch_number': 2,
                'operational_role': 'Virtual Switch Standby'
            },
            'peer_switch': {
                'switch_number': 1,
                'operational_role': 'Virtual Switch Active'
            }
        }
    }
}