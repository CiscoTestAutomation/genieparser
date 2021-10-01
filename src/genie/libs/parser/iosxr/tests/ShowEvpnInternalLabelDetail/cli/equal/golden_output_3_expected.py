

expected_output = {
    'vpn_id':
        {16001:
            {'encap': 'VXLAN',
            'esi': '0001.04ff.0b0c.0607.0811',
            'eth_tag': 0,
            'label': 24002,
            'mp_internal_label': 24002,
            'mp_resolved': True,
            'mp_info': 'Remote all-active',
            'pathlists':
                {'ead_es':
                    {'nexthop':
                        {'10.76.1.2':
                            {'label': 0}}},
                'summary':
                    {'nexthop':
                        {'10.76.1.2':
                            {'label': 16001,
                            'value': '0x03000001'}}},
                'ead_evi':
                    {'nexthop':
                        {'10.76.1.2':
                            {'label': 16001}}}},
            'vpn_id': 16001},
        16002:
            {'encap': 'VXLAN',
            'esi': '0001.04ff.0b0c.0607.0811',
            'eth_tag': 0,
            'label': 24003,
            'mp_internal_label': 24003,
            'mp_resolved': True,
            'mp_info': 'Remote all-active',
            'pathlists':
                {'ead_es':
                    {'nexthop':
                        {'10.76.1.2':
                            {'label': 0}}},
                'summary':
                    {'nexthop':
                        {'10.76.1.2':
                            {'label': 16002,
                                'value': '0x03000001'}}},
                'ead_evi':
                    {'nexthop':
                        {'10.76.1.2':
                            {'label': 16002}}}},
            'vpn_id': 16002},
        16003:
            {'encap': 'VXLAN',
            'esi': '0001.04ff.0b0c.0607.0811',
            'eth_tag': 0,
            'label': 24004,
            'mp_resolved': True,
            'mp_info': 'Remote all-active',
            'vpn_id': 16003}}}
