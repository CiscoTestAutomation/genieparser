# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# Parser
from genie.libs.parser.nxos.show_virtual_service import ShowVirtualServiceList

# =========================================
# Unit test for "show virtual-service list"
# =========================================
class test_show_virtual_service_list(unittest.TestCase):
    """Unit test for "show virtual-service list"."""

    empty_output = {'execute.return_value': """


        Virtual Service List:


        """}

    golden_parsed_output = {
        'service': {
            "guestshell+": {
                'status': "activated",
                'package': "guestshell.ova",
            },
            "lxc4": {
                'status': "not installed",
            },
            "sc_sanity_03": {
                'status': "installed",
                'package': "ft_mv_no_onep.ova",
            },
            "lxc_upgrade": {
                'status': "activate failed",
                'package': "c63lxc_no_onep.ova",
            },
        },
    }

    golden_output = {'execute.return_value': """
        
        
        Virtual Service List:
        
        Name                    Status             Package Name
        ----------------------------------------------------------------------
        guestshell+             Activated          guestshell.ova
        lxc4                    Not Installed      Not Available
        sc_sanity_03            Installed          ft_mv_no_onep.ova
        lxc_upgrade             Activate Failed    c63lxc_no_onep.ova
        """}

    def test_show_virtual_service_list_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowVirtualServiceList(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_virtual_service_list(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowVirtualServiceList(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


if __name__ == "__main__":
    unittest.main()
