#!/bin/env python
import unittest
from unittest.mock import Mock
from ats.topology import Device

from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

from genie.libs.parser.iosxe.cat4k.show_platform import ShowModule as ShowModulecat4k


class test_show_module_c4507(unittest.TestCase):
    dev1 = Device(name='empty')
    dev_cat4k = Device(name='c4507')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output_c4507 = {
        'chassis_type': 'WS-C4507R+E',
        'power_consumed': '40 Watts',
        'mod': {
            1: {
                'card_type': '10/100/1000BaseT Premium POE E Series',
                'hw_ver': '3.1',
                'mac_address_from': '11a1.b222.cc33',
                'mac_address_to': '11a1.b222.cc3f',
                'model': 'WS-X4648-RJ45V+E',
                'port': 48,
                'serial_number': 'ABCDE123456',
                'status': 'Ok'
            },
            3: {
                'card_type': 'Sup 7L-E 10GE (SFP+), 1000BaseX (SFP)',
                'fw_ver': '15.0(1r)SG10',
                'hw_ver': '3.0',
                'mac_address_from': '555a.888b.ccc0',
                'mac_address_to': '555a.888b.cccd',
                'model': 'WS-X45-SUP7L-E',
                'operating_mode': 'RPR',
                'port': 6,
                'redundancy_role': 'Active Supervisor',
                'redundancy_status': 'Active',
                'serial_number': 'QWERT987654',
                'status': 'Ok',
                'sw_ver': '03.06.07.E'
            },
            6: {
                'card_type': '10/100/1000BaseT Premium POE E Series',
                'hw_ver': '3.1',
                'mac_address_from': '00a0.bb11.ff3b',
                'mac_address_to': '00a0.bb11.ff3f',
                'model': 'WS-X4648-RJ45V+E',
                'port': 48,
                'serial_number': 'CDEFGH12345',
                'status': 'Ok'
            },
            7: {
                'card_type': '10/100/1000BaseT Premium POE E Series',
                'hw_ver': '3.1',
                'mac_address_from': 'b888.11aa.22dd',
                'mac_address_to': 'b888.11aa.22df',
                'model': 'WS-X4648-RJ45V+E',
                'port': 48,
                'serial_number': 'ASDFGH56789',
                'status': 'Ok'
            }
        },
        'system_failures': {
            'power_supply': "bad/off (see 'show power')"
        }
    }

    golden_output_c4507 = {'execute.return_value': '''\
        Chassis Type : WS-C4507R+E

        Power consumed by backplane : 40 Watts

        Mod Ports Card Type                              Model              Serial No.
        ---+-----+--------------------------------------+------------------+-----------
         1    48  10/100/1000BaseT Premium POE E Series  WS-X4648-RJ45V+E   ABCDE123456
         3     6  Sup 7L-E 10GE (SFP+), 1000BaseX (SFP)  WS-X45-SUP7L-E     QWERT987654
         6    48  10/100/1000BaseT Premium POE E Series  WS-X4648-RJ45V+E   CDEFGH12345
         7    48  10/100/1000BaseT Premium POE E Series  WS-X4648-RJ45V+E   ASDFGH56789

         M MAC addresses                    Hw  Fw           Sw               Status
        --+--------------------------------+---+------------+----------------+---------
         1 11a1.b222.cc33 to 11a1.b222.cc3f 3.1                               Ok
         3 555a.888b.ccc0 to 555a.888b.cccd 3.0 15.0(1r)SG10 03.06.07.E       Ok
         6 00a0.bb11.ff3b to 00a0.bb11.ff3f 3.1                               Ok
         7 b888.11aa.22dd to b888.11aa.22df 3.1                               Ok

        Mod  Redundancy role     Operating mode      Redundancy status
        ----+-------------------+-------------------+----------------------------------
         3   Active Supervisor   RPR                 Active

        System Failures:
        ----------------
        Power Supply:   bad/off (see 'show power')
    '''
    }

    def test_empty(self):
        self.dev1 = Mock(**self.empty_output)
        platform_obj = ShowModulecat4k(device=self.dev1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = platform_obj.parse()    

    def test_golden(self):
        self.maxDiff = None
        self.dev_cat4k = Mock(**self.golden_output_c4507)
        platform_obj = ShowModulecat4k(device=self.dev_cat4k)
        parsed_output = platform_obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_c4507)

if __name__ == '__main__':
    unittest.main()