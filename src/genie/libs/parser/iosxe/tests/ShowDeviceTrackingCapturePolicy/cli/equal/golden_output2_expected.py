expected_output={
  'target_db': {
    'vlan 30': {
      'hw_policy_signature': '0001DF9F',
      'policies': 1,
      'rules': 14,
      'sig': '0001DF9F',
      'sw_policy': {
        'policy': 'default',
        'feature': 'Device-tracking - Active'
      },
      'mask_id': {
        '00000400': {
          'rule': 'DHCP4 CLIENT',
          'protocol': 'UDP',
          'mask': '00000400',
          'action': 'PUNT',
          'match1': 0,
          'match2': 67,
          'feat': '1'
        },
        '00001000': {
          'rule': 'DHCP4 SERVER SOURCE',
          'protocol': 'UDP',
          'mask': '00001000',
          'action': 'PUNT',
          'match1': 0,
          'match2': 68,
          'feat': '1'
        },
        '00000800': {
          'rule': 'DHCP4 SERVER',
          'protocol': 'UDP',
          'mask': '00000800',
          'action': 'PUNT',
          'match1': 67,
          'match2': 0,
          'feat': '1'
        },
        '00004000': {
          'rule': 'ARP',
          'protocol': 'IPV4',
          'mask': '00004000',
          'action': 'PUNT',
          'match1': 0,
          'match2': 0,
          'feat': '1'
        },
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
        '00000001': {
          'rule': 'NS',
          'protocol': 'ICMPV6',
          'mask': '00000001',
          'action': 'PUNT',
          'match1': 135,
          'match2': 0,
          'feat': '1'
        },
        '00000002': {
          'rule': 'NA',
          'protocol': 'ICMPV6',
          'mask': '00000002',
          'action': 'PUNT',
          'match1': 136,
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
        },
        '00008000': {
          'rule': 'DAR',
          'protocol': 'ICMPV6',
          'mask': '00008000',
          'action': 'PUNT',
          'match1': 157,
          'match2': 0,
          'feat': '1'
        },
        '00010000': {
          'rule': 'DAC',
          'protocol': 'ICMPV6',
          'mask': '00010000',
          'action': 'PUNT',
          'match1': 158,
          'match2': 0,
          'feat': '1'
        }
      }
    }
  }
}
