

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
                                                    {'10.1.0.0 10.4.1.1':
                                                        {'adv_router': '10.4.1.1',
                                                        'lsa_id': '10.1.0.0',
                                                        'ospfv2':
                                                            {'body':
                                                                {'opaque': {}},
                                                            'header':
                                                                {'adv_router': '10.4.1.1',
                                                                'age': 385,
                                                                'checksum': '0x54d3',
                                                                'fragment_number': 0,
                                                                'length': 28,
                                                                'lsa_id': '10.1.0.0',
                                                                'mpls_te_router_id': '10.4.1.1',
                                                                'num_links': 0,
                                                                'opaque_id': 0,
                                                                'opaque_type': 1,
                                                                'option': '0x20',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'seq_num': '0x80000003',
                                                                'type': 10}}},
                                                    '10.1.0.0 10.100.2.2':
                                                        {'adv_router': '10.100.2.2',
                                                        'lsa_id': '10.1.0.0',
                                                        'ospfv2':
                                                            {'body':
                                                                {'opaque': {}},
                                                        'header':
                                                            {'adv_router': '10.100.2.2',
                                                            'age': 1612,
                                                            'checksum': '0x1c22',
                                                            'fragment_number': 0,
                                                            'length': 28,
                                                            'lsa_id': '10.1.0.0',
                                                            'mpls_te_router_id': '10.100.2.2',
                                                            'num_links': 0,
                                                            'opaque_id': 0,
                                                            'opaque_type': 1,
                                                            'option': '0x2',
                                                            'option_desc': 'No TOS-capability, No DC',
                                                            'seq_num': '0x80000003',
                                                            'type': 10}}},
                                                    '10.1.0.0 10.36.3.3':
                                                        {'adv_router': '10.36.3.3',
                                                        'lsa_id': '10.1.0.0',
                                                        'ospfv2':
                                                            {'body':
                                                                {'opaque': {}},
                                                        'header':
                                                            {'adv_router': '10.36.3.3',
                                                            'age': 113,
                                                            'checksum': '0x5cbb',
                                                            'fragment_number': 0,
                                                            'length': 28,
                                                            'lsa_id': '10.1.0.0',
                                                            'mpls_te_router_id': '10.36.3.3',
                                                            'num_links': 0,
                                                            'opaque_id': 0,
                                                            'opaque_type': 1,
                                                            'option': '0x20',
                                                            'option_desc': 'No TOS-capability, DC',
                                                            'seq_num': '0x80000003',
                                                            'type': 10}}},
                                                    '10.1.0.1 10.4.1.1':
                                                        {'adv_router': '10.4.1.1',
                                                        'lsa_id': '10.1.0.1',
                                                        'ospfv2':
                                                            {'body':
                                                                {'opaque':
                                                                    {'link_tlvs':
                                                                        {1:
                                                                            {'admin_group': '0x0',
                                                                            'link_id': '10.1.4.4',
                                                                            'link_name': 'broadcast network',
                                                                            'link_type': 2,
                                                                            'local_if_ipv4_addrs':
                                                                                {'10.1.4.1': {}},
                                                                            'max_bandwidth': 125000000,
                                                                            'max_reservable_bandwidth': 93750000,
                                                                            'remote_if_ipv4_addrs':
                                                                                {'0.0.0.0': {}},
                                                                            'te_metric': 1,
                                                                            'unknown_tlvs':
                                                                                {1:
                                                                                    {'length': 4,
                                                                                    'type': 32770,
                                                                                    'value': '00 00 00 01'}},
                                                                            'unreserved_bandwidths':
                                                                                {'0 93750000':
                                                                                    {'priority': 0,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '1 93750000':
                                                                                    {'priority': 1,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '2 93750000':
                                                                                    {'priority': 2,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '3 93750000':
                                                                                    {'priority': 3,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '4 93750000':
                                                                                    {'priority': 4,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '5 93750000':
                                                                                    {'priority': 5,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '6 93750000':
                                                                                    {'priority': 6,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '7 93750000':
                                                                                    {'priority': 7,
                                                                                    'unreserved_bandwidth': 93750000}}}}}},
                                                            'header':
                                                                {'adv_router': '10.4.1.1',
                                                                'age': 385,
                                                                'checksum': '0x6387',
                                                                'fragment_number': 1,
                                                                'length': 124,
                                                                'lsa_id': '10.1.0.1',
                                                                'num_links': 1,
                                                                'opaque_id': 1,
                                                                'opaque_type': 1,
                                                                'option': '0x20',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'seq_num': '0x80000003',
                                                                'type': 10}}},
                                                    '10.1.0.2 10.4.1.1':
                                                        {'adv_router': '10.4.1.1',
                                                        'lsa_id': '10.1.0.2',
                                                        'ospfv2':
                                                            {'body':
                                                                {'opaque':
                                                                    {'link_tlvs':
                                                                        {1:
                                                                            {'admin_group': '0x0',
                                                                            'link_id': '10.1.2.1',
                                                                            'link_name': 'broadcast network',
                                                                            'link_type': 2,
                                                                            'local_if_ipv4_addrs': {'10.1.2.1': {}},
                                                                            'max_bandwidth': 125000000,
                                                                            'max_reservable_bandwidth': 93750000,
                                                                            'remote_if_ipv4_addrs':
                                                                                {'0.0.0.0': {}},
                                                                            'te_metric': 1,
                                                                            'unknown_tlvs':
                                                                                {1:
                                                                                    {'length': 4,
                                                                                    'type': 32770,
                                                                                    'value': '00 00 00 01'}},
                                                                            'unreserved_bandwidths':
                                                                                {'0 93750000':
                                                                                    {'priority': 0,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '1 93750000':
                                                                                    {'priority': 1,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '2 93750000':
                                                                                    {'priority': 2,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '3 93750000':
                                                                                    {'priority': 3,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '4 93750000':
                                                                                    {'priority': 4,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '5 93750000':
                                                                                    {'priority': 5,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '6 93750000':
                                                                                    {'priority': 6,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '7 93750000':
                                                                                    {'priority': 7,
                                                                                    'unreserved_bandwidth': 93750000}}}}}},
                                                            'header':
                                                                {'adv_router': '10.4.1.1',
                                                                'age': 385,
                                                                'checksum': '0xb23e',
                                                                'fragment_number': 2,
                                                                'length': 124,
                                                                'lsa_id': '10.1.0.2',
                                                                'num_links': 1,
                                                                'opaque_id': 2,
                                                                'opaque_type': 1,
                                                                'option': '0x20',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'seq_num': '0x80000003',
                                                                'type': 10}}},
                                                    '10.1.0.37 10.100.2.2':
                                                        {'adv_router': '10.100.2.2',
                                                        'lsa_id': '10.1.0.37',
                                                        'ospfv2':
                                                            {'body':
                                                                {'opaque':
                                                                    {'link_tlvs':
                                                                        {1:
                                                                            {'admin_group': '0x0',
                                                                            'link_id': '10.2.3.3',
                                                                            'link_name': 'broadcast network',
                                                                            'link_type': 2,
                                                                            'local_if_ipv4_addrs':
                                                                                {'10.2.3.2': {}},
                                                                            'max_bandwidth': 125000000,
                                                                            'max_reservable_bandwidth': 93750000,
                                                                            'remote_if_ipv4_addrs':
                                                                                {'0.0.0.0': {}},
                                                                            'te_metric': 1,
                                                                            'unreserved_bandwidths':
                                                                                {'0 93750000':
                                                                                    {'priority': 0,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '1 93750000':
                                                                                    {'priority': 1,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '2 93750000':
                                                                                    {'priority': 2,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '3 93750000':
                                                                                    {'priority': 3,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '4 93750000':
                                                                                    {'priority': 4,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '5 93750000':
                                                                                    {'priority': 5,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '6 93750000':
                                                                                    {'priority': 6,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '7 93750000':
                                                                                    {'priority': 7,
                                                                                    'unreserved_bandwidth': 93750000}}}}}},
                                                            'header':
                                                                {'adv_router': '10.100.2.2',
                                                                'age': 1202,
                                                                'checksum': '0xe492',
                                                                'fragment_number': 37,
                                                                'length': 116,
                                                                'lsa_id': '10.1.0.37',
                                                                'num_links': 1,
                                                                'opaque_id': 37,
                                                                'opaque_type': 1,
                                                                'option': '0x2',
                                                                'option_desc': 'No TOS-capability, No DC',
                                                                'seq_num': '0x80000004',
                                                                'type': 10}}},
                                                    '10.1.0.38 10.100.2.2':
                                                        {'adv_router': '10.100.2.2',
                                                        'lsa_id': '10.1.0.38',
                                                        'ospfv2':
                                                            {'body':
                                                                {'opaque':
                                                                    {'link_tlvs':
                                                                        {1:
                                                                            {'admin_group': '0x0',
                                                                            'link_id': '10.2.4.4',
                                                                            'link_name': 'broadcast network',
                                                                            'link_type': 2,
                                                                            'local_if_ipv4_addrs':
                                                                                {'10.2.4.2': {}},
                                                                            'max_bandwidth': 125000000,
                                                                            'max_reservable_bandwidth': 93750000,
                                                                            'remote_if_ipv4_addrs':
                                                                                {'0.0.0.0': {}},
                                                                            'te_metric': 1,
                                                                            'unreserved_bandwidths':
                                                                                {'0 93750000':
                                                                                    {'priority': 0,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '1 93750000':
                                                                                    {'priority': 1,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '2 93750000':
                                                                                    {'priority': 2,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '3 93750000':
                                                                                    {'priority': 3,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '4 93750000':
                                                                                    {'priority': 4,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '5 93750000':
                                                                                    {'priority': 5,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '6 93750000':
                                                                                    {'priority': 6,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '7 93750000':
                                                                                    {'priority': 7,
                                                                                    'unreserved_bandwidth': 93750000}}}}}},
                                                            'header':
                                                                {'adv_router': '10.100.2.2',
                                                                'age': 1191,
                                                                'checksum': '0x2350',
                                                                'fragment_number': 38,
                                                                'length': 116,
                                                                'lsa_id': '10.1.0.38',
                                                                'num_links': 1,
                                                                'opaque_id': 38,
                                                                'opaque_type': 1,
                                                                'option': '0x2',
                                                                'option_desc': 'No TOS-capability, No DC',
                                                                'seq_num': '0x80000004',
                                                                'type': 10}}},
                                                    '10.1.0.39 10.100.2.2':
                                                        {'adv_router': '10.100.2.2',
                                                        'lsa_id': '10.1.0.39',
                                                        'ospfv2':
                                                            {'body':
                                                                {'opaque':
                                                                    {'link_tlvs':
                                                                        {1:
                                                                            {'admin_group': '0x0',
                                                                            'link_id': '10.1.2.1',
                                                                            'link_name': 'broadcast network',
                                                                            'link_type': 2,
                                                                            'local_if_ipv4_addrs':
                                                                                {'10.1.2.2': {}},
                                                                            'max_bandwidth': 125000000,
                                                                            'max_reservable_bandwidth': 93750000,
                                                                            'remote_if_ipv4_addrs':
                                                                                {'0.0.0.0': {}},
                                                                            'te_metric': 1,
                                                                            'unreserved_bandwidths':
                                                                                {'0 93750000':
                                                                                    {'priority': 0,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '1 93750000':
                                                                                    {'priority': 1,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '2 93750000':
                                                                                    {'priority': 2,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '3 93750000':
                                                                                    {'priority': 3,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '4 93750000':
                                                                                    {'priority': 4,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '5 93750000':
                                                                                    {'priority': 5,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '6 93750000':
                                                                                    {'priority': 6,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '7 93750000':
                                                                                    {'priority': 7,
                                                                                    'unreserved_bandwidth': 93750000}}}}}},
                                                            'header':
                                                                {'adv_router': '10.100.2.2',
                                                                'age': 1191,
                                                                'checksum': '0x4239',
                                                                'fragment_number': 39,
                                                                'length': 116,
                                                                'lsa_id': '10.1.0.39',
                                                                'num_links': 1,
                                                                'opaque_id': 39,
                                                                'opaque_type': 1,
                                                                'option': '0x2',
                                                                'option_desc': 'No TOS-capability, No DC',
                                                                'seq_num': '0x80000004',
                                                                'type': 10}}},
                                                    '10.1.0.4 10.36.3.3':
                                                        {'adv_router': '10.36.3.3',
                                                        'lsa_id': '10.1.0.4',
                                                        'ospfv2':
                                                            {'body':
                                                                {'opaque':
                                                                    {'link_tlvs':
                                                                        {1:
                                                                            {'admin_group': '0x0',
                                                                            'link_id': '10.3.4.4',
                                                                            'link_name': 'broadcast network',
                                                                            'link_type': 2,
                                                                            'local_if_ipv4_addrs':
                                                                                {'10.3.4.3': {}},
                                                                            'max_bandwidth': 125000000,
                                                                            'max_reservable_bandwidth': 93750000,
                                                                            'remote_if_ipv4_addrs':
                                                                                {'0.0.0.0': {}},
                                                                            'te_metric': 1,
                                                                            'unknown_tlvs':
                                                                                {1:
                                                                                    {'length': 4,
                                                                                    'type': 32770,
                                                                                    'value': '00 00 00 01'},
                                                                                2: {'length': 32,
                                                                                    'type': 32771,
                                                                                    'value': '00 00 00 00 00 0 0 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'}},
                                                                            'unreserved_bandwidths':
                                                                                {'0 93750000':
                                                                                    {'priority': 0,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '1 93750000':
                                                                                    {'priority': 1,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '2 93750000':
                                                                                    {'priority': 2,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '3 93750000':
                                                                                    {'priority': 3,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '4 93750000':
                                                                                    {'priority': 4,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '5 93750000':
                                                                                    {'priority': 5,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '6 93750000':
                                                                                    {'priority': 6,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '7 93750000':
                                                                                    {'priority': 7,
                                                                                    'unreserved_bandwidth': 93750000}}}}}},
                                                            'header':
                                                                {'adv_router': '10.36.3.3',
                                                                'age': 113,
                                                                'checksum': '0x8f5e',
                                                                'fragment_number': 4,
                                                                'length': 160,
                                                                'lsa_id': '10.1.0.4',
                                                                'num_links': 1,
                                                                'opaque_id': 4,
                                                                'opaque_type': 1,
                                                                'option': '0x20',
                                                                'option_desc': 'No TOS-capability, DC',
                                                                'seq_num': '0x80000003',
                                                                'type': 10}}},
                                                    '10.1.0.6 10.36.3.3':
                                                        {'adv_router': '10.36.3.3',
                                                        'lsa_id': '10.1.0.6',
                                                        'ospfv2':
                                                            {'body':
                                                                {'opaque':
                                                                    {'link_tlvs':
                                                                        {1:
                                                                            {'admin_group': '0x0',
                                                                            'link_id': '10.2.3.3',
                                                                            'link_name': 'broadcast network',
                                                                            'link_type': 2,
                                                                            'local_if_ipv4_addrs':
                                                                                {'10.2.3.3': {}},
                                                                            'max_bandwidth': 125000000,
                                                                            'max_reservable_bandwidth': 93750000,
                                                                            'remote_if_ipv4_addrs':
                                                                                {'0.0.0.0': {}},
                                                                            'te_metric': 1,
                                                                            'unknown_tlvs':
                                                                                {1:
                                                                                    {'length': 4,
                                                                                    'type': 32770,
                                                                                    'value': '00 00 00 01'},
                                                                                2: {'length': 32,
                                                                                    'type': 32771,
                                                                                    'value': '00 00 00 00 00 0 0 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00 00'}},
                                                                            'unreserved_bandwidths':
                                                                                {'0 93750000':
                                                                                    {'priority': 0,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '1 93750000':
                                                                                    {'priority': 1,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '2 93750000':
                                                                                    {'priority': 2,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '3 93750000':
                                                                                    {'priority': 3,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '4 93750000':
                                                                                    {'priority': 4,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '5 93750000':
                                                                                    {'priority': 5,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '6 93750000':
                                                                                    {'priority': 6,
                                                                                    'unreserved_bandwidth': 93750000},
                                                                                '7 93750000':
                                                                                    {'priority': 7,
                                                                                    'unreserved_bandwidth': 93750000}}}}}},
                                                        'header':
                                                            {'adv_router': '10.36.3.3',
                                                            'age': 113,
                                                            'checksum': '0x03ed',
                                                            'fragment_number': 6,
                                                            'length': 160,
                                                            'lsa_id': '10.1.0.6',
                                                            'num_links': 1,
                                                            'opaque_id': 6,
                                                            'opaque_type': 1,
                                                            'option': '0x20',
                                                            'option_desc': 'No TOS-capability, DC',
                                                            'seq_num': '0x80000003',
                                                            'type': 10}}}}}}}}}}}}}}}}
