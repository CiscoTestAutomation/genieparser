expected_output = {
    'cpp_ha_client_processes': {
        'total_processes': 5,
        'registered_process': 5,
        'client_processes': {
            'cpp_ha': 'Initialized',
            'cpp_sp': 'Initialized',
            'cpp_driver0': 'Initialized',
            'fman_fp': 'Initialized',
            'cpp_cp': 'Initialized'
        },
        'platform_state': {
            'curr': 'ACTIVE_SOLO',
            'next': 'ACTIVE_SOLO'
        },
        'ha_state': {
            'cpp': '0',
            'dir': 'BOTH',
            'role_state': {
                'curr': 'ACTIVE_SOLO',
                'next': 'ACTIVE_SOLO'
            }
        },
        'client_state': 'ENABLE',
        'image': '/tmp/sw/fp/0/0/fp/mount/usr/cpp/bin/qfp-ucode-radium',
        'load': {
            'load_count': 1,
            'time': 'Apr 26, 2022 19:00:47'
        },
        'active_threads': '0-3,10-11',
        'stuck_threads': '4-9',
        'fault_manager_flag': {
            'ignore_fault': 'FALSE',
            'ignore_stuck_thread': 'FALSE',
            'crashdump_in_progress': 'FALSE'
        }
    }
}
