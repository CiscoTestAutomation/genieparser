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
                        'proxy_itr_rloc': '3110:3110:3110:3110:3110:3110:3110:3110',
                        'local_rloc_last_resort': '3110:3110:3110:3110:3110:3110:3110:3110',
                        'solicit_map_request': 'accept and process',
                        'max_smr_per_map_cache': '8 more specifics',
                        'multiple_smr_supression_time': 2
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
                        'role': True
                    },
                    'site_registration_limit': 0,
                    'xtr_id': '0x0F305B2B-0x8B49D44B-0xE85E1044-0xD02ADB68',
                    'site_id': 'unspecified',
                    'locator_status_algorithms': {
                        'rloc_probe_algorithm': 'disabled',
                        'rloc_probe_on_route_change': False,
                        'rloc_probe_member_change': 'disabled',
                        'lsb_reports': 'process',
                        'ipv4_rloc_min_mask_len': 0,
                        'ipv6_rloc_min_mask_len': 128
                    },
                    'map_cache': {
                        'static_mappings': 1,
                        'size': 2,
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
                        'total_database_mapping': 2,
                        'static_database': {
                            'size': 0,
                            'limit': 4294967295
                        },
                        'dynamic_database': {
                            'size': 2,
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
                        'map_cache': 0,
                        'rib': 0,
                        'database': 0,
                        'prefix_list': 0
                    },
                    'site_reg_entries_exported': {
                        'map_cache': 0,
                        'rib': 0
                    },
                    'encapsulation_type': 'vxlan',
                    'etr_map_servers': {
                        'found': True,
                        '3120:3120:3120:3120:3120:3120:3120:3120': {
                            'last_map_register': {
                                'timestamp': '00:01:08',
                                'transport_state': 'TCP'
                            }
                        },
                        '3130:3130:3130:3130:3130:3130:3130:3130': {
                            'last_map_register': {
                                'timestamp': '00:00:09',
                                'transport_state': 'UDP'
                            }
                        },
                        '3140:3140:3140:3140:3140:3140:3140:3140': {
                            'last_map_register': {
                                'timestamp': '00:00:09',
                                'transport_state': 'UDP'
                            }
                        }
                    },
                    'itr_map_resolvers': {
                        'found': True,
                        '3120:3120:3120:3120:3120:3120:3120:3120': {
                            'reachable': True
                        },
                        '3130:3130:3130:3130:3130:3130:3130:3130': {
                            'reachable': True
                        },
                        '3140:3140:3140:3140:3140:3140:3140:3140': {
                            'reachable': True
                        }
                    }
                }
            }
        }
    }
}
