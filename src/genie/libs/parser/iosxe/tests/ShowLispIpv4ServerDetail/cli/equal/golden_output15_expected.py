expected_output = {
    'lisp_id': {
        0: {
            'site_name': {
                'multisite': {
                    'instance_id': {
                        21: {
                            'eid_prefix': {
                                '21.1.2.0/24': {
                                    'first_registered': '00:55:55',
                                    'last_registered': '00:55:50',
                                    'routing_table_tag': 0,
                                    'origin': 'Configuration, accepting more specifics',
                                    'merge_active': 'Yes',
                                    'proxy_reply': 'Yes',
                                    'skip_publication': 'No',
                                    'force_withdraw': 'No',
                                    'ttl': '1d00h',
                                    'state': 'complete',
                                    'extranet_iid': 'Unspecified',
                                    'publish_mode': 'no-extranet',
                                    'registration_erros': {
                                        'authentication_failures': 0,
                                        'allowed_locators_mismatch': 0
                                    },
                                    'etr': {
                                        '1.3.2.1': {
                                            'port': 29680,
                                            'last_registered': '00:55:50',
                                            'proxy_reply': True,
                                            'map_notify': True,
                                            'ttl': '1d00h',
                                            'state': 'complete',
                                            'nonce': '0x6FA5A401-0x3A73087D',
                                            'xtr_id': '0x9BF7AA03-0x9652F14E-0x7A1EB9D8-0x877EFCBE',
                                            'domain_id': '1',
                                            'multihoming_id': '11',
                                            'locators': {
                                                '1.3.2.1': {
                                                    'local': 'yes',
                                                    'state': 'up',
                                                    'priority': 1,
                                                    'weight': 50,
                                                    'scope': 'IPv4',
                                                    'rdp': '[1]'
                                                }
                                            }
                                        },
                                        '1.3.1.1': {
                                            'port': 25926,
                                            'last_registered': '00:55:50',
                                            'proxy_reply': True,
                                            'map_notify': True,
                                            'ttl': '1d00h',
                                            'state': 'complete',
                                            'nonce': '0x8339C1AF-0x60552A4E',
                                            'xtr_id': '0x66F7D145-0xFA746C63-0x55D793FC-0x8ABFFA90',
                                            'domain_id': '1',
                                            'multihoming_id': '11',
                                            'locators': {
                                                '1.3.1.1': {
                                                    'local': 'yes',
                                                    'state': 'up',
                                                    'priority': 1,
                                                    'weight': 50,
                                                    'scope': 'IPv4',
                                                    'rdp': '[1]'
                                                }
                                            }
                                        }
                                    },
                                    'merged_locators': {
                                        '1.3.1.1': {
                                            'port': 25926,
                                            'local': 'yes',
                                            'state': 'up',
                                            'priority': 1,
                                            'weight': 50,
                                            'scope': 'IPv4',
                                            'reg_etr': '1.3.1.1',
                                            'rdp': '[1]'
                                        },
                                        '1.3.2.1': {
                                            'port': 29680,
                                            'local': 'yes',
                                            'state': 'up',
                                            'priority': 1,
                                            'weight': 50,
                                            'scope': 'IPv4',
                                            'reg_etr': '1.3.2.1',
                                            'rdp': '[1]'
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
