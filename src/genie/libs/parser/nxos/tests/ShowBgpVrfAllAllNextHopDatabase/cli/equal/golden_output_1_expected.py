

expected_output = {
    'vrf':
        {'VRF1':
            {'address_family':
                {'ipv4 unicast':
                    {'af_nexthop_trigger_enable': True,
                    'nexthop_trigger_delay_critical': 2222,
                    'nexthop_trigger_delay_non_critical': 3333,
                    'next_hop': {
                        '0.0.0.0': {
                            'igp_cost': 0,
                            'igp_preference': 0,
                            'igp_route_type': 0,
                            'metric_next_advertise': 'never',
                            'resolve_time': 'never',
                            'rib_route': '0.0.0.0/0',
                             'attached': False,
                             'local': True,
                             'reachable': False,
                             'labeled': False,
                             'filtered': False,
                             'pending_update': False,
                            'refcount': 4,
                            'rnh_epoch': 0}}},
                'ipv6 unicast':
                    {'af_nexthop_trigger_enable': True,
                    'nexthop_trigger_delay_critical': 3000,
                    'nexthop_trigger_delay_non_critical': 10000,
                    'next_hop': {
                        '0::': {
                            'igp_cost': 0,
                            'igp_preference': 0,
                            'igp_route_type': 0,
                            'resolve_time': 'never',
                            'rib_route': '0::/0',
                            'metric_next_advertise': 'never',
                             'attached': False,
                             'local': True,
                             'reachable': False,
                             'labeled': False,
                             'filtered': False,
                             'pending_update': False,
                            'refcount': 3,
                            'rnh_epoch': 0}}}}},
        'default':
            {'address_family':
                {'ipv4 unicast':
                    {'af_nexthop_trigger_enable': True,
                    'nexthop_trigger_delay_critical': 3000,
                    'nexthop_trigger_delay_non_critical': 10000},
                'ipv6 label unicast':
                    {'af_nexthop_trigger_enable': True,
                    'nexthop_trigger_delay_critical': 3000,
                    'nexthop_trigger_delay_non_critical': 10000},
                'ipv6 unicast':
                    {'af_nexthop_trigger_enable': True,
                    'nexthop_trigger_delay_critical': 3000,
                    'nexthop_trigger_delay_non_critical': 10000},
                'vpnv4 unicast':
                    {'af_nexthop_trigger_enable': True,
                    'nexthop_trigger_delay_critical': 3000,
                    'nexthop_trigger_delay_non_critical': 10000,
                    'next_hop': {
                        '10.36.3.3': {
                            'attached_nexthop': {
                                '10.1.3.3': {
                                    'attached_nexthop_interface': 'Ethernet4/2',
                                }
                            },
                            'igp_cost': 41,
                            'igp_preference': 110,
                            'igp_route_type': 0,
                            'metric_next_advertise': 'never',
                            'resolve_time': '5w0d',
                            'rib_route': '10.36.3.3/32',
                             'attached': False,
                             'local': False,
                             'reachable': True,
                             'labeled': True,
                             'filtered': False,
                             'pending_update': False,
                            'refcount': 1,
                            'rnh_epoch': 1}}},
                'vpnv6 unicast':
                    {'af_nexthop_trigger_enable': True,
                    'nexthop_trigger_delay_critical': 3000,
                    'nexthop_trigger_delay_non_critical': 10000,
                    'next_hop': {
                        '::ffff:10.36.3.3': {
                            'attached_nexthop': {
                                '10.1.3.3': {
                                    'attached_nexthop_interface': 'Ethernet4/2',
                                }
                            },
                            'igp_cost': 41,
                            'igp_preference': 110,
                            'igp_route_type': 0,
                            'metric_next_advertise': 'never',
                            'resolve_time': '5w0d',
                            'rib_route': '10.36.3.3/32',
                             'attached': False,
                             'local': False,
                             'reachable': True,
                             'labeled': True,
                             'filtered': False,
                             'pending_update': False,
                            'refcount': 1,
                            'rnh_epoch': 1}}}}}}}
