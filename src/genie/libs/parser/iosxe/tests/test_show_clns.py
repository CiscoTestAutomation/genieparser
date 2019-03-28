# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
                                             SchemaMissingKeyError

# Parser
from genie.libs.parser.iosxe.show_clns import ShowClnsInterface

# =========================================================
# Parser for 'show clns interface'
#            'show show clns interface <inteface>'
# =========================================================
class test_show_ip_interface(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'interface':{
            'GigabitEthernet1':{
                'status':'up',
                'line_protocol': 'up',
                'clns_protocol_processing_enabled': False,
            },
            'GigabitEthernet2': {
                'status': 'up',
                'line_protocol': 'up',
                'clns_protocol_processing_enabled': True,
                'erpdus_enabled': True,
                'min_interval_msec': 10,
                'clns_fast_switching_enabled': True,
                'clns_sse_switching_enabled': False,
                'dec_compatibility_mode': 'OFF',
                'next_esh_ish_in': 20,
                'routing_protocol': {
                    'IS-IS': {
                        'test': {
                           'level_type': 'level-1-2',
                            'interface_number': '0x1',
                            'local_circuit_id': '0x1',
                            'neighbor_extended_local_circuit_id': '0x0',
                            'hello_interval':{
                                'level-1': {
                                    'metric': 10,
                                    'dr_id': 'R2.01',
                                    'curcuit_id': 'R2.01',
                                    'ipv6_metric': 10,
                                    'interval_msec': 1000,
                                } ,
                                'level-2': {
                                    'metric': 10,
                                    'dr_id': '0000.0000.0000.00',
                                    'curcuit_id': 'R2.01',
                                    'ipv6_metric': 10,
                                    'interval_msec': 654,
                                },
                            },
                            'priority':{
                                'level-1':{
                                    'priority': 64,
                                },
                                'level-2': {
                                    'priority': 64,
                                },
                            } ,
                            'adjacencies':{
                                'level-1': {
                                    'usage': 1
                                },
                                'level-2': {
                                    'usage': 0
                                },
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output = {'execute.return_value': '''\
    R2#show clns interface
    GigabitEthernet1 is up, line protocol is up
      CLNS protocol processing disabled
    GigabitEthernet2 is up, line protocol is up
      Checksums enabled, MTU 1497, Encapsulation SAP
      ERPDUs enabled, min. interval 10 msec.
      CLNS fast switching enabled
      CLNS SSE switching disabled
      DEC compatibility mode OFF for this interface
      Next ESH/ISH in 20 seconds
      Routing Protocol: IS-IS (test)
        Circuit Type: level-1-2
        Interface number 0x1, local circuit ID 0x1
        Neighbor Extended Local Circuit ID: 0x0
        Level-1 Metric: 10, Priority: 64, Circuit ID: R2.01
        DR ID: R2.01
        Level-1 IPv6 Metric: 10
        Number of active level-1 adjacencies: 1
        Level-2 Metric: 10, Priority: 64, Circuit ID: R2.01
        DR ID: 0000.0000.0000.00
        Level-2 IPv6 Metric: 10
        Number of active level-2 adjacencies: 0
        Next IS-IS LAN Level-1 Hello in 1 seconds
        Next IS-IS LAN Level-2 Hello in 645 milliseconds
    '''}

    golden_output_2 = {'execute.return_value': '''\
        R2#show clns interface
        GigabitEthernet3 is up, line protocol is up
          Checksums enabled, MTU 1497, Encapsulation SAP
          ERPDUs enabled, min. interval 10 msec.
          CLNS fast switching enabled
          CLNS SSE switching disabled
          DEC compatibility mode OFF for this interface
          Next ESH/ISH in 14 seconds
          Routing Protocol: IS-IS (test)
            Circuit Type: level-1-2
            Interface number 0x2, local circuit ID 0x2
            Neighbor Extended Local Circuit ID: 0x0
            Level-1 Metric: 10, Priority: 64, Circuit ID: R2.02
            DR ID: 0000.0000.0000.00
            Level-1 IPv6 Metric: 10
            Number of active level-1 adjacencies: 0
            Level-2 Metric: 10, Priority: 64, Circuit ID: R3.07
            DR ID: R3.07
            Level-2 IPv6 Metric: 10
            Number of active level-2 adjacencies: 1
            Next IS-IS LAN Level-1 Hello in 8 seconds
            Next IS-IS LAN Level-2 Hello in 1 seconds
        GigabitEthernet4 is up, line protocol is up
          Checksums enabled, MTU 1497, Encapsulation SAP
          ERPDUs enabled, min. interval 10 msec.
          CLNS fast switching enabled
          CLNS SSE switching disabled
          DEC compatibility mode OFF for this interface
          Next ESH/ISH in 40 seconds
          Routing Protocol: IS-IS (VRF1)
            Circuit Type: level-1-2
            Interface number 0x1, local circuit ID 0x1
            Neighbor Extended Local Circuit ID: 0x0
            Level-1 Metric: 10, Priority: 64, Circuit ID: R2.01
            DR ID: 0000.0000.0000.00
            Level-1 IPv6 Metric: 10
            Number of active level-1 adjacencies: 0
            Level-2 Metric: 10, Priority: 64, Circuit ID: R2.01
            DR ID: R2.01
            Level-2 IPv6 Metric: 10
            Number of active level-2 adjacencies: 1
            Next IS-IS LAN Level-1 Hello in 5 seconds
            Next IS-IS LAN Level-2 Hello in 663 milliseconds
        Loopback0 is up, line protocol is up
          Checksums enabled, MTU 1514, Encapsulation LOOPBACK
          ERPDUs enabled, min. interval 10 msec.
          CLNS fast switching disabled
          CLNS SSE switching disabled
          DEC compatibility mode OFF for this interface
          Next ESH/ISH in 25 seconds
          Routing Protocol: IS-IS (test)
            Circuit Type: level-1-2
            Interface number 0x0, local circuit ID 0x7
            Neighbor Extended Local Circuit ID: 0x0
            Level-1 Metric: 10, Priority: 64, Circuit ID: R2.07
            Level-1 IPv6 Metric: 10
            Number of active level-1 adjacencies: 0
            Level-2 Metric: 10, Priority: 64, Circuit ID: R2.07
            Level-2 IPv6 Metric: 10
            Number of active level-2 adjacencies: 0
            Next IS-IS Hello in 0 seconds
            if state DOWN
        Loopback1 is up, line protocol is up
          Checksums enabled, MTU 1514, Encapsulation LOOPBACK
          ERPDUs enabled, min. interval 10 msec.
          CLNS fast switching disabled
          CLNS SSE switching disabled
          DEC compatibility mode OFF for this interface
          Next ESH/ISH in 49 seconds
          Routing Protocol: IS-IS (VRF1)
            Circuit Type: level-1-2
            Interface number 0x0, local circuit ID 0x8
            Neighbor Extended Local Circuit ID: 0x0
            Level-1 Metric: 10, Priority: 64, Circuit ID: R2.08
            Level-1 IPv6 Metric: 10
            Number of active level-1 adjacencies: 0
            Level-2 Metric: 10, Priority: 64, Circuit ID: R2.08
            Level-2 IPv6 Metric: 10
            Number of active level-2 adjacencies: 0
            Next IS-IS Hello in 0 seconds
            if state DOWN

        '''}
    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowIpRipDatabase(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_clns_interface(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowClnsInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)


# =========================================================
# Parser for 'show clns interface'
#            'show show clns interface <inteface>'
# =========================================================
class test_show_ip_interface(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'interface':{
            'GigabitEthernet1':{
                'status':'up',
                'line_protocol': 'up',
                'clns_protocol_processing_enabled': False,
            },
            'GigabitEthernet2': {
                'status': 'up',
                'line_protocol': 'up',
                'clns_protocol_processing_enabled': True,
                'erpdus_enabled': True,
                'min_interval_msec': 10,
                'clns_fast_switching_enabled': True,
                'clns_sse_switching_enabled': False,
                'dec_compatibility_mode': 'OFF',
                'next_esh_ish_in': 20,
                'routing_protocol': {
                    'IS-IS': {
                        'test': {
                           'level_type': 'level-1-2',
                            'interface_number': '0x1',
                            'local_circuit_id': '0x1',
                            'neighbor_extended_local_circuit_id': '0x0',
                            'hello_interval':{
                                'level-1': {
                                    'metric': 10,
                                    'dr_id': 'R2.01',
                                    'curcuit_id': 'R2.01',
                                    'ipv6_metric': 10,
                                    'interval_msec': 1000,
                                } ,
                                'level-2': {
                                    'metric': 10,
                                    'dr_id': '0000.0000.0000.00',
                                    'curcuit_id': 'R2.01',
                                    'ipv6_metric': 10,
                                    'interval_msec': 654,
                                },
                            },
                            'priority':{
                                'level-1':{
                                    'priority': 64,
                                },
                                'level-2': {
                                    'priority': 64,
                                },
                            } ,
                            'adjacencies':{
                                'level-1': {
                                    'usage': 1
                                },
                                'level-2': {
                                    'usage': 0
                                },
                            }
                        }
                    }
                }
            }
        }
    }

    golden_output = {'execute.return_value': '''\
    R2#show clns interface
    GigabitEthernet1 is up, line protocol is up
      CLNS protocol processing disabled
    GigabitEthernet2 is up, line protocol is up
      Checksums enabled, MTU 1497, Encapsulation SAP
      ERPDUs enabled, min. interval 10 msec.
      CLNS fast switching enabled
      CLNS SSE switching disabled
      DEC compatibility mode OFF for this interface
      Next ESH/ISH in 20 seconds
      Routing Protocol: IS-IS (test)
        Circuit Type: level-1-2
        Interface number 0x1, local circuit ID 0x1
        Neighbor Extended Local Circuit ID: 0x0
        Level-1 Metric: 10, Priority: 64, Circuit ID: R2.01
        DR ID: R2.01
        Level-1 IPv6 Metric: 10
        Number of active level-1 adjacencies: 1
        Level-2 Metric: 10, Priority: 64, Circuit ID: R2.01
        DR ID: 0000.0000.0000.00
        Level-2 IPv6 Metric: 10
        Number of active level-2 adjacencies: 0
        Next IS-IS LAN Level-1 Hello in 1 seconds
        Next IS-IS LAN Level-2 Hello in 645 milliseconds
    '''}

    golden_output_2 = {'execute.return_value': '''\
        R2#show clns interface
        GigabitEthernet3 is up, line protocol is up
          Checksums enabled, MTU 1497, Encapsulation SAP
          ERPDUs enabled, min. interval 10 msec.
          CLNS fast switching enabled
          CLNS SSE switching disabled
          DEC compatibility mode OFF for this interface
          Next ESH/ISH in 14 seconds
          Routing Protocol: IS-IS (test)
            Circuit Type: level-1-2
            Interface number 0x2, local circuit ID 0x2
            Neighbor Extended Local Circuit ID: 0x0
            Level-1 Metric: 10, Priority: 64, Circuit ID: R2.02
            DR ID: 0000.0000.0000.00
            Level-1 IPv6 Metric: 10
            Number of active level-1 adjacencies: 0
            Level-2 Metric: 10, Priority: 64, Circuit ID: R3.07
            DR ID: R3.07
            Level-2 IPv6 Metric: 10
            Number of active level-2 adjacencies: 1
            Next IS-IS LAN Level-1 Hello in 8 seconds
            Next IS-IS LAN Level-2 Hello in 1 seconds
        GigabitEthernet4 is up, line protocol is up
          Checksums enabled, MTU 1497, Encapsulation SAP
          ERPDUs enabled, min. interval 10 msec.
          CLNS fast switching enabled
          CLNS SSE switching disabled
          DEC compatibility mode OFF for this interface
          Next ESH/ISH in 40 seconds
          Routing Protocol: IS-IS (VRF1)
            Circuit Type: level-1-2
            Interface number 0x1, local circuit ID 0x1
            Neighbor Extended Local Circuit ID: 0x0
            Level-1 Metric: 10, Priority: 64, Circuit ID: R2.01
            DR ID: 0000.0000.0000.00
            Level-1 IPv6 Metric: 10
            Number of active level-1 adjacencies: 0
            Level-2 Metric: 10, Priority: 64, Circuit ID: R2.01
            DR ID: R2.01
            Level-2 IPv6 Metric: 10
            Number of active level-2 adjacencies: 1
            Next IS-IS LAN Level-1 Hello in 5 seconds
            Next IS-IS LAN Level-2 Hello in 663 milliseconds
        Loopback0 is up, line protocol is up
          Checksums enabled, MTU 1514, Encapsulation LOOPBACK
          ERPDUs enabled, min. interval 10 msec.
          CLNS fast switching disabled
          CLNS SSE switching disabled
          DEC compatibility mode OFF for this interface
          Next ESH/ISH in 25 seconds
          Routing Protocol: IS-IS (test)
            Circuit Type: level-1-2
            Interface number 0x0, local circuit ID 0x7
            Neighbor Extended Local Circuit ID: 0x0
            Level-1 Metric: 10, Priority: 64, Circuit ID: R2.07
            Level-1 IPv6 Metric: 10
            Number of active level-1 adjacencies: 0
            Level-2 Metric: 10, Priority: 64, Circuit ID: R2.07
            Level-2 IPv6 Metric: 10
            Number of active level-2 adjacencies: 0
            Next IS-IS Hello in 0 seconds
            if state DOWN
        Loopback1 is up, line protocol is up
          Checksums enabled, MTU 1514, Encapsulation LOOPBACK
          ERPDUs enabled, min. interval 10 msec.
          CLNS fast switching disabled
          CLNS SSE switching disabled
          DEC compatibility mode OFF for this interface
          Next ESH/ISH in 49 seconds
          Routing Protocol: IS-IS (VRF1)
            Circuit Type: level-1-2
            Interface number 0x0, local circuit ID 0x8
            Neighbor Extended Local Circuit ID: 0x0
            Level-1 Metric: 10, Priority: 64, Circuit ID: R2.08
            Level-1 IPv6 Metric: 10
            Number of active level-1 adjacencies: 0
            Level-2 Metric: 10, Priority: 64, Circuit ID: R2.08
            Level-2 IPv6 Metric: 10
            Number of active level-2 adjacencies: 0
            Next IS-IS Hello in 0 seconds
            if state DOWN

        '''}
    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowIpRipDatabase(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_clns_interface(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowClnsInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)