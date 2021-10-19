
expected_output={
    'interfaces': { 
        'Dialer2': {
            'bandwidth': 250000,
            'description': 'TEST',
            'dialer_down_with_vinterface': True,
            'dialer_group': 2,
            'dialer_pool': 2,
            'encapsulation': {
                'type': 'ppp',
            },
            'ip_tcp_adjust_mss': 1452,
            'ipv4_negotiated': True,
            'ip_mtu': 1492,
            'ip_verify': { 'mode': 'rx',
                            'options': ['allow-default', 'allow-self-ping']},
            'ipv6': [ 'FE80::C100:14:100 link-local',
                        'IPV6-DELEGATION2 ::B/64'],
            'ipv6_enable': True,
            'ipv6_mtu': 1492,
            'ipv6_verify': { 'mode': 'rx',
                            'options': ['allow-default']},
            'ipv6_tcp_adjust_mss': 1432,
            'mtu': 1492,
            'ppp_chap_hostname': 'user@realm.isp',
            'ppp_chap_password': { 'encryption_type': 0,
                                    'password': 'password'},
            'service_policy_output': 'SHAPING'
        }
    }
}