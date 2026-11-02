expected_output = {
    'groups': {
        '228.1.2.240': {
            'group_end': '228.1.2.255',
            'mask': '/28',
            'mvr_vlan': 101,
            'global_default_mvr_vlan': False,
        },
        '230.1.1.1': {
            'group_end': '230.1.1.4',
            'count': 4,
            'mvr_vlan': 100,
            'global_default_mvr_vlan': True,
        },
        '235.1.1.6': {
            'group_end': '235.1.1.6',
            'count': 1,
            'mvr_vlan': 340,
            'global_default_mvr_vlan': False,
        },
        '225.1.3.1': {
            'group_end': '225.1.3.1',
            'count': 1,
            'mvr_vlan': 100,
            'global_default_mvr_vlan': True,
            'interface': 'Ethernet1/10',
        },
    },
}
