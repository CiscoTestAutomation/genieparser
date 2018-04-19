
# Python
import re
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Parser
from genie.libs.parser.nxos.show_system import ShowSystemInternalSysmgrServiceName

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# ====================================================================
# Parser for 'show system internal sysmgr service name <service_name>'
# ====================================================================

class test_show_system_internal_sysmgr_service_name(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        "instance": {
              "__inst_007__ospf": {
                   "tag": {
                        "N/A": {
                             "process_name": "ospf",
                             "internal_id": 41,
                             "state_start_date": "Sat Jul  1 14:49:10 2017",
                             "uuid": "0x47000119",
                             "reboot_state": "never_started",
                             "plugin_id": "1",
                             "state": "SRV_STATE_WAIT_SPAWN_CONDITION"
                        }
                   }
              },
              "__inst_002__ospf": {
                   "tag": {
                        "100": {
                             "sap": 321,
                             "process_name": "ospf",
                             "internal_id": 18,
                             "state_start_date": "Sat Jul  1 14:49:12 2017",
                             "uuid": "0x42000119",
                             "reboot_state": "never_crashed",
                             "restart_count": 1,
                             "plugin_id": "1",
                             "last_restart_date": "Sat Jul  1 14:49:10 2017",
                             "pid": 7150,
                             "state": "SRV_STATE_HANDSHAKED"
                        }
                   }
              },
              "__inst_001__ospf": {
                   "tag": {
                        "1": {
                             "sap": 320,
                             "process_name": "ospf",
                             "internal_id": 13,
                             "state_start_date": "Sat Jul  1 14:49:12 2017",
                             "uuid": "0x41000119",
                             "reboot_state": "never_crashed",
                             "restart_count": 1,
                             "plugin_id": "1",
                             "last_restart_date": "Sat Jul  1 14:49:10 2017",
                             "pid": 7154,
                             "state": "SRV_STATE_HANDSHAKED"
                    }
                }
            }
        }
    }

    golden_output = {'execute.return_value': '''
        Service "__inst_001__ospf" ("ospf", 13):
            UUID = 0x41000119, PID = 7154, SAP = 320
            State: SRV_STATE_HANDSHAKED (entered at time Sat Jul  1 14:49:12 2017).
            Restart count: 1
            Time of last restart: Sat Jul  1 14:49:10 2017.
            The service never crashed since the last reboot.
            Tag = 1
            Plugin ID: 1

        Service "__inst_002__ospf" ("ospf", 18):
            UUID = 0x42000119, PID = 7150, SAP = 321
            State: SRV_STATE_HANDSHAKED (entered at time Sat Jul  1 14:49:12 2017).
            Restart count: 1
            Time of last restart: Sat Jul  1 14:49:10 2017.
            The service never crashed since the last reboot.
            Tag = 100
            Plugin ID: 1
        Service "__inst_007__ospf" ("ospf", 41):
            UUID = 0x47000119, -- Currently not running --
            State: SRV_STATE_WAIT_SPAWN_CONDITION (entered at time Sat Jul  1 14:49:10 2017).
            The service has never been started since the last reboot.
            Tag = N/A
            Plugin ID: 1
        '''}

    def test_show_system_internal_sysmgr_service_name_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowSystemInternalSysmgrServiceName(device=self.device)
        parsed_output = obj.parse(process='ospf')
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_show_system_internal_sysmgr_service_name_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSystemInternalSysmgrServiceName(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(process='ospf')

if __name__ == '__main__':
    unittest.main()


# vim: ft=python et sw=4