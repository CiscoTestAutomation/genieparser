expected_output = {
    'lisp_id': {
        0: {
            'instance_id': {
                4100: {
                    'eid_prefixes': {
                        '50.1.0.0/16': {
                            'first_published': '00:02:20',
                            'last_published': '00:02:20',
                            'state': 'complete',
                            'exported_to': ['local-eid, map-cache, RIB'],
                            'publishers': {
                                '100.78.78.78:4342': {
                                    'port': 4342,
                                    'last_published': '00:02:20',
                                    'ttl': 'never',
                                    'publisher_epoch': 1,
                                    'entry_epoch': 1,
                                    'entry_state': 'complete',
                                    'xtr_id': '0x16681EFF-0x07BE4091-0xA22D0471-0x3FBD218B',
                                    'site_id': 'unspecified',
                                    'domain_id': '1',
                                    'multihoming_id': '1',
                                    'routing_tag': 101,
                                    'locators': {
                                        '100.88.88.88': {
                                            'priority': 10,
                                            'weight': 50,
                                            'state': 'up',
                                            'encap_iid': '-',
                                            'rdp': '[1]',
                                            'affinity_id_x': 101
                                        },
                                        '100.110.110.110': {
                                            'priority': 6,
                                            'weight': 50,
                                            'state': 'up',
                                            'encap_iid': '-',
                                            'rdp': '[2]',
                                            'affinity_id_x': 201
                                        },
                                        '100.120.120.120': {
                                            'priority': 10,
                                            'weight': 50,
                                            'state': 'up',
                                            'encap_iid': '-',
                                            'rdp': '[3]',
                                            'affinity_id_x': 301
                                        },
                                        '100.133.133.133': {
                                            'priority': 10,
                                            'weight': 50,
                                            'state': 'up',
                                            'encap_iid': '-',
                                            'rdp': '[3]',
                                            'affinity_id_x': 311
                                        },
	                                '100.165.165.165': {
                                            'priority': 10,
                                            'weight': 50,
                                            'state': 'up',
                                            'encap_iid': '-',
                                            'rdp': '[2]',
                                            'affinity_id_x': 211
                                        }
                                    }
                                },
                                '100.77.77.77:4342': {
                                    'port': 4342,
                                    'last_published': '00:02:20',
                                    'ttl': 'never',
                                    'publisher_epoch': 1,
                                    'entry_epoch': 1,
                                    'entry_state': 'complete',
                                    'xtr_id': '0x16681EFF-0x07BE4091-0xA22D0471-0x3FBD218B',
                                    'site_id': 'unspecified',
                                    'domain_id': '1',
                                    'multihoming_id': '1',
                                    'routing_tag': 101,
                                    'locators': {
                                        '100.88.88.88': {
                                            'priority': 10,
                                            'weight': 50,
                                            'state': 'up',
                                            'encap_iid': '-',
                                            'rdp': '[1]',
                                            'affinity_id_x': 101
                                        },
                                        '100.110.110.110': {
                                            'priority': 6,
                                            'weight': 50,
                                            'state': 'up',
                                            'encap_iid': '-',
                                            'rdp': '[2]',
                                            'affinity_id_x': 201
                                        },
                                        '100.120.120.120': {
                                            'priority': 10,
                                            'weight': 50,
                                            'state': 'up',
                                            'encap_iid': '-',
                                            'rdp': '[3]',
                                            'affinity_id_x': 301
                                        },
                                        '100.133.133.133': {
                                            'priority': 10,
                                            'weight': 50,
                                            'state': 'up',
                                            'encap_iid': '-',
                                            'rdp': '[3]',
                                            'affinity_id_x': 311
                                        },
	                                '100.165.165.165': {
                                            'priority': 10,
                                            'weight': 50,
                                            'state': 'up',
                                            'encap_iid': '-',
                                            'rdp': '[2]',
                                            'affinity_id_x': 211
                                        }
                                    }
                                },
                                '100.44.44.44:4342': {
                                    'port': 4342,
                                    'last_published': '00:02:20',
                                    'ttl': 'never',
                                    'publisher_epoch': 1,
                                    'entry_epoch': 1,
                                    'entry_state': 'complete',
                                    'xtr_id': '0x16681EFF-0x07BE4091-0xA22D0471-0x3FBD218B',
                                    'site_id': 'unspecified',
                                    'domain_id': '1',
                                    'multihoming_id': '1',
                                    'routing_tag': 101,
                                    'locators': {
                                        '100.88.88.88': {
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
                                    'last_published': '00:02:20',
                                    'ttl': 'never',
                                    'publisher_epoch': 1,
                                    'entry_epoch': 1,
                                    'entry_state': 'complete',
                                    'xtr_id': '0x16681EFF-0x07BE4091-0xA22D0471-0x3FBD218B',
                                    'site_id': 'unspecified',
                                    'domain_id': '1',
                                    'multihoming_id': '1',
                                    'routing_tag': 101,
                                    'locators': {
                                        '100.88.88.88': {
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
                                    'priority': 10,
                                    'weight': 50,
                                    'state': 'up',
                                    'encap_iid': '-',
                                    'rdp_len': 1,
                                    'src_add': '100.78.78.78',
                                    'publishers': {
                                        '100.44.44.44': {
                                            'priority': 10,
                                            'weight': 50,
                                            'state': 'up',
                                            'encap_iid': '-',
                                            'rdp_len': 0
                                        },
                                        '100.78.78.78': {
                                            'priority': 10,
                                            'weight': 50,
                                            'state': 'up',
                                            'encap_iid': '-',
                                            'rdp_len': 1
                                        }
                                    }
                                },
                                '100.110.110.110*': {
                                    'priority': 6,
                                    'weight': 50,
                                    'state': 'up',
                                    'encap_iid': '-',
                                    'rdp_len': 1,
                                    'src_add': '100.78.78.78',
                                    'publishers': {
                                        '100.78.78.78': {
                                            'priority': 6,
                                            'weight': 50,
                                            'state': 'up',
                                            'encap_iid': '-',
                                            'rdp_len': 1
                                        }
                                    }
                                },
                                '100.120.120.120': {
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
                                '100.133.133.133': {
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
	                        '100.165.165.165': {
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