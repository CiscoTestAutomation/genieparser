

expected_output = {
    'instance': {
        'test': {
            'vrf': {
                'default': {
                    'level_db': {
                        1: {
                            'R1_xe.00-00': {
                                'lsp_id': 'R1_xe.00-00',
                                'sequence': '0x000007CD',
                                'checksum': '0xAD22',
                                'lifetime': 1199,
                                'attach_bit': 0,
                                'p_bit': 0,
                                'overload_bit': 0,
                                't_bit': 3,
                                'lsp_status': '',
                                'instance': '0x000007C9',
                                'area_address': '49.0001',
                                'nlpid': '0xCC 0x8E',
                                'mt_entries': {
                                    0: {
                                        'att': 0,
                                        'ol': 0,
                                    },
                                    2: {
                                        'att': 0,
                                        'ol': 0,
                                    },
                                },
                                'hostname': 'R1_xe',
                                'length': 5,
                                'extended_is_neighbor': {
                                    'R1_xe.02': {
                                        'neighbor_id': 'R1_xe.02',
                                        'metric': 10,
                                    },
                                    'R1_xe.01': {
                                        'neighbor_id': 'R1_xe.01',
                                        'metric': 10,
                                    },
                                },
                                'mt_is_neighbor': {
                                    'R1_xe.02': {
                                        'neighbor_id': 'R1_xe.02',
                                        'metric': 10,
                                        'topo_id': 2,
                                    },
                                    'R1_xe.01': {
                                        'neighbor_id': 'R1_xe.01',
                                        'metric': 10,
                                        'topo_id': 2,
                                    },
                                },
                                'ip_address': '10.13.115.1',
                                'extended_ip': {
                                    '10.12.115.0/24': {
                                        'metric': 10,
                                        'up_down': 'U',
                                        'sub_tlv_length': 1,
                                        'sub_tlv_type': 4,
                                    },
                                    '10.13.115.0/24': {
                                        'metric': 10,
                                        'up_down': 'U',
                                        'sub_tlv_length': 1,
                                        'sub_tlv_type': 4,
                                    },
                                },
                                'ipv6_address': '2001:10:13:115::1',
                                'mt_ipv6_prefix': {
                                    '2001:10:12:115::/64': {
                                        'metric': 10,
                                        'topo_id': 2,
                                        'up_down': 'U',
                                        'ext_origin': 'I',
                                        'sub_tlv_length': 1,
                                        'sub_tlv_type': 4,
                                    },
                                    '2001:10:13:115::/64': {
                                        'metric': 10,
                                        'topo_id': 2,
                                        'up_down': 'U',
                                        'ext_origin': 'I',
                                        'sub_tlv_length': 1,
                                        'sub_tlv_type': 4,
                                    },
                                },
                                'digest_offset': 0,
                            },
                            'R1_xe.01-00': {
                                'lsp_id': 'R1_xe.01-00',
                                'sequence': '0x000007C7',
                                'checksum': '0x14CA',
                                'lifetime': 846,
                                'attach_bit': 0,
                                'p_bit': 0,
                                'overload_bit': 0,
                                't_bit': 3,
                                'lsp_status': '',
                                'instance': '0x000007C6',
                                'extended_is_neighbor': {
                                    'R1_xe.00': {
                                        'neighbor_id': 'R1_xe.00',
                                        'metric': 0,
                                    },
                                    'R2_xr.00': {
                                        'neighbor_id': 'R2_xr.00',
                                        'metric': 0,
                                    },
                                },
                                'digest_offset': 0,
                            },
                            'R1_xe.02-00': {
                                'lsp_id': 'R1_xe.02-00',
                                'sequence': '0x000007C7',
                                'checksum': '0x0D6A',
                                'lifetime': 852,
                                'attach_bit': 0,
                                'p_bit': 0,
                                'overload_bit': 0,
                                't_bit': 3,
                                'lsp_status': '',
                                'instance': '0x000007C6',
                                'extended_is_neighbor': {
                                    'R1_xe.00': {
                                        'neighbor_id': 'R1_xe.00',
                                        'metric': 0,
                                    },
                                    'R3_nx.00': {
                                        'neighbor_id': 'R3_nx.00',
                                        'metric': 0,
                                    },
                                },
                                'digest_offset': 0,
                            },
                            'R2_xr.00-00': {
                                'lsp_id': 'R2_xr.00-00',
                                'sequence': '0x000007C5',
                                'checksum': '0x94D6',
                                'lifetime': 887,
                                'attach_bit': 0,
                                'p_bit': 0,
                                'overload_bit': 0,
                                't_bit': 3,
                                'lsp_status': '',
                                'instance': '0x000007BD',
                                'area_address': '49.0001',
                                'nlpid': '0xCC 0x8E',
                                'ip_address': '10.16.2.2',
                                'extended_ip': {
                                    '10.16.2.2/32': {
                                        'metric': 10,
                                        'up_down': 'U',
                                        'sub_tlv_length': 1,
                                        'sub_tlv_type': 4,
                                    },
                                    '10.12.115.0/24': {
                                        'metric': 10,
                                        'up_down': 'U',
                                        'sub_tlv_length': 1,
                                        'sub_tlv_type': 4,
                                    },
                                    '10.23.115.0/24': {
                                        'metric': 10,
                                        'up_down': 'U',
                                        'sub_tlv_length': 1,
                                        'sub_tlv_type': 4,
                                    },
                                },
                                'hostname': 'R2_xr',
                                'length': 5,
                                'ipv6_address': '2001:2:2:2::2',
                                'mt_ipv6_prefix': {
                                    '2001:2:2:2::2/128': {
                                        'metric': 10,
                                        'topo_id': 2,
                                        'up_down': 'U',
                                        'ext_origin': 'I',
                                        'sub_tlv_length': 1,
                                        'sub_tlv_type': 4,
                                    },
                                    '2001:10:12:115::/64': {
                                        'metric': 10,
                                        'topo_id': 2,
                                        'up_down': 'U',
                                        'ext_origin': 'I',
                                        'sub_tlv_length': 1,
                                        'sub_tlv_type': 4,
                                    },
                                    '2001:10:23:115::/64': {
                                        'metric': 10,
                                        'topo_id': 2,
                                        'up_down': 'U',
                                        'ext_origin': 'I',
                                        'sub_tlv_length': 1,
                                        'sub_tlv_type': 4,
                                    },
                                },
                                'mt_entries': {
                                    0: {
                                        'att': 0,
                                        'ol': 0,
                                    },
                                    2: {
                                        'att': 0,
                                        'ol': 0,
                                    },
                                },
                                'extended_is_neighbor': {
                                    'R1_xe.01': {
                                        'neighbor_id': 'R1_xe.01',
                                        'metric': 10,
                                    },
                                    'R2_xr.03': {
                                        'neighbor_id': 'R2_xr.03',
                                        'metric': 10,
                                    },
                                },
                                'mt_is_neighbor': {
                                    'R2_xr.03': {
                                        'neighbor_id': 'R2_xr.03',
                                        'metric': 10,
                                        'topo_id': 2,
                                    },
                                },
                                'digest_offset': 0,
                            },
                            'R2_xr.03-00': {
                                'lsp_id': 'R2_xr.03-00',
                                'sequence': '0x000007C6',
                                'checksum': '0x86AC',
                                'lifetime': 594,
                                'attach_bit': 0,
                                'p_bit': 0,
                                'overload_bit': 0,
                                't_bit': 3,
                                'lsp_status': '',
                                'instance': '0x000007C5',
                                'extended_is_neighbor': {
                                    'R2_xr.00': {
                                        'neighbor_id': 'R2_xr.00',
                                        'metric': 0,
                                    },
                                    'R3_nx.00': {
                                        'neighbor_id': 'R3_nx.00',
                                        'metric': 0,
                                    },
                                },
                                'digest_offset': 0,
                            },
                            'R3_nx.00-00': {
                                'lsp_id': 'R3_nx.00-00',
                                'sequence': '0x00000B05',
                                'checksum': '0x7FA7',
                                'lifetime': 653,
                                'attach_bit': 0,
                                'p_bit': 0,
                                'overload_bit': 0,
                                't_bit': 3,
                                'lsp_status': '*',
                                'instance': '0x00000B05',
                                'area_address': '49.0001',
                                'nlpid': '0xCC 0x8E',
                                'router_id': '10.36.3.3',
                                'ip_address': '10.36.3.3',
                                'mt_entries': {
                                    2: {
                                        'att': 0,
                                        'ol': 0,
                                    },
                                    0: {
                                        'att': 0,
                                        'ol': 0,
                                    },
                                },
                                'hostname': 'R3_nx',
                                'length': 5,
                                'mt_is_neighbor': {
                                    'R3_nx.00': {
                                        'neighbor_id': 'R1_xe.02',
                                        'metric': 40,
                                        'topo_id': 2,
                                    },
                                },
                                'extended_is_neighbor': {
                                    'R2_xr.03': {
                                        'neighbor_id': 'R2_xr.03',
                                        'metric': 40,
                                    },
                                    'R1_xe.02': {
                                        'neighbor_id': 'R1_xe.02',
                                        'metric': 40,
                                    },
                                },
                                'extended_ip': {
                                    '10.36.3.3/32': {
                                        'metric': 1,
                                        'up_down': 'U',
                                    },
                                    '10.13.115.0/24': {
                                        'metric': 40,
                                        'up_down': 'U',
                                    },
                                    '10.23.115.0/24': {
                                        'metric': 40,
                                        'up_down': 'U',
                                    },
                                },
                                'mt_ipv6_prefix': {
                                    '2001:3:3:3::3/128': {
                                        'metric': 1,
                                        'topo_id': 2,
                                        'up_down': 'U',
                                        'ext_origin': 'I',
                                    },
                                    '2001:10:13:115::/64': {
                                        'metric': 40,
                                        'topo_id': 2,
                                        'up_down': 'U',
                                        'ext_origin': 'I',
                                    },
                                    '2001:10:23:115::/64': {
                                        'metric': 40,
                                        'topo_id': 2,
                                        'up_down': 'U',
                                        'ext_origin': 'I',
                                    },
                                },
                                'digest_offset': 0,
                            },
                        },
                        2: {
                            'R1_xe.00-00': {
                                'lsp_id': 'R1_xe.00-00',
                                'sequence': '0x000007C9',
                                'checksum': '0xBB89',
                                'lifetime': 1087,
                                'attach_bit': 0,
                                'p_bit': 0,
                                'overload_bit': 0,
                                't_bit': 3,
                                'lsp_status': '',
                                'instance': '0x000007C4',
                                'area_address': '49.0001',
                                'nlpid': '0xCC 0x8E',
                                'mt_entries': {
                                    0: {
                                        'att': 0,
                                        'ol': 0,
                                    },
                                    2: {
                                        'att': 0,
                                        'ol': 0,
                                    },
                                },
                                'hostname': 'R1_xe',
                                'length': 5,
                                'extended_is_neighbor': {
                                    'R1_xe.02': {
                                        'neighbor_id': 'R1_xe.02',
                                        'metric': 10,
                                    },
                                    'R1_xe.01': {
                                        'neighbor_id': 'R1_xe.01',
                                        'metric': 10,
                                    },
                                },
                                'mt_is_neighbor': {
                                    'R1_xe.02': {
                                        'neighbor_id': 'R1_xe.02',
                                        'metric': 10,
                                        'topo_id': 2,
                                    },
                                    'R1_xe.01': {
                                        'neighbor_id': 'R1_xe.01',
                                        'metric': 10,
                                        'topo_id': 2,
                                    },
                                },
                                'ip_address': '10.13.115.1',
                                'extended_ip': {
                                    '10.12.115.0/24': {
                                        'metric': 10,
                                        'up_down': 'U',
                                        'sub_tlv_length': 1,
                                        'sub_tlv_type': 4,
                                    },
                                    '10.13.115.0/24': {
                                        'metric': 10,
                                        'up_down': 'U',
                                        'sub_tlv_length': 1,
                                        'sub_tlv_type': 4,
                                    },
                                    '10.23.115.0/24': {
                                        'metric': 20,
                                        'up_down': 'U',
                                        'sub_tlv_length': 1,
                                        'sub_tlv_type': 4,
                                    },
                                },
                                'ipv6_address': '2001:10:13:115::1',
                                'mt_ipv6_prefix': {
                                    '2001:10:12:115::/64': {
                                        'metric': 10,
                                        'topo_id': 2,
                                        'up_down': 'U',
                                        'ext_origin': 'I',
                                        'sub_tlv_length': 1,
                                        'sub_tlv_type': 4,
                                    },
                                    '2001:10:13:115::/64': {
                                        'metric': 10,
                                        'topo_id': 2,
                                        'up_down': 'U',
                                        'ext_origin': 'I',
                                        'sub_tlv_length': 1,
                                        'sub_tlv_type': 4,
                                    },
                                    '2001:10:23:115::/64': {
                                        'metric': 20,
                                        'topo_id': 2,
                                        'up_down': 'U',
                                        'ext_origin': 'I',
                                        'sub_tlv_length': 1,
                                        'sub_tlv_type': 4,
                                    },
                                },
                                'digest_offset': 0,
                            },
                            'R1_xe.01-00': {
                                'lsp_id': 'R1_xe.01-00',
                                'sequence': '0x000007C0',
                                'checksum': '0x3A34',
                                'lifetime': 1137,
                                'attach_bit': 0,
                                'p_bit': 0,
                                'overload_bit': 0,
                                't_bit': 3,
                                'lsp_status': '',
                                'instance': '0x000007BF',
                                'extended_is_neighbor': {
                                    'R1_xe.00': {
                                        'neighbor_id': 'R1_xe.00',
                                        'metric': 0,
                                    },
                                    'R2_xr.00': {
                                        'neighbor_id': 'R2_xr.00',
                                        'metric': 0,
                                    },
                                },
                                'digest_offset': 0,
                            },
                            'R1_xe.02-00': {
                                'lsp_id': 'R1_xe.02-00',
                                'sequence': '0x000007C8',
                                'checksum': '0x23DB',
                                'lifetime': 867,
                                'attach_bit': 0,
                                'p_bit': 0,
                                'overload_bit': 0,
                                't_bit': 3,
                                'lsp_status': '',
                                'instance': '0x000007C7',
                                'extended_is_neighbor': {
                                    'R1_xe.00': {
                                        'neighbor_id': 'R1_xe.00',
                                        'metric': 0,
                                    },
                                    'R3_nx.00': {
                                        'neighbor_id': 'R3_nx.00',
                                        'metric': 0,
                                    },
                                },
                                'digest_offset': 0,
                            },
                            'R2_xr.00-00': {
                                'lsp_id': 'R2_xr.00-00',
                                'sequence': '0x000007D1',
                                'checksum': '0xE002',
                                'lifetime': 813,
                                'attach_bit': 0,
                                'p_bit': 0,
                                'overload_bit': 0,
                                't_bit': 3,
                                'lsp_status': '',
                                'instance': '0x000007C9',
                                'area_address': '49.0001',
                                'nlpid': '0xCC 0x8E',
                                'ip_address': '10.16.2.2',
                                'extended_ip': {
                                    '10.16.2.2/32': {
                                        'metric': 10,
                                        'up_down': 'U',
                                        'sub_tlv_length': 1,
                                        'sub_tlv_type': 4,
                                    },
                                    '10.12.115.0/24': {
                                        'metric': 10,
                                        'up_down': 'U',
                                        'sub_tlv_length': 1,
                                        'sub_tlv_type': 4,
                                    },
                                    '10.23.115.0/24': {
                                        'metric': 10,
                                        'up_down': 'U',
                                        'sub_tlv_length': 1,
                                        'sub_tlv_type': 4,
                                    },
                                    '10.36.3.3/32': {
                                        'metric': 11,
                                        'up_down': 'U',
                                        'sub_tlv_length': 1,
                                        'sub_tlv_type': 4,
                                    },
                                    '10.13.115.0/24': {
                                        'metric': 20,
                                        'up_down': 'U',
                                        'sub_tlv_length': 1,
                                        'sub_tlv_type': 4,
                                    },
                                },
                                'hostname': 'R2_xr',
                                'length': 5,
                                'ipv6_address': '2001:2:2:2::2',
                                'mt_ipv6_prefix': {
                                    '2001:2:2:2::2/128': {
                                        'metric': 10,
                                        'topo_id': 2,
                                        'up_down': 'U',
                                        'ext_origin': 'I',
                                        'sub_tlv_length': 1,
                                        'sub_tlv_type': 4,
                                    },
                                    '2001:10:12:115::/64': {
                                        'metric': 10,
                                        'topo_id': 2,
                                        'up_down': 'U',
                                        'ext_origin': 'I',
                                        'sub_tlv_length': 1,
                                        'sub_tlv_type': 4,
                                    },
                                    '2001:10:23:115::/64': {
                                        'metric': 10,
                                        'topo_id': 2,
                                        'up_down': 'U',
                                        'ext_origin': 'I',
                                        'sub_tlv_length': 1,
                                        'sub_tlv_type': 4,
                                    },
                                    '2001:3:3:3::3/128': {
                                        'metric': 11,
                                        'topo_id': 2,
                                        'up_down': 'U',
                                        'ext_origin': 'I',
                                        'sub_tlv_length': 1,
                                        'sub_tlv_type': 4,
                                    },
                                    '2001:10:13:115::/64': {
                                        'metric': 20,
                                        'topo_id': 2,
                                        'up_down': 'U',
                                        'ext_origin': 'I',
                                        'sub_tlv_length': 1,
                                        'sub_tlv_type': 4,
                                    },
                                },
                                'mt_entries': {
                                    0: {
                                        'att': 0,
                                        'ol': 0,
                                    },
                                    2: {
                                        'att': 0,
                                        'ol': 0,
                                    },
                                },
                                'extended_is_neighbor': {
                                    'R2_xr.03': {
                                        'neighbor_id': 'R2_xr.03',
                                        'metric': 10,
                                    },
                                    'R1_xe.01': {
                                        'neighbor_id': 'R1_xe.01',
                                        'metric': 10,
                                    },
                                },
                                'mt_is_neighbor': {
                                    'R1_xe.01': {
                                        'neighbor_id': 'R1_xe.01',
                                        'metric': 10,
                                        'topo_id': 2,
                                    },
                                },
                                'digest_offset': 0,
                            },
                            'R2_xr.03-00': {
                                'lsp_id': 'R2_xr.03-00',
                                'sequence': '0x000007C2',
                                'checksum': '0x8EA8',
                                'lifetime': 784,
                                'attach_bit': 0,
                                'p_bit': 0,
                                'overload_bit': 0,
                                't_bit': 3,
                                'lsp_status': '',
                                'instance': '0x000007C1',
                                'extended_is_neighbor': {
                                    'R2_xr.00': {
                                        'neighbor_id': 'R2_xr.00',
                                        'metric': 0,
                                    },
                                    'R3_nx.00': {
                                        'neighbor_id': 'R3_nx.00',
                                        'metric': 0,
                                    },
                                },
                                'digest_offset': 0,
                            },
                            'R3_nx.00-00': {
                                'lsp_id': 'R3_nx.00-00',
                                'sequence': '0x00000B05',
                                'checksum': '0x7FA7',
                                'lifetime': 1040,
                                'attach_bit': 0,
                                'p_bit': 0,
                                'overload_bit': 0,
                                't_bit': 3,
                                'lsp_status': '*',
                                'instance': '0x00000B05',
                                'area_address': '49.0001',
                                'nlpid': '0xCC 0x8E',
                                'router_id': '10.36.3.3',
                                'ip_address': '10.36.3.3',
                                'mt_entries': {
                                    2: {
                                        'att': 0,
                                        'ol': 0,
                                    },
                                    0: {
                                        'att': 0,
                                        'ol': 0,
                                    },
                                },
                                'hostname': 'R3_nx',
                                'length': 5,
                                'mt_is_neighbor': {
                                    'R3_nx.00': {
                                        'neighbor_id': 'R1_xe.02',
                                        'metric': 40,
                                        'topo_id': 2,
                                    },
                                },
                                'extended_is_neighbor': {
                                    'R2_xr.03': {
                                        'neighbor_id': 'R2_xr.03',
                                        'metric': 40,
                                    },
                                    'R1_xe.02': {
                                        'neighbor_id': 'R1_xe.02',
                                        'metric': 40,
                                    },
                                },
                                'extended_ip': {
                                    '10.36.3.3/32': {
                                        'metric': 1,
                                        'up_down': 'U',
                                    },
                                    '10.13.115.0/24': {
                                        'metric': 40,
                                        'up_down': 'U',
                                    },
                                    '10.23.115.0/24': {
                                        'metric': 40,
                                        'up_down': 'U',
                                    },
                                },
                                'mt_ipv6_prefix': {
                                    '2001:3:3:3::3/128': {
                                        'metric': 1,
                                        'topo_id': 2,
                                        'up_down': 'U',
                                        'ext_origin': 'I',
                                    },
                                    '2001:10:13:115::/64': {
                                        'metric': 40,
                                        'topo_id': 2,
                                        'up_down': 'U',
                                        'ext_origin': 'I',
                                    },
                                    '2001:10:23:115::/64': {
                                        'metric': 40,
                                        'topo_id': 2,
                                        'up_down': 'U',
                                        'ext_origin': 'I',
                                    },
                                },
                                'digest_offset': 0,
                            },
                        },
                    },
                },
                'VRF1': {
                    'level_db': {
                        1: {
                            'R1_xe.00-00': {
                                'lsp_id': 'R1_xe.00-00',
                                'sequence': '0x000007CA',
                                'checksum': '0xC7FC',
                                'lifetime': 616,
                                'attach_bit': 0,
                                'p_bit': 0,
                                'overload_bit': 0,
                                't_bit': 3,
                                'lsp_status': '',
                                'instance': '0x000007C6',
                                'area_address': '49.0001',
                                'nlpid': '0xCC 0x8E',
                                'mt_entries': {
                                    0: {
                                        'att': 0,
                                        'ol': 0,
                                    },
                                    2: {
                                        'att': 0,
                                        'ol': 0,
                                    },
                                },
                                'hostname': 'R1_xe',
                                'length': 5,
                                'extended_is_neighbor': {
                                    'R1_xe.02': {
                                        'neighbor_id': 'R1_xe.02',
                                        'metric': 10,
                                    },
                                },
                                'mt_is_neighbor': {
                                    'R1_xe.02': {
                                        'neighbor_id': 'R1_xe.02',
                                        'metric': 10,
                                        'topo_id': 2,
                                    },
                                },
                                'ip_address': '10.13.115.1',
                                'extended_ip': {
                                    '10.12.115.0/24': {
                                        'metric': 10,
                                        'up_down': 'U',
                                        'sub_tlv_length': 1,
                                        'sub_tlv_type': 4,
                                    },
                                    '10.13.115.0/24': {
                                        'metric': 10,
                                        'up_down': 'U',
                                        'sub_tlv_length': 1,
                                        'sub_tlv_type': 4,
                                    },
                                },
                                'ipv6_address': '2001:10:13:115::1',
                                'mt_ipv6_prefix': {
                                    '2001:10:12:115::/64': {
                                        'metric': 10,
                                        'topo_id': 2,
                                        'up_down': 'U',
                                        'ext_origin': 'I',
                                        'sub_tlv_length': 1,
                                        'sub_tlv_type': 4,
                                    },
                                    '2001:10:13:115::/64': {
                                        'metric': 10,
                                        'topo_id': 2,
                                        'up_down': 'U',
                                        'ext_origin': 'I',
                                        'sub_tlv_length': 1,
                                        'sub_tlv_type': 4,
                                    },
                                },
                                'digest_offset': 0,
                            },
                            'R1_xe.02-00': {
                                'lsp_id': 'R1_xe.02-00',
                                'sequence': '0x000007C7',
                                'checksum': '0x0D6A',
                                'lifetime': 625,
                                'attach_bit': 0,
                                'p_bit': 0,
                                'overload_bit': 0,
                                't_bit': 3,
                                'lsp_status': '',
                                'instance': '0x000007C6',
                                'extended_is_neighbor': {
                                    'R1_xe.00': {
                                        'neighbor_id': 'R1_xe.00',
                                        'metric': 0,
                                    },
                                    'R3_nx.00': {
                                        'neighbor_id': 'R3_nx.00',
                                        'metric': 0,
                                    },
                                },
                                'digest_offset': 0,
                            },
                            'R3_nx.00-00': {
                                'lsp_id': 'R3_nx.00-00',
                                'sequence': '0x00000B09',
                                'checksum': '0x68C0',
                                'lifetime': 841,
                                'attach_bit': 0,
                                'p_bit': 0,
                                'overload_bit': 0,
                                't_bit': 3,
                                'lsp_status': '*',
                                'instance': '0x00000B09',
                                'area_address': '49.0001',
                                'nlpid': '0xCC 0x8E',
                                'router_id': '10.36.3.3',
                                'ip_address': '10.36.3.3',
                                'mt_entries': {
                                    2: {
                                        'att': 0,
                                        'ol': 0,
                                    },
                                    0: {
                                        'att': 0,
                                        'ol': 0,
                                    },
                                },
                                'hostname': 'R3_nx',
                                'length': 5,
                                'mt_is_neighbor': {
                                    'R3_nx.00': {
                                        'neighbor_id': 'R1_xe.02',
                                        'metric': 40,
                                        'topo_id': 2,
                                    },
                                },
                                'extended_is_neighbor': {
                                    'R1_xe.02': {
                                        'neighbor_id': 'R1_xe.02',
                                        'metric': 40,
                                    },
                                },
                                'extended_ip': {
                                    '10.36.3.3/32': {
                                        'metric': 1,
                                        'up_down': 'U',
                                    },
                                    '10.13.115.0/24': {
                                        'metric': 40,
                                        'up_down': 'U',
                                    },
                                    '10.23.115.0/24': {
                                        'metric': 40,
                                        'up_down': 'U',
                                    },
                                },
                                'mt_ipv6_prefix': {
                                    '2001:3:3:3::3/128': {
                                        'metric': 1,
                                        'topo_id': 2,
                                        'up_down': 'U',
                                        'ext_origin': 'I',
                                    },
                                    '2001:10:13:115::/64': {
                                        'metric': 40,
                                        'topo_id': 2,
                                        'up_down': 'U',
                                        'ext_origin': 'I',
                                    },
                                    '2001:10:23:115::/64': {
                                        'metric': 40,
                                        'topo_id': 2,
                                        'up_down': 'U',
                                        'ext_origin': 'I',
                                    },
                                },
                                'digest_offset': 0,
                            },
                        },
                        2: {
                            'R1_xe.00-00': {
                                'lsp_id': 'R1_xe.00-00',
                                'sequence': '0x000007CB',
                                'checksum': '0x25D3',
                                'lifetime': 908,
                                'attach_bit': 0,
                                'p_bit': 0,
                                'overload_bit': 0,
                                't_bit': 3,
                                'lsp_status': '',
                                'instance': '0x000007C6',
                                'area_address': '49.0001',
                                'nlpid': '0xCC 0x8E',
                                'mt_entries': {
                                    0: {
                                        'att': 0,
                                        'ol': 0,
                                    },
                                    2: {
                                        'att': 0,
                                        'ol': 0,
                                    },
                                },
                                'hostname': 'R1_xe',
                                'length': 5,
                                'extended_is_neighbor': {
                                    'R1_xe.02': {
                                        'neighbor_id': 'R1_xe.02',
                                        'metric': 10,
                                    },
                                },
                                'mt_is_neighbor': {
                                    'R1_xe.02': {
                                        'neighbor_id': 'R1_xe.02',
                                        'metric': 10,
                                        'topo_id': 2,
                                    },
                                },
                                'ip_address': '10.13.115.1',
                                'extended_ip': {
                                    '10.12.115.0/24': {
                                        'metric': 10,
                                        'up_down': 'U',
                                        'sub_tlv_length': 1,
                                        'sub_tlv_type': 4,
                                    },
                                    '10.13.115.0/24': {
                                        'metric': 10,
                                        'up_down': 'U',
                                        'sub_tlv_length': 1,
                                        'sub_tlv_type': 4,
                                    },
                                    '10.23.115.0/24': {
                                        'metric': 50,
                                        'up_down': 'U',
                                        'sub_tlv_length': 1,
                                        'sub_tlv_type': 4,
                                    },
                                },
                                'ipv6_address': '2001:10:13:115::1',
                                'mt_ipv6_prefix': {
                                    '2001:10:12:115::/64': {
                                        'metric': 10,
                                        'topo_id': 2,
                                        'up_down': 'U',
                                        'ext_origin': 'I',
                                        'sub_tlv_length': 1,
                                        'sub_tlv_type': 4,
                                    },
                                    '2001:10:13:115::/64': {
                                        'metric': 10,
                                        'topo_id': 2,
                                        'up_down': 'U',
                                        'ext_origin': 'I',
                                        'sub_tlv_length': 1,
                                        'sub_tlv_type': 4,
                                    },
                                    '2001:10:23:115::/64': {
                                        'metric': 50,
                                        'topo_id': 2,
                                        'up_down': 'U',
                                        'ext_origin': 'I',
                                        'sub_tlv_length': 1,
                                        'sub_tlv_type': 4,
                                    },
                                },
                                'digest_offset': 0,
                            },
                            'R1_xe.02-00': {
                                'lsp_id': 'R1_xe.02-00',
                                'sequence': '0x000007C6',
                                'checksum': '0x27D9',
                                'lifetime': 1174,
                                'attach_bit': 0,
                                'p_bit': 0,
                                'overload_bit': 0,
                                't_bit': 3,
                                'lsp_status': '',
                                'instance': '0x000007C5',
                                'extended_is_neighbor': {
                                    'R1_xe.00': {
                                        'neighbor_id': 'R1_xe.00',
                                        'metric': 0,
                                    },
                                    'R3_nx.00': {
                                        'neighbor_id': 'R3_nx.00',
                                        'metric': 0,
                                    },
                                },
                                'digest_offset': 0,
                            },
                            'R3_nx.00-00': {
                                'lsp_id': 'R3_nx.00-00',
                                'sequence': '0x00000B06',
                                'checksum': '0x6EBD',
                                'lifetime': 1136,
                                'attach_bit': 0,
                                'p_bit': 0,
                                'overload_bit': 0,
                                't_bit': 3,
                                'lsp_status': '*',
                                'instance': '0x00000B06',
                                'area_address': '49.0001',
                                'nlpid': '0xCC 0x8E',
                                'router_id': '10.36.3.3',
                                'ip_address': '10.36.3.3',
                                'mt_entries': {
                                    2: {
                                        'att': 0,
                                        'ol': 0,
                                    },
                                    0: {
                                        'att': 0,
                                        'ol': 0,
                                    },
                                },
                                'hostname': 'R3_nx',
                                'length': 5,
                                'mt_is_neighbor': {
                                    'R3_nx.00': {
                                        'neighbor_id': 'R1_xe.02',
                                        'metric': 40,
                                        'topo_id': 2,
                                    },
                                },
                                'extended_is_neighbor': {
                                    'R1_xe.02': {
                                        'neighbor_id': 'R1_xe.02',
                                        'metric': 40,
                                    },
                                },
                                'extended_ip': {
                                    '10.36.3.3/32': {
                                        'metric': 1,
                                        'up_down': 'U',
                                    },
                                    '10.13.115.0/24': {
                                        'metric': 40,
                                        'up_down': 'U',
                                    },
                                    '10.23.115.0/24': {
                                        'metric': 40,
                                        'up_down': 'U',
                                    },
                                },
                                'mt_ipv6_prefix': {
                                    '2001:3:3:3::3/128': {
                                        'metric': 1,
                                        'topo_id': 2,
                                        'up_down': 'U',
                                        'ext_origin': 'I',
                                    },
                                    '2001:10:13:115::/64': {
                                        'metric': 40,
                                        'topo_id': 2,
                                        'up_down': 'U',
                                        'ext_origin': 'I',
                                    },
                                    '2001:10:23:115::/64': {
                                        'metric': 40,
                                        'topo_id': 2,
                                        'up_down': 'U',
                                        'ext_origin': 'I',
                                    },
                                },
                                'digest_offset': 0,
                            },
                        },
                    },
                },
            },
        },
    },
}
