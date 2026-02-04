expected_output = {
    "switch": {
        "1": {
            "alarms": {
                "ALARM CONTACT 1": {
                    "status": "not asserted",
                    "description": "external alarm contact 1",
                    "severity": "minor",
                    "trigger": "closed"
                },
                "ALARM CONTACT 2": {
                    "status": "not asserted",
                    "description": "external alarm contact 2",
                    "severity": "minor",
                    "trigger": "closed"
                },
                "ALARM CONTACT 3": {
                    "status": "not asserted",
                    "description": "external alarm contact 3",
                    "severity": "minor",
                    "trigger": "closed"
                },
                "ALARM CONTACT 4": {
                    "status": "not asserted",
                    "description": "external alarm contact 4",
                    "severity": "minor",
                    "trigger": "closed"
                }
            },
            "system_temperature": "OK",
            "temperature_sensors": {
                "Inlet Temp Sensor": {
                    "reading": {
                        "value": "46",
                        "unit": "C"
                    },
                    "state": "GREEN",
                    "yellow_threshold": "80 C",
                    "red_threshold": "96 C"
                },
                "Outlet Temp Sensor": {
                    "reading": {
                        "value": "40",
                        "unit": "C"
                    },
                    "state": "GREEN",
                    "yellow_threshold": "80 C",
                    "red_threshold": "96 C"
                },
                "External-1 Temp Sensor": {
                    "reading": {
                        "value": "32",
                        "unit": "C"
                    },
                    "state": "GREEN",
                    "yellow_threshold": "80 C",
                    "red_threshold": "96 C"
                },
                "External-2 Temp Sensor": {
                    "reading": {
                        "value": "33",
                        "unit": "C"
                    },
                    "state": "GREEN",
                    "yellow_threshold": "80 C",
                    "red_threshold": "96 C"
                },
                "HotSpot Temp Sensor": {
                    "reading": {
                        "value": "37",
                        "unit": "C"
                    },
                    "state": "GREEN",
                    "yellow_threshold": "105 C",
                    "red_threshold": "125 C"
                }
            },
            "power_supply": {
                "POWER SUPPLY-1": {
                    "pid": "Not Present",
                    "status": "Not Present"
                },
                "POWER SUPPLY-2": {
                    "pid": "PWR-RGD-AC-DC-250",
                    "serial": "DTH255202J5",
                    "status": "OK",
                    "sys_pwr": "Good",
                    "watts": "250"
                }
            },
            "sensors": {
                "PS-1 Vout": {
                    "status": "Not Present",
                    "reading": "0mV"
                },
                "PS-1 Curout": {
                    "status": "Not Present",
                    "reading": "0mA"
                },
                "PS-1 Powout": {
                    "status": "Not Present",
                    "reading": "0mW"
                },
                "PS-1 Hotspot": {
                    "status": "Not Present",
                    "reading": "0 C"
                },
                "PS-2 Vout": {
                    "status": "Good",
                    "reading": "55000mV"
                },
                "PS-2 Curout": {
                    "status": "Good",
                    "reading": "500mA"
                },
                "PS-2 Powout": {
                    "status": "Good",
                    "reading": "27500mW"
                },
                "PS-2 Hotspot": {
                    "status": "Good",
                    "reading": "49 C"
                }
            }
        }
    }
}
