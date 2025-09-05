expected_output = {
    "voq_details": {
        "Recircport/1": {
            "interface": "Recircport/1",
            "interface_hex": "0x1",
            "voq_oid": 285,
            "voq_oid_hex": "0x11D",
            "voq_set_size": 8,
            "base_voq_id": 256,
            "base_vsc_ids": [128, 208, 288],
            "voq_state": "Active",
            "voq_flush": "Flush not active",
            "is_empty": "Yes",
            "voq_profile_details": {
                "profile_oid": 284,
                "profile_oid_hex": "0x11C",
                "device_id": 0,
                "cgm_type": "Unicast",
                "profile_reference_count": 32,
                "is_reserved": "Yes",
                "for_speeds": 400000000000,
                "associated_voq_offsets": [0, 1, 2, 3, 4, 5, 6, 7],
                "hbm_enabled": "Disabled",
                "q_block_size": 384,
                "red_enabled": "Enabled",
                "fcn_enabled": "Disabled",
                "queue_user_config": {
                    "q_limit_bytes": 983040,
                    "red_ema_coefficient": 1.0,
                    "red_green": {
                        "minimum": 0,
                        "maximum": 983040,
                        "maximum_probability": 0,
                    },
                    "red_yellow": {
                        "minimum": 0,
                        "maximum": 0,
                        "maximum_probability": 0,
                    },
                },
                "queue_hw_values": {
                    "red_ema_coefficient": 1.0,
                    "red_action": "Drop",
                    "red_drop_thresholds": "",
                },
            },
        }
    }
}
