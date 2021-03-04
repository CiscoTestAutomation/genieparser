expected_output = {
  'vll': {
    'MY-FIRST-VLL': {
      'vcid': 2456,
      'vll_index': 2,
      'local': {
        'type': 'tagged',
        'interface': 'ethernet2/5',
        'vlan_id': 3043,
        'state': 'Up',
        'mct_state': 'None',
        'ifl_id': '--',
        'vc_type': 'tag',
        'mtu': 9190,
        'cos': '--',
        'extended_counters': True,
        'counters': False
      },
      'peer': {
        'ip': '192.168.1.1',
        'state': 'UP',
        'vc_type': 'tag',
        'mtu': 9190,
        'local_label': 852217,
        'remote_label': 852417,
        'local_group_id': 0,
        'remote_group_id': 0,
        'tunnel_lsp': {
          'name': 'mlx8.1_to_ces.2',
          'tunnel_interface': 'tnl15'
        },
        'lsps_assigned': 'No LSPs assigned'
      }
    }
  }
}
