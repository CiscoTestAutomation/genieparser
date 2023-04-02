expected_output = {
    'lisp_id': {
        0: {
            'instance_id': {
                102: {
                    'address_family': 'IPv6',
                    'eid_table': 'blue',
                    'state': 'Established',
                    'epoch': 0,
                    'entries': 1,
                    'eid_prefix': {
                        '2001:172:168:1::/64': {
                            'eid_epoch': 0,
                            'last_pub_time': '00:01:25',
                            'ttl': 'never',
                            'eid_state': 'complete',
                            'rloc_set': {
                                '2001:2:2:2::2': {
                                    'priority': 50,
                                    'weight': 50,
                                    'rloc_state': 'up',
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
