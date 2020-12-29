expected_output = {
    "switch": {
        "1": {
            "fan": {
                "1": {
                    "speed": 5130,
                    "state": "OK"
                },
                "2": {
                    "speed": 5100,
                    "state": "OK"
                }
            },
            "hotspot_temperature": {
                "red_threshold": "125",
                "state": "GREEN",
                "value": "36",
                "yellow_threshold": "105"
            },
            "inlet_temperature": {
                "red_threshold": "56",
                "state": "GREEN",
                "value": "22",
                "yellow_threshold": "46"
            },
            "outlet_temperature": {
                "red_threshold": "125",
                "state": "GREEN",
                "value": "27",
                "yellow_threshold": "105"
            },
            "power_supply": {
                "1": {
                    "pid": "PWR-C5-125WAC",
                    "poe_power": "n/a",
                    "serial_number": "LIT23083E9Q",
                    "status": "OK",
                    "system_power": "Good",
                    "watts": "125"
                },
                "2": {
                    "status": "Not Present"
                }
            },
            "system_temperature_state": "OK"
        }
    }
}
