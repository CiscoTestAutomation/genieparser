expected_output = {
      'ipv4_add': {
          '2.2.2.3/32': {
              'adj': {
                  'dstmac': '00a7.429b.db7f',
                   'ether_type': '0x8',
                   'iif_id': '0x553',
                   'ipv4_addr': '2.2.2.3',
                   'nh_type': 'NHADJ_NORMAL',
                   'objid': '0x40',
                   'srcmac': '40b5.c1ff.d902'
              },
              'da': 1,
              'ipv4route_id': '0x5a4d1cf0f4d8',
              'mac_addr': '00a7.429b.db7f',
              'npd': {
                  'child_device': 0,
                   'nh_gid': 8,
                   'nh_oid': '0x466',
                   'old_gid': 0,
                   'old_oid': '0x0',
                   'parent_oid': '0x6e6'
              },
                   'obj_id': '0x40',
                   'obj_name': 'IPNEXTHOP_ID',
                   'state': 'success',
                   'tblid': 0
          }
      }
}