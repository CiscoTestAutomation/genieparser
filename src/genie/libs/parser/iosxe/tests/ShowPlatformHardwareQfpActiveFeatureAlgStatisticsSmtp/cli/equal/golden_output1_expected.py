expected_output = {
        "total_packets_parsed": {
            "request": 12,
            "response": 13
        },
        "total_packets_policy_inspected": {
            "request": 12,
            "response": 13
        },
        "memory_management": {
            "scb": {
                "alloc": 1,
                "free": 1,
                "low_mem_req": 0,
                "alloc_fail": 0
            },
            "command_element": {
                "alloc": 20,
                "free": 20,
                "low_mem_req": 0
            },
            "log_element": {
                "alloc": 1,
                "free": 1,
                "low_mem_req": 0
            },
            "mask_element": {
                "alloc": 3,
                "free": 3,
                "low_mem_req": 0
            }
        },
        "reset_session": {
            "cli_match": 0,
            "no_smtp_engine": 0,
            "failover_detect": 0,
            "sw_error": 0,
            "dirty_bit": {
                "new_session": 0,
                "exist_session": 0,
                "after_parse": 0,
                "after_match": 0
            }
        },
        "abort_inspection_info": {
            "policy_not_exist": 0,
            "retransmit_packet": 0
        }
    }

