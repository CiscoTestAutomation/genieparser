expected_output = {
    'ssid': {
        0: {
            'events': {
                1: {
                    'ssid': 0,
                    'event_type': 'fsm_run',
                    'event_name': 'ACTIVE_REGISTER',
                    'fsm_name': 'Feature Table',
                    'timestamp': 'Fri Jun 18 22:14:40.000'
                },
                2: {
                    'ssid': 0,
                    'event_type': 'fsm_transition',
                    'event_name': 'ACTIVE_REGISTER',
                    'state': 'READY',
                    'prev_state': 'CREATING',
                    'timestamp': 'Fri Jun 18 22:14:40.000'
                },
                3: {
                    'ssid': 0,
                    'event_type': 'fsm_run',
                    'event_name': 'MAC_ACTIVITY',
                    'fsm_name': 'sisf_mac_fsm',
                    'timestamp': 'Wed Jun 30 17:03:14.000'
                },
                4: {
                    'ssid': 0,
                    'event_type': 'fsm_transition',
                    'event_name': 'MAC_ACTIVITY',
                    'state': 'MAC-REACHABLE',
                    'prev_state': 'MAC-STALE',
                    'timestamp': 'Wed Jun 30 17:03:14.000'
                }
            }
        },
        1: {
            'events': {
                1: {
                    'ssid': 1,
                    'event_type': 'fsm_run',
                    'event_name': 'ACTIVE_REGISTER',
                    'fsm_name': 'Feature Table',
                    'timestamp': 'Fri Jun 18 22:14:40.000'
                },
                2: {
                    'ssid': 1,
                    'event_type': 'fsm_transition',
                    'event_name': 'ACTIVE_REGISTER',
                    'state': 'READY',
                    'prev_state': 'CREATING',
                    'timestamp': 'Fri Jun 18 22:14:40.000'
                },
                3: {
                    'ssid': 1,
                    'event_type': 'bt_entry',
                    'state': 'Created Entry origin',
                    'static_mac': '000a.000a.000a',
                    'ipv4': '1.1.1.1',
                    'timestamp': 'Wed Jun 30 17:03:14.000'
                },
                4: {
                    'ssid': 1,
                    'event_type': 'fsm_run',
                    'event_name': 'LLA_RCV',
                    'fsm_name': 'Binding table',
                    'timestamp': 'Wed Jun 30 17:03:14.000'
                },
                5: {
                    'ssid': 1,
                    'event_type': 'fsm_transition',
                    'event_name': 'LLA_RCV',
                    'state': 'REACHABLE',
                    'prev_state': 'CREATING',
                    'timestamp': 'Wed Jun 30 17:03:14.000'
                },
                6: {
                    'ssid': 1,
                    'event_type': 'bt_entry',
                    'state': 'Entry State changed origin',
                    'static_mac': '000a.000a.000a',
                    'ipv4': '1.1.1.1',
                    'timestamp': 'Wed Jun 30 17:03:14.000'
                },
                7: {
                    'ssid': 1,
                    'event_type': 'fsm_run',
                    'event_name': 'T2_REACHABLE_TIMER',
                    'fsm_name': 'Binding table',
                    'timestamp': 'Wed Jun 30 17:08:24.000'
                },
                8: {
                    'ssid': 1,
                    'event_type': 'fsm_run',
                    'event_name': 'INACTIVE',
                    'fsm_name': 'Binding table',
                    'timestamp': 'Wed Jun 30 17:08:24.000'
                },
                9: {
                    'ssid': 1,
                    'event_type': 'fsm_transition',
                    'event_name': 'INACTIVE',
                    'state': 'STALE',
                    'prev_state': 'REACHABLE',
                    'timestamp': 'Wed Jun 30 17:08:24.000'
                },
                10: {
                    'ssid': 1,
                    'event_type': 'bt_entry',
                    'state': 'Entry State changed origin',
                    'static_mac': '000a.000a.000a',
                    'ipv4': '1.1.1.1',
                    'timestamp': 'Wed Jun 30 17:08:24.000'
                }
            }
        },
        2: {
            'events': {
                1: {
                    'ssid': 2,
                    'event_type': 'fsm_run',
                    'event_name': 'ACTIVE_REGISTER',
                    'fsm_name': 'Feature Table',
                    'timestamp': 'Fri Jun 25 19:52:11.000'
                },
                2: {
                    'ssid': 2,
                    'event_type': 'fsm_transition',
                    'event_name': 'ACTIVE_REGISTER',
                    'state': 'READY',
                    'prev_state': 'CREATING',
                    'timestamp': 'Fri Jun 25 19:52:11.000'
                }
            }
        },
        1000000: {
            'events': {
                1: {
                    'ssid': 1000000,
                    'event_type': 'fsm_run',
                    'event_name': 'MAC_T1',
                    'fsm_name': 'sisf_mac_fsm',
                    'timestamp': 'Wed Jun 30 17:08:14.000'
                },
                2: {
                    'ssid': 1000000,
                    'event_type': 'fsm_transition',
                    'event_name': 'MAC_T1',
                    'state': 'MAC-VERIFY',
                    'prev_state': 'MAC-REACHABLE',
                    'timestamp': 'Wed Jun 30 17:08:14.000'
                },
                3: {
                    'ssid': 1000000,
                    'event_type': 'fsm_run',
                    'event_name': 'MAC_R2',
                    'fsm_name': 'sisf_mac_fsm',
                    'timestamp': 'Wed Jun 30 17:08:14.000'
                },
                4: {
                    'ssid': 1000000,
                    'event_type': 'fsm_transition',
                    'event_name': 'MAC_R2',
                    'state': 'MAC-STALE',
                    'prev_state': 'MAC-VERIFY',
                    'timestamp': 'Wed Jun 30 17:08:14.000'
                },
                5: {
                    'ssid': 1000000,
                    'event_type': 'fsm_run',
                    'event_name': 'MAC_T3',
                    'fsm_name': 'sisf_mac_fsm',
                    'timestamp': 'Thu Jul 01 19:08:15.000'
                },
                6: {
                    'ssid': 1000000,
                    'event_type': 'fsm_run',
                    'event_name': 'MAC_R2',
                    'fsm_name': 'sisf_mac_fsm',
                    'timestamp': 'Thu Jul 01 19:08:15.000'
                },
                7: {
                    'ssid': 1000000,
                    'event_type': 'fsm_run',
                    'event_name': 'MAC_T5',
                    'fsm_name': 'sisf_mac_fsm',
                    'timestamp': 'Thu Jul 01 19:08:16.000'
                }
            }
        }
    }
}