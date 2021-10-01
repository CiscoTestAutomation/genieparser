

expected_output = {
    'vrf':
        {'default':
            {'address_family':
                {'ipv4':
                    {'instance':
                        {'1':
                            {'areas':
                                {'0.0.0.0':
                                    {'database':
                                        {'lsa_types':
                                            {10:
                                                {'lsa_type': 10,
                                                'lsas':
                                                    {'10.1.0.0 192.168.4.1':
                                                        {'adv_router': '192.168.4.1',
                                                        'lsa_id': '10.1.0.0',
                                                        'ospfv2':
                                                            {'body':
                                                                {'opaque': {}},
                                                            'header':
                                                                {'adv_router': '192.168.4.1',
                                                                'age': 720,
                                                                'checksum': '0x8c2b',
                                                                'fragment_number': 0,
                                                                'length': 28,
                                                                'lsa_id': '10.1.0.0',
                                                                'mpls_te_router_id': '192.168.4.1',
                                                                'num_links': 0,
                                                                'opaque_id': 0,
                                                                'opaque_type': 1,
                                                                'option': '0x2',
                                                                'option_desc': 'No TOS-capability, No DC',
                                                                'seq_num': '0x80000002',
                                                                'type': 10}}},
                                                    '10.1.0.0 192.168.154.1':
                                                        {'adv_router': '192.168.154.1',
                                                        'lsa_id': '10.1.0.0',
                                                        'ospfv2':
                                                            {'body':
                                                                {'opaque': {}},
                                                            'header':
                                                                {'adv_router': '192.168.154.1',
                                                                'age': 720,
                                                                'checksum': '0x8e27',
                                                                'fragment_number': 0,
                                                                'length': 28,
                                                                'lsa_id': '10.1.0.0',
                                                                'mpls_te_router_id': '192.168.154.1',
                                                                'num_links': 0,
                                                                'opaque_id': 0,
                                                                'opaque_type': 1,
                                                                'option': '0x2',
                                                                'option_desc': 'No TOS-capability, No DC',
                                                                'seq_num': '0x80000002',
                                                                'type': 10}}},
                                                    '10.1.0.0 192.168.51.1':
                                                        {'adv_router': '192.168.51.1',
                                                        'lsa_id': '10.1.0.0',
                                                        'ospfv2':
                                                            {'body':
                                                                {'opaque': {}},
                                                            'header':
                                                                {'adv_router': '192.168.51.1',
                                                                'age': 515,
                                                                'checksum': '0x9023',
                                                                'fragment_number': 0,
                                                                'length': 28,
                                                                'lsa_id': '10.1.0.0',
                                                                'mpls_te_router_id': '192.168.51.1',
                                                                'num_links': 0,
                                                                'opaque_id': 0,
                                                                'opaque_type': 1,
                                                                'option': '0x2',
                                                                'option_desc': 'No TOS-capability, No DC',
                                                                'seq_num': '0x80000002',
                                                                'type': 10}}},
                                                    '10.1.0.0 192.168.205.1':
                                                        {'adv_router': '192.168.205.1',
                                                        'lsa_id': '10.1.0.0',
                                                        'ospfv2':
                                                            {'body':
                                                                {'opaque': {}},
                                                            'header':
                                                                {'adv_router': '192.168.205.1',
                                                                'age': 497,
                                                                'checksum': '0x921f',
                                                                'fragment_number': 0,
                                                                'length': 28,
                                                                'lsa_id': '10.1.0.0',
                                                                'mpls_te_router_id': '192.168.205.1',
                                                                'num_links': 0,
                                                                'opaque_id': 0,
                                                                'opaque_type': 1,
                                                                'option': '0x2',
                                                                'option_desc': 'No TOS-capability, No DC',
                                                                'seq_num': '0x80000002',
                                                                'type': 10}}},
                                                    '10.1.0.233 192.168.51.1':
                                                        {'adv_router': '192.168.51.1',
                                                        'lsa_id': '10.1.0.233',
                                                        'ospfv2':
                                                            {'body':
                                                                {'opaque':
                                                                    {'link_tlvs':
                                                                        {1:
                                                                            {'admin_group': '0x0',
                                                                            'link_id': '192.168.145.2',
                                                                            'link_name': 'broadcast network',
                                                                            'link_type': 2,
                                                                            'local_if_ipv4_addrs':
                                                                                {'192.168.145.2': {}},
                                                                            'max_bandwidth': 5000000000,
                                                                            'max_reservable_bandwidth': 3749999872,
                                                                            'remote_if_ipv4_addrs':
                                                                                {'0.0.0.0': {}},
                                                                            'te_metric': 1,
                                                                            'unreserved_bandwidths':
                                                                                {'0 3749999872':
                                                                                    {'priority': 0,
                                                                                    'unreserved_bandwidth': 3749999872},
                                                                                '1 3749999872':
                                                                                    {'priority': 1,
                                                                                    'unreserved_bandwidth': 3749999872},
                                                                                '2 3749999872':
                                                                                    {'priority': 2,
                                                                                    'unreserved_bandwidth': 3749999872},
                                                                                '3 3749999872':
                                                                                    {'priority': 3,
                                                                                    'unreserved_bandwidth': 3749999872},
                                                                                '4 3749999872':
                                                                                    {'priority': 4,
                                                                                    'unreserved_bandwidth': 3749999872},
                                                                                '5 3749999872':
                                                                                    {'priority': 5,
                                                                                    'unreserved_bandwidth': 3749999872},
                                                                                '6 3749999872':
                                                                                    {'priority': 6,
                                                                                    'unreserved_bandwidth': 3749999872},
                                                                                '7 3749999872':
                                                                                    {'priority': 7,
                                                                                    'unreserved_bandwidth': 3749999872}}}}}},
                                                            'header':
                                                                {'adv_router': '192.168.51.1',
                                                                'age': 475,
                                                                'checksum': '0x9a3b',
                                                                'fragment_number': 233,
                                                                'length': 116,
                                                                'lsa_id': '10.1.0.233',
                                                                'num_links': 1,
                                                                'opaque_id': 233,
                                                                'opaque_type': 1,
                                                                'option': '0x2',
                                                                'option_desc': 'No TOS-capability, No DC',
                                                                'seq_num': '0x80000002',
                                                                'type': 10}}},
                                                    '10.1.0.237 192.168.51.1':
                                                        {'adv_router': '192.168.51.1',
                                                        'lsa_id': '10.1.0.237',
                                                        'ospfv2':
                                                            {'body':
                                                                {'opaque':
                                                                    {'link_tlvs':
                                                                        {1:
                                                                            {'admin_group': '0x0',
                                                                            'link_id': '192.168.81.2',
                                                                            'link_name': 'broadcast network',
                                                                            'link_type': 2,
                                                                            'local_if_ipv4_addrs':
                                                                                {'192.168.81.1': {}},
                                                                            'max_bandwidth': 5000000000,
                                                                            'max_reservable_bandwidth': 3749999872,
                                                                            'remote_if_ipv4_addrs':
                                                                                {'0.0.0.0': {}},
                                                                            'te_metric': 1,
                                                                            'unreserved_bandwidths':
                                                                                {'0 3749999872':
                                                                                    {'priority': 0,
                                                                                    'unreserved_bandwidth': 3749999872},
                                                                                '1 3749999872':
                                                                                    {'priority': 1,
                                                                                    'unreserved_bandwidth': 3749999872},
                                                                                '2 3749999872':
                                                                                    {'priority': 2,
                                                                                    'unreserved_bandwidth': 3749999872},
                                                                                '3 3749999872':
                                                                                    {'priority': 3,
                                                                                    'unreserved_bandwidth': 3749999872},
                                                                                '4 3749999872':
                                                                                    {'priority': 4,
                                                                                    'unreserved_bandwidth': 3749999872},
                                                                                '5 3749999872':
                                                                                    {'priority': 5,
                                                                                    'unreserved_bandwidth': 3749999872},
                                                                                '6 3749999872':
                                                                                    {'priority': 6,
                                                                                    'unreserved_bandwidth': 3749999872},
                                                                                '7 3749999872':
                                                                                    {'priority': 7,
                                                                                    'unreserved_bandwidth': 3749999872}}}}}},
                                                            'header':
                                                                {'adv_router': '192.168.51.1',
                                                                'age': 455,
                                                                'checksum': '0x7c40',
                                                                'fragment_number': 237,
                                                                'length': 116,
                                                                'lsa_id': '10.1.0.237',
                                                                'num_links': 1,
                                                                'opaque_id': 237,
                                                                'opaque_type': 1,
                                                                'option': '0x2',
                                                                'option_desc': 'No TOS-capability, No DC',
                                                                'seq_num': '0x80000002',
                                                                'type': 10}}},
                                                    '10.1.0.42 192.168.154.1':
                                                        {'adv_router': '192.168.154.1',
                                                        'lsa_id': '10.1.0.42',
                                                        'ospfv2':
                                                            {'body':
                                                                {'opaque':
                                                                    {'link_tlvs':
                                                                        {1:
                                                                            {'admin_group': '0x0',
                                                                            'link_id': '192.168.196.2',
                                                                            'link_name': 'broadcast network',
                                                                            'link_type': 2,
                                                                            'local_if_ipv4_addrs':
                                                                                {'192.168.196.2': {}},
                                                                            'max_bandwidth': 2500000000,
                                                                            'max_reservable_bandwidth': 1874999936,
                                                                            'remote_if_ipv4_addrs':
                                                                                {'0.0.0.0': {}},
                                                                            'te_metric': 2,
                                                                            'unreserved_bandwidths':
                                                                                {'0 1874999936':
                                                                                    {'priority': 0,
                                                                                    'unreserved_bandwidth': 1874999936},
                                                                                '1 1874999936':
                                                                                    {'priority': 1,
                                                                                    'unreserved_bandwidth': 1874999936},
                                                                                '2 1874999936':
                                                                                    {'priority': 2,
                                                                                    'unreserved_bandwidth': 1874999936},
                                                                                '3 1874999936':
                                                                                    {'priority': 3,
                                                                                    'unreserved_bandwidth': 1874999936},
                                                                                '4 1874999936':
                                                                                    {'priority': 4,
                                                                                    'unreserved_bandwidth': 1874999936},
                                                                                '5 1874999936':
                                                                                    {'priority': 5,
                                                                                    'unreserved_bandwidth': 1874999936},
                                                                                '6 1874999936':
                                                                                    {'priority': 6,
                                                                                    'unreserved_bandwidth': 1874999936},
                                                                                '7 1874999936':
                                                                                    {'priority': 7,
                                                                                    'unreserved_bandwidth': 1874999936}}}}}},
                                                            'header':
                                                                {'adv_router': '192.168.154.1',
                                                                'age': 510,
                                                                'checksum': '0xcce3',
                                                                'fragment_number': 42,
                                                                'length': 116,
                                                                'lsa_id': '10.1.0.42',
                                                                'num_links': 1,
                                                                'opaque_id': 42,
                                                                'opaque_type': 1,
                                                                'option': '0x2',
                                                                'option_desc': 'No TOS-capability, No DC',
                                                                'seq_num': '0x80000002',
                                                                'type': 10}}},
                                                    '10.1.0.47 192.168.154.1':
                                                        {'adv_router': '192.168.154.1',
                                                        'lsa_id': '10.1.0.47',
                                                        'ospfv2':
                                                            {'body':
                                                                {'opaque':
                                                                    {'link_tlvs':
                                                                        {1:
                                                                            {'admin_group': '0x0',
                                                                            'link_id': '192.168.145.2',
                                                                            'link_name': 'broadcast '
                                                                            'network',
                                                                            'link_type': 2,
                                                                            'local_if_ipv4_addrs':
                                                                                {'192.168.145.1': {}},
                                                                            'max_bandwidth': 5000000000,
                                                                            'max_reservable_bandwidth': 3749999872,
                                                                            'remote_if_ipv4_addrs':
                                                                                {'0.0.0.0': {}},
                                                                            'te_metric': 1,
                                                                            'unreserved_bandwidths':
                                                                                {'0 3749999872':
                                                                                    {'priority': 0,
                                                                                    'unreserved_bandwidth': 3749999872},
                                                                                '1 3749999872':
                                                                                    {'priority': 1,
                                                                                    'unreserved_bandwidth': 3749999872},
                                                                                '2 3749999872':
                                                                                    {'priority': 2,
                                                                                    'unreserved_bandwidth': 3749999872},
                                                                                '3 3749999872':
                                                                                    {'priority': 3,
                                                                                    'unreserved_bandwidth': 3749999872},
                                                                                '4 3749999872':
                                                                                    {'priority': 4,
                                                                                    'unreserved_bandwidth': 3749999872},
                                                                                '5 3749999872':
                                                                                    {'priority': 5,
                                                                                    'unreserved_bandwidth': 3749999872},
                                                                                '6 3749999872':
                                                                                    {'priority': 6,
                                                                                    'unreserved_bandwidth': 3749999872},
                                                                                '7 3749999872':
                                                                                    {'priority': 7,
                                                                                    'unreserved_bandwidth': 3749999872}}}}}},
                                                            'header':
                                                                {'adv_router': '192.168.154.1',
                                                                'age': 470,
                                                                'checksum': '0xcec3',
                                                                'fragment_number': 47,
                                                                'length': 116,
                                                                'lsa_id': '10.1.0.47',
                                                                'num_links': 1,
                                                                'opaque_id': 47,
                                                                'opaque_type': 1,
                                                                'option': '0x2',
                                                                'option_desc': 'No TOS-capability, No DC',
                                                                'seq_num': '0x80000002',
                                                                'type': 10}}},
                                                    '10.1.0.51 192.168.154.1':
                                                        {'adv_router': '192.168.154.1',
                                                        'lsa_id': '10.1.0.51',
                                                        'ospfv2':
                                                            {'body':
                                                                {'opaque':
                                                                    {'link_tlvs':
                                                                        {1:
                                                                            {'admin_group': '0x0',
                                                                            'link_id': '192.168.106.2',
                                                                            'link_name': 'broadcast network',
                                                                            'link_type': 2,
                                                                            'local_if_ipv4_addrs':
                                                                                {'192.168.106.1': {}},
                                                                            'max_bandwidth': 5000000000,
                                                                            'max_reservable_bandwidth': 3749999872,
                                                                            'remote_if_ipv4_addrs':
                                                                                {'0.0.0.0': {}},
                                                                            'te_metric': 1,
                                                                            'unreserved_bandwidths':
                                                                                {'0 3749999872':
                                                                                    {'priority': 0,
                                                                                    'unreserved_bandwidth': 3749999872},
                                                                                '1 3749999872':
                                                                                    {'priority': 1,
                                                                                    'unreserved_bandwidth': 3749999872},
                                                                                '2 3749999872':
                                                                                    {'priority': 2,
                                                                                    'unreserved_bandwidth': 3749999872},
                                                                                '3 3749999872':
                                                                                    {'priority': 3,
                                                                                    'unreserved_bandwidth': 3749999872},
                                                                                '4 3749999872':
                                                                                    {'priority': 4,
                                                                                    'unreserved_bandwidth': 3749999872},
                                                                                '5 3749999872':
                                                                                    {'priority': 5,
                                                                                    'unreserved_bandwidth': 3749999872},
                                                                                '6 3749999872':
                                                                                    {'priority': 6,
                                                                                    'unreserved_bandwidth': 3749999872},
                                                                                '7 3749999872':
                                                                                    {'priority': 7,
                                                                                    'unreserved_bandwidth': 3749999872}}}}}},
                                                            'header':
                                                                {'adv_router': '192.168.154.1',
                                                                'age': 450,
                                                                'checksum': '0xd8b3',
                                                                'fragment_number': 51,
                                                                'length': 116,
                                                                'lsa_id': '10.1.0.51',
                                                                'num_links': 1,
                                                                'opaque_id': 51,
                                                                'opaque_type': 1,
                                                                'option': '0x2',
                                                                'option_desc': 'No TOS-capability, No DC',
                                                                'seq_num': '0x80000002',
                                                                'type': 10}}},
                                                    '10.1.0.55 192.168.4.1':
                                                        {'adv_router': '192.168.4.1',
                                                        'lsa_id': '10.1.0.55',
                                                        'ospfv2':
                                                            {'body':
                                                                {'opaque':
                                                                    {'link_tlvs':
                                                                        {1:
                                                                            {'admin_group': '0x0',
                                                                            'link_id': '192.168.196.2',
                                                                            'link_name': 'broadcast network',
                                                                            'link_type': 2,
                                                                            'local_if_ipv4_addrs':
                                                                                {'192.168.196.1': {}},
                                                                            'max_bandwidth': 2500000000,
                                                                            'max_reservable_bandwidth': 1874999936,
                                                                            'remote_if_ipv4_addrs':
                                                                                {'0.0.0.0': {}},
                                                                            'te_metric': 2,
                                                                            'unreserved_bandwidths':
                                                                                {'0 1874999936':
                                                                                    {'priority': 0,
                                                                                    'unreserved_bandwidth': 1874999936},
                                                                                '1 1874999936':
                                                                                    {'priority': 1,
                                                                                    'unreserved_bandwidth': 1874999936},
                                                                                '2 1874999936':
                                                                                    {'priority': 2,
                                                                                    'unreserved_bandwidth': 1874999936},
                                                                                '3 1874999936':
                                                                                    {'priority': 3,
                                                                                    'unreserved_bandwidth': 1874999936},
                                                                                '4 1874999936':
                                                                                    {'priority': 4,
                                                                                    'unreserved_bandwidth': 1874999936},
                                                                                '5 1874999936':
                                                                                    {'priority': 5,
                                                                                    'unreserved_bandwidth': 1874999936},
                                                                                '6 1874999936':
                                                                                    {'priority': 6,
                                                                                    'unreserved_bandwidth': 1874999936},
                                                                                '7 1874999936':
                                                                                    {'priority': 7,
                                                                                    'unreserved_bandwidth': 1874999936}}}}}},
                                                        'header':
                                                            {'adv_router': '192.168.4.1',
                                                            'age': 510,
                                                            'checksum': '0x3372',
                                                            'fragment_number': 55,
                                                            'length': 116,
                                                            'lsa_id': '10.1.0.55',
                                                            'num_links': 1,
                                                            'opaque_id': 55,
                                                            'opaque_type': 1,
                                                            'option': '0x2',
                                                            'option_desc': 'No TOS-capability, No DC',
                                                            'seq_num': '0x80000002',
                                                            'type': 10}}},
                                                    '10.1.1.11 192.168.205.1':
                                                        {'adv_router': '192.168.205.1',
                                                        'lsa_id': '10.1.1.11',
                                                        'ospfv2':
                                                            {'body':
                                                                {'opaque':
                                                                    {'link_tlvs':
                                                                        {1:
                                                                            {'admin_group': '0x0',
                                                                            'link_id': '192.168.81.2',
                                                                            'link_name': 'broadcast '
                                                                            'network',
                                                                            'link_type': 2,
                                                                            'local_if_ipv4_addrs':
                                                                                {'192.168.81.2': {}},
                                                                            'max_bandwidth': 5000000000,
                                                                            'max_reservable_bandwidth': 3749999872,
                                                                            'remote_if_ipv4_addrs':
                                                                                {'0.0.0.0': {}},
                                                                            'te_metric': 1,
                                                                            'unreserved_bandwidths':
                                                                                {'0 3749999872':
                                                                                    {'priority': 0,
                                                                                    'unreserved_bandwidth': 3749999872},
                                                                                '1 3749999872':
                                                                                    {'priority': 1,
                                                                                    'unreserved_bandwidth': 3749999872},
                                                                                '2 3749999872':
                                                                                    {'priority': 2,
                                                                                    'unreserved_bandwidth': 3749999872},
                                                                                '3 3749999872':
                                                                                    {'priority': 3,
                                                                                    'unreserved_bandwidth': 3749999872},
                                                                                '4 3749999872':
                                                                                    {'priority': 4,
                                                                                    'unreserved_bandwidth': 3749999872},
                                                                                '5 3749999872':
                                                                                    {'priority': 5,
                                                                                    'unreserved_bandwidth': 3749999872},
                                                                                '6 3749999872':
                                                                                    {'priority': 6,
                                                                                    'unreserved_bandwidth': 3749999872},
                                                                                '7 3749999872':
                                                                                    {'priority': 7,
                                                                                    'unreserved_bandwidth': 3749999872}}}}}},
                                                            'header':
                                                                {'adv_router': '192.168.205.1',
                                                                'age': 447,
                                                                'checksum': '0x6537',
                                                                'fragment_number': 267,
                                                                'length': 116,
                                                                'lsa_id': '10.1.1.11',
                                                                'num_links': 1,
                                                                'opaque_id': 267,
                                                                'opaque_type': 1,
                                                                'option': '0x2',
                                                                'option_desc': 'No TOS-capability, No DC',
                                                                'seq_num': '0x80000002',
                                                                'type': 10}}},
                                                    '10.1.1.15 192.168.205.1':
                                                        {'adv_router': '192.168.205.1',
                                                        'lsa_id': '10.1.1.15',
                                                        'ospfv2':
                                                            {'body':
                                                                {'opaque':
                                                                    {'link_tlvs':
                                                                        {1: {'admin_group': '0x0',
                                                                        'link_id': '192.168.106.2',
                                                                        'link_name': 'broadcast '
                                                                        'network',
                                                                        'link_type': 2,
                                                                        'local_if_ipv4_addrs':
                                                                            {'192.168.106.2': {}},
                                                                        'max_bandwidth': 5000000000,
                                                                        'max_reservable_bandwidth': 3749999872,
                                                                        'remote_if_ipv4_addrs':
                                                                            {'0.0.0.0': {}},
                                                                        'te_metric': 1,
                                                                        'unreserved_bandwidths':
                                                                            {'0 3749999872':
                                                                                {'priority': 0,
                                                                                'unreserved_bandwidth': 3749999872},
                                                                            '1 3749999872':
                                                                                {'priority': 1,
                                                                                'unreserved_bandwidth': 3749999872},
                                                                            '2 3749999872':
                                                                                {'priority': 2,
                                                                                'unreserved_bandwidth': 3749999872},
                                                                            '3 3749999872':
                                                                                {'priority': 3,
                                                                                'unreserved_bandwidth': 3749999872},
                                                                            '4 3749999872':
                                                                                {'priority': 4,
                                                                                'unreserved_bandwidth': 3749999872},
                                                                            '5 3749999872':
                                                                                {'priority': 5,
                                                                                'unreserved_bandwidth': 3749999872},
                                                                            '6 3749999872':
                                                                                {'priority': 6,
                                                                                'unreserved_bandwidth': 3749999872},
                                                                            '7 3749999872':
                                                                                {'priority': 7,
                                                                                'unreserved_bandwidth': 3749999872}}}}}},
                                                            'header':
                                                                {'adv_router': '192.168.205.1',
                                                                'age': 457,
                                                                'checksum': '0x4765',
                                                                'fragment_number': 271,
                                                                'length': 116,
                                                                'lsa_id': '10.1.1.15',
                                                                'num_links': 1,
                                                                'opaque_id': 271,
                                                                'opaque_type': 1,
                                                                'option': '0x2',
                                                                'option_desc': 'No TOS-capability, No DC',
                                                                'seq_num': '0x80000002',
                                                                'type': 10}}}}}}}}}},
                        '2': {}}}}}}}
