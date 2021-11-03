expected_output = {
    "statistics": {
        "client_facing": {
            'msg_received': {
                'renew': 18,
                'request': 1,
                'solicit': 1
            },
            'msg_sent': {
                'relay_forward': 20
            },
            "total_discard": 0,
            "total_recvd": 20,
            "total_sent": 20
        },
        "server_facing": {
            'msg_received': {
                'relay_reply': 20
            },
            'msg_sent': {
                'advertise': 1,
                'reply': 19
            },
            "total_discard": 0,
            "total_recvd": 20,
            "total_sent": 20
        }
    }
}
