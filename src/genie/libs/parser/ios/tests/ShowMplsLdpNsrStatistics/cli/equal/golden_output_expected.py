expected_output = {
    "statistics": {
        "peer": {
            "10.169.197.252": {
                "local_space_id": {
                    0: {
                        "in_label_request_records": {"created": 0, "freed": 0},
                        "in_label_withdraw_records": {"created": 0, "freed": 0},
                        "local_address_withdraw": {"set": 0, "cleared": 0},
                        "transmit_contexts": {"enqueued": 0, "dequeued": 0},
                    }
                }
            },
            "10.169.197.253": {
                "local_space_id": {
                    0: {
                        "in_label_request_records": {"created": 0, "freed": 0},
                        "in_label_withdraw_records": {"created": 0, "freed": 0},
                        "local_address_withdraw": {"set": 0, "cleared": 0},
                        "transmit_contexts": {"enqueued": 0, "dequeued": 0},
                    }
                }
            },
        },
        "total_in_label_request_records": {"created": 0, "freed": 0},
        "total_in_label_withdraw_records": {"created": 0, "freed": 0},
        "total_local_address_withdraw_records": {"created": 0, "freed": 0},
        "label_request_acks": {
            "number_of_chkpt_messages": {
                "sent": 0,
                "in_queue": 0,
                "in_state_none": 0,
                "in_state_send": 0,
                "in_state_wait": 0,
            }
        },
        "label_withdraw_acks": {
            "number_of_chkpt_messages": {
                "sent": 0,
                "in_queue": 0,
                "in_state_none": 0,
                "in_state_send": 0,
                "in_state_wait": 0,
            }
        },
        "address_withdraw_acks": {
            "number_of_chkpt_messages": {
                "sent": 0,
                "in_queue": 0,
                "in_state_none": 0,
                "in_state_send": 0,
                "in_state_wait": 0,
            }
        },
        "session_sync": {
            "number_of_session_sync_msg_sent": 0,
            "number_of_address_records_created": 0,
            "number_of_address_records_freed": 0,
            "number_of_dup_address_records_created": 0,
            "number_of_dup_address_records_freed": 0,
            "number_of_remote_binding_records_created": 0,
            "number_of_remote_binding_records_freed": 0,
            "number_of_capability_records_created": 0,
            "number_of_capability_records_freed": 0,
            "number_of_addr_msg_in_state_none": 0,
            "number_of_dup_addr_msg_in_state_none": 0,
            "number_of_remote_binding_msg_in_state_none": 0,
            "number_of_capability_msg_in_state_none": 0,
            "number_of_addr_msg_in_state_send": 0,
            "number_of_dup_addr_msg_in_state_send": 0,
            "number_of_remote_binding_msg_in_state_send": 0,
            "number_of_capability_msg_in_state_send": 0,
            "number_of_addr_msg_in_state_wait": 0,
            "number_of_dup_addr_msg_in_state_wait": 0,
            "number_of_remote_binding_msg_in_state_wait": 0,
            "number_of_capability_msg_in_state_wait": 0,
            "number_of_sync_done_msg_sent": 0,
        },
    }
}
