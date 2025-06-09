expected_output = {
            'vlan': {
                13: {
                'protocol': 'ipv6',
                'snoop_state': 'ON',
                'stp_tcn_flood': 'OFF',
                'flood_md': ' OFF',
                'iosd_md': 'OFF',
                'pim_en': 'ON',
                'evpn_en': 'OFF',
                'secondary_vlan': 'NO',
                'vlan_urid': '0x5000000000000006',
                'fset_urid': {
                    'urid': '0x2000000000000006',
                    'hash': '7839ab25'
                },
                'fset_aux_urid': '0x0',
                'd_users_count': '0',
                'mrouter_ports': [
                    'Port-channel95 (Port:HundredGigE1/0/7)'
                ],
                'flood_ports': [
                    'Port-channel95'
                ],
                'gid': 8197,
                'mcid_asic': 2129,
                'hw_info_asic': {
                    'hw_vlan_mcid_oid': {
                    'oid': 2129,
                    'cookie': '0x20::6'
                    },
                    'multicast_state': 'enabled'
            }
        }
    }
}