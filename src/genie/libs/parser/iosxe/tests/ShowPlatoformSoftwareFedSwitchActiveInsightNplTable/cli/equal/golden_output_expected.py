expected_output={
  'entries': {
    1: {
      'key': {
        'get_field_by_name': '<bound method npl_dot1x_client_table_key_t.get_field_by_name',
        'port': {
          'id': '0x38',
          'smac': '0x222222',
          'vid': '0x0'
        }
      },
      'loc': '0x0',
      'mask': {
        'get_field_by_name': '<bound method npl_dot1x_client_table_key_t.get_field_by_name',
        'port': {
          'id': '0xff',
          'smac': '0xffffffffffff',
          'vid': '0x0'
        }
      },
      'value': {
        'action': 'NPL_DOT1X_CLIENT_TABLE_ACTION_WRITE(0x0)',
        'payloads': {
          'result_table': {
            'client_policy_id': '0x7',
            'client_vlan': '0x32',
            'drop': '0x0',
            'ipv4_policy_valid': '0x1',
            'ipv6_policy_valid': '0x1',
            'vlan_overwrite': '0x1'
          }
        }
      }
    },
    2: {
      'key': {
        'get_field_by_name': '<bound method npl_dot1x_client_table_key_t.get_field_by_name',
        'port': {
          'id': '0x38',
          'smac': '0x222222',
          'vid': '0x32'
        }
      },
      'loc': '0x1',
      'mask': {
        'get_field_by_name': '<bound method npl_dot1x_client_table_key_t.get_field_by_name',
        'port': {
          'id': '0xff',
          'smac': '0xffffffffffff',
          'vid': '0xfff'
        }
      },
      'value': {
        'action': 'NPL_DOT1X_CLIENT_TABLE_ACTION_WRITE(0x0)',
        'payloads': {
          'result_table': {
            'client_policy_id': '0x2',
            'client_vlan': '0x0',
            'drop': '0x0',
            'ipv4_policy_valid': '0x0',
            'ipv6_policy_valid': '0x0',
            'vlan_overwrite': '0x0'
          }
        }
      }
    }
  }
}
