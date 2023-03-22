expected_output = {
    'lisp_id': {
        0: {
            'instance_id': {
                4100: {
                    'eid_prefixes': {
                        '2001:192:168:1::71/128': {
                            'first_published': '00:26:03',
                            'last_published': '00:26:02',
                            'state': 'complete',
                            'exported_to': ['map-cache'],
                            'publishers': {
                                '100.100.100.100:4342': {
                                    'port': 4342,
                                    'last_published': '00:26:02',
                                    'ttl': 'never',
                                    'publisher_epoch': 0,
                                    'entry_epoch': 0,
                                    'entry_state': 'complete',
                                    'xtr_id': '0x84FB57F7-0x5707006C-0x0869FD13-0xFDDB56D5',
                                    'site_id': 'unspecified',
                                    'domain_id': 'unset',
                                    'multihoming_id': 'unspecified',
                                    'locators': {
                                        '11.11.11.11': {
                                            'priority': 10,
                                            'weight': 10,
                                            'state': 'up',
                                            'encap_iid': '-'
                                            }
                                        }
                                    },
                                '1000:1000:1000:1000:1000:1000:1000:1000.4342': {
                                    'port': 4342,
                                    'last_published': '00:26:03',
                                    'ttl': 'never',
                                    'publisher_epoch': 0,
                                    'entry_epoch': 0,
                                    'entry_state': 'complete',
                                    'xtr_id': '0x84FB57F7-0x5707006C-0x0869FD13-0xFDDB56D5',
                                    'site_id': 'unspecified',
                                    'domain_id': 'unset',
                                    'multihoming_id': 'unspecified',
                                    'locators': {
                                        '1111:1111::': {
                                            'priority': 10,
                                            'weight': 10,
                                            'state': 'up',
                                            'encap_iid': '-'
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