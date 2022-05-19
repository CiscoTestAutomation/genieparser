expected_output = {
    "chassis": "",
    "snmp_packets_input": {
        "packet_count": 34854563,
        "bad_snmp_version_errors": 0,
        "unknown_community_name": 234,
        "illegal_operation_for_community": 2,
        "encoding_errors": 1,
        "number_of_requested_variables": 6536,
        "number_of_altered_variables": 154,
        "get_request_pdus": 22102104,
        "get_next_pdus": 972411,
        "set_request_pdus": 856948,
    },
    "snmp_packets_output": {
        "packet_count": 42531179,
        "too_big_errors": 0,
        "maximum_packet_size": 1500,
        "no_such_name_errors": 160671,
        "bad_value_errors": 5,
        "general_errors": 2,
        "response_pdus": 34854547,
        "trap_pdus": 7676632,
    },
    "snmp_logging": {
        "status": "enabled",
        "logging_hosts": {
            "10.0.0.1": {
                "udp_port": 162,
                "host_statistics": {
                    "notification_type": "Trap",
                    "pkts_in_trap_queue": 0,
                    "max_len_trap_queue": 100,
                    "pkts_sent": 0,
                    "pkts_dropped": 0,
                },
            },
            "10.0.0.2": {
                "udp_port": 162,
                "host_statistics": {
                    "notification_type": "Inform",
                    "pkts_in_trap_queue": 0,
                    "max_len_trap_queue": 100,
                    "pkts_sent": 0,
                    "pkts_dropped": 0,
                },
            },
            "2001:ab8::1": {
                "udp_port": 162,
                "host_statistics": {
                    "notification_type": "Trap",
                    "pkts_in_trap_queue": 0,
                    "max_len_trap_queue": 100,
                    "pkts_sent": 0,
                    "pkts_dropped": 0,
                },
            },
            "2001:0:ab00:1234:0:2552:7777:1313": {
                "udp_port": 162,
                "host_statistics": {
                    "notification_type": "Inform",
                    "pkts_in_trap_queue": 0,
                    "max_len_trap_queue": 100,
                    "pkts_sent": 0,
                    "pkts_dropped": 0,
                },
            },
        },
        "inform_statistics": {
            "informs_sent": 0,
            "informs_retries": 0,
            "informs_pending": 0,
            "informs_dropped": 0,
        },
    },
}

