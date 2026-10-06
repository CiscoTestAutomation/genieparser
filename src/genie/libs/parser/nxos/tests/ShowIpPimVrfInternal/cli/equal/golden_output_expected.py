expected_output = {
    'vrf': {
        'default': {
            'address_family': {
                'ipv4': {
                    'vrf_id': 1,
                    'table_id': '0x00000001',
                    'interface_count': 8,
                    'bfd': {
                        'enable': False,
                    },
                    'mvpn': {
                        'enable': False,
                    },
                    'rp_change': False,
                    'vxlan_vni_id': 0,
                    'pfm_sd': {
                        'state': True,
                        'group_range': '224.0.0.0/4',
                        'originator_interface': 'loopback0',
                        'originator_ip': '55.55.55.55',
                        'announcement_interval': {
                            'value': 100,
                            'unit': 'seconds',
                        },
                        'announcement_gap': {
                            'value': 1200,
                            'unit': 'milliseconds',
                        },
                        'announcement_rate': 10,
                        'holdtime': {
                            'value': 60,
                            'unit': 'seconds',
                        },
                    },
                },
            },
        },
    },
}
