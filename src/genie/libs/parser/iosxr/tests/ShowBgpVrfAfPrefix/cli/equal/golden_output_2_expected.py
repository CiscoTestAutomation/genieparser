expected_output = {
    'vrf': {
        'VRF_1': {
            'address_family': {
                'ipv6_unicast': {
                    'prefix': '2000:90:45:1::/64',
                    'rd': '50.1.1.4:2',
                    'last_modified': 'Mar 27 02:45:53.105 for 1d16h',
                    'paths': {
                        'total_available_paths': 2,
                        'best_path': 1,
                        'path': {
                            '1': {
                                'as_path': {
                                    '5000': {
                                        'bgp_peer_neighbor_ip': {
                                            '50.1.1.1': {
                                                'metric': 4,
                                                'bgp_peer_neighbor_ip': '50.1.1.1',
                                                'origin_neighbors_ip': '50.1.1.8',
                                                'origin_router_id': 'bgp_neighbor',
                                                'received_label': '24026',
                                                'origin_metric': 0,
                                                'localpref': 100,
                                                'origin_codes': '?',
                                                'group_best': 'group-best',
                                                'import_candidate':'import-candidate',
                                                'imported':'imported',
                                                'status_codes': '*>i',
                                                'received_path_id': 0,
                                                'local_path_id': 0,
                                                'version': 720,
                                                'extended_community': 'RT:100:1001',
                                                'originator': '50.1.1.1',
                                                'cluster_list': '50.1.1.8',
                                                'source_afi': 'VPNv6 Unicast',
                                                'source_vrf': 'default',
                                                'source_rd': '50.1.1.1:0'
                                            }
                                        }
                                    }
                                }
                            },
                            '2': {
                                'as_path': {
                                    '5000': {
                                        'bgp_peer_neighbor_ip': {
                                            '50.1.1.5': {
                                                'metric': 4,
                                                'bgp_peer_neighbor_ip': '50.1.1.5',
                                                'origin_neighbors_ip': '50.1.1.8',
                                                'origin_router_id': '50.1.1.5',
                                                'received_label': '24024',
                                                'origin_metric': 0,
                                                'localpref': 100,
                                                'origin_codes': '?',
                                                'import_candidate':'import-candidate',
                                                'imported':'imported',
                                                'status_codes': '*i',
                                                'received_path_id': 0,
                                                'local_path_id': 0,
                                                'version': 0,
                                                'extended_community': 'RT:100:1001',
                                                'originator': '50.1.1.5',
                                                'cluster_list': '50.1.1.8',
                                                'source_afi': 'VPNv6 Unicast',
                                                'source_vrf': 'default',
                                                'source_rd': '50.1.1.5:0'
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