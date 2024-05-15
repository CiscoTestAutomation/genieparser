expected_output = {
    'lisp_id': {
        0: {
            'instance_id': {
                4100: {
                    'eid_prefixes': {
                        '192.168.1.0/24': {
                            'first_published': '00:05:30',
                            'last_published': '00:05:30',
                            'state': 'complete',
                            'exported_to': ['map-cache, RIB'],
                            'publishers': {
                                '100.44.44.44:4342': {
                                    'port': 4342,
                                    'last_published': '00:05:30',
                                    'ttl': 'never',
                                    'publisher_epoch': 0,
                                    'entry_epoch': 0,
                                    'entry_state': 'complete',
                                    'xtr_id': '0xB2CFA627-0xBFCAF2C5-0x05E0CCBB-0x56D0C962',
                                    'site_id': 'unspecified',
                                    'domain_id': '1',
                                    'multihoming_id': 'unspecified',
                                    'locators': {
                                        '100.154.154.154': {
                                            'priority': 10,
                                            'weight': 50,
                                            'state': 'up',
                                            'encap_iid': '-',
                                            'rdp': '[-]'
                                        }
                                    }
                                },
                                '100.55.55.55:4342': {
                                    'port': 4342,
                                    'last_published': '00:05:30',
                                    'ttl': 'never',
                                    'publisher_epoch': 0,
                                    'entry_epoch': 0,
                                    'entry_state': 'complete',
                                    'xtr_id': '0xB2CFA627-0xBFCAF2C5-0x05E0CCBB-0x56D0C962',
                                    'site_id': 'unspecified',
                                    'domain_id': '1',
                                    'multihoming_id': 'unspecified',
                                    'locators': {
                                        '100.154.154.154': {
                                            'priority': 10,
                                            'weight': 50,
                                            'state': 'up',
                                            'encap_iid': '-',
                                            'rdp': '[-]'
                                        }
                                    }
                                }
                            },
                            'merged_locators': {
                                '100.154.154.154*': {
                                    'priority': 10,
                                    'weight': 50,
                                    'state': 'up',
                                    'encap_iid': '-',
                                    'rdp_len': 0,
                                    'src_add': '100.44.44.44',
                                    'publishers': {
                                        '100.44.44.44': {
                                            'priority': 10,
                                            'weight': 50,
                                            'state': 'up',
                                            'encap_iid': '-',
                                            'rdp_len': 0
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