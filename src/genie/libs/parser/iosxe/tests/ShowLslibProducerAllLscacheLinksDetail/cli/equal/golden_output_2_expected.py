expected_output = {
  'link': {
    1: {
      'protocol': 'OSPF',
      'identifier': '0xFFFE',
      'local_node_descriptor': {
        'as_number': 65535,
        'bgp_identifier': '0.1.0.0',
        'area_id': '0.0.0.0',
        'router_id': '11.1.1.1'
      },
      'remote_node_descriptor': {
        'as_number': 65535,
        'bgp_identifier': '0.1.0.0',
        'area_id': '0.0.0.0',
        'router_id': '22.2.2.2'
      },
      'link_descriptor': {
        'link_id': '1.2',
        'local_intf_address': '1.2.0.12',
        'neighbor_intf_address': '1.2.0.21'
      },
      'internal_flag': '0x0',
      'action': 'Update',
      'merged_link_attr': {
        'admin_group': '0x00000001',
        'max_link_bw': 9,
        'max_reserv_link_bw': 17,
        'max_unreserv_link_bw': [9, 9, 9, 9, 9, 9, 9, 9],
        'te_default_metric': 301989888,
        'link_protection_type': '0x1200',
        'mpls_proto_mask': '0x12',
        'srlg': [18, 4608, 1184256, 303174144, 1184256, 4608, 18],
        'opaque_link_attr': '0x4C.0x69.0x6E.0x6B.0x20.0x4F.0x6E.0x65.0x20.0x54.0x77 0x6F.0x00',
        'link_name': 'L12',
        'adj_sid': ['18(0x1)', '1184256(0x3)'],
        'lan_adj_sid': ['4608(0x2)(18.0.18.0)', '303174144(0x4)(18.0.18.0)'],
        'extended_admin_group': '0x00000040 0x00000080',
        'link_delay': 1179648,
        'min_delay': 18,
        'max_delay': 1179666,
        'delay_variation': 1184274,
        'link_loss': '18 * 0.000003 (A)',
        'residual_bw': 9,
        'available_bw': 9,
        'utilized_bw': 9
      }
    }
  }
}
