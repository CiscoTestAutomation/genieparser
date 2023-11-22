expected_output = {
    'lisp_id': {
        'default': {
            'instance_id': {
                4099: {
                    'eid_table': 'vrf INTERNAL',
                    'lsb': '0x1',
                    'entries': {
                        'total': 3,
                        'no_route': 0,
                        'inactive': 0,
                        'do_not_register': 1,
                        'eids': {
                            '0.0.0.0/0': {
                                'eid': '0.0.0.0',
                                'mask': 0,
                                'locator_set': 'DEFAULT_ETR_LOCATOR',
                                'uptime': '18w2d',
                                'last_change': '18w2d',
                                'domain_id': 'unset',
                                'service_insertion': 'N/A',
                                'service_insertion_id': 0,
                                'locators': {
                                    '100.64.254.5': {
                                        'priority': 9,
                                        'weight': 10,
                                        'source': 'cfg-intf',
                                        'location': 'site-self',
                                        'state': 'reachable'
                                    }
                                }
                            },
                            '100.64.250.4/32': {
                                'eid': '100.64.250.4',
                                'mask': 32,
                                'locator_set': 'rloc_ee607b14-6b17-4c5b-babd-c895c2a8d22c',
                                'auto_discover_rlocs': True,
                                'uptime': '18w2d',
                                'last_change': '18w2d',
                                'domain_id': 'unset',
                                'service_insertion': 'N/A',
                                'service_insertion_id': 0,
                                'locators': {
                                    '100.64.254.5': {
                                        'priority': 10,
                                        'weight': 10,
                                        'source': 'cfg-intf',
                                        'location': 'site-self',
                                        'state': 'reachable'
                                    }
                                }
                            },
                            '100.65.0.1/32': {
                                'eid': '100.65.0.1',
                                'mask': 32,
                                'dynamic_eid': 'CIP_FIXED_DATA_POOL-IPV4',
                                'locator_set': 'rloc_ee607b14-6b17-4c5b-babd-c895c2a8d22c',
                                'auto_discover_rlocs': True,
                                'do_not_register': True,
                                'uptime': '18w2d',
                                'last_change': '18w0d',
                                'domain_id': 'unset',
                                'service_insertion': 'N/A',
                                'service_insertion_id': 0,
                                'locators': {
                                    '100.64.254.5': {
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