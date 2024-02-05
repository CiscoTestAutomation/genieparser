expected_output = {
    "critical_larams": 1,
    "major_alarms": 4,
    "minor_alarms": 0,
    "slot": {
        "P2": {
            "sensor": {
                "RPM: fan0": {
                    "state": "Warning",
                    "reading": "25800 RPM"
                },
                "RPM: fan1": {
                    "state": "Warning",
                    "reading": "25320 RPM"
                },
                "RPM: fan2": {
                    "state": "Warning",
                    "reading": "25920 RPM"
                },
                "RPM: fan3": {
                    "state": "Warning",
                    "reading": "25500 RPM"
                },
                "P: pwr": {
                    "state": "Normal",
                    "reading": "34 Watts"
                }
            }
        },
        "R0": {
            "sensor": {
                "Temp: Inlet": {
                    "state": "Critical",
                    "reading": "47 Celsius",
                    "threshold": {
                        "celsius": True,
                        "critical": 47
                    }
                },
                "Temp: Internal": {
                    "state": "Normal",
                    "reading": "47 Celsius",
                    "threshold": {
                        "celsius": True
                    }
                },
                "Temp: Outlet": {
                    "state": "Normal",
                    "reading": "50 Celsius",
                    "threshold": {
                        "celsius": True,
                        "critical": 75
                    }
                },
                "Temp: CPU": {
                    "state": "Normal",
                    "reading": "53 Celsius",
                    "threshold": {
                        "celsius": True,
                        "critical": 100
                    }
                },
                "V: 12v": {
                    "state": "Normal",
                    "reading": "11917 mV"
                },
                "V: 5v": {
                    "state": "Normal",
                    "reading": "5059 mV"
                },
                "V: 3.3v": {
                    "state": "Normal",
                    "reading": "3323 mV"
                },
                "V: 3.0v": {
                    "state": "Normal",
                    "reading": "2995 mV"
                },
                "V: 2.5v": {
                    "state": "Normal",
                    "reading": "2493 mV"
                },
                "V: 1.35v CPU": {
                    "state": "Normal",
                    "reading": "1351 mV"
                },
                "V: 1.8v": {
                    "state": "Normal",
                    "reading": "1822 mV"
                },
                "V: 1.2v": {
                    "state": "Normal",
                    "reading": "1198 mV"
                },
                "V: VNN CPU": {
                    "state": "Normal",
                    "reading": "977 mV"
                },
                "V: 1.1v": {
                    "state": "Normal",
                    "reading": "1073 mV"
                },
                "V: 1.0v": {
                    "state": "Normal",
                    "reading": "999 mV"
                },
                "V: 1.8v CPU": {
                    "state": "Normal",
                    "reading": "1832 mV"
                },
                "V: DDR": {
                    "state": "Normal",
                    "reading": "1535 mV"
                },
                "V: 3.3v STBY": {
                    "state": "Normal",
                    "reading": "3384 mV"
                },
                "V: 1.5v": {
                    "state": "Normal",
                    "reading": "1514 mV"
                },
                "V: 1.0v CPU": {
                    "state": "Normal",
                    "reading": "991 mV"
                },
                "V: VCC CPU": {
                    "state": "Normal",
                    "reading": "858 mV"
                },
                "V: 0.75v": {
                    "state": "Normal",
                    "reading": "763 mV"
                },
                "I: 12v": {
                    "state": "Normal",
                    "reading": "6 A"
                },
                "P: pwr": {
                    "state": "Normal",
                    "reading": "62 Watts"
                }
            }
        }
    }
}