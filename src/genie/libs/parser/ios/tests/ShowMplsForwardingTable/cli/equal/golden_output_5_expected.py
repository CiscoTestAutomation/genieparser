expected_output = {
    'vrf': {
        'default': {
            'local_label': {
                'None': {
                    'outgoing_label_or_vc': {
                        'No Label': {
                            'prefix_or_tunnel_id': {
                                '10.0.0.16/30': {
                                    'outgoing_interface': {
                                        'GigabitEthernet3': {
                                            'next_hop': '10.0.0.9',
                                            'bytes_label_switched': 0
                                        },
                                        'GigabitEthernet4': {
                                            'next_hop': '10.0.0.13',
                                            'bytes_label_switched': 0
                                        },
                                        'GigabitEthernet5': {
                                            'next_hop': '10.0.0.25',
                                            'bytes_label_switched': 0
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
