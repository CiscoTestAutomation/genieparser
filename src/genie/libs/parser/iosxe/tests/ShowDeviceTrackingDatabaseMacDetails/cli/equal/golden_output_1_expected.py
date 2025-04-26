expected_output={
  'device': {
    1: {
      'dev_code': 'L',
      'link_layer_address': '00ea.bd88.0448',
      'interface': 'Vl201',
      'vlan_id': 201,
      'pref_level': 'TRUSTED',
      'state': 'MAC-REACHABLE',
      'policy': 'evpn-device-track',
      'time_left': 'N/A',
      'input_index': 158,
      'attached': {
        1: {
          'ip': '192.168.1.200'
        }
      }
    },
    2: {
      'dev_code': 'L3F',
      'link_layer_address': '0000.0000.0001',
      'interface': 'Gi2/0/3',
      'vlan_id': 202,
      'pref_level': 'NO TRUST',
      'state': 'MAC-STALE',
      'policy': 'evpn-device-track',
      'time_left': '93559 s',
      'input_index': 34,
      'attached': {
        1: {
          'ip': '192.168.1.201'
        }
      }
    }
  }
}