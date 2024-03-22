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
                        'do_not_register': 1,
                        'eids': {
                            '2001:192:168:1::1/128': {
                                'eid': '2001:192:168:1::1',
                                'mask': 128,
                                'dynamic_eid': '2001_192_168_1',
                                'locator_set': 'RLOC',
                                'do_not_register': True,
                                'uptime': '8w1d',
                                'last_change': '8w1d',
                                'domain_id': 'local',
                                'service_insertion': 'N/A',
                                'service_insertion_id': 0,
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
                                'uptime': '8w1d',
                                'last_change': '8w1d',
                                'domain_id': 'local',
                                'service_insertion': 'N/A',
                                'service_insertion_id': 0,
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
