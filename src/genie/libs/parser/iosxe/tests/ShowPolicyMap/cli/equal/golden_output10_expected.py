expected_output = {
    "policy_map": {
        "police": {
            "class": {
                "class-default": {
                    "police": {
                        "cir_bps": 1000000,
                        "cir_bc_bytes": 31250,
                        "pir": 2000000,
                        "pir_be_bytes": 31250,
                        "conform_action": ["transmit"],
                        "exceed_action": ["set-prec-transmit 4", "set-frde-transmit"],
                        "violate_action": ["set-prec-transmit 2", "set-frde-transmit"],
                    }
                }
            }
        }
    }
}
