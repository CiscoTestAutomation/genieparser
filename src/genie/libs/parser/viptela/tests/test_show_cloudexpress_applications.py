# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# Parser
from genie.libs.parser.viptela.show_cloudexpress_applications import ShowCloudexpressApplication


# ============================================
# Parser for the following commands
#   * 'show cloudexpress applications'
# ============================================
class TestShowCloudexpressApplication(unittest.TestCase):
    device = Device(name='aDevice')
    maxDiff = None
    empty_output = {'execute.return_value': ''}

    golden_output = {
        'execute.return_value':
        '''
        vEdge# show cloudexpress applications

                                      EXIT     GATEWAY                                  LOCAL  REMOTE
        VPN  APPLICATION              TYPE     SYSTEM IP      INTERFACE  LATENCY  LOSS  COLOR  COLOR
        ---------------------------------------------------------------------------------------------
        1    salesforce               gateway  172.16.255.14  -          103      1     lte    lte
        1    google_apps              gateway  172.16.255.14  -          47       0     lte    lte
        '''
    }

    golden_parsed_output = {
        "index": {
            0: {
                "application": "salesforce",
                "exit_type": "gateway",
                "gw_sys_ip": "172.16.255.14",
                "interface": "-",
                "latency": 103,
                "local_color": "lte",
                "loss": 1,
                "remote_color": "lte",
                "vpn": 1,
            },
            1: {
                "application": "google_apps",
                "exit_type": "gateway",
                "gw_sys_ip": "172.16.255.14",
                "interface": "-",
                "latency": 47,
                "local_color": "lte",
                "loss": 0,
                "remote_color": "lte",
                "vpn": 1,
            },
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowCloudexpressApplication(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowCloudexpressApplication(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == '__main__':
    unittest.main()
