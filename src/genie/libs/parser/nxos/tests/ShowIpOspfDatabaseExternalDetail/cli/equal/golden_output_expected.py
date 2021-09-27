

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
                                            {5:
                                                {'lsa_type': 5,
                                                'lsas':
                                                    {'10.94.44.44 10.64.4.4':
                                                        {'lsa_id': '10.94.44.44',
                                                        'adv_router': '10.64.4.4',
                                                        'ospfv2':
                                                            {'body':
                                                                {'external':
                                                                    {'network_mask': '255.255.255.255',
                                                                    'topologies':
                                                                        {0:
                                                                            {'external_route_tag': 0,
                                                                            'flags': 'E',
                                                                            'forwarding_address': '0.0.0.0',
                                                                            'metric': 20,
                                                                            'mt_id': 0,
                                                                            'tos': 0}}}},
                                                            'header':
                                                                {'adv_router': '10.64.4.4',
                                                                'age': 1565,
                                                                'checksum': '0x7d61',
                                                                'length': 36,
                                                                'lsa_id': '10.94.44.44',
                                                                'option': '0x20',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'seq_num': '0x80000002',
                                                                'type': 5}}}}}}}}}}}}}}}}
