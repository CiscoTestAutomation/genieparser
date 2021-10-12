

expected_output = {
    'vrf':
        {'VRF1':
            {'address_family':
                {'ipv4':
                    {'instance':
                        {'1':
                            {'areas':
                                {'0.0.0.1':
                                    {'mpls':
                                        {'ldp':
                                            {'autoconfig': False,
                                            'autoconfig_area_id': '0.0.0.1',
                                            'igp_sync': False,
                                            'required': False}},
                                    'interfaces':
                                        {'Ethernet2/1':
                                            {'area': '0.0.0.1',
                                            'interface_type': 'broadcast',
                                            'mpls':
                                                {'ldp':
                                                    {'autoconfig': False,
                                                    'autoconfig_area_id': '0.0.0.1',
                                                    'igp_sync': False,
                                                    'required': False}},
                                            'name': 'Ethernet2/1',
                                            'state': 'bdr'}},
                                    'sham_links':
                                        {'10.151.22.22 10.229.11.11':
                                            {'area': '0.0.0.1',
                                            'interface_type': 'point_to_point',
                                            'mpls':
                                                {'ldp':
                                                    {'autoconfig': False,
                                                    'autoconfig_area_id': '0.0.0.1',
                                                    'igp_sync': False,
                                                    'required': False}},
                                            'name': '10.151.22.22 10.229.11.11',
                                            'state': 'point_to_point'},
                                        '10.151.22.22 10.21.33.33':
                                            {'area': '0.0.0.1',
                                            'interface_type': 'point_to_point',
                                            'mpls':
                                                {'ldp':
                                                    {'autoconfig': False,
                                                    'autoconfig_area_id': '0.0.0.1',
                                                    'igp_sync': False,
                                                    'required': False}},
                                            'name': '10.151.22.22 '
                                            '10.21.33.33',
                                            'state': 'point_to_point'}}}}}}}}},
        'default':
            {'address_family':
                {'ipv4':
                    {'instance':
                        {'1':
                            {'areas':
                                {'0.0.0.0':
                                    {'mpls':
                                        {'ldp':
                                            {'autoconfig': False,
                                            'autoconfig_area_id': '0.0.0.0',
                                            'igp_sync': False,
                                            'required': False}},
                                    'interfaces':
                                        {'Ethernet2/2':
                                            {'area': '0.0.0.0',
                                            'interface_type': 'broadcast',
                                            'mpls':
                                                {'ldp':
                                                    {'autoconfig': False,
                                                    'autoconfig_area_id': '0.0.0.0',
                                                    'igp_sync': False,
                                                    'required': False}},
                                            'name': 'Ethernet2/2',
                                            'state': 'bdr'},
                                        'Ethernet2/3':
                                            {'area': '0.0.0.0',
                                            'interface_type': 'broadcast',
                                            'mpls':
                                                {'ldp':
                                                    {'autoconfig': False,
                                                    'autoconfig_area_id': '0.0.0.0',
                                                    'igp_sync': False,
                                                    'required': False}},
                                            'name': 'Ethernet2/3',
                                            'state': 'bdr'},
                                        'Ethernet2/4':
                                            {'area': '0.0.0.0',
                                            'interface_type': 'broadcast',
                                            'mpls':
                                                {'ldp':
                                                    {'autoconfig': False,
                                                    'autoconfig_area_id': '0.0.0.0',
                                                    'igp_sync': False,
                                                    'required': False}},
                                            'name': 'Ethernet2/4',
                                            'state': 'bdr'},
                                        'loopback0':
                                            {'area': '0.0.0.0',
                                            'interface_type': 'loopback',
                                            'mpls':
                                                {'ldp':
                                                    {'autoconfig': False,
                                                    'autoconfig_area_id': '0.0.0.0',
                                                    'igp_sync': False,
                                                    'required': False}},
                                            'name': 'loopback0',
                                            'state': 'loopback'}}}}}}}}},
         'VRF2':
             {'address_family':
                  {'ipv4':
                       {'instance':
                            {'1':
                                 {'areas':
                                      {'0.0.1.1':
                                           {'mpls':
                                                {'ldp':
                                                     {'autoconfig': True,
                                                      'autoconfig_area_id': '0.0.1.1',
                                                      'igp_sync': False,
                                                      'required': False}},
                                           'interfaces':
                                                {'port-channel4001':
                                                     {'area': '0.0.1.1',
                                                      'interface_type': 'point_to_point',
                                                      'mpls':
                                                          {'ldp':
                                                               {'autoconfig': True,
                                                                'autoconfig_area_id': '0.0.1.1',
                                                                'igp_sync': False,
                                                                'required': False}},
                                                      'name': 'port-channel4001',
                                                      'state': 'point_to_point'},
                                                'port-channel4002':
                                                     {'area': '0.0.1.1',
                                                      'interface_type': 'point_to_point',
                                                      'mpls':
                                                          {'ldp':
                                                               {'autoconfig': True,
                                                                'autoconfig_area_id': '0.0.1.1',
                                                                'igp_sync': False,
                                                                'required': False}},
                                                      'name': 'port-channel4002',
                                                      'state': 'point_to_point'}}
                                            }}}}}}}
         }}
