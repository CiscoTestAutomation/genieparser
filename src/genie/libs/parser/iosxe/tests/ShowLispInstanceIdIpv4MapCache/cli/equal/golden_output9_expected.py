expected_output = {
    'lisp_id': {
        0: {
            'instance_id': {
                111: {
                    'eid_table': 'vrf internet ',
                    'entries': 4,
                    'eid_prefix': {
                        '172.168.0.0/16': {
                            'uptime': '00:03:39',
                            'expiry_time': 'never',
                            'via': 'pub-sub-send-map-req',
                            'map_reply_state': 'send-map-request',
                            'site': 'remote-to-site',
                            'negative_cache_entry': True,
                            'action': 'send-map-request'
                        },
                        '173.168.0.0/16': {
                            'uptime': '00:03:39',
                            'expiry_time': 'never',
                            'via': 'pub-sub-send-map-req',
                            'map_reply_state': 'send-map-request',
                            'site': 'remote-to-site',
                            'negative_cache_entry': True,
                            'action': 'send-map-request'
                        },
                        '192.168.0.0/16': {
                            'uptime': '00:03:39',
                            'expiry_time': 'never',
                            'via': 'pub-sub-send-map-req',
                            'map_reply_state': 'send-map-request',
                            'site': 'local-to-site',
                            'negative_cache_entry': True,
                            'action': 'send-map-request'
                        },
                        '193.168.0.0/16': {
                            'uptime': '00:03:26',
                            'expiry_time': 'never',
                            'via': 'pub-sub, self',
                            'map_reply_state': 'complete',
                            'site': 'local-to-site',
                            'locators': {
                                '16.16.16.16': {
                                    'uptime': '00:03:26',
                                    'rloc_state': 'up, self',
                                    'priority': 250,
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
