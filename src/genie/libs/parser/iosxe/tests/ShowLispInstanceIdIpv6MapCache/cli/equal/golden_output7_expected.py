expected_output = {
  'lisp_id': {
    0: {
      'instance_id': {
        4099: {
          'eid_table': 'vrf VN1 ',
          'entries': 7,
          'eid_prefix': {
            '::/0': {
              'uptime': '22:44:21',
              'expiry_time': '00:12:29',
              'via': 'map-reply',
              'map_reply_state': 'unknown-eid-forward',
              'action': 'send-map-request + Encapsulating to proxy ETR',
              'negative_cache_entry': False,
              'locators': {
                '3.3.3.188': {
                  'uptime': '22:44:20',
                  'rloc_state': 'up',
                  'priority': 10,
                  'weight': 10,
                  'encap_iid': '-',
                  'metric': 0
                }
              }
            },
            '2102:1:1:4109::/64': {
              'uptime': '6w6d',
              'expiry_time': 'never',
              'via': 'dynamic-EID',
              'map_reply_state': 'send-map-request',
              'action': 'send-map-request',
              'negative_cache_entry': True
            },
            '2102:1:1:410A::/64': {
              'uptime': '6w6d',
              'expiry_time': 'never',
              'via': 'dynamic-EID',
              'map_reply_state': 'send-map-request',
              'action': 'send-map-request',
              'negative_cache_entry': True
            },
            '2102:1:1:4209::/64': {
              'uptime': '6w6d',
              'expiry_time': 'never',
              'via': 'dynamic-EID',
              'map_reply_state': 'send-map-request',
              'action': 'send-map-request',
              'negative_cache_entry': True
            },
            '2102:1:1:420A::/64': {
              'uptime': '6w6d',
              'expiry_time': 'never',
              'via': 'dynamic-EID',
              'map_reply_state': 'send-map-request',
              'action': 'send-map-request',
              'negative_cache_entry': True
            },
            '2102:1:1:510C::/64': {
              'uptime': '6w6d',
              'expiry_time': 'never',
              'via': 'dynamic-EID',
              'map_reply_state': 'send-map-request',
              'action': 'send-map-request',
              'negative_cache_entry': True
            },
            '2102:1:1:6501::1/128': {
              'uptime': '4d11h',
              'expiry_time': '12:50:04',
              'via': 'map-reply',
              'map_reply_state': 'complete',
              'locators': {
                '3.3.3.188': {
                  'uptime': '4d11h',
                  'rloc_state': 'up',
                  'priority': 10,
                  'weight': 10,
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