expected_output = {
    'lisp_id': {
        0: {
            'instance_id': {
                21: {
                    'eid_prefixes': {
                        '21.1.2.0/24': {
                            'first_published': '01:47:21',
                            'last_published': '01:47:21',
                            'state': 'complete',
                            'exported_to': ['map-cache'],
                            'publishers': {
                                '4.2.1.1:4342': {
                                    'port': 4342,
                                    'last_published': '01:47:21',
                                    'ttl': 'never',
                                    'publisher_epoch': 1,
                                    'entry_epoch': 1,
                                    'entry_state': 'complete',
                                    'xtr_id': '0x100DEB22-0x5216D4C1-0x29462F8C-0x7DB47015',
                                    'site_id': 'unspecified',
                                    'domain_id': '1',
                                    'multihoming_id': '11',
                                    'publish_mode': 'no-extranet',
                                    'locators': {
                                        '1.3.1.1': {
                                            'priority': 1,
                                            'weight': 50,
                                            'state': 'up',
                                            'encap_iid': '-',
                                            'rdp': '[1]'
                                        },
                                        '1.3.2.1': {
                                            'priority': 1,
                                            'weight': 50,
                                            'state': 'up',
                                            'encap_iid': '-',
                                            'rdp': '[1]'
                                        }
                                    }
                                },
                                '1.2.1.1:4342': {
                                    'port': 4342,
                                    'last_published': '01:47:21',
                                    'ttl': 'never',
                                    'publisher_epoch': 1,
                                    'entry_epoch': 1,
                                    'entry_state': 'send-map-request',
                                    'xtr_id': 'unspecified',
                                    'site_id': 'unspecified',
                                    'domain_id': 'invalid',
                                    'multihoming_id': 'unspecified'
                                }
                            },
                            'merged_locators': {
                                '1.3.1.1': {
                                    'priority': 1,
                                    'weight': 50,
                                    'state': 'up',
                                    'encap_iid': '-',
                                    'rdp_len': 1,
                                    'src_add': '4.2.1.1',
                                    'publishers': {
                                        '4.2.1.1': {
                                            'priority': 1,
                                            'weight': 50,
                                            'state': 'up',
                                            'encap_iid': '-',
                                            'rdp_len': 1
                                        }
                                    }
                                },
                                '1.3.2.1': {
                                    'priority': 1,
                                    'weight': 50,
                                    'state': 'up',
                                    'encap_iid': '-',
                                    'rdp_len': 1,
                                    'src_add': '4.2.1.1',
                                    'publishers': {
                                        '4.2.1.1': {
                                            'priority': 1,
                                            'weight': 50,
                                            'state': 'up',
                                            'encap_iid': '-',
                                            'rdp_len': 1
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
