expected_output = {
    "chassis": "FCE2310A48M",
    "contact": "something@cisco.com",
    "location": "To be filled in",
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
        "input_queue_drops": 0
    },
    "snmp_output": {
        "packet_count": 35598123,
        "too_big_errors": 0,
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
            "ip_address": {
                "13.43.1.12": {
                    "port": 151,
                    "buffer": "0/10",
                    "sent": 102045,
                    "dropped": 3065
                },
                "12.44.133.10": {
                    "port": 111,
                    "buffer": "0/10",
                    "sent": 102045,
                    "dropped": 3065
                },
                "116.75.154.186": {
                    "port": 169,
                    "buffer": "0/10",
                    "sent": 201075,
                    "dropped": 11383
                },
                "126.35.67.19": {
                    "port": 108,
                    "buffer": "0/10",
                    "sent": 102045,
                    "dropped": 3065
                }
            }
        }
    }
}