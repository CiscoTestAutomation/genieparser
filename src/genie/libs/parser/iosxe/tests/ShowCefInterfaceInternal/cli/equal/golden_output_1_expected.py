expected_output = {
    'interface': {
        'GigabitEthernet0/0': {
            'state': 'up',
            'if_number': 6,
            'fast_if_number': 6,
            'firstsw_if_number': 6,
            'internet_address': '192.168.0.131/24',
            'hardware_idb': 'GigabitEthernet0/0',
            'fast_switching_type': 1,
            'interface_type': 27,
            'cef_switching': 'disabled',
            'vpn_forwarding_table': 'Mgmt-vrf',
            'input_fast_flags': '0x0',
            'output_fast_flags': '0x0',
            'ifindex': '5(5)',
            'slot': 20,
            'slot_unit': 0,
            'mtu': 1500,
            'suppressed_input_features': 'MCI Check',
            'flags': '0x26000',
            'hardware_flags': '0x5',
            'vrf': 'Mgmt-vrf(1)',
            'status_flags':{
                'hwidb': 'status 210040 status2 200010 status3 0 status4 22',
                'fibhwidb': 'status 210040 status2 200010 status3 0 status4 22'
            },
            'subblocks':{
                'ipv4': {
                    'address': '192.168.0.131/24',
                    'broadcast_address': '255.255.255.255',
                    'mtu': 1500
                },
                'ipv6': {
                    'discarded_packets': 2
                }
            }
        }
    }
}