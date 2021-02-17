expected_output = {
    'type':{
        'IP route': {
            'address': '172.16.52.0',
            'mask': '255.255.255.0',
            'state': 'Down',
            'state_description': 'no route',
            'change_count': 1,
            'last_change': '00:00:35',
            'threshold_down': 255,
            'threshold_up': 254,
        }
    },
    'delay_up_seconds': 2.0,
    'delay_down_seconds': 1.0,
    'first_hop_interface_state': 'unknown',
}


"""
expected_output = {
    'tracks': {
        1: {
            'type': 'IP route',
            'ip_address': '172.16.52.0',
            'subnet_mask': '255.255.255.0',
            'parameter': 'metric threshold',
            'metric_threshold': {
                'parameter_state': 'Down',
                'issue': 'no route',
                'change_count': 1,
                'last_change': '00:00:35',
                'threshold_down': 255,
                'threshold_up': 254,
            },
            'delay_up_seconds': 2.0,
            'delay_down_seconds': 1.0,
            'first_hop_interface_state': 'unknown',
        }
    }
}
"""