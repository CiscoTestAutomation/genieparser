expected_output = {
    'interface': {
        'Vlan1': {
            'state': 'up',
            'if_number': 159,
            'fast_if_number': 159,
            'firstsw_if_number': 159,
            'hardware_idb': 'Vlan1',
            'fast_switching_type': 1,
            'interface_type': 156,
            'cef_switching': 'disabled',
            'input_fast_flags': '0x0',
            'output_fast_flags': '0x0',
            'ifindex': '158(158)',
            'slot': 0,
            'slot_unit': 1,
            'mtu': 0,
            'input_features': 'IP not enabled discard',
            'suppressed_input_features': 'MCI Check',
            'flags': '0x26000',
            'hardware_flags': '0x5',
            'vrf': 'Default(0)',
            'status_flags':{
                'hwidb': 'status 210048 status2 200011 status3 0 status4 0',
                'fibhwidb': 'status 210048 status2 200011 status3 0 status4 0'
            },
            'subblocks':{
                'ipv4': {
                    'discarded_packets': 0
                },
                'ipv6': {
                    'discarded_packets': 0
                }
            }
        }
    }
}