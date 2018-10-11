
# Python
import re
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Parser
from genie.libs.parser.nxos.show_system import ShowSystemInternalSysmgrServiceName, \
                                               ShowSystemInternalL2fwderMac

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

class test_show_system_internal_l2fwder(unittest.TestCase):
    
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'vlans':
            {'1': {'mac_addresses': {'5e01.8000.0007': {'entry': 'G',
                                                      'mac_aging_time': '-',
                                                      'mac_type': 'static',
                                                      'ntfy': 'F',
                                                      'ports': 'sup-eth1(R)',
                                                      'secure': 'F'}}},
           '100': {'mac_addresses': {'5e01.8000.0007': {'entry': 'G',
                                                        'mac_aging_time': '-',
                                                        'mac_type': 'static',
                                                        'ntfy': 'F',
                                                        'ports': 'sup-eth1(R)',
                                                        'secure': 'F'},
                                     'fa16.3e59.d0b2': {'entry': '*',
                                                        'mac_aging_time': '-',
                                                        'mac_type': 'static',
                                                        'ntfy': 'F',
                                                        'ports': '(0x47000001) '
                                                                 'nve-peer1 '
                                                                 '93.1.1.',
                                                        'secure': 'F'},
                                     'fa16.3ec1.a96f': {'entry': '*',
                                                        'mac_aging_time': '00:01:43',
                                                        'mac_type': 'dynamic',
                                                        'ntfy': 'F',
                                                        'ports': 'Eth1/4',
                                                        'secure': 'F'}}},
           '1000': {'mac_addresses': {'5e01.8000.0007': {'entry': 'G',
                                                         'mac_aging_time': '-',
                                                         'mac_type': 'static',
                                                         'ntfy': 'F',
                                                         'ports': 'sup-eth1(R)',
                                                         'secure': 'F'}}},
           '1005': {'mac_addresses': {'5e01.8000.0007': {'entry': 'G',
                                                         'mac_aging_time': '-',
                                                         'mac_type': 'static',
                                                         'ntfy': 'F',
                                                         'ports': 'sup-eth1(R)',
                                                         'secure': 'F'}}},
           '1006': {'mac_addresses': {'5e01.8000.0007': {'entry': 'G',
                                                         'mac_aging_time': '-',
                                                         'mac_type': 'static',
                                                         'ntfy': 'F',
                                                         'ports': 'sup-eth1(R)',
                                                         'secure': 'F'}}},
           '1007': {'mac_addresses': {'5e01.8000.0007': {'entry': 'G',
                                                         'mac_aging_time': '-',
                                                         'mac_type': 'static',
                                                         'ntfy': 'F',
                                                         'ports': 'sup-eth1(R)',
                                                         'secure': 'F'}}},
           '1008': {'mac_addresses': {'5e01.8000.0007': {'entry': 'G',
                                                         'mac_aging_time': '-',
                                                         'mac_type': 'static',
                                                         'ntfy': 'F',
                                                         'ports': 'sup-eth1(R)',
                                                         'secure': 'F'}}},
           '1009': {'mac_addresses': {'5e01.8000.0007': {'entry': 'G',
                                                         'mac_aging_time': '-',
                                                         'mac_type': 'static',
                                                         'ntfy': 'F',
                                                         'ports': 'sup-eth1(R)',
                                                         'secure': 'F'}}},
           '101': {'mac_addresses': {'5e01.8000.0007': {'entry': 'G',
                                                        'mac_aging_time': '-',
                                                        'mac_type': 'static',
                                                        'ntfy': 'F',
                                                        'ports': 'sup-eth1(R)',
                                                        'secure': 'F'}}},
           '102': {'mac_addresses': {'5e01.8000.0007': {'entry': 'G',
                                                        'mac_aging_time': '-',
                                                        'mac_type': 'static',
                                                        'ntfy': 'F',
                                                        'ports': 'sup-eth1(R)',
                                                        'secure': 'F'}}},
           '103': {'mac_addresses': {'5e01.8000.0007': {'entry': 'G',
                                                        'mac_aging_time': '-',
                                                        'mac_type': 'static',
                                                        'ntfy': 'F',
                                                        'ports': 'sup-eth1(R)',
                                                        'secure': 'F'}}},
           '105': {'mac_addresses': {'5e01.8000.0007': {'entry': 'G',
                                                        'mac_aging_time': '-',
                                                        'mac_type': 'static',
                                                        'ntfy': 'F',
                                                        'ports': 'sup-eth1(R)',
                                                        'secure': 'F'}}},
           '106': {'mac_addresses': {'5e01.8000.0007': {'entry': 'G',
                                                        'mac_aging_time': '-',
                                                        'mac_type': 'static',
                                                        'ntfy': 'F',
                                                        'ports': 'sup-eth1(R)',
                                                        'secure': 'F'}}},
           '107': {'mac_addresses': {'5e01.8000.0007': {'entry': 'G',
                                                        'mac_aging_time': '-',
                                                        'mac_type': 'static',
                                                        'ntfy': 'F',
                                                        'ports': 'sup-eth1(R)',
                                                        'secure': 'F'}}},
           '108': {'mac_addresses': {'5e01.8000.0007': {'entry': 'G',
                                                        'mac_aging_time': '-',
                                                        'mac_type': 'static',
                                                        'ntfy': 'F',
                                                        'ports': 'sup-eth1(R)',
                                                        'secure': 'F'}}},
           '109': {'mac_addresses': {'5e01.8000.0007': {'entry': 'G',
                                                        'mac_aging_time': '-',
                                                        'mac_type': 'static',
                                                        'ntfy': 'F',
                                                        'ports': 'sup-eth1(R)',
                                                        'secure': 'F'}}},
           '110': {'mac_addresses': {'5e01.8000.0007': {'entry': 'G',
                                                        'mac_aging_time': '-',
                                                        'mac_type': 'static',
                                                        'ntfy': 'F',
                                                        'ports': 'sup-eth1(R)',
                                                        'secure': 'F'}}},
           '111': {'mac_addresses': {'5e01.8000.0007': {'entry': 'G',
                                                        'mac_aging_time': '-',
                                                        'mac_type': 'static',
                                                        'ntfy': 'F',
                                                        'ports': 'sup-eth1(R)',
                                                        'secure': 'F'}}},
           '112': {'mac_addresses': {'5e01.8000.0007': {'entry': 'G',
                                                        'mac_aging_time': '-',
                                                        'mac_type': 'static',
                                                        'ntfy': 'F',
                                                        'ports': 'sup-eth1(R)',
                                                        'secure': 'F'}}},
           '113': {'mac_addresses': {'5e01.8000.0007': {'entry': 'G',
                                                        'mac_aging_time': '-',
                                                        'mac_type': 'static',
                                                        'ntfy': 'F',
                                                        'ports': 'sup-eth1(R)',
                                                        'secure': 'F'}}},
           '114': {'mac_addresses': {'5e01.8000.0007': {'entry': 'G',
                                                        'mac_aging_time': '-',
                                                        'mac_type': 'static',
                                                        'ntfy': 'F',
                                                        'ports': 'sup-eth1(R)',
                                                        'secure': 'F'}}}}}

    golden_output = {'execute.return_value': '''
        N95_1# show system internal l2fwder Mac
        Legend: 
                * - primary entry, G - Gateway MAC, (R) - Routed MAC, O - Overlay MAC
                age - seconds since last seen,+ - primary entry using vPC Peer-Link,
                (T) - True, (F) - False, C - ControlPlane MAC
           VLAN     MAC Address      Type      age     Secure NTFY Ports
        ---------+-----------------+--------+---------+------+----+------------------
        G  1008    5e01.8000.0007    static   -          F     F   sup-eth1(R)
        G  1009    5e01.8000.0007    static   -          F     F   sup-eth1(R)
        G  1006    5e01.8000.0007    static   -          F     F   sup-eth1(R)
        G  1007    5e01.8000.0007    static   -          F     F   sup-eth1(R)
        G  1005    5e01.8000.0007    static   -          F     F   sup-eth1(R)
        G  1000    5e01.8000.0007    static   -          F     F   sup-eth1(R)
        G   114    5e01.8000.0007    static   -          F     F   sup-eth1(R)
        G   112    5e01.8000.0007    static   -          F     F   sup-eth1(R)
        G   113    5e01.8000.0007    static   -          F     F   sup-eth1(R)
        G   110    5e01.8000.0007    static   -          F     F   sup-eth1(R)
        G   111    5e01.8000.0007    static   -          F     F   sup-eth1(R)
        G   108    5e01.8000.0007    static   -          F     F   sup-eth1(R)
        G   109    5e01.8000.0007    static   -          F     F   sup-eth1(R)
        G   106    5e01.8000.0007    static   -          F     F   sup-eth1(R)
        G   107    5e01.8000.0007    static   -          F     F   sup-eth1(R)
        *   100    fa16.3e59.d0b2    static   -          F     F  (0x47000001) nve-peer1 93.1.1.  
        G   105    5e01.8000.0007    static   -          F     F   sup-eth1(R)
        G   102    5e01.8000.0007    static   -          F     F   sup-eth1(R)
        G   103    5e01.8000.0007    static   -          F     F   sup-eth1(R)
        G   100    5e01.8000.0007    static   -          F     F   sup-eth1(R)
        G   101    5e01.8000.0007    static   -          F     F   sup-eth1(R)
        G     1    5e01.8000.0007    static   -          F     F   sup-eth1(R)
        *   100    fa16.3ec1.a96f   dynamic   00:01:43   F     F     Eth1/4  
            1           1         -00:00:de:ad:be:ef         -             1
    '''}

    def test_show_system_internal_l2fwder_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowSystemInternalL2fwderMac(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_show_system_internal_l2fwder_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowSystemInternalL2fwderMac(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

if __name__ == '__main__':
    unittest.main()

# vim: ft=python et sw=4