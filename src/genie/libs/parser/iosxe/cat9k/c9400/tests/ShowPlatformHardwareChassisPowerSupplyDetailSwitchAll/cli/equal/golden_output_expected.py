expected_output = {
    "power_supplies": {
        "PS2": {
            "fan1_speed": 4108,
            "fan2_speed": 3978,
            "faults": {
                "LATCHED_FAULT": {
                    "description": "Vout " "out " "of " "range",
                    "reg_value": "0x00 " "0x00 " "0x02 ",
                },
                "REAL_TIME_FAULT": {
                    "description": "No " "Faults",
                    "reg_value": "0x00 " "0x00 " "0x00 ",
                },
            },
            "heatsink_temperature": 48,
            "input": {
                "current_a": 1.6,
                "current_b": "n.a",
                "power_a": 348.0,
                "power_b": "n.a",
                "voltage_a": 239.0,
                "voltage_b": "n.a",
            },
            "output": {"current": 5.7, "power": 313.0, "voltage": 55.0},
        },
        "PS5": {
            "fan1_speed": 4065,
            "fan2_speed": 4065,
            "faults": {
                "LATCHED_FAULT": {
                    "description": "No " "Faults",
                    "reg_value": "0x00 " "0x00 " "0x00 ",
                },
                "REAL_TIME_FAULT": {
                    "description": "No " "Faults",
                    "reg_value": "0x00 " "0x00 " "0x00 ",
                },
            },
            "heatsink_temperature": 47,
            "input": {
                "current_a": 1.7,
                "current_b": "n.a",
                "power_a": 391.0,
                "power_b": "n.a",
                "voltage_a": 239.0,
                "voltage_b": "n.a",
            },
            "output": {"current": 6.5, "power": 355.0, "voltage": 55.0},
        },
    }
}
