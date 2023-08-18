expected_output = {
    'isis': {
        '1': {
            'process_id': '1',
            'interface': {
                'Gi0/0/0/1': {
                    'interface_name': 'Gi0/0/0/1',
                    'all_status': 'No'
                }
            }
        },
        '10': {
            'process_id': '10',
            'interface': {
                'BE10': {
                    'interface_name': 'BE10',
                    'all_status': 'Yes',
                    'adjs_l1': '-',
                    'adjs_l2': '0',
                    'adj_topos_run_cfg': '1/1',
                    'adv_topos_run_cfg': '1/1',
                    'clns': 'Up',
                    'mtu_value': '1497',
                    'prio_l1': '-',
                    'prio_l2': '64'
                },
                'BE10.10': {
                    'interface_name': 'BE10.10',
                    'all_status': 'Yes',
                    'adjs_l1': '-',
                    'adjs_l2': '1*',
                    'adj_topos_run_cfg': '2/2',
                    'adv_topos_run_cfg': '2/2',
                    'clns': 'Up',
                    'mtu_value': '1497',
                    'prio_l1': '-',
                    'prio_l2': '64'
                },
                'Gi0/0/0/1.10': {
                    'interface_name': 'Gi0/0/0/1.10',
                    'all_status': 'No'
                },
                'Gi0/0/0/1.19': {
                    'interface_name': 'Gi0/0/0/1.19',
                    'all_status': 'No',
                    'adjs_l1': '-',
                    'adjs_l2': '-',
                    'adj_topos_run_cfg': '0/2',
                    'adv_topos_run_cfg': '0/2',
                    'clns': 'Down',
                    'mtu_value': '1497',
                    'prio_l1': '-',
                    'prio_l2': '-'
                }
            }
        },
        '99': {
            'process_id': '99',
            'interface': {
                'Gi0/0/0/6': {
                    'interface_name': 'Gi0/0/0/6',
                    'all_status': 'No',
                    'adjs_l1': '-',
                    'adjs_l2': '-',
                    'adj_topos_run_cfg': '0/1',
                    'adv_topos_run_cfg': '0/1',
                    'clns': 'Up',
                    'mtu_value': '1501',
                    'prio_l1': '-',
                    'prio_l2': '-'
                }
            }
        }
    }
}
