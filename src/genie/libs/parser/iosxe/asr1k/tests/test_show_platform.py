#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                       SchemaMissingKeyError

from genie.libs.parser.iosxe.asr1k.show_platform import ShowEnvironmentAll as ShowEnvironmentAllasr1k


class test_show_env_asr1k(unittest.TestCase):

    dev = Device(name='asr1k')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {'day': '2',
         'load': {'five_min': '0%', 'five_secs': '0%/0%', 'one_min': '1%'},
         'month': 'Nov',
         'sensor': {'PEM Iout': {'location': 'P1',
                                 'reading': '0 A',
                                 'sensor_name': 'PEM Iout',
                                 'state': 'Normal'},
                    'PEM Vin': {'location': 'P1',
                                'reading': '104 V AC',
                                'sensor_name': 'PEM Vin',
                                'state': 'Normal'},
                    'PEM Vout': {'location': 'P1',
                                 'reading': '0 V DC',
                                 'sensor_name': 'PEM Vout',
                                 'state': 'Normal'},
                    'Temp: Asic1': {'location': '0',
                                    'reading': '41 Celsius',
                                    'sensor_name': 'Temp: Asic1',
                                    'state': 'Normal'},
                    'Temp: C2D C0': {'location': 'R0',
                                     'reading': '38 Celsius',
                                     'sensor_name': 'Temp: C2D C0',
                                     'state': 'Normal'},
                    'Temp: C2D C1': {'location': 'R0',
                                     'reading': '34 Celsius',
                                     'sensor_name': 'Temp: C2D C1',
                                     'state': 'Normal'},
                    'Temp: CPP Rear': {'location': 'F0',
                                       'reading': '54 Celsius',
                                       'sensor_name': 'Temp: CPP Rear',
                                       'state': 'Normal'},
                    'Temp: CPU AIR': {'location': 'R0',
                                      'reading': '31 Celsius',
                                      'sensor_name': 'Temp: CPU AIR',
                                      'state': 'Normal'},
                    'Temp: Center': {'location': '0',
                                     'reading': '34 Celsius',
                                     'sensor_name': 'Temp: Center',
                                     'state': 'Normal'},
                    'Temp: FC': {'location': 'P1',
                                 'reading': '27 Celsius',
                                 'sensor_name': 'Temp: FC',
                                 'state': 'Fan Speed 65%'},
                    'Temp: HKP Die': {'location': 'F0',
                                      'reading': '51 Celsius',
                                      'sensor_name': 'Temp: HKP Die',
                                      'state': 'Normal'},
                    'Temp: Inlet': {'location': 'R0',
                                    'reading': '27 Celsius',
                                    'sensor_name': 'Temp: Inlet',
                                    'state': 'Normal'},
                    'Temp: Left': {'location': '0',
                                   'reading': '29 Celsius',
                                   'sensor_name': 'Temp: Left',
                                   'state': 'Normal'},
                    'Temp: Left Ext': {'location': 'F0',
                                       'reading': '39 Celsius',
                                       'sensor_name': 'Temp: Left Ext',
                                       'state': 'Normal'},
                    'Temp: MCH AIR': {'location': 'R0',
                                      'reading': '39 Celsius',
                                      'sensor_name': 'Temp: MCH AIR',
                                      'state': 'Normal'},
                    'Temp: MCH DIE': {'location': 'R0',
                                      'reading': '52 Celsius',
                                      'sensor_name': 'Temp: MCH DIE',
                                      'state': 'Normal'},
                    'Temp: MCH Die': {'location': 'F0',
                                      'reading': '60 Celsius',
                                      'sensor_name': 'Temp: MCH Die',
                                      'state': 'Normal'},
                    'Temp: Olv Die': {'location': 'F0',
                                      'reading': '49 Celsius',
                                      'sensor_name': 'Temp: Olv Die',
                                      'state': 'Normal'},
                    'Temp: Outlet': {'location': 'R0',
                                     'reading': '29 Celsius',
                                     'sensor_name': 'Temp: Outlet',
                                     'state': 'Normal'},
                    'Temp: PEM': {'location': 'P1',
                                  'reading': '26 Celsius',
                                  'sensor_name': 'Temp: PEM',
                                  'state': 'Normal'},
                    'Temp: Pop Die': {'location': 'F0',
                                      'reading': '56 Celsius',
                                      'sensor_name': 'Temp: Pop Die',
                                      'state': 'Normal'},
                    'Temp: Rght Ext': {'location': 'F0',
                                       'reading': '39 Celsius',
                                       'sensor_name': 'Temp: Rght Ext',
                                       'state': 'Normal'},
                    'Temp: Right': {'location': '0',
                                    'reading': '33 Celsius',
                                    'sensor_name': 'Temp: Right',
                                    'state': 'Normal'},
                    'Temp: SCBY AIR': {'location': 'R0',
                                       'reading': '39 Celsius',
                                       'sensor_name': 'Temp: SCBY AIR',
                                       'state': 'Normal'},
                    'V1: 12v': {'location': 'R0',
                                'reading': '11821 mV',
                                'sensor_name': 'V1: 12v',
                                'state': 'Normal'},
                    'V1: GP1': {'location': 'R0',
                                'reading': '913 mV',
                                'sensor_name': 'V1: GP1',
                                'state': 'Normal'},
                    'V1: GP2': {'location': 'R0',
                                'reading': '1191 mV',
                                'sensor_name': 'V1: GP2',
                                'state': 'Normal'},
                    'V1: VDD': {'location': 'R0',
                                'reading': '3281 mV',
                                'sensor_name': 'V1: VDD',
                                'state': 'Normal'},
                    'V1: VMA': {'location': 'R0',
                                'reading': '1201 mV',
                                'sensor_name': 'V1: VMA',
                                'state': 'Normal'},
                    'V1: VMB': {'location': 'R0',
                                'reading': '2504 mV',
                                'sensor_name': 'V1: VMB',
                                'state': 'Normal'},
                    'V1: VMC': {'location': 'R0',
                                'reading': '3295 mV',
                                'sensor_name': 'V1: VMC',
                                'state': 'Normal'},
                    'V1: VMD': {'location': 'R0',
                                'reading': '2500 mV',
                                'sensor_name': 'V1: VMD',
                                'state': 'Normal'},
                    'V1: VME': {'location': 'R0',
                                'reading': '1801 mV',
                                'sensor_name': 'V1: VME',
                                'state': 'Normal'},
                    'V1: VMF': {'location': 'R0',
                                'reading': '1533 mV',
                                'sensor_name': 'V1: VMF',
                                'state': 'Normal'},
                    'V2: 12v': {'location': 'R0',
                                'reading': '11821 mV',
                                'sensor_name': 'V2: 12v',
                                'state': 'Normal'},
                    'V2: GP1': {'location': 'R0',
                                'reading': '2497 mV',
                                'sensor_name': 'V2: GP1',
                                'state': 'Normal'},
                    'V2: GP2': {'location': 'R0',
                                'reading': '1186 mV',
                                'sensor_name': 'V2: GP2',
                                'state': 'Normal'},
                    'V2: VDD': {'location': 'R0',
                                'reading': '3276 mV',
                                'sensor_name': 'V2: VDD',
                                'state': 'Normal'},
                    'V2: VMA': {'location': 'R0',
                                'reading': '1054 mV',
                                'sensor_name': 'V2: VMA',
                                'state': 'Normal'},
                    'V2: VMB': {'location': 'R0',
                                'reading': '1098 mV',
                                'sensor_name': 'V2: VMB',
                                'state': 'Normal'},
                    'V2: VMC': {'location': 'R0',
                                'reading': '1059 mV',
                                'sensor_name': 'V2: VMC',
                                'state': 'Normal'},
                    'V2: VMD': {'location': 'R0',
                                'reading': '991 mV',
                                'sensor_name': 'V2: VMD',
                                'state': 'Normal'},
                    'V2: VME': {'location': 'R0',
                                'reading': '1103 mV',
                                'sensor_name': 'V2: VME',
                                'state': 'Normal'},
                    'V2: VMF': {'location': 'R0',
                                'reading': '1005 mV',
                                'sensor_name': 'V2: VMF',
                                'state': 'Normal'},
                    'V3: 12v': {'location': 'F0',
                                'reading': '11806 mV',
                                'sensor_name': 'V3: 12v',
                                'state': 'Normal'},
                    'V3: VDD': {'location': 'F0',
                                'reading': '3286 mV',
                                'sensor_name': 'V3: VDD',
                                'state': 'Normal'},
                    'V3: VMA': {'location': 'F0',
                                'reading': '3291 mV',
                                'sensor_name': 'V3: VMA',
                                'state': 'Normal'},
                    'V3: VMB': {'location': 'F0',
                                'reading': '2495 mV',
                                'sensor_name': 'V3: VMB',
                                'state': 'Normal'},
                    'V3: VMC': {'location': 'F0',
                                'reading': '1499 mV',
                                'sensor_name': 'V3: VMC',
                                'state': 'Normal'},
                    'V3: VMD': {'location': 'F0',
                                'reading': '1000 mV',
                                'sensor_name': 'V3: VMD',
                                'state': 'Normal'}},
         'sensor_list': 'Environmental Monitoring',
         'source': 'NTP',
         'time': '16:53:30.232',
         'week_day': 'Wed',
         'year': '2016',
         'zone': 'JST'}

    golden_output = {'execute.return_value': '''\
        ------------------ show environment all ------------------

        Load for five secs: 0%/0%; one minute: 1%; five minutes: 0%
        Time source is NTP, 16:53:30.232 JST Wed Nov 2 2016

        Sensor List:  Environmental Monitoring 
         Sensor           Location          State             Reading
         V1: VMA          0                 Normal            1098 mV
         V1: VMB          0                 Normal            1201 mV
         V1: VMC          0                 Normal            1499 mV
         V1: VMD          0                 Normal            1801 mV
         V1: VME          0                 Normal            2495 mV
         V1: VMF          0                 Normal            3295 mV
         V1: 12v          0                 Normal            11879 mV
         V1: VDD          0                 Normal            3281 mV
         V1: GP1          0                 Normal            749 mV
         V1: GP2          0                 Normal            903 mV
         V2: VMB          0                 Normal            996 mV
         V2: VME          0                 Normal            751 mV
         V2: VMF          0                 Normal            751 mV
         V2: 12v          0                 Normal            11879 mV
         V2: VDD          0                 Normal            3276 mV
         V2: GP2          0                 Normal            749 mV
         Temp: Left       0                 Normal            29 Celsius
         Temp: Center     0                 Normal            34 Celsius
         Temp: Asic1      0                 Normal            41 Celsius
         Temp: Right      0                 Normal            33 Celsius
         V1: VMA          F0                Normal            1801 mV
         V1: VMB          F0                Normal            1201 mV
         V1: VMC          F0                Normal            1000 mV
         V1: VMD          F0                Normal            1054 mV
         V1: VME          F0                Normal            1010 mV
         V1: VMF          F0                Normal            1098 mV
         V1: 12v          F0                Normal            11850 mV
         V1: VDD          F0                Normal            3286 mV
         V1: GP1          F0                Normal            920 mV
         V1: GP2          F0                Normal            769 mV
         V2: VMA          F0                Normal            3291 mV
         V2: VMB          F0                Normal            2495 mV
         V2: VMC          F0                Normal            1499 mV
         V2: VMD          F0                Normal            1196 mV
         V2: VME          F0                Normal            1098 mV
         V2: VMF          F0                Normal            1000 mV
         V2: 12v          F0                Normal            11777 mV
         V2: VDD          F0                Normal            3281 mV
         V2: GP1          F0                Normal            771 mV
         V2: GP2          F0                Normal            1101 mV
         Temp: Inlet      F0                Normal            37 Celsius
         Temp: Pop Die    F0                Normal            56 Celsius
         Temp: Left Ext   F0                Normal            39 Celsius
         Temp: HKP Die    F0                Normal            51 Celsius
         Temp: CPP Rear   F0                Normal            54 Celsius
         Temp: Olv Die    F0                Normal            49 Celsius
         Temp: Rght Ext   F0                Normal            39 Celsius
         Temp: MCH Die    F0                Normal            60 Celsius
         V3: VMA          F0                Normal            3291 mV
         V3: VMB          F0                Normal            2495 mV
         V3: VMC          F0                Normal            1499 mV
         V3: VMD          F0                Normal            1000 mV
         V3: 12v          F0                Normal            11806 mV
         V3: VDD          F0                Normal            3286 mV
         PEM Iout         P0                Normal            29 A
         PEM Vout         P0                Normal            12 V DC
         PEM Vin          P0                Normal            101 V AC
         Temp: PEM        P0                Normal            28 Celsius
         Temp: FC         P0                Fan Speed 65%     27 Celsius
         PEM Iout         P1                Normal            0 A
         PEM Vout         P1                Normal            0 V DC
         PEM Vin          P1                Normal            104 V AC
         Temp: PEM        P1                Normal            26 Celsius
         Temp: FC         P1                Fan Speed 65%     27 Celsius
         V1: VMA          R0                Normal            1201 mV
         V1: VMB          R0                Normal            2504 mV
         V1: VMC          R0                Normal            3295 mV
         V1: VMD          R0                Normal            2500 mV
         V1: VME          R0                Normal            1801 mV
         V1: VMF          R0                Normal            1533 mV
         V1: 12v          R0                Normal            11821 mV
         V1: VDD          R0                Normal            3281 mV
         V1: GP1          R0                Normal            913 mV
         V1: GP2          R0                Normal            1191 mV
         V2: VMA          R0                Normal            1054 mV
         V2: VMB          R0                Normal            1098 mV
         V2: VMC          R0                Normal            1059 mV
         V2: VMD          R0                Normal            991 mV
         V2: VME          R0                Normal            1103 mV
         V2: VMF          R0                Normal            1005 mV
         V2: 12v          R0                Normal            11821 mV
         V2: VDD          R0                Normal            3276 mV
         V2: GP1          R0                Normal            2497 mV
         V2: GP2          R0                Normal            1186 mV
         Temp: Outlet     R0                Normal            29 Celsius
         Temp: CPU AIR    R0                Normal            31 Celsius
         Temp: Inlet      R0                Normal            27 Celsius
         Temp: SCBY AIR   R0                Normal            39 Celsius
         Temp: MCH DIE    R0                Normal            52 Celsius
         Temp: MCH AIR    R0                Normal            39 Celsius
         Temp: C2D C0     R0                Normal            38 Celsius
         Temp: C2D C1     R0                Normal            34 Celsius
    '''
    }

    golden_parsed_output_1 = {'sensor': {'Temp: FC PWM1': {'location': 'P6',
                              'reading': '25 Celsius',
                              'sensor_name': 'Temp: FC PWM1',
                              'state': 'Fan Speed 45%'}}}

    golden_output_1 = {'execute.return_value': '''\
        Router#### FAN 7 OUT ###show env all | in P6 | P7
         Temp1            P6                Normal            40 Celsius
         Temp: FC PWM1    P6                Fan Speed 45%     25 Celsius
    '''
    }

    def test_empty(self):
        self.dev = Mock(**self.empty_output)
        obj = ShowEnvironmentAllasr1k(device=self.dev)
        with self.assertRaises(SchemaEmptyParserError):
            parsered_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output)
        obj = ShowEnvironmentAllasr1k(device=self.dev)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_1(self):
        self.maxDiff = None
        self.dev = Mock(**self.golden_output_1)
        obj = ShowEnvironmentAllasr1k(device=self.dev)
        parsed_output = obj.parse(key_word='P6 | P7')
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

if __name__ == '__main__':
    unittest.main()
