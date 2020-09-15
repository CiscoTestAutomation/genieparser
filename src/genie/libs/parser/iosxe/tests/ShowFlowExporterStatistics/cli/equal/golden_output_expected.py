expected_output = {
    "flow_exporter": {
        "test": {
            "pkt_send_stats": {
                "last_cleared": "00:10:17",
                "successfully_sent": 6,
                "successfully_sent_bytes": 410,
                "reason_not_given": 163,
                "reason_not_given_bytes": 7820,
                "no_destination_address": 421,
                "no_destination_address_bytes": 10423,
            },
            "client_send_stats": {
                "Flow Monitor Test": {
                    "records_added": {"total": 21, "sent": 8, "failed": 13},
                    "bytes_added": {"total": 1260, "sent": 145, "failed": 1115},
                }
            },
        }
    }
}
