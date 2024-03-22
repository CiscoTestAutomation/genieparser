expected_output = {
    "Tunnel0": {
        "nhs_ip": {
            "111.0.0.100": {
                "nhs_state": "E",
                "nbma_address": "111.1.1.1",
                "priority": 0,
                "cluster": 0,
                "req_sent": 0,
                "req_failed": 0,
                "reply_recv": 0,
                "current_request_id": 94,
                "protection_socket_requested": "FALSE",
            }
        }
    },
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
                "receive_time": "00:00:49",
                "current_request_id": 35914,
                "ack": 35914,
                "protection_socket_requested": "FALSE",
            },
            "172.16.0.1": {
                "nhs_state": "E",
                "priority": 0,
                "cluster": 0,
                "req_sent": 124174,
                "req_failed": 0,
                "reply_recv": 0,
                "current_request_id": 35915,
                "protection_socket_requested": "FALSE"
            }
        }
    },
    "Tunnel111": {
        "nhs_ip": {
            "111.0.0.100": {
                "nhs_state": "E",
                "nbma_address": "111.1.1.1",
                "priority": 0,
                "cluster": 0,
                "req_sent": 184399,
                "req_failed": 0,
                "reply_recv": 0,
                "current_request_id": 35916,
            }
        }
    },
    "pending_registration_requests": {
        "req_id": {
            "16248": {
                "ret": 64,
                "nhs_ip": "111.0.0.100",
                "nhs_state": "expired",
                "tunnel": "Tu111",
            },
            "57": {
                "ret": 64,
                "nhs_ip": "172.16.0.1",
                "nhs_state": "expired",
                "tunnel": "Tu100",
            },
        }
    },
}
