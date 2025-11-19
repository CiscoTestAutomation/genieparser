expected_output = {
    'syspage_index': 6,
    'packet_stats': {
        'min_packet_received': 1,
        'max_packet_received': 216
    },
    'message_stats': {
        'min_message_sent': 1,
        'max_message_sent': 1,
        'total_message_received': 14458,
        'total_message_sent': 2
    },
    'runtime_stats': {
        'min_clock_runtime_msec': 0,
        'max_clock_runtime_msec': 5,
        'min_cpu_runtime_msec': 0,
        'max_cpu_runtime_msec': 5
    },
    'fastpath_stats': {
        'fastpath_invocation': 20413,
        'epoll_timeout': 9062,
        'epoll_intr': 0,
        'fastpath_triggered_by_ios': 48,
        'wakeup': 13,
        'fastpath_top_epoll_error': 0,
        'second_level_epoll_error': 0,
        'special_ipc_request': 0
    },
    'file_descriptors': {
        'mstr_efd': 9,
        'fastpath_wakeup_fd': 7,
        'rd_efd': {
            'fd': 10,
            'epoll_add_failed': 0,
            'epoll_del_failed': 0
        },
        'rd_hdlr_efd': {
            'fd': 11,
            'epoll_add_failed': 0,
            'epoll_del_failed': 0
        },
        'wr_efd': {
            'fd': 12,
            'epoll_add_failed': 0,
            'epoll_del_failed': 0
        }
    },
    'event_stats': {
        'wakeup_efd_ready': 13,
        'rd_efd_ready': 7607,
        'rd_efd_processed': 7607,
        'rd_hdlr_efd_ready': 3738,
        'rd_hdlr_efd_processed': 3738,
        'wr_efd_ready': 2,
        'wr_efd_processed': 2
    },
    'ios_stats': {
        'ios_triggered_by_fastpath': 15930,
        'ios_triggered_by_packet': 27691,
        'ios_scheduler_wakeup': 43504
    },
    'data_path_stats': {
        'console_data_path_invocation': 845,
        'stdout_data_path_invocation': 0,
        'chasfs_process_thread_event': 2535,
        'tipc_process_thread_event': 0
    },
    'memory_stats': {
        'memory_allocation_failures': 0,
        'read_paused': 0,
        'read_pause_cleared': 0,
        'read_disabled': 0,
        'read_disable_cleared': 0
    },
    'current_state': {
        'read_paused': 'no',
        'read_disabled': 'no'
    },
    'utilization': {
        '5_seconds': {
            'clock_percent': 0,
            'cpu_percent': 0
        },
        '1_min': {
            'clock_percent': 0,
            'cpu_percent': 0
        },
        '5_min': {
            'clock_percent': 0,
            'cpu_percent': 0
        }
    },
    'mutex_stats': {
        'max_acquire_time_msec': 11937,
        'timestamp': '*Apr 14 18:15:50.475'
    }
}
