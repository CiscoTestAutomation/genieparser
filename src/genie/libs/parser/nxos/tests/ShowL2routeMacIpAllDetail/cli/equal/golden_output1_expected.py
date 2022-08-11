expected_output = {
  'topology': {
    'topo_id': {
     1001: {
      'mac_ip': {
       '0011.01ff.0001': {
        'mac_addr': '0011.01ff.0001',
        'mac_ip_prod_type': 'hmm',
        'mac_ip_flags': '--',
        'seq_num': 0,
        'next_hop1': 'local',
        'host_ip': '2001:db8:646::1',
       },
       '0011.01ff.0002': {
        'mac_addr': '0011.01ff.0002',
        'mac_ip_prod_type': 'bgp',
        'mac_ip_flags': '--',
        'seq_num': 0,
        'next_hop1': '2001:1:4::1',
        'host_ip': '2001:1:1::1',
       },
       'fa16.3eff.f6c1': {
        'mac_addr': 'fa16.3eff.f6c1',
        'mac_ip_prod_type': 'bgp',
        'mac_ip_flags': '--',
        'seq_num': 0,
        'next_hop1': '192.168.106.1',
        'host_ip': '10.36.10.11',
       },
       'fa16.3eff.9f0a': {
        'mac_addr': 'fa16.3eff.9f0a',
        'mac_ip_prod_type': 'hmm',
        'mac_ip_flags': '--',
        'seq_num': 0,
        'next_hop1': 'local',
        'host_ip': '10.36.10.55',
        'sent_to': 'bgp',
        'soo': 774975538,
        'l3_info': 10001,
       },
      },
     },
    }
  }
}
