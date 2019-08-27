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


if __name__ == '__main__':
    unittest.main()