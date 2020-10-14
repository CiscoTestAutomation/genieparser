expected_output = {
    "policy_map": {
        "policy_4-6-3~6": {
            "class": {
                "class_4-6-3": {
                    "average_rate_traffic_shaping": True,
                    "cir_bps": 100000000,
                    "bc_bits": 80000000,
                },
                "class_4-6-4~6": {
                    "average_rate_traffic_shaping": True,
                    "cir_bps": 100000000,
                    "bc_bits": 80000000,
                    "be_bits": 60000000,
                },
                "system-cpp-police-sys-data": {
                    "police": {
                        "rate_pps": 100,
                        "conform_action": ["transmit"],
                        "exceed_action": ["drop"],
                    }
                },
            }
        }
    }
}
