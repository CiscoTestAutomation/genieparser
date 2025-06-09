expected_output = {
    'automatic_selection_process': 'Enable',
    'equipment_clock': '2048 (EEC-Option1)',
    'clock_mode': 'QL-Enable',
    'esmc_state': 'Enabled',
    'ssm_option': '1',
    't0': 'GigabitEthernet0/0/2',
    'global_hold_off_time': 300,
    'global_wait_to_restore': 10,
    'tsm_delay': 180,
    'revertive': 'Yes',
    'local_interfaces': {
        'Internal': {
            'signal_type': 'NA',
            'mode': 'NA/Dis',
            'priority': 251,
            'ql_in': 'QL-SEC',
            'esmc_tx': 'NA',
            'esmc_rx': 'NA'
        },
        '*GigabitEthernet0/0/2': {
            'signal_type': 'NA',
            'mode': 'Sync/En',
            'priority': 1,
            'ql_in': 'QL-SEC',
            'esmc_tx': '-',
            'esmc_rx': '-'
        },
        'GigabitEthernet0/0/6': {
            'signal_type': 'NA',
            'mode': 'Sync/En',
            'priority': 2,
            'ql_in': 'QL-SEC',
            'esmc_tx': '-',
            'esmc_rx': '-'
        },
        'TenGigabitEthernet0/0/10': {
            'signal_type': 'NA',
            'mode': 'Sync/En',
            'priority': 3,
            'ql_in': 'QL-SEC',
            'esmc_tx': '-',
            'esmc_rx': '-'
        },
        'TwoGigabitEthernet0/0/18': {
            'signal_type': 'NA',
            'mode': 'Sync/En',
            'priority': 4,
            'ql_in': 'QL-SEC',
            'esmc_tx': '-',
            'esmc_rx': '-'
        }
    }
}
