# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import (
    SchemaEmptyParserError,
    SchemaMissingKeyError,
)

from genie.libs.parser.junos.show_smnp import ShowSnmpMibWalkSystem


# =========================================================
# Unit test for show snmp mib walk system
# =========================================================
class TestShowSnmpMibWalkSystem(unittest.TestCase):

    device = Device(name="aDevice")

    maxDiff = None

    empty_output = {"execute.return_value": ""}

    golden_parsed_output_1 = {
        "snmp-object-information": {
            "snmp-object": [
                {
                    "name": "sysDescr.0",
                    "object-value": "Juniper "
                    "Networks, Inc. "
                    "vmx internet "
                    "router, kernel "
                    "JUNOS 19.2R1.8, "
                    "Build date: "
                    "2019-06-21 "
                    "21:03:26 UTC "
                    "Copyright (c) "
                    "1996-2019 "
                    "Juniper "
                    "Networks, Inc.",
                },
                {"name": "sysObjectID.0", "object-value": "jnxProductNameVMX"},
                {"name": "sysUpTime.0", "object-value": "1805867174"},
                {"name": "sysContact.0", "object-value": "KHK"},
                {"name": "sysName.0", "object-value": "sr_hktGCS001"},
                {
                    "name": "sysLocation.0",
                    "object-value": "TH-HK2/floor_1B-002/rack_KHK1104",
                },
                {"name": "sysServices.0", "object-value": "6"},
            ]
        }
    }

    golden_output_1 = {
        "execute.return_value": """
            show snmp mib walk system
        sysDescr.0    = Juniper Networks, Inc. vmx internet router, kernel JUNOS 19.2R1.8, Build date: 2019-06-21 21:03:26 UTC Copyright (c) 1996-2019 Juniper Networks, Inc.
        sysObjectID.0 = jnxProductNameVMX
        sysUpTime.0   = 1805867174
        sysContact.0  = KHK
        sysName.0     = sr_hktGCS001
        sysLocation.0 = TH-HK2/floor_1B-002/rack_KHK1104
        sysServices.0 = 6
    """
    }

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSnmpMibWalkSystem(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowSnmpMibWalkSystem(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_1)
