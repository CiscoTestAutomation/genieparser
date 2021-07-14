expected_output = {
    'enforcement': 'stressed',
        'entries': {
            1: {
                'target': "Twe1/0/1",
                'type': "PORT",
                'policy': "poll",
                'feature': "Destination Guard",
                'target_type': "vlan",
                'range': 'all',
            },
            2: {
                'target': "vlan 5",
                'type': "VLAN",
                'policy': "poll",
                'feature': "Destination Guard",
                'target_type': "vlan",
                'range': 'all',
            },
            3: {
                'target': "vlan 38",
                'type': "VLAN",
                'policy': "poll",
                'feature': "Destination Guard",
                'target_type': "vlan",
                'range': 'all',
            },
            4: {
                'target': "vlan 39",
                'type': "VLAN",
                'policy': "poll",
                'feature': "Destination Guard",
                'target_type': "vlan",
                'range': 'all',
            },
        }
}