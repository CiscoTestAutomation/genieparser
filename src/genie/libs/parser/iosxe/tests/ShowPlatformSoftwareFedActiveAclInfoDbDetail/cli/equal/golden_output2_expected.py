expected_output={
  'cg_name': {
    'implicit_deny_v6!pre-auth:xACSACLx-IPV6-PERMIT_ALL_IPV6_TRAFFIC-64a351c6!xACSACLx-IP-PERMIT_ALL_IPV4_TRAFFIC-57f6b0d3:': {
      'cg_id': 272,
      'feature': 'Cgacl',
      'prot': 'IPv4',
      'region': '0xd00b87d8',
      'dir': 'Ingress',
      'asic': 0,
      'oid': '0xB3C',
      'seq': {
        '1': {
          'ipv4_src_value': '0x00000000',
          'ipv4_src_mask': '0x00000000',
          'ipv4_dst_value': '0x00000000',
          'ipv4_dst_mask': '0x00000000',
          'packet_count': 0,
          'pro': {
            'V': {
              'proto': '0x0',
              'frag': '0x0',
              'tcp_flg': '0x0',
              'tcp_op': '0x0',
              'src_port': '0x0',
              'dst_port': '0x0'
            },
            'M': {
              'proto': '0x0',
              'frag': '0x0',
              'tcp_flg': '0x0',
              'tcp_op': '0x0',
              'src_port': '0x0',
              'dst_port': '0x0'
            }
          },
          'tost': {
            'V': {
              'tos': '0x0',
              'ttl': '0x0',
              'cos': '0x0',
              'v4_opt': '0x0',
              'src_obj': '0x0',
              'dst_obj': '0x0'
            },
            'M': {
              'tos': '0x0',
              'ttl': '0x0',
              'cos': '0x0',
              'v4_opt': '0x0',
              'src_obj': '0x0',
              'dst_obj': '0x0'
            }
          },
          'counter_asic': '0',
          'counter_oid': '0xB3D',
          'result': 'PERMIT',
          'logging': 'NONE'
        },
        '2': {
          'ipv4_src_value': '0x00000000',
          'ipv4_src_mask': '0x00000000',
          'ipv4_dst_value': '0x00000000',
          'ipv4_dst_mask': '0x00000000',
          'packet_count': 0,
          'pro': {
            'V': {
              'proto': '0x11',
              'frag': '0x0',
              'tcp_flg': '0x0',
              'tcp_op': '0x0',
              'src_port': '0x44',
              'dst_port': '0x43'
            },
            'M': {
              'proto': '0xff',
              'frag': '0x0',
              'tcp_flg': '0x0',
              'tcp_op': '0x0',
              'src_port': '0xffff',
              'dst_port': '0xffff'
            }
          },
          'tost': {
            'V': {
              'tos': '0x0',
              'ttl': '0x0',
              'cos': '0x0',
              'v4_opt': '0x0',
              'src_obj': '0x0',
              'dst_obj': '0x0'
            },
            'M': {
              'tos': '0x0',
              'ttl': '0x0',
              'cos': '0x0',
              'v4_opt': '0x0',
              'src_obj': '0x0',
              'dst_obj': '0x0'
            }
          },
          'counter_asic': '0',
          'counter_oid': '0xB3E',
          'result': 'PERMIT',
          'logging': 'NONE'
        }
      }
    }
  }
}
