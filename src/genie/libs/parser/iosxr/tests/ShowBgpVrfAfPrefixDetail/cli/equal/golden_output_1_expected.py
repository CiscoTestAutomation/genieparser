expected_output = {
    'vrf': {
        'SRV6_L3VPN_BE': {
            'address_family': {
                'ipv6_unicast': {
                    'prefix': 'fd00::3/128',
                    'rd': '100:1',
                    'last_modified': 'Apr 10 04:42:45.519 for 2d01h',
                    'paths': {
                        'total_available_paths': 2,
                        'best_path': 1,
                        'path': {
                            '1': {
                                'advertised_peer_ce': 'fd00:ffff:100:11::2',
                                'as_path': {
                                    '65535': {
                                        'bgp_peer_neighbor_ip': {
                                            'fc00:a000:2000::3': {
                                                'metric': 30,
                                                'bgp_peer_neighbor_ip': 'fc00:a000:2000::3',
                                                'origin_neighbors_ip': 'fc00:a000:1000::11',
                                                'origin_router_id': '10.0.0.3',
                                                'received_label': '0xe0030',
                                                'origin_metric': 0,
                                                'localpref': 100,
                                                'origin_codes': 'i',
                                                'group_best': 'group-best',
                                                'import_candidate': 'import-candidate',
                                                'imported': 'imported',
                                                'status_codes': '*>i',
                                                'received_path_id': 0,
                                                'local_path_id': 1,
                                                'version': 181,
                                                'extended_community': 'RT:100:1',
                                                'if_handle': '0x00000000',
                                                'originator': '10.0.0.3',
                                                'cluster_list': '10.0.0.11, 10.0.0.13',
                                                'psid_type': {
                                                    'L3': {
                                                        'psid_type': 'L3',
                                                        'subtlv_count': 1,
                                                        'r_value': '0x00',
                                                        'subtlv': {
                                                            't_value': '1',
                                                            'sid_value': 'fc00:c000:2003::',
                                                            'f_value': '0x00',
                                                            'r2_value': '0x00',
                                                            'behaviour': '62',
                                                            'r3_value': '0x00',
                                                            'sstlv_count': 1,
                                                            'subsubtlv': {
                                                                't': {
                                                                    '1': {
                                                                        'loc_blk': '32',
                                                                        'loc_node': '16',
                                                                        'func': '16',
                                                                        'arg': '0',
                                                                        'tpose_len': '16',
                                                                        'tpose_offset': '48'
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                },
                                                'source_afi': 'VPNv6 Unicast',
                                                'source_vrf': 'SRV6_L3VPN_BE',
                                                'source_rd': '100:1'
                                            }
                                        }
                                    }
                                }
                            },
                            '2': {
                                'as_path': {
                                    '65535': {
                                        'bgp_peer_neighbor_ip': {
                                            'fc00:a000:2000::3': {
                                                'metric': 30,
                                                'bgp_peer_neighbor_ip': 'fc00:a000:2000::3',
                                                'origin_neighbors_ip': 'fc00:a000:1000::12',
                                                'origin_router_id': '10.0.0.3',
                                                'received_label': '0xe0030',
                                                'origin_metric': 0,
                                                'localpref': 100,
                                                'origin_codes': 'i',
                                                'import_candidate': 'import-candidate',
                                                'imported': 'imported',
                                                'status_codes': '*i',
                                                'received_path_id': 0,
                                                'local_path_id': 0,
                                                'version': 0,
                                                'extended_community': 'RT:100:1',
                                                'if_handle': '0x00000000',
                                                'originator': '10.0.0.3',
                                                'cluster_list': '10.0.0.12, 10.0.0.13',
                                                'psid_type': {
                                                    'L3': {
                                                        'psid_type': 'L3',
                                                        'subtlv_count': 1,
                                                        'r_value': '0x00',
                                                        'subtlv': {
                                                            't_value': '1',
                                                            'sid_value': 'fc00:c000:2003::',
                                                            'f_value': '0x00',
                                                            'r2_value': '0x00',
                                                            'behaviour': '62',
                                                            'r3_value': '0x00',
                                                            'sstlv_count': 1,
                                                            'subsubtlv': {
                                                                't': {
                                                                    '1': {
                                                                        'loc_blk': '32',
                                                                        'loc_node': '16',
                                                                        'func': '16',
                                                                        'arg': '0',
                                                                        'tpose_len': '16',
                                                                        'tpose_offset': '48'
                                                                    }
                                                                }
                                                            }
                                                        }
                                                    }
                                                },
                                                'source_afi': 'VPNv6 Unicast',
                                                'source_vrf': 'SRV6_L3VPN_BE',
                                                'source_rd': '100:1'
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
