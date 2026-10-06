expected_output = {
    'critical_alarms': 0,
    'major_alarms': 0,
    'minor_alarms': 0,
    'sensor_list': {
        'Environmental Monitoring': {
            'location': {
                'R0': {
                    'sensor': {
                        'Temp: CPU board': {
                            'state': 'Normal',
                            'reading': '33 Celsius',
                            'threshold': {
                                'minor': 52,
                                'major': 57,
                                'critical': 62,
                                'shutdown': 67,
                                'unit': 'Celsius',
                            },
                        },
                        'Temp: FANIO': {
                            'state': 'Normal',
                            'reading': '35 Celsius',
                            'threshold': {
                                'minor': 53,
                                'major': 58,
                                'critical': 63,
                                'shutdown': 68,
                                'unit': 'Celsius',
                            },
                        },
                        'Temp: F_Left': {
                            'state': 'Normal',
                            'reading': '28 Celsius',
                            'threshold': {
                                'minor': 52,
                                'major': 57,
                                'critical': 62,
                                'shutdown': 67,
                                'unit': 'Celsius',
                            },
                        },
                        'Temp: E104': {
                            'state': 'Normal',
                            'reading': '34 Celsius',
                            'threshold': {
                                'minor': 65,
                                'major': 70,
                                'critical': 75,
                                'shutdown': 80,
                                'unit': 'Celsius',
                            },
                        },
                        'Temp: F_Right': {
                            'state': 'Normal',
                            'reading': '30 Celsius',
                            'threshold': {
                                'minor': 54,
                                'major': 59,
                                'critical': 64,
                                'shutdown': 69,
                                'unit': 'Celsius',
                            },
                        },
                        'Temp: S1_K0_00': {
                            'state': 'Normal',
                            'reading': '45 Celsius',
                            'threshold': {
                                'minor': 95,
                                'major': 105,
                                'critical': 115,
                                'shutdown': 125,
                                'unit': 'Celsius',
                            },
                        },
                        'Temp: S1_K0_01': {
                            'state': 'Normal',
                            'reading': '45 Celsius',
                            'threshold': {
                                'minor': 95,
                                'major': 105,
                                'critical': 115,
                                'shutdown': 125,
                                'unit': 'Celsius',
                            },
                        },
                        'Temp: S1_K0_02': {
                            'state': 'Normal',
                            'reading': '45 Celsius',
                            'threshold': {
                                'minor': 95,
                                'major': 105,
                                'critical': 115,
                                'shutdown': 125,
                                'unit': 'Celsius',
                            },
                        },
                        'Temp: S1_K0_03': {
                            'state': 'Normal',
                            'reading': '47 Celsius',
                            'threshold': {
                                'minor': 95,
                                'major': 105,
                                'critical': 115,
                                'shutdown': 125,
                                'unit': 'Celsius',
                            },
                        },
                        'Temp: S1_K0_04': {
                            'state': 'Normal',
                            'reading': '46 Celsius',
                            'threshold': {
                                'minor': 95,
                                'major': 105,
                                'critical': 115,
                                'shutdown': 125,
                                'unit': 'Celsius',
                            },
                        },
                        'Temp: S1_K0_05': {
                            'state': 'Normal',
                            'reading': '46 Celsius',
                            'threshold': {
                                'minor': 95,
                                'major': 105,
                                'critical': 115,
                                'shutdown': 125,
                                'unit': 'Celsius',
                            },
                        },
                        'Temp: S1_K0_06': {
                            'state': 'Normal',
                            'reading': '46 Celsius',
                            'threshold': {
                                'minor': 95,
                                'major': 105,
                                'critical': 115,
                                'shutdown': 125,
                                'unit': 'Celsius',
                            },
                        },
                        'CPU_P3P3V_S0': {
                            'state': 'Normal',
                            'reading': '3297 mV',
                        },
                        'CPU_P3P3V_S5': {
                            'state': 'Normal',
                            'reading': '3296 mV',
                        },
                        'CPU_P0P78V_S0': {
                            'state': 'Normal',
                            'reading': '778 mV',
                        },
                        'CPU_P1P8V_S5': {
                            'state': 'Normal',
                            'reading': '1799 mV',
                        },
                        'CPU_P1P1V_S3': {
                            'state': 'Normal',
                            'reading': '1107 mV',
                        },
                        'CPU_P1P8V_S0': {
                            'state': 'Normal',
                            'reading': '1795 mV',
                        },
                        'CPU_P3V3_STBY': {
                            'state': 'Normal',
                            'reading': '3326 mV',
                        },
                        'CPU_A2P5V': {
                            'state': 'Normal',
                            'reading': '2492 mV',
                        },
                        'CPU_A1P2V': {
                            'state': 'Normal',
                            'reading': '1194 mV',
                        },
                        'CPU_P12V': {
                            'state': 'Normal',
                            'reading': '12013 mV',
                        },
                        'CPU_P0P75V_S5': {
                            'state': 'Normal',
                            'reading': '748 mV',
                        },
                        'CPU_P0P75V_S0': {
                            'state': 'Normal',
                            'reading': '748 mV',
                        },
                        'CPU_P5V': {
                            'state': 'Normal',
                            'reading': '4976 mV',
                        },
                        'CPU_P5V_MGMIO': {
                            'state': 'Normal',
                            'reading': '4970 mV',
                        },
                        'CPU_P3P3V_FRU_S': {
                            'state': 'Normal',
                            'reading': '3282 mV',
                        },
                        'CPU_A3P3V_MGMIO': {
                            'state': 'Normal',
                            'reading': '3284 mV',
                        },
                        'BB_A3P3': {
                            'state': 'Normal',
                            'reading': '3310 mV',
                        },
                        'BB_PLL_1P8V': {
                            'state': 'Normal',
                            'reading': '1804 mV',
                        },
                        'BB_PLL_3P3V': {
                            'state': 'Normal',
                            'reading': '3310 mV',
                        },
                        'BB_P1VF': {
                            'state': 'Normal',
                            'reading': '1008 mV',
                        },
                        'BB_1_8V': {
                            'state': 'Normal',
                            'reading': '1804 mV',
                        },
                        'BB_P1_2VF': {
                            'state': 'Normal',
                            'reading': '1195 mV',
                        },
                        'BB_NPU_AVDD_1P8': {
                            'state': 'Normal',
                            'reading': '1804 mV',
                        },
                        'BB_VDDS_KR0_0P7': {
                            'state': 'Normal',
                            'reading': '748 mV',
                        },
                        'BB_VDDA_KR0_P0V': {
                            'state': 'Normal',
                            'reading': '937 mV',
                        },
                        'BB_VDDCK_KR0_1P': {
                            'state': 'Normal',
                            'reading': '1175 mV',
                        },
                    },
                },
            },
        },
    },
    'power_supply': {
        'PS1': {
            'model_no': 'C9K-PWR-750WAC',
            'type': 'ac',
            'capacity': 'n.a.',
            'status': 'bad-input',
            'fan_1_state': 'n.a.',
            'fan_2_state': 'n.a.',
        },
        'PS2': {
            'model_no': 'C9K-PWR-750WAC',
            'type': 'ac',
            'capacity': '750 W',
            'status': 'active',
            'fan_1_state': 'good',
            'fan_2_state': 'n.a.',
        },
    },
    'fan': {
        'FT1': {
            'status': 'active',
            'fan_1_state': 'good',
            'fan_2_state': 'good',
        },
        'FT2': {
            'status': 'active',
            'fan_1_state': 'good',
            'fan_2_state': 'good',
        },
        'FT3': {
            'status': 'active',
            'fan_1_state': 'good',
            'fan_2_state': 'good',
        },
        'FT4': {
            'status': 'active',
            'fan_1_state': 'good',
            'fan_2_state': 'good',
        },
        'FT5': {
            'status': 'active',
            'fan_1_state': 'good',
            'fan_2_state': 'good',
        },
    },
}
