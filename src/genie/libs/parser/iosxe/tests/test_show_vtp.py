# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                       SchemaMissingKeyError

# Parser
from genie.libs.parser.iosxe.show_vtp import ShowVtpStatus, \
                                        ShowVtpPassword

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
# Parser for 'show vtp status'
# ============================================
class test_show_vtp_status(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        "vtp": {
        "pruning_mode": False,
        "device_id": "3820.5622.a580",
        "traps_generation": False,
        "updater_id": "192.168.234.1",
        "updater_interface": "Vl100",
        "updater_reason": "lowest numbered VLAN interface found",
        "configuration_revision": 55,
        "maximum_vlans": 1005,
        "md5_digest": '0x2D 0x35 0x38 0x3C 0x3D 0x55 0x62 0x66 0x67 0x70 '\
                      '0x72 0x74 0x9E 0xDD 0xDE 0xE9',
        "existing_vlans": 53,
        "enabled": True,
        "operating_mode": "server",
        "conf_last_modified_time": "12-5-17 09:35:46",
        "conf_last_modified_by": "192.168.234.1",
        "version": "1",
        "version_capable": [1,2,3],
        }

    }

    golden_output = {'execute.return_value': '''\
        VTP Version capable             : 1 to 3
        VTP version running             : 1
        VTP Domain Name                 : 
        VTP Pruning Mode                : Disabled
        VTP Traps Generation            : Disabled
        Device ID                       : 3820.5622.a580
        Configuration last modified by 192.168.234.1 at 12-5-17 09:35:46
        Local updater ID is 192.168.234.1 on interface Vl100 (lowest numbered VLAN interface found)

        Feature VLAN:
        --------------
        VTP Operating Mode                : Server
        Maximum VLANs supported locally   : 1005
        Number of existing VLANs          : 53
        Configuration Revision            : 55
        MD5 digest                        : 0x9E 0x35 0x3C 0x74 0xDD 0xE9 0x3D 0x62 
                                            0xDE 0x2D 0x66 0x67 0x70 0x72 0x55 0x38
    '''}

    golden_parsed_output_2 = {
        'vtp': {
            'conf_last_modified_by': '0.0.0.0',
            'conf_last_modified_time': '0-0-00 00:00:00',
            'configuration_revision': 0,
            'domain_name': '<>',
            'enabled': False,
            'existing_vlans': 100,
            'maximum_vlans': 1005,
            'md5_digest': '0x11 0x22 0x50 0x77 0x99 0xA1 0xB2 0xC3',
            'operating_mode': 'transparent',
            'pruning_mode': True,
            'traps_generation': True,
            'version': '1',
            'version_capable': ['2']
        }
    }

    golden_output_2 = {'execute.return_value': '''\
        VTP Version : running VTP1 (VTP2 capable)
        Configuration Revision : 0
        Maximum VLANs supported locally : 1005
        Number of existing VLANs : 100
        VTP Operating Mode : Transparent
        VTP Domain Name : <>
        VTP Pruning Mode : Enabled
        VTP V2 Mode : Disabled
        VTP Traps Generation : Enabled
        MD5 digest : 0x11 0xA1 0xB2 0x77 0x22 0x50 0xC3 0x99
        Configuration last modified by 0.0.0.0 at 0-0-00 00:00:00
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

    golden_output_4 = {'execute.return_value': '''\
        show vtp status
        VTP Version capable             : 1 to 3
        VTP version running             : 3
        VTP Domain Name                 : GENIE
        VTP Pruning Mode                : Disabled
        VTP Traps Generation            : Disabled
        Device ID                       : 02da.308e.1ae9

        Feature VLAN:
        --------------
        VTP Operating Mode                : Primary Server
        Number of existing VLANs          : 40
        Number of existing extended VLANs : 0
        Maximum VLANs supported locally   : 2048
        Configuration Revision            : 25
        Primary ID                        : 02da.308e.1ae9
        Primary Description               : genie
        MD5 digest                        : 0x3D 0x05 0xEE 0x1F 0x35 0xCC 0x7C 0x74
                                            0x41 0x7A 0xB2 0x1F 0xE9 0x77 0x9A 0xCD


        Feature MST:
        --------------
        VTP Operating Mode                : Transparent


        Feature UNKNOWN:
        --------------
        VTP Operating Mode                : Transparent

    '''
    }

    golden_parsed_output_4 = {
        'vtp': {
            'device_id': '02da.308e.1ae9',
            'domain_name': 'GENIE',
            'feature': {
                'mst': {
                    'enabled': False, 'operating_mode': 'transparent'
                },
                'unknown': {
                    'enabled': False,
                    'operating_mode': 'transparent'
                },
                'vlan': {
                    'configuration_revision': 25,
                    'enabled': True,
                    'existing_extended_vlans': 0,
                    'existing_vlans': 40,
                    'maximum_vlans': 2048,
                    'md5_digest': '0x05 0x1F 0x1F 0x35 0x3D 0x41 '
                                  '0x74 0x77 0x7A 0x7C 0x9A 0xB2 '
                                  '0xCC 0xCD 0xE9 0xEE',
                    'operating_mode': 'primary server',
                    'primary_description': 'genie',
                    'primary_id': '02da.308e.1ae9'
                }
            },
            'pruning_mode': False,
            'traps_generation': False,
            'version': '3',
            'version_capable': [1, 2, 3]
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

    def test_golden_2(self):
        self.device = Mock(**self.golden_output_2)
        obj = ShowVtpStatus(device=self.device)
        parsed_output = obj.parse()
        self.maxDiff = None
        self.assertEqual(parsed_output,self.golden_parsed_output_2)

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
