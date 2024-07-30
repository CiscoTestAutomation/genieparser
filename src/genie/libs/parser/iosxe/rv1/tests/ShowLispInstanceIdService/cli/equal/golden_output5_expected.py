expected_output = {
    'lisp_id': {
        0: {
            'instance_id': {
                101: {
                    'locator_table': 'default',
                    'eid_table': 'vrf red',
                    'itr': {
                        'enabled': False,
                        'proxy_itr_router': True,
                        'proxy_itr_rloc': '21.21.21.21',
                        'local_rloc_last_resort': '21.21.21.21',
                        'solicit_map_request': 'accept and process',
                        'max_smr_per_map_cache': '8 more specifics',
                        'multiple_smr_supression_time': 2
                    },
                    'etr': {
                        'enabled': True,
                        'proxy_etr_router': True,
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
                        'role': 'disabled',
                    },
                    'first_packet_petr': {
                        'role': 'disabled'
                    },
                    'multiple_ip_per_mac': False,
                    'delegated_database_tree': 'disabled',
                    'mcast_flood_access_tunnel': False,
                    'pub_sub_eid': False,
                    'pub_sub': {
                        'role': True,
                        'publishers': ['4.4.4.4', '13.13.13.13', '199.199.199.199']
                    },
                    'site_registration_limit': 0,
                    'xtr_id': '0xCE3D96E6-0x19F0BD99-0x41D4411B-0xC0B63713',
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
                        'static_mappings': 0,
                        'size': 3,
                        'limit': 4294967295,
                        'imported_route': {
                            'count': 0,
                            'limit': 5000
                        },
                        'activity_check_period': 60,
                        'signal_supress': False,
                        'conservative_allocation': False,
                        'fib_updates': 'established',
                        'persistent': 'disabled',
                        'activity_tracking': True
                    },
                    'database': {
                        'total_database_mapping': 0,
                        'static_database': {
                            'size': 0,
                            'limit': 4294967295
                        },
                        'dynamic_database': {
                            'size': 0,
                            'limit': 4294967295
                        },
                        'route_import': {
                            'size': 0,
                            'limit': 5000
                        },
                        'import_site_reg': {
                            'size': 0,
                            'limit': 4294967295
                        },
                        'dummy_database': {
                            'size': 0,
                            'limit': 4294967295
                        },
                        'import_publication': {
                            'size': 0,
                            'limit': 4294967295
                        },
                        'proxy_database': {
                            'size': 0
                        },
                        'inactive': {
                            'size': 0
                        }
                    },
                    'publication_entries_exported': {
                        'map_cache': 3,
                        'rib': 3,
                        'database': 0,
                        'prefix_list': 0
                    },
                    'site_reg_entries_exported': {
                        'map_cache': 0,
                        'rib': 0
                    },
                    'encapsulation_type': 'lisp',
                    'etr_map_servers': {
                        'found': True,
                        '4.4.4.4': {
                            'last_map_register': {
                                'timestamp': 'never'
                            }
                        },
                        '13.13.13.13': {
                            'last_map_register': {
                                'timestamp': 'never'
                            }
                        }
                    },
                    'itr_map_resolvers': {
                        'found': True,
                        '4.4.4.4': {
                            'reachable': True
                        },
                        '13.13.13.13': {
                            'reachable': True
                        }
                    }
                }
            }
        }
    }
}
