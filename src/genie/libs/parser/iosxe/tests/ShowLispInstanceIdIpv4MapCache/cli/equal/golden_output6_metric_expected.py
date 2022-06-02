expected_output = {
     'lisp_id': {
         0: {
             'instance_id': {
                 111: {
                     'eid_prefix': {
                         '0.0.0.0/0': {
                             'action': 'send-map-request + Encapsulating to proxy ETR',
                             'expiry_time': '00:14:59',
                             'locators': {
                                 '21.21.21.21': {
                                     'encap_iid': '-',
                                     'metric': None,
                                     'priority': 255,
                                     'rloc_state': 'admin-down',
                                     'uptime': '00:00:23',
                                     'weight': 50,
                                 },
                                 '24.24.24.24': {
                                     'encap_iid': '-',
                                     'metric': 0,
                                     'priority': 50,
                                     'rloc_state': 'up',
                                     'uptime': '00:00:23',
                                     'weight': 50,
                                 },
                             },
                             'map_reply_state': 'unknown-eid-forward',
                             'negative_cache_entry': False,
                             'uptime': '00:00:01',
                             'via': 'map-reply',
                         },
                     },
                     'eid_table': 'vrf prov ',
                     'entries': 1,
                 },
             },
         },
     },
 }