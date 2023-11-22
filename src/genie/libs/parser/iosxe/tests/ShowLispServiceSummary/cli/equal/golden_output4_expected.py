expected_output = {
    'lisp_router_instances': {
        0: {
            'lisp_router_instance_id': 0,
            'service': {
                'ipv4': {
                    'etr': {
                        'summary': {
                            'eid_tables_incomplete_map_cache_entries': 0,
                            'eid_tables_inconsistent_locators': 0,
                            'eid_tables_pending_map_cache_update_to_fib': 0,
                            'instance_count': 10,
                            'maximum_db_entries': 212992,
                            'maximum_map_cache_entries': 212992,
                            'total_db_entries': 1,
                            'total_db_entries_inactive': 0,
                            'total_eid_tables': 2,
                            'total_map_cache_entries': 10,
                        },
                    },
                    'virtual_network_ids': {
                        '4097': {
                            'cache_idle': '0.0%',
                            'cache_size': 2,
                            'db_no_route': 0,
                            'db_size': 0,
                            'incomplete': '0.0%',
                            'interface': 'LISP0.4097',
                            'lisp_role': {
                                'etr-pitr-petr': {
                                    'lisp_role_type': 'etr-pitr-petr',
                                },
                            },
                            'vrf': 'default',
                        },
                        '4099': {
                            'cache_idle': '0.0%',
                            'cache_size': 8,
                            'db_no_route': 0,
                            'db_size': 1,
                            'incomplete': '0.0%',
                            'interface': 'LISP0.4099',
                            'lisp_role': {
                                'etr-pitr-petr': {
                                    'lisp_role_type': 'etr-pitr-petr',
                                },
                            },
                            'vrf': 'BISNET_VN',
                        },
                    },
                },
            },
        },
    },
}
