expected_output={
  'target_db': {
    'Gi1/0/4': {
      'hw_policy_signature': '0000039C',
      'policies': 2,
      'rules': 6,
      'sig': '0000039C',
      'sw_policy': {
        'policy': 'ra_host',
        'feature': 'RA guard - Active'
      },
      'mask_id': {
        '00000200': {
          'rule': 'DHCP SERVER SOURCE',
          'protocol': 'UDP',
          'mask': '00000200',
          'action': 'PUNT',
          'match1': 0,
          'match2': 546,
          'feat': '1'
        },
        '00000080': {
          'rule': 'DHCP CLIENT',
          'protocol': 'UDP',
          'mask': '00000080',
          'action': 'PUNT',
          'match1': 0,
          'match2': 547,
          'feat': '1'
        },
        '00000100': {
          'rule': 'DHCP SERVER',
          'protocol': 'UDP',
          'mask': '00000100',
          'action': 'PUNT',
          'match1': 547,
          'match2': 0,
          'feat': '1'
        },
        '00000004': {
          'rule': 'RS',
          'protocol': 'ICMPV6',
          'mask': '00000004',
          'action': 'PUNT',
          'match1': 133,
          'match2': 0,
          'feat': '1'
        },
        '00000008': {
          'rule': 'RA',
          'protocol': 'ICMPV6',
          'mask': '00000008',
          'action': 'PUNT',
          'match1': 134,
          'match2': 0,
          'feat': '1'
        },
        '00000010': {
          'rule': 'REDIR',
          'protocol': 'ICMPV6',
          'mask': '00000010',
          'action': 'PUNT',
          'match1': 137,
          'match2': 0,
          'feat': '1'
        }
      }
    }
  }
}
