expected_output = {
  'total': 4,
  'interfaces': {
    'ethernet1/1': {
      'area': 0,
      'network': '10.254.32.221/30',
      'cost': 410,
      'state': 'down',
      'full_neighbors': 0,
      'configured_neighbors': 0
    },
    'ethernet5/1': {
      'area': 0,
      'network': '10.254.32.3/31',
      'cost': 21,
      'state': 'ptpt',
      'full_neighbors': 1,
      'configured_neighbors': 1
    },
    'ethernet7/1': {
      'area': 0,
      'network': '10.254.32.109/31',
      'cost': 20,
      'state': 'ptpt',
      'full_neighbors': 1,
      'configured_neighbors': 1
    },
    'loopback1': {
      'area': 0,
      'network': '10.76.33.22/32',
      'cost': 1,
      'state': 'DR',
      'full_neighbors': 0,
      'configured_neighbors': 0
    }
  }
}
