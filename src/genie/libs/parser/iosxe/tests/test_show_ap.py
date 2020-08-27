import unittest
from unittest.mock import Mock

from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.iosxe.show_ap import ShowApDot11DualBandSummary


# ===============================================
# Unit test for 'show ap dot11 dual-band summary'
# ===============================================
class TestShowApDot11DualBandSummary(unittest.TestCase):
    """Unit test for 'show ap dot11 dual-band summary'"""

    maxDiff = None
    empty_output = {'execute.return_value': ''}
    golden_parsed_output1 = {
        "ap_dot11_dual-band_summary": {
            1: {
                "ap_name": "aa-test-4800",
                "ap_mac_address": "64d8.14ec.1120",
                "slot_id": 0,
                "admin_state": "Enabled",
                "oper_state": "Down",
                "width": 20,
                "tx_pwr": "*1/8 (23 dBm)",
                "mode": "Local",
                "subband": "All",
                "channel": "(6)*"
            },
            2: {
                "ap_name": "aa-test-4800",
                "ap_mac_address": "64d8.14ec.1120",
                "slot_id": 2,
                "admin_state": "Enabled",
                "oper_state": "Down",
                "width": 20,
                "tx_pwr": "N/A",
                "mode": "Monitor",
                "subband": "All",
                "channel": "N/A"
            }
        }
    }

    golden_output1 = {'execute.return_value': '''
AP Name                           Mac Address     Slot  Admin State   Oper State     Width  Txpwr           Mode    Subband    channel 
---------------------------------------------------------------------------------------------------------------------------------------------------------
aa-test-4800                 64d8.14ec.1120  0     Enabled       Down           20     *1/8 (23 dBm)   Local   All        (6)*                     
aa-test-4800                 64d8.14ec.1120  2     Enabled       Down           20     N/A             Monitor All        N/A

    '''}

    def test_show_ap_dot11_dual_band_summary_full(self):
        self.device = Mock(**self.golden_output1)
        obj = ShowApDot11DualBandSummary(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ap_dot11_dual_band_summary_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowApDot11DualBandSummary(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()
