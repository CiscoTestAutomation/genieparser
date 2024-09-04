expected_output={
  'interfaces': {
    'Gi2/0/10': {
      'bindings': [
        {
          'feature': 'Pacl',
          'direction': 'ingress',
          'protocol': 'MAC',
          'cg_id': 1,
          'cg_name': 'pacl_mac',
          'status': 'Success',
          'src_og_lkup_hdl': 0,
          'dst_og_lkup_hdl': 0
        },
        {
          'feature': 'Pacl',
          'direction': 'ingress',
          'protocol': 'IPv4',
          'cg_id': 9,
          'cg_name': 'pacl_gi2/0/10_v4',
          'status': 'Success',
          'src_og_lkup_hdl': 0,
          'dst_og_lkup_hdl': 0
        },
        {
          'feature': 'Pacl',
          'direction': 'ingress',
          'protocol': 'IPv6',
          'cg_id': 16,
          'cg_name': 'pacl_gi2/0/10_v6',
          'status': 'Success',
          'src_og_lkup_hdl': 0,
          'dst_og_lkup_hdl': 0
        }
      ]
    }
  }
}
