expected_output = {
     'vrf': {
         'vrf-blue': {
             'address_family': {
                 'ipv4': {
                     'routes': {
                         '172.16.10.10/32': {
                             'active': True,
                             'metric': 0,
                             'next_hop': {
                                 'next_hop_list': {
                                     1: {
                                         'index': 1,
                                         'next_hop': '10.0.0.2',
                                         'updated': '00:04:47',
                                         'vrf': 'vrf-red',
                                     },
                                 },
                             },
                             'route': '172.16.10.10/32',
                             'route_preference': 200,
                             'source_protocol': 'bgp',
                             'source_protocol_codes': 'B',
                         },
                         '192.168.1.0/24': {
                             'active': True,
                             'next_hop': {
                                 'outgoing_interface': {
                                     'GigabitEthernet2': {
                                         'outgoing_interface': 'GigabitEthernet2',
                                     },
                                 },
                             },
                             'route': '192.168.1.0/24',
                             'source_protocol': 'connected',
                             'source_protocol_codes': 'C',
                         },
                         '192.168.1.1/32': {
                             'active': True,
                             'next_hop': {
                                 'outgoing_interface': {
                                     'GigabitEthernet2': {
                                         'outgoing_interface': 'GigabitEthernet2',
                                     },
                                 },
                             },
                             'route': '192.168.1.1/32',
                             'source_protocol': 'local',
                             'source_protocol_codes': 'L',
                         },
                         '192.168.11.11/32': {
                             'active': True,
                             'metric': 130816,
                             'next_hop': {
                                 'next_hop_list': {
                                     1: {
                                         'index': 1,
                                         'next_hop': '192.168.1.2',
                                         'outgoing_interface': 'GigabitEthernet2',
                                         'updated': '01:03:35',
                                     },
                                 },
                             },
                             'route': '192.168.11.11/32',
                             'route_preference': 90,
                             'source_protocol': 'eigrp',
                             'source_protocol_codes': 'D',
                         },
                     },
                 },
             },
         },
     },
 }
