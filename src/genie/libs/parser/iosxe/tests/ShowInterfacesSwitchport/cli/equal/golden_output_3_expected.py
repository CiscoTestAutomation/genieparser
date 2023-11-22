expected_output = {
    'GigabitEthernet1/1': {
        'access_vlan': '607',
        'access_vlan_name': '<SANITIZED>',
        'capture_mode': False,
        'capture_vlans': 'all',
        'oper_ethertype': '0x8100',
	'encapsulation': {
            'administrative_encapsulation': 'negotiate',
            'native_vlan': '1',
            'native_vlan_name': 'default',
            'operational_encapsulation': 'native',
        },
        'native_vlan_tagging': True,
        'negotiation_of_trunk': False,
        'operational_mode': 'static access',
        'port_channel': {
            'port_channel_int': 'Port-channel17',
            'port_channel_member': True,
        },
        'private_vlan': {
        },
        'pruning_vlans': '2-1001',
        'switchport_enable': True,
        'switchport_mode': 'static access',
        'trunk_vlans': 'all',
        'unknown_multicast_blocked': False,
        'unknown_unicast_blocked': False,
    }
}
