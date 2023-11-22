expected_output = {
    "chassis": "FCE2310A48M",
    "snmp_input": {
        "packet_count": 35072424,
        "bad_snmp_version_errors": 0,
        "unknown_community_name": 2089,
        "illegal_operation_for_community_name_supplied": 68,
        "encoding_errors": 0,
        "number_of_requested_variables": 341796946,
        "number_of_altered_variables": 7328,
        "get_request_pdus": 954173,
        "get_next_pdus": 31072480,
        "set_request_pdus": 3878,
        "input_queue_drops": 0,
        "maximum_queue_size": 1000
    },
    "snmp_output": {
        "packet_count": 35598123,
        "too_big_errors": 0,
        "maximum_packet_size": 1500,
        "no_such_name_errors": 1,
        "bad_value_errors": 0,
        "general_errors": 0,
        "response_pdus": 322899,
        "trap_pdus": 527788
    },
    "snmp_input_queue": 0,
    "snmp_global_trap": "enabled",
    "snmp_logging": {
        "status": "enabled",
        "endpoints": {
            "10.76.1.12": {
                "port": 151,
                "queue": 0,
                "queue_size": 10,
                "sent": 102045,
                "dropped": 3065
            },
            "10.76.133.10": {
                "port": 111,
                "queue": 0,
                "queue_size": 10,
                "sent": 102045,
                "dropped": 3065
            },
            "10.16.154.186": {
                "port": 169,
                "queue": 0,
                "queue_size": 10,
                "sent": 201075,
                "dropped": 11383
            },
            "10.166.67.19": {
                "port": 108,
                "queue": 0,
                "queue_size": 10,
                "sent": 102045,
                "dropped": 3065
            }           
        }
    }
}
