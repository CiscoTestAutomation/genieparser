expected_output = {
    'asic_0_mcid_oid': 6161,
    'fset_mcidgid': 10131,
    'fset_urid': '0x300000000002f4fc',
    'interfaces': {
        1: {
            'adjid': '0xf80055d1',
            'flags': 'InHw',
            'iftype': 'svi_if',
            'interface': 'Vl103',
            'physicalif': '-----------',
            'urids': {
                'adj_obj': '0x90::33',
                'child_repl': '0x20::214f',
                'mio': '0x80::fb72e',
                'parent': '0x60::3bd93',
            },
        },
        2: {
            'adjid': 'l2_mcg:',
            'flags': 'l3_port:',
            'iftype': 'urid:0x20::214f),',
            'interface': '50573',
            'physicalif': '(cookie:',
        },
        3: {
            'adjid': 'l2_mcg:',
            'flags': 'l3_port:',
            'iftype': 'urid:0x20::2154),',
            'interface': '2645',
            'physicalif': '(cookie:',
        },
    },
    'md5': '9a7bd17c9f727428:7d2424963dcb5c24',
    'mioitem_count': 3,
    'remote_port_count': 2,
    'state': 'allocated',
    'svi_port_count': 2,
    'type': 's_g_vrf',
    'users': {
        '0x100000000002f595': {
            'l3m_entry': {
                'group': '232.0.0.8',
                'ip': '104.1.1.2',
                'mvrf': 0,
            },
            'urid': '0x100000000002f595',
        },
    },
    'users_count': 1,
}