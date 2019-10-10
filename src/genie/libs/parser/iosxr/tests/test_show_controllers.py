
# Python
import unittest
from unittest.mock import Mock

# Genie
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# iosxr show_controllers
from genie.libs.parser.iosxr.show_controllers import (ShowControllersCoherentDSP,
                                                     ShowControllersOptics,
                                                     ShowControllersFiaDiagshellL2showLocation,
                                                     )


# =====================================================
#  Unit test for 'show controllers coherentDSP {port}'
# =====================================================
class test_show_controllers_coherentDSP(unittest.TestCase):
    '''Unit test for show controllers coherentDSP {port}'''

    maxDiff = None
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "0/0/1/2": {
            "port": "CoherentDSP 0/0/1/2",
            "controller_state": "Up",
            "inherited_secondary_state": "Normal",
            "configured_secondary_state": "Normal",
            "derived_state": "In Service",
            "loopback_mode": "None",
            "ber_thresholds_sf": "1.0E-5",
            "ber_thresholds_sd": "1.0E-7",
            "performance_monitoring": "Enable",
            "alarm_info": {
                "los": 1,
                "lof": 0,
                "lom": 0,
                "oof": 0,
                "oom": 0,
                "ais": 0,
                "iae": 0,
                "biae": 0,
                "sf_ber": 0,
                "sd_ber": 0,
                "bdi": 2,
                "tim": 0,
                "fecmis_match": 0,
                "fec_unc": 0
            },
            "detected_alarms": "None",
            "bit_error_rate_info": {
                "prefec_ber": "0.0E+00",
                "postfec_ber": "0.0E+00",
            },
            "otu_tti": "Received",
            "fec_mode": "STANDARD"
        },
    }

    golden_output = {'execute.return_value': '''
        #show controllers coherentDSP 0/0/1/2
        Sat Aug  3 03:10:15.685 EST

        Port                                            : CoherentDSP 0/0/1/2
        Controller State                                : Up
        Inherited Secondary State                       : Normal
        Configured Secondary State                      : Normal
        Derived State                                   : In Service
        Loopback mode                                   : None
        BER Thresholds                                  : SF = 1.0E-5  SD = 1.0E-7
        Performance Monitoring                          : Enable

        Alarm Information:
        LOS = 1 LOF = 0 LOM = 0
        OOF = 0 OOM = 0 AIS = 0
        IAE = 0 BIAE = 0        SF_BER = 0
        SD_BER = 0      BDI = 2 TIM = 0
        FECMISMATCH = 0 FEC-UNC = 0     
        Detected Alarms                                 : None

        Bit Error Rate Information
        PREFEC  BER                                     : 0.0E+00 
        POSTFEC BER                                     : 0.0E+00 

        OTU TTI Received 

        FEC mode                                        : STANDARD
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowControllersCoherentDSP(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(port='0/0/1/2')

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowControllersCoherentDSP(device=self.device)
        parsed_output = obj.parse(port='0/0/1/2')
        self.assertEqual(parsed_output, self.golden_parsed_output)


# ==================================================
#  Unit test for 'show controllers optics {port}'
# ==================================================
class test_show_controllers_optics(unittest.TestCase):
    '''Unit test for show controllers optics {port}'''

    maxDiff = None
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        "0/0/0/0": {
            "name": "Optics 0/0/0/0",
            "controller_state": "Up",
            "transport_admin_state": "In Service",
            "laser_state": "On",
            "led_state": "Green",
            "optics_status": {
                "optics_type": "SFP+ 10G SR",
                "wavelength": "850.00 nm",
                "alarm_status": {
                    "detected_alarms": [],
                },
                "los_lol_fault_status": {},
                "laser_bias_current": "6.1 mA",
                "actual_tx_power": "-2.45 dBm",
                "rx_power": "-7.56 dBm",
                "performance_monitoring": "Enable",
                "threshold_values": {
                    "Rx Power Threshold(dBm)": {
                        "parameter": "Rx Power Threshold(dBm)",
                        "high_alarm": "2.0",
                        "low_alarm": "-13.9",
                        "high_warning": "-1.0",
                        "low_warning": "-9.9"
                    },
                    "Tx Power Threshold(dBm)": {
                        "parameter": "Tx Power Threshold(dBm)",
                        "high_alarm": "1.6",
                        "low_alarm": "-11.3",
                        "high_warning": "-1.3",
                        "low_warning": "-7.3"
                    },
                    "LBC Threshold(mA)": {
                        "parameter": "LBC Threshold(mA)",
                        "high_alarm": "10.00",
                        "low_alarm": "2.00",
                        "high_warning": "10.00",
                        "low_warning": "2.00"
                    },
                    "Temp. Threshold(celsius)": {
                        "parameter": "Temp. Threshold(celsius)",
                        "high_alarm": "75.00",
                        "low_alarm": "-5.00",
                        "high_warning": "70.00",
                        "low_warning": "0.00"
                    },
                    "Voltage Threshold(volt)": {
                        "parameter": "Voltage Threshold(volt)",
                        "high_alarm": "3.63",
                        "low_alarm": "2.97",
                        "high_warning": "3.46",
                        "low_warning": "3.13"
                    }
                },
                "polarization_parameters": "not supported by optics",
                "temperature": "35.00 Celsius",
                "voltage": "3.26 V"
            },
            "transceiver_vendor_details": {
                "form_factor": "SFP+",
                "optics_type": "SFP+ 10G SR",
                "name": "CISCO-AVAGO",
                "oui_number": "00.17.6a",
                "part_number": "SFBR-7702SDZ-CS5",
                "rev_number": "G2.5",
                "serial_number": "AGD162040SP",
                "pid": "SFP-10G-SR",
                "vid": "V03",
                "date_code": "12/05/20"
            }
        }
    }

    golden_output1 = {'execute.return_value': '''
        #show controllers optics 0/0/0/0
        Sat Aug  3 03:11:08.682 EST

         Controller State: Up 
         Transport Admin State: In Service 
         Laser State: On 
         LED State: Green 
         Optics Status 
                 Optics Type:  SFP+ 10G SR
                 Wavelength = 850.00 nm 

                 Alarm Status:
                 -------------
                 Detected Alarms: None


                 LOS/LOL/Fault Status:

                 Laser Bias Current = 6.1 mA
                 Actual TX Power = -2.45 dBm 
                 RX Power = -7.56 dBm 

                 Performance Monitoring: Enable 

                 THRESHOLD VALUES
                 ----------------

                 Parameter                 High Alarm  Low Alarm  High Warning  Low Warning
                 ------------------------  ----------  ---------  ------------  -----------
                 Rx Power Threshold(dBm)          2.0      -13.9          -1.0         -9.9
                 Tx Power Threshold(dBm)          1.6      -11.3          -1.3         -7.3
                 LBC Threshold(mA)              10.00       2.00         10.00         2.00
                 Temp. Threshold(celsius)       75.00      -5.00         70.00         0.00
                 Voltage Threshold(volt)         3.63       2.97          3.46         3.13

                 Polarization parameters not supported by optics

                 Temperature = 35.00 Celsius 
                 Voltage = 3.26 V 

         Transceiver Vendor Details

                 Form Factor            : SFP+
                 Optics type            : SFP+ 10G SR
                 Name                   : CISCO-AVAGO
                 OUI Number             : 00.17.6a
                 Part Number            : SFBR-7702SDZ-CS5
                 Rev Number             : G2.5
                 Serial Number          : AGD162040SP
                 PID                    : SFP-10G-SR
                 VID                    : V03
                 Date Code(yy/mm/dd)    : 12/05/20
    '''}

    golden_parsed_output2 = {
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

    golden_output2 = {'execute.return_value': '''
        #show controllers optics 0/0/1/2
        Sat Aug  3 03:11:51.141 EST

         Controller State: Up 
         Transport Admin State: In Service 
         Laser State: On 
         LED State: Green 
         Optics Status 
                 Optics Type:  CFP2 DWDM
                 DWDM carrier Info: C BAND, MSA ITU Channel=97, Frequency=191.30THz,
                 Wavelength=1567.133nm 

                 Alarm Status:
                 -------------
                 Detected Alarms: None


                 LOS/LOL/Fault Status:

                 Alarm Statistics:

                 -------------
                 HIGH-RX-PWR = 0            LOW-RX-PWR = 1          
                 HIGH-TX-PWR = 0            LOW-TX-PWR = 1          
                 HIGH-LBC = 0               HIGH-DGD = 0          
                 OOR-CD = 0                 OSNR = 0          
                 WVL-OOL = 0                MEA  = 0          
                 IMPROPER-REM = 0          
                 TX-POWER-PROV-MISMATCH = 0          
                 Laser Bias Current = 0.0 %
                 Actual TX Power = 0.99 dBm 
                 RX Power = -20.50 dBm 

                 Performance Monitoring: Enable 

                 THRESHOLD VALUES
                 ----------------

                 Parameter                 High Alarm  Low Alarm  High Warning  Low Warning
                 ------------------------  ----------  ---------  ------------  -----------
                 Rx Power Threshold(dBm)          1.5      -30.0           0.0          0.0
                 Tx Power Threshold(dBm)          3.5      -10.0           0.0          0.0
                 LBC Threshold(mA)                N/A        N/A          0.00         0.00

                 LBC High Threshold = 98 % 
                 Configured Tx Power = 1.00 dBm 
                 Configured OSNR lower Threshold = 0.00 dB 
                 Configured DGD Higher Threshold = 180.00 ps 
                 Chromatic Dispersion 5 ps/nm 
                 Configured CD-MIN -10000 ps/nm  CD-MAX 16000 ps/nm 
                 Optical Signal to Noise Ratio = 27.00 dB 
                 Polarization Dependent Loss = 0.00 dB 
                 Differential Group Delay = 2.00 ps 
                  
         Transceiver Vendor Details
                  
                 Form Factor            : CFP2
                 Name                   : CISCO-ACACIA    
                 Part Number            : AC200-D23-190   
                 Rev Number             : 16672
                 Serial Number          : 180653009       
                 PID                    : ONS-C2-WDM-DE-1HL 
                 VID                    : VES#
                 Date Code(yy/mm/dd)    : 18/02/03
    '''}

    golden_parsed_output3 = {
        "0/0/0/20": {
            "name": "Optics 0/0/0/20",
            "controller_state": "Down",
            "transport_admin_state": "In Service",
            "laser_state": "Off",
            "optics_status": {
                "optics_type": "Unavailable",
                "dwdm_carrier_info": "Unavailable",
                "msa_itu_channel": "Unavailable",
                "frequency": "Unavailable",
                "wavelength": "Unavailable",
                "actual_tx_power": "Unavailable",
                "rx_power": "Unavailable"
            }
        }
    }

    golden_output3 = {'execute.return_value': '''
        #show controllers optics 0/0/0/20
        Sat Aug  3 03:15:25.076 EST

         Controller State: Down 
         Transport Admin State: In Service 
         Laser State: Off 
                 Optics not present
                 Optics Type: Unavailable
                 DWDM Carrier Info: Unavailable, MSA ITU Channel= Unavailable, Frequency= Unavailable , Wavelength= Unavailable 
                 TX Power = Unavailable 
                 RX Power = Unavailable 
    '''}

    golden_parsed_output4 = {
        "0/0/0/18": {
            "name": "Optics 0/0/0/18",
            "controller_state": "Up",
            "transport_admin_state": "In Service",
            "laser_state": "Off",
            "led_state": "Off",
            "optics_status": {
                "optics_type": "SFP+ 10G SR",
                "wavelength": "850.00 nm",
                "alarm_status": {
                    "detected_alarms": [
                        "LOW-RX1-PWR",
                        "LOW-TX1-PWR",
                        "LOW-TX1_LBC"
                    ]
                },
                "los_lol_fault_status": {
                    "detected_los_lol_fault": [
                        "RX-LOS"
                    ]
                },
                "laser_bias_current": "0.0 mA",
                "actual_tx_power": "-17.25 dBm",
                "rx_power": "-40.00 dBm",
                "performance_monitoring": "Enable",
                "threshold_values": {
                    "Rx Power Threshold(dBm)": {
                        "parameter": "Rx Power Threshold(dBm)",
                        "high_alarm": "2.0",
                        "low_alarm": "-13.9",
                        "high_warning": "-1.0",
                        "low_warning": "-9.9"
                    },
                    "Tx Power Threshold(dBm)": {
                        "parameter": "Tx Power Threshold(dBm)",
                        "high_alarm": "1.6",
                        "low_alarm": "-11.3",
                        "high_warning": "-1.3",
                        "low_warning": "-7.3"
                    },
                    "LBC Threshold(mA)": {
                        "parameter": "LBC Threshold(mA)",
                        "high_alarm": "11.00",
                        "low_alarm": "4.00",
                        "high_warning": "10.00",
                        "low_warning": "5.00"
                    },
                    "Temp. Threshold(celsius)": {
                        "parameter": "Temp. Threshold(celsius)",
                        "high_alarm": "75.00",
                        "low_alarm": "-5.00",
                        "high_warning": "70.00",
                        "low_warning": "0.00"
                    },
                    "Voltage Threshold(volt)": {
                        "parameter": "Voltage Threshold(volt)",
                        "high_alarm": "3.63",
                        "low_alarm": "2.97",
                        "high_warning": "3.46",
                        "low_warning": "3.13"
                    }
                },
                "polarization_parameters": "not supported by optics",
                "temperature": "31.00 Celsius",
                "voltage": "3.30 V"
            },
            "transceiver_vendor_details": {
                "form_factor": "SFP+",
                "optics_type": "SFP+ 10G SR",
                "name": "CISCO-FINISAR",
                "oui_number": "00.90.65",
                "part_number": "FTLX8571D3BCL-C2",
                "rev_number": "A",
                "serial_number": "FNS210108H7",
                "pid": "SFP-10G-SR",
                "vid": "V03",
                "date_code": "17/01/03"
            }
        }
    }

    golden_output4 = {'execute.return_value': '''
        #show controllers optics 0/0/0/18
        Sat Aug  3 03:19:06.519 EST

         Controller State: Up 
         Transport Admin State: In Service 
         Laser State: Off 
         LED State: Off 
         Optics Status 
                 Optics Type:  SFP+ 10G SR
                 Wavelength = 850.00 nm 

                 Alarm Status:
                 -------------
                 Detected Alarms: 
                         LOW-RX1-PWR   
                         LOW-TX1-PWR   
                         LOW-TX1_LBC   

                 LOS/LOL/Fault Status:
                 Detected LOS/LOL/FAULT: RX-LOS   


                 Laser Bias Current = 0.0 mA
                 Actual TX Power = -17.25 dBm 
                 RX Power = -40.00 dBm 

                 Performance Monitoring: Enable 

                 THRESHOLD VALUES
                 ----------------

                 Parameter                 High Alarm  Low Alarm  High Warning  Low Warning
                 ------------------------  ----------  ---------  ------------  -----------
                 Rx Power Threshold(dBm)          2.0      -13.9          -1.0         -9.9
                 Tx Power Threshold(dBm)          1.6      -11.3          -1.3         -7.3
                 LBC Threshold(mA)              11.00       4.00         10.00         5.00
                 Temp. Threshold(celsius)       75.00      -5.00         70.00         0.00
                 Voltage Threshold(volt)         3.63       2.97          3.46         3.13

                 Polarization parameters not supported by optics

                 Temperature = 31.00 Celsius 
                 Voltage = 3.30 V 

         Transceiver Vendor Details

                 Form Factor            : SFP+
                 Optics type            : SFP+ 10G SR
                 Name                   : CISCO-FINISAR
                 OUI Number             : 00.90.65
                 Part Number            : FTLX8571D3BCL-C2
                 Rev Number             : A
                 Serial Number          : FNS210108H7
                 PID                    : SFP-10G-SR
                 VID                    : V03
                 Date Code(yy/mm/dd)    : 17/01/03 
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowControllersOptics(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(port='0/0/0/0')

    def test_golden1(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowControllersOptics(device=self.device)
        parsed_output = obj.parse(port='0/0/0/0')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_golden2(self):
        self.device = Mock(**self.golden_output2)
        obj = ShowControllersOptics(device=self.device)
        parsed_output = obj.parse(port='0/0/1/2')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_golden3(self):
        self.device = Mock(**self.golden_output3)
        obj = ShowControllersOptics(device=self.device)
        parsed_output = obj.parse(port='0/0/0/20')
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_golden4(self):
        self.device = Mock(**self.golden_output4)
        obj = ShowControllersOptics(device=self.device)
        parsed_output = obj.parse(port='0/0/0/18')
        self.assertEqual(parsed_output, self.golden_parsed_output4)


# ==============================================================================================
#  Unit test for 'show controllers fia diagshell {diagshell_unit} "l2 show" location {location}'
# ==============================================================================================
class test_show_controllers_fia_diagshell_location(unittest.TestCase):
    '''Unit test for:
        * 'show controllers fia diagshell {diagshell_unit} "l2 show" location {location}'
    '''

    maxDiff = None
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'nodes': 
            {'0/0/CPU0': 
                {'vlan': 
                    {4: 
                        {'mac': 
                            {'00:00:03:00:01:0c': 
                                {'encap_id': '0x301d',
                                'gport': '0xc000001',
                                'trunk': 1}}},
                    2522: 
                        {'mac': 
                            {'fc:00:00:01:00:02': 
                                {'encap_id': '0xffffffff',
                                'gport': '0x9800401d',
                                'static': True}}},
                    2524: 
                        {'mac': 
                            {'fc:00:00:01:00:0b': 
                                {'encap_id': '0x3001',
                                'gport': '0xc000000',
                                'static': True,
                                'trunk': 0}}},
                    2544: 
                        {'mac': 
                            {'fc:00:00:01:00:8b': 
                                {'encap_id': '0x2007',
                                'gport': '0x8000048'},
                            'fc:00:00:01:00:9b': 
                                {'encap_id': '0x2007',
                                'gport': '0x8000048',
                                'trunk': 0}}}}}}}

    golden_output1 = {'execute.return_value': '''
        RP/0/RP0/CPU0:UUT4#show controller fia diagshell 0 'l2 show' location all

        Node ID: 0/0/CPU0
        mac=fc:00:00:01:00:8b vlan=2544 GPORT=0x8000048 encap_id=0x2007
        mac=fc:00:00:01:00:02 vlan=2522 GPORT=0x9800401d Static encap_id=0xffffffff
        mac=fc:00:00:01:00:9b vlan=2544 GPORT=0x8000048 Trunk=0 encap_id=0x2007
        mac=fc:00:00:01:00:0b vlan=2524 GPORT=0xc000000 Trunk=0 Static encap_id=0x3001
        mac=00:00:03:00:01:0c vlan=4 GPORT=0xc000001 Trunk=1 encap_id=0x301d
        '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowControllersFiaDiagshellL2showLocation(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden1(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowControllersFiaDiagshellL2showLocation(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)


if __name__ == '__main__':
    unittest.main()
