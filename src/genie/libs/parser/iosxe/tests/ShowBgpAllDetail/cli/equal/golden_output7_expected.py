expected_output = {
    'instance': {
        'default': {
            'vrf': {
                'default': {
                    'address_family': {
                        '': {
                            'prefixes': {
                                '5.5.5.5/32': {
                                    'available_path': '2',
                                    'best_path': '1',
                                    'index': {
                                        1: {
                                            'cluster_list': '1.1.1.1',
                                            'gateway': '1.1.1.1',
                                            'localpref': 1000,
                                            'metric': 0,
                                            'next_hop': '1.1.1.4',
                                            'next_hop_igp_metric': '11',
                                            'origin_codes': 'i',
                                            'originator': '1.1.1.1',
                                            'recipient_pathid': '0x0',
                                            'refresh_epoch': 1,
                                            'route_info': 'Local',
                                            'status_codes': '*>',
                                            'transfer_pathid': '0x0',
                                        },
                                        2: {
                                            'cluster_list': '1.1.1.1',
                                            'gateway': '1.1.1.1',
                                            'localpref': 100,
                                            'metric': 0,
                                            'mpls_labels': {
                                                'in': 'nolabel',
                                                'out': '17',
                                            },
                                            'next_hop': '1.1.1.3',
                                            'next_hop_igp_metric': '11',
                                            'origin_codes': 'i',
                                            'originator': '1.1.1.1',
                                            'recipient_pathid': '0x1',
                                            'refresh_epoch': 1,
                                            'route_info': 'Local',
                                            'status_codes': '* i',
                                            'transfer_pathid': '0',
                                        },
                                    },
                                    'paths': '2 available, best #1, table default',
                                    'table_version': '10016',
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}

