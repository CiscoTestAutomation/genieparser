expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv6': {
                    'instance': {
                        'mpls1': {
                            'areas': {
                                '0.0.0.0': {
                                    'database': {
                                        'lsa_types': {
                                            9: {
                                                'lsa_type': 9,
                                                'lsas': {
                                                    '0 95.95.95.95': {
                                                        'adv_router': '95.95.95.95',
                                                        'lsa_id': 0,
                                                        'ospfv3': {
                                                            'body': {
                                                                'number_of_prefix': 3,
                                                                'prefixes': {
                                                                    1: {
                                                                        'metric': 10,
                                                                        'options': 'None',
                                                                        'prefix_address': '2001:200:10::',
                                                                        'prefix_length': 64,
                                                                        'priority': 'Low'
                                                                    },
                                                                    2: {'metric': 1,
                                                                        'options': 'None',
                                                                        'prefix_address': '2001:100:20::',
                                                                        'prefix_length': 64,
                                                                        'priority': 'Low'
                                                                    },
                                                                    3: {'metric': 0,
                                                                        'options': 'LA',
                                                                        'prefix_address': '95::95',
                                                                        'prefix_length': 128,
                                                                        'priority': 'Medium'
                                                                    }
                                                                }
                                                            },
                                                            'header': {
                                                                'adv_router': '95.95.95.95',
                                                                'age': 1784,
                                                                'checksum': '0x2ce8',
                                                                'length': 76,
                                                                'lsa_id': 0,
                                                                'ref_adv_router': '95.95.95.95',
                                                                'ref_lsa_id': 0,
                                                                'ref_lsa_type': '2001',
                                                                'routing_bit_enable': True,
                                                                'seq_num': '8000081f',
                                                                'type': 'Intra-Area-Prefix-LSA'
                                                            }
                                                        }
                                                    },
                                                    '0 96.96.96.96': {
                                                        'adv_router': '96.96.96.96',
                                                        'lsa_id': 0,
                                                        'ospfv3': {
                                                            'body': {
                                                                'number_of_prefix': 3,
                                                                'prefixes': {
                                                                    1: {
                                                                        'metric': 1,
                                                                        'options': 'None',
                                                                        'prefix_address': '2001:100:10::',
                                                                        'prefix_length': 64,
                                                                        'priority': 'Low'
                                                                    },
                                                                    2: {'metric': 10,
                                                                        'options': 'None',
                                                                        'prefix_address': '2001:200:10::',
                                                                        'prefix_length': 64,
                                                                        'priority': 'Low'
                                                                    },
                                                                    3: {'metric': 0,
                                                                        'options': 'LA',
                                                                        'prefix_address': '96::96',
                                                                        'prefix_length': 128,
                                                                        'priority': 'Medium'
                                                                    }
                                                                }
                                                            },
                                                            'header': {
                                                                'adv_router': '96.96.96.96',
                                                                'age': 501,
                                                                'checksum': '0xd641',
                                                                'length': 76,
                                                                'lsa_id': 0,
                                                                'ref_adv_router': '96.96.96.96',
                                                                'ref_lsa_id': 0,
                                                                'ref_lsa_type': '2001',
                                                                'routing_bit_enable': True,
                                                                'seq_num': '80000822',
                                                                'type': 'Intra-Area-Prefix-LSA'
                                                            }
                                                        }
                                                    },
                                                    '0 99.99.99.99': {
                                                        'adv_router': '99.99.99.99',
                                                         'lsa_id': 0,
                                                         'ospfv3': {
                                                             'body': {
                                                                 'number_of_prefix': 3,
                                                                 'prefixes': {
                                                                     1: {
                                                                         'metric': 1,
                                                                         'options': 'None',
                                                                         'prefix_address': '2001:100:10::',
                                                                         'prefix_length': 64,
                                                                         'priority': 'Low'
                                                                     },
                                                                     2: {'metric': 1,
                                                                         'options': 'None',
                                                                         'prefix_address': '2001:100:20::',
                                                                         'prefix_length': 64,
                                                                         'priority': 'Low'
                                                                     },
                                                                     3: {'metric': 0,
                                                                         'options': 'LA',
                                                                         'prefix_address': '2001:1100::1001',
                                                                         'prefix_length': 128,
                                                                         'priority': 'Medium'
                                                                     }
                                                                 }
                                                             },
                                                             'header': {
                                                                 'adv_router': '99.99.99.99',
                                                                 'age': 1000,
                                                                 'checksum': '0x2e86',
                                                                 'length': 76,
                                                                 'lsa_id': 0,
                                                                 'ref_adv_router': '99.99.99.99',
                                                                 'ref_lsa_id': 0,
                                                                 'ref_lsa_type': '2001',
                                                                 'routing_bit_enable': True,
                                                                 'seq_num': '80000059',
                                                                 'type': 'Intra-Area-Prefix-LSA'
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
             }
         }
     }
}
