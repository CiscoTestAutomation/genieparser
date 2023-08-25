expected_output = {
    'prefixes': {
        '::ffff:10.0.0.1': {
            'iid': '0xa000001',
            'prefix': '::ffff:10.0.0.1',
            'context': '[EVPN-VPWS:evi=1001:eth_tag=10001:type=0]',
            'owner': 'l2vpn_iid',
            'state': 'InUse',
            'read_write': 'Y'
        },
        '::ffff:10.0.0.2': {
            'iid': '0xa000002',
            'prefix': '::ffff:10.0.0.2',
            'context': '[EVPN-ELAN:evi=1002:esi=0194.aef0.f99c.dd00.2400:nh=:::eth_tag=0:type=0]',
            'owner': 'l2vpn_iid',
            'state': 'InUse',
            'read_write': 'Y'
        },
        '::ffff:10.0.0.3': {
            'iid': '0xa000003',
            'prefix': '::ffff:10.0.0.3',
            'context': '[EVPN-ELAN:evi=1002:esi=01b0.a651.645c.dd00.2f00:nh=:::eth_tag=0:type=0]',
            'owner': 'l2vpn_iid',
            'state': 'InUse',
            'read_write': 'Y'
        }
    }
}
