expected_output =  {
     'tag': {
         '1': {
             'level': {
                 1: {
                     'r1.00-00': {
                         'area_address': '49.0001',
                         'attach_bit': 0,
                         'extended_is_neighbor': {
                             'r2.00': {
                                 'metric': [10, 20, 30],
                                 'neighbor_id': 'r2.00',
                             },
                         },
                         'hostname': 'r1',
                         'ip_address': '1.1.1.1',
                         'ipv4_internal_reachability': {
                             '1.1.1.1/32': {
                                 'ip_prefix': '1.1.1.1',
                                 'metric': 0,
                                 'prefix_len': '32',
                             },
                             '10.10.10.0/30': {
                                 'ip_prefix': '10.10.10.0',
                                 'metric': 10,
                                 'prefix_len': '30',
                             },
                             '20.20.20.0/30': {
                                 'ip_prefix': '20.20.20.0',
                                 'metric': 20,
                                 'prefix_len': '30',
                             },
                             '30.30.30.0/30': {
                                 'ip_prefix': '30.30.30.0',
                                 'metric': 30,
                                 'prefix_len': '30',
                             },
                             '30.30.30.4/30': {
                                 'ip_prefix': '30.30.30.4',
                                 'metric': 30,
                                 'prefix_len': '30',
                             },
                         },
                         'ipv6_address': '2001:DB8:F:1::1',
                         'lsp_checksum': '0x116C',
                         'lsp_holdtime': '1170',
                         'lsp_rcvd': '1199',
                         'lsp_sequence_num': '0x0000000D',
                         'mt_ipv6_reachability': {
                             '2001:DB8:1::/126': {
                                 'ip_prefix': '2001:DB8:1::',
                                 'metric': 10,
                                 'prefix_len': '126',
                             },
                             '2001:DB8:2::/126': {
                                 'ip_prefix': '2001:DB8:2::',
                                 'metric': 10,
                                 'prefix_len': '126',
                             },
                             '2001:DB8:3::/126': {
                                 'ip_prefix': '2001:DB8:3::',
                                 'metric': 10,
                                 'prefix_len': '126',
                             },
                             '2001:DB8:F:1::1/128': {
                                 'ip_prefix': '2001:DB8:F:1::1',
                                 'metric': 0,
                                 'prefix_len': '128',
                             },
                         },
                         'mt_is_neighbor': {
                             'r2.00': {
                                 'metric': 10,
                                 'neighbor_id': 'r2.00',
                             },
                         },
                         'nlpid': '0xCC 0x8E',
                         'overload_bit': 0,
                         'p_bit': 0,
                         'router_id': '1.1.1.1',
                         'topology': {
                             'ipv4': {
                                 'code': '0x0',
                             },
                             'ipv6': {
                                 'code': '0x2',
                             },
                         },
                     },
                     'r2.00-00': {
                         'area_address': '49.0001',
                         'attach_bit': 0,
                         'extended_is_neighbor': {
                             'r1.00': {
                                 'metric': [10, 20, 30],
                                 'neighbor_id': 'r1.00',
                             },
                         },
                         'hostname': 'r2',
                         'ip_address': '2.2.2.2',
                         'ipv4_internal_reachability': {
                             '10.10.10.0/30': {
                                 'ip_prefix': '10.10.10.0',
                                 'metric': 10,
                                 'prefix_len': '30',
                             },
                             '2.2.2.2/32': {
                                 'ip_prefix': '2.2.2.2',
                                 'metric': 0,
                                 'prefix_len': '32',
                             },
                             '20.20.20.0/30': {
                                 'ip_prefix': '20.20.20.0',
                                 'metric': 20,
                                 'prefix_len': '30',
                             },
                             '30.30.30.0/30': {
                                 'ip_prefix': '30.30.30.0',
                                 'metric': 30,
                                 'prefix_len': '30',
                             },
                         },
                         'ipv6_address': '2001:DB8:F:2::2',
                         'local_router': True,
                         'lsp_checksum': '0x5635',
                         'lsp_holdtime': '1193',
                         'lsp_rcvd': '*',
                         'lsp_sequence_num': '0x0000000C',
                         'mt_ipv6_reachability': {
                             '2001:DB8:1::/126': {
                                 'ip_prefix': '2001:DB8:1::',
                                 'metric': 10,
                                 'prefix_len': '126',
                             },
                             '2001:DB8:2::/126': {
                                 'ip_prefix': '2001:DB8:2::',
                                 'metric': 10,
                                 'prefix_len': '126',
                             },
                             '2001:DB8:3::/126': {
                                 'ip_prefix': '2001:DB8:3::',
                                 'metric': 10,
                                 'prefix_len': '126',
                             },
                             '2001:DB8:F:2::2/128': {
                                 'ip_prefix': '2001:DB8:F:2::2',
                                 'metric': 0,
                                 'prefix_len': '128',
                             },
                         },
                         'mt_is_neighbor': {
                             'r1.00': {
                                 'metric': [10, 10, 10],
                                 'neighbor_id': 'r1.00',
                             },
                         },
                         'nlpid': '0xCC 0x8E',
                         'overload_bit': 0,
                         'p_bit': 0,
                         'router_id': '2.2.2.2',
                         'topology': {
                             'ipv4': {
                                 'code': '0x0',
                             },
                             'ipv6': {
                                 'code': '0x2',
                             },
                         },
                     },
                 },
             },
         },
     },
 }