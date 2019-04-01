# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device
from ats.topology import loader

# Metaparser
from genie.metaparser.util.exceptions import SchemaEmptyParserError, SchemaMissingKeyError

# iosxe show_protocols
from genie.libs.parser.iosxe.show_protocols import ShowIpProtocols,\
                                                   ShowIpProtocolsSectionRip,\
                                                   ShowIpv6ProtocolsSectionRip

# =================================
# Unit test for 'show ip protocols'
# =================================
class test_show_ip_protocols(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output1 = {
    'protocols': {
        'ospf': {
            'vrf': {
                'default': {
                    'address_family': {
                        'ipv4': {
                            'instance': {
                                '1': {
                                    'areas': {
                                        '0.0.0.0': {
                                            'configured_interfaces': ['Loopback0', 'GigabitEthernet2', 'GigabitEthernet1'],
                                            },
                                        },
                                    'total_normal_area': 1,
                                    'router_id': '1.1.1.1',
                                    'outgoing_filter_list': 'not set',
                                    'routing_information_sources': {
                                        'gateway': {
                                            '3.3.3.3': {
                                                'last_update': '07:33:00',
                                                'distance': 110,
                                                },
                                            '4.4.4.4': {
                                                'last_update': '00:19:15',
                                                'distance': 110,
                                                },
                                            '2.2.2.2': {
                                                'last_update': '07:33:00',
                                                'distance': 110,
                                                },
                                            },
                                        },
                                    'total_stub_area': 0,
                                    'spf_control': {
                                        'paths': 4,
                                        },
                                    'total_nssa_area': 0,
                                    'preference': {
                                        'multi_values': {
                                            'granularity': {
                                                'detail': {
                                                    'inter_area': 113,
                                                    'intra_area': 112,
                                                    },
                                                },
                                            'external': 114,
                                            },
                                        'single_value': {
                                            'all': 110,
                                            },
                                        },
                                    'total_areas': 1,
                                    'incoming_filter_list': 'not set',
                                    },
                                },
                            },
                        },
                    },
                },
            },
        'bgp': {
            'instance': {
                'default': {
                    'bgp_id': 100,
                    'vrf': {
                        'default': {
                            'address_family': {
                                'ipv4': {
                                    'igp_sync': False,
                                    'automatic_route_summarization': False,
                                    'maximum_path': 1,
                                    'outgoing_filter_list': 'not set',
                                    'preference': {
                                        'multi_values': {
                                            'external': 20,
                                            'local': 200,
                                            'internal': 200,
                                            },
                                        },
                                    'neighbor': {
                                        '4.4.4.4': {
                                            'neighbor_id': '4.4.4.4',
                                            'last_update': '03:34:58',
                                            'distance': 200,
                                            },
                                        },
                                    'incoming_filter_list': 'not set',
                                    },
                                },
                            },
                        },
                    },
                },
            },
        'application': {
            'holddown': 0,
            'maximum_path': 32,
            'outgoing_filter_list': 'not set',
            'preference': {
                'single_value': {
                    'all': 4,
                    },
                },
            'update_frequency': 0,
            'flushed': 0,
            'invalid': 0,
            'incoming_filter_list': 'not set',
            },
        },
    }

    golden_parsed_output2 = {
    'protocols': {
        'ospf': {
            'vrf': {
                'default': {
                    'address_family': {
                        'ipv4': {
                            'instance': {
                                '1': {
                                    'passive_interfaces': ['Loopback0'],
                                    'total_areas': 1,
                                    'router_id': '192.168.0.10',
                                    'incoming_filter_list': 'not set',
                                    'routing_information_sources': {
                                        'gateway': {
                                            '192.168.0.9': {
                                                'distance': 110,
                                                'last_update': '01:36:38',
                                                },
                                            },
                                        },
                                    'outgoing_filter_list': 'not set',
                                    'total_normal_area': 1,
                                    'total_nssa_area': 0,
                                    'total_stub_area': 0,
                                    'spf_control': {
                                        'paths': 4,
                                        },
                                    'preference': {
                                        'single_value': {
                                            'all': 110,
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        'application': {
            'update_frequency': 0,
            'flushed': 0,
            'preference': {
                'single_value': {
                    'all': 4,
                    },
                },
            'incoming_filter_list': 'not set',
            'outgoing_filter_list': 'not set',
            'invalid': 0,
            'maximum_path': 32,
            'holddown': 0,
            },
        'bgp': {
            'instance': {
                'default': {
                    'bgp_id': 1,
                    'vrf': {
                        'default': {
                            'address_family': {
                                'ipv4': {
                                    'igp_sync': False,
                                    'automatic_route_summarization': False,
                                    'incoming_filter_list': 'not set',
                                    'maximum_path': 1,
                                    'neighbor': {
                                        '192.168.0.9': {
                                            'neighbor_id': '192.168.0.9',
                                            'distance': 200,
                                            'last_update': '01:35:12',
                                            },
                                        },
                                    'outgoing_filter_list': 'not set',
                                    'preference': {
                                        'multi_values': {
                                            'local': 200,
                                            'internal': 200,
                                            'external': 20,
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }

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
    'protocols': {
        'application': {
            'holddown': 0,
            'incoming_filter_list': 'not set',
            'update_frequency': 0,
            'preference': {
                'single_value': {
                    'all': 4,
                    },
                },
            'outgoing_filter_list': 'not set',
            'invalid': 0,
            'maximum_path': 32,
            'flushed': 0,
            },
        'isis': {
            'vrf': {
                'default': {
                    'address_family': {
                        'ipv4': {
                            'instance': {
                                'banana': {
                                    'routing_information_sources': {
                                        'gateway': {
                                            '11.139.6.3': {
                                                'last_update': '05:56:34',
                                                'distance': 115,
                                                },
                                            '11.139.6.9': {
                                                'last_update': '05:56:34',
                                                'distance': 115,
                                                },
                                            '11.139.6.2': {
                                                'last_update': '05:56:34',
                                                'distance': 115,
                                                },
                                            '11.139.6.4': {
                                                'last_update': '05:56:34',
                                                'distance': 115,
                                                },
                                            },
                                        },
                                    'incoming_filter_list': 'not set',
                                    'configured_interfaces': ['TenGigabitEthernet0/0/26', 'TenGigabitEthernet0/0/27'],
                                    'redistributing': 'isis banana',
                                    'passive_interfaces': ['Loopback0'],
                                    'outgoing_filter_list': 'not set',
                                    'preference': {
                                        'single_value': {
                                            'all': 115,
                                            },
                                        },
                                    'maximum_path': 4,
                                    },
                                },
                            },
                        },
                    },
                },
            },
        'bgp': {
            'instance': {
                'default': {
                    'bgp_id': 9999,
                    'vrf': {
                        'default': {
                            'address_family': {
                                'ipv4': {
                                    'igp_sync': False,
                                    'incoming_filter_list': 'not set',
                                    'preference': {
                                        'multi_values': {
                                            'local': 200,
                                            'external': 20,
                                            'internal': 200,
                                            },
                                        },
                                    'neighbor': {
                                        '11.139.6.3': {
                                            'neighbor_id': '11.139.6.3',
                                            'distance': 200,
                                            'last_update': '12w5d',
                                            },
                                        '11.139.6.2': {
                                            'neighbor_id': '11.139.6.2',
                                            'distance': 200,
                                            'last_update': '14w4d',
                                            },
                                        },
                                    'outgoing_filter_list': 'not set',
                                    'automatic_route_summarization': False,
                                    'maximum_path': 1,
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }

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
    'protocols': {
        'isis': {
            'vrf': {
                'default': {
                    'address_family': {
                        'ipv4': {
                            'instance': {
                                'default': {
                                    'preference': {
                                        'single_value': {
                                            'all': 115,
                                            },
                                        },
                                    'outgoing_filter_list': 'not set',
                                    'incoming_filter_list': 'not set',
                                    'redistributing': 'isis',
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }

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

    golden_parsed_output = {
    'protocols': {
        'rip': {
            'vrf': {
                'default': {
                    'address_family': {
                        'ipv4': {
                            'instance': {
                                'rip': {
                                    'receive_version': '2',
                                    'incoming_route_metric': {
                                        'list': '21',
                                        'added': '10',
                                        },
                                    'outgoing_update_filterlist': {
                                        'outgoing_update_filterlist': 'not set',
                                        },
                                    'maximum_paths': 4,
                                    'output_delay': 50,
                                    'neighbors': {
                                        '10.1.3.3': {
                                            'distance': 120,
                                            'last_update': '00:00:00',
                                            },
                                        '10.1.2.2': {
                                            'distance': 120,
                                            'last_update': '00:00:04',
                                            },
                                        },
                                    'incoming_update_filterlist': {
                                        'incoming_update_filterlist': 'not set',
                                        },
                                    'default_redistribution_metric': 3,
                                    'automatic_network_summarization_in_effect': False,
                                    'redistribute': {
                                        'rip': {
                                            },
                                        'static': {
                                            },
                                        'connected': {
                                            },
                                        },
                                    'timers': {
                                        'flush_interval': 23,
                                        'invalid_interval': 21,
                                        'holddown_interval': 22,
                                        'next_update': 8,
                                        'update_interval': 10,
                                        },
                                    'send_version': '2',
                                    'network': ['10.0.0.0'],
                                    'distance': 120,
                                    'interfaces': {
                                        'GigabitEthernet3.100': {
                                            'receive_version': '2',
                                            'triggered_rip': 'no',
                                            'passive': True,
                                            'send_version': '2',
                                            'summary_address': {
                                                '172.16.0.0/17': {
                                                    },
                                                },
                                            'key_chain': '1',
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        'application': {
            'outgoing_filter_list': 'not set',
            'incoming_filter_list': 'not set',
            'holddown': 0,
            'maximum_path': 32,
            'invalid': 0,
            'flushed': 0,
            'preference': {
                'single_value': {
                    'all': 4,
                    },
                },
            'update_frequency': 0,
            },
        },
    }
    golden_output = {'execute.return_value': '''\
    R1#show ip protocols
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

        Routing Protocol is "rip"
          Output delay 50 milliseconds between packets
          Outgoing update filter list for all interfaces is not set
          Incoming update filter list for all interfaces is not set
          Incoming routes will have 10 added to metric if on list 21
          Sending updates every 10 seconds, next due in 8 seconds
          Invalid after 21 seconds, hold down 22, flushed after 23
          Default redistribution metric is 3
          Redistributing: connected, static, rip
          Neighbor(s):
            10.1.2.2
          Default version control: send version 2, receive version 2
            Interface                           Send  Recv  Triggered RIP  Key-chain
            GigabitEthernet3.100                2     2          No        1
          Automatic network summarization is not in effect
          Address Summarization:
            172.16.0.0/17 for GigabitEthernet3.100
          Maximum path: 4
          Routing for Networks:
            10.0.0.0
          Passive Interface(s):
            GigabitEthernet2.100
          Routing Information Sources:
            Gateway         Distance      Last Update
            10.1.3.3             120      00:00:00
            10.1.2.2             120      00:00:04
          Distance: (default is 120)

        '''}

    golden_parsed_output_5 = {
    'protocols': {
        'rip': {
            'vrf': {
                'VRF1': {
                    'address_family': {
                        'ipv4': {
                            'instance': {
                                'rip': {
                                    'redistribute': {
                                        'connected': {
                                            },
                                        'rip': {
                                            },
                                        'static': {
                                            },
                                        },
                                    'outgoing_update_filterlist': {
                                        'interfaces': {
                                            'GigabitEthernet3.100': {
                                                'filter': '130',
                                                'per_user': True,
                                                'default': 'not set',
                                                },
                                            'GigabitEthernet2.100': {
                                                'filter': '150',
                                                'per_user': True,
                                                'default': 'not set',
                                                },
                                            },
                                        'outgoing_update_filterlist': '150',
                                        },
                                    'maximum_paths': 4,
                                    'timers': {
                                        'update_interval': 30,
                                        'next_update': 2,
                                        'flush_interval': 240,
                                        'holddown_interval': 180,
                                        'invalid_interval': 180,
                                        },
                                    'network': ['10.0.0.0'],
                                    'output_delay': 50,
                                    'neighbors': {
                                        '10.1.3.3': {
                                            'distance': 120,
                                            'last_update': '20:33:00',
                                            },
                                        '10.1.2.2': {
                                            'distance': 120,
                                            'last_update': '00:00:21',
                                            },
                                        },
                                    'interfaces': {
                                        'GigabitEthernet3.200': {
                                            'triggered_rip': 'no',
                                            'send_version': '1 2',
                                            'key_chain': 'none',
                                            'receive_version': '2',
                                            },
                                        'GigabitEthernet2.200': {
                                            'triggered_rip': 'no',
                                            'send_version': '2',
                                            'key_chain': 'none',
                                            'receive_version': '2',
                                            },
                                        },
                                    'distance': 120,
                                    'incoming_update_filterlist': {
                                        'interfaces': {
                                            'GigabitEthernet2.100': {
                                                'filter': '13',
                                                'per_user': True,
                                                'default': 'not set',
                                                },
                                            },
                                        'incoming_update_filterlist': '100',
                                        },
                                    'send_version': '2',
                                    'receive_version': '2',
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }
    golden_output_5 = {'execute.return_value': '''
    R1#show ip protocols vrf VRF1
    Routing Protocol is "rip"
      Output delay 50 milliseconds between packets
      Outgoing update filter list for all interfaces is 150
        GigabitEthernet2.100 filtered by 150 (per-user), default is not set
        GigabitEthernet3.100 filtered by 130 (per-user), default is not set
      Incoming update filter list for all interfaces is 100
        GigabitEthernet2.100 filtered by 13 (per-user), default is not set
      Sending updates every 30 seconds, next due in 2 seconds
      Invalid after 180 seconds, hold down 180, flushed after 240
      Redistributing: connected, static, rip
      Default version control: send version 2, receive version 2
        Interface                           Send  Recv  Triggered RIP  Key-chain
        GigabitEthernet2.200                2     2          No        none
        GigabitEthernet3.200                1 2   2          No        none
      Maximum path: 4
      Routing for Networks:
         10.0.0.0
        10.0.0.0
      Routing Information Sources:
        Gateway         Distance      Last Update
        10.1.3.3             120      20:33:00
        10.1.2.2             120      00:00:21
      Distance: (default is 120)
    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowIpProtocols(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_vrf_default(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpProtocols(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_vrf_vrf1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_5)
        obj = ShowIpProtocols(device=self.device)
        parsed_output = obj.parse(vrf="VRF1")
        self.assertEqual(parsed_output, self.golden_parsed_output_5)


# ============================================
# Parser for 'show ip protocols | sec rip'
# Parser for 'show ip protocols vrf {vrf} | sec rip'
# ============================================
class test_show_ip_protocols_section_rip(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
    'protocols': {
        'rip': {
            'vrf': {
                'default': {
                    'address_family': {
                        'ipv4': {
                            'instance': {
                                'rip': {
                                    'timers': {
                                        'next_update': 8,
                                        'flush_interval': 23,
                                        'update_interval': 10,
                                        'invalid_interval': 21,
                                        'holddown_interval': 22,
                                        },
                                    'default_redistribution_metric': 3,
                                    'redistribute': {
                                        'rip': {
                                            },
                                        'connected': {
                                            },
                                        'static': {
                                            },
                                        },
                                    'automatic_network_summarization_in_effect': False,
                                    'send_version': '2',
                                    'distance': 120,
                                    'incoming_route_metric': {
                                        'added': '10',
                                        'list': '21',
                                        },
                                    'neighbors': {
                                        '10.1.2.2': {
                                            'distance': 120,
                                            'last_update': '00:00:04',
                                            },
                                        '10.1.3.3': {
                                            'distance': 120,
                                            'last_update': '00:00:00',
                                            },
                                        },
                                    'maximum_paths': 4,
                                    'receive_version': '2',
                                    'interfaces': {
                                        'GigabitEthernet3.100': {
                                            'receive_version': '2',
                                            'summary_address': {
                                                '172.16.0.0/17': {
                                                    },
                                                },
                                            'triggered_rip': 'no',
                                            'send_version': '2',
                                            'key_chain': '1',
                                            'passive': True,
                                            },
                                        },
                                    'incoming_update_filterlist': {
                                        'incoming_update_filterlist': 'not set',
                                        },
                                    'network': ['10.0.0.0'],
                                    'output_delay': 50,
                                    'outgoing_update_filterlist': {
                                        'outgoing_update_filterlist': 'not set',
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }

    golden_output = {'execute.return_value': '''\
R1#show ip protocols | sec rip
Routing Protocol is "rip"
  Output delay 50 milliseconds between packets
  Outgoing update filter list for all interfaces is not set
  Incoming update filter list for all interfaces is not set
  Incoming routes will have 10 added to metric if on list 21
  Sending updates every 10 seconds, next due in 8 seconds
  Invalid after 21 seconds, hold down 22, flushed after 23
  Default redistribution metric is 3
  Redistributing: connected, static, rip
  Neighbor(s):
    10.1.2.2
  Default version control: send version 2, receive version 2
    Interface                           Send  Recv  Triggered RIP  Key-chain
    GigabitEthernet3.100                2     2          No        1
  Automatic network summarization is not in effect
  Address Summarization:
    172.16.0.0/17 for GigabitEthernet3.100
  Maximum path: 4
  Routing for Networks:
    10.0.0.0
  Passive Interface(s):
    GigabitEthernet2.100
  Routing Information Sources:
    Gateway         Distance      Last Update
    10.1.3.3             120      00:00:00
    10.1.2.2             120      00:00:04
  Distance: (default is 120)

    '''}

    golden_parsed_output_2 = {
    'protocols': {
        'rip': {
            'vrf': {
                'VRF1': {
                    'address_family': {
                        'ipv4': {
                            'instance': {
                                'rip': {
                                    'timers': {
                                        'holddown_interval': 180,
                                        'flush_interval': 240,
                                        'invalid_interval': 180,
                                        'update_interval': 30,
                                        'next_update': 2,
                                        },
                                    'send_version': '2',
                                    'interfaces': {
                                        'GigabitEthernet2.200': {
                                            'triggered_rip': 'no',
                                            'receive_version': '2',
                                            'send_version': '2',
                                            'key_chain': 'none',
                                            },
                                        'GigabitEthernet3.200': {
                                            'triggered_rip': 'no',
                                            'receive_version': '2',
                                            'send_version': '1 2',
                                            'key_chain': 'none',
                                            },
                                        },
                                    'neighbors': {
                                        '10.1.2.2': {
                                            'last_update': '00:00:21',
                                            'distance': 120,
                                            },
                                        '10.1.3.3': {
                                            'last_update': '20:33:00',
                                            'distance': 120,
                                            },
                                        },
                                    'redistribute': {
                                        'connected': {
                                            },
                                        'static': {
                                            },
                                        'rip': {
                                            },
                                        },
                                    'maximum_paths': 4,
                                    'receive_version': '2',
                                    'outgoing_update_filterlist': {
                                        'interfaces': {
                                            'GigabitEthernet2.100': {
                                                'per_user': True,
                                                'default': 'not set',
                                                'filter': '150',
                                                },
                                            'GigabitEthernet3.100': {
                                                'per_user': True,
                                                'default': 'not set',
                                                'filter': '130',
                                                },
                                            },
                                        'outgoing_update_filterlist': '150',
                                        },
                                    'distance': 120,
                                    'network': ['10.0.0.0'],
                                    'output_delay': 50,
                                    'incoming_update_filterlist': {
                                        'interfaces': {
                                            'GigabitEthernet2.100': {
                                                'per_user': True,
                                                'default': 'not set',
                                                'filter': '13',
                                                },
                                            },
                                        'incoming_update_filterlist': '100',
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }
    golden_output_2 = {'execute.return_value': '''
R1#show ip protocols vrf VRF1 | sec rip
Routing Protocol is "rip"
  Output delay 50 milliseconds between packets
  Outgoing update filter list for all interfaces is 150
    GigabitEthernet2.100 filtered by 150 (per-user), default is not set
    GigabitEthernet3.100 filtered by 130 (per-user), default is not set
  Incoming update filter list for all interfaces is 100
    GigabitEthernet2.100 filtered by 13 (per-user), default is not set
  Sending updates every 30 seconds, next due in 2 seconds
  Invalid after 180 seconds, hold down 180, flushed after 240
  Redistributing: connected, static, rip
  Default version control: send version 2, receive version 2
    Interface                           Send  Recv  Triggered RIP  Key-chain
    GigabitEthernet2.200                2     2          No        none
    GigabitEthernet3.200                1 2   2          No        none
  Maximum path: 4
  Routing for Networks:
     10.0.0.0
    10.0.0.0
  Routing Information Sources:
    Gateway         Distance      Last Update
    10.1.3.3             120      20:33:00
    10.1.2.2             120      00:00:21
  Distance: (default is 120)
'''}

    golden_parsed_output_3 = {
'protocols': {
    'rip': {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv4': {
                        'instance': {
                            'rip': {
                                'incoming_update_filterlist': {
                                    'incoming_update_filterlist': 'not set',
                                    },
                                'distance': 120,
                                'receive_version': 'any',
                                'redistribute': {
                                    'rip': {
                                        },
                                    },
                                'interfaces': {
                                    'Loopback3': {
                                        'triggered_rip': 'no',
                                        'key_chain': 'none',
                                        'receive_version': '2',
                                        'send_version': '2',
                                        },
                                    'Vlan203': {
                                        'triggered_rip': 'no',
                                        'key_chain': 'none',
                                        'receive_version': '2',
                                        'send_version': '2',
                                        },
                                    'Vlan103': {
                                        'triggered_rip': 'no',
                                        'key_chain': 'none',
                                        'receive_version': '2',
                                        'send_version': '2',
                                        },
                                    },
                                'automatic_network_summarization_in_effect': True,
                                'network': ['201.3.14.0'],
                                'send_version': '1',
                                'timers': {
                                    'update_interval': 30,
                                    'holddown_interval': 180,
                                    'invalid_interval': 180,
                                    'flush_interval': 240,
                                    'next_update': 10,
                                    },
                                'neighbors': {
                                    '201.3.14.2': {
                                        'distance': 120,
                                        'last_update': '1w3d',
                                        },
                                    },
                                'outgoing_update_filterlist': {
                                    'outgoing_update_filterlist': 'not set',
                                    },
                                'maximum_paths': 4,
                                },
                            },
                        },
                    },
                },
            },
        },
    },
}
    golden_output_3 = {'execute.return_value': '''
    R1#show ip protocols | section rip
    Routing Protocol is "rip"
      Outgoing update filter list for all interfaces is not set
      Incoming update filter list for all interfaces is not set
      Sending updates every 30 seconds, next due in 10 seconds
      Invalid after 180 seconds, hold down 180, flushed after 240
      Redistributing: rip
      Default version control: send version 1, receive any version
        Interface                           Send  Recv  Triggered RIP  Key-chain
        Vlan103                             2     2          No        none            
        Vlan203                             2     2          No        none            
        Loopback3                           2     2          No        none            
      Automatic network summarization is in effect
      Maximum path: 4
      Routing for Networks:
        201.3.14.0
      Routing Information Sources:
        Gateway         Distance      Last Update
        201.3.14.2           120      1w3d
      Distance: (default is 120)
    R1#
    '''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowIpProtocolsSectionRip(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_vrf_default(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpProtocolsSectionRip(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_vrf_vrf1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowIpProtocolsSectionRip(device=self.device)
        parsed_output = obj.parse(vrf="VRF1")
        self.assertEqual(parsed_output, self.golden_parsed_output_2)

    def test_golden_2(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_3)
        obj = ShowIpProtocolsSectionRip(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output_3)


# ============================================
# Parser for 'show ipv6 protocols | sec rip'
# Parser for 'show ipv6 protocols vrf {vrf} | sec rip'
# ============================================
class test_show_ipv6_protocols(unittest.TestCase):
    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}

    golden_parsed_output = {
        'vrf': {
            'default': {
                'address_family': {
                    'ipv6': {
                        'instance': {
                            'rip ripng': {
                                'redistribute': {
                                    'static': {
                                        'metric': 3,
                                    },
                                },
                                'interfaces': {
                                    'GigabitEthernet3.100': {},
                                    'GigabitEthernet2.100': {},
                                },
                            },
                        },
                    },
                },
            },
        },
    }

    golden_output = {'execute.return_value': '''\
R1#show ipv6 protocols | sec rip
IPv6 Routing Protocol is "rip ripng"
  Interfaces:
    GigabitEthernet3.100
    GigabitEthernet2.100
  Redistribution:
    Redistributing protocol static with metric 3
    '''}

    golden_parsed_output_2 = {
        'vrf': {
            'VRF1': {
                'address_family': {
                    'ipv6': {
                        'instance': {
                            'rip ripng': {
                                'redistribute': {
                                    'static': {
                                        'route_policy': 'static-to-rip',
                                    },
                                    'connected': {},
                                },
                                'interfaces': {
                                    'GigabitEthernet3.200': {},
                                    'GigabitEthernet2.200': {},
                                },
                            },
                        },
                    },
                },
            },
        },
    }
    golden_output_2 = {'execute.return_value': '''
R1#show ipv6 protocols vrf VRF1 | sec rip
IPv6 Routing Protocol is "rip ripng"
  Interfaces:
    GigabitEthernet3.200
    GigabitEthernet2.200
  Redistribution:
    Redistributing protocol connected with transparent metric
    Redistributing protocol static with transparent metric route-map static-to-rip
'''}

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowIpv6ProtocolsSectionRip(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_vrf_default(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output)
        obj = ShowIpv6ProtocolsSectionRip(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

    def test_golden_vrf_vrf1(self):
        self.maxDiff = None
        self.device = Mock(**self.golden_output_2)
        obj = ShowIpv6ProtocolsSectionRip(device=self.device)
        parsed_output = obj.parse(vrf="VRF1")
        self.assertEqual(parsed_output, self.golden_parsed_output_2)


if __name__ == '__main__':
    unittest.main()
