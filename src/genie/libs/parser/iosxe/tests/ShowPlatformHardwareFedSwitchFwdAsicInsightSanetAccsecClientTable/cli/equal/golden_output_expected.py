expected_output = {
  'entries': {
    1: {
      'mask': 'P_MAC',
      'sysport_gid': 579,
      'mac': '0000.9922.2222',
      'vlan': 0,
      'client_pid': 5,
      'client_vlan': 50,
      'drop': 0,
      'policy': 'IPv4v6',
      'ovrd_vlan': 1
    },
    2: {
      'mask': 'P_MAC_V',
      'sysport_gid': 579,
      'mac': '0000.9922.2222',
      'vlan': 50,
      'client_pid': 2,
      'client_vlan': 0,
      'drop': 0,
      'policy': 'NONE',
      'ovrd_vlan': 0
    },
    3: {
      'mask': 'P',
      'sysport_gid': 579,
      'mac': '0000.0000.0000',
      'vlan': 0,
      'client_pid': 4,
      'client_vlan': 0,
      'drop': 0,
      'policy': 'NONE',
      'ovrd_vlan': 0
    }
  },
  'mask_type': {
    'P': 'Port_id 0xff',
    'MAC': 'MAC FFFF.FFFF.FFFF',
    'V': 'Vid 0xfff'
  }
}
