

expected_output = {
    'vrf':{
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
                                                     'igp_sync': True,
                                                     'required': True,
                                                     'achieved': True}},
                                          'interfaces':
                                               {'port-channel4001':
                                                    {'area': '0.0.1.1',
                                                     'interface_type': 'point_to_point',
                                                     'mpls':
                                                         {'ldp':
                                                              {'autoconfig': True,
                                                               'autoconfig_area_id': '0.0.1.1',
                                                               'igp_sync': True,
                                                               'required': True,
                                                               'achieved': True}},
                                                     'name': 'port-channel4001',
                                                     'state': 'point_to_point'},
                                               'port-channel4002':
                                                    {'area': '0.0.1.1',
                                                     'interface_type': 'point_to_point',
                                                     'mpls':
                                                         {'ldp':
                                                              {'autoconfig': True,
                                                               'autoconfig_area_id': '0.0.1.1',
                                                               'igp_sync': True,
                                                               'required': True,
                                                               'achieved': True}},
                                                     'name': 'port-channel4002',
                                                     'state': 'point_to_point'}}
                                           }}}}}}}}}
