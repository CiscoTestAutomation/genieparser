expected_output = {
    "lisp_id": {
        0: {
            "rp": "Active",
            "sso": "enabled",
            "checkpoint_connection": "open",
            "peer_redundancy_state": "synchronized",
            "number_of_bulk_sync_started": 1,
            "last_bulk_sync_started": "Jan 23 15:55:26.712 PST",
            "last_bulk_sync_finished": "Jan 23 15:55:26.713 PST",
            "last_sync_lost": "never",
            "queued_checkpoint_requests": 0,
            "max_checkpoint_requests": 17,
            "unack_checkpoint_requests": 16,
        },
        1: {
            "rp": "Standby",
            "sso": "disabled",
            "checkpoint_connection": "closed",
            "peer_redundancy_state": "unsynchronized",
            "number_of_bulk_sync_started": 2,
            "last_bulk_sync_started": "never",
            "last_bulk_sync_finished": "never",
            "last_sync_lost": "Jan 23 15:55:26.713 PST",
            "queued_checkpoint_requests": 2,
            "max_checkpoint_requests": 14,
            "unack_checkpoint_requests": 14,
        },
    }
}
