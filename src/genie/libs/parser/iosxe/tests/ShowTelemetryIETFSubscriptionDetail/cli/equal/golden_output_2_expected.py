expected_output = {
  2147483659: {
    'encoding': 'encode-xml',
    'filter': {
      'filter_type': 'xpath',
      'xpath': '/if:interfaces-state/interface/oper-status'
    },
    'legacy_receivers': {
      '5.28.35.35': {
        'port': 45128,
        'protocol': 'netconf'
      }
    },
    'state': 'Valid',
    'stream': 'yang-push',
    'update_policy': {
      'period': 1000,
      'update_trigger': 'periodic'
    }
  }
}