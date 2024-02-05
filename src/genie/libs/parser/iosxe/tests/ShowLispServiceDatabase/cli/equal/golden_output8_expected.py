expected_output = {
    'lisp_id': {
        0: {
            'instance_id': {
                4100: {
                    'eid_table': 'vrf red',
                    'lsb': '0x1',
                    'entries': {
                        'total': 1,
                        'no_route': 0,
                        'inactive': 0,
                        'do_not_register': 1,
                        'eids': {
                            '172.168.1.1/32': {
                                'eid': '172.168.1.1',
                                'mask': 32,
                                'dynamic_eid': 'vrf_red_172_168_1_0',
                                'locator_set': 'RLOC',
                                'uptime': '00:04:20',
                                'last_change': '00:04:20',
                                'domain_id': 'local',
                                'service_insertion': 'N/A',
                                'do_not_register': True,
                                'locators': {
                                    '100.22.22.22': {
                                        'priority': 10,
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
