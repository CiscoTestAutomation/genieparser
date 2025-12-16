expected_output = {'packets': {3: {'cbug_id': 10,
              'packet_copy_in': 'ac3a67e5 34115057 a86cfa92 08004500 021b0003 00003c06 bd925a01 001e6401 012813c4 '
                                '13c40000 43070000 2f235018 2238d157 0000494e 56495445 20736970 3a323030 31403130 '
                                '302e312e 312e3430 3a353036 30205349 502f322e 300d0a56 69613a20 5349502f 322e302f '
                                '54435020 39302e31 2e302e31 303a3530 36303b62 72616e63 683d7a39 68473462 4b2d3537 '
                                '35302d31 2d300d0a 46726f6d 3a207369 7070203c 7369703a 73697070 4039302e 312e302e '
                                '31303a35 3036303e 3b746167 3d353735 30534950 70546167 3030310d 0a546f3a 20323030 '
                                '31203c73 69703a32 30303140 3130302e 312e312e 34303a35 3036303e 0d0a4361 6c6c2d49 '
                                '443a2031 2d353735 30403930 2e312e30 2e31300d 0a435365 713a2031 20494e56 4954450d '
                                '0a436f6e 74616374 3a207369 703a7369 70704039 302e312e 302e3130 3a353036 300d0a4d '
                                '61782d46 6f727761 7264733a 2037300d 0a537562 6a656374 3a205065 72666f72 6d616e63 '
                                '65205465 73740d0a 436f6e74 656e742d 54797065 3a206170 706c6963 6174696f 6e2f7364 '
                                '700d0a43 6f6e7465 6e742d4c 656e6774 683a2020 20313239 0d0a0d0a 763d300d 0a6f3d75 '
                                '73657231 20353336 35353736 35203233 35333638 37363337 20494e20 49503420 39302e31 '
                                '2e302e31 300d0a73 3d2d0d0a 633d494e 20495034 2039302e 312e302e 31300d0a 743d3020 '
                                '300d0a6d 3d617564 696f2036 30303020 5254502f 41565020 300d0a61 3d727470 6d61703a '
                                '30205043 4d552f38 3030300d 0a',
              'packet_copy_out': 'c471fe70 8933ac3a 67e53412 08004500 021b0003 00003b06 b39c6401 01146401 012813c4 '
                                 '13c40000 43070000 2f235018 2238c661 0000494e 56495445 20736970 3a323030 31403130 '
                                 '302e312e 312e3430 3a353036 30205349 502f322e 300d0a56 69613a20 5349502f 322e302f '
                                 '54435020 39302e31 2e302e31 303a3530 36303b62 72616e63 683d7a39 68473462 4b2d3537 '
                                 '35302d31 2d300d0a 46726f6d 3a207369 7070203c 7369703a 73697070 4039302e 312e302e '
                                 '31303a35 3036303e 3b746167 3d353735 30534950 70546167 3030310d 0a546f3a 20323030 '
                                 '31203c73 69703a32 30303140 3130302e 312e312e 34303a35 3036303e 0d0a4361 6c6c2d49 '
                                 '443a2031 2d353735 30403930 2e312e30 2e31300d 0a435365 713a2031 20494e56 4954450d '
                                 '0a436f6e 74616374 3a207369 703a7369 70704039 302e312e 302e3130 3a353036 300d0a4d '
                                 '61782d46 6f727761 7264733a 2037300d 0a537562 6a656374 3a205065 72666f72 6d616e63 '
                                 '65205465 73740d0a 436f6e74 656e742d 54797065 3a206170 706c6963 6174696f 6e2f7364 '
                                 '700d0a43 6f6e7465 6e742d4c 656e6774 683a2020 20313239 0d0a0d0a 763d300d 0a6f3d75 '
                                 '73657231 20353336 35353736 35203233 35333638 37363337 20494e20 49503420 39302e31 '
                                 '2e302e31 300d0a73 3d2d0d0a 633d494e 20495034 2039302e 312e302e 31300d0a 743d3020 '
                                 '300d0a6d 3d617564 696f2036 30303020 5254502f 41565020 300d0a61 3d727470 6d61703a '
                                 '30205043 4d552f38 3030300d 0a',
              'path_trace': {'ALG PARSER': {'action': 'OK', 'caller': 'NAT', 'type': 'SIP ALG'},
                            'ALG PARSER_2': {'action': 'OK', 'caller': 'FW', 'type': 'SIP ALG'},
                            'ALG PARSER_3': {'action': 'OK', 'caller': 'NAT', 'type': 'SIP ALG'},
                            'ALG WRITEBACK': {'action': 'OK'},
                            'ALG WRITEBACK_10': {'action': 'OK'},
                            'ALG WRITEBACK_11': {'action': 'OK'},
                            'ALG WRITEBACK_2': {'action': 'OK'},
                            'ALG WRITEBACK_3': {'action': 'OK'},
                            'ALG WRITEBACK_4': {'action': 'OK'},
                            'ALG WRITEBACK_5': {'action': 'OK'},
                            'ALG WRITEBACK_6': {'action': 'OK'},
                            'ALG WRITEBACK_7': {'action': 'OK'},
                            'ALG WRITEBACK_8': {'action': 'OK'},
                            'ALG WRITEBACK_9': {'action': 'OK'},
                            'ipv4_input': {'destination': '100.1.1.40',
                                          'dst_port': '5060',
                                          'input': 'GigabitEthernet0/0/1',
                                          'output': '<unknown>',
                                          'protocol': '6 (TCP)',
                                          'source': '90.1.0.30',
                                          'src_port': '5060'},
                            'nat': {'action': 'Translate Source',
                                   'direction': 'IN to OUT',
                                   'event_flags': '0x0',
                                   'from': '',
                                   'in_uidb': '8',
                                   'lookup_flags': '0x1',
                                   'map_id_result': '0',
                                   'match_id': '5',
                                   'new_address': '100.1.1.20',
                                   'new_dest_port': '5060',
                                   'new_src_port': '5060',
                                   'old_address': '90.1.0.30',
                                   'orig_dest_port': '5060',
                                   'orig_src_port': '5060',
                                   'out_uidb': '0',
                                   'proc_flags': '0x0',
                                   'protocol': 'TCP',
                                   'rule_id': '0',
                                   'steps': 'SESS-FOUND',
                                   'table_id': '0',
                                   'trace_point': '0x0',
                                   'vrfid': '0'},
                            'qos': {'action': 'FWD',
                                   'avg_queue_len': 'n/a',
                                   'direction': 'Egress',
                                   'inst_queue_len': '0',
                                   'pak_priority': 'FALSE',
                                   'pal_queue_id': '0 (0x0)',
                                   'priority': 'FALSE',
                                   'queue_id': '114 (0x72)',
                                   'queue_limit': '4210',
                                   'wred_enabled': 'FALSE'},
                            'threat_defense_vtcp': {'ack': '12067',
                                      'action': 'VTCP_SUCCESS: VTCP Success',
                                      'flags': '0x18 (ACK PSH)',
                                      'len': '499',
                                      'mss': '1460',
                                      'seq': '17159'},
                            'vtcp': {'ack': '12067',
                                    'action': 'OK',
                                    'flags': '0x18 (ACK PSH)',
                                    'len': '499',
                                    'mss': '1460',
                                    'seq': '17159'},
                            'vtcp_2': {'ack': '12067',
                                    'action': 'OK',
                                    'flags': '0x18 (ACK PSH)',
                                    'len': '499',
                                    'mss': '0',
                                    'seq': '17159'},
                            'vtcp_3': {'ack': '12067',
                                    'action': 'OK',
                                    'flags': '0x18 (ACK PSH)',
                                    'len': '499',
                                    'mss': '0',
                                    'seq': '17159'},
                            'zbfw': {'action': 'Fwd',
                                    'avc_classification_id': '0',
                                    'avc_classification_name': 'N/A',
                                    'class_map_name': 'policyclassmap_sip',
                                    'egress_interface': 'GigabitEthernet0/0/2',
                                    'input_interface': 'GigabitEthernet0/0/1',
                                    'input_vpn_id': '65535',
                                    'input_vrf_id': 'Name     : 0:',
                                    'nat': 'nat44 (nat api)',
                                    'output_vpn_id': '65535',
                                    'output_vrf_id': 'Name     : 0:',
                                    'policy_name': 'sericepolicymap',
                                    'utd_context_id': '0',
                                    'zone_pair_name': 'private2public'}},
              'summary': {'input': 'GigabitEthernet0/0/1',
                         'output': 'GigabitEthernet0/0/2',
                         'start_timestamp': '04/08/2025 12:10:31.614897',
                         'start_timestamp_ns': 354469269115268,
                         'state': 'FWD',
                         'stop_timestamp': '04/08/2025 12:10:31.615120',
                         'stop_timestamp_ns': 354469269338243}}}}
