expected_output={
  'interface_class_name': {
    'Gi3/0/31': {
      'direction': 'Ingress',
      'feature': 'Pacl',
      'protocol': 'IPv4',
      'cg_id': 12,
      'cg_name': 'pre-auth',
      'oid': '0xAE9',
      'no_of_ace': 12,
      'ipv4_ace_key_mask': {
        'ipv4_src_value': '0.0.0.0',
        'ipv4_src_mask': '0.0.0.0',
        'ipv4_dst_value': '0.0.0.0',
        'ipv4_dst_mask': '0.0.0.0',
        'V': {
          'proto': '0x11',
          'tos': '0x0',
          'tcp_flg': '0x0',
          'ttl': '0x0',
          'ipv4_flags': '0x0',
          'src_port': '0x44',
          'dst_port': '0x43'
        },
        'M': {
          'proto': '0xff',
          'tos': '0x0',
          'tcp_flg': '0x0',
          'ttl': '0x0',
          'ipv4_flags': '0x0',
          'src_port': '0xffff',
          'dst_port': '0xffff'
        },
        'result_actions': {
          'punt': 'N',
          'drop': 'N',
          'mirror': 'N',
          'counter': '0x0',
          'counter_value': 0
        }
      }
    }
  }
}
