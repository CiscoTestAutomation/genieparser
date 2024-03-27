expected_output = {
    'lisp_id': {
        0: {
            'instance_id': {
                4100: {
                    'eid_prefixes': {
                        '2001:192:168:1::71/128': {
                            'first_published': '00:00:04',
                            'last_published': '00:00:04',
                            'state': 'complete',
                            'exported_to': ['local-eid, map-cache, RIB'],
                            'publishers': {
                                '100.78.78.78:4342': {
                                    'port': 4342,
                                    'last_published': '00:00:04',
                                    'ttl': '1d00h',
                                    'publisher_epoch': 0,
                                    'entry_epoch': 0,
                                    'entry_state': 'complete',
                                    'xtr_id': '0xF4FBA727-0x1D32915D-0x6A2D6A61-0x8FC142D2',
                                    'site_id': 'unspecified',
                                    'domain_id': '1',
                                    'multihoming_id': '1',
                                    'sgt': 100,
                                    'locators': {
                                        '100.88.88.88': {
                                            'priority': 10,
                                            'weight': 50,
                                            'state': 'up',
                                            'encap_iid': '-',
                                            'rdp': '[1]'
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
                                '100.77.77.77:4342': {
                                    'port': 4342,
                                    'last_published': '00:00:04',
                                    'ttl': '1d00h',
                                    'publisher_epoch': 0,
                                    'entry_epoch': 0,
                                    'entry_state': 'complete',
                                    'xtr_id': '0xF4FBA727-0x1D32915D-0x6A2D6A61-0x8FC142D2',
                                    'site_id': 'unspecified',
                                    'domain_id': '1',
                                    'multihoming_id': '1',
                                    'sgt': 100,
                                    'locators': {
                                        '100.88.88.88': {
                                            'priority': 10,
                                            'weight': 50,
                                            'state': 'up',
                                            'encap_iid': '-',
                                            'rdp': '[1]'
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
                                    'last_published': '00:00:04',
                                    'ttl': '1d00h',
                                    'publisher_epoch': 0,
                                    'entry_epoch': 0,
                                    'entry_state': 'complete',
                                    'xtr_id': '0x97C99A83-0x7BF5C550-0x921EE140-0xC495F7FB',
                                    'site_id': 'unspecified',
                                    'domain_id': '1',
                                    'multihoming_id': 'unspecified',
                                    'sgt': 100,
                                    'locators': {
                                        '100.11.11.11': {
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
                                    'last_published': '00:00:04',
                                    'ttl': '1d00h',
                                    'publisher_epoch': 0,
                                    'entry_epoch': 0,
                                    'entry_state': 'complete',
                                    'xtr_id': '0x97C99A83-0x7BF5C550-0x921EE140-0xC495F7FB',
                                    'site_id': 'unspecified',
                                    'domain_id': '1',
                                    'multihoming_id': 'unspecified',
                                    'sgt': 100,
                                    'locators': {
                                        '100.11.11.11': {
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
                                '100.11.11.11*': {
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
                                '100.88.88.88': {
                                    'priority': 10,
                                    'weight': 50,
                                    'state': 'up',
                                    'encap_iid': '-',
                                    'rdp_len': 1,
                                    'src_add': '100.78.78.78',
                                    'publishers': {
                                        '100.78.78.78': {
                                            'priority': 10,
                                            'weight': 50,
                                            'state': 'up',
                                            'encap_iid': '-',
                                            'rdp_len': 1
                                        }
                                    }
                                },
                                '100.99.99.99': {
                                    'priority': 10,
                                    'weight': 50,
                                    'state': 'up',
                                    'encap_iid': '-',
                                    'rdp_len': 1,
                                    'src_add': '100.78.78.78',
	                            'publishers': {
                                        '100.78.78.78': {
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