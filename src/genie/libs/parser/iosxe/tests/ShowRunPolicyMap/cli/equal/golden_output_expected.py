expected_output = {
    "policy_map": {
        "L3VPN-0_in": {
            "class": {
                "HEY_in": {
                    "police": {
                        "cir_bps": "365",
                        "pir_bps": "235",
                        "conformed": "transmit",
                        "exceeded": "drop",
                    }
                },
                "OSPF": {
                    "police": {
                        "cir_bps": "543",
                        "pir_bps": "876",
                        "conformed": "transmit",
                        "exceeded": "drop",
                    }
                },
                "class-default": {
                    "police": {
                        "cir_bps": "2565",
                        "cir_bc_bytes": "4234",
                        "conformed": "transmit",
                        "exceeded": "drop",
                    },
                    "service_policy": "child",
                },
            }
        }
    }
}
