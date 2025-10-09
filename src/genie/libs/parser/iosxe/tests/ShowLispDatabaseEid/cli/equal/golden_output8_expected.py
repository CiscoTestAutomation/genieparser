expected_output = {
    'lisp_id': {
        0: {
            'instance_id': {
                22: {
                    'address_family': 'IPv4',
                    'eid_table': 'vrf sub2',
                    'lsb': '0x3',
                    'all_no_route': False,
                    'entries_total': 1,
                    'no_route_entries': 0,
                    'inactive_entries': 0,
                    'do_not_register_entries': 0,
                    'eid_prefix': '22.1.1.0/24',
                    'eid_info': 'locator-set set1, auto-discover-rlocs, proxy',
                    'domain_id': 'local',
                    'publish_mode': 'no-extranet',
                    'locators': {
                        '1.3.1.1': {
                            'priority': 1,
                            'weight': 50,
                            'source': 'auto-disc',
                            'state': 'site-other, report-reachable',
                            'config_missing': False
                        },
                        '1.3.2.1': {
                            'priority': 1,
                            'weight': 50,
                            'source': 'cfg-intf',
                            'state': 'site-self, reachable',
                            'config_missing': False
                        }
                    },
                    'map_servers': {
                        '4.2.1.1': {
                            'uptime': '00:11:01',
                            'ack': 'Yes',
                            'domain_id': '4'
                        }
                    }
                }
            }
        }
    }
}
