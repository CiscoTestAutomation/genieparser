expected_output = {
    'automatic_selection_process': 'Enable',
    'clock_mode': 'QL-Enable',
    'clock_state': 'Free-running',
    'equipment_clock': '2048 (EEC-Option1)',
    'esmc_state': 'Enabled',
    'force_switch': 'FALSE',
    'global_hold_off_time': 300,
    'global_wait_to_restore': 300,
    'last_transition_recorded': '(begin)-> 2A (ql_mode_enable)-> 1A (src_added)-> 1A',
    'local_interfaces': {
        'GigabitEthernet0/0/2': {
            'active_alarms': 'None',
            'alarms': 'FALSE',
            'description': 'None',
            'esmc_rx': 'ENABLED',
            'esmc_tx': 'ENABLED',
            'hold_off_time': 300,
            'lock_out': 'FALSE',
            'mode': 'Synchronous(Ql-enabled)',
            'priority': '1',
            'ql_receive': 'QL-DNU',
            'ql_receive_configured': '-',
            'ql_receive_overrided': '-',
            'ql_transmit': 'QL-SEC',
            'ql_transmit_configured': '-',
            'signal_fail': 'FALSE',
            'signal_type': 'NA',
            'slot_disabled': 'FALSE',
            'snmp_input_source_index': 11,
            'snmp_parent_list_index': 0,
            'wait_to_restore': 300,
        },
        'Internal': {
            'active_alarms': 'None',
            'alarms': 'FALSE',
            'description': 'None',
            'hold_off_time': 0,
            'lock_out': 'FALSE',
            'mode': 'NA(Ql-enabled)',
            'priority': '251',
            'ql_receive': 'QL-SEC',
            'ql_receive_configured': '-',
            'ql_receive_overrided': '-',
            'ql_transmit': '-',
            'ql_transmit_configured': '-',
            'signal_fail': 'FALSE',
            'signal_type': 'NA',
            'slot_disabled': 'FALSE',
            'snmp_input_source_index': 1,
            'snmp_parent_list_index': 0,
            'ssm_rx': 'DISABLED',
            'ssm_tx': 'DISABLED',
            'wait_to_restore': 0,
        },
    },
    'manual_switch': 'FALSE',
    'nominated_interfaces': {
        'GigabitEthernet0/0/2': {
            'esmc_rx': '-',
            'esmc_tx': '-',
            'is_source': False,
            'mode_or_ql': 'Sync/En',
            'prio': '1',
            'ql_in': 'QL-DNU',
            'sigtype': 'NA',
        },
        'Internal': {
            'esmc_rx': 'NA',
            'esmc_tx': 'NA',
            'is_source': True,
            'mode_or_ql': 'NA/Dis',
            'prio': '251',
            'ql_in': 'QL-SEC',
            'sigtype': 'NA',
            'source_type': 'Synchronization source selected',
        },
    },
    'num_of_sync_sources': 1,
    'revertive': 'No',
    'squelch_threshold': 'QL-SEC',
    'ssm_option': '1',
    't0': 'Internal',
    'tsm_delay': 180,
}
