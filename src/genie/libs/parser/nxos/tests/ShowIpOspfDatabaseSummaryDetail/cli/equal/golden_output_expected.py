

expected_output = {
    'vrf':
        {'default':
            {'address_family':
                {'ipv4':
                    {'instance':
                        {'1':
                            {'areas':
                                {'0.0.0.1':
                                    {'database':
                                        {'lsa_types':
                                            {3:
                                                {'lsa_type': 3,
                                                'lsas':
                                                    {'10.1.2.0 10.100.2.2':
                                                        {'lsa_id': '10.1.2.0',
                                                        'adv_router': '10.100.2.2',
                                                        'ospfv2':
                                                            {'body':
                                                                {'summary':
                                                                    {'network_mask': '255.255.255.0',
                                                                    'topologies':
                                                                        {0:
                                                                            {'metric': 4294,
                                                                            'mt_id': 0,
                                                                            'tos': 0}}}},
                                                            'header':
                                                                {'adv_router': '10.100.2.2',
                                                                'age': 788,
                                                                'checksum': '0xfc54',
                                                                'length': 28,
                                                                'lsa_id': '10.1.2.0',
                                                                'option': '0x22',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'seq_num': '0x80000001',
                                                                'type': 3}}},
                                                    '10.1.2.0 10.36.3.3':
                                                        {'lsa_id': '10.1.2.0',
                                                        'adv_router': '10.36.3.3',
                                                        'ospfv2':
                                                            {'body':
                                                                {'summary':
                                                                    {'network_mask': '255.255.255.0',
                                                                    'topologies':
                                                                        {0:
                                                                            {'metric': 151,
                                                                            'mt_id': 0,
                                                                            'tos': 0}}}},
                                                            'header':
                                                                {'adv_router': '10.36.3.3',
                                                                'age': 632,
                                                                'checksum': '0x5655',
                                                                'length': 28,
                                                                'lsa_id': '10.1.2.0',
                                                                'option': '0x2',
                                                                'option_desc': 'No TOS-capability, No DC',
                                                               'seq_num': '0x80000002',
                                                               'type': 3}}},
                                                    '10.1.3.0 10.36.3.3':
                                                        {'lsa_id': '10.1.3.0',
                                                        'adv_router': '10.36.3.3',
                                                        'ospfv2':
                                                            {'body':
                                                                {'summary':
                                                                    {'network_mask': '255.255.255.0',
                                                                    'topologies':
                                                                        {0:
                                                                            {'metric': 40,
                                                                            'mt_id': 0,
                                                                            'tos': 0}}}},
                                                            'header':
                                                                {'adv_router': '10.36.3.3',
                                                                'age': 642,
                                                                'checksum': '0xf029',
                                                                'length': 28,
                                                                'lsa_id': '10.1.3.0',
                                                                'option': '0x2',
                                                                'option_desc': 'No TOS-capability, No DC',
                                                               'seq_num': '0x80000002',
                                                               'type': 3}}},
                                                    '10.2.3.0 10.100.2.2':
                                                        {'lsa_id': '10.2.3.0',
                                                        'adv_router': '10.100.2.2',
                                                        'ospfv2':
                                                            {'body':
                                                                {'summary':
                                                                    {'network_mask': '255.255.255.0',
                                                                    'topologies':
                                                                        {0:
                                                                            {'metric': 222,
                                                                            'mt_id': 0,
                                                                            'tos': 0}}}},
                                                            'header':
                                                                {'adv_router': '10.100.2.2',
                                                                'age': 788,
                                                                'checksum': '0x4601',
                                                                'length': 28,
                                                                'lsa_id': '10.2.3.0',
                                                                'option': '0x22',
                                                                'option_desc': 'No TOS-capability, DC',
                                                               'seq_num': '0x80000001',
                                                               'type': 3}}},
                                                    '10.2.3.0 10.36.3.3':
                                                        {'lsa_id': '10.2.3.0',
                                                        'adv_router': '10.36.3.3',
                                                        'ospfv2':
                                                            {'body':
                                                                {'summary':
                                                                    {'network_mask': '255.255.255.0',
                                                                    'topologies':
                                                                        {0:
                                                                            {'metric': 262,
                                                                            'mt_id': 0,
                                                                            'tos': 0}}}},
                                                            'header':
                                                                {'adv_router': '10.36.3.3',
                                                                'age': 397,
                                                                'checksum': '0x96a2',
                                                                'length': 28,
                                                                'lsa_id': '10.2.3.0',
                                                                'option': '0x2',
                                                                'option_desc': 'No TOS-capability, No DC',
                                                                'seq_num': '0x80000003',
                                                                'type': 3}}},
                                                    '10.100.2.2 10.100.2.2':
                                                        {'lsa_id': '10.100.2.2',
                                                        'adv_router': '10.100.2.2',
                                                        'ospfv2':
                                                            {'body':
                                                                {'summary':
                                                                    {'network_mask': '255.255.255.255',
                                                                    'topologies':
                                                                        {0:
                                                                            {'metric': 1,
                                                                            'mt_id': 0,
                                                                            'tos': 0}}}},
                                                            'header':
                                                                {'adv_router': '10.100.2.2',
                                                                'age': 789,
                                                                'checksum': '0xfa31',
                                                                'length': 28,
                                                                'lsa_id': '10.100.2.2',
                                                                'option': '0x22',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'seq_num': '0x80000001',
                                                                'type': 3}}},
                                                    '10.36.3.3 10.36.3.3':
                                                        {'lsa_id': '10.36.3.3',
                                                        'adv_router': '10.36.3.3',
                                                        'ospfv2':
                                                            {'body':
                                                                {'summary':
                                                                    {'network_mask': '255.255.255.255',
                                                                    'topologies':
                                                                        {0:
                                                                            {'metric': 1,
                                                                            'mt_id': 0,
                                                                            'tos': 0}}}},
                                                            'header':
                                                                {'adv_router': '10.36.3.3',
                                                                'age': 642,
                                                                'checksum': '0x8eb4',
                                                                'length': 28,
                                                                'lsa_id': '10.36.3.3',
                                                                'option': '0x2',
                                                                'option_desc': 'No TOS-capability, No DC',
                                                              'seq_num': '0x80000002',
                                                              'type': 3}}},
                                                    '10.94.44.44 10.64.4.4':
                                                        {'lsa_id': '10.94.44.44',
                                                        'adv_router': '10.64.4.4',
                                                        'ospfv2':
                                                            {'body':
                                                                {'summary':
                                                                    {'network_mask': '255.255.255.255',
                                                                    'topologies':
                                                                        {0:
                                                                            {'metric': 1,
                                                                            'mt_id': 0,
                                                                            'tos': 0}}}},
                                                            'header':
                                                                {'adv_router': '10.64.4.4',
                                                                'age': 403,
                                                                'checksum': '0x2b50',
                                                                'length': 28,
                                                                'lsa_id': '10.94.44.44',
                                                                'option': '0x22',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'seq_num': '0x80000001',
                                                                'type': 3}}}}}}}},
                                '0.0.0.0':
                                    {'database':
                                        {'lsa_types':
                                            {3:
                                                {'lsa_type': 3,
                                                'lsas':
                                                    {'10.186.3.0 10.4.1.1':
                                                        {'lsa_id': '10.186.3.0',
                                                        'adv_router': '10.4.1.1',
                                                        'ospfv2':
                                                            {'body':
                                                                {'summary':
                                                                    {'network_mask': '255.255.255.0',
                                                                    'topologies':
                                                                        {0:
                                                                            {'metric': 1,
                                                                            'mt_id': 0,
                                                                            'tos': 0}}}},
                                                            'header':
                                                                {'adv_router': '10.4.1.1',
                                                                'age': 694,
                                                                'checksum': '0x43dc',
                                                                'length': 28,
                                                                'lsa_id': '10.186.3.0',
                                                                'option': '0x22',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'seq_num': '0x80000001',
                                                                'type': 3}}},
                                                    '10.186.3.0 10.36.3.3':
                                                        {'lsa_id': '10.186.3.0',
                                                        'adv_router': '10.36.3.3',
                                                        'ospfv2':
                                                            {'body':
                                                                {'summary':
                                                                    {'network_mask': '255.255.255.0',
                                                                    'topologies':
                                                                        {0:
                                                                            {'metric': 40,
                                                                            'mt_id': 0,
                                                                            'tos': 0}}}},
                                                            'header':
                                                                {'adv_router': '10.36.3.3',
                                                                'age': 642,
                                                                'checksum': '0x6ea1',
                                                                'length': 28,
                                                                'lsa_id': '10.186.3.0',
                                                                'option': '0x2',
                                                                'option_desc': 'No TOS-capability, No DC',
                                                                'seq_num': '0x80000002',
                                                                'type': 3}}},
                                                    '10.229.3.0 10.36.3.3':
                                                        {'lsa_id': '10.229.3.0',
                                                        'adv_router': '10.36.3.3',
                                                        'ospfv2':
                                                            {'body':
                                                                {'summary':
                                                                    {'network_mask': '255.255.255.0',
                                                                    'topologies':
                                                                        {0:
                                                                            {'metric': 40,
                                                                            'mt_id': 0,
                                                                            'tos': 0}}}},
                                                            'header':
                                                                {'adv_router': '10.36.3.3',
                                                                'age': 642,
                                                                'checksum': '0x62ac',
                                                                'length': 28,
                                                                'lsa_id': '10.229.3.0',
                                                                'option': '0x2',
                                                                'option_desc': 'No TOS-capability, No DC',
                                                                'seq_num': '0x80000002',
                                                                'type': 3}}},
                                                    '10.229.4.0 10.36.3.3':
                                                        {'lsa_id': '10.229.4.0',
                                                        'adv_router': '10.36.3.3',
                                                        'ospfv2':
                                                            {'body':
                                                                {'summary':
                                                                    {'network_mask': '255.255.255.0',
                                                                    'topologies':
                                                                        {0:
                                                                            {'metric': 41,
                                                                            'mt_id': 0,
                                                                            'tos': 0}}}},
                                                            'header':
                                                                {'adv_router': '10.36.3.3',
                                                                'age': 401,
                                                                'checksum': '0x5dad',
                                                                'length': 28,
                                                                'lsa_id': '10.229.4.0',
                                                                'option': '0x2',
                                                                'option_desc': 'No TOS-capability, No DC',
                                                                'seq_num': '0x80000004',
                                                                'type': 3}}},
                                                    '10.19.4.0 10.36.3.3':
                                                        {'lsa_id': '10.19.4.0',
                                                        'adv_router': '10.36.3.3',
                                                        'ospfv2':
                                                            {'body':
                                                                {'summary':
                                                                    {'network_mask': '255.255.255.0',
                                                                    'topologies':
                                                                        {0:
                                                                            {'metric': 40,
                                                                            'mt_id': 0,
                                                                            'tos': 0}}}},
                                                            'header':
                                                                {'adv_router': '10.36.3.3',
                                                                'age': 642,
                                                                'checksum': '0x4bc1',
                                                                'length': 28,
                                                                'lsa_id': '10.19.4.0',
                                                                'option': '0x2',
                                                                'option_desc': 'No TOS-capability, No DC',
                                                                'seq_num': '0x80000002',
                                                                'type': 3}}},
                                                    '10.64.4.4 10.36.3.3':
                                                        {'lsa_id': '10.64.4.4',
                                                        'adv_router': '10.36.3.3',
                                                        'ospfv2':
                                                            {'body':
                                                                {'summary':
                                                                    {'network_mask': '255.255.255.255',
                                                                    'topologies':
                                                                        {0:
                                                                            {'metric': 41,
                                                                            'mt_id': 0,
                                                                            'tos': 0}}}},
                                                            'header':
                                                                {'adv_router': '10.36.3.3',
                                                                'age': 401,
                                                                'checksum': '0xef26',
                                                                'length': 28,
                                                                'lsa_id': '10.64.4.4',
                                                                'option': '0x2',
                                                                'option_desc': 'No TOS-capability, No DC',
                                                                'seq_num': '0x80000003',
                                                                'type': 3}}}}}}}}}}}}}}}}
