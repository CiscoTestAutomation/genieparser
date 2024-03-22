expected_output = {
    "Tunnel100": {
        "nhs_ip": {
            "100.0.0.100": {
                "nhs_state": "RE",
                "nbma_address": "101.1.1.1",
                "priority": 0,
                "cluster": 0,
                "req_sent": 105434,
                "req_failed": 0,
                "reply_recv": 105434,
                "receive_time": "00:00:58",
                "current_request_id": 35914,
                "ack": 35914,
                "protection_socket_requested": "FALSE",
            },
            "172.16.0.1": {
                "nhs_state": "E",
                "priority": 0,
                "cluster": 0,
                "req_sent": 124175,
                "req_failed": 0,
                "reply_recv": 0,
                "current_request_id": 57,
                "protection_socket_requested": "FALSE"
            }
        }
    },
    "pending_registration_requests": {
        "req_id": {"57": {"ret": 64, "nhs_ip": "172.16.0.1", "nhs_state": "expired"}}
    },
}
