expected_output = {
  'id': {
    2147483659: {
      'encoding': 'encode-xml',
      'filter': {
        'filter_type': 'xpath',
        'xpath': '/if:interfaces-state/interface/oper-status'
      },
      'legacy_receivers': {
        '10.69.35.35': {
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
}
