expected_output = {
    'lisp_id': {
        0: {
            'instance_id': {
                21: {
                    'address_family': 'IPv4',
                    'eid_table': 'vrf sub1',
                    'lsb': '0x3',
                    'all_no_route': False,
                    'entries_total': 1,
                    'no_route_entries': 0,
                    'inactive_entries': 0,
                    'do_not_register_entries': 0,
                    'eid_prefix': '21.1.1.0/24',
                    'eid_info': 'locator-set set1, auto-discover-rlocs, proxy',
                    'domain_id': 'local',
                    'publish_mode': 'publish-extranet instance-id 11',
                    'locators': {
                        '1.3.1.1': {
                            'priority': 1,
                            'weight': 50,
                            'source': 'cfg-intf',
                            'state': 'site-self, reachable',
                            'config_missing': False
                        },
                        '1.3.2.1': {
                            'priority': 1,
                            'weight': 50,
                            'source': 'auto-disc',
                            'state': 'site-other, report-reachable',
                            'config_missing': False
                        }
                    },
                    'map_servers': {
                        '1.2.1.1': {
                            'uptime': '00:00:48',
                            'ack': 'Yes',
                            'domain_id': '1'
                        },
                        '4.2.1.1': {
                            'uptime': '00:00:48',
                            'ack': 'Yes',
                            'domain_id': '4'
                        }
                    }
                }
            }
        }
    }
}
