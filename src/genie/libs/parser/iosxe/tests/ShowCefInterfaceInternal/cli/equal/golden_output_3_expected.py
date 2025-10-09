expected_output = {
    'interface': {
        'TwoGigabitEthernet1/0/36': {
            'cef_switching': 'enabled',
            'fast_if_number': 186,
            'fast_switching_type': 1,
            'firstsw_if_number': 186,
            'flags': '0x26000',
            'hardware_flags': '0x5',
            'hardware_idb': 'TwoGigabitEthernet1/0/36',
            'if_number': 186,
            'ifindex': '185(185)',
            'input_fast_flags': '0x4001',
            'input_features': 'Access List, Verify Unicast Reverse-Path',
            'interface_type': 146,
            'internet_address': '50.0.0.2/24',
            'ip_unicast_rpf_check': True,
            'mtu': 1500,
            'output_fast_flags': '0x0',
            'slot': 1,
            'slot_unit': 36,
            'state': 'up',
            'status_flags': {
                'fibhwidb': 'status 210040 status2 200019 status3 40000000 status4 2000',
                'hwidb': 'status 210040 status2 200019 status3 40000000 status4 2000',
            },
            'subblocks': {
                'ipv4': {
                    'address': '50.0.0.2/24',
                    'broadcast_address': '255.255.255.255',
                    'mtu': 1500,
                },
            },
            'suppressed_input_features': 'MCI Check',
            'vrf': 'Default(0)',
        },
    },
}