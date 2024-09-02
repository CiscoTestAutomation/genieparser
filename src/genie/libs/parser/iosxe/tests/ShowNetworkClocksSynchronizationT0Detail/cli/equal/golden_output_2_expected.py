expected_output = {
    'automatic_selection_process': 'Enable',
    'equipment_clock': '2048 (EEC-Option1)',
    'clock_state': 'Free-running',
    'clock_mode': 'QL-Enable',
    'esmc_state': 'Enabled',
    'ssm_option': '1',
    't0': 'Internal',
    'global_hold_off_time': 300,
    'global_wait_to_restore': 300,
    'tsm_delay': 180,
    'revertive': 'No',
    'force_switch': 'FALSE',
    'manual_switch': 'FALSE',
    'num_of_sync_sources': 1,
    'squelch_threshold': 'QL-SEC',
    'last_transition_recorded': '(begin)-> 2A (ql_mode_enable)-> 1A (src_added)-> 1A',
    'local_interfaces': {
        'Internal': {
            'description': 'None',
            'signal_type': 'NA',
            'mode': 'NA (Ql-enabled)',
            'ssm_tx': 'DISABLED',
            'ssm_rx': 'DISABLED',
            'ql_receive': 'QL-SEC',
            'ql_receive_configured': '-',
            'ql_receive_overrided': '-',
            'ql_transmit': '-',
            'ql_transmit_configured': '-'
        },
        'GigabitEthernet0/0/2': {
            'description': 'None',
            'signal_type': 'NA',
            'mode': 'Synchronous (Ql-enabled)',
            'esmc_tx': 'ENABLED',
            'esmc_rx': 'ENABLED',
            'ql_receive': 'QL-DNU',
            'ql_receive_configured': '-',
            'ql_receive_overrided': '-',
            'ql_transmit': 'QL-SEC',
            'ql_transmit_configured': '-'
        }
    }
}
