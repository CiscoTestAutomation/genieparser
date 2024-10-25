expected_output = {
    'lisp_id': {
        0: {
            'instance_id': {
                11: {
                    'eid_table': 'vrf prov1 ',
                    'entries': 2,
                    'eid_prefix': {
                        '21.1.1.0/24': {
                            'uptime': '01:26:23',
                            'expiry_time': 'never',
                            'via': 'pub-sub',
                            'map_reply_state': 'complete',
                            'site': 'local-to-site',
                            'locators': {
                                '1.3.1.1': {
                                    'uptime': '01:26:23',
                                    'rloc_state': 'up, self',
                                    'priority': 1,
                                    'weight': 50,
                                    'encap_iid': '21'
                                },
                                '1.3.2.1': {
                                    'uptime': '01:26:18',
                                    'rloc_state': 'up',
                                    'priority': 1,
                                    'weight': 50,
                                    'encap_iid': '21'
                                }
                            }
                        },
                        '21.2.1.0/24': {
                            'uptime': '01:26:08',
                            'expiry_time': 'never',
                            'via': 'pub-sub',
                            'map_reply_state': 'complete',
                            'site': 'remote-to-site',
                            'locators': {
                                '2.5.1.1': {
                                    'uptime': '01:26:08',
                                    'rloc_state': 'up',
                                    'priority': 1,
                                    'weight': 50,
                                    'encap_iid': '-'
                                }
                            }
                        }
                    }
                }
            }
        }
    }
}
