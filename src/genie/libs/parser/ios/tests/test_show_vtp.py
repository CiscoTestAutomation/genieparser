# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError
# Parser
from genie.libs.parser.ios.show_vtp import ShowVtpStatus


# ============================================
# unit test for 'show vtp status'
# ============================================
class test_show_vtp_status(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "vtp": {
            "conf_last_modified_by": "0.0.0.0",
            "conf_last_modified_time": "8-12-99 15:04:49",
            "configuration_revision": 247,
            "domain_name": "Lab_Network",
            "enabled": True,
            "existing_vlans": 33,
            "maximum_vlans": 1005,
            "md5_digest": "0x45 0x49 0x52 0x63 0x80 0xB6 0xC8 0xFD",
            "operating_mode": "client",
            "pruning_mode": True,
            "traps_generation": False,
            "version": "2"
        }
    }

    golden_output = {'execute.return_value': '''\
        Router# show vtp status 

         VTP Version                     : 2
         Configuration Revision          : 247
         Maximum VLANs supported locally : 1005
         Number of existing VLANs        : 33
         VTP Operating Mode              : Client
         VTP Domain Name                 : Lab_Network
         VTP Pruning Mode                : Enabled
         VTP V2 Mode                     : Disabled
         VTP Traps Generation            : Disabled
         MD5 digest                      : 0x45 0x52 0xB6 0xFD 0x63 0xC8 0x49 0x80
         Configuration last modified by 0.0.0.0 at 8-12-99 15:04:49
    '''}

    golden_parsed_output_3 = {
        'vtp': {
            'device_id': '3820.5622.a580',
            'feature': {
                'mst': {
                    'configuration_revision': 0,
                    'enabled': True,
                    'operating_mode': 'server',
                    'primary_id': '0000.0000.0000',
                },
                'unknown': {
                    'enabled': False,
                    'operating_mode': 'transparent',
                },
                'vlan': {
                    'configuration_revision': 2,
                    'enabled': True,
                    'existing_extended_vlans': 0,
                    'existing_vlans': 100,
                    'maximum_vlans': 4096,
                    'md5_digest': '0x15 0x17 0x1A 0x1C 0x25 0x2C ' \
                                  '0x3C 0x48 0x6B 0x70 0x7D 0x87 ' \
                                  '0x92 0xC2 0xC7 0xFC',
                    'operating_mode': 'primary server',
                    'primary_description': 'SW1',
                    'primary_id': '3820.5622.a580',
                },
            },

            'pruning_mode': False,
            'traps_generation': False,
            'version': '3',
            'version_capable': [1, 2, 3]
        }
    }

    golden_output_3 = {'execute.return_value': '''\
        VTP Version capable             : 1 to 3
        VTP version running             : 3
        VTP Domain Name                 : 
        VTP Pruning Mode                : Disabled
        VTP Traps Generation            : Disabled
        Device ID                       : 3820.5622.a580

        Feature VLAN:
        --------------
        VTP Operating Mode                : Primary Server
        Number of existing VLANs          : 100
        Number of existing extended VLANs : 0
        Maximum VLANs supported locally   : 4096
        Configuration Revision            : 2
        Primary ID                        : 3820.5622.a580
        Primary Description               : SW1
        MD5 digest                        : 0xC2 0x3C 0x1A 0x2C 0x1C 0x48 0x7D 0xFC 
                                            0x6B 0x17 0x15 0x87 0x92 0xC7 0x70 0x25 


        Feature MST:
        --------------
        VTP Operating Mode                : Server
        Configuration Revision            : 0
        Primary ID                        : 0000.0000.0000
        Primary Description               : 
        MD5 digest                        : 


        Feature UNKNOWN:
        --------------
        VTP Operating Mode                : Transparent

    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowVtpStatus(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowVtpStatus(device=self.device)
        parsed_output = obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)


    def test_golden_3(self):
        self.device = Mock(**self.golden_output_3)
        obj = ShowVtpStatus(device=self.device)
        parsed_output = obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output_3)


if __name__ == '__main__':
    unittest.main()