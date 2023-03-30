expected_output = {
    'lisp_id': {
        0: {
            'locator_table': 'default',
            'itr': {
                'enabled': False,
                'proxy_itr_router': True,
                'proxy_itr_rloc': '11:11:11:11::',
                'local_rloc_last_resort': '*** NOT FOUND ***',
                'use_proxy_etr_rloc': ['66:66:66:66::'],
                'solicit_map_request': 'accept and process',
                'max_smr_per_map_cache': '8 more specifics',
                'multiple_smr_supression_time': 20
                },
            'etr': {
                'enabled': True,
                'proxy_etr_router': False,
                'accept_mapping_data': 'disabled, verify disabled',
                'map_cache_ttl': '1d00h'
                },
            'nat_traversal_router': False,
            'mobility_first_hop_router': 'disabled',
            'map_server': {
                'enabled': False
                },
            'map_resolver': {
                'enabled': False
                },
            'mr_use_petr': {
                'role': 'disabled'
                },
            'first_packet_petr': {
                'role': 'disabled'
                },
            'multiple_ip_per_mac': False,
            'delegated_database_tree': 'disabled',
            'mcast_flood_access_tunnel': False,
            'pub_sub': {
                'role': True,
                'publishers': ['44:44:44:44::']
                },
            'map_resolvers': {
                '44:44:44:44::': {
                    'mr_address': '44:44:44:44::',
                    'prefix_list': '200:200:200:200::'
                    }
                },
            'mapping_servers': {
                '44:44:44:44::': {
                    'ms_address': '44:44:44:44::',
                    'prefix_list': '200:200:200:200::'
                    }
                },
            'xtr_id': '0x50E5AAE2-0xDBB7E2DF-0x761B5EE7-0xE174F775',
            'site_id': 'unspecified',
            'locator_status_algorithms': {
                'rloc_probe_algorithm': 'disabled',
                'rloc_probe_on_route_change': False,
                'rloc_probe_member_change': 'disabled',
                'lsb_reports': 'process',
                'ipv4_rloc_min_mask_len': 0,
                'ipv6_rloc_min_mask_len': 0
                },
            'map_cache': {
                'limit': 4294967295,
                'activity_check_period': 60,
                'persistent': 'disabled'
                },
            'database': {
                'dynamic_database_limit': 4294967295
                }
            }
        }
    } 
