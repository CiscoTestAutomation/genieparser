expected_output = {
        'vlan': {
            50: {
            'protocol': 'ipv4',
            'snoop_state': 'ON',
            'stp_tcn_flood': 'OFF',
            'flood_md': 'ON',
            'iosd_md': 'ON',
            'pim_en': 'OFF',
            'evpn_en': 'OFF',
            'secondary_vlan': 'NO',
            'vlan_urid': '0x40000000000000d1',
            'fset_urid_hash': '0x20000000000000d1 ( 80040362 )',
            'fset_aux_urid': '0x0',
            'd_users_count': '0',
            'mroute_port': [
                
            ],
            'flood_port': [
                'GigabitEthernet1/0/6',
                'GigabitEthernet2/0/10',
                'GigabitEthernet3/0/10',
                'Port-channel126'
            ],
            'gid': 8424,
            'mcid_asic': 3224,
            'hw_info_asic': {
                'hw_vlan_mcid_oid': '3224 (cookie:urid:0x20::d1)',
                'multicast_state': 'disabled'
            }
        }
    }
}


