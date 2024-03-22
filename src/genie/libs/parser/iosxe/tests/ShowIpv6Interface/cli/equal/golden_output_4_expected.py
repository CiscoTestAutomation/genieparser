expected_output={
    'GigabitEthernet1/0/11': {
         'addresses_config_method': 'DHCP',
         'enabled': True,
         'ipv6': {
             '2001:db8:8548:1::1/64': {
                 'ip': '2001:db8:8548:1::1',
                 'prefix_length': '64',
                 'status': 'valid',
             },
             'FE80::F816:3EFF:FE19:ABBA': {
                 'ip': 'FE80::F816:3EFF:FE19:ABBA',
                 'origin': 'link_layer',
                 'status': 'valid',
             },
             'enabled': True,
             'nd': {
                 'advertised_default_router_preference': 'Medium',
                 'suppress': False,
             },
         },
         'oper_status': 'up',
     },

}