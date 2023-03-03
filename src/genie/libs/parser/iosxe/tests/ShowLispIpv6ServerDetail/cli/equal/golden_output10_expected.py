expected_output = {
    'lisp_id': {
        0: {
            'site_name': {
                'site1': {
                    'instance_id': {
                        4100: {
                            'eid_prefix': {
                                '2001:192:168:1::/64': {
                                    'first_registered': '11:08:06',
                                    'last_registered': '11:08:02',
                                    'routing_table_tag': 0,
                                    'origin': 'Dynamic, more specific of ::/0',
                                    'merge_active': 'Yes',
                                    'proxy_reply': 'Yes',
                                    'skip_publication': 'No',
                                    'force_withdraw': 'No',
                                    'ttl': '1d00h',
                                    'state': 'complete',
                                    'extranet_iid': 'Unspecified',
                                    'registration_erros': {
                                        'authentication_failures': 0,
                                        'allowed_locators_mismatch': 0
                                        },
                                    'etr': {
                                        '100.99.99.99': {
                                            'last_registered': '11:08:02',
                                            'proxy_reply': True,
                                            'map_notify': True,
                                            'ttl': '1d00h',
                                            'nonce': '0xC8F70C9D-0xD812064E',
                                            'state': 'complete',
                                            'xtr_id': '0xD0C06D20-0xAF0B90F4-0x19419FE7-0x33E596CD',
                                            'domain_id': '1',
                                            'multihoming_id': '1',
                                            'port': 30343,
                                            'locators': {
                                                '100.99.99.99': {
                                                    'local': 'yes',
                                                    'state': 'up',
                                                    'priority': 10,
                                                    'weight': 50,
                                                    'scope': 'IPv4',
                                                    'rdp': '[-]'
                                                    }
                                                }
                                            }
                                        },
                                    'merged_locators': {
                                        '100.99.99.99': {
                                            'local': 'yes',
                                            'state': 'up',
                                            'priority': 10,
                                            'weight': 50,
                                            'scope': 'IPv4',
                                            'reg_etr': '100.99.99.99',
                                            'port': 30343,
                                            'rdp': '[-]'
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
