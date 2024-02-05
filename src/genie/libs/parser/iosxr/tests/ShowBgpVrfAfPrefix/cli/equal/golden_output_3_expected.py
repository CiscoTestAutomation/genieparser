expected_output = {
    'vrf': {
        'VRF_1': {
            'address_family': {
                'vpnv4_unicast': {
                    'prefix': '200.1.1.0/24',
                    'rd': '50.1.1.4:0',
                    'last_modified': 'Apr  4 10:33:32.365 for 13:57:38',
                    'paths': {
                        'total_available_paths': 2,
                        'best_path': 1,
                        'path': {
                            '1': {
                                'as_path': {
                                    'Local': {
                                        'bgp_peer_neighbor_ip': {
                                            '50.1.1.1': {
                                                'metric': 65538,
                                                'bgp_peer_neighbor_ip': '50.1.1.1',
                                                'origin_neighbors_ip': '50.1.1.8',
                                                'origin_router_id': '50.1.1.1',
                                                'received_label': '24017',
                                                'origin_metric': 0,
                                                'localpref': 100,
                                                'origin_codes': '?',
                                                'group_best': 'group-best',
                                                'import_candidate':'import-candidate',
                                                'imported':'imported',
                                                'status_codes': '*>i',
                                                'received_path_id': 0,
                                                'local_path_id': 0,
                                                'version': 41,
                                                'extended_community': 'RT:100:1001',
                                                'originator': '50.1.1.1',
                                                'cluster_list': '50.1.1.8',
                                                'source_afi': 'VPNv4 Unicast',
                                                'source_vrf': 'default',
                                                'source_rd': '50.1.1.1:0'
                                            }
                                        }
                                    }
                                }
                            },
                            '2': {
                                'as_path': {
                                    'Local': {
                                        'bgp_peer_neighbor_ip': {
                                            '50.1.1.5': {
                                                'metric': 65538,
                                                'bgp_peer_neighbor_ip': '50.1.1.5',
                                                'origin_neighbors_ip': '50.1.1.8',
                                                'origin_router_id': '50.1.1.5',
                                                'received_label': '24021',
                                                'origin_metric': 0,
                                                'localpref': 100,
                                                'origin_codes': '?',
                                                'backup':'backup',
                                                'add_path':'add-path',
                                                'import_candidate':'import-candidate',
                                                'imported':'imported',
                                                'status_codes': '*i',
                                                'received_path_id': 0,
                                                'local_path_id': 1,
                                                'version': 49,
                                                'extended_community': 'VRF Route Import:50.1.1.5:17 Source AS:100:0 RT:100:1001',
                                                'originator': '50.1.1.5',
                                                'cluster_list': '50.1.1.8',
                                                'source_afi': 'VPNv4 Unicast',
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
