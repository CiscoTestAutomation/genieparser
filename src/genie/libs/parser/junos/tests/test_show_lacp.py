import unittest
from unittest.mock import Mock

from pyats.topology import Device
from pyats.topology import loader
from genie.metaparser.util.exceptions import SchemaEmptyParserError
from genie.libs.parser.junos.show_lacp import ShowLacpInterfacesInterface

""" TestCase for:
        * show lacp interfaces {interface}
"""
class TestShowLacpInterfacesInterface(unittest.TestCase):

    device = Device(name="aDevice")

    maxDiff = None

    empty_output = {"execute.return_value": ""}

    golden_output = {
        "execute.return_value": """
        show lacp interfaces ae4
        Aggregated interface: ae4
            LACP state:       Role   Exp   Def  Dist  Col  Syn  Aggr  Timeout  Activity
            xe-3/0/1       Actor    No    No   Yes  Yes  Yes   Yes     Fast    Active
            xe-3/0/1     Partner    No    No   Yes  Yes  Yes   Yes     Fast    Active
            LACP protocol:        Receive State  Transmit State          Mux State
            xe-3/0/1                  Current   Fast periodic Collecting distributing
    """
    }

    golden_parsed_output = {
        "lacp-interface-information-list": {
            "lacp-interface-information": {
                "lag-lacp-header": {"aggregate-name": "ae4"},
                "lag-lacp-protocol": [
                    {
                        "lacp-mux-state": "Collecting distributing",
                        "lacp-receive-state": "Current",
                        "lacp-transmit-state": "Fast periodic",
                        "name": "xe-3/0/1",
                    }
                ],
                "lag-lacp-state": [
                    {
                        "lacp-activity": "Active",
                        "lacp-aggregation": "Yes",
                        "lacp-collecting": "Yes",
                        "lacp-defaulted": "No",
                        "lacp-distributing": "Yes",
                        "lacp-expired": "No",
                        "lacp-role": "Actor",
                        "lacp-synchronization": "Yes",
                        "lacp-timeout": "Fast",
                        "name": "xe-3/0/1",
                    },
                    {
                        "lacp-activity": "Active",
                        "lacp-aggregation": "Yes",
                        "lacp-collecting": "Yes",
                        "lacp-defaulted": "No",
                        "lacp-distributing": "Yes",
                        "lacp-expired": "No",
                        "lacp-role": "Partner",
                        "lacp-synchronization": "Yes",
                        "lacp-timeout": "Fast",
                        "name": "xe-3/0/1",
                    },
                ],
            }
        }
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowLacpInterfacesInterface(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            obj.parse()

    def test_golden_instance(self):
        self.device = Mock(**self.golden_output)
        obj = ShowLacpInterfacesInterface(device=self.device)
        parsed_output = obj.parse(interface="ae4")
        self.assertEqual(parsed_output, self.golden_parsed_output)

if __name__ == '__main__':
    unittest.main()
