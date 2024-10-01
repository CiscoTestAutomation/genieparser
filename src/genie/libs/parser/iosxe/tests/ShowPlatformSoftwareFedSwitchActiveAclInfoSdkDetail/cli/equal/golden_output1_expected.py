expected_output={
  'class_group_name': {
    'V4SGACL;000': {
      'direction': 'Egress',
      'feature': 'Sgacl',
      'protocol': 'IPv4',
      'cg_id': 273,
      'pol_hdl': '0x5405cf68',
      'oid': '0x81E',
      'no_of_ace': 1,
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
          'drop': 'Y',
          'mirror': 'N',
          'counter': '0x0',
          'counter_value': 0
        }
      }
    },
    'V6SGACL<000': {
      'direction': 'Egress',
      'feature': 'Sgacl',
      'protocol': 'IPv6',
      'cg_id': 545,
      'pol_hdl': '0x5405f6c8',
      'oid': '0x823',
      'no_of_ace': 1,
      'ipv6_ace_key_mask': {
        'ipv6_src_mac_value': '0x0.0x0.0x0.0x0.0x0.0x0',
        'ipv6_src_mac_mask': '0x0.0x0.0x0.0x0.0x0.0x0',
        'ipv6_dst_mac_value': '0x0.0x0.0x0.0x0.0x0.0x0',
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
          'counter': '0x0',
          'counter_value': 0
        }
      }
    }
  }
}