expected_output = {
    'vrf': {
        'VRF_1': {
            'address_family': {
                'ipv6_unicast': {
                    'prefix': '2000:90:11:1::/64',
                    'rd': '50.1.1.1:0',
                    'local_label': '24021',
                    'last_modified': 'Mar 31 12:40:50.327 for 2d16h',
                    'paths': {
                        'total_available_paths': 2,
                        'best_path': 1,
                        'path': {
                            '1': {
                                'advertised_peer_pe': '50.1.1.8',
                                'advertised_peer_ce': '2000:90:11:1::2',
                                'as_path': {
                                    'Local': {
                                        'bgp_peer_neighbor_ip': {
                                            '::': {
                                                'bgp_peer_neighbor_ip': '::',
                                                'origin_neighbors_ip': '::',
                                                'origin_router_id': '50.1.1.1',
                                                'origin_metric': 0,
                                                'localpref': 100,
                                                'weight': 32768,
                                                'origin_codes': '?',
                                                'group_best': 'group-best',
                                                'import_candidate':'import-candidate',
                                                'redistributed':'redistributed',
                                                'status_codes': '*>',
                                                'received_path_id': 0,
                                                'local_path_id': 0,
                                                'version': 17,
                                                'extended_community': 'RT:100:1001'
                                            }
                                        }
                                    }
                                }
                            },
                            '2': {
                                'as_path': {
                                    '5000': {
                                        'bgp_peer_neighbor_ip': {
                                            '2000:90:11:1::2': {
                                                'bgp_peer_neighbor_ip': '2000:90:11:1::2',
                                                'origin_neighbors_ip': '2000:90:11:1::2',
                                                'origin_router_id': '70.1.1.1',
                                                'origin_metric': 0,
                                                'localpref': 100,
                                                'origin_codes': '?',
                                                'group_best': 'group-best',
                                                'status_codes': '*',
                                                'received_path_id': 0,
                                                'local_path_id': 0,
                                                'version': 0,
                                                'extended_community': 'RT:100:1001'
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