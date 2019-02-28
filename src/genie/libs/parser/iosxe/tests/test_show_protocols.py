# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxe show_protocols
from genie.libs.parser.iosxe.show_protocols import ShowIpProtocols


# =================================
# Unit test for 'show ip protocols'
# =================================
class test_show_ip_protocols(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
        'protocols': 
            {'application': 
                {'flushed': 0,
                'holddown': 0,
                'incoming_filter_list': 'not set',
                'invalid': 0,
                'maximum_path': 32,
                'outgoing_filter_list': 'not set',
                'preference': 
                    {'single_value': 
                        {'all': 4}},
                'update_frequency': 0},
            'bgp': 
                {'instance': 
                    {'default': 
                        {'bgp_id': 100,
                        'vrf': 
                            {'default': 
                                {'address_family': 
                                    {'ipv4': 
                                        {'automatic_route_summarization': False,
                                        'igp_sync': False,
                                        'incoming_filter_list': 'not set',
                                        'maximum_path': 1,
                                        'neighbor': 
                                            {'4.4.4.4': 
                                                {'distance': 200,
                                                'last_update': '03:34:58',
                                                'neighbor_id': '4.4.4.4'}},
                                        'outgoing_filter_list': 'not set',
                                        'preference': 
                                            {'multi_values': 
                                                {'external': 20,
                                                'internal': 200,
                                                'local': 200}}}}}}}}},
            'ospf': 
                {'vrf': 
                    {'default': 
                        {'address_family': 
                            {'ipv4': 
                                {'instance': 
                                    {'1': 
                                        {'areas': 
                                            {'0.0.0.0': 
                                                {'configured_interfaces': ['Loopback0', 'GigabitEthernet2', 'GigabitEthernet1']}},
                                        'incoming_filter_list': 'not set',
                                        'outgoing_filter_list': 'not set',
                                        'preference': 
                                            {'multi_values': 
                                                {'external': 114,
                                                'granularity': 
                                                    {'detail': 
                                                        {'inter_area': 113,
                                                        'intra_area': 112}}},
                                            'single_value': 
                                                {'all': 110}},
                                        'router_id': '1.1.1.1',
                                        'routing_information_sources': 
                                            {'gateway': 
                                                {'2.2.2.2': 
                                                    {'distance': 110,
                                                    'last_update': '07:33:00'},
                                                '3.3.3.3': 
                                                    {'distance': 110,
                                                    'last_update': '07:33:00'},
                                                '4.4.4.4': 
                                                    {'distance': 110,
                                                    'last_update': '00:19:15'}}},
                                        'spf_control': 
                                            {'paths': 4},
                                        'total_areas': 1,
                                        'total_normal_area': 1,
                                        'total_nssa_area': 0,
                                        'total_stub_area': 0}}}}}}}}}

    golden_parsed_output2 = {
        'protocols': 
            {'application': 
                {'flushed': 0,
                'holddown': 0,
                'incoming_filter_list': 'not set',
                'invalid': 0,
                'maximum_path': 32,
                'outgoing_filter_list': 'not set',
                'preference': {'single_value': {'all': 4}},
                'update_frequency': 0},
            'bgp': 
                {'instance': 
                    {'default': 
                        {'bgp_id': 1,
                        'vrf': 
                            {'default': 
                                {'address_family': 
                                    {'ipv4': 
                                        {'automatic_route_summarization': False,
                                        'igp_sync': False,
                                        'incoming_filter_list': 'not set',
                                        'maximum_path': 1,
                                        'neighbor': 
                                            {'192.168.0.9': 
                                                {'distance': 200,
                                                'last_update': '01:35:12',
                                                'neighbor_id': '192.168.0.9'}},
                                        'outgoing_filter_list': 'not set',
                                        'preference': 
                                            {'multi_values': 
                                                {'external': 20,
                                                'internal': 200,
                                                'local': 200}}}}}}}}},
            'ospf': 
                {'vrf': 
                    {'default': 
                        {'address_family': 
                            {'ipv4': 
                                {'instance': 
                                    {'1': 
                                        {'incoming_filter_list': 'not set',
                                        'outgoing_filter_list': 'not set',
                                        'passive_interfaces': ['Loopback0'],
                                        'preference': 
                                            {'single_value': 
                                                {'all': 110}},
                                        'router_id': '192.168.0.10',
                                        'routing_information_sources': 
                                            {'gateway': 
                                                {'192.168.0.9': 
                                                    {'distance': 110,
                                                    'last_update': '01:36:38'}}},
                                        'spf_control': 
                                            {'paths': 4},
                                        'total_areas': 1,
                                        'total_normal_area': 1,
                                        'total_nssa_area': 0,
                                        'total_stub_area': 0}}}}}}}}}

    golden_output3 = {'execute.return_value': '''
        show ip protocols
        *** IP Routing is NSF aware ***

        Routing Protocol is "application"
          Sending updates every 0 seconds
          Invalid after 0 seconds, hold down 0, flushed after 0
          Outgoing update filter list for all interfaces is not set
          Incoming update filter list for all interfaces is not set
          Maximum path: 32
          Routing for Networks:
          Routing Information Sources:
            Gateway         Distance      Last Update
          Distance: (default is 4)

        Routing Protocol is "isis banana"
          Outgoing update filter list for all interfaces is not set
          Incoming update filter list for all interfaces is not set
          Redistributing: isis banana
          Address Summarization:
            None
          Maximum path: 4
          Routing for Networks:
            TenGigabitEthernet0/0/26
            TenGigabitEthernet0/0/27
          Passive Interface(s):
            Loopback0
          Routing Information Sources:
            Gateway         Distance      Last Update
            11.139.6.3           115      05:56:34
            11.139.6.2           115      05:56:34
            11.139.6.4           115      05:56:34
            11.139.6.9           115      05:56:34
          Distance: (default is 115)

        Routing Protocol is "bgp 9999"
          Outgoing update filter list for all interfaces is not set
          Incoming update filter list for all interfaces is not set
          IGP synchronization is disabled
          Automatic route summarization is disabled
          Maximum path: 1
          Routing Information Sources:
            Gateway         Distance      Last Update
            11.139.6.3           200      12w5d
            11.139.6.2           200      14w4d
          Distance: external 20 internal 200 local 200
        '''}

    golden_parsed_output3 = {
        'protocols': 
            {'application': 
                {'flushed': 0,
                'holddown': 0,
                'incoming_filter_list': 'not set',
                'invalid': 0,
                'maximum_path': 32,
                'outgoing_filter_list': 'not set',
                'preference': 
                    {'single_value': 
                        {'all': 4}},
                'update_frequency': 0},
            'bgp': 
                {'instance': 
                    {'default': 
                        {'bgp_id': 9999,
                        'vrf': 
                            {'default': 
                                {'address_family': 
                                    {'ipv4': 
                                        {'automatic_route_summarization': False,
                                        'igp_sync': False,
                                        'incoming_filter_list': 'not set',
                                        'maximum_path': 1,
                                        'neighbor': 
                                            {'11.139.6.2': 
                                                {'distance': 200,
                                                'last_update': '14w4d',
                                                'neighbor_id': '11.139.6.2'},
                                            '11.139.6.3': 
                                                {'distance': 200,
                                                'last_update': '12w5d',
                                                'neighbor_id': '11.139.6.3'}},
                                        'outgoing_filter_list': 'not set',
                                        'preference': 
                                            {'multi_values': 
                                                {'external': 20,
                                                'internal': 200,
                                                'local': 200}}}}}}}}},
            'isis': 
                {'vrf': 
                    {'default': 
                        {'address_family': 
                            {'ipv4': 
                                {'instance': 
                                    {'banana': 
                                        {'configured_interfaces': ['TenGigabitEthernet0/0/26', 'TenGigabitEthernet0/0/27'],
                                        'incoming_filter_list': 'not set',
                                        'maximum_path': 4,
                                        'outgoing_filter_list': 'not set',
                                        'passive_interfaces': ['Loopback0'],
                                        'preference': 
                                            {'single_value': 
                                                {'all': 115}},
                                        'redistributing': 'isis banana',
                                        'routing_information_sources': 
                                            {'gateway': 
                                                {'11.139.6.2': 
                                                    {'distance': 115,
                                                    'last_update': '05:56:34'},
                                                '11.139.6.3': 
                                                    {'distance': 115,
                                                    'last_update': '05:56:34'},
                                                '11.139.6.4': 
                                                    {'distance': 115,
                                                    'last_update': '05:56:34'},
                                                '11.139.6.9': 
                                                    {'distance': 115,
                                                    'last_update': '05:56:34'}}}}}}}}}}}}

    golden_output4 = {'execute.return_value': '''
        Router# show ip protocols
        *** IP Routing is NSF aware ***
        Routing Protocol is "isis"
          Sending updates every 0 seconds
          Invalid after 0 seconds, hold down 0, flushed after 0
          Outgoing update filter list for all interfaces is not set
          Incoming update filter list for all interfaces is not set
          Redistributing: isis
          Address Summarization:
            None
          Routing for Networks:
            Serial0
          Routing Information Sources:
          Distance: (default is 115)
        '''}

    golden_parsed_output4 = {
        'protocols': 
            {'isis': 
                {'vrf': 
                    {'default': 
                        {'address_family': 
                            {'ipv4': 
                                {'instance': 
                                    {'default': 
                                        {'incoming_filter_list': 'not set',
                                        'outgoing_filter_list': 'not set',
                                        'preference': 
                                            {'single_value': {'all': 115}},
                                            'redistributing': 'isis'}}}}}}}}}

    def test_show_ip_protocols_full1(self):

        self.maxDiff = None

        def mapper(key):
            return self.outputs[key]

        raw1 = '''\
            R1_ospf_xe#show ip protocols 
            *** IP Routing is NSF aware ***

            Routing Protocol is "application"
              Sending updates every 0 seconds
              Invalid after 0 seconds, hold down 0, flushed after 0
              Outgoing update filter list for all interfaces is not set
              Incoming update filter list for all interfaces is not set
              Maximum path: 32
              Routing for Networks:
              Routing Information Sources:
                Gateway         Distance      Last Update
              Distance: (default is 4)

            Routing Protocol is "ospf 1"
              Outgoing update filter list for all interfaces is not set
              Incoming update filter list for all interfaces is not set
              Router ID 1.1.1.1
              Number of areas in this router is 1. 1 normal 0 stub 0 nssa
              Maximum path: 4
              Routing for Networks:
              Routing on Interfaces Configured Explicitly (Area 0):
                Loopback0
                GigabitEthernet2
                GigabitEthernet1
              Routing Information Sources:
                Gateway         Distance      Last Update
                3.3.3.3              110      07:33:00
                2.2.2.2              110      07:33:00
                4.4.4.4              110      00:19:15
              Distance: (default is 110)
              Distance: intra-area 112 inter-area 113 external 114

            Routing Protocol is "bgp 100"
              Outgoing update filter list for all interfaces is not set
              Incoming update filter list for all interfaces is not set
              IGP synchronization is disabled
              Automatic route summarization is disabled
              Maximum path: 1
              Routing Information Sources:
                Gateway         Distance      Last Update
                4.4.4.4              200      03:34:58
              Distance: external 20 internal 200 local 200
            '''

        raw2 = '''\
            R1_ospf_xe#show running-config | section router ospf 1
              router ospf 1
                mpls traffic-eng router-id Loopback0
                mpls traffic-eng area 0
            '''

        raw3 = '''\
            R1_ospf_xe#show running-config | section router ospf 2
              router ospf 2 vrf VRF1
                area 1 virtual-link 5.5.5.5
                area 1 sham-link 11.11.11.11 22.22.22.22 cost 111 ttl-security hops 3
                redistribute bgp
            '''

        self.outputs = {}
        self.outputs['show ip protocols'] = raw1
        self.outputs['show running-config | section router ospf 1'] = raw2
        self.outputs['show running-config | section router ospf 2'] = raw3

        self.device.execute = Mock()
        self.device.execute.side_effect = mapper
        
        obj = ShowIpProtocols(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output1)

    def test_show_ip_protocols_full2(self):
        
        self.maxDiff = None

        def mapper(key):
            return self.outputs[key]

        raw1 = '''\
            show ip protocols
            *** IP Routing is NSF aware ***

            Routing Protocol is "application"
              Sending updates every 0 seconds
              Invalid after 0 seconds, hold down 0, flushed after 0
              Outgoing update filter list for all interfaces is not set
              Incoming update filter list for all interfaces is not set
              Maximum path: 32
              Routing for Networks:
              Routing Information Sources:
                Gateway         Distance      Last Update
              Distance: (default is 4)

            Routing Protocol is "ospf 1"
              Outgoing update filter list for all interfaces is not set
              Incoming update filter list for all interfaces is not set
              Router ID 192.168.0.10
              Number of areas in this router is 1. 1 normal 0 stub 0 nssa
              Maximum path: 4
              Routing for Networks:
                10.0.0.84 0.0.0.3 area 11
                10.0.0.88 0.0.0.3 area 11
                192.168.0.10 0.0.0.0 area 11
              Passive Interface(s):
                Loopback0
              Routing Information Sources:
                Gateway         Distance      Last Update
                192.168.0.9          110      01:36:38
              Distance: (default is 110)

            Routing Protocol is "bgp 1"
              Outgoing update filter list for all interfaces is not set
              Incoming update filter list for all interfaces is not set
              IGP synchronization is disabled
              Automatic route summarization is disabled
              Neighbor(s):
                Address          FiltIn FiltOut DistIn DistOut Weight RouteMap
                192.168.0.9                                          
              Maximum path: 1
              Routing Information Sources:
                Gateway         Distance      Last Update
                192.168.0.9          200      01:35:12
              Distance: external 20 internal 200 local 200
            '''

        raw2 = '''\
            R1_ospf_xe#show running-config | section router ospf 1
              router ospf 1
                mpls traffic-eng router-id Loopback0
                mpls traffic-eng area 0
            '''

        raw3 = '''\
            R1_ospf_xe#show running-config | section router ospf 2
              router ospf 2 vrf VRF1
                area 1 virtual-link 5.5.5.5
                area 1 sham-link 11.11.11.11 22.22.22.22 cost 111 ttl-security hops 3
                redistribute bgp
            '''

        self.outputs = {}
        self.outputs['show ip protocols'] = raw1
        self.outputs['show running-config | section router ospf 1'] = raw2
        self.outputs['show running-config | section router ospf 2'] = raw3

        self.device.execute = Mock()
        self.device.execute.side_effect = mapper
        
        obj = ShowIpProtocols(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output2)

    def test_show_ip_protocols_full3(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output3)
        obj = ShowIpProtocols(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output3)

    def test_show_ip_protocols_full4(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output4)
        obj = ShowIpProtocols(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output4)

    def test_show_ip_protocols_empty(self):
        self.maxDiff = None
        self.device = Mock(**self.empty_output)
        obj = ShowIpProtocols(device=self.device)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()


if __name__ == '__main__':
    unittest.main()
