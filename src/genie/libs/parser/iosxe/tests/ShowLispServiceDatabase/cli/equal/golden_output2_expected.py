expected_output = {
    'lisp_id': {
        0: {
            'instance_id': {
                4100: {
                    'eid_table': 'vrf red',
                    'lsb': '0x1',
                    'entries': {
                        'total': 2,
                        'no_route': 0,
                        'inactive': 0,
                        'eids': {
                            '2001:192:168:1::1/128': {
                                'eid': '2001:192:168:1::1',
                                'mask': 128,
                                'dynamic_eid': '2001_192_168_1',
                                'locator_set': 'RLOC',
                                'uptime': '01:08:34',
                                'last_change': '01:08:34',
                                'domain_id': 'local',
                                'service_insertion': 'N/A (0)',
                                'locators': {
                                    '11.11.11.11': {
                                        'priority': 10,
                                        'weight': 10,
                                        'source': 'cfg-intf',
                                        'location': 'site-self',
                                        'state': 'reachable'
                                        }
                                    }
                                },
                            '2001:192:168:1::71/128': {
                                'eid': '2001:192:168:1::71',
                                'mask': 128,
                                'dynamic_eid': '2001_192_168_1',
                                'locator_set': 'RLOC',
                                'uptime': '01:08:47',
                                'last_change': '01:08:47',
                                'domain_id': 'local',
                                'service_insertion': 'N/A (0)',
                                'locators': {
                                    '11.11.11.11': {
                                        'priority': 10,
                                        'weight': 10,
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