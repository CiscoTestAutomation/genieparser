
expected_output = {
  'interfaces':{
    'Port-channel1.3': {
      'encapsulation': {
        'dot1q': 10,
        'dot1q_native': False,
        'type': 'dot1Q',
        'second_dot1q': '20',
        },
        'ipv4': { 'ip': '4.4.4.4',
                  'netmask': '255.255.255.248'},
        'vrf': 'TEST'
      }
    }
}