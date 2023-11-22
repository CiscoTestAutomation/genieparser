expected_output = {
    'instance': {
        'default': {
            'vrf': {
                'evi_3': {
                    'address_family': {
                        'l2vpn evpn': {
                            'prefixes': {
                                '[3][1.1.1.3:3][0][32][1.1.1.3]/17': {
                                    'available_path': '1',
                                    'best_path': '1',
                                    'index': {
                                        1: {
                                            'ext_community': 'RT:1:3 ENCAP:8 EVPN Mcast Flags:3',
                                            'gateway': '0.0.0.0',
                                            'local_vxlan_vtep': {
                                                'local_router_mac': '0000.0000.0000',
                                                'vtep_ip': 'ABCD:1::2',
                                            },
                                            'localpref': 100,
                                            'next_hop': '::',
                                            'next_hop_via': 'default',
                                            'origin_codes': '?',
                                            'originator': '1.1.1.1',
                                            'pmsi': {
                                                'tun_id': {
                                                    'local': True,
                                                },
                                                'tun_type': 'IR',
                                                'vni': '20103',
                                            },
                                            'recipient_pathid': '0',
                                            'refresh_epoch': 1,
                                            'route_info': 'Local',
                                            'status_codes': '*>',
                                            'transfer_pathid': '0x0',
                                            'update_group': 1,
                                            'weight': '32768',
                                        },
                                    },
                                    'nlri_data': {
                                        'eti': '0',
                                        'ip_len': '32',
                                        'orig_rtr_id': '1.1.1.3',
                                        'rd': '1.1.1.3:3',
                                        'route-type': '3',
                                        'subnet': '17',
                                    },
                                    'paths': '1 available, best #1, table evi_3',
                                    'table_version': '2',
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}
