expected_output = {
  'id':{
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
    },
    4294967295: {
      'encoding': 'encode-xml',
      'filter': {
        'filter_type': 'xpath',
        'xpath': '/ios-events-ios-xe-oper:bgp-peer-state-change'
      },
      'legacy_receivers': {
        '0.0.0.0': {
          'port': 0,
          'protocol': 'rfc5277'
        }
      },
      'state': 'Invalid',
      'stream': 'rfc5277',
      'update_policy': {
        'dampening_period': 0,
        'synch_on_start': 'No',
        'update_trigger': 'on-change'
      }
    }
  }
}