expected_output = {
    "config_session_lock": {
        "owner_pid": {
            578: {
                "tty_number": 2,
                "tty_username": "testuser",
                "user_debug_info": "CLI Session Lock",
                "lock_active_time_in_sec": 17,
            }
        }
    },
    "parser_configure_lock": {
        "owner_pid": {
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
            11: {
                "user": "User11",
                "tty": 31,
                "type": "EXCLUSIVE",
                "state": "LOCKED",
                "class": "Exposed",
                "count": 0,
                "pending_requests": 0,
                "user_debug_info": "0",
            },
        }
    },
}
