expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4_unicast': {
                    'prefix': '70.3.3.3/32',
                    'last_modified': 'May 11 06:39:45.020 for 05:29:21',
                    'paths': {
                        'total_available_paths': 1,
                        'best_path': 1,
                        'best_advertised_peer': '0.2',
                        'path': {
                            '1': {
                                'advertised_peer': '0.2',
                                'as_path': {
                                    '7000': {
                                        'bgp_peer_neighbor_ip': {
                                            '50.1.1.4': {
                                                'metric': 65537,
                                                'bgp_peer_neighbor_ip': '50.1.1.4',
                                                'origin_neighbors_ip': '50.1.1.4',
                                                'origin_router_id': '50.1.1.4',
                                                'origin_metric': 0,
                                                'localpref': 100,
                                                'best': True,
                                                'origin': 'IGP',
                                                'state': 'internal',
                                                'valid': True,
                                                'received_path_id': 0,
                                                'local_path_id': 0,
                                                'version': 85
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
