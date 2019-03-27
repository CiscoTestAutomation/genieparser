# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxe show_monitor
from genie.libs.parser.iosxe.show_policy_map import ShowPolicyMapControlPlane


# =============================================
# Unit test for 'show policy map control plane'
# =============================================
class test_show_policy_map_control_plane(unittest.TestCase):
    '''Unit test for "how policy map control plane" '''

    device = Device(name='aDevice')

    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 ={
        'Control Plane':
            {'service_policy':
                {'input':
                    {'policy_name':
                        {'Control_Plane_In':
                            {'class_map':
                                {'Ping_Class':
                                    {'match_all': True,
                                     'packets': 0,
                                     'bytes': 0,
                                     'rate':
                                        {'interval': 300,
                                         'offered_rate_bps': 0,
                                         'drop_rate_bps': 0},
                                     'match': 'access-group name Ping_Option',
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
                                'TELNET_Class':
                                    {'match_all': True,
                                     'packets': 0,
                                     'bytes': 0,
                                     'rate':
                                        {'interval': 300,
                                         'offered_rate_bps': 0,
                                         'drop_rate_bps': 0},
                                     'match': 'access-group name TELNET_Permit',
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
                                'TACACS_Class':
                                    {'match_all': True,
                                     'packets': 0,
                                     'bytes': 0,
                                     'rate':
                                         {'interval': 300,
                                          'offered_rate_bps': 0,
                                          'drop_rate_bps': 0},
                                     'match': 'access-group name TACACS_Permit',
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
                                'SNMP_Class':
                                    {'match_all': True,
                                     'packets': 0,
                                     'bytes': 0,
                                     'rate':
                                         {'interval': 300,
                                          'offered_rate_bps': 0,
                                          'drop_rate_bps': 0},
                                     'match': 'access-group name SNMP_Permit',
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
                                'FTP_Class':
                                    {'match_all': True,
                                     'packets': 0,
                                     'bytes': 0,
                                     'rate':
                                         {'interval': 300,
                                          'offered_rate_bps': 0,
                                          'drop_rate_bps': 0},
                                     'match': 'access-group name FTP_Permit',
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
                                'BGP_Class':
                                    {'match_all': True,
                                     'packets': 32,
                                     'bytes': 2032,
                                     'rate':
                                         {'interval': 300,
                                          'offered_rate_bps': 0,
                                          'drop_rate_bps': 0},
                                     'match': 'access-group name BGP_Permit',
                                     'qos_set':
                                         {'ip_precedence': 6,
                                          'marker_statistics': 'Disabled'}},
                                'OSPF_Class':
                                    {'match_all': True,
                                     'packets': 58,
                                     'bytes': 11788,
                                     'rate':
                                         {'interval': 300,
                                          'offered_rate_bps': 0,
                                          'drop_rate_bps': 0},
                                     'match': 'access-group name OSPF_Permit',
                                     'qos_set':
                                         {'ip_precedence': 6,
                                          'marker_statistics': 'Disabled'}},
                                'LDP_Class':
                                    {'match_all': True,
                                     'packets': 128,
                                     'bytes': 9552,
                                     'rate':
                                         {'interval': 300,
                                          'offered_rate_bps': 0,
                                          'drop_rate_bps': 0},
                                     'match': 'access-group name LDP_Permit',
                                     'qos_set':
                                         {'ip_precedence': 6,
                                          'marker_statistics': 'Disabled'}},
                                'ICMP_Class1':
                                    {'match_all': True,
                                     'packets': 0,
                                     'bytes': 0,
                                     'rate':
                                         {'interval': 300,
                                          'offered_rate_bps': 0,
                                          'drop_rate_bps': 0},
                                     'match': 'access-group name ICMP_Permit1',
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
                                'ICMP_Class2':
                                    {'match_all': True,
                                     'packets': 4,
                                     'bytes': 482,
                                     'rate':
                                         {'interval': 300,
                                          'offered_rate_bps': 0,
                                          'drop_rate_bps': 0},
                                     'match': 'access-group name ICMP_Permit2',
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
                                'NTP_Class':
                                     {'match_all': True,
                                      'packets': 3,
                                      'bytes': 330,
                                      'rate':
                                          {'interval': 300,
                                           'offered_rate_bps': 0,
                                           'drop_rate_bps': 0},
                                      'match': 'access-group name NTP_Permit',
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
                                'ALL_Class':
                                    {'match_all': True,
                                     'packets': 23,
                                     'bytes': 1548,
                                     'rate':
                                         {'interval': 300,
                                          'offered_rate_bps': 0,
                                          'drop_rate_bps': 0},
                                     'match': 'access-group name ALL_Permit',
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
                                'class-default':
                                    {'match_all': False,
                                     'packets': 276,
                                     'bytes': 16554,
                                     'rate':
                                         {'interval': 300,
                                          'offered_rate_bps': 0,
                                          'drop_rate_bps': 0},
                                     'match': 'any'}}}}}}}}


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
              Router#

                          '''}

    def test_show_policy_map_control_plane_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowPolicyMapControlPlane(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse(name='control-plane')

    def test_show_policy_map_control_plane_full1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output1)
        obj = ShowPolicyMapControlPlane(device=self.device)
        parsed_output = obj.parse(name='control-plane')
        self.assertEqual(parsed_output, self.golden_parsed_output1)


if __name__ == '__main__':
    unittest.main()
