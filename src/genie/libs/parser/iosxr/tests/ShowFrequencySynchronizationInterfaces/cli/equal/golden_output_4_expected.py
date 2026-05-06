expected_output = {
    'interfaces': {
        'GigabitEthernet0/0/0/1': {
            'input': {
                'selection': 'not assigned',
                'status': 'Down',
            },
            'interface': 'GigabitEthernet0/0/0/1',
            'interface_status': 'shutdown',
            'next_selection_points': 'ETH_RXMUX',
            'output': {
                'effective_ql': 'Opt-I/PRC',
                'selected_source': 'TenGigE0/0/0/26',
                'selected_source_ql': 'Opt-I/PRC',
            },
            'ssm': {
                'status': 'Enabled',
            },
            'wait_to_restore_time': 5,
        },
        'GigabitEthernet0/0/0/17': {
            'input': {
                'effective_ql': 'Failed',
                'last_received_ql': 'Failed',
                'priority': 10,
                'status': 'Down',
                'time_of_day_priority': 100,
            },
            'interface': 'GigabitEthernet0/0/0/17',
            'interface_status': 'up',
            'next_selection_points': 'ETH_RXMUX',
            'output': {
                'effective_ql': 'Opt-I/PRC',
                'selected_source': 'TenGigE0/0/0/26',
                'selected_source_ql': 'Opt-I/PRC',
            },
            'selection': 'input',
            'ssm': {
                'esmc_ssms': {
                    'received': {
                        'dnu_dus': 0,
                        'event': 0,
                        'information': 0,
                        'total': 0,
                    },
                    'sent': {
                        'dnu_dus': 0,
                        'event': 19,
                        'information': 1155531,
                        'total': 1155550,
                    },
                },
                'last_ssm_received': 'never',
                'peer_time': '1w6d',
                'status': 'Enabled',
            },
        },
        'GigabitEthernet0/0/0/9': {
            'input': {
                'selection': 'not assigned',
                'status': 'Down',
            },
            'interface': 'GigabitEthernet0/0/0/9',
            'interface_status': 'shutdown',
            'next_selection_points': 'ETH_RXMUX',
            'output': {
                'effective_ql': 'Opt-I/PRC',
                'selected_source': 'TenGigE0/0/0/26',
                'selected_source_ql': 'Opt-I/PRC',
            },
            'ssm': {
                'status': 'Enabled',
            },
            'wait_to_restore_time': 0,
        },
        'TenGigE0/0/0/16': {
            'input': {
                'selection': 'not assigned',
                'status': 'Down',
            },
            'interface': 'TenGigE0/0/0/16',
            'interface_status': 'up',
            'next_selection_points': 'ETH_RXMUX',
            'output': {
                'effective_ql': 'Opt-I/PRC',
                'selected_source': 'TenGigE0/0/0/26',
                'selected_source_ql': 'Opt-I/PRC',
            },
            'ssm': {
                'esmc_ssms': {
                    'received': {
                        'dnu_dus': 0,
                        'event': 0,
                        'information': 88570,
                        'total': 88570,
                    },
                    'sent': {
                        'dnu_dus': 0,
                        'event': 10,
                        'information': 88552,
                        'total': 88562,
                    },
                },
                'last_ssm_received': '0.423s ago',
                'peer_time': '1d00h',
                'status': 'Enabled',
            },
            'wait_to_restore_time': 0,
        },
        'TenGigE0/0/0/26': {
            'input': {
                'effective_ql': 'Opt-I/PRC',
                'last_received_ql': 'Opt-I/PRC',
                'priority': 10,
                'status': 'Up',
                'time_of_day_priority': 25,
            },
            'interface': 'TenGigE0/0/0/26',
            'interface_status': 'up',
            'next_selection_points': 'ETH_RXMUX',
            'output': {
                'effective_ql': 'DNU',
                'selected_source': 'TenGigE0/0/0/26',
                'selected_source_ql': 'Opt-I/PRC',
            },
            'selection': 'input',
            'ssm': {
                'esmc_ssms': {
                    'received': {
                        'dnu_dus': 0,
                        'event': 3,
                        'information': 88490,
                        'total': 88493,
                    },
                    'sent': {
                        'dnu_dus': 87848,
                        'event': 7,
                        'information': 88490,
                        'total': 88497,
                    },
                },
                'last_ssm_received': '0.380s ago',
                'peer_time': '1d00h',
                'status': 'Enabled',
            },
        },
        'TenGigE0/0/0/27': {
            'input': {
                'effective_ql': 'Opt-I/PRC',
                'last_received_ql': 'Opt-I/PRC',
                'priority': 20,
                'status': 'Up',
                'time_of_day_priority': 25,
            },
            'interface': 'TenGigE0/0/0/27',
            'interface_status': 'up',
            'next_selection_points': 'ETH_RXMUX',
            'output': {
                'effective_ql': 'Opt-I/PRC',
                'selected_source': 'TenGigE0/0/0/26',
                'selected_source_ql': 'Opt-I/PRC',
            },
            'selection': 'input',
            'ssm': {
                'esmc_ssms': {
                    'received': {
                        'dnu_dus': 0,
                        'event': 1,
                        'information': 88499,
                        'total': 88500,
                    },
                    'sent': {
                        'dnu_dus': 585,
                        'event': 8,
                        'information': 88499,
                        'total': 88507,
                    },
                },
                'last_ssm_received': '0.470s ago',
                'peer_time': '1d00h',
                'status': 'Enabled',
            },
        },
    }, 
}  
