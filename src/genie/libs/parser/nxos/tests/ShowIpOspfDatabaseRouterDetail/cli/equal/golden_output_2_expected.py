

expected_output = {
    'vrf':
        {'default':
            {'address_family':
                {'ipv4':
                    {'instance':
                        {'UNDERLAY':
                            {'areas':
                                {'0.0.0.0':
                                    {'database':
                                        {'lsa_types':
                                            {1:
                                                {'lsa_type': 1,
                                                'lsas':
                                                    {'10.186.0.1 10.186.0.1':
                                                        {'adv_router': '10.186.0.1',
                                                        'lsa_id': '10.186.0.1',
                                                        'ospfv2':
                                                            {'body':
                                                                {'router':
                                                                    {'links':
                                                                        {'10.55.1.1':
                                                                            {'link_data': '255.255.255.255',
                                                                            'link_id': '10.55.1.1',
                                                                            'num_tos_metrics': 0,
                                                                            'topologies':
                                                                                {0:
                                                                                    {'metric': 1,
                                                                                    'mt_id': 0,
                                                                                    'tos': 0}},
                                                                            'type': 'stub network'},
                                                                        '10.51.0.1':
                                                                            {'link_data': '255.255.255.255',
                                                                            'link_id': '10.51.0.1',
                                                                            'num_tos_metrics': 0,
                                                                            'topologies':
                                                                                {0:
                                                                                    {'metric': 1,
                                                                                    'mt_id': 0,
                                                                                    'tos': 0}},
                                                                            'type': 'stub network'},
                                                                        '10.186.0.1':
                                                                            {'link_data': '255.255.255.255',
                                                                            'link_id': '10.186.0.1',
                                                                            'num_tos_metrics': 0,
                                                                            'topologies':
                                                                                {0:
                                                                                    {'metric': 1,
                                                                                    'mt_id': 0,
                                                                                    'tos': 0}},
                                                                            'type': 'stub network'},
                                                                        '10.186.0.2':
                                                                            {'link_data': '10.186.1.1',
                                                                            'link_id': '10.186.0.2',
                                                                            'num_tos_metrics': 0,
                                                                            'topologies':
                                                                                {0:
                                                                                    {'metric': 40,
                                                                                    'mt_id': 0,
                                                                                    'tos': 0}},
                                                                            'type': 'router (point-to-point)'},
                                                                        '10.186.0.3':
                                                                            {'link_data': '0.0.0.5',
                                                                            'link_id': '10.186.0.3',
                                                                            'num_tos_metrics': 0,
                                                                            'topologies':
                                                                                {0:
                                                                                    {'metric': 4,
                                                                                    'mt_id': 0,
                                                                                    'tos': 0}},
                                                                            'type': 'router (point-to-point)'},
                                                                        '10.186.0.4':
                                                                            {'link_data': '0.0.0.4',
                                                                            'link_id': '10.186.0.4',
                                                                            'num_tos_metrics': 0,
                                                                            'topologies':
                                                                                {0:
                                                                                    {'metric': 4,
                                                                                    'mt_id': 0,
                                                                                    'tos': 0}},
                                                                            'type': 'router (point-to-point)'},
                                                                        '10.186.1.0':
                                                                            {'link_data': '255.255.255.0',
                                                                            'link_id': '10.186.1.0',
                                                                            'num_tos_metrics': 0,
                                                                            'topologies':
                                                                                {0:
                                                                                    {'metric': 40,
                                                                                    'mt_id': 0,
                                                                                    'tos': 0}},
                                                                            'type': 'stub network'}},
                                                                    'num_of_links': 7}},
                                                            'header':
                                                                {'adv_router': '10.186.0.1',
                                                                'age': 29,
                                                                'checksum': '0x5cf6',
                                                                'length': 108,
                                                                'lsa_id': '10.186.0.1',
                                                                'option': '0x2',
                                                                'option_desc': 'No TOS-capability, No DC',
                                                                'seq_num': '0x80000905',
                                                                'type': 1}}}}}}}}}}}}}}}}
