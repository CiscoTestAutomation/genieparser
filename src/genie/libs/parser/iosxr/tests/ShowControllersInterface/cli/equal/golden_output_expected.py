expected_output = {
    'interface': {
        'FourHundredGigE0/0/0/2': {
            'state': {
            'administrative_state': 'disabled',
            'operational_state': 'Down (Reason: Link is shutdown)',
            'led_state': 'Off'
            },
            'phy': {
            'media_type': '2x200G over 8 lane passive copper',
            'optics': {
                'vendor': 'CISCO-LUXSHARE',
                'part_number': 'L0FDD013-SD-R',
                'serial_number': 'SNL2750F020',
                'wavelength': '0 nm'
            },
            'digital_optical_monitoring': {
                'transceiver_temp': '0.000 C',
                'transceiver_voltage': '0.000 V',
                'lane': {
                    '0': {
                        'wavelength_nm': 'n/a',
                        'tx_power_dbm': '-40.0',
                        'tx_power_mw': '0.0001',
                        'rx_power_dbm': '-40.0',
                        'rx_power_mw': '0.0001',
                        'laser_bias_ma': '0.000'
                    },
                    '1': {
                        'wavelength_nm': 'n/a',
                        'tx_power_dbm': '-40.0',
                        'tx_power_mw': '0.0001',
                        'rx_power_dbm': '-40.0',
                        'rx_power_mw': '0.0001',
                        'laser_bias_ma': '0.000'
                    },
                    '2': {
                        'wavelength_nm': 'n/a',
                        'tx_power_dbm': '-40.0',
                        'tx_power_mw': '0.0001',
                        'rx_power_dbm': '-40.0',
                        'rx_power_mw': '0.0001',
                        'laser_bias_ma': '0.000'
                    },
                    '3': {
                        'wavelength_nm': 'n/a',
                        'tx_power_dbm': '-40.0',
                        'tx_power_mw': '0.0001',
                        'rx_power_dbm': '-40.0',
                        'rx_power_mw': '0.0001',
                        'laser_bias_ma': '0.000'
                    },
                    '4': {
                        'wavelength_nm': 'n/a',
                        'tx_power_dbm': '-40.0',
                        'tx_power_mw': '0.0001',
                        'rx_power_dbm': '-40.0',
                        'rx_power_mw': '0.0001',
                        'laser_bias_ma': '0.000'
                    },
                    '5': {
                        'wavelength_nm': 'n/a',
                        'tx_power_dbm': '-40.0',
                        'tx_power_mw': '0.0001',
                        'rx_power_dbm': '-40.0',
                        'rx_power_mw': '0.0001',
                        'laser_bias_ma': '0.000'
                    },
                    '6': {
                        'wavelength_nm': 'n/a',
                        'tx_power_dbm': '-40.0',
                        'tx_power_mw': '0.0001',
                        'rx_power_dbm': '-40.0',
                        'rx_power_mw': '0.0001',
                        'laser_bias_ma': '0.000'
                    },
                    '7': {
                        'wavelength_nm': 'n/a',
                        'tx_power_dbm': '-40.0',
                        'tx_power_mw': '0.0001',
                        'rx_power_dbm': '-40.0',
                        'rx_power_mw': '0.0001',
                        'laser_bias_ma': '0.000'
                    }
                },
                'alarm_thresholds': {
                    'Transceiver Temp (C)': {
                        'alarm_high': '0.000',
                        'warning_high': '0.000',
                        'warning_low': '0.000',
                        'alarm_low': '0.000'
                    },
                    'Transceiver Voltage (V)': {
                        'alarm_high': '0.000',
                        'warning_high': '0.000',
                        'warning_low': '0.000',
                        'alarm_low': '0.000'
                    },
                    'Laser Bias (mA)': {
                        'alarm_high': '0.000',
                        'warning_high': '0.000',
                        'warning_low': '0.000',
                        'alarm_low': '0.000'
                    },
                    'Transmit Power (mW)': {
                        'alarm_high': '0.000',
                        'warning_high': '0.000',
                        'warning_low': '0.000',
                        'alarm_low': '0.000'
                    },
                    'Transmit Power (dBm)': {
                        'alarm_high': '-inf',
                        'warning_high': '-inf',
                        'warning_low': '-inf',
                        'alarm_low': '-inf'
                    },
                    'Receive Power (mW)': {
                        'alarm_high': '0.000',
                        'warning_high': '0.000',
                        'warning_low': '0.000',
                        'alarm_low': '0.000'
                    },
                    'Receive Power (dBm)': {
                        'alarm_high': '-inf',
                        'warning_high': '-inf',
                        'warning_low': '-inf',
                        'alarm_low': '-inf'
                    }
                }
            },
            'statistics': {
                'fec': {
                    'corrected_codeword_count': 0,
                    'uncorrected_codeword_count': 0
                }
            }
            },
            'mac_address_information': {
            'operational_address': 'fc58.9a14.a010',
            'burnt_in_address': 'fc58.9a14.a010'
            },
            'autonegotiation': 'Autonegotiation disabled.',
            'priority_flow_control': {
            'total_rx_pfc_frames': 0,
            'total_tx_pfc_frames': 0,
            'total_rx_dropped_data_frames': 0,
            'cos': {
                0: {'status': 'off', 'rx_pfc_frames': 0},
                1: {'status': 'off', 'rx_pfc_frames': 0},
                2: {'status': 'off', 'rx_pfc_frames': 0},
                3: {'status': 'off', 'rx_pfc_frames': 0},
                4: {'status': 'off', 'rx_pfc_frames': 0},
                5: {'status': 'off', 'rx_pfc_frames': 0},
                6: {'status': 'off', 'rx_pfc_frames': 0},
                7: {'status': 'off', 'rx_pfc_frames': 0}
            }
            },
            'operational_values': {
            'speed': '400Gbps',
            'duplex': 'Full Duplex',
            'flowcontrol': 'None',
            'priority_flow_control': 'None',
            'loopback': 'None (or external)',
            'mtu': 1514,
            'mru': 1518,
            'forward_error_correction': 'Standard (Reed-Solomon)'
            }
        }
    }
}
