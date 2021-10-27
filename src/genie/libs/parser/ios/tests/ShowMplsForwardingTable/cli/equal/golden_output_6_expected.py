expected_output = {
    'vrf': {
        'default': {
            'local_label': {
                24: {
                    'outgoing_label_or_vc': {
                        'No Label': {
                            'prefix_or_tunnel_id': {
                                '10.23.120.0/24': {
                                    'outgoing_interface': {
                                        'GigabitEthernet2.120': {
                                            'next_hop': '10.12.120.2',
                                            'bytes_label_switched': 0
                                        },
                                        'GigabitEthernet3.120': {
                                            'next_hop': '10.13.120.3',
                                            'bytes_label_switched': 0
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                25: {
                    'outgoing_label_or_vc': {
                        'No Label': {
                            'prefix_or_tunnel_id': {
                                '10.23.120.0/24[V]': {
                                    'outgoing_interface': {
                                        'GigabitEthernet2.420': {
                                            'next_hop': '10.12.120.2',
                                            'bytes_label_switched': 0
                                        },
                                        'GigabitEthernet3.420': {
                                            'next_hop': '10.13.120.3',
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
