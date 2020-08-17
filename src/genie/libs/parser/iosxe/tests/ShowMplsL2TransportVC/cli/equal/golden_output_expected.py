expected_output = {
    "interface": {
        "Serial5/0": {
            "destination_address": {
                "10.0.0.1": {
                    "vc_id": {"55": {"vc_status": "UP", "local_circuit": "FR DLCI 55"}}
                }
            }
        },
        "ATM4/0": {
            "destination_address": {
                "10.0.0.1": {
                    "vc_id": {
                        "100": {"vc_status": "UP", "local_circuit": "ATM AAL5 0/100"},
                        "200": {"vc_status": "UP", "local_circuit": "ATM AAL5 0/200"},
                    }
                }
            }
        },
        "ATM4/0.300": {
            "destination_address": {
                "10.0.0.1": {
                    "vc_id": {
                        "300": {"vc_status": "UP", "local_circuit": "ATM AAL5 0/300"}
                    }
                }
            }
        },
    }
}
