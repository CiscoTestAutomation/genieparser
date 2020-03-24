
# Python
import re
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Parser
from genie.libs.parser.nxos.show_system import ShowSystemInternalSysmgrServiceName, \
                                               ShowSystemInternalL2fwderMac

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError

# ====================================================================
# Parser for 'show system internal sysmgr service name <service_name>'
# ====================================================================

class test_show_system_internal_sysmgr_service_name(unittest.TestCase):

    maxDiff = None
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

    golden_parsed_output2 = {
        'instance': 
            {'__inst_001__ospf': 
                {'tag': 
                    {'ENT': 
                        {'internal_id': 83,
                        'last_restart_date': 'Wed '
                                            'Mar '
                                            '18 '
                                            '10:14:35 '
                                            '2020',
                        'pid': 23994,
                        'plugin_id': '1',
                        'process_name': 'ospf',
                        'reboot_state': 'never_crashed',
                        'restart_count': 1,
                        'sap': 320,
                        'state': 'SRV_STATE_HANDSHAKED',
                        'state_start_date': 'Wed '
                                           'Mar 18 '
                                           '10:14:35 '
                                           '2020',
                        'uuid': '0x41000119'}}},
            '__inst_002__ospf': 
                {'tag': 
                    {'IPN': 
                        {'internal_id': 88,
                        'last_restart_date': 'Wed '
                                            'Mar '
                                            '18 '
                                            '10:14:35 '
                                            '2020',
                        'pid': 23993,
                        'plugin_id': '1',
                        'process_name': 'ospf',
                        'reboot_state': 'never_crashed',
                        'restart_count': 1,
                        'sap': 321,
                        'state': 'SRV_STATE_HANDSHAKED',
                        'state_start_date': 'Wed '
                                           'Mar 18 '
                                           '10:14:35 '
                                           '2020',
                        'uuid': '0x42000119'}}},
            '__inst_003__ospf': 
                {'tag': 
                    {'l3vpn': 
                        {'internal_id': 93,
                        'last_restart_date': 'Wed '
                                          'Mar '
                                          '18 '
                                          '10:14:35 '
                                          '2020',
                        'pid': 23992,
                        'plugin_id': '1',
                        'process_name': 'ospf',
                        'reboot_state': 'never_crashed',
                        'restart_count': 1,
                        'sap': 322,
                        'state': 'SRV_STATE_HANDSHAKED',
                        'state_start_date': 'Wed '
                                         'Mar '
                                         '18 '
                                         '10:14:35 '
                                         '2020',
                        'uuid': '0x43000119'}}},
            '__inst_004__ospf': 
                {'tag': 
                    {'N/A': 
                        {'internal_id': 98,
                        'plugin_id': '1',
                        'process_name': 'ospf',
                        'reboot_state': 'never_started',
                        'state': 'SRV_STATE_WAIT_SPAWN_CONDITION',
                        'state_start_date': 'Wed '
                                           'Mar 18 '
                                           '10:14:35 '
                                           '2020',
                        'uuid': '0x44000119'}}},
            '__inst_005__ospf': 
                {'tag': 
                    {'N/A': 
                        {'internal_id': 103,
                        'plugin_id': '1',
                        'process_name': 'ospf',
                        'reboot_state': 'never_started',
                        'state': 'SRV_STATE_WAIT_SPAWN_CONDITION',
                        'state_start_date': 'Wed '
                                           'Mar 18 '
                                           '10:14:35 '
                                           '2020',
                        'uuid': '0x45000119'}}},
            '__inst_006__ospf': 
                {'tag': 
                    {'N/A': 
                        {'internal_id': 107,
                        'plugin_id': '1',
                        'process_name': 'ospf',
                        'reboot_state': 'never_started',
                        'state': 'SRV_STATE_WAIT_SPAWN_CONDITION',
                        'state_start_date': 'Wed '
                                           'Mar 18 '
                                           '10:14:35 '
                                           '2020',
                        'uuid': '0x46000119'}}},
            '__inst_007__ospf': 
                {'tag': 
                    {'N/A': 
                        {'internal_id': 111,
                        'plugin_id': '1',
                        'process_name': 'ospf',
                        'reboot_state': 'never_started',
                        'state': 'SRV_STATE_WAIT_SPAWN_CONDITION',
                        'state_start_date': 'Wed '
                                           'Mar 18 '
                                           '10:14:35 '
                                           '2020',
                        'uuid': '0x47000119'}}},
            '__inst_008__ospf': 
                {'tag': 
                    {'N/A': 
                        {'internal_id': 115,
                        'plugin_id': '1',
                        'process_name': 'ospf',
                        'reboot_state': 'never_started',
                        'state': 'SRV_STATE_WAIT_SPAWN_CONDITION',
                        'state_start_date': 'Wed '
                                           'Mar 18 '
                                           '10:14:35 '
                                           '2020',
                        'uuid': '0x48000119'}}},
            '__inst_009__ospf': 
                {'tag': 
                    {'N/A': 
                        {'internal_id': 119,
                        'plugin_id': '1',
                        'process_name': 'ospf',
                        'reboot_state': 'never_started',
                        'state': 'SRV_STATE_WAIT_SPAWN_CONDITION',
                        'state_start_date': 'Wed '
                                           'Mar 18 '
                                           '10:14:35 '
                                           '2020',
                        'uuid': '0x49000119'}}},
            '__inst_010__ospf': 
                {'tag': 
                    {'N/A': 
                        {'internal_id': 123,
                        'plugin_id': '1',
                        'process_name': 'ospf',
                        'reboot_state': 'never_started',
                        'state': 'SRV_STATE_WAIT_SPAWN_CONDITION',
                        'state_start_date': 'Wed '
                                           'Mar 18 '
                                           '10:14:35 '
                                           '2020',
                        'uuid': '0x4A000119'}}},
            '__inst_011__ospf': 
                {'tag': 
                    {'N/A': 
                        {'internal_id': 127,
                        'plugin_id': '1',
                        'process_name': 'ospf',
                        'reboot_state': 'never_started',
                        'state': 'SRV_STATE_WAIT_SPAWN_CONDITION',
                        'state_start_date': 'Wed '
                                           'Mar 18 '
                                           '10:14:35 '
                                           '2020',
                        'uuid': '0x4B000119'}}},
            '__inst_012__ospf': 
                {'tag': 
                    {'N/A': 
                        {'internal_id': 131,
                        'plugin_id': '1',
                        'process_name': 'ospf',
                        'reboot_state': 'never_started',
                        'state': 'SRV_STATE_WAIT_SPAWN_CONDITION',
                        'state_start_date': 'Wed '
                                           'Mar 18 '
                                           '10:14:35 '
                                           '2020',
                        'uuid': '0x4C000119'}}},
            '__inst_013__ospf': 
                {'tag': 
                    {'N/A': 
                        {'internal_id': 135,
                        'plugin_id': '1',
                        'process_name': 'ospf',
                        'reboot_state': 'never_started',
                        'state': 'SRV_STATE_WAIT_SPAWN_CONDITION',
                        'state_start_date': 'Wed '
                                           'Mar 18 '
                                           '10:14:35 '
                                           '2020',
                        'uuid': '0x4D000119'}}},
            '__inst_014__ospf': 
                {'tag': 
                    {'N/A': 
                        {'internal_id': 139,
                        'plugin_id': '1',
                        'process_name': 'ospf',
                        'reboot_state': 'never_started',
                        'state': 'SRV_STATE_WAIT_SPAWN_CONDITION',
                        'state_start_date': 'Wed '
                                           'Mar 18 '
                                           '10:14:35 '
                                           '2020',
                        'uuid': '0x4E000119'}}},
            '__inst_015__ospf': 
                {'tag': 
                    {'N/A': 
                        {'internal_id': 143,
                        'plugin_id': '1',
                        'process_name': 'ospf',
                        'reboot_state': 'never_started',
                        'state': 'SRV_STATE_WAIT_SPAWN_CONDITION',
                        'state_start_date': 'Wed '
                                           'Mar 18 '
                                           '10:14:35 '
                                           '2020',
                        'uuid': '0x4F000119'}}},
            '__inst_016__ospf': 
                {'tag': 
                    {'N/A': 
                        {'internal_id': 147,
                        'plugin_id': '1',
                        'process_name': 'ospf',
                        'reboot_state': 'never_started',
                        'state': 'SRV_STATE_WAIT_SPAWN_CONDITION',
                        'state_start_date': 'Wed '
                                           'Mar 18 '
                                           '10:14:35 '
                                           '2020',
                        'uuid': '0x50000119'}}}}}

    golden_output2 = {'execute.return_value': '''
        show system internal sysmgr service name ospf

        Service "__inst_001__ospf" ("ospf", 83):
         
                UUID = 0x41000119, PID = 23994, SAP = 320
         
                State: SRV_STATE_HANDSHAKED (entered at time Wed Mar 18 10:14:35 2020).
         
                Restart count: 1
         
                Time of last restart: Wed Mar 18 10:14:35 2020.
         
                The service never crashed since the last reboot.
         
                Tag = ENT
         
                Plugin ID: 1
         
         
         
        Service "__inst_002__ospf" ("ospf", 88):
         
                UUID = 0x42000119, PID = 23993, SAP = 321
         
                State: SRV_STATE_HANDSHAKED (entered at time Wed Mar 18 10:14:35 2020).
         
                Restart count: 1
         
                Time of last restart: Wed Mar 18 10:14:35 2020.
         
                The service never crashed since the last reboot.
         
                Tag = IPN
         
                Plugin ID: 1
         
         
         
        Service "__inst_003__ospf" ("ospf", 93):
         
                UUID = 0x43000119, PID = 23992, SAP = 322
         
                State: SRV_STATE_HANDSHAKED (entered at time Wed Mar 18 10:14:35 2020).
         
                Restart count: 1
         
                Time of last restart: Wed Mar 18 10:14:35 2020.
         
                The service never crashed since the last reboot.
         
                Tag = l3vpn
         
                Plugin ID: 1
         
         
         
        Service "__inst_004__ospf" ("ospf", 98):
         
                UUID = 0x44000119, -- Currently not running --
         
                State: SRV_STATE_WAIT_SPAWN_CONDITION (entered at time Wed Mar 18 10:14:35 2020).
         
                The service has never been started since the last reboot.
         
                Tag = N/A
         
                Plugin ID: 1
         
         
         
        Service "__inst_005__ospf" ("ospf", 103):
         
                UUID = 0x45000119, -- Currently not running --
         
                State: SRV_STATE_WAIT_SPAWN_CONDITION (entered at time Wed Mar 18 10:14:35 2020).
         
                The service has never been started since the last reboot.
         
                Tag = N/A
         
                Plugin ID: 1
         
         
         
        Service "__inst_006__ospf" ("ospf", 107):
         
                UUID = 0x46000119, -- Currently not running --
         
                State: SRV_STATE_WAIT_SPAWN_CONDITION (entered at time Wed Mar 18 10:14:35 2020).
         
                The service has never been started since the last reboot.
         
                Tag = N/A
         
                Plugin ID: 1
         
         
         
        Service "__inst_007__ospf" ("ospf", 111):
         
                UUID = 0x47000119, -- Currently not running --
         
                State: SRV_STATE_WAIT_SPAWN_CONDITION (entered at time Wed Mar 18 10:14:35 2020).
         
                The service has never been started since the last reboot.
         
                Tag = N/A
         
                Plugin ID: 1
         
         
         
        Service "__inst_008__ospf" ("ospf", 115):
         
                UUID = 0x48000119, -- Currently not running --
         
                State: SRV_STATE_WAIT_SPAWN_CONDITION (entered at time Wed Mar 18 10:14:35 2020).
         
                The service has never been started since the last reboot.
         
                Tag = N/A
         
                Plugin ID: 1
         
         
         
        Service "__inst_009__ospf" ("ospf", 119):
         
                UUID = 0x49000119, -- Currently not running --
         
                State: SRV_STATE_WAIT_SPAWN_CONDITION (entered at time Wed Mar 18 10:14:35 2020).
         
                The service has never been started since the last reboot.
         
                Tag = N/A
         
                Plugin ID: 1
         
         
         
        Service "__inst_010__ospf" ("ospf", 123):
         
                UUID = 0x4A000119, -- Currently not running --
         
                State: SRV_STATE_WAIT_SPAWN_CONDITION (entered at time Wed Mar 18 10:14:35 2020).
         
                The service has never been started since the last reboot.
         
                Tag = N/A
         
                Plugin ID: 1
         
         
         
        Service "__inst_011__ospf" ("ospf", 127):
         
                UUID = 0x4B000119, -- Currently not running --
         
                State: SRV_STATE_WAIT_SPAWN_CONDITION (entered at time Wed Mar 18 10:14:35 2020).
         
                The service has never been started since the last reboot.
         
                Tag = N/A
         
                Plugin ID: 1
         
         
         
        Service "__inst_012__ospf" ("ospf", 131):
         
                UUID = 0x4C000119, -- Currently not running --
         
                State: SRV_STATE_WAIT_SPAWN_CONDITION (entered at time Wed Mar 18 10:14:35 2020).
         
                The service has never been started since the last reboot.
         
                Tag = N/A
         
                Plugin ID: 1
         
         
         
        Service "__inst_013__ospf" ("ospf", 135):
         
                UUID = 0x4D000119, -- Currently not running --
         
                State: SRV_STATE_WAIT_SPAWN_CONDITION (entered at time Wed Mar 18 10:14:35 2020).
         
                The service has never been started since the last reboot.
         
                Tag = N/A
         
                Plugin ID: 1
         
         
         
        Service "__inst_014__ospf" ("ospf", 139):
         
                UUID = 0x4E000119, -- Currently not running --
         
                State: SRV_STATE_WAIT_SPAWN_CONDITION (entered at time Wed Mar 18 10:14:35 2020).
         
                The service has never been started since the last reboot.
         
                Tag = N/A
         
                Plugin ID: 1
         
         
         
        Service "__inst_015__ospf" ("ospf", 143):
         
                UUID = 0x4F000119, -- Currently not running --
         
                State: SRV_STATE_WAIT_SPAWN_CONDITION (entered at time Wed Mar 18 10:14:35 2020).
         
                The service has never been started since the last reboot.
         
                Tag = N/A
         
                Plugin ID: 1
         
         
         
        Service "__inst_016__ospf" ("ospf", 147):
         
                UUID = 0x50000119, -- Currently not running --
         
                State: SRV_STATE_WAIT_SPAWN_CONDITION (entered at time Wed Mar 18 10:14:35 2020).
         
                The service has never been started since the last reboot.
         
                Tag = N/A
         
                Plugin ID: 1
        '''}

    def test_show_system_internal_sysmgr_service_name_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowSystemInternalSysmgrServiceName(device=self.device)
        parsed_output = obj.parse(process='ospf')
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden2(self):
        self.device = Mock(**self.golden_output2)
        obj = ShowSystemInternalSysmgrServiceName(device=self.device)
        parsed_output = obj.parse(process='ospf')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

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
            {'1': {'mac_addresses': {'5e01.80ff.0007': {'entry': 'G',
                                                      'mac_aging_time': '-',
                                                      'mac_type': 'static',
                                                      'ntfy': 'F',
                                                      'ports': 'sup-eth1(R)',
                                                      'secure': 'F'}}},
           '100': {'mac_addresses': {'5e01.80ff.0007': {'entry': 'G',
                                                        'mac_aging_time': '-',
                                                        'mac_type': 'static',
                                                        'ntfy': 'F',
                                                        'ports': 'sup-eth1(R)',
                                                        'secure': 'F'},
                                     'fa16.3eff.2a0c': {'entry': '*',
                                                        'mac_aging_time': '-',
                                                        'mac_type': 'static',
                                                        'ntfy': 'F',
                                                        'ports': '(0x47000001) '
                                                                 'nve-peer1 '
                                                                 '93.1.1.',
                                                        'secure': 'F'},
                                     'fa16.3eff.6b31': {'entry': '*',
                                                        'mac_aging_time': '00:01:43',
                                                        'mac_type': 'dynamic',
                                                        'ntfy': 'F',
                                                        'ports': 'Eth1/4',
                                                        'secure': 'F'}}},
           '1000': {'mac_addresses': {'5e01.80ff.0007': {'entry': 'G',
                                                         'mac_aging_time': '-',
                                                         'mac_type': 'static',
                                                         'ntfy': 'F',
                                                         'ports': 'sup-eth1(R)',
                                                         'secure': 'F'}}},
           '1005': {'mac_addresses': {'5e01.80ff.0007': {'entry': 'G',
                                                         'mac_aging_time': '-',
                                                         'mac_type': 'static',
                                                         'ntfy': 'F',
                                                         'ports': 'sup-eth1(R)',
                                                         'secure': 'F'}}},
           '1006': {'mac_addresses': {'5e01.80ff.0007': {'entry': 'G',
                                                         'mac_aging_time': '-',
                                                         'mac_type': 'static',
                                                         'ntfy': 'F',
                                                         'ports': 'sup-eth1(R)',
                                                         'secure': 'F'}}},
           '1007': {'mac_addresses': {'5e01.80ff.0007': {'entry': 'G',
                                                         'mac_aging_time': '-',
                                                         'mac_type': 'static',
                                                         'ntfy': 'F',
                                                         'ports': 'sup-eth1(R)',
                                                         'secure': 'F'}}},
           '1008': {'mac_addresses': {'5e01.80ff.0007': {'entry': 'G',
                                                         'mac_aging_time': '-',
                                                         'mac_type': 'static',
                                                         'ntfy': 'F',
                                                         'ports': 'sup-eth1(R)',
                                                         'secure': 'F'}}},
           '1009': {'mac_addresses': {'5e01.80ff.0007': {'entry': 'G',
                                                         'mac_aging_time': '-',
                                                         'mac_type': 'static',
                                                         'ntfy': 'F',
                                                         'ports': 'sup-eth1(R)',
                                                         'secure': 'F'}}},
           '101': {'mac_addresses': {'5e01.80ff.0007': {'entry': 'G',
                                                        'mac_aging_time': '-',
                                                        'mac_type': 'static',
                                                        'ntfy': 'F',
                                                        'ports': 'sup-eth1(R)',
                                                        'secure': 'F'}}},
           '102': {'mac_addresses': {'5e01.80ff.0007': {'entry': 'G',
                                                        'mac_aging_time': '-',
                                                        'mac_type': 'static',
                                                        'ntfy': 'F',
                                                        'ports': 'sup-eth1(R)',
                                                        'secure': 'F'}}},
           '103': {'mac_addresses': {'5e01.80ff.0007': {'entry': 'G',
                                                        'mac_aging_time': '-',
                                                        'mac_type': 'static',
                                                        'ntfy': 'F',
                                                        'ports': 'sup-eth1(R)',
                                                        'secure': 'F'}}},
           '105': {'mac_addresses': {'5e01.80ff.0007': {'entry': 'G',
                                                        'mac_aging_time': '-',
                                                        'mac_type': 'static',
                                                        'ntfy': 'F',
                                                        'ports': 'sup-eth1(R)',
                                                        'secure': 'F'}}},
           '106': {'mac_addresses': {'5e01.80ff.0007': {'entry': 'G',
                                                        'mac_aging_time': '-',
                                                        'mac_type': 'static',
                                                        'ntfy': 'F',
                                                        'ports': 'sup-eth1(R)',
                                                        'secure': 'F'}}},
           '107': {'mac_addresses': {'5e01.80ff.0007': {'entry': 'G',
                                                        'mac_aging_time': '-',
                                                        'mac_type': 'static',
                                                        'ntfy': 'F',
                                                        'ports': 'sup-eth1(R)',
                                                        'secure': 'F'}}},
           '108': {'mac_addresses': {'5e01.80ff.0007': {'entry': 'G',
                                                        'mac_aging_time': '-',
                                                        'mac_type': 'static',
                                                        'ntfy': 'F',
                                                        'ports': 'sup-eth1(R)',
                                                        'secure': 'F'}}},
           '109': {'mac_addresses': {'5e01.80ff.0007': {'entry': 'G',
                                                        'mac_aging_time': '-',
                                                        'mac_type': 'static',
                                                        'ntfy': 'F',
                                                        'ports': 'sup-eth1(R)',
                                                        'secure': 'F'}}},
           '110': {'mac_addresses': {'5e01.80ff.0007': {'entry': 'G',
                                                        'mac_aging_time': '-',
                                                        'mac_type': 'static',
                                                        'ntfy': 'F',
                                                        'ports': 'sup-eth1(R)',
                                                        'secure': 'F'}}},
           '111': {'mac_addresses': {'5e01.80ff.0007': {'entry': 'G',
                                                        'mac_aging_time': '-',
                                                        'mac_type': 'static',
                                                        'ntfy': 'F',
                                                        'ports': 'sup-eth1(R)',
                                                        'secure': 'F'}}},
           '112': {'mac_addresses': {'5e01.80ff.0007': {'entry': 'G',
                                                        'mac_aging_time': '-',
                                                        'mac_type': 'static',
                                                        'ntfy': 'F',
                                                        'ports': 'sup-eth1(R)',
                                                        'secure': 'F'}}},
           '113': {'mac_addresses': {'5e01.80ff.0007': {'entry': 'G',
                                                        'mac_aging_time': '-',
                                                        'mac_type': 'static',
                                                        'ntfy': 'F',
                                                        'ports': 'sup-eth1(R)',
                                                        'secure': 'F'}}},
           '114': {'mac_addresses': {'5e01.80ff.0007': {'entry': 'G',
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
        G  1008    5e01.80ff.0007    static   -          F     F   sup-eth1(R)
        G  1009    5e01.80ff.0007    static   -          F     F   sup-eth1(R)
        G  1006    5e01.80ff.0007    static   -          F     F   sup-eth1(R)
        G  1007    5e01.80ff.0007    static   -          F     F   sup-eth1(R)
        G  1005    5e01.80ff.0007    static   -          F     F   sup-eth1(R)
        G  1000    5e01.80ff.0007    static   -          F     F   sup-eth1(R)
        G   114    5e01.80ff.0007    static   -          F     F   sup-eth1(R)
        G   112    5e01.80ff.0007    static   -          F     F   sup-eth1(R)
        G   113    5e01.80ff.0007    static   -          F     F   sup-eth1(R)
        G   110    5e01.80ff.0007    static   -          F     F   sup-eth1(R)
        G   111    5e01.80ff.0007    static   -          F     F   sup-eth1(R)
        G   108    5e01.80ff.0007    static   -          F     F   sup-eth1(R)
        G   109    5e01.80ff.0007    static   -          F     F   sup-eth1(R)
        G   106    5e01.80ff.0007    static   -          F     F   sup-eth1(R)
        G   107    5e01.80ff.0007    static   -          F     F   sup-eth1(R)
        *   100    fa16.3eff.2a0c    static   -          F     F  (0x47000001) nve-peer1 93.1.1.  
        G   105    5e01.80ff.0007    static   -          F     F   sup-eth1(R)
        G   102    5e01.80ff.0007    static   -          F     F   sup-eth1(R)
        G   103    5e01.80ff.0007    static   -          F     F   sup-eth1(R)
        G   100    5e01.80ff.0007    static   -          F     F   sup-eth1(R)
        G   101    5e01.80ff.0007    static   -          F     F   sup-eth1(R)
        G     1    5e01.80ff.0007    static   -          F     F   sup-eth1(R)
        *   100    fa16.3eff.6b31   dynamic   00:01:43   F     F     Eth1/4  
            1           1         -00:00:de:ff:6c:9d         -             1
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