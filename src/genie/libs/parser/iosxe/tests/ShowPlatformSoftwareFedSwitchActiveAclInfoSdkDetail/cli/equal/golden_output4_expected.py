expected_output = {
  'class_group_name': {
    'IPACL_PO1_OUT': {
      'direction': 'Egress',
      'feature': 'Racl',
      'protocol': 'IPv4',
      'cg_id': 9,
      'pol_hdl': '0xac061058',
      'oid': '0x1152',
      'no_of_ace': 6,
      'ipv4_ace_key_mask': {
        'ipv4_src_value': '0.0.0.0',
        'ipv4_src_mask': '0.0.0.0',
        'ipv4_dst_value': '225.0.1.1',
        'ipv4_dst_mask': '255.255.255.255',
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
          'mir_cum': '0x0',
          'mir_cmd': '0x0',
          'counter': '0x0',
          'counter_value': 0
        }
      },
      'ipv4_ace_key_mask_1': {
        'ipv4_src_value': '0.0.0.0',
        'ipv4_src_mask': '0.0.0.0',
        'ipv4_dst_value': '225.0.1.2',
        'ipv4_dst_mask': '255.255.255.255',
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
          'mir_cum': '0x0',
          'mir_cmd': '0x0',
          'counter': '0x0',
          'counter_value': 0
        }
      },
      'ipv4_ace_key_mask_2': {
        'ipv4_src_value': '0.0.0.0',
        'ipv4_src_mask': '0.0.0.0',
        'ipv4_dst_value': '224.0.0.0',
        'ipv4_dst_mask': '255.255.255.0',
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
          'mir_cum': '0x0',
          'mir_cmd': '0x0',
          'counter': '0x0',
          'counter_value': 0
        }
      },
      'ipv4_ace_key_mask_3': {
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
          'punt': 'Y',
          'drop': 'N',
          'mirror': 'N',
          'mir_cum': '0x0',
          'mir_cmd': '0x0',
          'counter': '0x1153',
          'counter_value': 0
        }
      },
      'ipv4_ace_key_mask_4': {
        'ipv4_src_value': '0.0.0.0',
        'ipv4_src_mask': '0.0.0.0',
        'ipv4_dst_value': '224.0.0.0',
        'ipv4_dst_mask': '255.255.255.0',
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
          'mir_cum': '0x0',
          'mir_cmd': '0x0',
          'counter': '0x0',
          'counter_value': 0
        }
      },
      'ipv4_ace_key_mask_5': {
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
          'punt': 'Y',
          'drop': 'N',
          'mirror': 'N',
          'mir_cum': '0x0',
          'mir_cmd': '0x0',
          'counter': '0x1155',
          'counter_value': 0
        }
      }
    },
    'IPACLv6_PO1_OUT': {
      'direction': 'Egress',
      'feature': 'Racl',
      'protocol': 'IPv6',
      'cg_id': 10,
      'pol_hdl': '0xac067be8',
      'oid': '0x1157',
      'no_of_ace': 8,
      'ipv6_ace_key_mask': {
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
          'mir_cum': '0x0',
          'mir_cmd': '0x0',
          'counter': '0x0',
          'counter_value': 0
        }
      },
      'ipv6_ace_key_mask_1': {
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
          'mir_cum': '0x0',
          'mir_cmd': '0x0',
          'counter': '0x0',
          'counter_value': 0
        }
      },
      'ipv6_ace_key_mask_2': {
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
          'mir_cum': '0x0',
          'mir_cmd': '0x0',
          'counter': '0x0',
          'counter_value': 0
        }
      },
      'ipv6_ace_key_mask_3': {
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
          'punt': 'Y',
          'drop': 'N',
          'mirror': 'N',
          'mir_cum': '0x0',
          'mir_cmd': '0x0',
          'counter': '0x1158',
          'counter_value': 0
        }
      },
      'ipv6_ace_key_mask_4': {
        'V': {
          'proto': '0x3a',
          'tos': '0x0',
          'tcp_flg': '0x0',
          'ttl': '0x0',
          'ipv4_flags': '0x0',
          'src_port': '0x0',
          'dst_port': '0x0'
        },
        'M': {
          'proto': '0xff',
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
          'mir_cum': '0x0',
          'mir_cmd': '0x0',
          'counter': '0x0',
          'counter_value': 0
        }
      },
      'ipv6_ace_key_mask_5': {
        'V': {
          'proto': '0x3a',
          'tos': '0x0',
          'tcp_flg': '0x0',
          'ttl': '0x0',
          'ipv4_flags': '0x0',
          'src_port': '0x0',
          'dst_port': '0x0'
        },
        'M': {
          'proto': '0xff',
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
          'mir_cum': '0x0',
          'mir_cmd': '0x0',
          'counter': '0x0',
          'counter_value': 0
        }
      },
      'ipv6_ace_key_mask_6': {
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
          'mir_cum': '0x0',
          'mir_cmd': '0x0',
          'counter': '0x0',
          'counter_value': 0
        }
      },
      'ipv6_ace_key_mask_7': {
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
          'punt': 'Y',
          'drop': 'N',
          'mirror': 'N',
          'mir_cum': '0x0',
          'mir_cmd': '0x0',
          'counter': '0x1159',
          'counter_value': 0
        }
      }
    }
  }
}
