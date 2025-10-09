expected_output={
  'vlan': 50,
  'multicast_group_id': {
    'oid': 11177,
    'asic': 0
  },
  'gid': '0x2016',
  'punject_switch_profile': True,
  'trusted_ports': {
    'Port-channel120': {
      'interface_id': '0x000004da',
      'po_id': '0x00000000'
    },
    'GigabitEthernet2/0/25': {
      'interface_id': '0x00000421',
      'po_id': '0x000004da'
    },
    'GigabitEthernet3/0/3': {
      'interface_id': '0x00000495',
      'po_id': '0x000004da'
    }
  },
  'acl_info': {
    'oid': 547,
    'asic': 0,
    'entries': {
      0: {
        'position': 0,
        'protocol': 'UDP',
        'src_port': 68,
        'dst_port': 67,
        'action': 'PUNT',
        'counter_oid': 548
      },
      1: {
        'position': 1,
        'protocol': 'UDP',
        'src_port': 67,
        'dst_port': 68,
        'action': 'PUNT',
        'counter_oid': 548
      },
      2: {
        'position': 2,
        'protocol': 'UDP',
        'src_port': 67,
        'dst_port': 67,
        'action': 'PUNT',
        'counter_oid': 548
      }
    }
  }
}
