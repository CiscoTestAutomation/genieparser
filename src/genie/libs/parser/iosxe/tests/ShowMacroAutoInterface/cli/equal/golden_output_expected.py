expected_output={
  'asp_status': 'Enabled',
  'fallback': {
    'type': 'CDP',
    'status': 'Disabled'
  },
  'interfaces': {
    'Vlan1': {
      'asp': 'TRUE',
      'fallback': 'None',
      'macro': 'No Macro Applied'
    },
    'GigabitEthernet0/0': {
      'asp': 'TRUE',
      'fallback': 'None',
      'macro': 'No Macro Applied'
    },
    'GigabitEthernet1/0/1': {
      'asp': 'TRUE',
      'fallback': 'None',
      'macro': 'No Macro Applied'
    },
    'GigabitEthernet1/0/37': {
      'asp': 'FALSE',
      'fallback': 'None',
      'macro': 'CISCO_LAST_RESORT_EVENT'
    },
    'Ap1/0/1': {
      'asp': 'TRUE',
      'fallback': 'None',
      'macro': 'CISCO_LAST_RESORT_EVENT'
    },
    'Tunnel2': {
      'asp': 'TRUE',
      'fallback': 'None',
      'macro': 'No Macro Applied'
    }
  }
}
