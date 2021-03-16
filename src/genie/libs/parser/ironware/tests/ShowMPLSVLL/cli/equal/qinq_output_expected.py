expected_output = {
  'vll': {
    'MY-QINQ-VLL': {
      'vcid': 4567,
      'vll_index': 72,
      'local': {
        'type': 'tagged',
        'interface': 'ethernet2/1',
        'outer_vlan_id': 100,
        'inner_vlan_id': 45,
        'state': 'Up',
        'mct_state': 'None',
        'ifl_id': '--',
        'vc_type': 'tag',
        'mtu': 9190,
        'cos': '--',
        'extended_counters': True
      },
      'peer': {
        'ip': '192.168.2.2',
        'state': 'UP',
        'vc_type': '--',
        'mtu': 0,
        'local_label': '--',
        'remote_label': '--',
        'local_group_id': 0,
        'remote_group_id': '--',
        'tunnel_lsp': {
          'name': 'my_qinq_tunnel_lsp',
          'tunnel_interface': 'tnl3'
        },
        'lsps_assigned': 'No LSPs assigned'
      }
    }
  }
}
