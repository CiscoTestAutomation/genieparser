expected_output={
   'ip_address': {
      '10.1.1.101': {
            'filter_mode': 'active',
            'filter_type': 'ip-mac',
            'interface_name': 'Gi1/0/13',
            'mac_address': '00:0A:00:0B:00:01',
            'vlan': '10',
      },
      '10.1.1.85': {
            'filter_mode': 'active',
            'filter_type': 'ip-mac',
            'interface_name': 'Te7/0/37',
            'mac_address': '50:06:04:84:C2:77',
            'vlan': '10',
      },
      'deny-all': {
            'filter_mode': 'active',
            'filter_type': 'ip-mac',
            'interface_name': 'Gi2/0/13',
            'mac_address': 'deny-all',
            'vlan': '10,20,120',
      },
   },
}