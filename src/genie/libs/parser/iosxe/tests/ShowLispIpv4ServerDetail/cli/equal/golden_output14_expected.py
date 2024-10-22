expected_output = {
    'lisp_id': {
        0: {
            'site_name': {
                'multisite': {
                    'instance_id': {
                        21: {
                            'eid_prefix': {
                                '21.2.1.0/24': {
                                    'first_registered': '03:05:56',
                                    'last_registered': '02:16:17',
                                    'routing_table_tag': 0,
                                    'origin': 'Configuration, accepting more specifics',
                                    'merge_active': 'Yes',
                                    'proxy_reply': 'Yes',
                                    'skip_publication': 'No',
                                    'force_withdraw': 'No',
                                    'ttl': '1d00h',
                                    'state': 'complete',
                                    'extranet_iid': 'Unspecified',
                                    'publish_mode': 'publish-extranet instance-id 11',
                                    'registration_erros': {
                                        'authentication_failures': 0,
                                        'allowed_locators_mismatch': 0
                                    },
                                    'etr': {
                                        '1.3.1.1': {
                                            'port': 49766,
                                            'last_registered': '02:16:17',
                                            'proxy_reply': True,
                                            'map_notify': True,
                                            'ttl': '1d00h',
                                            'state': 'complete',
                                            'nonce': '0x61A433D9-0x167DDB75',
                                            'xtr_id': '0x100DEB22-0x5216D4C1-0x29462F8C-0x7DB47015',
                                            'domain_id': '2',
                                            'multihoming_id': '11',
                                            'locators': {
                                                '1.3.1.1': {
                                                    'local': 'yes',
                                                    'state': 'up',
                                                    'priority': 1,
                                                    'weight': 50,
                                                    'scope': 'IPv4',
                                                    'rdp': '[2]'
                                                }
                                            }
                                        },
                                        '1.3.2.1': {
                                            'port': 55901,
                                            'last_registered': '02:16:17',
                                            'proxy_reply': True,
                                            'map_notify': True,
                                            'ttl': '1d00h',
                                            'state': 'complete',
                                            'nonce': '0x341D913F-0x878CD944',
                                            'xtr_id': '0x22D1E891-0x1F24D6FC-0x36171867-0xC1A7E20A',
                                            'domain_id': '2',
                                            'multihoming_id': '11',
                                            'locators': {
                                                '1.3.2.1': {
                                                    'local': 'yes',
                                                    'state': 'up',
                                                    'priority': 1,
                                                    'weight': 50,
                                                    'scope': 'IPv4',
                                                    'rdp': '[2]'
                                                }
                                            }
                                        }
                                    },
                                    'merged_locators': {
                                        '1.3.1.1': {
                                            'port': 49766,
                                            'local': 'yes',
                                            'state': 'up',
                                            'priority': 1,
                                            'weight': 50,
                                            'scope': 'IPv4',
                                            'reg_etr': '1.3.1.1',
                                            'rdp': '[2]'
                                        },
                                        '1.3.2.1': {
                                            'port': 55901,
                                            'local': 'yes',
                                            'state': 'up',
                                            'priority': 1,
                                            'weight': 50,
                                            'scope': 'IPv4',
                                            'reg_etr': '1.3.2.1',
                                            'rdp': '[2]'
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
