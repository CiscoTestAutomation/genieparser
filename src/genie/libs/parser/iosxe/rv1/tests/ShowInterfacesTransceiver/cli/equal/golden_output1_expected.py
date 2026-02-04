expected_output = {
    "interfaces": {
        "HundredGigE2/0/0": {
            "transceiver": {
                "status": "enabled",
                "slot": 2,
                "subslot": 0,
                "port": 0
            },
            "details": {
                "module_temperature": 22.214,
                "tx_voltage": 3.2405,
                "tx_power": 6.1,
                "rx_power": 6.5
            },
            "lanes": {
                0: {
                    "tx_power": 0.2,
                    "bias_current": 7.494
                },
                1: {
                    "tx_power": 0.1,
                    "bias_current": 7.494
                },
                2: {
                    "tx_power": 0.0,
                    "bias_current": 7.494
                },
                3: {
                    "tx_power": 0.1,
                    "bias_current": 7.494
                }
            },
            "idprom": {
                "description": "QSFP28 optics (type 134)",
                "transceiver_type": "QSFP 100GE SR (411)",
                "pid": "QSFP-100G-SR4-S",
                "vendor_revision": "06",
                "serial_number": "AVF2304S40E",
                "vendor_name": "CISCO-AVAGO",
                "vendor_oui": "00.17.6A",
                "clei_code": "CMUIATKCAA",
                "part_number": "10-3142-03",
                "device_state": "Enabled",
                "date_code": "19/01/27",
                "connector_type": "MPO",
                "encoding": "64B66B",
                "nominal_bitrate": "25GE (25500 Mbits/s)ITU Channel not available (Wavelength not available),"
            },
            "port": "HundredGigE2/0/0",
            "temp": "22.1",
            "voltage": "3.24",
            "current": "7.4",
            "opticaltx": "0.09",
            "opticalrx": "0.44"
        }
    }
}