expected_output = {
            'vlan': {
                50: {
                'protocol': 'ipv6',
                'snoop_state': 'OFF',
                'stp_tcn_flood': 'OFF',
                'flood_md': ' ON',
                'iosd_md': 'OFF',
                'pim_en': 'OFF',
                'evpn_en': 'OFF',
                'secondary_vlan': 'NO',
                'vlan_urid': '0x50000000000000d2',
                'fset_urid': {
                    'urid': '0x20000000000000d2',
                    'hash': 'afc0c589'
                },
                'fset_aux_urid': '0x0',
                'd_users_count': '0',
                'mrouter_ports': [
                    
                ],
                'flood_ports': [
                    'GigabitEthernet1/0/6',
                    'GigabitEthernet2/0/10',
                    'GigabitEthernet3/0/10',
                    'Port-channel126'
                ],
                'gid': 8425,
                'mcid_asic': 3225,
                'hw_info_asic': {
                    'hw_vlan_mcid_oid': {
                    'oid': 3225,
                    'cookie': '0x20::d2'
                    },
                    'multicast_state': 'disabled'
            }
        }
    }
}