expected_output = {
    'lisp_id': {
        0: {
            'instance_id': {
                21: {
                    'eid_prefixes': {
                        '21.2.1.0/24': {
                            'first_published': '01:42:25',
                            'last_published': '01:42:25',
                            'state': 'complete',
                            'exported_to': ['local-eid, map-cache, RIB'],
                            'publishers': {
                                '1.2.1.1:4342': {
                                    'port': 4342,
                                    'last_published': '01:42:25',
                                    'ttl': 'never',
                                    'publisher_epoch': 1,
                                    'entry_epoch': 1,
                                    'entry_state': 'complete',
                                    'xtr_id': '0x100DEB22-0x5216D4C1-0x29462F8C-0x7DB47015',
                                    'site_id': 'unspecified',
                                    'domain_id': '2',
                                    'multihoming_id': '11',
                                    'publish_mode': 'publish-extranet instance-id 11',
                                    'locators': {
                                        '1.3.1.1': {
                                            'priority': 1,
                                            'weight': 50,
                                            'state': 'up',
                                            'encap_iid': '-',
                                            'rdp': '[2]'
                                        },
                                        '1.3.2.1': {
                                            'priority': 1,
                                            'weight': 50,
                                            'state': 'up',
                                            'encap_iid': '-',
                                            'rdp': '[2]'
                                        }
                                    }
                                },
                                '4.2.1.1:4342': {
                                    'port': 4342,
                                    'last_published': '01:42:25',
                                    'ttl': 'never',
                                    'publisher_epoch': 1,
                                    'entry_epoch': 1,
                                    'entry_state': 'complete',
                                    'xtr_id': '0xF6E8376A-0x2F286B28-0x7AFF278C-0x4B28E87F',
                                    'site_id': 'unspecified',
                                    'domain_id': '2',
                                    'multihoming_id': '22',
                                    'publish_mode': 'publish-extranet instance-id 11',
                                    'locators': {
                                        '2.5.1.1': {
                                            'priority': 1,
                                            'weight': 50,
                                            'state': 'up',
                                            'encap_iid': '-',
                                            'rdp': '[2]'
                                        }
                                    }
                                }
                            },
                            'merged_locators': {
                                '1.3.1.1': {
                                    'priority': 1,
                                    'weight': 50,
                                    'state': 'up',
                                    'encap_iid': '-',
                                    'rdp_len': 1,
                                    'src_add': '1.2.1.1',
                                    'publishers': {
                                        '1.2.1.1': {
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
                                    'src_add': '1.2.1.1',
                                    'publishers': {
                                        '1.2.1.1': {
                                            'priority': 1,
                                            'weight': 50,
                                            'state': 'up',
                                            'encap_iid': '-',
                                            'rdp_len': 1
                                        }
                                    }
                                },
                                '2.5.1.1*': {
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
