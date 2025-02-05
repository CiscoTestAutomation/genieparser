expected_output={
  'interface_class_name': {
    'implicit_deny:xACSACLx-IP-PERMIT_ALL_IPV4_TRAFFIC-57f6b0d3:': {
      'direction': 'Ingress',
      'feature': 'Cgacl',
      'protocol': 'IPv4',
      'cg_id': 1552,
      'pol_hdl': '0x24073568',
      'oid': '0xE39',
      'no_of_ace': 2,
      'ipv4_ace_key_mask': {
        'ipv4_src_value': '0.0.0.0',
        'ipv4_src_mask': '0.0.0.0',
        'ipv4_dst_value': '0.0.0.0',
        'ipv4_dst_mask': '0.0.0.0',
        'V': {
          'proto': '0x0',
          'tos': '0x0',
          'tcp_flg': '0x0',
          'ttl': '0x0',
          'ipv4_flags': '0x0',
          'src_port': '0x0',
          'dst_port': '0x0'
        },
        'M': {
          'proto': '0x0',
          'tos': '0x0',
          'tcp_flg': '0x0',
          'ttl': '0x0',
          'ipv4_flags': '0x0',
          'src_port': '0x0',
          'dst_port': '0x0'
        },
        'result_actions': {
          'punt': 'N',
          'drop': 'N',
          'mirror': 'N',
          'counter': '0xe3a',
          'counter_value': 0
        }
      },
      'ipv4_ace_key_mask_1': {
        'ipv4_src_value': '0.0.0.0',
        'ipv4_src_mask': '0.0.0.0',
        'ipv4_dst_value': '0.0.0.0',
        'ipv4_dst_mask': '0.0.0.0',
        'V': {
          'proto': '0x0',
          'tos': '0x0',
          'tcp_flg': '0x0',
          'ttl': '0x0',
          'ipv4_flags': '0x0',
          'src_port': '0x0',
          'dst_port': '0x0'
        },
        'M': {
          'proto': '0x0',
          'tos': '0x0',
          'tcp_flg': '0x0',
          'ttl': '0x0',
          'ipv4_flags': '0x0',
          'src_port': '0x0',
          'dst_port': '0x0'
        },
        'result_actions': {
          'punt': 'N',
          'drop': 'Y',
          'mirror': 'N',
          'counter': '0xe3b',
          'counter_value': 0
        }
      }
    }
  }
}
