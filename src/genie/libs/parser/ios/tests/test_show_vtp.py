# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError
# Parser
from genie.libs.parser.ios.show_vtp import ShowVtpStatus
from genie.libs.parser.ios.show_vtp import ShowVtpPassword


# ============================================
# Parser for 'show vtp password'
# ============================================
class test_show_vtp_password(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "vtp": {
            "configured": False,
        }
    }

    golden_output = {'execute.return_value': '''\
        The VTP password is not configured.
    '''}

    golden_parsed_output_2 = {
        "vtp": {
            "configured": True,
            "password": 'testing',
        }
    }

    golden_output_2 = {'execute.return_value': '''\
        VTP Password: testing
    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowVtpPassword(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowVtpPassword(device=self.device)
        parsed_output = obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_2(self):
        self.device = Mock(**self.golden_output_2)
        obj = ShowVtpPassword(device=self.device)
        parsed_output_2 = obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output_2,self.golden_parsed_output_2)


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
            'device_id': '3820.56ff.c7a2',
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
                    'primary_id': '3820.56ff.c7a2',
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
        Device ID                       : 3820.56ff.c7a2

        Feature VLAN:
        --------------
        VTP Operating Mode                : Primary Server
        Number of existing VLANs          : 100
        Number of existing extended VLANs : 0
        Maximum VLANs supported locally   : 4096
        Configuration Revision            : 2
        Primary ID                        : 3820.56ff.c7a2
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

    golden_output_4 = {'execute.return_value': '''\
        VTP Version capable             : 1 to 3
        VTP version running             : 3
        VTP Domain Name                 : GENIE
        VTP Pruning Mode                : Disabled
        VTP Traps Generation            : Disabled
        Device ID                       : 885a.92ff.7c92
        
        Feature VLAN:
        --------------
        VTP Operating Mode                : Client
        Number of existing VLANs          : 47
        Number of existing extended VLANs : 0
        Maximum VLANs supported locally   : 2048
        Configuration Revision            : 15
        Primary ID                        : 501c.bfff.a91e
        Primary Description               : sw001
        MD5 digest                        : 0xD9 0xAA 0x42 0x1D 0xD7 0xD6 0xA7 0x23
                                            0xE8 0xBE 0xA0 0xB3 0x33 0xB1 0x7A 0x62
        
        
        Feature MST:
        --------------
        VTP Operating Mode                : Transparent

    '''}

    golden_parsed_output_4 = {
        'vtp': {
            'version_capable': [1, 2, 3],
            'version': '3',
            'feature': {
                'vlan': {
                    'operating_mode': 'client',
                    'enabled': True,
                    'existing_vlans': 47,
                    'existing_extended_vlans': 0,
                    'maximum_vlans': 2048,
                    'configuration_revision': 15,
                    'primary_id': '501c.bfff.a91e',
                    'primary_description': 'sw001',
                    'md5_digest': '0x1D 0x23 0x33 0x42 0x62 0x7A 0xA0 0xA7 0xAA 0xB1 0xB3 0xBE 0xD6 0xD7 0xD9 0xE8'
                },
                'mst': {
                    'operating_mode': 'transparent',
                    'enabled': False
                }
            },
                'domain_name': 'GENIE',
                'pruning_mode': False,
                'traps_generation': False,
                'device_id': '885a.92ff.7c92'
            }
        }
    
    
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

    def test_golden_4(self):
        self.device = Mock(**self.golden_output_4)
        obj = ShowVtpStatus(device=self.device)
        parsed_output = obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output_4)

if __name__ == '__main__':
    unittest.main()
