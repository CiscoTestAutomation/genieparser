expected_output = {
    'lsps': {
        'my_tp_tunnel_1_1': {
            'id': 1,
            'source': 'my_tp_tunnel (R1:1)',
            'destination': 'my_tp_tunnel (R2:1)',
            'state': 'Up',
            'role': 'Head',
            'oam_profile': 'default',
            'bfd_profile': 'default',
            'cc_cv_state': 'Down',
            'cc_cv_session_id': 0,
            'working_lsp': {
                'in_label': 'Pop',
                'out_label': '16',
                'interface': 'GigabitEthernet3',
                'fec': '1.1.1.1/32',
                'weight': 1,
                'backup': 'No',
            },
            'protect_lsp': {
                'status': 'Not established'
            }
        },
        'my_tp_tunnel_2_1': {
            'id': 2,
            'source': 'my_tp_tunnel (R1:2)',
            'destination': 'my_tp_tunnel (R2:2)',
            'state': 'Down',
            'role': 'Tail',
            'oam_profile': 'profile1',
            'bfd_profile': 'profile2',
            'cc_cv_state': 'Up',
            'cc_cv_session_id': 12345,
            'working_lsp': {
                'in_label': '20',
                'out_label': 'Untagged',
                'interface': 'GigabitEthernet4',
                'fec': '2.2.2.2/32',
                'weight': 2,
                'backup': 'Yes',
            },
            'protect_lsp': {
                'in_label': '21',
                'out_label': '18',
                'interface': 'GigabitEthernet5',
                'fec': '3.3.3.3/32',
                'weight': 1,
                'backup': 'No'
            }
        }
    }
}
