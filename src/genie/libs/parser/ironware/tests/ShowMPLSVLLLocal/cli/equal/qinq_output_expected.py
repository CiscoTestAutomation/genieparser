expected_output = {
  'vll': {
    'MY-QINQ-VLL-LOCAL': {
      'vll_id': 4,
      'ifl_id': '4096',
      'state': 'UP',
      'endpoint_1': {
        'type': 'tagged',
        'outer_vlan_id': 100,
        'inner_vlan_id': 45,
        'interface': 'ethernet2/1',
        'cos': '--'
      },
      'endpoint_2': {
        'type': 'tagged',
        'vlan_id': 100,
        'interface': 'ethernet2/3',
        'cos': '--'
      },
      'extended_counters': True
    }
  }
}
