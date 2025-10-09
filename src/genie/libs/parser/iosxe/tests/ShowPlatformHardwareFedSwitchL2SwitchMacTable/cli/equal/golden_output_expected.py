expected_output={
  'mac_table': {
    'mac_address': {
      '00:aa:00:bb:00:01': {
        'switch_gid': '100',
        'dest_type': 'L2_DENSE_PORT',
        'dest_cookie': 'Gi2/0/6',
        'aging': 'static',
        'switch_cookie': '100'
      },
      '00:aa:00:bb:00:02': {
        'switch_gid': '100',
        'dest_type': 'L2_DENSE_PORT',
        'dest_cookie': 'Gi1/0/4',
        'aging': 'dynamic',
        'switch_cookie': '100'
      },
      '00:11:00:22:00:33': {
        'switch_gid': '100',
        'dest_type': 'L2_DENSE_PORT',
        'dest_cookie': 'Gi2/0/6',
        'aging': 'static',
        'switch_cookie': '100'
      },
      '70:6b:b9:28:e3:83': {
        'switch_gid': '100',
        'dest_type': 'L2_DENSE_PORT',
        'dest_cookie': 'Gi2/0/6',
        'aging': 'static',
        'switch_cookie': '100'
      },
      '00:01:02:02:aa:be': {
        'switch_gid': '100',
        'dest_type': 'L2_DENSE_PORT',
        'dest_cookie': 'Gi1/0/4',
        'aging': 'dynamic',
        'switch_cookie': '100'
      }
    }
  }
}
