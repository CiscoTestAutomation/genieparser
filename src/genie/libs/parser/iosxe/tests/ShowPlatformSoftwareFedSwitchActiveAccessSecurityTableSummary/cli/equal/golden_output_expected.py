expected_output={
  'access_security_table_summary': {
    'mac_client_port_and_mac_entries': {
      1: {
        'interface': 'Gi2/0/34',
        'mac': 'B07D.479E.7D8D',
        'logical_id': 0,
        'position': 4096,
        'asic': 0,
        'auth_act': 'FWD_ALL_LRN_DATA',
        'restore_auth_act': 'None',
        'flag': 'NONE',
        'drop': 'No',
        'ovrd_vlan': 0,
        'policy': 'IPv4v6',
        'policy_oid': 2796,
        'packets': 3
      },
      2: {
        'interface': 'Gi2/0/31',
        'mac': 'B07D.479E.7D8A',
        'logical_id': 1,
        'position': 4097,
        'asic': 0,
        'auth_act': 'FWD_ALL_LRN_ALL',
        'restore_auth_act': 'None',
        'flag': 'NONE',
        'drop': 'No',
        'ovrd_vlan': 1100,
        'policy': 'IPv4v6',
        'policy_oid': 2800,
        'packets': 3
      }
    },
    'secure_mac_client_port_vlan_and_mac_entries': {
      1: {
        'interface': 'Gi2/0/37',
        'vlan': 100,
        'mac': 'B07D.479E.7D90',
        'logical_id': 0,
        'position': 12288,
        'asic': 0,
        'auth_act': 'FWD_ALL_LRN_DATA',
        'restore_auth_act': 'None',
        'flag': 'NONE',
        'drop': 'No',
        'policy': 'NONE',
        'policy_oid': 569,
        'packets': 0
      }
    },
    'default_client_port_only_entries': {
      1: {
        'interface': 'Gi2/0/34',
        'logical_id': 0,
        'position': 24576,
        'asic': 0,
        'auth_act': 'DROP_ALL_LRN_DATA',
        'restore_auth_act': 'None',
        'flag': 'NONE',
        'policy_oid': 573,
        'packets': 2
      }
    }
  }
}
