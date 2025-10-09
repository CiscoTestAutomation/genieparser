expected_output = {
    'lisp_id': {
        0: {
            'instance_id': {
                11: {
                    'eid_prefixes': {
                        '::/0': {
                            'exported_to': ['none'],
                            'first_published': '00:05:08',
                            'last_published': '00:04:52',
                            'merged_locators': {
                                '1:3:1::1': {
                                    'encap_iid': '-',
                                    'priority': 1,
                                    'publishers': {
                                        '1:2:1::1': {
                                            'encap_iid': '-',
                                            'priority': 1,
                                            'rdp_len': '0',
                                            'selected': False,
                                            'state': 'up',
                                            'weight': 50
                                        },
                                        '4:2:1::1': {
                                            'encap_iid': '-',
                                            'priority': 1,
                                            'rdp_len': '1',
                                            'selected': False,
                                            'state': 'up',
                                            'weight': 50
                                        }
                                    },
                                    'rdp_len': '1',
                                    'src_add': '4:2:1::1',
                                    'state': 'up',
                                    'weight': 50
                                },
                                '1:3:2::1': {
                                    'encap_iid': '-',
                                    'priority': 1,
                                    'publishers': {
                                        '1:2:1::1': {
                                            'encap_iid': '-',
                                            'priority': 1,
                                            'rdp_len': '0',
                                            'selected': False,
                                            'state': 'up',
                                            'weight': 50
                                        },
                                        '4:2:1::1': {
                                            'encap_iid': '-',
                                            'priority': 1,
                                            'rdp_len': '1',
                                            'selected': False,
                                            'state': 'up',
                                            'weight': 50
                                        }
                                    },
                                   'rdp_len': '1',
                                   'src_add': '4:2:1::1',
                                   'state': 'up',
                                   'weight': 50
                                },
                                '2:5:1::1': {
                                    'encap_iid': '-',
                                    'priority': 1,
                                    'publishers': {
                                        '4:2:1::1': {
                                            'encap_iid': '-',
                                            'priority': 1,
                                            'rdp_len': '1',
                                            'selected': False,
                                            'state': 'up',
                                            'weight': 100
                                        }
                                    },
                                    'rdp_len': '1',
                                    'src_add': '4:2:1::1',
                                    'state': 'up',
                                    'weight': 100
                                }
                            },
                            'publishers': {
                                '1:2:1::1.4342': {
                                    'domain_id': '1',
                                    'entry_epoch': 0,
                                    'entry_state': 'unknown-eid-forward',
                                    'last_published': '00:05:08',
                                    'locators': {
                                        '1:3:1::1': {
                                            'domain_id': 1,
                                            'encap_iid': '-',
                                            'metric': '-',
                                            'multihoming_id': 11,
                                            'priority': 1,
                                            'state': 'up',
                                            'weight': 50
                                        },
                                        '1:3:2::1': {
                                            'domain_id': 1,
                                            'encap_iid': '-',
                                            'metric': '0',
                                            'multihoming_id': 11,
                                            'priority': 1,
                                            'state': 'up',
                                            'weight': 50
                                        }
                                    },
                                    'multihoming_id': '11',
                                    'port': 4342,
                                    'publisher_epoch': 0,
                                    'site_id': 'unspecified',
                                    'ttl': 'never',
                                    'xtr_id': '0xE5C0A419-0x2B4D3BDF-0xEE3A0DCA-0x441F597F'
                                },
                                '4:2:1::1.4342': {
                                    'domain_id': '1',
                                    'entry_epoch': 0,
                                    'entry_state': 'unknown-eid-forward',
                                    'last_published': '00:04:52',
                                    'locators': {
                                        '1:3:1::1': {
                                            'domain_id': 1,
                                            'encap_iid': '-',
                                            'metric': '-',
                                            'multihoming_id': 11,
                                            'priority': 1,
                                            'state': 'up',
                                            'weight': 50
                                        },
                                        '1:3:2::1': {
                                            'domain_id': 1,
                                            'encap_iid': '-',
                                            'metric': '-',
                                            'multihoming_id': 11,
                                            'priority': 1,
                                            'state': 'up',
                                            'weight': 50
                                        },
                                        '2:5:1::1': {
                                            'domain_id': 2,
                                            'encap_iid': '-',
                                            'metric': '0',
                                            'multihoming_id': 22,
                                            'priority': 1,
                                            'state': 'up',
                                            'weight': 100
                                        }
                                    },
                                    'multihoming_id': '11',
                                    'port': 4342,
                                    'publisher_epoch': 0,
                                    'site_id': 'unspecified',
                                    'ttl': 'never',
                                    'xtr_id': '0xE5C0A419-0x2B4D3BDF-0xEE3A0DCA-0x441F597F'
                                }
                            },
                            'state': 'unknown-eid-forward'
                        }
                    }
                }
            }
        }
    }
}