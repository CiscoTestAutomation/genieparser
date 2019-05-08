# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# Parser
from genie.libs.parser.nxos.show_guestshell import ShowGuestshell


# ===============================
# Unit test for "show guestshell"
# ===============================
class test_show_guestshell(unittest.TestCase):
    """Unit test for "show guestshell"."""

    empty_output = {'execute.return_value': """

    """}

    golden_parsed_output_1 = {
        'state': 'activated',
        'info': {
            'package_location': '/isanboot/bin/guestshell.ova',
            'version': '2.4(0.0)',
            'description': 'Cisco Systems Guest Shell',
            'signing_key_type': 'Cisco release key',
        },
        'resource_reservation': {
            'disk': 1000,
            'memory': 500,
            'cpu': 1,
        }
    }

    golden_output_1 = {'execute.return_value': """
        Virtual service guestshell+ detail
          State                 : Activated
          Package information
            Name                : guestshell.ova
            Path                : /isanboot/bin/guestshell.ova
            Application
              Name              : GuestShell
              Installed version : 2.4(0.0)
              Description       : Cisco Systems Guest Shell
            Signing
              Key type          : Cisco release key
              Method            : SHA-1
            Licensing
              Name              : None
              Version           : None
          Resource reservation
            Disk                : 1000 MB
            Memory              : 500 MB
            CPU                 : 1% system CPU

          Attached devices
            Type              Name        Alias
            ---------------------------------------------
            Disk              _rootfs
            Disk              /cisco/cor
            Serial/shell
            Serial/aux
            Serial/Syslog                 serial2
            Serial/Trace                  serial3
    """}

    def test_show_guestshell_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowGuestshell(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_guestshell_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowGuestshell(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)


if __name__ == "__main__":
    unittest.main()
