expected_output = {
    'vrf': {
        'default': {
            'local_label': {
                16022: {
                    'outgoing_label_or_vc': {
                        'Pop Label': {
                            'prefix_or_tunnel_id': {
                                '10.151.22.22/32': {
                                    'outgoing_interface': {
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
