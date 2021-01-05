expected_output = {
  'vll': {
    'MY-DOWN-VLL': {
      'vcid': 2344,
      'vll_index': 45,
      'local': {
        'type': 'tagged',
        'interface': 'ethernet4/7',
        'vlan_id': 3033,
        'state': 'Down',
        'mct_state': 'None',
        'ifl_id': '--',
        'vc_type': 'tag',
        'mtu': 9190,
        'cos': '--',
        'extended_counters': True
      },
      'peer': {
        'ip': '192.168.1.1',
        'state': 'DOWN',
        'reason': 'endpoint is not UP',
        'vc_type': '--',
        'mtu': 0,
        'local_label': '--',
        'remote_label': '--',
        'local_group_id': 0,
        'remote_group_id': '--',
        'tunnel_lsp': {
          'name': 'my_tunnel_lsp.1',
          'tunnel_interface': 'tnl32'
        },
        'lsps_assigned': 'No LSPs assigned'
      }
    }
  }
}
