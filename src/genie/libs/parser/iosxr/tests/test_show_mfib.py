# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxr show_mfib
from genie.libs.parser.iosxr.show_mfib import ShowMfibRouteSummary


# ==========================================================================
# Unittest for 'show mfib route summary'
# ==========================================================================
class test_show_mfib_route_summary(unittest.TestCase):
    """ Unit test for show mfib route summary. """

    empty_output = {'execute.return_value': ''}

    golden_output_1 = {'execute.return_value': """
        Tue Jun 16 22:36:59.181 PDT
        IP Multicast Forwarding Information Base Summary for ALL VRFs (num VRFs: 4)
          No. of (*,G) routes = 20
          No. of (S,G) routes = 176"""}

    golden_output_2 = {'execute.return_value': """
        Tue Jun 16 22:36:44.453 PDT
        IP Multicast Forwarding Information Base Summary for VRF default
          No. of (*,G) routes = 4
          No. of (S,G) routes = 2"""}

    golden_output_3 = {'execute.return_value': """
        Tue Jun 16 22:42:18.713 PDT
        IP Multicast Forwarding Information Base Summary for VRF vpn1
          No. of (*,G) routes = 5
          No. of (S,G) routes = 44"""}

    golden_parsed_output_1 = {
        'vrf':
            {'all':
                {'no_g_routes': 20,
                 'no_sg_routes': 176,
                 'num_vrfs': 4
                 }
             }
        }

    golden_parsed_output_2 = {
        'vrf':
            {'default':
                {'no_g_routes': 4,
                 'no_sg_routes': 2
                 }
             }
        }

    golden_parsed_output_3 = {
        'vrf':
            {'vpn1':
                 {'no_g_routes': 5,
                  'no_sg_routes': 44
                  }
             }
    }

    def test_show_mfib_route_summary_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowMfibRouteSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_mfib_route_summary_full_all_vrfs(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowMfibRouteSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

    def test_show_mfib_route_summary_full_default_vrf(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowMfibRouteSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_show_mfib_route_summary_full_custom_vrf(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_3)
        obj = ShowMfibRouteSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_3)


if __name__ == '__main__':
    unittest.main()
