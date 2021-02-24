expected_output = {
  'interfaces': {
    'ethernet1/1': {
      'ip': '10.254.32.221',
      'ok': 'YES',
      'method': 'NVRAM',
      'status': 'admin/down',
      'protocol': 'down',
      'vrf': 'default-vrf'
    },
    'ethernet5/1': {
      'ip': '10.254.32.3',
      'ok': 'YES',
      'method': 'NVRAM',
      'status': 'up',
      'protocol': 'up',
      'vrf': 'default-vrf'
    },
    'ethernet7/1': {
      'ip': '10.254.32.109',
      'ok': 'YES',
      'method': 'manual',
      'status': 'up',
      'protocol': 'up',
      'vrf': 'default-vrf'
    },
    've150': {
      'ip': '10.15.15.2',
      'ok': 'YES',
      'method': 'NVRAM',
      'status': 'up',
      'protocol': 'up',
      'vrf': 'default-vrf',
      'flag': 'VS'
    },
    'management1': {
      'ip': '172.16.15.4',
      'ok': 'YES',
      'method': 'NVRAM',
      'status': 'up',
      'protocol': 'up',
      'vrf': 'oob'
    },
    'loopback1': {
      'ip': '10.69.9.9',
      'ok': 'YES',
      'method': 'NVRAM',
      'status': 'up',
      'protocol': 'up',
      'vrf': 'default-vrf'
    }
  }
}
