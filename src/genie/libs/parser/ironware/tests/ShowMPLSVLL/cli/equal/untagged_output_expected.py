expected_output = {
  'vll': {
    'MY-UNTAGGED-VLL': {
      'vcid': 3566,
      'vll_index': 37,
      'local': {
        'type': 'untagged',
        'interface': 'ethernet2/8',
        'state': 'Up',
        'mct_state': 'None',
        'ifl_id': '--',
        'vc_type': 'tag',
        'mtu': 9190,
        'cos': '--',
        'extended_counters': True
      },
      'peer': {
        'ip': '192.168.1.2',
        'state': 'UP',
        'vc_type': 'tag',
        'mtu': 9190,
        'local_label': 851974,
        'remote_label': 852059,
        'local_group_id': 0,
        'remote_group_id': 0,
        'tunnel_lsp': {
          'name': 'my_untagged-lsp',
          'tunnel_interface': 'tnl32'
        },
        'lsps_assigned': 'No LSPs assigned'
      }
    }
  }
}
