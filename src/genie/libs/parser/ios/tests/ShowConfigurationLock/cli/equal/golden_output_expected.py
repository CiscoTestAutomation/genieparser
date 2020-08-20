expected_output = {
    "parser_configure_lock": {
        "owner_pid": {
            3: {
                "user": "unknown",
                "tty": 0,
                "type": "EXCLUSIVE",
                "state": "LOCKED",
                "class": "EXPOSED",
                "count": 1,
                "pending_requests": 0,
                "user_debug_info": "configure terminal",
                "session_idle_state": "TRUE",
                "num_of_exec_cmds_executed": 0,
                "num_of_exec_cmds_blocked": 0,
                "config_wait_for_show_completion": "FALSE",
                "remote_ip_address": "Unknown",
                "lock_active_time_in_sec": 6,
                "lock_expiration_timer_in_sec": 593,
            },
            -1: {
                "user": "unknown",
                "tty": -1,
                "type": "NO LOCK",
                "state": "FREE",
                "class": "unknown",
                "count": 0,
                "pending_requests": 0,
            },
            10: {
                "user": "User1",
                "tty": 3,
                "type": "EXCLUSIVE",
                "state": "LOCKED",
                "class": "Exposed",
                "count": 0,
                "pending_requests": 0,
                "user_debug_info": "0",
            },
        }
    }
}
