# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                             SchemaMissingKeyError

# iosxe show_bgp
from genie.libs.parser.iosxe.show_device_tracking_features import ShowDeviceTrackingFeatures

class test_show_device_tracking_features(unittest.TestCase):
    """unit test for show device-tracking features"""
    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}
    golden_parsed_output_brief = {
        "features":{
            "DHCP Guard":{
                "feature":"DHCP Guard",
                "priority":200,
                "state":"READY"
            },
            "RA guard":{
                "feature":"RA guard",
                "priority":192,
                "state":"READY"
            }
        
        }
    }
    golden_output_brief = {'execute.return_value': '''
        Feature name   priority state
        DHCP Guard        200   READY
        RA guard          192   READY
    '''}

    def test_show_device_tracking_features(self):
        self.device = Mock(**self.golden_output_brief)
        obj = ShowDeviceTrackingFeatures(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_brief)

if __name__ == '__main__':
    unittest.main()
