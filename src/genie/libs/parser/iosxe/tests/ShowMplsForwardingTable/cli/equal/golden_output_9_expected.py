expected_output = {
    'vrf': {
        'default': {
            'local_label': {
                25: {
                    'outgoing_label_or_vc': {
                        '16021': {
                            'prefix_or_tunnel_id': {
                                '0-23.23.23.23/32-4': {
                                    'outgoing_interface': {
                                        'Ethernet0/2': {
                                            'next_hop': '13.1.1.2',
                                            'bytes_label_switched': 0,
                                            'flexalgo_info': {
                                                'pdb_index': 10,
                                                'metric': 30,
                                                'algo': 130,
                                                'via_srms': 1
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
}