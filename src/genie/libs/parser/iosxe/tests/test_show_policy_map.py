# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxe show_monitor
from genie.libs.parser.iosxe.show_policy_map import ShowPolicyMapType,\
                                                    ShowPolicyMap


# ====================================================================
# Unit test for :
#   *'show policy-map control-plane'
#   *'show policy-map interface {interface}'
#   *'show policy-map interface {interface} output class {class_name}'
# =====================================================================
class test_show_policy_map_type(unittest.TestCase):
    '''Unit test for
       "show policy-map control-plane"
       "show policy-map interface {interface}"
       "show policy-map interface {interface} output class {class_name}"
    '''

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}


    golden_parsed_output1 ={
        'Control Plane':
            {'service_policy':
                {'input':
                    {'policy_name':
                        {'Control_Plane_In':
                            {'class_map':
                                {' Ping_Class':
                                    {'match_all': True,
                                     'packets': 0,
                                     'bytes': 0,
                                     'rate':
                                         {'interval': 300,
                                          'offered_rate_bps': 0,
                                          'drop_rate_bps': 0},
                                     'match': ' access-group name Ping_Option',
                                     'police':
                                         {'cir_bps': 8000,
                                          'bc_bytes': 1500,
                                          'conformed':
                                              {'packets': 0,
                                               'bytes': 0,
                                               'actions': 'drop',
                                               'bps': 0},
                                          'exceeded':
                                              {'packets': 0,
                                               'bytes': 0,
                                               'actions': 'drop',
                                               'bps': 0}}},
                                ' TELNET_Class':
                                    {'match_all': True,
                                     'packets': 0,
                                     'bytes': 0,
                                     'rate':
                                         {'interval': 300,
                                          'offered_rate_bps': 0,
                                          'drop_rate_bps': 0},
                                     'match': ' access-group name TELNET_Permit',
                                     'police':
                                         {'cir_bps': 8000,
                                          'bc_bytes': 1500,
                                          'conformed':
                                              {'packets': 0,
                                               'bytes': 0,
                                               'actions': 'drop',
                                               'bps': 0},
                                          'exceeded':
                                              {'packets': 0,
                                               'bytes': 0,
                                               'actions': 'drop',
                                               'bps': 0}}},
                                ' TACACS_Class':
                                     {'match_all': True,
                                      'packets': 0,
                                      'bytes': 0,
                                      'rate':
                                          {'interval': 300,
                                           'offered_rate_bps': 0,
                                           'drop_rate_bps': 0},
                                      'match': ' access-group name TACACS_Permit',
                                      'police':
                                          {'cir_bps': 8000,
                                           'bc_bytes': 1500,
                                           'conformed':
                                               {'packets': 0,
                                                'bytes': 0,
                                                'actions': 'drop',
                                                'bps': 0},
                                           'exceeded':
                                               {'packets': 0,
                                                'bytes': 0,
                                                'actions': 'drop',
                                                'bps': 0}}},
                                ' SNMP_Class':
                                     {'match_all': True,
                                      'packets': 0,
                                      'bytes': 0,
                                      'rate':
                                          {'interval': 300,
                                           'offered_rate_bps': 0,
                                           'drop_rate_bps': 0},
                                      'match': ' access-group name SNMP_Permit',
                                      'police':
                                          {'cir_bps': 8000,
                                           'bc_bytes': 1500,
                                           'conformed':
                                               {'packets': 0,
                                                'bytes': 0,
                                                'actions': 'drop',
                                                'bps': 0},
                                           'exceeded':
                                               {'packets': 0,
                                                'bytes': 0,
                                                'actions': 'drop',
                                                'bps': 0}}},
                                ' FTP_Class':
                                     {'match_all': True,
                                      'packets': 0,
                                      'bytes': 0,
                                      'rate':
                                          {'interval': 300,
                                           'offered_rate_bps': 0,
                                           'drop_rate_bps': 0},
                                      'match': ' access-group name FTP_Permit',
                                      'police':
                                          {'cir_bps': 8000,
                                           'bc_bytes': 1500,
                                           'conformed':
                                               {'packets': 0,
                                                'bytes': 0,
                                                'actions': 'drop',
                                                'bps': 0},
                                           'exceeded':
                                               {'packets': 0,
                                                'bytes': 0,
                                                'actions': 'drop',
                                                'bps': 0}}},
                                ' BGP_Class':
                                     {'match_all': True,
                                      'packets': 32,
                                      'bytes': 2032,
                                      'rate':
                                          {'interval': 300,
                                           'offered_rate_bps': 0,
                                           'drop_rate_bps': 0},
                                      'match': ' access-group name BGP_Permit',
                                      'qos_set':
                                          {'ip_precedence': 6,
                                           'marker_statistics': 'Disabled'}},
                                ' OSPF_Class':
                                     {'match_all': True,
                                      'packets': 58,
                                      'bytes': 11788,
                                      'rate':
                                          {'interval': 300,
                                           'offered_rate_bps': 0,
                                           'drop_rate_bps': 0},
                                      'match': ' access-group name OSPF_Permit',
                                      'qos_set':
                                          {'ip_precedence': 6,
                                           'marker_statistics': 'Disabled'}},
                                ' LDP_Class':
                                     {'match_all': True,
                                      'packets': 128,
                                      'bytes': 9552,
                                      'rate':
                                          {'interval': 300,
                                           'offered_rate_bps': 0,
                                           'drop_rate_bps': 0},
                                      'match': ' access-group name LDP_Permit',
                                      'qos_set':
                                          {'ip_precedence': 6,
                                           'marker_statistics': 'Disabled'}},
                                ' ICMP_Class1':
                                     {'match_all': True,
                                      'packets': 0,
                                      'bytes': 0,
                                      'rate':
                                          {'interval': 300,
                                           'offered_rate_bps': 0,
                                           'drop_rate_bps': 0},
                                      'match': ' access-group name ICMP_Permit1',
                                      'police':
                                          {'cir_bps': 8000,
                                           'bc_bytes': 1500,
                                           'conformed':
                                               {'packets': 0,
                                                'bytes': 0,
                                                'actions': 'drop',
                                                'bps': 0},
                                           'exceeded':
                                               {'packets': 0,
                                                'bytes': 0,
                                                'actions': 'drop',
                                                'bps': 0}}},
                                ' ICMP_Class2':
                                     {'match_all': True,
                                      'packets': 4,
                                      'bytes': 482,
                                      'rate':
                                          {'interval': 300,
                                           'offered_rate_bps': 0,
                                           'drop_rate_bps': 0},
                                      'match': ' access-group name ICMP_Permit2',
                                      'police':
                                          {'cir_bps': 12000000,
                                           'bc_bytes': 150000,
                                           'conformed':
                                               {'packets': 4,
                                                'bytes': 482,
                                                'actions': 'transmit',
                                                'bps': 0},
                                           'exceeded':
                                               {'packets': 0,
                                                'bytes': 0,
                                                'actions': 'drop',
                                                'bps': 0}}},
                                ' NTP_Class':
                                     {'match_all': True,
                                      'packets': 3,
                                      'bytes': 330,
                                      'rate':
                                          {'interval': 300,
                                           'offered_rate_bps': 0,
                                           'drop_rate_bps': 0},
                                      'match': ' access-group name NTP_Permit',
                                      'police':
                                          {'cir_bps': 8000,
                                           'bc_bytes': 1500,
                                           'conformed':
                                               {'packets': 3,
                                                'bytes': 330,
                                                'actions': 'drop',
                                                'bps': 0},
                                           'exceeded':
                                               {'packets': 0,
                                                'bytes': 0,
                                                'actions': 'drop',
                                                'bps': 0}}},
                                ' ALL_Class':
                                     {'match_all': True,
                                      'packets': 23,
                                      'bytes': 1548,
                                      'rate':
                                          {'interval': 300,
                                           'offered_rate_bps': 0,
                                           'drop_rate_bps': 0},
                                      'match': ' access-group name ALL_Permit',
                                      'police':
                                          {'cir_bps': 200000,
                                           'bc_bytes': 15000,
                                           'conformed':
                                               {'packets': 23,
                                                'bytes': 1548,
                                                'actions': 'transmit',
                                                'bps': 0},
                                           'exceeded':
                                               {'packets': 0,
                                                'bytes': 0,
                                                'actions': 'drop',
                                                'bps': 0}}},
                                ' class-default':
                                     {'match_all': False,
                                      'packets': 276,
                                      'bytes': 16554,
                                      'rate':
                                          {'interval': 300,
                                           'offered_rate_bps': 0,
                                           'drop_rate_bps': 0},
                                      'match': ' any'}}}}}}}}

    golden_output1 = {'execute.return_value': '''
        Router#show policy-map control-plane
        Load for five secs: 29%/0%; one minute: 7%; five minutes: 6%
        Time source is NTP, .17:46:23.484 JST Mon Oct 31 2016

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
        'Control Plane':
            {'service_policy':
                {'input':
                    {'policy_name':
                        {'TEST':
                            {'class_map':
                                {'TEST':
                                    {'match_all': True,
                                     'packets': 20,
                                     'bytes': 11280,
                                     'rate':
                                         {'interval': 300,
                                          'offered_rate_bps': 0,
                                          'drop_rate_bps': 0},
                                     'match': 'access-group 101',
                                     'police':
                                         {'police_bps': 8000,
                                          'police_limit': 1500,
                                          'extended_limit': 1500,
                                          'conformed':
                                              {'packets': 15,
                                               'bytes': 6210,
                                               'actions': 'transmit',
                                               'bps': 0},
                                          'exceeded':
                                              {'packets': 5,
                                               'bytes': 5070,
                                               'actions': 'drop',
                                               'bps': 0},
                                          'violated':
                                              {'packets': 0,
                                               'bytes': 0,
                                               'actions': 'drop',
                                               'bps': 0}}},
                                'class-default':
                                     {'match_all': False,
                                      'packets': 105325,
                                      'bytes': 11415151,
                                      'rate':
                                         {'interval': 300,
                                          'offered_rate_bps': 0,
                                          'drop_rate_bps': 0},
                                      'match': 'any'}}}}}}}}

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

    golden_parsed_output3 ={
        'Control Plane':
            {'service_policy':
                {'input':
                    {'policy_name':
                        {'control-plane-in':
                            {'class_map':
                                {' telnet-class':
                                    {'match_all': True,
                                     'packets': 10521,
                                     'bytes': 673344,
                                     'rate':
                                         {'interval': 300,
                                          'offered_rate_bps': 18000,
                                          'drop_rate_bps': 15000},
                                     'match': ' access-group 102',
                                     'police':
                                         {'cir_bps': 64000,
                                          'bc_bytes': 8000,
                                          'conformed':
                                              {'packets': 1430,
                                               'bytes': 91520,
                                               'actions': 'transmit',
                                               'bps': 2000},
                                          'exceeded':
                                              {'packets': 9091,
                                               'bytes': 581824,
                                               'actions': 'drop',
                                               'bps': 15000}}},
                                ' class-default':
                                    {'match_all': False,
                                     'packets': 0,
                                     'bytes': 0,
                                     'rate':
                                         {'interval': 300,
                                          'offered_rate_bps': 0,
                                          'drop_rate_bps': 0},
                                     'match': ' any'}}}}}}}}

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

    golden_parsed_output4 ={
        'Control Plane':
            {'service_policy':
                {'input':
                    {'policy_name':
                        {'copp-ftp':
                            {'class_map':
                                {' copp-ftp':
                                    {'match_all': False,
                                     'packets': 2234,
                                     'bytes': 223400,
                                     'rate':
                                         {'interval': 300,
                                          'offered_rate_bps': 0,
                                          'drop_rate_bps': 0},
                                     'match': ' access-group name copp-ftp',
                                     'police':
                                         {'cir_bps': 10000000,
                                          'bc_bytes': 312500,
                                          'conformed':
                                              {'packets': 2234,
                                               'bytes': 223400,
                                               'actions': 'transmit',
                                               'bps': 0},
                                          'exceeded':
                                              {'packets': 0,
                                               'bytes': 0,
                                               'actions': 'drop',
                                               'bps': 0}}},
                                ' class-default':
                                    {'match_all': False,
                                     'packets': 0,
                                     'bytes': 0,
                                     'rate':
                                         {'interval': 300,
                                          'offered_rate_bps': 0,
                                          'drop_rate_bps': 0},
                                     'match': ' any'}}},
                        'control-plane-in':
                            {'class_map':
                                {' telnet-class':
                                    {'match_all': True,
                                     'packets': 10521,
                                     'bytes': 673344,
                                     'rate':
                                         {'interval': 300,
                                          'offered_rate_bps': 18000,
                                          'drop_rate_bps': 15000},
                                     'match': ' access-group 102',
                                     'police':
                                         {'cir_bps': 64000,
                                          'bc_bytes': 8000,
                                          'conformed':
                                              {'packets': 1430,
                                               'bytes': 91520,
                                               'actions': 'transmit',
                                               'bps': 2000},
                                          'exceeded':
                                              {'packets': 9091,
                                               'bytes': 581824,
                                               'actions': 'drop',
                                               'bps': 15000}}},
                                ' class-default':
                                    {'match_all': False,
                                     'packets': 0,
                                     'bytes': 0,
                                     'rate':
                                         {'interval': 300,
                                          'offered_rate_bps': 0,
                                          'drop_rate_bps': 0},
                                     'match': ' any'}}}}}}}}

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
        'GigabitEthernet0/1/5': {
            'service_policy': {
                'output': {
                    'policy_name': {
                        'shape-out': {
                            'class_map': {
                                ' class-default': {
                                    'match_all': False,
                                    'packets': 0,
                                    'bytes': 0,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0,
                                        'drop_rate_bps': 0},
                                    'match': ' any',
                                    'queueing': {
                                        'queue_limit': '64 packets',
                                        'queue_depth': 0,
                                        'total_drops': 0,
                                        'no_buffer_drops': 0,
                                        'pkts_output': 0,
                                        'bytes_output': 0,
                                        'shape_cir_bps': 474656,
                                        'shape_bc_bps': 1899,
                                        'shape_be_bps': 1899,
                                        'target_shape_rate': 474656}}}}}}}}}

    golden_output5 = {'execute.return_value': '''
        Router#show policy-map interface gigabitEthernet 0/1/5 output class class-default

        Load for five secs: 1%/0%; one minute: 5%; five minutes: 6%
        Time source is NTP, 11:16:50.635 JST Tue Oct 25 2016

        GigabitEthernet0/1/5

        Service-policy output: shape-out

        Class-map: class-default (match-any)
            0 packets, 0 bytes
            5 minute offered rate 0000 bps, drop rate 0000 bps
            Match: any
            Queueing
                queue limit 64 packets
                (queue depth/total drops/no-buffer drops) 0/0/0
                (pkts output/bytes output) 0/0
                shape (average) cir 474656, bc 1899, be 1899
                target shape rate 474656
    Router#'''}

    golden_parsed_output6 = {
        'GigabitEthernet0/0/0': {
            'service_policy': {
                'output': {
                    'policy_name': {
                        'CORE-Out': {
                            'class_map': {
                                ' EXP0': {
                                    'match_all': True,
                                    'packets': 0,
                                    'bytes': 0,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0},
                                    'match': ' mpls experimental topmost 0'},
                                ' EXP1': {
                                    'match_all': True,
                                    'packets': 0,
                                    'bytes': 0,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0},
                                    'match': ' mpls experimental topmost 1'},
                                ' EXP2': {
                                    'match_all': True,
                                    'packets': 0,
                                    'bytes': 0,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0},
                                    'match': ' mpls experimental topmost 2'},
                                ' EXP3': {
                                    'match_all': True,
                                    'packets': 0,
                                    'bytes': 0,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0},
                                    'match': ' mpls experimental topmost 3'},
                                ' EXP4': {
                                    'match_all': True,
                                    'packets': 0,
                                    'bytes': 0,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0},
                                    'match': ' mpls experimental topmost 4'},
                                ' EXP5': {
                                    'match_all': True,
                                    'packets': 0,
                                    'bytes': 0,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0},
                                    'match': ' mpls experimental topmost 5'},
                                ' EXP6': {
                                    'match_all': True,
                                    'packets': 27,
                                    'bytes': 1869,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0},
                                    'match': ' mpls experimental topmost 6'},
                                ' EXP7': {
                                    'match_all': True,
                                    'packets': 0,
                                    'bytes': 0,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0},
                                    'match': ' mpls experimental topmost 7'},
                                ' class-default': {
                                    'match_all': False,
                                    'packets': 193,
                                    'bytes': 19600,
                                    'rate': {
                                        'interval': 300,
                                        'offered_rate_bps': 0,
                                        'drop_rate_bps': 0},
                                    'match': ' any'}}}}}}}}

    golden_output6 = {'execute.return_value': '''
        Router#show policy-map interface gigabitEthernet 0/0/0
        Load for five secs: 1%/0%; one minute: 4%; five minutes: 5%
        Time source is NTP, 14:58:52.473 JST Fri Oct 28 2016

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

    def test_show_policy_map_control_plane_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowPolicyMapType(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_show_policy_map_control_plane_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowPolicyMapType(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_policy_map_control_plane_full2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output2)
        obj = ShowPolicyMapType(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_policy_map_control_plane_full3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowPolicyMapType(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_show_policy_map_control_plane_full4(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output4)
        obj = ShowPolicyMapType(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output4)

    def test_show_policy_map_interface_full5(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output5)
        obj = ShowPolicyMapType(device=self.device)
        parsed_output = obj.parse(interface='gigabitEthernet 0/1/5', class_name='class-default')
        self.assertEqual(parsed_output, self.golden_parsed_output5)

    def test_show_policy_map_interface_full6(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output6)
        obj = ShowPolicyMapType(device=self.device)
        parsed_output = obj.parse(interface='gigabitEthernet 0/0/0')
        self.assertEqual(parsed_output, self.golden_parsed_output6)


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
        Time source is NTP, 22:28:37.624 JST Fri Nov 4 2016

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
                            'bc_bytes': 83619,
                            'conform_action': 'transmit',
                            'exceed_action': 'drop'}}}}}}

    golden_output2 = {'execute.return_value':'''

        Router#show policy-map police-in
        Load for five secs: 11%/0%; one minute: 4%; five minutes: 4%
        Time source is NTP, 07:03:58.319 JST Wed Oct 26 2016

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
                            'bc_bytes': 3000,
                            'be_bytes': 3000,
                            'conform_color': 'hipri-conform',
                            'conform_action': 'transmit',
                            'exceed_action': 'transmit',
                            'violate_action': 'drop',
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
                            'bc_bytes': 1500,
                            'conform_action': 'set-qos-transmit 5',
                            'exceed_action': 'drop'}},
                    'user2-acl-child': {
                        'police': {
                            'cir_bps': 20000,
                            'bc_bytes': 1500,
                            'conform_action': 'set-qos-transmit 5',
                            'exceed_action': 'drop'}},
                    'class-default': {
                        'police': {
                            'cir_bps': 50000,
                            'bc_bytes': 1500,
                            'conform_action': 'transmit',
                            'exceed_action': 'drop'}}}}}}

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
                            'class': {
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

    def test_show_policy_map_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowPolicyMap(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()