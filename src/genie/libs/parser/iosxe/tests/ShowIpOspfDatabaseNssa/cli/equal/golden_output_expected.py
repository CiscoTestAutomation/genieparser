expected_output = {
    "ospf_router": {
        "router_id": "1.1.1.1",
        "process_id": 1,
        "type_7_as_external_link_states": {
            "area": 40,
            "link_states": {
                0: {
                    "ls_age": 117,
                    "options": "(No TOS-capability, Type 7/5 translation, DC)",
                    "ls_type": "AS External Link",
                    "link_state_id": "223.255.0.0",
                    "advertising_router": "1.1.1.1",
                    "ls_seq_number": "80000001",
                    "checksum": 0x66B7,
                    "length": 36,
                    "network_mask": 16,
                    "metric_type": 1,
                    "mtid": 0,
                    "metric": 10,
                    "forward_address": "10.10.10.1",
                    "external_route_tag": 0
                }
            }
        }
    }
}
