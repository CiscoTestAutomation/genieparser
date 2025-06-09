expected_output={
  'fed_arp_snooping_vlan_data': {
    'vlan': 50,
    'punject_switch_profile': True,
    'arp_snoop_enable': True,
    'acl_info': {
      'asic': 0,
      'oid': 552,
      'entries': [
        {
          'position': 0,
          'action': 'PUNT',
          'counter_oid': 553
        }
      ]
    }
  }
}
