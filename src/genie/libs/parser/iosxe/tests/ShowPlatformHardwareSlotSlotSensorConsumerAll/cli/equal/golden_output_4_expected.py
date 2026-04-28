expected_output = {
    "slot": {
        "registration": "Registered",
        "sensors": {
            640: {"name": "Temp1", "data": 22, "unit": "C", "last_poll": "15:53:27"},
            641: {"name": "Temp: FC PWM1", "data": 25, "unit": "C", "last_poll": "15:53:27"},
            660: {"name": "Temp1", "data": 24, "unit": "C", "last_poll": "15:53:27"},
            661: {"name": "Temp: FC PWM1", "data": 25, "unit": "C", "last_poll": "15:53:27"},
            620: {"name": "Temp1", "data": 22, "unit": "C", "last_poll": "15:53:27"},
            621: {"name": "Temp: FC PWM1", "data": 25, "unit": "C", "last_poll": "15:53:27"},

            500: {"name": "Vin", "data": 228000, "unit": "mV", "last_poll": "15:53:27"},
            501: {"name": "Pin", "data": 872784, "unit": "", "last_poll": "15:53:27"},
            502: {"name": "Iin", "data": 3828, "unit": "mA", "last_poll": "15:53:27"},
            503: {"name": "Vout", "data": 12035, "unit": "mV", "last_poll": "15:53:27"},
            504: {"name": "Pout", "data": -4797, "unit": "", "last_poll": "15:53:27"},
            505: {"name": "Iout", "data": 64625, "unit": "mA", "last_poll": "15:53:27"},
            506: {"name": "Temp1", "data": 23, "unit": "C", "last_poll": "15:53:27"},
            507: {"name": "Temp2", "data": 31, "unit": "C", "last_poll": "15:53:27"},
            508: {"name": "Temp3", "data": 34, "unit": "C", "last_poll": "15:53:27"},

            520: {"name": "Vin", "data": 0, "unit": "mV", "last_poll": "15:53:27"},
            521: {"name": "Pin", "data": 0, "unit": "", "last_poll": "15:53:27"},
            522: {"name": "Iin", "data": 0, "unit": "mA", "last_poll": "15:53:27"},
            523: {"name": "Vout", "data": 0, "unit": "mV", "last_poll": "15:53:27"},
            524: {"name": "Pout", "data": 0, "unit": "", "last_poll": "15:53:27"},
            525: {"name": "Iout", "data": 0, "unit": "mA", "last_poll": "15:53:27"},
            526: {"name": "Temp1", "data": 23, "unit": "C", "last_poll": "15:53:27"},
            527: {"name": "Temp2", "data": 0, "unit": "C", "last_poll": "15:53:27"},
            528: {"name": "Temp3", "data": 24, "unit": "C", "last_poll": "15:53:27"},

            540: {"name": "Vin", "data": 0, "unit": "mV", "last_poll": "15:53:27"},
            541: {"name": "Pin", "data": 0, "unit": "", "last_poll": "15:53:27"},
            542: {"name": "Iin", "data": 0, "unit": "mA", "last_poll": "15:53:27"},
            543: {"name": "Vout", "data": 0, "unit": "mV", "last_poll": "15:53:27"},
            544: {"name": "Pout", "data": 0, "unit": "", "last_poll": "15:53:27"},
            545: {"name": "Iout", "data": 0, "unit": "mA", "last_poll": "15:53:27"},
            546: {"name": "Temp1", "data": 22, "unit": "C", "last_poll": "15:53:27"},
            547: {"name": "Temp2", "data": 0, "unit": "C", "last_poll": "15:53:27"},
            548: {"name": "Temp3", "data": 24, "unit": "C", "last_poll": "15:53:27"},

            20: {"name": "VVM 0: VX1", "data": 604, "unit": "mV", "last_poll": "15:53:27"},
            21: {"name": "VVM 0: VX2", "data": 1212, "unit": "mV", "last_poll": "15:53:27"},
            22: {"name": "VVM 0: VX3", "data": 1209, "unit": "mV", "last_poll": "15:53:27"},
            23: {"name": "VVM 0: VX4", "data": 996, "unit": "mV", "last_poll": "15:53:27"},
            24: {"name": "VVM 0: VP1", "data": 3333, "unit": "mV", "last_poll": "15:53:27"},
            25: {"name": "VVM 0: VP2", "data": 3347, "unit": "mV", "last_poll": "15:53:27"},
            26: {"name": "VVM 0: VP3", "data": 5033, "unit": "mV", "last_poll": "15:53:27"},
            27: {"name": "VVM 0: VP4", "data": 1509, "unit": "mV", "last_poll": "15:53:27"},
            28: {"name": "VVM 0: VH", "data": 11924, "unit": "mV", "last_poll": "15:53:27"},

            29: {"name": "VVM 1: VX3", "data": 1053, "unit": "mV", "last_poll": "15:53:27"},
            30: {"name": "VVM 1: VP1", "data": 1701, "unit": "mV", "last_poll": "15:53:27"},
            31: {"name": "VVM 1: VP2", "data": 1810, "unit": "mV", "last_poll": "15:53:27"},
            32: {"name": "VVM 1: VP3", "data": 2525, "unit": "mV", "last_poll": "15:53:27"},
            33: {"name": "VVM 1: VP4", "data": 3248, "unit": "mV", "last_poll": "15:53:27"},
            34: {"name": "VVM 1: VH", "data": 11909, "unit": "mV", "last_poll": "15:53:27"},

            35: {"name": "VVM 2: VX1", "data": 995, "unit": "mV", "last_poll": "15:53:27"},
            36: {"name": "VVM 2: VP1", "data": 1197, "unit": "mV", "last_poll": "15:53:27"},
            37: {"name": "VVM 2: VP2", "data": 1807, "unit": "mV", "last_poll": "15:53:27"},
            38: {"name": "VVM 2: VH", "data": 11914, "unit": "mV", "last_poll": "15:53:27"},

            39: {"name": "Temp: CPU-IN", "data": 24, "unit": "C", "last_poll": "15:53:27"},
            40: {"name": "Temp: Outlet", "data": 31, "unit": "C", "last_poll": "15:53:27"},
            41: {"name": "Temp: Center", "data": 18, "unit": "C", "last_poll": "15:53:27"},
            42: {"name": "Temp: Inlet", "data": 29, "unit": "C", "last_poll": "15:53:27"},
            43: {"name": "Temp: DDR4 In", "data": 29, "unit": "C", "last_poll": "15:53:27"},
            44: {"name": "Temp: DDR4 Out", "data": 23, "unit": "C", "last_poll": "15:53:27"}
        }
    }
}