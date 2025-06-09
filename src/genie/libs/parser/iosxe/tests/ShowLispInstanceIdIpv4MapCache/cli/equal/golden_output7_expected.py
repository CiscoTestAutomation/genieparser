expected_output = {
  'lisp_id': {
    0: {
      'instance_id': {
        4099: {
          'eid_table': 'vrf VN1 ',
          'entries': 10,
          'eid_prefix': {
            '0.0.0.0/0': {
              'uptime': '00:00:07',
              'expiry_time': '00:00:52',
              'via': 'static-send-map-request',
              'action': 'send-map-request',
              'negative_cache_entry': True
            },
            '8.8.8.0/30': {
              'uptime': '4d11h',
              'expiry_time': '01:14:41',
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
            },
            '11.9.1.0/24': {
              'uptime': '6w6d',
              'expiry_time': 'never',
              'via': 'dynamic-EID',
              'map_reply_state': 'send-map-request',
              'action': 'send-map-request',
              'negative_cache_entry': True
            },
            '11.10.1.0/24': {
              'uptime': '6w6d',
              'expiry_time': 'never',
              'via': 'dynamic-EID',
              'map_reply_state': 'send-map-request',
              'action': 'send-map-request',
              'negative_cache_entry': True
            },
            '12.9.1.0/24': {
              'uptime': '6w6d',
              'expiry_time': 'never',
              'via': 'dynamic-EID',
              'map_reply_state': 'send-map-request',
              'action': 'send-map-request',
              'negative_cache_entry': True
            },
            '12.10.1.0/24': {
              'uptime': '6w6d',
              'expiry_time': 'never',
              'via': 'dynamic-EID',
              'map_reply_state': 'send-map-request',
              'action': 'send-map-request',
              'negative_cache_entry': True
            },
            '27.1.1.0/24': {
              'uptime': '6w6d',
              'expiry_time': 'never',
              'via': 'dynamic-EID',
              'map_reply_state': 'send-map-request',
              'action': 'send-map-request',
              'negative_cache_entry': True
            },
            '54.54.41.1/32': {
              'uptime': '4d11h',
              'expiry_time': '01:14:42',
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
            },
            '72.0.0.0/5': {
              'uptime': '4d11h',
              'expiry_time': '00:09:42',
              'via': 'map-reply',
              'map_reply_state': 'unknown-eid-forward',
              'locators': {
                '3.3.3.188': {
                  'uptime': '4d11h',
                  'rloc_state': 'up',
                  'priority': 10,
                  'weight': 10,
                  'encap_iid': '-',
                  'metric': 0
                }
              }
            },
            '89.1.0.0/16': {
              'uptime': '6w6d',
              'expiry_time': 'never',
              'via': 'dynamic-EID',
              'map_reply_state': 'send-map-request',
              'action': 'send-map-request',
              'negative_cache_entry': True
            }
          }
        }
      }
    }
  }
}