expected_output = {
    'lisp_id': {
        0: {
            'instance_id': {
                101: {
                    'eid_table': 'Vlan 101',
                    'lsb': '0x1',
                    'entries': {
                        'total': 2,
                        'no_route': 0,
                        'inactive': 0,
                        'do_not_register': 1,
                        'eids': {
                            'aabb.cc00.c901/48': {
                                'eid': 'aabb.cc00.c901',
                                'mask': 48,
                                'dynamic_eid': 'Auto-L2-group-101',
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
                            },
                            'aabb.cc80.ca00/48': {
                                'eid': 'aabb.cc80.ca00',
                                'mask': 48,
                                'dynamic_eid': 'Auto-L2-group-101',
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
                            }
                        }
                    }
                }
            }
        }
    }
}
