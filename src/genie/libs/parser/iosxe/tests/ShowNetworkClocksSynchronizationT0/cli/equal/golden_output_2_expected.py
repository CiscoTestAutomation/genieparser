expected_output = {
    'automatic_selection_process': 'Enable',
    'equipment_clock': '2048 (EEC-Option1)',
    'clock_mode': 'QL-Enable',
    'esmc_state': 'Enabled',
    'ssm_option': '1',
    't0': 'Internal',
    'global_hold_off_time': 300,
    'global_wait_to_restore': 300,
    'tsm_delay': 180,
    'revertive': 'No',
    'local_interfaces': {
        '*Internal': {
            'signal_type': 'NA',
            'mode': 'NA/Dis',
            'priority': 251,
            'ql_in': 'QL-SEC',
            'esmc_tx': 'NA',
            'esmc_rx': 'NA'
        },
        'GigabitEthernet0/0/2': {
            'signal_type': 'NA',
            'mode': 'Sync/En',
            'priority': 1,
            'ql_in': 'QL-DNU',
            'esmc_tx': '-',
            'esmc_rx': '-'
        }
    }
}
