expected_output = {
    'lisp_id': {
        0: {
            'instance_id': {
                1023: {
                    'eid_table': 'Vlan 1023',
                    'lsb': '0x1',
                    'entries': {
                        'total': 2,
                        'no_route': 0,
                        'inactive': 0,
                        'do_not_register': 0,
                        'eids': {
                            'aaaa.0011.0001/48': {
                                'eid': 'aaaa.0011.0001',
                                'mask': 48,
                                'dynamic_eid': 'Auto-L2-group-1023',
                                'locator_set': 'RLOC',
                                'uptime': '00:00:02',
                                'last_change': '00:00:02',
                                'domain_id': 'local',
                                'multihoming_site_id': 100,
                                'service_insertion': 'N/A',
                                'locators': {
                                    '10.10.10.10': {
                                        'priority': 10,
                                        'weight': 10,
                                        'source': 'cfg-intf',
                                        'location': 'site-self',
                                        'state': 'reachable'
                                    }
                                }
                            },
                            'aaaa.0011.0002/48': {
                                'eid': 'aaaa.0011.0002',
                                'mask': 48,
                                'dynamic_eid': 'Auto-L2-group-1023',
                                'locator_set': 'RLOC',
                                'uptime': '00:00:01',
                                'last_change': '00:00:01',
                                'domain_id': 'local',
                                'service_insertion': 'N/A',
                                'locators': {
                                    '10.10.10.10': {
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