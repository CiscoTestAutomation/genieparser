expected_output = {
    'instance': {
        'default': {
            'vrf': {
                'default': {
                    'address_family': {
                        'ipv4 unicast': {
                            'prefix': {
                                '192.168.11.11/32': {
                                    'prefix': '192.168.11.11/32',
                                    'prefixversion': 14,
                                    'totalpaths': 1,
                                    'bestpathnr': 1,
                                    'flag_code': '0x08041a',
                                    'on_xmitlist': True,
                                    'in_urib': True,
                                    'best_urib_route': True,
                                    'in_hw': True,
                                    'path': {
                                        1: {
                                            'pathnr': 0,
                                            'advertised_path_id': 1,
                                            'pathtype': 'internal',
                                            'pathvalid': True,
                                            'pathbest': True,
                                            'in_rib': True,
                                            'imported_from': (
                                                '192.168.3.3:3:'
                                                '192.168.11.11/32'
                                            ),
                                            'imported_from_vrf': 'vni100',
                                            'as_path': '150',
                                            'as_path_source': 'external',
                                            'ipnexthop': '192.168.1.0',
                                            'nexthopmetric': 81,
                                            'neighbor': '192.168.101.101',
                                            'neighborid': '192.168.101.101',
                                            'origin': 'incomplete',
                                            'med': 0,
                                            'localpref': 100,
                                            'weight': 0,
                                            'inlabel': 100,
                                            'extcommunity': [
                                                'RT:100:100',
                                                'ENCAP:8',
                                                'Router MAC:5254.004e.a437',
                                            ],
                                            'originatorid': '192.168.1.0',
                                            'clusterlist': [
                                                '192.168.101.101',
                                            ],
                                            'advertisedto': [
                                                '192.168.30.2',
                                            ],
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}
