expected_output = {
    "switch": {
        "1": {
            "alarms": {
                "ALARM CONTACT 1": {
                    "status": "not asserted",
                    "description": "external alarm contact 1",
                    "severity": "minor",
                    "trigger": "closed"
                }
            },
            "system_temperature": "OK",
            "temperature_sensors": {
                "Inlet Temp Sensor": {
                    "reading": {
                        "value": "45",
                        "unit": "C"
                    },
                    "state": "GREEN",
                    "yellow_threshold": "80 C",
                    "red_threshold": "96 C"
                },
                "HotSpot Temp Sensor": {
                    "reading": {
                        "value": "46",
                        "unit": "C"
                    },
                    "state": "GREEN",
                    "yellow_threshold": "105 C",
                    "red_threshold": "125 C"
                }
            }
        }
    },
    "power_supplies": {
        "POWER SUPPLY": {
            "type": "DC",
            "status": "OK"
        }
    }
}
