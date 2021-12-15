expected_output = {
    'lisp_id': {
        0: {
            'instance_id': {
                4100: {
                    'lisp_virtual_intf': 'LISP0.4100',
                    'user': 'LISP',
                    'eid_vrf': {
                        'red (0x2)': {
                            'address_family': {
                                'IPv4': {
                                    'configured_roles': ['ETR', 'PITR'],
                                    'eid_table': 'IPv4:red',
                                    'alt_table': '<null>',
                                    'locator_status_bit': 'Disabled',
                                    'nonce': 'N/A',
                                    'ttl_propagation': 'Enabled',
                                    'table_supression': 'Disabled',
                                    'sgt_policy_fwd': 'Disabled'
                                    },
                                'IPv6': {
                                    'configured_roles': ['ETR', 'PITR'],
                                    'eid_table': 'IPv6:red',
                                    'alt_table': '<null>',
                                    'locator_status_bit': 'Disabled',
                                    'nonce': 'N/A',
                                    'ttl_propagation': 'Enabled',
                                    'table_supression': 'Disabled',
                                    'sgt_policy_fwd': 'Disabled'
                                    },
                                'L2': {
                                    'l2_domain_id': 0,
                                    'ipv4_unnum_if': 'N/A',
                                    'ipv6_unnum_if': 'N/A'
                                    }
                                },
                            'rloc_transport': {
                                'vrf': 'Default',
                                'ipv4_rloc_table': 'IPv4:Default',
                                'ipv6_rloc_table': 'IPv6:Default',
                                'ipv4_path_mtu_discovery': {
                                    'min': 576,
                                    'max': 65535
                                    },
                                'ipv6_path_mtu_discovery': {
                                    'min': 1280,
                                    'max': 65535
                                    },
                                'ipv4_rloc_fltr_handle': '0x0',
                                'ipv6_rloc_fltr_handle': '0x0'
                                }
                            }
                        }
                    }
                }
            }
        }
    }