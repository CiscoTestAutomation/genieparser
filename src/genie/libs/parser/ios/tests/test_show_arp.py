# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

# Parser
from genie.libs.parser.ios.show_arp import ShowIpArp, \
                                           ShowIpArpSummary,\
                                           ShowIpTraffic, \
                                           ShowArpApplication, \
                                           ShowArpSummary, \
                                           ShowArp

from genie.libs.parser.iosxe.tests.test_show_arp import test_show_arp_application as \
                                                 test_show_arp_application_iosxe, \
                                                 test_show_arp_summary as \
                                                 test_show_arp_summary_iosxe, \
                                                 test_show_arp as \
                                                 test_show_arp_iosxe
# ============================================
# Parser for 'show arp [vrf <WORD>] <WROD>'
# ============================================
class test_show_ip_arp(unittest.TestCase):
		
		device = Device(name='aDevice')
		empty_output = {'execute.return_value': ''}
		
		golden_parsed_output = {
			'interfaces': {
				'FastEthernet0': {
					'ipv4': {
						'neighbors': {
							'10.1.8.1': {
								'age': '79',
                              	'ip': '10.1.8.1',
                              	'link_layer_address': '0012.7f57.ac80',
                              	'origin': 'dynamic',
                              	'protocol': 'Internet',
                              	'type': 'ARPA'},
			                '10.1.8.146': {
			                	'age': '-',
                                'ip': '10.1.8.146',
                                'link_layer_address': '843d.c638.b9b7',
                                'origin': 'static',
                                'protocol': 'Internet',
                                'type': 'ARPA'}}}},
                'Port-channel10': {
                	'ipv4': {
                		'neighbors': {
                			'10.9.1.1': {
                				'age': '-',
                              	'ip': '10.9.1.1',
                              	'link_layer_address': '843d.c638.b9c6',
                              	'origin': 'static',
                              	'protocol': 'Internet',
                              	'type': 'ARPA'}}}},
                'Vlan99': {
                	'ipv4': {
                		'neighbors': {
                			'10.69.1.2': {
                				'age': '-',
                               	'ip': '10.69.1.2',
                              	'link_layer_address': '843d.c638.b9c1',
                               	'origin': 'static',
                               	'protocol': 'Internet',
                               	'type': 'ARPA'}
                        }
                    }
                }
            }
        }

		golden_output = {'execute.return_value': '''\
			R5#show ip arp 
			Protocol  Address          Age (min)  Hardware Addr   Type   Interface
			Internet  10.1.8.1               79   0012.7f57.ac80  ARPA   FastEthernet0
			Internet  10.9.1.1                -   843d.c638.b9c6  ARPA   Port-channel10
			Internet  10.69.1.2               -   843d.c638.b9c1  ARPA   Vlan99
			Internet  10.1.8.146              -   843d.c638.b9b7  ARPA   FastEthernet0
		'''}

		golden_parsed_output_1 = {
			'interfaces': {
				'FastEthernet0': {
					'ipv4': {
						'neighbors': {
							'10.1.8.1': {
								'age': '79',
                              	'ip': '10.1.8.1',
                              	'link_layer_address': '0012.7f57.ac80',
                              	'origin': 'dynamic',
                              	'protocol': 'Internet',
                              	'type': 'ARPA'},
                            '10.1.8.146': {
                            	'age': '-',
                                'ip': '10.1.8.146',
                                'link_layer_address': '843d.c638.b9b7',
                                'origin': 'static',
                                'protocol': 'Internet',
                                'type': 'ARPA'}
                        }
                    }
                }
            }
        }

		golden_output_1 = {'execute.return_value': '''\
			R5#show ip arp 
			Protocol  Address          Age (min)  Hardware Addr   Type   Interface
			Internet  10.1.8.1               79   0012.7f57.ac80  ARPA   FastEthernet0
			Internet  10.1.8.146              -   843d.c638.b9b7  ARPA   FastEthernet0
		'''}

		def test_empty(self):
				self.device1 = Mock(**self.empty_output)
				obj = ShowIpArp(device=self.device1)
				with self.assertRaises(SchemaEmptyParserError):
						parsed_output = obj.parse()

		def test_golden(self):
				self.device = Mock(**self.golden_output)
				obj = ShowIpArp(device=self.device)
				parsed_output = obj.parse()
				self.assertEqual(parsed_output,self.golden_parsed_output)

		def test_golden_1(self):
				self.device = Mock(**self.golden_output_1)
				obj = ShowIpArp(device=self.device)
				parsed_output = obj.parse(vrf='Mgmt-vrf',
					intf_or_ip='FastEthernet0')
				self.assertEqual(parsed_output,self.golden_parsed_output_1)

#=========================================================
# Unit test for show ip arp summary
#=========================================================
class test_show_ip_arp_summary(unittest.TestCase):

		device = Device(name='aDevice')
		empty_output = {'execute.return_value': ''}

		golden_parsed_output = {
				'incomp_entries': 0,
				'total_entries': 4}

		golden_output = {'execute.return_value': '''
			R5#show ip arp summary 
			4 IP ARP entries, with 0 of them incomplete
		'''
		}

		def test_empty(self):
				self.device = Mock(**self.empty_output)
				obj = ShowIpArpSummary(device=self.device)
				with self.assertRaises(SchemaEmptyParserError):
						parsed_output = obj.parse()

		def test_golden(self):
				self.maxDiff = None
				self.device = Mock(**self.golden_output)
				obj = ShowIpArpSummary(device=self.device)
				parsed_output = obj.parse()
				self.assertEqual(parsed_output, self.golden_parsed_output)

#=========================================================
# Unit test for show ip traffic
#=========================================================
class test_show_ip_traffic(unittest.TestCase):

		device = Device(name='aDevice')
		empty_output = {'execute.return_value': ''}

		golden_parsed_output = {'arp_statistics': {'arp_drops_input_full': 0,
                    'arp_in_other': 0,
                    'arp_in_replies': 25520,
                    'arp_in_requests': 26338,
                    'arp_in_reverse': 42,
                    'arp_out_proxy': 0,
                    'arp_out_replies': 1399,
                    'arp_out_requests': 123,
                    'arp_out_reverse': 0},
 'bgp_statistics': {'bgp_received_keepalives': 0,
                    'bgp_received_notifications': 0,
                    'bgp_received_opens': 0,
                    'bgp_received_route_refresh': 0,
                    'bgp_received_total': 0,
                    'bgp_received_unrecognized': 0,
                    'bgp_received_updates': 0,
                    'bgp_sent_keepalives': 0,
                    'bgp_sent_notifications': 0,
                    'bgp_sent_opens': 0,
                    'bgp_sent_route_refresh': 0,
                    'bgp_sent_total': 0,
                    'bgp_sent_updates': 0},
 'eigrp_ipv4_statistics': {'eigrp_ipv4_received_total': 0,
                           'eigrp_ipv4_sent_total': 0},
 'icmp_statistics': {'icmp_received_checksum_errors': 0,
                     'icmp_received_echo': 43838,
                     'icmp_received_echo_reply': 713,
                     'icmp_received_format_errors': 0,
                     'icmp_received_info_request': 0,
                     'icmp_received_irdp_advertisements': 0,
                     'icmp_received_irdp_solicitations': 0,
                     'icmp_received_mask_replies': 0,
                     'icmp_received_mask_requests': 0,
                     'icmp_received_other': 0,
                     'icmp_received_parameter': 0,
                     'icmp_received_quench': 0,
                     'icmp_received_redirects': 0,
                     'icmp_received_timestamp': 0,
                     'icmp_received_unreachable': 0,
                     'icmp_sent_echo': 730,
                     'icmp_sent_echo_reply': 43838,
                     'icmp_sent_info_reply': 0,
                     'icmp_sent_irdp_advertisements': 0,
                     'icmp_sent_irdp_solicitations': 0,
                     'icmp_sent_mask_replies': 0,
                     'icmp_sent_mask_requests': 0,
                     'icmp_sent_parameter_problem': 0,
                     'icmp_sent_quench': 0,
                     'icmp_sent_redirects': 0,
                     'icmp_sent_time_exceeded': 0,
                     'icmp_sent_timestamp': 0,
                     'icmp_sent_unreachable': 4},
 'igmp_statistics': {'igmp_checksum_errors': '0/0',
                     'igmp_dvmrp': '0/0',
                     'igmp_format_errors': '0/0',
                     'igmp_host_leaves': '0/0',
                     'igmp_host_queries': '0/0',
                     'igmp_host_reports': '0/0',
                     'igmp_pim': '0/0',
                     'igmp_total': '0/0'},
 'ip_statistics': {'ip_bcast_received': 653921,
                   'ip_bcast_sent': 6,
                   'ip_drop_encap_failed': 10,
                   'ip_drop_forced_drop': 0,
                   'ip_drop_no_adj': 0,
                   'ip_drop_no_route': 0,
                   'ip_drop_opts_denied': 0,
                   'ip_drop_src_ip': 0,
                   'ip_drop_unicast_rpf': 0,
                   'ip_drop_unresolved': 0,
                   'ip_frags_fragmented': 0,
                   'ip_frags_no_fragmented': 0,
                   'ip_frags_no_reassembled': 0,
                   'ip_frags_reassembled': 0,
                   'ip_frags_timeouts': 0,
                   'ip_mcast_received': 0,
                   'ip_mcast_sent': 0,
                   'ip_opts_alert': 0,
                   'ip_opts_basic_security': 0,
                   'ip_opts_cipso': 0,
                   'ip_opts_end': 0,
                   'ip_opts_extended_security': 0,
                   'ip_opts_loose_src_route': 0,
                   'ip_opts_nop': 0,
                   'ip_opts_other': 0,
                   'ip_opts_record_route': 0,
                   'ip_opts_strct_src_route': 0,
                   'ip_opts_strm_id': 0,
                   'ip_opts_timestamp': 0,
                   'ip_opts_ump': 0,
                   'ip_rcvd_bad_hop': 811,
                   'ip_rcvd_bad_optns': 0,
                   'ip_rcvd_checksum_errors': 0,
                   'ip_rcvd_format_errors': 0,
                   'ip_rcvd_local_destination': 843331,
                   'ip_rcvd_not_gateway': 6,
                   'ip_rcvd_sec_failures': 0,
                   'ip_rcvd_total': 844148,
                   'ip_rcvd_unknwn_protocol': 0,
                   'ip_rcvd_with_optns': 0,
                   'ip_sent_forwarded': 0,
                   'ip_sent_generated': 212110},
 'ospf_statistics': {'ospf_received_checksum_errors': 0,
                     'ospf_received_database_desc': 0,
                     'ospf_received_hello': 0,
                     'ospf_received_link_state_req': 0,
                     'ospf_received_lnk_st_acks': 0,
                     'ospf_received_lnk_st_updates': 0,
                     'ospf_received_total': 0,
                     'ospf_sent_database_desc': 0,
                     'ospf_sent_hello': 0,
                     'ospf_sent_lnk_st_acks': 0,
                     'ospf_sent_lnk_st_updates': 0,
                     'ospf_sent_total': 0},
 'pimv2_statistics': {'pimv2_asserts': '0/0',
                      'pimv2_bootstraps': '0/0',
                      'pimv2_candidate_rp_advs': '0/0',
                      'pimv2_checksum_errors': 0,
                      'pimv2_format_errors': 0,
                      'pimv2_grafts': '0/0',
                      'pimv2_hellos': '0/0',
                      'pimv2_join_prunes': '0/0',
                      'pimv2_non_rp': 0,
                      'pimv2_non_sm_group': 0,
                      'pimv2_registers': '0/0',
                      'pimv2_registers_stops': '0/0',
                      'pimv2_state_refresh': '0/0',
                      'pimv2_total': '0/0'},
 'tcp_statistics': {'tcp_received_checksum_errors': 0,
                    'tcp_received_no_port': 0,
                    'tcp_received_total': 116563,
                    'tcp_sent_total': 139252},
 'udp_statistics': {'udp_received_no_port': 289579,
                    'udp_received_total': 682217,
                    'udp_received_udp_checksum_errors': 0,
                    'udp_sent_fwd_broadcasts': 0,
                    'udp_sent_total': 28296}}

		golden_output = {'execute.return_value': '''
			R5#show ip traffic 
			IP statistics:
			  Rcvd:  844148 total, 843331 local destination
			         0 format errors, 0 checksum errors, 811 bad hop count
			         0 unknown protocol, 6 not a gateway
			         0 security failures, 0 bad options, 0 with options
			  Opts:  0 end, 0 nop, 0 basic security, 0 loose source route
			         0 timestamp, 0 extended security, 0 record route
			         0 stream ID, 0 strict source route, 0 alert, 0 cipso, 0 ump
			         0 other
			  Frags: 0 reassembled, 0 timeouts, 0 couldn't reassemble
			         0 fragmented, 0 couldn't fragment
			  Bcast: 653921 received, 6 sent
			  Mcast: 0 received, 0 sent
			  Sent:  212110 generated, 0 forwarded
			  Drop:  10 encapsulation failed, 0 unresolved, 0 no adjacency
			         0 no route, 0 unicast RPF, 0 forced drop
			         0 options denied, 0 source IP address zero

			ICMP statistics:
			  Rcvd: 0 format errors, 0 checksum errors, 0 redirects, 0 unreachable
			        43838 echo, 713 echo reply, 0 mask requests, 0 mask replies, 0 quench
			        0 parameter, 0 timestamp, 0 info request, 0 other
			        0 irdp solicitations, 0 irdp advertisements
			  Sent: 0 redirects, 4 unreachable, 730 echo, 43838 echo reply
			        0 mask requests, 0 mask replies, 0 quench, 0 timestamp
			        0 info reply, 0 time exceeded, 0 parameter problem
			        0 irdp solicitations, 0 irdp advertisements

			BGP statistics:
			  Rcvd: 0 total, 0 opens, 0 notifications, 0 updates
			        0 keepalives, 0 route-refresh, 0 unrecognized
			  Sent: 0 total, 0 opens, 0 notifications, 0 updates
			        0 keepalives, 0 route-refresh

			TCP statistics:
			  Rcvd: 116563 total, 0 checksum errors, 0 no port
			  Sent: 139252 total

			EIGRP-IPv4 statistics:
			  Rcvd: 0 total
			  Sent: 0 total

			PIMv2 statistics: Sent/Received
			  Total: 0/0, 0 checksum errors, 0 format errors
			  Registers: 0/0 (0 non-rp, 0 non-sm-group), Register Stops: 0/0,  Hellos: 0/0
			  Join/Prunes: 0/0, Asserts: 0/0, grafts: 0/0
			  Bootstraps: 0/0, Candidate_RP_Advertisements: 0/0
			  State-Refresh: 0/0

			IGMP statistics: Sent/Received
			  Total: 0/0, Format errors: 0/0, Checksum errors: 0/0
			  Host Queries: 0/0, Host Reports: 0/0, Host Leaves: 0/0 
			  DVMRP: 0/0, PIM: 0/0

			UDP statistics:
			  Rcvd: 682217 total, 0 checksum errors, 289579 no port
			  Sent: 28296 total, 0 forwarded broadcasts

			OSPF statistics:
			  Rcvd: 0 total, 0 checksum errors
			  	0 hello, 0 database desc, 0 link state req
			  	0 link state updates, 0 link state acks

			  Sent: 0 total
			  	0 hello, 0 database desc, 0 link state req
			  	0 link state updates, 0 link state acks

			ARP statistics:
			  Rcvd: 26338 requests, 25520 replies, 42 reverse, 0 other
			  Sent: 123 requests, 1399 replies (0 proxy), 0 reverse
			  Drop due to input queue full: 0
		'''
		}

		def test_empty(self):
				self.device = Mock(**self.empty_output)
				obj = ShowIpTraffic(device=self.device)
				with self.assertRaises(SchemaEmptyParserError):
						parsed_output = obj.parse()

		def test_golden(self):
				self.maxDiff = None
				self.device = Mock(**self.golden_output)
				obj = ShowIpTraffic(device=self.device)
				parsed_output = obj.parse()
				self.assertEqual(parsed_output, self.golden_parsed_output)

# ============================================
# Unit test for 'show arp'
# ============================================
class test_show_arp(test_show_arp_iosxe):
    device = Device(name='aDevice')
    empty_output_ios = {'execute.return_value': ''}
    golden_output_ios = {'execute.return_value': '''\
        Protocol   Address       Age (min)   Hardware Addr    Type    Interface
        Internet   10.1.1.5           134    0005.0032.0854   ARPA    FastEthernet0/0/0
        Internet   10.1.1.7             -    0005.0032.0000   ARPA    FastEthernet0/0/0
        '''}
    golden_parsed_output_ios = {
        'interfaces': {
            'FastEthernet0/0/0': {
                'ipv4': {
                    'neighbors': {
                        '10.1.1.5': {
                            'ip': '10.1.1.5',
                            'link_layer_address': '0005.0032.0854',
                            'age': '134',
                            'origin': 'dynamic',
                            'type': 'ARPA',
                            'protocol': 'Internet',
                            },
                        '10.1.1.7': {
                            'ip': '10.1.1.7',
                            'link_layer_address': '0005.0032.0000',
                            'age': '-',
                            'origin': 'static',
                            'type': 'ARPA',
                            'protocol': 'Internet',
                            },
                        },
                    },
                },
            },
        }

    def test_empty(self):
        self.device1 = Mock(**self.empty_output)
        obj = ShowArp(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowArp(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output)

    def test_golden_1(self):
        self.device = Mock(**self.golden_output_1)
        obj = ShowArp(device=self.device)
        parsed_output = obj.parse(vrf='Mgmt-vrf', intf_or_ip='GigabitEthernet0/0')
        self.assertEqual(parsed_output,self.golden_parsed_output_1)   

    def test_empty_ios(self):
        self.device1 = Mock(**self.empty_output_ios)
        obj = ShowArp(device=self.device1)
        with self.assertRaises(SchemaEmptyParserError):
            parsed_output = obj.parse()

    def test_golden_ios(self):
        self.device = Mock(**self.golden_output_ios)
        obj = ShowArp(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output,self.golden_parsed_output_ios)     

# ============================================
# unit test for 'show arp application'
# ============================================
class test_show_arp_application(test_show_arp_application_iosxe):
    def test_empty(self):
          self.device = Mock(**self.empty_output)
          obj = ShowArpApplication(device=self.device)
          with self.assertRaises(SchemaEmptyParserError):
              parsed_output = obj.parse()

    def test_golden(self):
        self.device = Mock(**self.golden_output)
        obj = ShowArpApplication(device=self.device)
        parsed_output = obj.parse()
        self.assertEqual(parsed_output, self.golden_parsed_output)

# ============================================
# unit test for 'show arp summary'
# ============================================
class test_show_arp_summary(test_show_arp_summary_iosxe):

  device = Device('aDevice')
  empty_output_ios = {'execute.return_value':''}
  
  golden_parsed_output_ios = {
      'total_num_of_entries': {
          'arp_table_entries': 4,
          'dynamic_arp_entries': 0,
          'incomplete_arp_entries': 0,
          'interface_arp_entries': 3,
          'static_arp_entries': 1,
          'alias_arp_entries': 0,
          'simple_application_arp_entries': 0,
          'application_alias_arp_entries': 0,
          'application_timer_arp_entries': 0,
          'learn_arp_entries': 0,
      },
      'maximum_entries': {
          'maximum_configured_learn_arp_entry_limit': 512000,
          'maximum_limit_of_learn_arp_entry': 512000,
      },
      'arp_entry_threshold': 409600,
      'permit_threshold': 486400,
      'interface_entries': {
          'GigabitEthernet4/7': 1,
          'GigabitEthernet4/1.1': 1,
          'GigabitEthernet4/1': 1
      },
  }

  golden_output_ios = {'execute.return_value': '''\
      Total number of entries in the ARP table: 4.
      Total number of Dynamic ARP entries: 0.
      Total number of Incomplete ARP entries: 0.
      Total number of Interface ARP entries: 3.
      Total number of Static ARP entries: 1.
      Total number of Alias ARP entries: 0.
      Total number of Simple Application ARP entries: 0.
      Total number of Application Alias ARP entries: 0.
      Total number of Application Timer ARP entries: 0.
      Maximum limit of Learn ARP entry : 512000.
      Maximum configured Learn ARP entry limit : 512000.
      Learn ARP Entry Threshold is 409600 and Permit Threshold is 486400.
      Total number of Learn ARP entries: 0.
      Interface           Entry Count
      GigabitEthernet4/7            1
      GigabitEthernet4/1.1          1
      GigabitEthernet4/1            1
      E0BC0/0                       
      '''
  }

  def test_empty(self):
      self.device = Mock(**self.empty_output)
      obj = ShowArpSummary(device=self.device)
      with self.assertRaises(SchemaEmptyParserError):
          parsed_output = obj.parse()

  def test_golden(self):
      self.device = Mock(**self.golden_output)
      obj = ShowArpSummary(device=self.device)
      parsed_output = obj.parse()
      self.assertEqual(parsed_output, self.golden_parsed_output)

  def test_empty_ios(self):
      self.device = Mock(**self.empty_output_ios)
      obj = ShowArpSummary(device=self.device)
      with self.assertRaises(SchemaEmptyParserError):
          parsed_output = obj.parse()

  def test_golden_ios(self):
      self.device = Mock(**self.golden_output_ios)
      obj = ShowArpSummary(device=self.device)
      parsed_output = obj.parse()
      self.assertEqual(parsed_output, self.golden_parsed_output_ios)

if __name__ == '__main__':
		unittest.main()