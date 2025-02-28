expected_output={
        'type': 's_g_vrf',
        'state': 'allocated',
        'md5': '35ddf2ee900391c0:6ced99293343193f',
        'fset_urid': '0x3000000000000007',
        'remote_port_count': 0,
        'svi_port_count': 0,
        'users_count': 1,
        'mioitem_count': 1,
        'interfaces': {
            1: {
            'adjid': '0xf8004e31',
            'interface': 'Gi1/0/26',
            'physicalif': 'Gi1/0/26',
            'iftype': 'phy_if',
            'flags': 'InHw',
            'urids': {
                'mio': '0x80::11',
                'parent': '0x0',
                'child_repl': '0x0',
                'adj_obj': '0x90::3'
            },
            'asic': {
                'asic_index': '0',
                'l3_port_oid': 2854,
                'port_oid': 2105
            }
            }
        },
        'fset_mcidgid': 8203,
        'asic_0_mcid_oid': 2868,
        'hw_ip_mcg_info_asic_0': {
            1: {
            'member_info': {
                'l3_port': 2854
            }
            }
        },
        'users': {
            '0x1000000000000565': {
            'urid': '0x1000000000000565',
            'l3m_entry': {
                'mvrf': 0,
                'ip': '2.2.2.2',
                'group': '232.1.1.1'
            }
        }
    }
}
