expected_output = {
    'automatic_selection_process': 'Enable',
    'clock_mode': 'QL-Enable',
    'equipment_clock': '2048 (EEC-Option1)',
    'esmc_state': 'Enabled',
    'global_hold_off_time': 300,
    'global_wait_to_restore': 10,
    'nominated_interfaces': {
        'GigabitEthernet0/0/2': {
            'esmc_rx': '-',
            'esmc_tx': '-',
            'is_source': True,
            'mode': 'Sync/En',
            'priority': 1,
            'ql_in': 'QL-SEC',
            'signal_type': 'NA',
            'source_type': 'Synchronization source selected'
        },
        'GigabitEthernet0/0/6': {
            'esmc_rx': '-',
            'esmc_tx': '-',
            'is_source': False,
            'mode': 'Sync/En',
            'priority': 2,
            'ql_in': 'QL-SEC',
            'signal_type': 'NA'
        },
        'Internal': {
            'esmc_rx': 'NA',
            'esmc_tx': 'NA',
            'is_source': False,
            'mode': 'NA/Dis',
            'priority': 251,
            'ql_in': 'QL-SEC',
            'signal_type': 'NA'
        },
        'TenGigabitEthernet0/0/10': {
            'esmc_rx': '-',
            'esmc_tx': '-',
            'is_source': False,
            'mode': 'Sync/En',
            'priority': 3,
            'ql_in': 'QL-SEC',
            'signal_type': 'NA'
        },
        'TwoGigabitEthernet0/0/18': {
            'esmc_rx': '-',
            'esmc_tx': '-',
            'is_source': False,
            'mode': 'Sync/En',
            'priority': 4,
            'ql_in': 'QL-SEC',
            'signal_type': 'NA'
        }
    },
    'revertive': 'Yes',
    'ssm_option': '1',
    't0': 'GigabitEthernet0/0/2',
    'tsm_delay': 180
}
