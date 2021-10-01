

expected_output = {
    "0/0/1/2": {
        "name": "Optics 0/0/1/2",
        "controller_state": "Up",
        "transport_admin_state": "In Service",
        "laser_state": "On",
        "led_state": "Green",
        "optics_status": {
            "optics_type": "CFP2 DWDM",
            "dwdm_carrier_info": "C BAND",
            "msa_itu_channel": "97",
            "frequency": "191.30THz",
            "wavelength": "1567.133nm",
            "alarm_status": {
                "detected_alarms": [],
            },
            "los_lol_fault_status": {},
            "alarm_statistics": {
                "high_rx_pwr": 0,
                "low_rx_pwr": 1,
                "high_tx_pwr": 0,
                "low_tx_pwr": 1,
                "high_lbc": 0,
                "high_dgd": 0,
                "oor_cd": 0,
                "osnr": 0,
                "wvl_ool": 0,
                "mea": 0,
                "improper_rem": 0,
                "tc_power_prov_mismatch": 0
            },
            "laser_bias_current": "0.0 %",
            "actual_tx_power": "0.99 dBm",
            "rx_power": "-20.50 dBm",
            "performance_monitoring": "Enable",
            "threshold_values": {
                "Rx Power Threshold(dBm)": {
                    "parameter": "Rx Power Threshold(dBm)",
                    "high_alarm": "1.5",
                    "low_alarm": "-30.0",
                    "high_warning": "0.0",
                    "low_warning": "0.0"
                },
                "Tx Power Threshold(dBm)": {
                    "parameter": "Tx Power Threshold(dBm)",
                    "high_alarm": "3.5",
                    "low_alarm": "-10.0",
                    "high_warning": "0.0",
                    "low_warning": "0.0"
                },
                "LBC Threshold(mA)": {
                    "parameter": "LBC Threshold(mA)",
                    "high_alarm": "N/A",
                    "low_alarm": "N/A",
                    "high_warning": "0.00",
                    "low_warning": "0.00"
                }
            },
            "lbc_high_threshold": "98 %",
            "configured_tx_power": "1.00 dBm",
            "configured_osnr_lower_threshold": "0.00 dB",
            "configured_dgd_higher_threshold": "180.00 ps",
            "chromatic_dispersion": "5 ps/nm",
            "configured_cd_min": "-10000 ps/nm ",
            "configured_cd_max": "16000 ps/nm",
            "optical_snr": "27.00 dB",
            "polarization_dependent_loss": "0.00 dB",
            "differential_group_delay": "2.00 ps"
        },
        "transceiver_vendor_details": {
            "form_factor": "CFP2",
            "name": "CISCO-ACACIA",
            "part_number": "AC200-D23-190",
            "rev_number": "16672",
            "serial_number": "180653009",
            "pid": "ONS-C2-WDM-DE-1HL",
            "vid": "VES#",
            "date_code": "18/02/03"
        }
    }
}
