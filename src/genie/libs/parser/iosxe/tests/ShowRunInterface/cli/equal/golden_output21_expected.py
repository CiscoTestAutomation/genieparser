expected_output = {
    'interfaces': {
        'TenGigabitEthernet1/0/11': {
            'authentication_order': 'dot1x',
            'authentication_port_control': 'auto',
            'authentication_priority': 'dot1x',
            'dot1x_pae_authenticator': True,
            'spanning_tree_portfast_trunk': True,
            'switchport_mode': 'trunk',
            'switchport_trunk_native_vlan': 101,
        },
    },
}
