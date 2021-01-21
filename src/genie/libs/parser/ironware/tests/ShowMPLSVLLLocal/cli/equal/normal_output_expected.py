expected_output = {
  'vll': {
    'MY-NORMAL-VLL-LOCAL': {
      'vll_id': 3,
      'ifl_id': '--',
      'state': 'UP',
      'endpoint': {
        1: {
          'type': 'tagged',
          'vlan_id': 2501,
          'interface': 'ethernet2/10',
          'cos': 6
        },
        2: {
          'type': 'tagged',
          'vlan_id': 2501,
          'interface': 'ethernet2/9',
          'cos': 5
        }
      },
      'extended_counters': True
    }
  }
}
