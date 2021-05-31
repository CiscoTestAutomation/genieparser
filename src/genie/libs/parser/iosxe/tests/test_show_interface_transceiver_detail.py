import unittest
from unittest.mock import Mock
# from ats.topology import Device
# from ats.topology import loader
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError
from genie.libs.parser.iosxe.show_interface import ShowInterfaceTransceiverDetail


class test_show_interface_transceiver_detail(unittest.TestCase):
    '''Unit test for "show lisp session"'''

    empty_output = {'execute.return_value': ''}
    golden_parsed_output1 = {
        "interfaces": {
            "TwentyFiveGigE2/1/1": {
                "transceiver": "internally calibrated.",
                "Temperature": {
                    "Value": 25.5,
                    "HighAlarmThreshold": 90.0,
                    "HighWarnThreshold": 85.0,
                    "LowWarnThreshold": -5.0,
                    "LowAlarmThreshold": -10.0
                },
                "Voltage": {
                    "Value": 3.27,
                    "HighAlarmThreshold": 3.6,
                    "HighWarnThreshold": 3.5,
                    "LowWarnThreshold": 3.05,
                    "LowAlarmThreshold": 3.0
                },
                "Current": {
                    "Value": 5.7,
                    "Lane": "N/A",
                    "HighAlarmThreshold": 50.0,
                    "HighWarnThreshold": 40.0,
                    "LowWarnThreshold": 2.0,
                    "LowAlarmThreshold": 1.0
                },
                "OpticalTX": {
                    "Value": -2.7,
                    "Lane": "N/A",
                    "HighAlarmThreshold": 1.0,
                    "HighWarnThreshold": 0.0,
                    "LowWarnThreshold": -8.3,
                    "LowAlarmThreshold": -9.3
                },
                "OpticalRX": {
                    "Value": -3.5,
                    "Lane": "N/A",
                    "HighAlarmThreshold": 1.0,
                    "HighWarnThreshold": 0.0,
                    "LowWarnThreshold": -12.1,
                    "LowAlarmThreshold": -13.1
                }
            }
        }
    }

    golden_output1 = {'execute.return_value': '''
    # show interface TwentyFiveGigE1/0/1 transceiver detail
    
    ITU Channel not available (Wavelength not available),
    Transceiver is internally calibrated.
    mA: milliamperes, dBm: decibels (milliwatts), NA or N/A: not applicable.
    ++ : high alarm, +  : high warning, -  : low warning, -- : low alarm.
    A2D readouts (if they differ), are reported in parentheses.
    The threshold values are calibrated.
    
                                    High Alarm  High Warn  Low Warn   Low Alarm
                 Temperature        Threshold   Threshold  Threshold  Threshold
    Port         (Celsius)          (Celsius)   (Celsius)  (Celsius)  (Celsius)
    ---------    -----------------  ----------  ---------  ---------  ---------
    Twe2/1/1     25.5                   90.0       85.0       -5.0      -10.0
    
                                    High Alarm  High Warn  Low Warn   Low Alarm
                 Voltage            Threshold   Threshold  Threshold  Threshold
    Port         (Volts)            (Volts)     (Volts)    (Volts)    (Volts)
    ---------    -----------------  ----------  ---------  ---------  ---------
    Twe2/1/1     3.27                   3.60       3.50       3.05       3.00
    
                                      High Alarm  High Warn  Low Warn   Low Alarm
                     Current          Threshold   Threshold  Threshold  Threshold
    Port       Lane  (milliamperes)   (mA)        (mA)       (mA)       (mA)
    ---------  ----  ---------------  ----------  ---------  ---------  ---------
    Twe2/1/1   N/A    5.7                 50.0       40.0        2.0        1.0
    
                     Optical          High Alarm  High Warn  Low Warn   Low Alarm
                     Transmit Power   Threshold   Threshold  Threshold  Threshold
    Port       Lane  (dBm)            (dBm)       (dBm)      (dBm)      (dBm)
    ---------  ----  ---------------  ----------  ---------  ---------  ---------
    Twe2/1/1   N/A   -2.7                  1.0        0.0       -8.3       -9.3
    
                     Optical          High Alarm  High Warn  Low Warn   Low Alarm
                     Receive Power    Threshold   Threshold  Threshold  Threshold
    Port       Lane  (dBm)            (dBm)       (dBm)      (dBm)      (dBm)
    ---------  ----  ---------------  ----------  ---------  ---------  ---------
    Twe2/1/1   N/A   -3.5                  1.0        0.0      -12.1      -13.1
     '''}

    def test_show_interface_transceiver_detail_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowInterfaceTransceiverDetail(device=self.device)
        parsed_output = obj.parse(interface='TwentyFiveGigE2/1/1')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_interface_transceiver_detail_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowInterfaceTransceiverDetail(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(interface='TwentyFiveGigE1/0/1')


if __name__ == '__main__':
    unittest.main()
