expected_output = {
    'mac_address': {
        'ec1d.8b0a.e3df': {
            'head': {
                'vlan': 0
            },
            'key': {
                'vlan': 39,
                'mac': '0xec1d8b0ae3df',
                'l3_if': 1,
                'gpn': 1688,
                'epoch': 0,
                'static': 1,
                'flood_en': 0,
                'vlan_lead_wless_flood_en': 0,
                'client_home_asic': 0,
                'learning_peerid': 0,
                'learning_peerid_valid': 0
            },
            'mask': {
                'vlan': 0,
                'mac': '0x0',
                'l3_if': 1,
                'gpn': 0,
                'epoch': 0,
                'static': 1,
                'flood_en': 0,
                'vlan_lead_wless_flood_en': 0,
                'client_home_asic': 0,
                'learning_peerid': 0,
                'learning_peerid_valid': 0
            },
            'src_ad': {
                'need_to_learn': 0,
                'lrn_v': 0,
                'catchall': 0,
                'static_mac': 0,
                'chain_ptr_v': 0,
                'chain_ptr': 0,
                'static_entry_v': 0,
                'auth_state': 0,
                'auth_mode': 0,
                'traf_mode': 0,
                'is_src_ce': 0
            },
            'dst_ad': {
                'si': '0x2d',
                'bridge': 0,
                'replicate': 0,
                'blk_fwd_o': 0,
                'v4_mac': 1,
                'v6_mac': 1,
                'catchall': 0,
                'ign_src_lrn': 0,
                'port_mask_o': 0,
                'afd_cli_f': 0,
                'afd_lbl': 0,
                'priority': 3,
                'dest_mod_idx':0,
                'destined_to_us': 1,
                'pv_trunk': 0
            }
        },
        '0000.0001.7000': {
            'head': {
                'vlan': 10
            },
            'key': {
                'vlan': 5,
                'mac': '0x17000',
                'l3_if': 0,
                'gpn': 0,
                'epoch': 15,
                'static': 1,
                'flood_en': 0,
                'vlan_lead_wless_flood_en': 0,
                'client_home_asic': 0,
                'learning_peerid': 0,
                'learning_peerid_valid': 0
            },
            'mask': {
                'vlan': 0,
                'mac': '0x0',
                'l3_if': 0,
                'gpn': 0,
                'epoch': 0,
                'static': 1,
                'flood_en': 0,
                'vlan_lead_wless_flood_en': 0,
                'client_home_asic': 0,
                'learning_peerid': 0,
                'learning_peerid_valid': 0
            },
            'src_ad': {
                'need_to_learn': 0,
                'lrn_v': 0,
                'catchall': 0,
                'static_mac': 0,
                'chain_ptr_v': 0,
                'chain_ptr': 0,
                'static_entry_v': 1,
                'auth_state': 0,
                'auth_mode': 0,
                'traf_mode': 0,
                'is_src_ce': 0
            },
            'dst_ad': {
                'si': '0x1',
                'bridge': 0,
                'replicate': 0,
                'blk_fwd_o': 0,
                'v4_mac': 0,
                'v6_mac': 0,
                'catchall': 0,
                'ign_src_lrn': 0,
                'port_mask_o': 0,
                'afd_cli_f': 0,
                'afd_lbl': 0,
                'priority': 3,
                'dest_mod_idx':0,
                'destined_to_us': 0,
                'pv_trunk': 0
            }
        }
    },
    'total_mac_address': 2
}