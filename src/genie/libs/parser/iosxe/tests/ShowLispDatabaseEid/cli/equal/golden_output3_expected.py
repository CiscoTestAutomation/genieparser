expected_output = {
    'lisp_id': {
        0: {
            'instance_id': {
                101: {
                    'address_family': 'IPv4',
                    'eid_table': 'vrf red',
                    'lsb': '0x1',
                    'all_no_route': False,
                    'entries_total': 9,
                    'no_route_entries': 0,
                    'inactive_entries': 0,
                    'do_not_register_entries': 1,
                    'eid_prefix': '184.168.1.0/24',
                    'eid_info': 'locator-set RLOC, proxy',
                    'domain_id': 'local',
                    'locators': {
                        '100.121.121.121': {
                            'priority': 50,
                            'weight': 50,
                            'source': 'cfg-addr',
                            'state': 'site-self, reachable',
                            'config_missing': False,
                            'affinity_id_x': 20,
                            'affinity_id_y': 20
                            }
                        },
                    'map_servers': {
                        '100.77.77.77': {
                            'uptime': '00:00:00',
                            'ack': 'Yes',
                            'domain_id': '7'
                            },
                        '100.78.78.78': {
                            'uptime': '00:00:00',
                            'ack': 'Yes',
                            'domain_id': '7'
                            }
                        }
                    }
                }
            }
        }
    }