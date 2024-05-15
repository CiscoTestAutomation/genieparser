expected_output = {
    'lisp_id': {
        0: {
            'instance_id': {
                4100: {
                    'eid_prefixes': {
                        '2001:192:168:1::/64': {
                            'first_published': '13:38:54',
                            'last_published': '13:35:53',
                            'state': 'complete',
                            'exported_to': ['prefix-list, RIB'],
                            'publishers': {
                                '100.77.77.77:4342': {
                                    'port': 4342,
                                    'last_published': '13:35:53',
                                    'ttl': 'never',
                                    'publisher_epoch': 0,
                                    'entry_epoch': 0,
                                    'entry_state': 'complete',
                                    'xtr_id': '0xA68BE4A7-0xBAC522DA-0x2C7C0C7C-0x62D298A1',
                                    'site_id': 'unspecified',
                                    'domain_id': '1',
                                    'multihoming_id': '1',
                                    'locators': {
                                        '100.88.88.88': {
                                            'priority': 10,
                                            'weight': 50,
                                            'state': 'up',
                                            'encap_iid': '-',
                                            'rdp': '[-]'
                                        },
                                        '100.99.99.99': {
                                            'priority': 10,
                                            'weight': 50,
                                            'state': 'up',
                                            'encap_iid': '-',
                                            'rdp': '[1]'
                                        }
                                    }
                                },
                                '100.78.78.78:4342': {
                                    'port': 4342,
                                    'last_published': '13:35:53',
                                    'ttl': 'never',
                                    'publisher_epoch': 0,
                                    'entry_epoch': 0,
                                    'entry_state': 'complete',
                                    'xtr_id': '0xA68BE4A7-0xBAC522DA-0x2C7C0C7C-0x62D298A1',
                                    'site_id': 'unspecified',
                                    'domain_id': '1',
                                    'multihoming_id': '1',
                                    'locators': {
                                        '100.88.88.88': {
                                            'priority': 10,
                                            'weight': 50,
                                            'state': 'up',
                                            'encap_iid': '-',
                                            'rdp': '[-]'
                                        },
                                        '100.99.99.99': {
                                            'priority': 10,
                                            'weight': 50,
                                            'state': 'up',
                                            'encap_iid': '-',
                                            'rdp': '[1]'
                                        }
                                    }
                                },
                                '100.44.44.44:4342': {
                                    'port': 4342,
                                    'last_published': '13:38:54',
                                    'ttl': 'never',
                                    'publisher_epoch': 0,
                                    'entry_epoch': 0,
                                    'entry_state': 'complete',
                                    'xtr_id': '0xD0C06D20-0xAF0B90F4-0x19419FE7-0x33E596CD',
                                    'site_id': 'unspecified',
                                    'domain_id': '1',
                                    'multihoming_id': '1',
                                    'locators': {
                                        '100.99.99.99': {
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
                                    'last_published': '13:38:54',
                                    'ttl': 'never',
                                    'publisher_epoch': 0,
                                    'entry_epoch': 0,
                                    'entry_state': 'complete',
                                    'xtr_id': '0xD0C06D20-0xAF0B90F4-0x19419FE7-0x33E596CD',
                                    'site_id': 'unspecified',
                                    'domain_id': '1',
                                    'multihoming_id': '1',
                                    'locators': {
                                        '100.99.99.99': {
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
                                '100.88.88.88': {
                                    'priority': 20,
                                    'weight': 90,
                                    'state': 'up',
                                    'encap_iid': '-',
                                    'rdp_len': 0,
                                    'src_add': '100.77.77.77',
                                    'publishers': {
                                        '100.77.77.77': {
                                            'priority': 20,
                                            'weight': 90,
                                            'state': 'up',
                                            'encap_iid': '-',
                                            'rdp_len': 0
                                        }
                                    }
                                },
                                '100.99.99.99*': {
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
                                },
                                '100.99.99.99': {
                                    'priority': 10,
                                    'weight': 50,
                                    'state': 'up',
                                    'encap_iid': '-',
                                    'rdp_len': 1,
                                    'src_add': '100.77.77.77',
	                            'publishers': {
                                        '100.77.77.77': {
                                            'priority': 10,
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