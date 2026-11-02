expected_output = {
    "critical_alarms": 0,
    "critical_larams": 0,
    "major_alarms": 0,
    "minor_alarms": 2,
    "slot": {
        "P0": {
            "sensor": {
                "I: PEM In": {"reading": "234    mA", "state": "Normal"},
                "I: PEM Out": {"reading": "2500   mA", "state": "Normal"},
                "P: In power": {"reading": "40     Watts", "state": "Normal"},
                "P: Out power": {"reading": "28     Watts", "state": "Normal"},
                "RPM: fan0": {"reading": "4672   RPM", "state": "Normal"},
                "Temp: Temp 1": {
                    "reading": "35     Celsius",
                    "state": "Normal",
                    "threshold": {"celsius": True},
                },
                "Temp: Temp 2": {
                    "reading": "38     Celsius",
                    "state": "Normal",
                    "threshold": {"celsius": True},
                },
                "Temp: Temp 3": {
                    "reading": "38     Celsius",
                    "state": "Normal",
                    "threshold": {"celsius": True},
                },
                "V: PEM In": {"reading": "204502 mV", "state": "Normal"},
                "V: PEM Out": {"reading": "12000  mV", "state": "Normal"},
            }
        },
        "P1": {
            "sensor": {
                "I: PEM In": {"reading": "0      mA", "state": "Normal"},
                "I: PEM Out": {"reading": "0      mA", "state": "Normal"},
                "P: In power": {"reading": "0      Watts", "state": "Normal"},
                "P: Out power": {"reading": "0      Watts", "state": "Normal"},
                "RPM: fan0": {"reading": "0      RPM", "state": "Minor_Low"},
                "Temp: Temp 1": {
                    "reading": "0      Celsius",
                    "state": "Normal",
                    "threshold": {"celsius": True},
                },
                "Temp: Temp 2": {
                    "reading": "0      Celsius",
                    "state": "Normal",
                    "threshold": {"celsius": True},
                },
                "Temp: Temp 3": {
                    "reading": "0      Celsius",
                    "state": "Normal",
                    "threshold": {"celsius": True},
                },
                "V: PEM In": {"reading": "0      mV", "state": "Normal"},
                "V: PEM Out": {"reading": "0      mV", "state": "Minor_Low"},
            }
        },
        "P2": {
            "sensor": {
                "P: Power": {"reading": "0      Watts", "state": "Normal"},
                "RPM: fan0": {"reading": "5220   RPM", "state": "Normal"},
                "RPM: fan1": {"reading": "5280   RPM", "state": "Normal"},
                "RPM: fan2": {"reading": "5040   RPM", "state": "Normal"},
            }
        },
        "R0": {
            "sensor": {
                "P: Power": {"reading": "30     Watts", "state": "Normal"},
                "Temp: CPU": {
                    "reading": "37     Celsius",
                    "state": "Normal",
                    "threshold": {"celsius": True, "critical": 95},
                },
                "Temp: Inlet 1": {
                    "reading": "27     Celsius",
                    "state": "Normal",
                    "threshold": {"celsius": True, "critical": 42, "minor": 40},
                },
                "Temp: Inlet 2": {
                    "reading": "28     Celsius",
                    "state": "Normal",
                    "threshold": {
                        "celsius": True,
                        "critical": 100,
                        "minor": 90,
                    },
                },
                "Temp: Outlet 1": {
                    "reading": "29     Celsius",
                    "state": "Normal",
                    "threshold": {"celsius": True, "critical": 75, "minor": 70},
                },
                "Temp: Outlet 2": {
                    "reading": "28     Celsius",
                    "state": "Normal",
                    "threshold": {"celsius": True, "critical": 75, "minor": 70},
                },
                "Temp: Working": {
                    "reading": "27     Celsius",
                    "state": "Normal",
                    "threshold": {"celsius": True},
                },
                "V: 0.75V": {"reading": "746    mV", "state": "Normal"},
                "V: 0.85V_DDR": {"reading": "849    mV", "state": "Normal"},
                "V: 0.8V_CORE": {"reading": "798    mV", "state": "Normal"},
                "V: 0.8V_PHY": {"reading": "798    mV", "state": "Normal"},
                "V: 0.8V_SW": {"reading": "830    mV", "state": "Normal"},
                "V: 0.8V_SYS": {"reading": "847    mV", "state": "Normal"},
                "V: 1.0V": {"reading": "996    mV", "state": "Normal"},
                "V: 1.1V": {"reading": "1097   mV", "state": "Normal"},
                "V: 1.2V": {"reading": "1206   mV", "state": "Normal"},
                "V: 1.2V_CPU": {"reading": "1197   mV", "state": "Normal"},
                "V: 1.8V": {"reading": "1796   mV", "state": "Normal"},
                "V: 12V": {"reading": "11980  mV", "state": "Normal"},
                "V: 2.5V": {"reading": "2505   mV", "state": "Normal"},
                "V: 3.3V": {"reading": "3308   mV", "state": "Normal"},
                "V: 3.3V_STBY": {"reading": "3327   mV", "state": "Normal"},
                "V: 3.3V_USB": {"reading": "3306   mV", "state": "Normal"},
                "V: 5V": {"reading": "5000   mV", "state": "Normal"},
            }
        },
    },
}
