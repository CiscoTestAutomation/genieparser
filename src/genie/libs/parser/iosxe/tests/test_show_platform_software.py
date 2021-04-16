# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device
from pyats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                             SchemaMissingKeyError

# iosxe show_mka_sessions
from genie.libs.parser.iosxe.show_platform_software import ShowPlatformSoftware

# ==========================================
# Unit test for
#   * 'show platform software objectmanager'
# ==========================================

class test_Show_Platform_Software(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    golden_parsed_output_brief={
   "statistics":{
      "Object_update":{
         "pending_issue":0,
         "pending_ack":0
      },
      "Batch_begin":{
         "pending_issue":0,
         "pending_ack":0
      },
      "Batch_end":{
         "pending_issue":0,
         "pending_ack":0
      },
      "Command":{
         "pending_ack":0
      },
      "Total_objects":827,
      "Stale_objects":0,
      "Resolve_objects":0,
      "Childless_delete_objects":0,
      "Error-objects":0,
      "num_of_bundles":0,
      "paused_types":0
   }
}

    golden_output_brief = {'execute.return_value': '''
    Forwarding Manager Asynchronous Object Manager Statistics

    Object update: Pending-issue: 0, Pending-acknowledgement: 0
    Batch begin:   Pending-issue: 0, Pending-acknowledgement: 0
    Batch end:     Pending-issue: 0, Pending-acknowledgement: 0
    Command:       Pending-acknowledgement: 0
    Total-objects: 827
    Stale-objects: 0
    Resolve-objects: 0
    Childless-delete-objects: 0
    Error-objects: 0
    Number of bundles: 0
    Paused-types: 0

    '''}

    def test_Show_Platform_Software(self):
        self.device = Mock(**self.golden_output_brief)
        obj = ShowPlatformSoftware(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_brief)

if __name__ == '__main__':
    unittest.main()
