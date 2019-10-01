# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxr show_mrib
from genie.libs.parser.iosxr.show_l2vpn import (ShowL2vpnBridgeDomain, ShowL2vpnForwardingBridgeDomainMacAddress)

# ===========================================
#  Unit test for 'show l2vpn bridge-domain'
# ===========================================

class TestShowL2vpnBridgeDomain(unittest.TestCase):
    '''Unit test for "show l2vpn bridge-domain"'''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'bridge_group': {
            'g1': {
                'bridge_domain': {
                    'EVPN-Multicast-BTV': {
                        'id': 0,
                        'state': 'up',
                        'shg_id': 0,
                        'mst_i': 0,
                        'aging': 300,
                        'mac_limit': 4000,
                        'action': 'none',
                        'notification': 'syslog',
                        'filter_mac_address': 0,
                        'ac': {
                            'ac': 1,
                            'ac_up': 1,
                            'interfaces': {
                                'GigabitEthernet0/1/0/0': {
                                    'state': 'up',
                                    'static_mac_address': 2,
                                    'mst_i': 0,
                                    'mst_i_state': 'unprotected',
                                },
                            },
                        },
                        'vfi': {
                            'vfi': 1,
                            1: {
                                'neighbor': {
                                    '10.1.1.1': {
                                        'pw_id': {
                                            1: {
                                                'state': 'up',
                                                'static_mac_address': 0,
                                            },
                                        },
                                    },
                                },
                            },
                        },
                        'pw': {
                            'pw': 1,
                            'pw_up': 1,
                        },
                    },
                },
            },
        },
    }

    golden_output1 = {'execute.return_value': '''
        RP/0/RP0/CPU0:router# show l2vpn bridge-domain

        Bridge group: g1, bridge-domain: EVPN-Multicast-BTV, id: 0, state: up, ShgId: 0, MSTi: 0
          Aging: 300 s, MAC limit: 4000, Action: none, Notification: syslog
          Filter MAC addresses: 0
          ACs: 1 (1 up), VFIs: 1, PWs: 1 (1 up)
          List of ACs:
            Gi0/1/0/0, state: up, Static MAC addresses: 2, MSTi: 0 (unprotected)
          List of Access PWs:
          List of VFIs:
            VFI 1
              Neighbor 10.1.1.1 pw-id 1, state: up, Static MAC addresses: 0
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowL2vpnBridgeDomain(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowL2vpnBridgeDomain(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)


# ====================================================================================
#  Unit test for 'show l2vpn forwarding bridge-domain mac-address location {location}'
# ====================================================================================
class TestShowL2vpnForwardingBridgeDomain(unittest.TestCase):
    '''Unit test for 
        show l2vpn forwarding bridge-domain mac-address location {location}
        show l2vpn forwarding bridge-domain {bridge_domain} mac-address location {location}
    '''

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'mac_table': {
            'Te0/0/1/0/3.3': {
                'mac_address': {
                    '0001.0000.0002': {
                        'lc_learned': 'N/A',
                                        'learned_from': 'Te0/0/1/0/3.3',
                                        'mapped_to': 'N/A',
                                        'resync_age': '0d '
                                                      '0h '
                                                      '0m '
                                                      '14s',
                                        'type': 'dynamic'},
                    '0001.0000.0003': {
                        'lc_learned': 'N/A',
                                        'learned_from': 'Te0/0/1/0/3.3',
                                        'mapped_to': 'N/A',
                                        'resync_age': '0d '
                                                      '0h '
                                                      '0m '
                                                      '14s',
                                        'type': 'dynamic'},
                    '0001.0000.0004': {
                        'lc_learned': 'N/A',
                                        'learned_from': 'Te0/0/1/0/3.3',
                                        'mapped_to': 'N/A',
                                        'resync_age': '0d '
                                                      '0h '
                                                      '0m '
                                                      '14s',
                                        'type': 'dynamic'},
                    '0001.0000.0005': {
                        'lc_learned': 'N/A',
                                        'learned_from': 'Te0/0/1/0/3.3',
                                        'mapped_to': 'N/A',
                                        'resync_age': '0d '
                                                      '0h '
                                                      '0m '
                                                      '14s',
                                        'type': 'dynamic'},
                    '0001.0000.0006': {
                        'lc_learned': 'N/A',
                                        'learned_from': 'Te0/0/1/0/3.3',
                                        'mapped_to': 'N/A',
                                        'resync_age': '0d '
                                                      '0h '
                                                      '0m '
                                                      '14s',
                                        'type': 'dynamic'},
                    '0001.0000.0007': {
                        'lc_learned': 'N/A',
                                        'learned_from': 'Te0/0/1/0/3.3',
                                        'mapped_to': 'N/A',
                                        'resync_age': '0d '
                                                      '0h '
                                                      '0m '
                                                      '14s',
                                        'type': 'dynamic'},
                    '0001.0000.0008': {
                        'lc_learned': 'N/A',
                                        'learned_from': 'Te0/0/1/0/3.3',
                                        'mapped_to': 'N/A',
                                        'resync_age': '0d '
                                                      '0h '
                                                      '0m '
                                                      '14s',
                                        'type': 'dynamic'},
                    '0001.0000.0009': {
                        'lc_learned': 'N/A',
                                        'learned_from': 'Te0/0/1/0/3.3',
                                        'mapped_to': 'N/A',
                                        'resync_age': '0d '
                                                      '0h '
                                                      '0m '
                                                      '14s',
                                        'type': 'dynamic'},
                     '0001.0000.000a': {
                        'lc_learned': 'N/A',
                                        'learned_from': 'Te0/0/1/0/3.3',
                                        'mapped_to': 'N/A',
                                        'resync_age': '0d '
                                                      '0h '
                                                      '0m '
                                                      '14s',
                                        'type': 'dynamic'},
                    '0001.0000.000b': {
                        'lc_learned': 'N/A',
                                        'learned_from': 'Te0/0/1/0/3.3',
                                        'mapped_to': 'N/A',
                                        'resync_age': '0d '
                                                      '0h '
                                                      '0m '
                                                      '14s',
                                        'type': 'dynamic'},
                    '0001.0000.000c': {
                        'lc_learned': 'N/A',
                                        'learned_from': 'Te0/0/1/0/3.3',
                                        'mapped_to': 'N/A',
                                        'resync_age': '0d '
                                                      '0h '
                                                      '0m '
                                                      '14s',
                                        'type': 'dynamic'},
                    '0001.0000.000d': {
                        'lc_learned': 'N/A',
                                        'learned_from': 'Te0/0/1/0/3.3',
                                        'mapped_to': 'N/A',
                                        'resync_age': '0d '
                                                      '0h '
                                                      '0m '
                                                      '14s',
                                        'type': 'dynamic'},
                    '0001.0000.000e': {
                        'lc_learned': 'N/A',
                                        'learned_from': 'Te0/0/1/0/3.3',
                                        'mapped_to': 'N/A',
                                        'resync_age': '0d '
                                                      '0h '
                                                      '0m '
                                                      '14s',
                                        'type': 'dynamic'},
                    '0001.0000.000f': {
                        'lc_learned': 'N/A',
                                        'learned_from': 'Te0/0/1/0/3.3',
                                        'mapped_to': 'N/A',
                                        'resync_age': '0d '
                                                      '0h '
                                                      '0m '
                                                      '14s',
                                        'type': 'dynamic'},
                    '0001.0000.0010': {
                        'lc_learned': 'N/A',
                                        'learned_from': 'Te0/0/1/0/3.3',
                                        'mapped_to': 'N/A',
                                        'resync_age': '0d '
                                                      '0h '
                                                      '0m '
                                                      '14s',
                                        'type': 'dynamic'},
                    '0001.0000.0011': {
                        'lc_learned': 'N/A',
                                        'learned_from': 'Te0/0/1/0/3.3',
                                        'mapped_to': 'N/A',
                                        'resync_age': '0d '
                                                      '0h '
                                                      '0m '
                                                      '14s',
                                        'type': 'dynamic'},
                    '0001.0000.0012': {
                        'lc_learned': 'N/A',
                                        'learned_from': 'Te0/0/1/0/3.3',
                                        'mapped_to': 'N/A',
                                        'resync_age': '0d '
                                                      '0h '
                                                      '0m '
                                                      '14s',
                                        'type': 'dynamic'},
                    '0001.0000.0013': {
                        'lc_learned': 'N/A',
                                        'learned_from': 'Te0/0/1/0/3.3',
                                        'mapped_to': 'N/A',
                                        'resync_age': '0d '
                                                      '0h '
                                                      '0m '
                                                      '14s',
                                        'type': 'dynamic'}}}}}

    golden_output = {'execute.return_value': '''
        RP/0/RP0/CPU0:ios#show l2vpn forwarding bridge-domain mac-address location 0/$
        Wed Jul 3 14:10:20.666 UTC
        To Resynchronize MAC table from the Network Processors, use the command...
        l2vpn resynchronize forwarding mac-address-table location <r/s/i>

        Mac Address Type Learned from/Filtered on LC learned Resync Age/Last Change Mapped to 
        -------------- ------- --------------------------- ---------- ---------------------- -------------- 
        0001.0000.0002 dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.0000.0003 dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.0000.0004 dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.0000.0005 dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.0000.0006 dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.0000.0007 dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.0000.0008 dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.0000.0009 dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.0000.000a dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.0000.000b dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.0000.000c dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.0000.000d dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.0000.000e dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.0000.000f dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.0000.0010 dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.0000.0011 dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.0000.0012 dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A 
        0001.0000.0013 dynamic Te0/0/1/0/3.3 N/A 0d 0h 0m 14s N/A
    '''}

    golden_parsed_output_1 = {
        'mac_table': {
            '(10.25.40.40, 10007)': {
                'mac_address': {
                    '0021.0001.0002': {
                        'lc_learned': 'N/A',
                        'learned_from': '(10.25.40.40, '
                                       '10007)',
                        'mapped_to': 'N/A',
                        'resync_age': '14 '
                                     'Mar '
                                     '12:46:04',
                        'type': 'dynamic'},
                    '1234.0001.0005': {'lc_learned': 'N/A',
                        'learned_from': '(10.25.40.40, '
                                       '10007)',
                        'mapped_to': 'N/A',
                        'resync_age': 'N/A',
                        'type': 'static'}
                }
            },
            'BD id:0': {
                'mac_address': {
                    '0021.0001.0001': {
                        'lc_learned': 'N/A',
                                      'learned_from': 'BD '
                                                      'id:0',
                                      'mapped_to': 'N/A',
                                      'resync_age': 'N/A',
                                      'type': 'EVPN'},
                    '0021.0001.0003': {'lc_learned': 'N/A',
                                      'learned_from': 'BD '
                                                      'id:0',
                                      'mapped_to': 'N/A',
                                      'resync_age': 'N/A',
                                      'type': 'EVPN'},
                    '0021.0001.0004': {'lc_learned': 'N/A',
                                      'learned_from': 'BD '
                                                      'id:0',
                                      'mapped_to': 'N/A',
                                      'resync_age': 'N/A',
                                      'type': 'EVPN'},
                    '0021.0001.0005': {'lc_learned': 'N/A',
                                      'learned_from': 'BD '
                                                      'id:0',
                                      'mapped_to': 'N/A',
                                      'resync_age': 'N/A',
                                      'type': 'EVPN'},
                    '1234.0001.0001': {'lc_learned': 'N/A',
                                      'learned_from': 'BD '
                                                      'id:0',
                                      'mapped_to': 'N/A',
                                      'resync_age': 'N/A',
                                      'type': 'EVPN'},
                    '1234.0001.0002': {'lc_learned': 'N/A',
                                      'learned_from': 'BD '
                                                      'id:0',
                                      'mapped_to': 'N/A',
                                      'resync_age': 'N/A',
                                      'type': 'EVPN'},
                    '1234.0001.0003': {'lc_learned': 'N/A',
                                      'learned_from': 'BD '
                                                      'id:0',
                                      'mapped_to': 'N/A',
                                      'resync_age': 'N/A',
                                      'type': 'EVPN'},
                    '1234.0001.0004': {'lc_learned': 'N/A',
                                      'learned_from': 'BD '
                                                      'id:0',
                                      'mapped_to': 'N/A',
                                      'resync_age': 'N/A',
                                      'type': 'EVPN'}
                }
            },
            'BE1.2': {
                'mac_address': {
                    '0021.0002.0005': {
                        'lc_learned': 'N/A',
                        'learned_from': 'BE1.2',
                        'mapped_to': 'N/A',
                        'resync_age': '14 '
                                      'Mar '
                                      '12:46:04',
                        'type': 'dynamic'},
                    '1234.0002.0004': {
                        'lc_learned': 'N/A',
                        'learned_from': 'BE1.2',
                        'mapped_to': 'N/A',
                        'resync_age': 'N/A',
                        'type': 'static'}
                }
            }
        }
    }

    golden_output_1 = {'execute.return_value': '''
        RP/0/RP0/CPU0:router# show l2vpn forwarding bridge-domain mac-address location 0
        Mac Address    Type    Learned from/Filtered on    LC learned Resync Age/Last Change Mapped to
        -------------- ------- --------------------------- ---------- ---------------------- --------------
        0021.0001.0001 EVPN    BD id: 0                    N/A        N/A                    N/A
        0021.0001.0003 EVPN    BD id: 0                    N/A        N/A                    N/A
        0021.0001.0004 EVPN    BD id: 0                    N/A        N/A                    N/A
        0021.0001.0005 EVPN    BD id: 0                    N/A        N/A                    N/A
        1234.0001.0001 EVPN    BD id: 0                    N/A        N/A                    N/A
        1234.0001.0002 EVPN    BD id: 0                    N/A        N/A                    N/A
        1234.0001.0003 EVPN    BD id: 0                    N/A        N/A                    N/A
        1234.0001.0004 EVPN    BD id: 0                    N/A        N/A                    N/A
        0021.0001.0002 dynamic (10.25.40.40, 10007)        N/A        14 Mar 12:46:04        N/A
        1234.0001.0005 static  (10.25.40.40, 10007)        N/A        N/A                    N/A
        0021.0002.0005 dynamic BE1.2                       N/A        14 Mar 12:46:04        N/A
        1234.0002.0004 static  BE1.2                       N/A        N/A                    N/A
    '''}

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowL2vpnForwardingBridgeDomainMacAddress(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_empty(self):
        self.device = Mock(**self.empty_output)
        obj = ShowL2vpnForwardingBridgeDomainMacAddress(device=self.device)
        with self.assertRaises(TypeError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowL2vpnForwardingBridgeDomainMacAddress(device=self.device)
        parsed_output = obj.parse(location=0)
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_1)
        obj = ShowL2vpnForwardingBridgeDomainMacAddress(device=self.device)
        parsed_output = obj.parse(location=0, bridge_domain=0)
        self.assertEqual(parsed_output, self.golden_parsed_output_1)

if __name__ == '__main__':
    unittest.main()
