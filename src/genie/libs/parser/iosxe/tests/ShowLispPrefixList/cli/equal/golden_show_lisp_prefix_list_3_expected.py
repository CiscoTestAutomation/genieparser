expected_output = {
    'lisp_id': {
        0: {
            'prefix_list_name': {
                'multisite': {
                    'number_of_entries': 0,
                    'users': [
                        { 'itr_map_resolver': '100.14.14.14' },
                        { 'itr_map_resolver': '100.13.13.13' },
                        { 'itr_map_resolver': '100.14.14.14' },
                        { 'itr_map_resolver': '100.13.13.13' },
                    ],
                    'prefix_list_users': {
                        'instance_id': {
                            101: {
                                'address_family': {
                                    'IPv4': {
                                        'users': {
                                            'itr_map_resolver': {
                                                'address': [
                                                    '100.14.14.14',
                                                    '100.13.13.13'
                                                ]
                                            }
                                        }
                                    },
                                    'IPv6': {
                                        'users': {
                                            'itr_map_resolver': {
                                                'address': [
                                                    '100.14.14.14',
                                                    '100.13.13.13'
                                                ]
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
