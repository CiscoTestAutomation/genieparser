expected_output = {
    'frr_db_summary': {
        'protected_intfs_num': 3,
        'protected_lsps_num': 3,
        'backup_tunnels_num': 3,
        'active_intfs_num': 0,
        'frr_active_tunnels_num': 0
    },
    'p2p_lsps': {
        'Tunnel13': {
            'lsp2': {
                'src_ip': '1.1.1.1',
                'dst_ip': '3.3.3.3',
                'state': 'ready',
                'in_label': '29',
                'out_intf': 'TenGigabitEthernet0/0/8',
                'out_label': 'implicit-null',
                'frr_tunnel': 'Tunnel232',
                'frr_out_label': 'implicit-null'
            }
        },
        'Tunnel14': {
            'lsp10': {
                'src_ip': '1.1.1.1',
                'dst_ip': '4.4.4.4',
                'state': 'ready',
                'in_label': '30',
                'out_intf': 'GigabitEthernet0/0/5',
                'out_label': '23',
                'frr_tunnel': 'Tunnel23',
                'frr_out_label': '23'
            }
        },
        'Tunnel141': {
            'lsp10': {
                'src_ip': '1.1.1.1',
                'dst_ip': '4.4.4.4',
                'state': 'ready',
                'in_label': '19',
                'out_intf': 'TwentyFiveGigE0/0/16',
                'out_label': '22',
                'frr_tunnel': 'Tunnel231',
                'frr_out_label': '22'
            }
        }
    },
    'p2mp_sub_lsps': {
        'Tunnel18': {
            'lsp9': {
                'src_ip': '1.1.1.1',
                'dst_ip': '3.3.3.3',
                'state': 'ready',
                'in_label': '39',
                'out_intf': 'TenGigabitEthernet0/0/7',
                'out_label': 'implicit-null',
                'frr_tunnel': 'Tunnel232',
                'frr_out_label': 'implicit-null'
            }
        },
        'Tunnel22': {
            'lsp7': {
                'src_ip': '1.1.1.1',
                'dst_ip': '4.4.4.4',
                'state': 'ready',
                'in_label': '49',
                'out_intf': 'GigabitEthernet0/0/7',
                'out_label': '23',
                'frr_tunnel': 'Tunnel23',
                'frr_out_label': '23'
            }
        },
        'Tunnel151': {
            'lsp6': {
                'src_ip': '1.1.1.1',
                'dst_ip': '4.4.4.4',
                'state': 'ready',
                'in_label': '59',
                'out_intf': 'TwentyFiveGigE0/0/7',
                'out_label': '22',
                'frr_tunnel': 'Tunnel231',
                'frr_out_label': '22'
            }
        }
    }
}
