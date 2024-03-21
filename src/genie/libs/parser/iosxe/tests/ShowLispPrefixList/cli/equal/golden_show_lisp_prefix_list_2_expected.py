expected_output = {
    'lisp_id': {
        0: {
            'prefix_list_name': {
                'site2list': {
                    'number_of_entries': 1,
                    'users': [
                        { 'import_publication': ' ' },
                        { 'itr_map_resolver': '3130:3130:3130:3130:3130:3130:3130:3130' },
                        { 'itr_map_resolver': '3120:3120:3120:3120:3120:3120:3120:3120' },
                        { 'import_publication': ' ' },
                        { 'itr_map_resolver': '3130:3130:3130:3130:3130:3130:3130:3130' },
                        { 'itr_map_resolver': '3120:3120:3120:3120:3120:3120:3120:3120' },
                        { 'itr_map_resolver': '3130:3130:3130:3130:3130:3130:3130:3130' },
                        { 'itr_map_resolver': '3120:3120:3120:3120:3120:3120:3120:3120' },
                    ],
                    'prefix_list_users': {
                        'instance_id': {
                            10: {
                                'address_family': {
                                    'MAC': {
                                        'users': {
                                            'itr_map_resolver': {
                                                'address': [
                                                    '3130:3130:3130:3130:3130:3130:3130:3130',
                                                    '3120:3120:3120:3120:3120:3120:3120:3120'
                                                ]
                                            }
                                        }
                                    }
                                }
                            },
                            101: {
                                'address_family': {
                                    'IPv6': {
                                        'users': {
                                            'import_publication': {},
                                            'itr_map_resolver': {
                                                'address': [
                                                    '3130:3130:3130:3130:3130:3130:3130:3130',
                                                    '3120:3120:3120:3120:3120:3120:3120:3120'
                                                ]
                                            }
                                        }
                                    }
                                }
                            },
                            5000: {
                                'address_family': {
                                    'IPv6': {
                                        'users': {
                                            'import_publication': {},
                                            'itr_map_resolver': {
                                                'address': [
                                                    '3130:3130:3130:3130:3130:3130:3130:3130',
                                                    '3120:3120:3120:3120:3120:3120:3120:3120'
                                                ]
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                    'entries': {
                        '2001:1820:1680:2000::/64': {
                            'sources': 'static, publication',
                            'source_list': ['static', 'publication'],
                            'first_added': '00:01:06',
                            'last_verified_by': 'by publication',
                            'last_verified': '00:00:00',
                            'number_of_publication_sources': 2
                        }
                    }
                }
            }
        }
    }
}
