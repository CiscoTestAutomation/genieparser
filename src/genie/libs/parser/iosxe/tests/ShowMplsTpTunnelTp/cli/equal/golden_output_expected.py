expected_output = {
    'mpls_tp_tunnel': {
        1: {
            'admin': 'up',
            'bandwidth': 0,
            'bfd_template': 'BFD',
            'dst_global_id': 0,
            'dst_node_id': '103.3.3.3',
            'dst_tunnel': 1,
            'oper': 'up',
            'protect_lsp': {
                'bfd_state': 'Up',
                'fault_oam': 'Clear',
                'lockout': 'Clear',
                'lsp_num': 1,
                'path': {
                    '0::101.1.1.1::1::0::103.3.3.3::1::1 (protect/active)': {
                        'in_label': 6100,
                        'label_table': 0,
                        'out_label': 6400,
                    },
                },
                'signal_degrade': 'No',
                'status': 'Active',
            },
            'protection_trigger': 'LDI LKR',
            'psc': 'Disabled',
            'src_global_id': 0,
            'src_node_id': '101.1.1.1',
            'src_tunnel': 1,
            'working_lsp': {
                'bfd_state': 'Up',
                'fault_oam': 'Clear',
                'lockout': 'Clear',
                'lsp_num': 0,
                'path': {
                    '0::101.1.1.1::1::0::103.3.3.3::1::0 (working/standby)': {
                        'bandwidth_admitted': 0,
                        'forwarding': 'Installed',
                        'in_label': 4100,
                        'interface': 'Te0/0/13',
                        'label_table': 0,
                        'out_label': 5200,
                        'outgoing_tp_link': 1,
                    },
                },
                'signal_degrade': 'No',
                'status': 'Standby',
            },
        }
    }
}
