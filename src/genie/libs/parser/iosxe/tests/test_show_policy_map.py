# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxe show_monitor
from genie.libs.parser.iosxe.show_policy_map import ShowPolicyMap,\
                                                    ShowPolicyMapControlPlane,\
                                                    ShowPolicyMapInterface,\
                                                    ShowPolicyMapInterfaceInput,\
                                                    ShowPolicyMapInterfaceOutput,\
                                                    ShowPolicyMapInterfaceClass,\
                                                    ShowPolicyMapTargetClass

# ====================================================================
# Unit test for :
#   * 'show policy-map interface {interface} input class {class_name}',
#   * 'show policy-map interface {interface} output class {class_name}',
#   * 'show policy-map interface {interface} input',
#   * 'show policy-map interface {interface} output',
#   * 'show policy-map interface {interface}',
#   * 'show policy-map interface class {class_name}',
#   * 'show policy-map target service-group {num}',
#   * 'show policy-map control-plane'
#   * 'show policy-map interface',
# =====================================================================


class test_show_policy_map_type(unittest.TestCase):
    ''' Unit test for
           * 'show policy-map interface {interface} input class {class_name}',
           * 'show policy-map interface {interface} output class {class_name}',
           * 'show policy-map interface {interface} input',
           * 'show policy-map interface {interface} output',
           * 'show policy-map interface {interface}',
           * 'show policy-map interface class {class_name}',
           * 'show policy-map target service-group {num}',
           * 'show policy-map control-plane'
           * 'show policy-map interface',
    '''

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'Control Plane': {
            'service_policy': {
                'input': {
                    'policy_name': {
                        'Control_Plane_In': {
                            'class_map': {
                                'Ping_Class': {
                                    'match_evaluation': 'match-all',
                                    'packets': 0,
                                    'bytes': 0,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0,
                                        'drop_rate_bps': 0},
                                    'match': ['access-group name Ping_Option'],
                                    'police': {
                                        'cir_bps': 8000,
                                        'cir_bc_bytes': 1500,
                                        'conformed': {
                                            'packets': 0,
                                            'bytes': 0,
                                            'actions': {"drop": True},
                                            'bps': 0},
                                        'exceeded': {
                                            'packets': 0,
                                            'bytes': 0,
                                            'actions': {"drop": True},
                                            'bps': 0}}},
                                'TELNET_Class': {
                                    'match_evaluation': 'match-all',
                                    'packets': 0,
                                    'bytes': 0,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0,
                                        'drop_rate_bps': 0},
                                    'match': ['access-group name TELNET_Permit'],
                                    'police': {
                                        'cir_bps': 8000,
                                        'cir_bc_bytes': 1500,
                                        'conformed': {
                                            'packets': 0,
                                            'bytes': 0,
                                            'actions': {"drop": True},
                                            'bps': 0},
                                        'exceeded': {
                                            'packets': 0,
                                            'bytes': 0,
                                            'actions': {"drop": True},
                                            'bps': 0}}},
                                'TACACS_Class': {
                                    'match_evaluation': 'match-all',
                                    'packets': 0,
                                    'bytes': 0,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0,
                                        'drop_rate_bps': 0},
                                    'match': ['access-group name TACACS_Permit'],
                                    'police': {
                                        'cir_bps': 8000,
                                        'cir_bc_bytes': 1500,
                                        'conformed': {
                                            'packets': 0,
                                            'bytes': 0,
                                            'actions': {"drop": True},
                                            'bps': 0},
                                        'exceeded': {
                                            'packets': 0,
                                            'bytes': 0,
                                            'actions': {"drop": True},
                                            'bps': 0}}},
                                'SNMP_Class': {
                                    'match_evaluation': 'match-all',
                                    'packets': 0,
                                    'bytes': 0,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0,
                                        'drop_rate_bps': 0},
                                    'match': ['access-group name SNMP_Permit'],
                                    'police': {
                                        'cir_bps': 8000,
                                        'cir_bc_bytes': 1500,
                                        'conformed': {
                                            'packets': 0,
                                            'bytes': 0,
                                            'actions': {"drop": True},
                                            'bps': 0},
                                        'exceeded': {
                                            'packets': 0,
                                            'bytes': 0,
                                            'actions': {"drop": True},
                                            'bps': 0}}},
                                'FTP_Class': {
                                    'match_evaluation': 'match-all',
                                    'packets': 0,
                                    'bytes': 0,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0,
                                        'drop_rate_bps': 0},
                                    'match': ['access-group name FTP_Permit'],
                                    'police': {
                                        'cir_bps': 8000,
                                        'cir_bc_bytes': 1500,
                                        'conformed': {
                                            'packets': 0,
                                            'bytes': 0,
                                            'actions': {"drop": True},
                                            'bps': 0},
                                        'exceeded': {
                                            'packets': 0,
                                            'bytes': 0,
                                            'actions': {"drop": True},
                                            'bps': 0}}},
                                'BGP_Class': {
                                    'match_evaluation': 'match-all',
                                    'packets': 32,
                                    'bytes': 2032,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0,
                                        'drop_rate_bps': 0},
                                    'match': ['access-group name BGP_Permit'],
                                    'qos_set': {
                                        'ip precedence': {
                                            '6': {
                                                'marker_statistics': 'Disabled'}}}},
                                'OSPF_Class': {
                                    'match_evaluation': 'match-all',
                                    'packets': 58,
                                    'bytes': 11788,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0,
                                        'drop_rate_bps': 0},
                                    'match': ['access-group name OSPF_Permit'],
                                    'qos_set': {
                                        'ip precedence': {
                                            '6': {
                                                'marker_statistics': 'Disabled'}}}},
                                'LDP_Class': {
                                    'match_evaluation': 'match-all',
                                    'packets': 128,
                                    'bytes': 9552,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0,
                                        'drop_rate_bps': 0},
                                    'match': ['access-group name LDP_Permit'],
                                    'qos_set': {
                                        'ip precedence': {
                                            '6': {
                                                'marker_statistics': 'Disabled'}}}},
                                'ICMP_Class1': {
                                    'match_evaluation': 'match-all',
                                    'packets': 0,
                                    'bytes': 0,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0,
                                        'drop_rate_bps': 0},
                                    'match': ['access-group name ICMP_Permit1'],
                                    'police': {
                                        'cir_bps': 8000,
                                        'cir_bc_bytes': 1500,
                                        'conformed': {
                                            'packets': 0,
                                            'bytes': 0,
                                            'actions': {"drop": True},
                                            'bps': 0},
                                        'exceeded': {
                                            'packets': 0,
                                            'bytes': 0,
                                            'actions': {"drop": True},
                                            'bps': 0}}},
                                'ICMP_Class2': {
                                    'match_evaluation': 'match-all',
                                    'packets': 4,
                                    'bytes': 482,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0,
                                        'drop_rate_bps': 0},
                                    'match': ['access-group name ICMP_Permit2'],
                                    'police': {
                                        'cir_bps': 12000000,
                                        'cir_bc_bytes': 150000,
                                        'conformed': {
                                            'packets': 4,
                                            'bytes': 482,
                                            'actions': {"transmit": True},
                                            'bps': 0},
                                        'exceeded': {
                                            'packets': 0,
                                            'bytes': 0,
                                            'actions': {"drop": True},
                                            'bps': 0}}},
                                'NTP_Class': {
                                    'match_evaluation': 'match-all',
                                    'packets': 3,
                                    'bytes': 330,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0,
                                        'drop_rate_bps': 0},
                                    'match': ['access-group name NTP_Permit'],
                                    'police': {
                                        'cir_bps': 8000,
                                        'cir_bc_bytes': 1500,
                                        'conformed': {
                                            'packets': 3,
                                            'bytes': 330,
                                            'actions': {"drop": True},
                                            'bps': 0},
                                        'exceeded': {
                                            'packets': 0,
                                            'bytes': 0,
                                            'actions': {"drop": True},
                                            'bps': 0}}},
                                'ALL_Class': {
                                    'match_evaluation': 'match-all',
                                    'packets': 23,
                                    'bytes': 1548,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0,
                                        'drop_rate_bps': 0},
                                    'match': ['access-group name ALL_Permit'],
                                    'police': {
                                        'cir_bps': 200000,
                                        'cir_bc_bytes': 15000,
                                        'conformed': {
                                            'packets': 23,
                                            'bytes': 1548,
                                            'actions': {"transmit": True},
                                            'bps': 0},
                                        'exceeded': {
                                            'packets': 0,
                                            'bytes': 0,
                                            'actions': {"drop": True},
                                            'bps': 0}}},
                                'class-default': {
                                    'match_evaluation': 'match-any',
                                    'packets': 276,
                                    'bytes': 16554,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0,
                                        'drop_rate_bps': 0},
                                    'match': ['any']}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        Router#show policy-map control-plane
        Load for five secs: 29%/0%; one minute: 7%; five minutes: 6%
        Time source is NTP, .17:46:23.484 EST Mon Oct 31 2016

        Control Plane 

        Service-policy input: Control_Plane_In

            Class-map: Ping_Class (match-all)  
                0 packets, 0 bytes
                5 minute offered rate 0000 bps, drop rate 0000 bps
                Match: access-group name Ping_Option
                police:
                    cir 8000 bps, bc 1500 bytes
                    conformed 0 packets, 0 bytes; actions:
                        drop 
                    exceeded 0 packets, 0 bytes; actions:
                        drop 
                    conformed 0000 bps, exceeded 0000 bps

            Class-map: TELNET_Class (match-all)  
                0 packets, 0 bytes
                5 minute offered rate 0000 bps, drop rate 0000 bps
                Match: access-group name TELNET_Permit
                police:
                    cir 8000 bps, bc 1500 bytes
                    conformed 0 packets, 0 bytes; actions:
                        drop 
                    exceeded 0 packets, 0 bytes; actions:
                        drop 
                    conformed 0000 bps, exceeded 0000 bps

            Class-map: TACACS_Class (match-all)  
                0 packets, 0 bytes
                5 minute offered rate 0000 bps, drop rate 0000 bps
                Match: access-group name TACACS_Permit
                police:
                    cir 8000 bps, bc 1500 bytes
                    conformed 0 packets, 0 bytes; actions:
                        drop 
                    exceeded 0 packets, 0 bytes; actions:
                        drop 
                    conformed 0000 bps, exceeded 0000 bps

            Class-map: SNMP_Class (match-all)  
                0 packets, 0 bytes
                5 minute offered rate 0000 bps, drop rate 0000 bps
                Match: access-group name SNMP_Permit
                police:
                      cir 8000 bps, bc 1500 bytes
                    conformed 0 packets, 0 bytes; actions:
                      drop 
                    exceeded 0 packets, 0 bytes; actions:
                      drop 
                    conformed 0000 bps, exceeded 0000 bps
           
            Class-map: FTP_Class (match-all)  
                0 packets, 0 bytes
                5 minute offered rate 0000 bps, drop rate 0000 bps
                Match: access-group name FTP_Permit
                police:
                      cir 8000 bps, bc 1500 bytes
                    conformed 0 packets, 0 bytes; actions:
                      drop 
                    exceeded 0 packets, 0 bytes; actions:
                      drop 
                    conformed 0000 bps, exceeded 0000 bps
           
            Class-map: BGP_Class (match-all)  
                32 packets, 2032 bytes
                5 minute offered rate 0000 bps, drop rate 0000 bps
                Match: access-group name BGP_Permit
                QoS Set
                    ip precedence 6
                    Marker statistics: Disabled
             
            Class-map: OSPF_Class (match-all)  
                58 packets, 11788 bytes
                5 minute offered rate 0000 bps, drop rate 0000 bps
                Match: access-group name OSPF_Permit
                QoS Set
                    ip precedence 6
                    Marker statistics: Disabled
           
            Class-map: LDP_Class (match-all)  
                128 packets, 9552 bytes
                5 minute offered rate 0000 bps, drop rate 0000 bps
                Match: access-group name LDP_Permit
                QoS Set
                    ip precedence 6
                    Marker statistics: Disabled
           
            Class-map: ICMP_Class1 (match-all)  
                0 packets, 0 bytes
                5 minute offered rate 0000 bps, drop rate 0000 bps
                Match: access-group name ICMP_Permit1
                police:
                    cir 8000 bps, bc 1500 bytes
                    conformed 0 packets, 0 bytes; actions:
                        drop 
                    exceeded 0 packets, 0 bytes; actions:
                        drop 
                    conformed 0000 bps, exceeded 0000 bps
           
            Class-map: ICMP_Class2 (match-all)  
                4 packets, 482 bytes
                5 minute offered rate 0000 bps, drop rate 0000 bps
                Match: access-group name ICMP_Permit2
                police:
                    cir 12000000 bps, bc 150000 bytes
                    conformed 4 packets, 482 bytes; actions:
                        transmit 
                    exceeded 0 packets, 0 bytes; actions:
                        drop 
                    conformed 0000 bps, exceeded 0000 bps
        
            Class-map: NTP_Class (match-all)  
                3 packets, 330 bytes
                5 minute offered rate 0000 bps, drop rate 0000 bps
                Match: access-group name NTP_Permit
                police:
                    cir 8000 bps, bc 1500 bytes
                    conformed 3 packets, 330 bytes; actions:
                        drop 
                    exceeded 0 packets, 0 bytes; actions:
                        drop 
                    conformed 0000 bps, exceeded 0000 bps
           
            Class-map: ALL_Class (match-all)  
                23 packets, 1548 bytes
                5 minute offered rate 0000 bps, drop rate 0000 bps
                Match: access-group name ALL_Permit
                police:
                    cir 200000 bps, bc 15000 bytes
                    conformed 23 packets, 1548 bytes; actions:
                        transmit 
                    exceeded 0 packets, 0 bytes; actions:
                        drop 
                    conformed 0000 bps, exceeded 0000 bps
           
            Class-map: class-default (match-any)  
                276 packets, 16554 bytes
                5 minute offered rate 0000 bps, drop rate 0000 bps
                Match: any 
            Router# '''}

    golden_parsed_output2 = {
        'Control Plane': {
            'service_policy': {
                'input': {
                    'policy_name': {
                        'TEST': {
                            'class_map': {
                                'TEST': {
                                    'match_evaluation': 'match-all',
                                    'packets': 20,
                                    'bytes': 11280,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0,
                                        'drop_rate_bps': 0},
                                    'match': ['access-group 101'],
                                    'police': {
                                        'police_bps': 8000,
                                        'police_limit': 1500,
                                        'extended_limit': 1500,
                                        'conformed': {
                                            'packets': 15,
                                            'bytes': 6210,
                                            'actions': {"transmit": True},
                                            'bps': 0},
                                        'exceeded': {
                                            'packets': 5,
                                            'bytes': 5070,
                                            'actions': {"drop": True},
                                            'bps': 0},
                                        'violated': {
                                            'packets': 0,
                                            'bytes': 0,
                                            'actions': {"drop": True},
                                            'bps': 0}}},
                                'class-default': {
                                    'match_evaluation': 'match-any',
                                    'packets': 105325,
                                    'bytes': 11415151,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0,
                                        'drop_rate_bps': 0},
                                    'match': ['any']}}}}}}}}

    golden_output2 = {'execute.return_value': '''
        Device# show policy-map control-plane

        Control Plane
        Service-policy input:TEST
        Class-map:TEST (match-all)
            20 packets, 11280 bytes
            5 minute offered rate 0 bps, drop rate 0 bps
            Match:access-group 101
            police:
                8000 bps, 1500 limit, 1500 extended limit
                conformed 15 packets, 6210 bytes; action:transmit
                exceeded 5 packets, 5070 bytes; action:drop
                violated 0 packets, 0 bytes; action:drop
                conformed 0 bps, exceed 0 bps, violate 0 bps
        Class-map:class-default (match-any)
            105325 packets, 11415151 bytes
            5 minute offered rate 0 bps, drop rate 0 bps
            Match:any
        '''}

    golden_parsed_output3 = {
        'Control Plane': {
            'service_policy': {
                'input': {
                    'policy_name': {
                        'control-plane-in': {
                            'class_map': {
                                'telnet-class': {
                                    'match_evaluation': 'match-all',
                                    'packets': 10521,
                                    'bytes': 673344,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 18000,
                                        'drop_rate_bps': 15000},
                                    'match': ['access-group 102'],
                                    'police': {
                                        'cir_bps': 64000,
                                        'cir_bc_bytes': 8000,
                                        'conformed': {
                                            'packets': 1430,
                                            'bytes': 91520,
                                            'actions': {"transmit": True},
                                            'bps': 2000},
                                        'exceeded': {
                                            'packets': 9091,
                                            'bytes': 581824,
                                            'actions': {"drop": True},
                                            'bps': 15000}}},
                                'class-default': {
                                    'match_evaluation': 'match-any',
                                    'packets': 0,
                                    'bytes': 0,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0,
                                        'drop_rate_bps': 0},
                                    'match': ['any']}}}}}}}}

    golden_output3 = {'execute.return_value': '''
        Router# show policy-map control-plane
        Control Plane
        Service-policy input: control-plane-in
        Class-map: telnet-class (match-all)
            10521 packets, 673344 bytes
            5 minute offered rate 18000 bps, drop rate 15000 bps
            Match: access-group 102
            police:  cir 64000 bps, bc 8000 bytes
               conformed 1430 packets, 91520 bytes; actions:
               transmit
               exceeded 9091 packets, 581824 bytes; actions:
               drop
               conformed 2000 bps, exceeded 15000 bps
        Class-map: class-default (match-any)
            0 packets, 0 bytes
            5 minute offered rate 0000 bps, drop rate 0000 bps
            Match: any

    '''}

    golden_parsed_output4 = {
        'Control Plane': {
            'service_policy': {
                'input': {
                    'policy_name': {
                        'copp-ftp': {
                            'class_map': {
                                'copp-ftp': {
                                    'match_evaluation': 'match-any',
                                    'packets': 2234,
                                    'bytes': 223400,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0,
                                        'drop_rate_bps': 0},
                                    'match': ['access-group name copp-ftp'],
                                    'police': {
                                        'cir_bps': 10000000,
                                        'cir_be_bytes': 312500,
                                        'conformed': {
                                            'packets': 2234,
                                            'bytes': 223400,
                                            'actions': {"transmit": True},
                                            'bps': 0},
                                        'exceeded': {
                                            'packets': 0,
                                            'bytes': 0,
                                            'actions': {"drop": True},
                                            'bps': 0}}},
                                'class-default': {
                                    'match_evaluation': 'match-any',
                                    'packets': 0,
                                    'bytes': 0,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0,
                                        'drop_rate_bps': 0},
                                    'match': ['any']}}},
                        'control-plane-in': {
                            'class_map': {
                                'telnet-class': {
                                    'match_evaluation': 'match-all',
                                    'packets': 10521,
                                    'bytes': 673344,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 18000,
                                        'drop_rate_bps': 15000},
                                    'match': ['access-group 102'],
                                    'police': {
                                        'cir_bps': 64000,
                                        'cir_bc_bytes': 8000,
                                        'conformed': {
                                            'packets': 1430,
                                            'bytes': 91520,
                                            'actions': {"transmit": True},
                                            'bps': 2000},
                                        'exceeded': {
                                            'packets': 9091,
                                            'bytes': 581824,
                                            'actions': {"drop": True},
                                            'bps': 15000}}},
                                'class-default': {
                                    'match_evaluation': 'match-any',
                                    'packets': 0,
                                    'bytes': 0,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0,
                                        'drop_rate_bps': 0},
                                    'match': ['any']}}}}}}}}

    golden_output4 = {'execute.return_value': '''
        Router# show policy-map control-plane
        Control Plane

        Service-policy input: copp-ftp

        Class-map: copp-ftp (match-any)
            2234 packets, 223400 bytes
            5 minute offered rate 0000 bps, drop rate 0000 bps
            Match: access-group name copp-ftp
            police:
            cir 10000000 bps, be 312500 bytes
            conformed 2234 packets, 223400 bytes; actions:
            transmit
            exceeded 0 packets, 0 bytes; actions:
            drop
            conformed 0000 bps, exceeded 0000 bps

        Class-map: class-default (match-any)
            0 packets, 0 bytes
            5 minute offered rate 0000 bps, drop rate 0000 bps
            Match: any
           
        Control Plane
        Service-policy input: control-plane-in
        Class-map: telnet-class (match-all)
            10521 packets, 673344 bytes
            5 minute offered rate 18000 bps, drop rate 15000 bps
            Match: access-group 102
            police:  cir 64000 bps, bc 8000 bytes
            conformed 1430 packets, 91520 bytes; actions:
            transmit
            exceeded 9091 packets, 581824 bytes; actions:
            drop
            conformed 2000 bps, exceeded 15000 bps
        Class-map: class-default (match-any)
            0 packets, 0 bytes
            5 minute offered rate 0000 bps, drop rate 0000 bps
            Match: any

    '''}

    golden_parsed_output5 = {
        'GigabitEthernet0/0/0': {
            'service_policy': {
                'output': {
                    'policy_name': {
                        'CORE-Out': {
                            'class_map': {
                                'EXP0': {
                                    'match_evaluation': 'match-all',
                                    'packets': 0,
                                    'bytes': 0,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0},
                                    'match': ['mpls experimental topmost 0']},
                                'EXP1': {
                                    'match_evaluation': 'match-all',
                                    'packets': 0,
                                    'bytes': 0,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0},
                                    'match': ['mpls experimental topmost 1']},
                                'EXP2': {
                                    'match_evaluation': 'match-all',
                                    'packets': 0,
                                    'bytes': 0,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0},
                                    'match': ['mpls experimental topmost 2']},
                                'EXP3': {
                                    'match_evaluation': 'match-all',
                                    'packets': 0,
                                    'bytes': 0,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0},
                                    'match': ['mpls experimental topmost 3']},
                                'EXP4': {
                                    'match_evaluation': 'match-all',
                                    'packets': 0,
                                    'bytes': 0,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0},
                                    'match': ['mpls experimental topmost 4']},
                                'EXP5': {
                                    'match_evaluation': 'match-all',
                                    'packets': 0,
                                    'bytes': 0,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0},
                                    'match': ['mpls experimental topmost 5']},
                                'EXP6': {
                                    'match_evaluation': 'match-all',
                                    'packets': 27,
                                    'bytes': 1869,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0},
                                    'match': ['mpls experimental topmost 6']},
                                'EXP7': {
                                    'match_evaluation': 'match-all',
                                    'packets': 0,
                                    'bytes': 0,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0},
                                    'match': ['mpls experimental topmost 7']},
                                'class-default': {
                                    'match_evaluation': 'match-any',
                                    'packets': 193,
                                    'bytes': 19600,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0,
                                        'drop_rate_bps': 0},
                                    'match': ['any']}}}}}}}}

    golden_output5 = {'execute.return_value': '''
        Router#show policy-map interface gigabitEthernet 0/0/0
        Load for five secs: 1%/0%; one minute: 4%; five minutes: 5%
        Time source is NTP, 14:58:52.473 EST Fri Oct 28 2016

        GigabitEthernet0/0/0 

        Service-policy output: CORE-Out

        Class-map: EXP0 (match-all)  
            0 packets, 0 bytes
            5 minute offered rate 0000 bps
            Match: mpls experimental topmost 0 

        Class-map: EXP1 (match-all)  
            0 packets, 0 bytes
            5 minute offered rate 0000 bps
            Match: mpls experimental topmost 1 

        Class-map: EXP2 (match-all)  
            0 packets, 0 bytes
            5 minute offered rate 0000 bps
            Match: mpls experimental topmost 2 

        Class-map: EXP3 (match-all)  
            0 packets, 0 bytes
            5 minute offered rate 0000 bps
            Match: mpls experimental topmost 3 

        Class-map: EXP4 (match-all)  
            0 packets, 0 bytes
            5 minute offered rate 0000 bps
            Match: mpls experimental topmost 4 

        Class-map: EXP5 (match-all)  
            0 packets, 0 bytes
            5 minute offered rate 0000 bps
            Match: mpls experimental topmost 5 

        Class-map: EXP6 (match-all)  
            27 packets, 1869 bytes
            5 minute offered rate 0000 bps
            Match: mpls experimental topmost 6 

        Class-map: EXP7 (match-all)  
            0 packets, 0 bytes
            5 minute offered rate 0000 bps
            Match: mpls experimental topmost 7 

        Class-map: class-default (match-any)  
            193 packets, 19600 bytes
            5 minute offered rate 0000 bps, drop rate 0000 bps
            Match: any 
    Router#    '''}

    golden_parsed_output6 = {
        'serial3/1': {
            'service_policy': {
                'output': {
                    'policy_name': {
                        'pol': {
                            'class_map': {
                                'silver': {
                                    'match_evaluation': 'match-all',
                                    'packets': 366,
                                    'bytes': 87840,
                                    'rate': {
                                        'interval': 30,
                                        'offered_rate_bps': 15000,
                                        'drop_rate_bps': 300},
                                    'match': ['ip precedence 1'],
                                    'queueing': True,
                                    'output_queue': 'Conversation 266',
                                    'bandwidth_percent': 10,
                                    'pkts_matched': 363,
                                    'bytes_matched': 87120,
                                    'queue_depth': 147,
                                    'total_drops': 38,
                                    'no_buffer_drops': 0,
                                    'random_detect': {
                                        'exponential_weight': '9',
                                        'mean_queue_depth': 25920,
                                        'class': {
                                            '0': {
                                                'transmitted': '0/0',
                                                'random_drop': '0/0',
                                                'tail_drop': '0/0',
                                                'minimum_thresh': '20000',
                                                'maximum_thresh': '40000',
                                                'mark_prob': '1/10'},
                                            '1': {
                                                'transmitted': '328/78720',
                                                'random_drop': '38/9120',
                                                'tail_drop': '0/0',
                                                'minimum_thresh': '22000',
                                                'maximum_thresh': '40000',
                                                'mark_prob': '1/10'},
                                            '2': {
                                                'transmitted': '0/0',
                                                'random_drop': '0/0',
                                                'tail_drop': '0/0',
                                                'minimum_thresh': '24000',
                                                'maximum_thresh': '40000',
                                                'mark_prob': '1/10'},
                                            '3': {
                                                'transmitted': '0/0',
                                                'random_drop': '0/0',
                                                'tail_drop': '0/0',
                                                'minimum_thresh': '26000',
                                                'maximum_thresh': '40000',
                                                'mark_prob': '1/10'},
                                            '4': {
                                                'transmitted': '0/0',
                                                'random_drop': '0/0',
                                                'tail_drop': '0/0',
                                                'minimum_thresh': '28000',
                                                'maximum_thresh': '40000',
                                                'mark_prob': '1/10'}}},
                                    'policy': {
                                        'wred-policy': {
                                            'class': {
                                                'prec2': {
                                                    'bandwidth': 1000,
                                                    'random_detect': {
                                                        'precedence': [2],
                                                        'bytes1': [100],
                                                        'bytes2': [200],
                                                        'bytes3': [10]}},
                                                'class-default': {
                                                    'random_detect': {
                                                        'precedence': [4, 6],
                                                        'bytes1': [150, 200],
                                                        'bytes2': [300, 400],
                                                        'bytes3': [15, 5]}}}}}}}}}}}},
        'Ethernet0/0/1': {
            'service_policy': {
                'output': {
                    'policy_name': {
                        'wred-policy (1177)': {
                            'class_map': {
                                'prec2': {
                                    'match_evaluation': 'match-all 1178/10',
                                    'packets': 0,
                                    'bytes': 0,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0,
                                        'drop_rate_bps': 0},
                                    'match': ['ip precedence 2  (1179)'],
                                    'queueing': True,
                                    'queue_limit_bytes': 62500,
                                    'queue_depth': 0,
                                    'total_drops': 0,
                                    'no_buffer_drops': 0,
                                    'pkts_queued': 0,
                                    'bytes_queued': 0,
                                    'bandwidth_kbps': 1000,
                                    'random_detect': {
                                        'exp_weight_constant': '9 (1/512)',
                                        'mean_queue_depth': 0,
                                        'class': {
                                            '0': {
                                                'transmitted': '0/0',
                                                'random_drop': '0/0',
                                                'tail_drop': '0/0',
                                                'minimum_thresh': '15625',
                                                'maximum_thresh': '31250',
                                                'mark_prob': '1/10'},
                                            '1': {
                                                'transmitted': '0/0',
                                                'random_drop': '0/0',
                                                'tail_drop': '0/0',
                                                'minimum_thresh': '17578',
                                                'maximum_thresh': '31250',
                                                'mark_prob': '1/10'},
                                            '2': {
                                                'transmitted': '0/0',
                                                'random_drop': '0/0',
                                                'tail_drop': '0/0',
                                                'minimum_thresh': '100',
                                                'maximum_thresh': '200',
                                                'mark_prob': '1/10'},
                                            '3': {
                                                'transmitted': '0/0',
                                                'random_drop': '0/0',
                                                'tail_drop': '0/0',
                                                'minimum_thresh': '21484',
                                                'maximum_thresh': '31250',
                                                'mark_prob': '1/10'},
                                            '4': {
                                                'transmitted': '0/0',
                                                'random_drop': '0/0',
                                                'tail_drop': '0/0',
                                                'minimum_thresh': '23437',
                                                'maximum_thresh': '31250',
                                                'mark_prob': '1/10'},
                                            '5': {
                                                'transmitted': '0/0',
                                                'random_drop': '0/0',
                                                'tail_drop': '0/0',
                                                'minimum_thresh': '25390',
                                                'maximum_thresh': '31250',
                                                'mark_prob': '1/10'},
                                            '6': {
                                                'transmitted': '0/0',
                                                'random_drop': '0/0',
                                                'tail_drop': '0/0',
                                                'minimum_thresh': '27343',
                                                'maximum_thresh': '31250',
                                                'mark_prob': '1/10'},
                                            '7': {
                                                'transmitted': '0/0',
                                                'random_drop': '0/0',
                                                'tail_drop': '0/0',
                                                'minimum_thresh': '29296',
                                                'maximum_thresh': '31250',
                                                'mark_prob': '1/10'}}}},
                                'class-default': {
                                    'match_evaluation': 'match-any 1182/0',
                                    'packets': 0,
                                    'bytes': 0,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0,
                                        'drop_rate_bps': 0},
                                    'match': ['any  (1183)'],
                                    'queue_limit_bytes': 562500,
                                    'queue_depth': 0,
                                    'total_drops': 0,
                                    'no_buffer_drops': 0,
                                    'pkts_queued': 0,
                                    'bytes_queued': 0,
                                    'random_detect': {
                                        'exp_weight_constant': '9 (1/512)',
                                        'mean_queue_depth': 0,
                                        'class': {
                                            '0': {
                                                'transmitted': '0/0',
                                                'random_drop': '0/0',
                                                'tail_drop': '0/0',
                                                'minimum_thresh': '140625',
                                                'maximum_thresh': '281250',
                                                'mark_prob': '1/10'},
                                            '1': {
                                                'transmitted': '0/0',
                                                'random_drop': '0/0',
                                                'tail_drop': '0/0',
                                                'minimum_thresh': '158203',
                                                'maximum_thresh': '281250',
                                                'mark_prob': '1/10'},
                                            '2': {
                                                'transmitted': '0/0',
                                                'random_drop': '0/0',
                                                'tail_drop': '0/0',
                                                'minimum_thresh': '175781',
                                                'maximum_thresh': '281250',
                                                'mark_prob': '1/10'},
                                            '3': {
                                                'transmitted': '0/0',
                                                'random_drop': '0/0',
                                                'tail_drop': '0/0',
                                                'minimum_thresh': '193359',
                                                'maximum_thresh': '281250',
                                                'mark_prob': '1/10'},
                                            '4': {
                                                'transmitted': '0/0',
                                                'random_drop': '0/0',
                                                'tail_drop': '0/0',
                                                'minimum_thresh': '150',
                                                'maximum_thresh': '300',
                                                'mark_prob': '1/15'},
                                            '5': {
                                                'transmitted': '0/0',
                                                'random_drop': '0/0',
                                                'tail_drop': '0/0',
                                                'minimum_thresh': '228515',
                                                'maximum_thresh': '281250',
                                                'mark_prob': '1/10'},
                                            '6': {
                                                'transmitted': '0/0',
                                                'random_drop': '0/0',
                                                'tail_drop': '0/0',
                                                'minimum_thresh': '200',
                                                'maximum_thresh': '400',
                                                'mark_prob': '1/5'},
                                            '7': {
                                                'transmitted': '0/0',
                                                'random_drop': '0/0',
                                                'tail_drop': '0/0',
                                                'minimum_thresh': '263671',
                                                'maximum_thresh': '281250',
                                                'mark_prob': '1/10'}}}}}}}}}}}

    golden_output6 = {'execute.return_value': '''
        Router# show policy-map interface
        serial3/1
        Service-policy output: pol
        Class-map: silver (match-all)
            366 packets, 87840 bytes
            30 second offered rate 15000 bps, drop rate 300 bps
            Match: ip precedence 1
            Queueing
            Output Queue: Conversation 266
            Bandwidth 10 (%)
            (pkts matched/bytes matched) 363/87120
            depth/total drops/no-buffer drops) 147/38/0
            exponential weight: 9
            mean queue depth: 25920
            class     Transmitted       Random drop      Tail drop     Minimum Maximum Mark
                      pkts/bytes        pkts/bytes       pkts/bytes    thresh  thresh  prob
                                                                       (bytes)  (bytes)
            0             0/0               0/0               0/0      20000    40000  1/10
            1           328/78720          38/9120            0/0      22000    40000  1/10
            2             0/0               0/0               0/0      24000    40000  1/10
            3             0/0               0/0               0/0      26000    40000  1/10
            4             0/0               0/0               0/0      28000    40000  1/10

            policy wred-policy
                class prec2
                    bandwidth 1000
                    random-detect
                    random-detect precedence 2 100 bytes 200 bytes 10
                class class-default
                    random-detect
                    random-detect precedence 4 150 bytes 300 bytes 15
                    random-detect precedence 6 200 bytes 400 bytes 5
        
        Ethernet0/0/1
        Service-policy output: wred-policy (1177)
        Class-map: prec2 (match-all) (1178/10)
            0 packets, 0 bytes
            5 minute offered rate 0 bps, drop rate 0 bps
            Match: ip precedence 2  (1179)
            Queueing
            queue limit 62500 bytes
            (queue depth/total drops/no-buffer drops) 0/0/0
            (pkts queued/bytes queued) 0/0
            bandwidth 1000 (kbps)
            Exp-weight-constant: 9 (1/512)
            Mean queue depth: 0 bytes
            class     Transmitted       Random drop      Tail drop Minimum        Maximum     Mark
                      pkts/bytes        pkts/bytes       pkts/bytes thresh         thresh     prob
                                                                     bytes         bytes
            0             0/0               0/0              0/0     15625         31250     1/10
            1             0/0               0/0              0/0     17578         31250     1/10
            2             0/0               0/0              0/0       100           200     1/10
            3             0/0               0/0              0/0     21484         31250     1/10
            4             0/0               0/0              0/0     23437         31250     1/10
            5             0/0               0/0              0/0     25390         31250     1/10
            6             0/0               0/0              0/0     27343         31250     1/10
            7             0/0               0/0              0/0     29296         31250     1/10
        Class-map: class-default (match-any) (1182/0)
            0 packets, 0 bytes
            5 minute offered rate 0 bps, drop rate 0 bps
            Match: any  (1183)
            0 packets, 0 bytes
            5 minute rate 0 bps
            queue limit 562500 bytes
            (queue depth/total drops/no-buffer drops) 0/0/0
            (pkts queued/bytes queued) 0/0
            Exp-weight-constant: 9 (1/512)
            Mean queue depth: 0 bytes
            class     Transmitted       Random drop      Tail drop Minimum        Maximum     Mark
                      pkts/bytes        pkts/bytes       pkts/bytes thresh         thresh     prob
                                                                     bytes         bytes
            0             0/0               0/0              0/0     140625        281250     1/10
            1             0/0               0/0              0/0     158203        281250     1/10
            2             0/0               0/0              0/0     175781        281250     1/10
            3             0/0               0/0              0/0     193359        281250     1/10
            4             0/0               0/0              0/0        150           300     1/15
            5             0/0               0/0              0/0     228515        281250     1/10
            6             0/0               0/0              0/0        200           400     1/5
            7             0/0               0/0              0/0     263671        281250     1/10
            
    '''}

    golden_parsed_output7 = {
        'FastEthernet4/1/1': {
            'service_policy': {
                'input': {
                    'policy_name': {
                        'mypolicy': {
                            'class_map': {
                                'class1': {
                                    'match_evaluation': 'match-all',
                                    'packets': 500,
                                    'bytes': 125000,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 4000,
                                        'drop_rate_bps': 0},
                                    'match': ['packet length min 100 max 300'],
                                    'qos_set': {
                                        'qos-group': {
                                            '20': {
                                                'packets_marked': 500}}}}}}}}}}}

    golden_output7 = {'execute.return_value': '''
        Router# show policy-map interface
        FastEthernet4/1/1
            Service-policy input: mypolicy
                Class-map: class1 (match-all)
                    500 packets, 125000 bytes
                    5 minute offered rate 4000 bps, drop rate 0 bps
                    Match: packet length min 100 max 300
                    QoS Set
                        qos-group 20
                            Packets marked 500
        '''}

    golden_parsed_output8 = {
        'TenGigabitEthernet0/0/2': {
            'service_policy': {
                'output': {
                    'policy_name': {
                        'shape_priority': {
                            'queue_stats_for_all_priority_classes': {
                                'priority_level': {
                                    '1': {
                                        'queueing': True,
                                        'queue_limit_us': 3932,
                                        'queue_limit_bytes': 49152,
                                        'queue_depth': 49476,
                                        'total_drops': 44577300,
                                        'no_buffer_drops': 0,
                                        'pkts_output': 2348138,
                                        'bytes_output': 1202246656},
                                    '2': {
                                        'queueing': True,
                                        'queue_limit_us': 1966,
                                        'queue_limit_bytes': 49152,
                                        'queue_depth': 51072,
                                        'total_drops': 42228358,
                                        'no_buffer_drops': 0,
                                        'pkts_output': 4697080,
                                        'bytes_output': 2404904960}}},
                            'class_map': {
                                'class_priority': {
                                    'match_evaluation': 'match-any',
                                    'packets': 46925438,
                                    'bytes': 24025824256,
                                    'rate': {'interval': 30,
                                             'offered_rate_bps': 1871849000,
                                             'drop_rate_bps': 1778171000},
                                    'match': ['cos  1', 'cos  2'],
                                    'priority': {
                                        'percent': 10,
                                        'kbps': 100000,
                                        'burst_bytes': 2500000,
                                        'exceed_drops': 44577300},
                                    'priority_level': 1},
                                'class_priority_level2': {
                                    'match_evaluation': 'match-any',
                                    'packets': 46925438,
                                    'bytes': 24025824256,
                                    'rate': {
                                        'interval': 30,
                                        'offered_rate_bps': 1871849000,
                                        'drop_rate_bps': 1684485000},
                                    'match': ['cos  3', 'cos  4'],
                                    'priority': {
                                        'percent': 20,
                                        'kbps': 200000,
                                        'burst_bytes': 5000000,
                                        'exceed_drops': 42228358},
                                    'priority_level': 2},
                                'class_bw': {
                                    'match_evaluation': 'match-any',
                                    'packets': 23462719,
                                    'bytes': 12012912128,
                                    'rate': {
                                        'interval': 30,
                                        'offered_rate_bps': 935925000,
                                        'drop_rate_bps': 281045000},
                                    'match': ['cos  5'],
                                    'queueing': True,
                                    'queue_limit_us': 393,
                                    'queue_limit_bytes': 49152,
                                    'queue_depth': 49476,
                                    'total_drops': 7045085,
                                    'no_buffer_drops': 0,
                                    'pkts_output': 16417634,
                                    'bytes_output': 8405828608,
                                    'bandwidth_remaining_percent': 70},
                                'class-default': {
                                    'match_evaluation': 'match-any',
                                    'packets': 0,
                                    'bytes': 0,
                                    'rate': {
                                        'interval': 30,
                                        'offered_rate_bps': 0,
                                        'drop_rate_bps': 0},
                                    'match': ['any'],
                                    'queue_limit_us': 393,
                                    'queue_limit_bytes': 49152,
                                    'queue_depth': 0,
                                    'total_drops': 0,
                                    'no_buffer_drops': 0,
                                    'pkts_output': 0,
                                    'bytes_output': 0}}}}}}}}

    golden_output8 = {'execute.return_value': '''
        Device# show policy-map interface TenGigabitEthernet0/0/2
            show policy-map interface TenGigabitEthernet0/0/2
            TenGigabitEthernet0/0/2

                Service-policy output: shape_priority

                    queue stats for all priority classes:
                        Queueing
                        priority level 1
                        queue limit 3932 us/ 49152 bytes
                        (queue depth/total drops/no-buffer drops) 49476/44577300/0
                        (pkts output/bytes output) 2348138/1202246656

                    queue stats for all priority classes:
                        Queueing
                        priority level 2
                        queue limit 1966 us/ 49152 bytes
                        (queue depth/total drops/no-buffer drops) 51072/42228358/0
                        (pkts output/bytes output) 4697080/2404904960

                    Class-map: class_priority (match-any)
                        46925438 packets, 24025824256 bytes
                        30 second offered rate 1871849000 bps, drop rate 1778171000 bps
                        Match: cos  1
                        Match: cos  2
                        Priority: 10% (100000 kbps), burst bytes 2500000, b/w exceed drops: 44577300

                        Priority Level: 1

                    Class-map: class_priority_level2 (match-any)
                        46925438 packets, 24025824256 bytes
                        30 second offered rate 1871849000 bps, drop rate 1684485000 bps
                        Match: cos  3
                        Match: cos  4
                        Priority: 20% (200000 kbps), burst bytes 5000000, b/w exceed drops: 42228358
                
                        Priority Level: 2

                    Class-map: class_bw (match-any)
                        23462719 packets, 12012912128 bytes
                        30 second offered rate 935925000 bps, drop rate 281045000 bps
                        Match: cos  5
                        Queueing
                        queue limit 393 us/ 49152 bytes
                        (queue depth/total drops/no-buffer drops) 49476/7045085/0
                        (pkts output/bytes output) 16417634/8405828608
                        bandwidth remaining 70%

                    Class-map: class-default (match-any)
                        0 packets, 0 bytes
                        30 second offered rate 0000 bps, drop rate 0000 bps
                        Match: any
                  
                        queue limit 393 us/ 49152 bytes
                        (queue depth/total drops/no-buffer drops) 0/0/0
                        (pkts output/bytes output) 0/0
    '''}

    golden_parsed_output9 = {
        'GigabitEthernet0/0/1': {
            'service_policy': {
                'input': {
                    'policy_name': {
                        'TEST': {
                            'class_map': {
                                'class-default': {
                                    'match_evaluation': 'match-any',
                                    'packets': 0,
                                    'bytes': 0,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0,
                                        'drop_rate_bps': 0},
                                    'match': ['any']}}}}},
                'output': {
                    'policy_name': {
                        'TEST2': {
                            'class_map': {
                                'class-default': {
                                    'match_evaluation': 'match-any',
                                    'packets': 0,
                                    'bytes': 0,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0,
                                        'drop_rate_bps': 0},
                                    'match': ['any']}}}}}}}}

    golden_output9 = {'execute.return_value': '''
            PE1#show policy-map interface GigabitEthernet0/0/1

            Load for five secs: 3%/0%; one minute: 3%; five minutes: 2%
            Time source is NTP, 17:47:15.313 EST Tue Apr 9 2019

            GigabitEthernet0/0/1

                Service-policy input: TEST

                    Class-map: class-default (match-any)
                        0 packets, 0 bytes
                        5 minute offered rate 0000 bps, drop rate 0000 bps
                        Match: any

                Service-policy output: TEST2

                    Class-map: class-default (match-any)
                        0 packets, 0 bytes
                        5 minute offered rate 0000 bps, drop rate 0000 bps
                        Match: any      '''}

    golden_parsed_output10 = {
        'GigabitEthernet0/1/1': {
            'service_policy': {
                'output': {
                    'policy_name': {
                        'shape-out': {
                            'class_map': {
                                'class-default': {
                                    'bytes': 0,
                                    'bytes_output': 0,
                                    'match': ['any'],
                                    'match_evaluation': 'match-any',
                                    'no_buffer_drops': 0,
                                    'packets': 0,
                                    'pkts_output': 0,
                                    'queue_depth': 0,
                                    'queue_limit_packets': '64',
                                    'queueing': True,
                                    'rate': {
                                        'drop_rate_bps': 0,
                                        'interval': 300,
                                        'offered_rate_bps': 0},
                                    'shape_bc_bps': 2000,
                                    'shape_be_bps': 2000,
                                    'shape_cir_bps': 500000,
                                    'shape_type': 'average',
                                    'target_shape_rate': 500000,
                                    'total_drops': 0}}}}}}}}

    golden_output10 = {'execute.return_value': '''
        Router#show policy-map interface gigabitEthernet 0/1/1 output class class-default
        Load for five secs: 11%/0%; one minute: 5%; five minutes: 5%
        Time source is NTP, 22:21:45.748 EST Fri Nov 4 2016

        GigabitEthernet0/1/1 

            Service-policy output: shape-out

                Class-map: class-default (match-any)  
                    0 packets, 0 bytes
                    5 minute offered rate 0000 bps, drop rate 0000 bps
                    Match: any 
                    Queueing
                    queue limit 64 packets
                    (queue depth/total drops/no-buffer drops) 0/0/0
                    (pkts output/bytes output) 0/0
                    shape (average) cir 500000, bc 2000, be 2000
                    target shape rate 500000
    '''}

    golden_parsed_output11 = {
        'TenGigabitEthernet0/3/0.41': {
            'service_policy': {
                'output': {
                    'policy_name': {
                        'VLAN51_QoS': {
                            'class_map': {
                                'VLAN51_QoS': {
                                    'match_evaluation': 'match-all',
                                    'packets': 0,
                                    'bytes': 0,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0,
                                        'drop_rate_bps': 0},
                                    'match': ['access-group name VLAN51_QoS'],
                                    'queueing': True,
                                    'queue_limit_packets': '64',
                                    'queue_depth': 0,
                                    'total_drops': 0,
                                    'no_buffer_drops': 0,
                                    'pkts_output': 0,
                                    'bytes_output': 0,
                                    'shape_type': 'average',
                                    'shape_cir_bps': 80000,
                                    'shape_bc_bps': 320,
                                    'shape_be_bps': 0,
                                    'target_shape_rate': 80000,
                                    'police': {
                                        'conformed': {
                                            'packets': 0,
                                            'bytes': 0,
                                            'actions': {"transmit": True},
                                            'bps': 0},
                                        'exceeded': {
                                            'packets': 0,
                                            'bytes': 0,
                                            'actions': {"transmit": True},
                                            'bps': 0},
                                        'violated': {
                                            'packets': 0,
                                            'bytes': 0,
                                            'actions': {"drop": True},
                                            'bps': 0}}},
                                'class-default': {
                                    'match_evaluation': 'match-any',
                                    'packets': 0,
                                    'bytes': 0,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0,
                                        'drop_rate_bps': 0},
                                    'match': ['any'],
                                    'queue_limit_packets': '41666',
                                    'queue_depth': 0,
                                    'total_drops': 0,
                                    'no_buffer_drops': 0,
                                    'pkts_output': 0,
                                    'bytes_output': 0}}}}}}}}

    golden_output11 = {'execute.return_value': '''
        PE1#show policy-map interface TenGigabitEthernet 0/3/0.41 output

        Load for five secs: 2%/0%; one minute: 2%; five minutes: 2%
        Time source is NTP, 17:42:14.490 EST Tue Apr 9 2019
        
        TenGigabitEthernet0/3/0.41

            Service-policy output: VLAN51_QoS

                Class-map: VLAN51_QoS (match-all)
                    0 packets, 0 bytes
                    5 minute offered rate 0000 bps, drop rate 0000 bps
                    Match: access-group name VLAN51_QoS
                    Queueing
                    queue limit 64 packets
                    (queue depth/total drops/no-buffer drops) 0/0/0
                    (pkts output/bytes output) 0/0
                    shape (average) cir 80000, bc 320, be 0
                    target shape rate 80000
                    police:
                        cir 8000000 bps, bc 4000 bytes, be 1000 bytes
                        conformed 0 packets, 0 bytes; actions:
                            transmit
                        exceeded 0 packets, 0 bytes; actions:
                            transmit
                        violated 0 packets, 0 bytes; actions:
                             drop
                        conformed 0000 bps, exceeded 0000 bps, violated 0000 bps

                Class-map: class-default (match-any)
                    0 packets, 0 bytes
                    5 minute offered rate 0000 bps, drop rate 0000 bps
                    Match: any
            
                    queue limit 41666 packets
                    (queue depth/total drops/no-buffer drops) 0/0/0
                    (pkts output/bytes output) 0/0
        PE1# '''}

    golden_parsed_output12 = {
        'GigabitEthernet0/1/4': {
            'service_policy': {
                'input': {
                    'policy_name': {
                        'police-in': {
                            'class_map': {
                                'class-default': {
                                    'bytes': 0,
                                    'match': ['any'],
                                    'match_evaluation': 'match-any',
                                    'packets': 0,
                                    'police': {
                                        'cir_bc_bytes': 83619,
                                        'cir_bps': 445500,
                                        'conformed': {
                                            'actions': {"transmit": True},
                                            'bps': 0,
                                            'bytes': 0,
                                            'packets': 0},
                                        'exceeded': {
                                            'actions': {"drop": True},
                                            'bps': 0,
                                            'bytes': 0,
                                            'packets': 0}},
                                    'rate': {
                                        'drop_rate_bps': 0,
                                        'interval': 300,
                                        'offered_rate_bps': 0}}}}}}}}}

    golden_output12 = {'execute.return_value': '''
            show policy-map interface gigabitEthernet 0/1/4 input class class-default
            Load for five secs: 1%/0%; one minute: 3%; five minutes: 3%
            Time source is NTP, 12:22:26.378 EST Wed Oct 26 2016

            GigabitEthernet0/1/4 

                Service-policy input: police-in

                    Class-map: class-default (match-any)  
                        0 packets, 0 bytes
                        5 minute offered rate 0000 bps, drop rate 0000 bps
                        Match: any 
                        police:
                            cir 445500 bps, bc 83619 bytes
                            conformed 0 packets, 0 bytes; actions:
                              transmit 
                            exceeded 0 packets, 0 bytes; actions:
                              drop 
                            conformed 0000 bps, exceeded 0000 bps
        Router#'''}

    golden_parsed_output13 = {
        'GigabitEthernet0/0/1': {
            'service_policy': {
                'input': {
                    'policy_name': {
                        'TEST': {
                            'class_map': {
                                'class-default': {
                                    'match_evaluation': 'match-any',
                                    'packets': 0,
                                    'bytes': 0,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0,
                                        'drop_rate_bps': 0},
                                    'match': ['any']}}}}}}}}

    golden_output13 = {'execute.return_value': '''
            PE1#show policy-map interface GigabitEthernet 0/0/1 input

            Load for five secs: 2%/0%; one minute: 2%; five minutes: 2%
            Time source is NTP, 17:41:12.649 EST Tue Apr 9 2019

            GigabitEthernet0/0/1

                Service-policy input: TEST

                    Class-map: class-default (match-any)
                        0 packets, 0 bytes
                        5 minute offered rate 0000 bps, drop rate 0000 bps
                        Match: any
            PE1# '''}

    golden_parsed_output14 = {
        'GigabitEthernet0/0/1': {
            'service_policy': {
                'input': {
                    'policy_name': {
                        'TEST': {}}},
                'output': {
                    'policy_name': {
                        'TEST2': {}}}}},
        'TenGigabitEthernet0/3/0.41': {
            'service_policy': {
                'output': {
                    'policy_name': {
                        'VLAN51_QoS': {}}}}}}

    golden_output14 = {'execute.return_value': '''
        PE1#show policy-map interface class TEST2

        Load for five secs: 4%/0%; one minute: 2%; five minutes: 2%
        Time source is NTP, 18:05:19.663 EST Tue Apr 9 2019

        GigabitEthernet0/0/1

            Service-policy input: TEST

            Service-policy output: TEST2
        TenGigabitEthernet0/3/0.41

            Service-policy output: VLAN51_QoS
        PE1# '''}

    golden_parsed_output15 = {
        'GigabitEthernet0/0/1': {
            'service_policy': {
                'input': {
                    'policy_name': {
                        'TEST': {}}},
                'output': {
                    'policy_name': {
                        'TEST2': {}}}}},
        'TenGigabitEthernet0/3/0.41': {
            'service_policy': {
                'output': {
                    'policy_name': {
                        'VLAN51_QoS': {
                            'class_map': {
                                'VLAN51_QoS': {
                                    'match_evaluation': 'match-all',
                                    'packets': 0,
                                    'bytes': 0,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0,
                                        'drop_rate_bps': 0},
                                    'match': ['access-group name VLAN51_QoS'],
                                    'queueing': True,
                                    'queue_limit_packets': '64',
                                    'queue_depth': 0,
                                    'total_drops': 0,
                                    'no_buffer_drops': 0,
                                    'pkts_output': 0,
                                    'bytes_output': 0,
                                    'shape_type': 'average',
                                    'shape_cir_bps': 80000,
                                    'shape_bc_bps': 320,
                                    'shape_be_bps': 0,
                                    'target_shape_rate': 80000,
                                    'police': {
                                        'conformed': {
                                            'packets': 0,
                                            'bytes': 0,
                                            'actions': {"transmit": True},
                                            'bps': 0},
                                        'exceeded': {
                                            'packets': 0,
                                            'bytes': 0,
                                            'actions': {"transmit": True},
                                            'bps': 0},
                                        'violated': {
                                            'packets': 0,
                                            'bytes': 0,
                                            'actions': {"drop": True},
                                            'bps': 0}}}}}}}}}}

    golden_output15 = {'execute.return_value': '''
        PE1#show policy-map interface class VLAN51_QoS

        Load for five secs: 4%/0%; one minute: 3%; five minutes: 2%
        Time source is NTP, 18:05:52.025 EST Tue Apr 9 2019

        GigabitEthernet0/0/1

            Service-policy input: TEST

            Service-policy output: TEST2
        TenGigabitEthernet0/3/0.41

            Service-policy output: VLAN51_QoS

                Class-map: VLAN51_QoS (match-all)
                    0 packets, 0 bytes
                    5 minute offered rate 0000 bps, drop rate 0000 bps
                    Match: access-group name VLAN51_QoS
                    Queueing
                    queue limit 64 packets
                    (queue depth/total drops/no-buffer drops) 0/0/0
                    (pkts output/bytes output) 0/0
                    shape (average) cir 80000, bc 320, be 0
                    target shape rate 80000
                    police:
                        cir 8000000 bps, bc 4000 bytes, be 1000 bytes
                        conformed 0 packets, 0 bytes; actions:
                            transmit
                        exceeded 0 packets, 0 bytes; actions:
                            transmit
                        violated 0 packets, 0 bytes; actions:
                            drop
                        conformed 0000 bps, exceeded 0000 bps, violated 0000 bps
        PE1# '''}

    golden_parsed_output16 = {
        'Port-channel1': {
            'service_group': 1,
            'service_policy': {
                'output': {
                    'policy_name': {
                        'VLAN51_QoS': {
                            'class_map': {
                                'VLAN51_QoS': {
                                    'match_evaluation': 'match-all',
                                    'packets': 30,
                                    'bytes': 13638,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 1000,
                                        'drop_rate_bps': 1000},
                                    'match': ['access-group name VLAN51_QoS'],
                                    'police': {
                                        'cir_bps': 8000,
                                        'cir_bc_bytes': 1000,
                                        'conformed': {
                                            'packets': 22,
                                            'bytes': 1494,
                                            'actions': {"transmit": True},
                                            'bps': 0},
                                        'exceeded': {
                                            'packets': 8,
                                            'bytes': 12144,
                                            'actions': {"drop": True},
                                            'bps': 1000}}},
                                'class-default': {
                                    'match_evaluation': 'match-any',
                                    'packets': 0,
                                    'bytes': 0,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0,
                                        'drop_rate_bps': 0},
                                    'match': ['any']}}}}}}}}

    golden_output16 = {'execute.return_value': '''
            Router#show policy-map target service-group 1
            Load for five secs: 98%/0%; one minute: 98%; five minutes: 96%
            Time source is NTP, 18:59:17.791 EST Wed Nov 9 2016

                Port-channel1: Service Group 1

                Service-policy output: VLAN51_QoS

                    Class-map: VLAN51_QoS (match-all)
                        30 packets, 13638 bytes
                        5 minute offered rate 1000 bps, drop rate 1000 bps
                        Match: access-group name VLAN51_QoS
                        police:
                            cir 8000 bps, bc 1000 bytes
                            conformed 22 packets, 1494 bytes; actions:
                            transmit
                            exceeded 8 packets, 12144 bytes; actions:
                            drop
                            conformed 0000 bps, exceeded 1000 bps

                    Class-map: class-default (match-any)
                        0 packets, 0 bytes
                        5 minute offered rate 0000 bps, drop rate 0000 bps
                        Match: any
            '''}

    golden_parsed_output17 = {
        'GigabitEthernet9/5: Service Group 1': {
            'service_policy': {
                'input': {
                    'policy_name': {
                        'policy1': {
                            'class_map': {
                                'class-default': {
                                    'match_evaluation': 'match-any',
                                    'packets': 0,
                                    'bytes': 0,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0,
                                        'drop_rate_bps': 0},
                                    'match': ['any'],
                                    'police': {
                                        'cir_bps': 200000,
                                        'cir_bc_bytes': 6250,
                                        'conformed': {
                                            'packets': 0,
                                            'bytes': 0,
                                            'actions': {"transmit": True},
                                            'bps': 0},
                                        'exceeded': {
                                            'packets': 0,
                                            'bytes': 0,
                                            'actions': {"drop": True},
                                            'bps': 0}}}}}}},
                'output': {
                    'policy_name': {
                        'policy2': {
                            'class_map': {
                                'class-default': {
                                    'match_evaluation': 'match-any',
                                    'packets': 0,
                                    'bytes': 0,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0,
                                        'drop_rate_bps': 0},
                                    'match': ['any'],
                                    'queueing': True,
                                    'queue_limit_packets': '131072',
                                    'queue_depth': 0,
                                    'total_drops': 0,
                                    'no_buffer_drops': 0,
                                    'pkts_output': 0,
                                    'bytes_output': 0,
                                    'bandwidth': 'remaining ratio 2'}}}}}}}}

    golden_output17 = {'execute.return_value': '''
        Device# show policy-map target service-group 1

 GigabitEthernet9/5: Service Group 1

  Service-policy input: policy1

    Class-map: class-default (match-any)
      0 packets, 0 bytes
      5 minute offered rate 0000 bps, drop rate 0000 bps
      Match: any
      police:
          cir 200000 bps, bc 6250 bytes
        conformed 0 packets, 0 bytes; actions:
          transmit
        exceeded 0 packets, 0 bytes; actions:
          drop
        conformed 0000 bps, exceed 0000 bps

  Service-policy output: policy2

  Counters last updated 00:00:34 ago
    Class-map: class-default (match-any)
      0 packets, 0 bytes
      5 minute offered rate 0000 bps, drop rate 0000 bps
      Match: any
      Queueing
      queue limit 131072 packets
      (queue depth/total drops/no-buffer drops) 0/0/0
      (pkts output/bytes output) 0/0
      bandwidth remaining ratio 2
    '''}

    golden_parsed_output18 = {"TenGigabitEthernet0/0/0.101": {
        "service_policy": {
            "input": {
                "policy_name": {
                    "L3VPN_in": {
                        "class_map": {
                            "class-default": {
                                "match_evaluation": "match-any",
                                "packets": 0,
                                "bytes": 0,
                                "rate": {
                                    "interval": 300,
                                    "offered_rate_bps": 0,
                                    "drop_rate_bps": 0
                                },
                                "match": [
                                    "any"
                                ],
                                "police": {
                                    "cir_bps": 400000,
                                    "cir_bc_bytes": 400000,
                                    "conformed": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {
                                            "transmit": True
                                        },
                                        "bps": 0
                                    },
                                    "exceeded": {
                                        "packets": 0,
                                        "bytes": 0,
                                        "actions": {
                                            "drop": True
                                        },
                                        "bps": 0
                                    }
                                }
                            }
                        },
                        'child_policy_name': {
                            "STD_in_child": {
                                "class_map": {
                                    "IPP567": {
                                        "match_evaluation": "match-all",
                                        "packets": 0,
                                        "bytes": 0,
                                        "rate": {
                                            "interval": 300,
                                            "offered_rate_bps": 0,
                                            "drop_rate_bps": 0
                                        },
                                        "match": [
                                            "ip precedence 3  4  5"
                                        ],
                                        "qos_set": {
                                            "ip precedence": {
                                                "1": {
                                                    "marker_statistics": "Disabled"
                                                }
                                            },
                                            "qos-group": {
                                                "1": {
                                                    "marker_statistics": "Disabled"
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    },
                }
            },
            "output": {
                "policy_name": {
                    "L3VPN_out": {
                        "class_map": {
                            "class-default": {
                                "match_evaluation": "match-any",
                                "packets": 2121212,
                                "bytes": 121212,
                                "rate": {
                                    "interval": 300,
                                    "offered_rate_bps": 11111171,
                                    "drop_rate_bps": 1118111
                                },
                                "match": [
                                    "any"
                                ],
                                "queueing": True,
                                "queue_limit_packets": "512",
                                "queue_depth": 0,
                                "total_drops": 11111,
                                "no_buffer_drops": 0,
                                "pkts_output": 11511,
                                "bytes_output": 111611,
                                "shape_type": "average",
                                "shape_cir_bps": 111222,
                                "shape_bc_bps": 2323,
                                "shape_be_bps": 3434,
                                "target_shape_rate": 454545
                            }
                        },
                        'child_policy_name': {
                            "leeaf": {
                                "queue_stats_for_all_priority_classes": {
                                    "priority_level": {
                                        "1": {
                                            "queueing": True,
                                            "queue_depth": 0,
                                            "total_drops": 0,
                                            "no_buffer_drops": 0,
                                            "pkts_output": 123456,
                                            "bytes_output": 7890123
                                        }
                                    }
                                },
                                "class_map": {
                                    "IPP67": {
                                        "match_evaluation": "match-all",
                                        "bandwidth_kbps": 234,
                                        "bandwidth_percent": 50,
                                        "packets": 123,
                                        "bytes": 4567,
                                        "rate": {
                                            "interval": 300,
                                            "offered_rate_bps": 123123123,
                                            "drop_rate_bps": 456456456
                                        },
                                        "match": [
                                            "ip precedence 6  7"
                                        ],
                                        "queueing": True,
                                        "queue_limit_packets": "64",
                                        "queue_depth": 63,
                                        "total_drops": 2655550,
                                        "no_buffer_drops": 0,
                                        "pkts_output": 6612304,
                                        "bytes_output": 819909328
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }
    }

    golden_output18 = {'execute.return_value':'''
    PE1#show policy-map interface te0/0/0.101
 TenGigabitEthernet0/0/0.101

  Service-policy input: L3VPN_in

    Class-map: class-default (match-any)
      0 packets, 0 bytes
      5 minute offered rate 0000 bps, drop rate 0000 bps
      Match: any
      police:
          cir 400000 bps, bc 400000 bytes
        conformed 0 packets, 0 bytes; actions:
          transmit
        exceeded 0 packets, 0 bytes; actions:
          drop
        conformed 0000 bps, exceeded 0000 bps

      Service-policy : STD_in_child

        Class-map: IPP567 (match-all)
          0 packets, 0 bytes
          5 minute offered rate 0000 bps, drop rate 0000 bps
          Match: ip precedence 3  4  5
          QoS Set
            ip precedence 1
              Marker statistics: Disabled
            qos-group 1
              Marker statistics: Disabled

  Service-policy output: L3VPN_out

    Class-map: class-default (match-any)
      2121212 packets, 121212 bytes
      5 minute offered rate 11111171 bps, drop rate 1118111 bps
      Match: any
      Queueing
      queue limit 64 packets
      (queue depth/total drops/no-buffer drops) 0/11111/0
      (pkts output/bytes output) 11511/111611
      shape (average) cir 111222, bc 2323, be 3434
      target shape rate 454545

      Service-policy : leeaf

        queue stats for all priority classes:
          Queueing
          priority level 1
          queue limit 512 packets
          (queue depth/total drops/no-buffer drops) 0/0/0
          (pkts output/bytes output) 123456/7890123

        Class-map: IPP67 (match-all)
          123 packets, 4567 bytes
          5 minute offered rate 123123123 bps, drop rate 456456456 bps
          Match: ip precedence 6  7
          Queueing
          queue limit 64 packets
          (queue depth/total drops/no-buffer drops) 63/2655550/0
          (pkts output/bytes output) 6612304/819909328
          bandwidth 50% (234 kbps)
          '''}

    golden_parsed_output19 = {'TenGigabitEthernet0/0/0.101': 
        {'service_policy': 
            {'input': 
                {'policy_name': 
                    {'L3VPNin': 
                        {'class_map': 
                            {'ARP_in': 
                                {'bytes': 0,
                                'match': ['protocol ' 'arp'],
                                                   'match_evaluation': 'match-all',
                                                   'packets': 0,
                                                   'police': {'cir_bc_bytes': 125,
                                                              'cir_bps': 100,
                                                              'conformed': {'actions': {'transmit': True},
                                                                            'bps': 0,
                                                                            'bytes': 0,
                                                                            'packets': 0},
                                                              'exceeded': {'actions': {'drop': True},
                                                                           'bps': 0,
                                                                           'bytes': 0,
                                                                           'packets': 0},
                                                              'pir_be_bytes': 658,
                                                              'pir_bps': 20000,
                                                              'violated': {'actions': {'drop': True},
                                                                           'bps': 0,
                                                                           'bytes': 0,
                                                                           'packets': 0}},
                                                   'rate': {'drop_rate_bps': 0,
                                                            'interval': 300,
                                                            'offered_rate_bps': 0}}}}}}}}}

    golden_output19 = {'execute.return_value':'''
show policy-map interface te0/0/0.101
 TenGigabitEthernet0/0/0.101

  Service-policy input: L3VPNin

    Class-map: ARP_in (match-all)
      0 packets, 0 bytes
      5 minute offered rate 0000 bps, drop rate 0000 bps
      Match: protocol arp
      police:
          cir 100 bps, bc 125 bytes
          pir 20000 bps, be 658 bytes
        conformed 0 packets, 0 bytes; actions:
          transmit
        exceeded 0 packets, 0 bytes; actions:
          drop
        violated 0 packets, 0 bytes; actions:
          drop
        conformed 0000 bps, exceeded 0000 bps, violated 0000 bps
          '''}

    golden_parsed_output20 = {
    "TenGigabitEthernet0/0/0.101": {
        "service_policy": {
            "input": {
                "policy_name": {
                    "L3VPNin": {
                        "class_map": {
                            "IPP11111": {
                                "match_evaluation": "match-all",
                                "bandwidth_percent": 4,
                                "bandwidth_kbps": 536,
                                "packets": 253,
                                "bytes": 5656,
                                "rate": {
                                    "interval": 300,
                                    "offered_rate_bps": 0,
                                    "drop_rate_bps": 0
                                },
                                "match": [
                                    "ip precedence 6  7"
                                ],
                                "queueing": True,
                                "queue_limit_packets": "32",
                                "queue_depth": 98,
                                "total_drops": 666,
                                "no_buffer_drops": 0,
                                "pkts_output": 125,
                                "bytes_output": 253654
                            }
                        }
                    }
                }
            }
        }
    }
}

    golden_output20 = {'execute.return_value':'''
show policy-map interface te0/0/0.101
 TenGigabitEthernet0/0/0.101

  Service-policy input: L3VPNin

    Class-map: IPP11111 (match-all)
      253 packets, 5656 bytes
      5 minute offered rate 0000 bps, drop rate 0000 bps
      Match: ip precedence 6  7
      Queueing
      queue limit 32 packets
      (queue depth/total drops/no-buffer drops) 98/666/0
      (pkts output/bytes output) 125/253654
      bandwidth 4% (536 kbps)
          '''}

    golden_parsed_output21 = {
        'GigabitEthernet4.1': {
            'service_policy': {
                'output': {
                    'policy_name': {
                        'parent-policy': {
                            'child_policy_name': {
                                'child-policy': {
                                    'class_map': {
                                        'band-policy': {
                                            'bandwidth_kbps': 110000,
                                            'bytes': 0,
                                            'bytes_output': 0,
                                            'match': ['none'],
                                            'match_evaluation': 'match-all',
                                            'no_buffer_drops': 0,
                                            'packets': 0,
                                            'pkts_output': 0,
                                            'queue_depth': 0,
                                            'queue_limit_packets': '64',
                                            'queueing': True,
                                            'rate': {'drop_rate_bps': 0,
                                                     'interval': 300,
                                                     'offered_rate_bps': 0},
                                            'total_drops': 0},
                                        'class-default': {
                                            'bytes': 0,
                                            'bytes_output': 0,
                                            'match': ['any'],
                                            'match_evaluation': 'match-any',
                                            'no_buffer_drops': 0,
                                            'packets': 0,
                                            'pkts_output': 0,
                                            'queue_depth': 0,
                                            'queue_limit_packets': '100',
                                            'random_detect': {
                                                'exp_weight_constant': '4 (1/16)',
                                                'mean_queue_depth': 0},
                                            'rate': {'drop_rate_bps': 0,
                                                     'interval': 300,
                                                     'offered_rate_bps': 0},
                                            'total_drops': 0},
                                        'high-priority': {
                                            'bytes': 0,
                                            'match': ['none'],
                                            'match_evaluation': 'match-all',
                                            'packets': 0,
                                            'rate': {'drop_rate_bps': 0,
                                                     'interval': 300,
                                                     'offered_rate_bps':
                                                         0}},
                                        'low-priority': {
                                            'bytes': 0,
                                            'match': ['none'],
                                            'match_evaluation': 'match-all',
                                            'packets': 0,
                                            'rate': {'drop_rate_bps': 0,
                                                     'interval': 300,
                                                     'offered_rate_bps': 0}},
                                        'test-cir': {
                                            'bandwidth_kbps': 600000,
                                            'bytes': 0,
                                            'bytes_output': 0,
                                            'match': ['none'],
                                            'match_evaluation': 'match-all',
                                            'no_buffer_drops': 0,
                                            'packets': 0,
                                            'pkts_output': 0,
                                            'queue_depth': 0,
                                            'queue_limit_packets': '64',
                                            'queueing': True,
                                            'rate': {'drop_rate_bps': 0,
                                                     'interval': 300,
                                                     'offered_rate_bps': 0},
                                            'total_drops': 0}},
                                    'queue_stats_for_all_priority_classes': {
                                        'priority_level': {
                                            'default': {'bytes_output': 0,
                                                        'no_buffer_drops': 0,
                                                        'pkts_output': 0,
                                                        'queue_depth': 0,
                                                        'total_drops':
                                                            0}}}}},
                            'class_map': {
                                'class-default': {
                                    'bytes': 0,
                                    'bytes_output': 0,
                                    'match': ['any'],
                                    'match_evaluation':
                                        'match-any',
                                    'no_buffer_drops': 0,
                                    'packets': 0,
                                    'pkts_output': 0,
                                    'queue_depth': 0,
                                    'queue_limit_packets': '512',
                                    'queueing': True,
                                    'rate': {'drop_rate_bps': 0,
                                             'interval': 300,
                                             'offered_rate_bps': 0},
                                    'shape_bc_bps': 21000000,
                                    'shape_be_bps': 21000000,
                                    'shape_cir_bps': 1000000000,
                                    'shape_type': 'average',
                                    'target_shape_rate':
                                        3000000000,
                                    'total_drops': 0}}}}}}}}

    golden_output21 = {'execute.return_value':'''
    GigabitEthernet4.1
    
      Service-policy output: parent-policy
    
        Class-map: class-default (match-any)
          0 packets, 0 bytes
          5 minute offered rate 0000 bps, drop rate 0000 bps
          Match: any
          Queueing
          queue limit 34 packets
          (queue depth/total drops/no-buffer drops) 0/0/0
          (pkts output/bytes output) 0/0
          shape (average) cir 1000000000, bc 21000000, be 21000000
          target shape rate 3000000000
    
          Service-policy : child-policy
    
            queue stats for all priority classes:
              Queueing
              queue limit 512 packets
              (queue depth/total drops/no-buffer drops) 0/0/0
              (pkts output/bytes output) 0/0
    
            Class-map: high-priority (match-all)
              0 packets, 0 bytes
              5 minute offered rate 0000 bps, drop rate 0000 bps
              Match: none
              Priority: 1000000 kbps, burst bytes 25000000, b/w exceed drops: 0
    
    
            Class-map: low-priority (match-all)
              0 packets, 0 bytes
              5 minute offered rate 0000 bps, drop rate 0000 bps
              Match: none
              Priority: 1000000 kbps, burst bytes 25000000, b/w exceed drops: 0
    
    
            Class-map: band-policy (match-all)
              0 packets, 0 bytes
              5 minute offered rate 0000 bps, drop rate 0000 bps
              Match: none
              Queueing
              queue limit 64 packets
              (queue depth/total drops/no-buffer drops) 0/0/0
              (pkts output/bytes output) 0/0
              bandwidth 110000 kbps
    
            Class-map: test-cir (match-all)
              0 packets, 0 bytes
              5 minute offered rate 0000 bps, drop rate 0000 bps
              Match: none
              Queueing
              queue limit 64 packets
              (queue depth/total drops/no-buffer drops) 0/0/0
              (pkts output/bytes output) 0/0
              bandwidth 600000 kbps
    
            Class-map: class-default (match-any)
              0 packets, 0 bytes
              5 minute offered rate 0000 bps, drop rate 0000 bps
              Match: any
    
              queue limit 100 packets
              (queue depth/total drops/no-buffer drops) 0/0/0
              (pkts output/bytes output) 0/0
                Exp-weight-constant: 4 (1/16)
                Mean queue depth: 0 packets
                class       Transmitted         Random drop      Tail drop          
                Minimum        Maximum     Mark
                        pkts/bytes            pkts/bytes       pkts/bytes          
                        thresh         thresh     prob
    
                0               0/0               0/0              0/0                 
                25            50  1/10
                1               0/0               0/0              0/0                 
                50            70  1/10
                2               0/0               0/0              0/0                 
                80           100  1/10
                3               0/0               0/0              0/0                 
                80           100  1/10
                4               0/0               0/0              0/0                 
                80           100  1/10
                5               0/0               0/0              0/0                 
                80           100  1/10
                6               0/0               0/0              0/0                 
                80           100  1/10
                7               0/0               0/0              0/0                 
                25            50  1/10

    '''}

    def test_show_policy_map_control_plane_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowPolicyMapControlPlane(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_policy_map_control_plane_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowPolicyMapControlPlane(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_policy_map_control_plane_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowPolicyMapControlPlane(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_policy_map_control_plane_full3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowPolicyMapControlPlane(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_show_policy_map_control_plane_full4(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output4)
        obj = ShowPolicyMapControlPlane(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output4)

    # ---------------------------------------------------------------------

    def test_show_policy_map_interface_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output5)
        obj = ShowPolicyMapInterface(device=self.device)
        parsed_output = obj.parse(interface='gigabitEthernet 0/0/0')
        self.assertEqual(parsed_output, self.golden_parsed_output5)

    def test_show_policy_map_interface_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output6)
        obj = ShowPolicyMapInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output6)

    def test_show_policy_map_interface_full3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output7)
        obj = ShowPolicyMapInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output7)

    def test_show_policy_map_interface_full4(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output8)
        obj = ShowPolicyMapInterface(device=self.device)
        parsed_output = obj.parse(interface='TenGigabitEthernet0/0/2')
        self.assertEqual(parsed_output, self.golden_parsed_output8)

    def test_show_policy_map_interface_full5(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output9)
        obj = ShowPolicyMapInterface(device=self.device)
        parsed_output = obj.parse(interface='GigabitEthernet0/0/1')
        self.assertEqual(parsed_output, self.golden_parsed_output9)

    def test_show_policy_map_interface_full6(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output18)
        obj = ShowPolicyMapInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output18)

    def test_show_policy_map_interface_full7(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output19)
        obj = ShowPolicyMapInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output19)

    def test_show_policy_map_interface_full8(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output20)
        obj = ShowPolicyMapInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output20)

    def test_show_policy_map_interface_output_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output10)
        obj = ShowPolicyMapInterfaceOutput(device=self.device)
        parsed_output = obj.parse(interface='gigabitEthernet 0/1/1',
                                  class_name='class-default')
        self.assertEqual(parsed_output, self.golden_parsed_output10)

    def test_show_policy_map_interface_output_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output11)
        obj = ShowPolicyMapInterfaceOutput(device=self.device)
        parsed_output = obj.parse(interface='TenGigabitEthernet 0/3/0.41')
        self.assertEqual(parsed_output, self.golden_parsed_output11)

    def test_show_policy_map_interface_input_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output12)
        obj = ShowPolicyMapInterfaceInput(device=self.device)
        parsed_output = obj.parse(interface='gigabitEthernet 0/1/4',
                                  class_name='class-default')
        self.assertEqual(parsed_output, self.golden_parsed_output12)

    def test_show_policy_map_interface_input_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output13)
        obj = ShowPolicyMapInterfaceInput(device=self.device)
        parsed_output = obj.parse(interface='GigabitEthernet 0/0/1')
        self.assertEqual(parsed_output, self.golden_parsed_output13)

    def test_show_policy_map_interface_class_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output14)
        obj = ShowPolicyMapInterfaceClass(device=self.device)
        parsed_output = obj.parse(class_name='TEST2')
        self.assertEqual(parsed_output, self.golden_parsed_output14)

    def test_show_policy_map_interface_class_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output15)
        obj = ShowPolicyMapInterfaceClass(device=self.device)
        parsed_output = obj.parse(class_name='VLAN51_QoS')
        self.assertEqual(parsed_output, self.golden_parsed_output15)

    def test_show_policy_map_target_full(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output16)
        obj = ShowPolicyMapTargetClass(device=self.device)
        parsed_output = obj.parse(num='1')
        self.assertEqual(parsed_output, self.golden_parsed_output16)

    def test_show_policy_map_target_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output17)
        obj = ShowPolicyMapTargetClass(device=self.device)
        parsed_output = obj.parse(num='1')
        self.assertEqual(parsed_output, self.golden_parsed_output17)

    def test_show_policy_map_interface_class13(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output21)
        obj = ShowPolicyMapInterface(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output21)

# =============================================
# Unit test for :
#    *'show policy map'
#    *'show policy map {name}'
# =============================================

class test_show_policy_map(unittest.TestCase):
    '''Unit test for "show policy map"
                     "show policy map {name}"
    '''

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'policy_map': {
            'shape-out': {
                'class': {
                    'class-default': {
                        'average_rate_traffic_shaping': True,
                        'cir_bps': 1000000}}}}}

    golden_output1 = {'execute.return_value':'''
        Router#show policy-map shape-out
        Load for five secs: 1%/0%; one minute: 4%; five minutes: 4%
        Time source is NTP, 22:28:37.624 EST Fri Nov 4 2016

            Policy Map shape-out
                Class class-default
                    Average Rate Traffic Shaping
                    cir 1000000 (bps)   
        Router#	        
    '''}

    golden_parsed_output2 = {
        'policy_map': {
            'police-in': {
                'class': {
                    'class-default': {
                        'police': {
                            'cir_bps': 445500,
                            'cir_bc_bytes': 83619,
                            'conform_action': ['transmit'],
                            'exceed_action': ['drop']}}}}}}

    golden_output2 = {'execute.return_value':'''

        Router#show policy-map police-in
        Load for five secs: 11%/0%; one minute: 4%; five minutes: 4%
        Time source is NTP, 07:03:58.319 EST Wed Oct 26 2016

            Policy Map police-in
                Class class-default
                    police cir 445500 bc 83619
                        conform-action transmit 
                        exceed-action drop 
    '''}

    golden_parsed_output3 = {
        'policy_map': {
            'parent-policy': {
                'class': {
                    'class-default': {
                        'police': {
                            'cir_bps': 50000,
                            'cir_bc_bytes': 3000,
                            'cir_be_bytes': 3000,
                            'conform_color': 'hipri-conform',
                            'conform_action': ['transmit'],
                            'exceed_action': ['transmit'],
                            'violate_action': ['drop'],
                            'service_policy': 'child-policy'}}}},
            'police': {
                'class': {
                    'prec1': {
                        'priority_level': {
                            '1': {
                                'kbps': 20000}}},
                    'prec2': {
                        'bandwidth_kbps': 20000},
                    'class-default': {
                        'bandwidth_kbps': 20000}}},
            'child-policy': {
                'class': {
                    'user1-acl-child': {
                        'police': {
                            'cir_bps': 10000,
                            'cir_bc_bytes': 1500,
                            'conform_action': ['set-qos-transmit 5'],
                            'exceed_action': ['drop']}},
                    'user2-acl-child': {
                        'police': {
                            'cir_bps': 20000,
                            'cir_bc_bytes': 1500,
                            'conform_action': ['set-qos-transmit 5'],
                            'exceed_action': ['drop']}},
                    'class-default': {
                        'police': {
                            'cir_bps': 50000,
                            'cir_bc_bytes': 1500,
                            'conform_action': ['transmit'],
                            'exceed_action': ['drop']}}}}}}

    golden_output3 = {'execute.return_value': '''
        Router# show policy-map
        Policy Map parent-policy
            Class class-default
            police cir 50000 bc 3000 be 3000
            conform-color hipri-conform
            conform-action transmit
            exceed-action transmit
            violate-action drop
            service-policy child-policy
        Policy Map police
            Class prec1
                priority level 1 20000 (kb/s)
            Class prec2
                bandwidth 20000 (kb/s)
            Class class-default
                bandwidth 20000 (kb/s)
        Policy Map child-policy
            Class user1-acl-child
                police cir 10000 bc 1500
                conform-action set-qos-transmit 5
                exceed-action drop
            Class user2-acl-child
                police cir 20000 bc 1500
                conform-action set-qos-transmit 5
                exceed-action drop
            Class class-default
                police cir 50000 bc 1500
                conform-action transmit 
                exceed-action drop
    '''}

    golden_parsed_output4 = {
        'policy_map': {
            'pol1': {
                'class': {
                    'class-default': {
                        'weighted_fair_queueing': {
                            'bandwidth_percent': 70,
                            'exponential_weight': 9,
                            'explicit_congestion_notification': True,
                            'class_val': {
                                '0': {
                                    'min_threshold': '-',
                                    'max_threshold': '-',
                                    'mark_probability': '1/10'},
                                '1': {
                                    'min_threshold': '-',
                                    'max_threshold': '-',
                                    'mark_probability': '1/10'},
                                '2': {
                                    'min_threshold': '-',
                                    'max_threshold': '-',
                                    'mark_probability': '1/10'},
                                '3': {
                                    'min_threshold': '-',
                                    'max_threshold': '-',
                                    'mark_probability': '1/10'},
                                '4': {
                                    'min_threshold': '-',
                                    'max_threshold': '-',
                                    'mark_probability': '1/10'},
                                '5': {
                                    'min_threshold': '-',
                                    'max_threshold': '-',
                                    'mark_probability': '1/10'},
                                '6': {
                                    'min_threshold': '-',
                                    'max_threshold': '-',
                                    'mark_probability': '1/10'},
                                '7': {
                                    'min_threshold': '-',
                                    'max_threshold': '-',
                                    'mark_probability': '1/10'},
                                'rsvp': {
                                    'min_threshold': '-',
                                    'max_threshold': '-',
                                    'mark_probability': '1/10'}}}}}}}}

    golden_output4 = {'execute.return_value': '''
        Router# show policy-map

        Policy Map pol1
            Class class-default
                Weighted Fair Queueing
                    Bandwidth 70 (%)
                    exponential weight 9
                    explicit congestion notification
                    class    min-threshold    max-threshold    mark-probability
                    ----------------------------------------------------------
                    ----------------------------------------------------------

                    0        -                -                1/10
                    1        -                -                1/10
                    2        -                -                1/10
                    3        -                -                1/10
                    4        -                -                1/10
                    5        -                -                1/10
                    6        -                -                1/10
                    7        -                -                1/10
                    rsvp     -                -                1/10

        Policy Map pol1
            Class class-default
                Weighted Fair Queueing
                    Bandwidth 70 (%)
                    exponential weight 9
                    explicit congestion notification
                    class    min-threshold    max-threshold    mark-probability
                    ----------------------------------------------------------
                    ----------------------------------------------------------

                    0        -                -                1/10
                    1        -                -                1/10
                    2        -                -                1/10
                    3        -                -                1/10
                    4        -                -                1/10
                    5        -                -                1/10
                    6        -                -                1/10
                    7        -                -                1/10
                    rsvp     -                -                1/10

    '''}

    golden_parsed_output5 = {
        'policy_map': {
            'PHB': {
                'class': {
                    'cos1': {
                        'police': {
                            'cir_bc_bytes': 8000,
                             'cir_bps': 200000,
                             'conform_action': ['transmit'],
                             'exceed_action': ['drop']},
                        'priority': True},
                    'cos2': {
                        'bandwidth_kbps': 100,
                        'bandwidth_remaining_percent': 40},
                    'cos3': {
                        'bandwidth_kbps': 200,
                        'bandwidth_remaining_percent': 50,
                        'set': 'cos 5'},
                    'cos5': {
                        'shape_average_min': 30}}}}}

    golden_output5 = {'execute.return_value': '''
            Router# show policy-map
                Policy Map PHB
                    Class cos1
                        police cir 200000 bc 8000
                            conform-action transmit
                            exceed-action drop
                        priority
                    Class cos2
                        bandwidth 100
                        bandwidth remaining percent 40
                    Class cos3
                        bandwidth 200
                        bandwidth remaining percent 50

                Policy Map PHB
                    Class cos1
                        police cir 200000 bc 8000
                            conform-action transmit
                            exceed-action drop
                        priority
                    Class cos2
                        bandwidth 100
                    Class cos3
                        bandwidth 200

                Policy-map ingress_policy
                    Class cos3
                        Set cos 5
                Policy-map egress policy
                    Class cos5
                        Shape average 30m '''}

    golden_parsed_output6 = {
        'policy_map': {
            'child': {
                'class': {
                    'voice': {
                        'priority': True,
                        'police': {
                            'cir_bps': 8000,
                            'cir_bc_bytes': 9216,
                            'cir_be_bytes': 0,
                            'conform_action': ['transmit'],
                            'exceed_action': ['drop'],
                            'violate_action': ['drop']}},
                    'video': {
                        'bandwidth_remaining_percent': 80}}}}}

    golden_output6 = {'execute.return_value': '''
        Router# show policy-map child

        Policy Map child
            Class voice
                priority
                police 8000 9216 0
                    conform-action transmit
                    exceed-action drop
                    violate-action drop
            Class video
                bandwidth remaining 80 (%)
        '''}

    golden_parsed_output7 = {
        'policy_map': {
            'parent': {
                'class': {
                    'class-default': {
                        'average_rate_traffic_shaping': True,
                        'cir_bps': 10000000,
                        'service_policy': 'child'}}}}}

    golden_output7 = {'execute.return_value': '''
        Router# show policy-map parent
        Policy Map parent
            Class class-default
                Average Rate Traffic Shaping
                cir 10000000 (bps)
                service-policy child
    '''}

    golden_parsed_output8 = {
        'policy_map': {
            'policy1': {
                'class': {
                    'class1': {
                        'police': {
                            'cir_percent': 20,
                            'bc_ms': 300,
                            'pir_percent': 40,
                            'be_ms': 400,
                            'conform_action': ['transmit'],
                            'exceed_action': ['drop'],
                            'violate_action': ['drop']}}}}}}

    golden_output8 = {'execute.return_value': '''
        Router# show policy-map policy1
            Policy Map policy1
                Class class1
                    police cir percent 20 bc 300 ms pir percent 40 be 400 ms
                        conform-action transmit
                        exceed-action drop
                        violate-action drop
    '''}

    golden_parsed_output9 = {
        'policy_map': {
            'pol1': {
                'class': {
                    'class c1': {
                        'random_detect': {
                            'bandwidth_percent': 10,
                            'exponential_weight': 9,
                            'class_val': {
                                '0': {
                                    'min_threshold': '-',
                                    'max_threshold': '-',
                                    'mark_probability': '1/10'},
                                '1': {
                                    'min_threshold': '20000',
                                    'max_threshold': '30000',
                                    'mark_probability': '1/10'},
                                '2': {
                                    'min_threshold': '-',
                                    'max_threshold': '-',
                                    'mark_probability': '1/10'},
                                '3': {
                                    'min_threshold': '-',
                                    'max_threshold': '-',
                                    'mark_probability': '1/10'},
                                '4': {
                                    'min_threshold': '-',
                                    'max_threshold': '-',
                                    'mark_probability': '1/10'},
                                '5': {
                                    'min_threshold': '-',
                                    'max_threshold': '-',
                                    'mark_probability': '1/10'},
                                '6': {
                                    'min_threshold': '-',
                                    'max_threshold': '-',
                                    'mark_probability': '1/10'},
                                '7': {
                                    'min_threshold': '-',
                                    'max_threshold': '-',
                                    'mark_probability': '1/10'},
                                'rsvp': {
                                    'min_threshold': '-',
                                    'max_threshold': '-',
                                    'mark_probability': '1/10'}}}}}}}}

    golden_output9 = {'execute.return_value': '''
        Router# show policy-map
        Policy Map pol1
            Class class c1
        Bandwidth 10 (%)
        exponential weight 9
        class   min-threshold(bytes)   max-threshold(bytes)  mark-probability
        -------------------------------------------------------------------
 
        0       -                       -                      1/10
        1       20000                   30000                  1/10
        2       -                       -                      1/10
        3       -                       -                      1/10
        4       -                       -                      1/10
        5       -                       -                      1/10
        6       -                       -                      1/10
        7       -                       -                      1/10
        rsvp    -                       -                      1/10
    '''}

    golden_parsed_output10 = {
        'policy_map': {
            'police': {
                'class': {
                    'class-default': {
                        'police': {
                            'cir_bps': 1000000,
                            'cir_bc_bytes': 31250,
                            'pir': 2000000,
                            'pir_be_bytes': 31250,
                            'conform_action': ['transmit'],
                            'exceed_action': ['set-prec-transmit 4', 'set-frde-transmit'],
                            'violate_action': ['set-prec-transmit 2', 'set-frde-transmit']}}}}}}

    golden_output10 = {'execute.return_value': '''
        Router# show policy-map police
        Policy Map police
            Class class-default
                police cir 1000000 bc 31250 pir 2000000 be 31250
                    conform-action transmit
                    exceed-action set-prec-transmit 4
                    exceed-action set-frde-transmit
                    violate-action set-prec-transmit 2
                    violate-action set-frde-transmit
    '''}

    golden_parsed_output11 = {
        'policy_map': {
            'pm_hier2_child_0_2': {
                'class': {
                    'cm_0': {
                        'priority_levels': 1,
                        'police': {
                            'cir_percent': 5,
                            'bc_ms': 2,
                            'be_ms': 0,
                            'conform_action': ['transmit'],
                            'exceed_action': ['drop'],
                            'violate_action': ['drop']},
                        'queue_limit_packets': 77},
                    'cm_1': {
                        'average_rate_traffic_shaping': True,
                        'cir_percent': 80,
                        'bandwidth_remaining_ratio': 80},
                    'class-default': {
                        'average_rate_traffic_shaping': True,
                        'cir_percent': 50,
                        'bandwidth_remaining_ratio': 20}}}}}

    golden_output11 = {'execute.return_value': '''
         Router# show policy-map pm_hier2_child_0_2
         Policy Map pm_hier2_child_0_2
         Class cm_0
         priority level 1
         police percent 5 2 ms 0 ms conform-action transmit exceed-action drop violate-action drop
         queue-limit 77 packets
         Class cm_1
         Average Rate Traffic Shaping
         cir 80%
         bandwidth remaining ratio 80 
         Class class-default
         Average Rate Traffic Shaping
         cir 50%
         bandwidth remaining ratio 20 
    '''}

    golden_parsed_output12 = {
        'policy_map': {
            'child-policy': {
                'class': {
                    'band-policy': {
                        'bandwidth_kbps': 150000},
                    'class-default': {
                        'queue_limit_packets': 100,
                        'random_detect': {
                            'class_val': {
                                '0': {'mark_probability': '1/10',
                                      'max_threshold': '50',
                                      'min_threshold': '25'},
                                '1': {'mark_probability': '1/10',
                                      'max_threshold': '70',
                                      'min_threshold': '50'},
                                '2': {'mark_probability': '1/10',
                                      'max_threshold': '100',
                                      'min_threshold': '80'},
                                '3': {'mark_probability': '1/10',
                                      'max_threshold': '100',
                                      'min_threshold': '80'},
                                '4': {'mark_probability': '1/10',
                                      'max_threshold': '100',
                                      'min_threshold': '80'},
                                '5': {'mark_probability': '1/10',
                                      'max_threshold': '100',
                                      'min_threshold': '80'},
                                '6': {'mark_probability': '1/10',
                                      'max_threshold': '100',
                                      'min_threshold': '80'},
                                '7': {'mark_probability': '1/10',
                                      'max_threshold': '50',
                                      'min_threshold': '25'}},
                            'exponential_weight': 4,
                            'wred_type': 'packet-based'}},
                    'high-priority': {
                        'priority': True,
                        'priority_kbps': 2000000},
                    'low-priority': {
                        'priority': True,
                        'priority_kbps': 2000000},
                    'test-cir': {
                        'bandwidth_kbps': 800000}}}}}

    golden_output12 = {'execute.return_value':'''
      Policy Map child-policy
        Class high-priority
          priority 2000000 (kbps)
        Class low-priority
          priority 2000000 (kbps)
        Class band-policy
          bandwidth 150000 (kbps)
        Class test-cir
          bandwidth 800000 (kbps)
        Class class-default
           packet-based wred, exponential weight 4
    
          class    min-threshold    max-threshold    mark-probablity
          ----------------------------------------------------------
          0       25               50               1/10
          1       50               70               1/10
          2       80               100              1/10
          3       80               100              1/10
          4       80               100              1/10
          5       80               100              1/10
          6       80               100              1/10
          7       25               50               1/10
          queue-limit 100 packets
    '''}
    golden_parsed_output13 = {
        'policy_map': {
            'parent-policy2': {
                'class': {
                    'class-default': {
                        'average_rate_traffic_shaping': True,
                        'bc_bits': 2000000,
                        'be_bits': 300000,
                        'cir_bps': 1000000}}}}}

    golden_output13 = {'execute.return_value':'''
        Policy Map parent-policy2
            Class class-default
              Average Rate Traffic Shaping
              cir 1000000 (bps) bc 2000000 (bits) be 300000 (bits)

    '''}

    golden_parsed_output14 = {
        "policy_map": {
            "policy_4-6-3~6": {
                "class": {
                    "class_4-6-3": {
                        "average_rate_traffic_shaping": True,
                        "cir_bps": 100000000,
                        "bc_bits": 80000000,
                    },
                    "class_4-6-4~6": {
                        "average_rate_traffic_shaping": True,
                        "cir_bps": 100000000,
                        "bc_bits": 80000000,
                        "be_bits": 60000000,
                    },
                    "system-cpp-police-sys-data": {
                        "police": {
                            "rate_pps": 100,
                            "conform_action": ["transmit"],
                            "exceed_action": ["drop"],
                        }
                    }
                }
            }
        }
    }
    golden_output14 = {'execute.return_value':'''
        show policy-map

        Policy Map policy_4-6-3~6
            Class class_4-6-3
            Average Rate Traffic Shaping
            cir 100000000 (bps) bc 80000000 (bits)
            Class class_4-6-4~6
            Average Rate Traffic Shaping
            cir 100000000 (bps) bc 80000000 (bits) be 60000000 (bits)
            Class system-cpp-police-sys-data
            police rate 100 pps
            conform-action transmit
            exceed-action drop
    '''}

    def test_show_policy_map_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowPolicyMap(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_policy_map_golden1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowPolicyMap(device=self.device)
        parsed_output = obj.parse(name='shape-out')
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_policy_map_golden2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowPolicyMap(device=self.device)
        parsed_output = obj.parse(name='police-in')
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_policy_map_golden3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowPolicyMap(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_show_policy_map_golden4(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output4)
        obj = ShowPolicyMap(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output4)

    def test_show_policy_map_golden5(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output5)
        obj = ShowPolicyMap(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output5)

    def test_show_policy_map_golden6(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output6)
        obj = ShowPolicyMap(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output6)

    def test_show_policy_map_golden7(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output7)
        obj = ShowPolicyMap(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output7)

    def test_show_policy_map_golden8(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output8)
        obj = ShowPolicyMap(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output8)

    def test_show_policy_map_golden9(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output9)
        obj = ShowPolicyMap(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output9)

    def test_show_policy_map_golden10(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output10)
        obj = ShowPolicyMap(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output10)

    def test_show_policy_map_golden11(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output11)
        obj = ShowPolicyMap(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output11)

    def test_show_policy_map_golden12(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output12)
        obj = ShowPolicyMap(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output12)

    def test_show_policy_map_golden13(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output13)
        obj = ShowPolicyMap(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output13)

    def test_show_policy_map_golden14(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output14)
        obj = ShowPolicyMap(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output14)

if __name__ == '__main__':
    unittest.main()
