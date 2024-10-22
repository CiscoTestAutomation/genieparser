expected_output = {
    'lisp_id': {
        0: {
            'instance_id': {
                21: {
                    'eid_table': 'vrf sub1',
                    'lsb': '0x3',
                    'entries': {
                        'total': 3,
                        'no_route': 0,
                        'inactive': 0,
                        'do_not_register': 0,
                        'eids': {
                            '21.1.1.0/24': {
                                'eid': '21.1.1.0',
                                'mask': 24,
                                'locator_set': 'set1',
                                'proxy': True,
                                'auto_discover_rlocs': True,
                                'uptime': '00:50:59',
                                'last_change': '00:50:07',
                                'domain_id': 'local',
                                'service_insertion': 'N/A',
                                'publish_mode': 'publish-extranet instance-id 11',
                                'locators': {
                                    '1.3.1.1': {
                                        'priority': 1,
                                        'weight': 50,
                                        'source': 'auto-disc',
                                        'location': 'site-other',
                                        'state': 'report-reachable'
                                    },
                                    '1.3.2.1': {
                                        'priority': 1,
                                        'weight': 50,
                                        'source': 'cfg-intf',
                                        'location': 'site-self',
                                        'state': 'reachable'
                                    }
                                }
                            },
                            '21.1.2.0/24': {
                                'eid': '21.1.2.0',
                                'mask': 24,
                                'locator_set': 'set1',
                                'proxy': True,
                                'auto_discover_rlocs': True,
                                'uptime': '00:50:59',
                                'last_change': '00:50:07',
                                'domain_id': 'local',
                                'service_insertion': 'N/A',
                                'publish_mode': 'no-extranet',
                                'locators': {
                                    '1.3.1.1': {
                                        'priority': 1,
                                        'weight': 50,
                                        'source': 'auto-disc',
                                        'location': 'site-other',
                                        'state': 'report-reachable'
                                    },
                                    '1.3.2.1': {
                                        'priority': 1,
                                        'weight': 50,
                                        'source': 'cfg-intf',
                                        'location': 'site-self',
                                        'state': 'reachable'
                                    }
                                }
                            },
                            '21.2.1.0/24': {
                                'eid': '21.2.1.0',
                                'mask': 24,
                                'locator_set': 'set1',
                                'proxy': True,
                                'auto_discover_rlocs': True,
                                'dbmap_src': 'import from publication',
                                'uptime': '00:00:19',
                                'last_change': '00:00:19',
                                'domain_id': '2',
                                'service_insertion': 'N/A',
                                'publish_mode': 'publish-extranet instance-id 11',
                                'locators': {
                                    '1.3.1.1': {
                                        'priority': 1,
                                        'weight': 50,
                                        'source': 'auto-disc',
                                        'location': 'site-other',
                                        'state': 'report-reachable'
                                    },
                                    '1.3.2.1': {
                                        'priority': 1,
                                        'weight': 50,
                                        'source': 'cfg-intf',
                                        'location': 'site-self',
                                        'state': 'reachable'
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
