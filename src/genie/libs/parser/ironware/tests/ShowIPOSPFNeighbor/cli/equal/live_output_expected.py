expected_output = {
  'vrf': {
    'default': {
      'neighbors': {
        '10.254.32.22': {
          'interface': '7/1',
          'local_ip': '10.254.32.23',
          'priority': 1,
          'state': 'FULL/OTHER',
          'neighbor_rid': '10.9.3.4',
          'state_changes': 4,
          'options': 82,
          'lsa_retransmits': 0
        },
        '10.254.32.20': {
          'interface': '5/1',
          'local_ip': '10.254.32.21',
          'priority': 1,
          'state': 'FULL/OTHER',
          'neighbor_rid': '10.49.2.1',
          'state_changes': 4,
          'options': 82,
          'lsa_retransmits': 0
        }
      }
    }
  },
  'total': 2,
  'total_full': 2
}
