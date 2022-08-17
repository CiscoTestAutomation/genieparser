

expected_output = {
'bgp': {'instance': {'default': {'bgp_id': 65535,
                                  'protocol_shutdown': False,
                                  'vrf': {'default': {'af_name': {'ipv4 unicast': {}},
                                                      'enforce_first_as': True,
                                                      'fast_external_fallover': True,
                                                      'flush_routes': False,
                                                      'graceful_restart': True,
                                                      'isolate': False,
                                                      'log_neighbor_changes': False},
                                          'test1': {'enforce_first_as': True,
                                                    'fast_external_fallover': True,
                                                    'flush_routes': False,
                                                    'graceful_restart': True,
                                                    'isolate': False,
                                                    'log_neighbor_changes': False,
                                                    'neighbor_id': {'1.1.1.1': {'nbr_description': 'SimpleDescription',
                                                                                'nbr_fall_over_bfd': False,
                                                                                'nbr_suppress_four_byte_as_capability': False}}},
                                          'test2': {'enforce_first_as': True,
                                                    'fast_external_fallover': True,
                                                    'flush_routes': False,
                                                    'graceful_restart': True,
                                                    'isolate': False,
                                                    'log_neighbor_changes': False,
                                                    'neighbor_id': {'2.2.2.2': {'nbr_description': 'More-"complex" '
                                                                                                   'Description_1234!',
                                                                                'nbr_fall_over_bfd': False,
                                                                                'nbr_suppress_four_byte_as_capability': False}}}}}}}
}
