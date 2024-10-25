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
                                            'metric': 0,
                                            'multihoming_id': 11,
                                            'priority': 1,
                                            'state': 'up',
                                            'weight': 50
                                        },
                                        '1:3:2::1': {
                                            'domain_id': 1,
                                            'encap_iid': '-',
                                            'metric': 0,
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
                                            'metric': 0,
                                            'multihoming_id': 11,
                                            'priority': 1,
                                            'state': 'up',
                                            'weight': 50
                                        },
                                        '1:3:2::1': {
                                            'domain_id': 1,
                                            'encap_iid': '-',
                                            'metric': 0,
                                            'multihoming_id': 11,
                                            'priority': 1,
                                            'state': 'up',
                                            'weight': 50
                                        },
                                        '2:5:1::1': {
                                            'domain_id': 2,
                                            'encap_iid': '-',
                                            'metric': 0,
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
                        },
                        '11:1:1::1/128': {
                            'exported_to': ['none'],
                            'first_published': '00:05:08',
                            'last_published': '00:04:54',
                            'merged_locators': {
                                '1:3:3::1': {
                                    'encap_iid': '-',
                                    'priority': 1,
                                    'publishers': {
                                        '1:2:1::1': {
                                            'encap_iid': '-',
                                            'priority': 1,
                                            'rdp_len': '0',
                                            'selected': True,
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
                                }
                            },
                            'publishers': {
                                '1:2:1::1.4342': {
                                    'domain_id': '1',
                                    'entry_epoch': 0,
                                    'entry_state': 'complete',
                                    'last_published': '00:05:08',
                                    'locators': {
                                        '1:3:3::1': {
                                            'encap_iid': '-',
                                            'priority': 1,
                                            'rdp': '[-]',
                                            'state': 'up',
                                            'weight': 50
                                        }
                                    },
                                    'multihoming_id': '11',
                                    'port': 4342,
                                    'publisher_epoch': 0,
                                    'site_id': 'unspecified',
                                    'ttl': 'never',
                                    'xtr_id': '0x82E42571-0x26EB3C24-0x8929C732-0xE539F297'
	                        },
                                '4:2:1::1.4342': {
                                    'domain_id': '1',
                                    'entry_epoch': 0,
                                    'entry_state': 'complete',
                                    'last_published': '00:04:54',
                                    'locators': {
                                        '1:3:3::1': {
                                            'encap_iid': '-',
                                            'priority': 1,
                                            'rdp': '[0]',
                                            'state': 'up',
                                            'weight': 50
                                        }
                                    },
                                    'multihoming_id': '11',
                                    'port': 4342,
                                    'publisher_epoch': 0,
                                    'site_id': 'unspecified',
                                    'ttl': 'never',
                                    'xtr_id': '0x82E42571-0x26EB3C24-0x8929C732-0xE539F297'
                                }
                            },
                            'state': 'complete'
                        },
                        '21:1:1::/96': {
                            'exported_to': ['map-cache, '
                                            'RIB'],
                            'first_published': '00:01:56',
                            'last_published': '00:01:56',
                            'merged_locators': {
                                '1:3:1::1': {
                                    'encap_iid': '21',
                                    'priority': 1,
                                    'publishers': {
                                        '1:2:1::1': {
                                            'encap_iid': '21',
                                            'priority': 1,
                                            'rdp_len': 'ext',
                                            'selected': False,
                                            'state': 'up',
                                            'weight': 50
                                        },
                                        '4:2:1::1': {
                                            'encap_iid': '21',
                                            'priority': 1,
                                            'rdp_len': 'ext',
                                            'selected': False,
                                            'state': 'up',
                                            'weight': 50
                                        }
                                    },
                                    'rdp_len': 'ext',
                                    'src_add': '4:2:1::1',
                                    'state': 'up',
                                    'weight': 50
                                },
                                '1:3:2::1': {
                                    'encap_iid': '21',
                                    'priority': 1,
                                    'publishers': {
	                                '1:2:1::1': {
                                            'encap_iid': '21',
                                            'priority': 1,
                                            'rdp_len': 'ext',
                                            'selected': True,
                                            'state': 'up',
                                            'weight': 50
                                        },
                                        '4:2:1::1': {
                                            'encap_iid': '21',
                                            'priority': 1,
                                            'rdp_len': 'ext',
                                            'selected': False,
                                            'state': 'up',
                                            'weight': 50
                                        }
                                    },
                                    'rdp_len': 'ext',
                                    'src_add': '4:2:1::1',
                                    'state': 'up',
                                    'weight': 50
                                }
                            },
                            'publishers': {
                                '1:2:1::1.4342': {
                                    'domain_id': 'extranet',
                                    'entry_epoch': 0,
                                    'entry_state': 'complete',
                                    'last_published': '00:01:56',
                                    'locators': {
                                        '1:3:1::1': {
                                            'encap_iid': '21',
                                            'priority': 1,
                                            'rdp': '[-]',
                                            'state': 'up',
                                            'weight': 50
                                        },
                                        '1:3:2::1': {
                                            'encap_iid': '21',
                                            'priority': 1,
                                            'rdp': '[-]',
                                            'state': 'up',
                                            'weight': 50
                                        }
                                    },
                                    'multihoming_id': 'unspecified',
                                    'port': 4342,
                                    'publish_mode': 'publish-extranet '
                                    'instance-id '
                                    '11',
                                    'publisher_epoch': 0,
                                    'sgt': 211,
                                    'site_id': 'unspecified',
                                    'ttl': 'never',
                                    'xtr_id': '0x6F2A92D0-0x145ECA8A-0xF1C24AB4-0xE8A4F310'
                                },
                                '4:2:1::1.4342': {
                                    'domain_id': 'extranet',
                                    'entry_epoch': 0,
                                    'entry_state': 'complete',
                                    'last_published': '00:01:56',
                                    'locators': {
                                        '1:3:1::1': {
                                            'encap_iid': '21',
                                            'priority': 1,
                                            'rdp': '[-]',
                                            'state': 'up',
                                            'weight': 50					    
                                        },
                                        '1:3:2::1': {
                                            'encap_iid': '21',
                                            'priority': 1,
                                            'rdp': '[-]',
                                            'state': 'up',
                                            'weight': 50
                                        }
                                    },
                                    'multihoming_id': 'unspecified',
                                    'port': 4342,
                                    'publish_mode': 'publish-extranet instance-id 11',
                                    'publisher_epoch': 0,
                                    'sgt': 211,
                                    'site_id': 'unspecified',
                                    'ttl': 'never',
                                    'xtr_id': '0x6F2A92D0-0x145ECA8A-0xF1C24AB4-0xE8A4F310'
                                }
                            },
                            'state': 'complete'
                        },
                        '21:1:2::/96': {
                            'exported_to': ['map-cache, '
                                            'RIB'],
                            'first_published': '00:01:56',
                            'last_published': '00:01:56',
                            'merged_locators': {
                                '1:3:1::1': {
                                    'encap_iid': '21',
                                    'priority': 1,
                                    'publishers': {
                                        '1:2:1::1': {
	                                    'encap_iid': '21',
                                            'priority': 1,
                                            'rdp_len': 'ext',
                                            'selected': False,
                                            'state': 'up',
                                            'weight': 50
                                        },
                                        '4:2:1::1': {
                                            'encap_iid': '21',
                                            'priority': 1,
                                            'rdp_len': 'ext',
                                            'selected': False,
                                            'state': 'up',
                                            'weight': 50
                                        }
                                    },
                                    'rdp_len': 'ext',
                                    'src_add': '4:2:1::1',
                                    'state': 'up',
                                    'weight': 50
                                },
                                '1:3:2::1': {
                                    'encap_iid': '21',
                                    'priority': 1,
                                    'publishers': {
                                        '1:2:1::1': {
                                            'encap_iid': '21',
                                            'priority': 1,
                                            'rdp_len': 'ext',
                                            'selected': True,
                                            'state': 'up',
                                            'weight': 50
                                        },
                                        '4:2:1::1': {
                                            'encap_iid': '21',
                                            'priority': 1,
                                            'rdp_len': 'ext',
                                            'selected': False,
                                            'state': 'up',
                                            'weight': 50
                                        }
                                    },
                                    'rdp_len': 'ext',
                                    'src_add': '4:2:1::1',
                                    'state': 'up',
                                    'weight': 50
                                }
                            },
                            'publishers': {
                                '1:2:1::1.4342': {
                                    'domain_id': 'extranet',
                                    'entry_epoch': 0,
                                    'entry_state': 'complete',
                                    'last_published': '00:01:56',
                                    'locators': {
                                        '1:3:1::1': {
                                            'encap_iid': '21',
                                            'priority': 1,
                                            'rdp': '[-]',
                                            'state': 'up',
                                            'weight': 50
                                        },
                                        '1:3:2::1': {
                                            'encap_iid': '21',
                                            'priority': 1,
                                            'rdp': '[-]',
                                            'state': 'up',
                                            'weight': 50
                                        }
                                    },
                                    'multihoming_id': 'unspecified',
                                    'port': 4342,
                                    'publish_mode': 'publish-extranet '
                                    'instance-id '
                                    '11',
                                    'publisher_epoch': 0,
                                    'sgt': 212,
                                    'site_id': 'unspecified',
                                    'ttl': 'never',
                                    'xtr_id': '0x6F2A92D0-0x145ECA8A-0xF1C24AB4-0xE8A4F310'
                                },
                                '4:2:1::1.4342': {
                                    'domain_id': 'extranet',
                                    'entry_epoch': 0,
                                    'entry_state': 'complete',
                                    'last_published': '00:01:56',
                                    'locators': {
                                        '1:3:1::1': {
                                            'encap_iid': '21',
                                            'priority': 1,
                                            'rdp': '[-]',
                                            'state': 'up',
                                            'weight': 50
                                        },
                                        '1:3:2::1': {
                                            'encap_iid': '21',
                                            'priority': 1,
                                            'rdp': '[-]',
                                            'state': 'up',
                                            'weight': 50
                                        }
                                    },
                                    'multihoming_id': 'unspecified',
                                    'port': 4342,
                                    'publish_mode': 'publish-extranet '
                                    'instance-id '
                                    '11',
                                    'publisher_epoch': 0,
                                    'sgt': 212,
                                    'site_id': 'unspecified',
                                    'ttl': 'never',
                                    'xtr_id': '0x6F2A92D0-0x145ECA8A-0xF1C24AB4-0xE8A4F310'
                                }
                            },
                            'state': 'complete'
                        },
                        '21:2:1::/96': {
                            'exported_to': ['map-cache, '
                                            'RIB'],
                            'first_published': '00:01:54',
                            'last_published': '00:01:54',
                            'merged_locators': {
                                '1:3:1::1': {
                                    'encap_iid': '21',
                                    'priority': 1,
                                    'publishers': {
                                        '1:2:1::1': {
                                            'encap_iid': '21',
                                            'priority': 1,
                                            'rdp_len': 'ext',
                                            'selected': False,
                                            'state': 'up',
                                            'weight': 50
                                        }
                                    },
                                    'rdp_len': 'ext',
                                    'src_add': '1:2:1::1',
                                    'state': 'up',
                                    'weight': 50
                                },
                                '2:5:1::1': {
                                    'encap_iid': '21',
                                    'priority': 1,
                                    'publishers': {
                                        '4:2:1::1': {
                                            'encap_iid': '21',
                                            'priority': 1,
                                            'rdp_len': 'ext',
                                            'selected': True,
                                            'state': 'up',
                                            'weight': 50
                                        }
                                    },
                                    'rdp_len': 'ext',
                                    'src_add': '4:2:1::1',
                                    'state': 'up',
                                    'weight': 50
                                }
                            },
                            'publishers': {
                                '1:2:1::1.4342': {
                                    'domain_id': 'extranet',
                                    'entry_epoch': 0,
                                    'entry_state': 'complete',
                                    'last_published': '00:01:54',
                                    'locators': {
                                        '1:3:1::1': {
                                            'encap_iid': '21',
                                            'priority': 1,
                                            'rdp': '[-]',
                                            'state': 'up',
                                            'weight': 50
                                        }
                                    },
                                   'multihoming_id': 'unspecified',
                                   'port': 4342,
                                   'publish_mode': 'publish-extranet '
                                   'instance-id '
                                   '11',
                                   'publisher_epoch': 0,
                                   'site_id': 'unspecified',
                                   'ttl': 'never',
                                   'xtr_id': '0xE5C0A419-0x2B4D3BDF-0xEE3A0DCA-0x441F597F'
                                },
                                '4:2:1::1.4342': {
                                    'domain_id': 'extranet',
                                    'entry_epoch': 0,
                                    'entry_state': 'complete',
                                    'last_published': '00:01:54',
                                    'locators': {
                                        '2:5:1::1': {
                                            'encap_iid': '21',
                                            'priority': 1,
                                            'rdp': '[-]',
                                            'state': 'up',
                                            'weight': 50
                                        }
                                    },
                                    'multihoming_id': 'unspecified',
                                    'port': 4342,
                                    'publish_mode': 'publish-extranet instance-id 11',
                                    'publisher_epoch': 0,
                                    'site_id': 'unspecified',
                                    'ttl': 'never',
                                    'xtr_id': '0x9F725593-0x164CF828-0x76FAFC86-0x7180604E'
                                }
                            },
                            'state': 'complete'
                        },
                        '22:1:1::/96': {
                            'exported_to': ['map-cache, '
                                            'RIB'],
                            'first_published': '00:01:56',
                            'last_published': '00:01:56',
                            'merged_locators': {
                                '1:3:1::1': {
                                    'encap_iid': '22',
                                    'priority': 1,
                                    'publishers': {
                                        '1:2:1::1': {
                                            'encap_iid': '22',
                                            'priority': 1,
                                            'rdp_len': 'ext',
                                            'selected': False,
                                            'state': 'up',
                                            'weight': 50
                                        },
                                        '4:2:1::1': {
                                            'encap_iid': '22',
                                            'priority': 1,
                                            'rdp_len': 'ext',
                                            'selected': False,
                                            'state': 'up',
                                            'weight': 50
                                        }
                                    },
                                    'rdp_len': 'ext',
                                    'src_add': '4:2:1::1',
                                    'state': 'up',
                                    'weight': 50
                                },
                                '1:3:2::1': {
                                    'encap_iid': '22',
                                    'priority': 1,
                                    'publishers': {
                                        '1:2:1::1': {
                                            'encap_iid': '22',
                                            'priority': 1,
                                            'rdp_len': 'ext',
                                            'selected': True,
                                            'state': 'up',
                                            'weight': 50
                                        },
                                        '4:2:1::1': {
                                            'encap_iid': '22',
                                            'priority': 1,
                                            'rdp_len': 'ext',
                                            'selected': False,
                                            'state': 'up',
                                            'weight': 50
                                        }
                                    },
                                    'rdp_len': 'ext',
                                    'src_add': '4:2:1::1',
                                    'state': 'up',
                                    'weight': 50
                                }
                            },
                            'publishers': {
                                '1:2:1::1.4342': {
                                    'domain_id': 'extranet',
                                    'entry_epoch': 0,
                                    'entry_state': 'complete',
                                    'last_published': '00:01:56',
                                    'locators': {
                                        '1:3:1::1': {
                                            'encap_iid': '22',
                                            'priority': 1,
                                            'rdp': '[-]',
                                            'state': 'up',
                                            'weight': 50
                                        },
                                        '1:3:2::1': {
                                            'encap_iid': '22',
                                            'priority': 1,
                                            'rdp': '[-]',
                                            'state': 'up',
                                            'weight': 50
                                        }
	                            },
                                   'multihoming_id': 'unspecified',
                                   'port': 4342,
                                   'publish_mode': 'publish-extranet instance-id 11',
                                   'publisher_epoch': 0,
                                   'sgt': 221,
                                   'site_id': 'unspecified',
                                   'ttl': 'never',
                                   'xtr_id': '0x6F2A92D0-0x145ECA8A-0xF1C24AB4-0xE8A4F310'
                                },
                                '4:2:1::1.4342': {
                                    'domain_id': 'extranet',
                                    'entry_epoch': 0,
                                    'entry_state': 'complete',
                                    'last_published': '00:01:56',
                                    'locators': {
	                                '1:3:1::1': {
                                            'encap_iid': '22',
                                            'priority': 1,
                                            'rdp': '[-]',
                                            'state': 'up',
                                            'weight': 50
                                        },
                                        '1:3:2::1': {
                                            'encap_iid': '22',
                                            'priority': 1,
                                            'rdp': '[-]',
                                            'state': 'up',
                                            'weight': 50
                                        }
                                    },
                                    'multihoming_id': 'unspecified',
                                    'port': 4342,
                                    'publish_mode': 'publish-extranet instance-id 11',
                                    'publisher_epoch': 0,
                                    'sgt': 221,
                                    'site_id': 'unspecified',
                                    'ttl': 'never',
                                    'xtr_id': '0x6F2A92D0-0x145ECA8A-0xF1C24AB4-0xE8A4F310'
                                }
                            },
                            'state': 'complete'
                        }
                    }
                }
            }
        }
    }
}