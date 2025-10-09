expected_output = {
    'lisp_id': {
        0: {
            'instance_id': {
                4100: {
                    'eid_prefix': {
                        '0.0.0.0/0': {
                            'action': 'send-map-request',
                            'expiry_time': 'never',
                            'negative_cache_entry': True,
                            'uptime': '00:21:36',
                            'via': 'static-send-map-request'
                        },
                        '128.0.0.0/2': {
                            'expiry_time': '00:08:11',
                            'map_reply_state': 'forward-native',
                            'uptime': '00:21:36',
                            'via': 'map-reply'
                        },
                        '192.0.0.0/14': {
                            'expiry_time': '6d23h',
                            'locators': {
                                '100.155.155.155': {
                                    'encap_iid': '-',
                                    'priority': 10,
                                    'rloc_state': 'up',
                                    'uptime': '00:00:41',
                                    'weight': 50
                                }
                            },
                            'map_reply_state': 'complete',
                            'uptime': '00:00:41',
                            'via': 'transient-publication'
                        },
                        '192.0.0.0/8': {
                            'expiry_time': '6d23h',
                            'locators': {
                                '100.155.155.155': {
                                    'encap_iid': '-',
                                    'priority': 10,
                                    'rloc_state': 'up',
                                    'uptime': '00:21:36',
                                    'weight': 50
                                }
                            },
                            'map_reply_state': 'complete',
                            'uptime': '00:21:36',
                            'via': 'transient-publication'
                        },
                        '192.1.0.0/16': {
                            'action': 'send-map-request',
                            'expiry_time': 'never',
                            'map_reply_state': 'send-map-request',
                            'negative_cache_entry': True,
                            'uptime': '00:21:36',
                            'via': 'dynamic-EID'
                        },
                        '192.2.0.0/16': {
                            'action': 'send-map-request',
                            'expiry_time': 'never',
                            'map_reply_state': 'send-map-request',
                            'negative_cache_entry': True,
                            'uptime': '00:21:36',
                            'via': 'dynamic-EID'
                        },
                        '192.3.0.0/16': {
                            'action': 'send-map-request',
                            'expiry_time': 'never',
                            'map_reply_state': 'send-map-request',
                            'negative_cache_entry': True,
                            'uptime': '00:21:36',
                            'via': 'dynamic-EID'
                        },
                        '192.4.0.0/16': {
                            'action': 'send-map-request',
                            'expiry_time': 'never',
                            'map_reply_state': 'send-map-request',
                            'negative_cache_entry': True,
                            'uptime': '00:21:36',
                            'via': 'dynamic-EID'
                        },
                        '192.5.0.0/16': {
                            'action': 'send-map-request',
                            'expiry_time': 'never',
                            'map_reply_state': 'send-map-request',
                            'negative_cache_entry': True,
                            'uptime': '00:21:36',
                            'via': 'dynamic-EID'
                        }
                    },
                    'eid_table': 'vrf VRF1 ',
                    'entries': 9
                }
            }
        }
    }
}
