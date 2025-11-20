expected_output = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'instance': {
                            '1': {
                                'areas': {
                                    '0.0.0.0': {
                                        'database': {
                                            'lsa_types': {
                                                10: {
                                                    'lsa_type': 10,
                                                    'lsas': {
                                                        '8.0.0.15 1.1.1.2': {
                                                            'adv_router': '1.1.1.2',
                                                            'lsa_id': '8.0.0.15',
                                                            'ospfv2': {
                                                                'header': {
                                                                    'age': 198,
                                                                    'option': 'None',
                                                                    'option_desc': 'No TOS-capability, DC',
                                                                    'type': 10,
                                                                    'lsa_id': '8.0.0.15',
                                                                    'adv_router': '1.1.1.2',
                                                                    'opaque_type': 8,
                                                                    'opaque_id': 15,
                                                                    'seq_num': '80000001',
                                                                    'checksum': '0x124b',
                                                                    'length': 108,
                                                                    },
                                                                'body': {
                                                                    'opaque': {
                                                                        'extended_link_tlvs': {
                                                                            1: {
                                                                                'length': 84,
                                                                                'link_type': 1,
                                                                                'link_id': '1.1.1.3',
                                                                                'link_data': '99.3.2.1',
                                                                                'sub_tlvs': {
                                                                                    1: {
                                                                                        'length': 8,
                                                                                        'type': 'Local-ID Remote-ID',
                                                                                        'local_interface_id': 15,
                                                                                        'remote_interface_id': 16,
                                                                                        },
                                                                                    2: {
                                                                                        'length': 4,
                                                                                        'type': 'Remote If Address',
                                                                                        'neighbor_address': '99.3.2.2',
                                                                                        },
                                                                                    3: {
                                                                                        'type': 'Opaque link info',
                                                                                        'length': 24,
                                                                                        'opaque_type': 32770,
                                                                                        'enterprise_num': 9,
                                                                                        'opaque_value': '76312e30302d494c412d435f305f305f30202020',
                                                                                        },
                                                                                    },
                                                                                },
                                                                            },
                                                                        },
                                                                    },
                                                                },
                                                            },
                                                        } ,
                                                        },
                                                      },
                                                    },
                                                  },
                                                },
                                              },
                                            },
                                          },
                                        },
                                      },
                                    },
                                  }
