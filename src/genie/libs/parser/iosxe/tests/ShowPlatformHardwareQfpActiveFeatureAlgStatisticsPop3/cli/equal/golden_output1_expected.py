expected_output = {
    "total_packets_parsed": {
        "request": 14,
        "response": 0
    },
    "total_packets_policy_inspected": {
        "request": 16
    },
    "memory_management": {
        "scb": {
            "alloc": 2,
            "free": 2,
            "low_mem_req": 0,
            "alloc_fail": 0
        }
    },
    "reset_session": {
        "cli_match": 10,
        "no_pop3_engine": 0,
        "dirty_bit": {
            "new_session": 0,
            "exist_session": 0,
            "after_parse": 0,
            "after_match": 0
        }
    },
    "drop_packets_info": {
        "no_regex_table": 0,
        "fragmented_packet": 0,
        "command_pending": 0
    },
    "abort_inspection_info": {
        "policy_not_exist": 0
    },
}

