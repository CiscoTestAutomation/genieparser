expected_output = {
    'vrf': {
        'default': {
            'local_label': {
                201: {
                    'outgoing_label_or_vc': {
                        'Pop tag': {
                            'prefix_or_tunnel_id': {
                                '10.18.18.18/32': {
                                    'outgoing_interface': {
                                        'Port-channel1/1/0': {
                                            'next_hop': 'point2point',
                                            'bytes_label_switched': 0
                                        }
                                    }
                                }
                            }
                        },
                        '2/35': {
                            'prefix_or_tunnel_id': {
                                '10.18.18.18/32': {
                                    'outgoing_interface': {
                                        'ATM4/1/0.1': {
                                            'next_hop': 'point2point',
                                            'bytes_label_switched': 0
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                251: {
                    'outgoing_label_or_vc': {
                        '18': {
                            'prefix_or_tunnel_id': {
                                '10.17.17.17/32': {
                                    'outgoing_interface': {
                                        'Port-channel1/1/0': {
                                            'next_hop': 'point2point',
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
