# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError,\
                                             SchemaMissingKeyError

# Parser
from genie.libs.parser.iosxe.show_arp import ShowArp, ShowIpArpSummary,\
                                             ShowIpTraffic,\
                                             ShowArpApplication,\
                                             ShowArpSummary


# ============================================
# Parser for 'show arp [vrf <WORD>] <WROD>'
# ============================================
class test_show_arp(unittest.TestCase):
		
		device = Device(name='aDevice')
		empty_output = {'execute.return_value': ''}
		
		golden_parsed_output = {
			'interfaces': {
				'Vlan100': {
					'ipv4': {
						'neighbors': {
							'201.0.12.1': {
								'age': '-',
                              	'ip': '201.0.12.1',
                             	'link_layer_address': '58bf.eab6.2f51',
                              	'origin': 'static',
                              	'protocol': 'Internet',
                              	'type': 'ARPA'},
               				'201.0.12.2': {'age': '29',
                              	'ip': '201.0.12.2',
                              	'link_layer_address': '3820.5672.fc51',
                              	'origin': 'dynamic',
                              	'protocol': 'Internet',
                              	'type': 'ARPA'}
                        }
                    }
                },
                'Vlan200': {
                	'ipv4': {
                		'neighbors': {
                			'201.0.14.1': {
                				'age': '-',
                              	'ip': '201.0.14.1',
                              	'link_layer_address': '58bf.eab6.2f62',
                              	'origin': 'static',
                              	'protocol': 'Internet',
                              	'type': 'ARPA'}
                        }
                    }
                }
            }
        }

		golden_output = {'execute.return_value': '''\
				Protocol  Address          Age (min)  Hardware Addr   Type   Interface
				Internet  201.0.12.1              -   58bf.eab6.2f51  ARPA   Vlan100
				Internet  201.0.12.2             29   3820.5672.fc51  ARPA   Vlan100
				Internet  201.0.14.1              -   58bf.eab6.2f62  ARPA   Vlan200
		'''}
		
		golden_parsed_output_1 = {
			'interfaces': {
				'GigabitEthernet0/0': {
					'ipv4': {
						'neighbors': {
							'10.1.18.1': {
								'age': '45',
                                'ip': '10.1.18.1',
                                'link_layer_address': '0012.7f57.ac80',
                                'origin': 'dynamic',
                                'protocol': 'Internet',
                                'type': 'ARPA'},
		                  	'10.1.18.122': {
		                  		'age': '-',
                              	'ip': '10.1.18.122',
                              	'link_layer_address': '58bf.eab6.2f00',
                              	'origin': 'static',
                              	'protocol': 'Internet',
                              	'type': 'ARPA'},
		                  	'10.1.18.13': {
		                  		'age': '142',
                             	'ip': '10.1.18.13',
                             	'link_layer_address': '00b0.c215.441d',
                             	'origin': 'dynamic',
                             	'protocol': 'Internet',
                             	'type': 'ARPA'},
		                  	'10.1.18.254': {
		                  		'age': '247',
                              	'ip': '10.1.18.254',
                              	'link_layer_address': '5cf3.fc25.ab76',
                              	'origin': 'dynamic',
                              	'protocol': 'Internet',
                              	'type': 'ARPA'}
                        }
                    }
                }
            }
        }

		golden_output_1 = {'execute.return_value': '''\
				Protocol  Address          Age (min)  Hardware Addr   Type   Interface
				Internet  10.1.18.122             -   58bf.eab6.2f00  ARPA   GigabitEthernet0/0
				Internet  10.1.18.1              45   0012.7f57.ac80  ARPA   GigabitEthernet0/0
				Internet  10.1.18.13            142   00b0.c215.441d  ARPA   GigabitEthernet0/0
				Internet  10.1.18.254           247   5cf3.fc25.ab76  ARPA   GigabitEthernet0/0

		'''}


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

#=========================================================
# Unit test for show ip arp summary
#=========================================================
class test_show_ip_arp_summary(unittest.TestCase):

		device = Device(name='aDevice')
		empty_output = {'execute.return_value': ''}

		golden_parsed_output = {
				'incomp_entries': 0,
				'total_entries': 8}

		golden_output = {'execute.return_value': '''
				R1_csr1000v#show ip arp summary 
				8 IP ARP entries, with 0 of them incomplete
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

		golden_parsed_output = {
			'arp_statistics': {
				'arp_drops_input_full': 0,
				'arp_in_other': 0,
				'arp_in_replies': 764,
				'arp_in_requests': 2020,
				'arp_in_reverse': 0,
				'arp_out_proxy': 2,
				'arp_out_replies': 126,
				'arp_out_requests': 29,
				'arp_out_reverse': 0},
 			'ip_statistics': {
 				'ip_bcast_received': 33324,
				'ip_bcast_sent': 5,
				'ip_drop_encap_failed': 8,
				'ip_drop_forced_drop': 0,
				'ip_drop_no_adj': 20,
				'ip_drop_no_route': 19,
				'ip_drop_opts_denied': 0,
				'ip_drop_src_ip': 0,
				'ip_drop_unicast_rpf': 0,
				'ip_drop_unresolved': 0,
				'ip_drop_unsupp_address': 0,
				'ip_frags_fragmented': 1,
				'ip_frags_fragments': 5,
				'ip_frags_invalid_hole': 0,
				'ip_frags_no_fragmented': 0,
				'ip_frags_no_reassembled': 0,
				'ip_frags_reassembled': 0,
				'ip_frags_timeouts': 0,
				'ip_mcast_received': 144833,
				'ip_mcast_sent': 66274,
				'ip_opts_alert': 12717,
				'ip_opts_basic_security': 0,
				'ip_opts_cipso': 0,
				'ip_opts_end': 0,
				'ip_opts_extended_security': 0,
				'ip_opts_ignored': 0,
				'ip_opts_loose_src_route': 0,
				'ip_opts_nop': 0,
				'ip_opts_other': 0,
				'ip_opts_record_route': 0,
				'ip_opts_strct_src_route': 0,
				'ip_opts_strm_id': 0,
				'ip_opts_timestamp': 0,
				'ip_opts_ump': 0,
				'ip_rcvd_bad_hop': 0,
				'ip_rcvd_bad_optns': 0,
				'ip_rcvd_checksum_errors': 0,
				'ip_rcvd_format_errors': 0,
				'ip_rcvd_local_destination': 110596,
				'ip_rcvd_not_gateway': 5,
				'ip_rcvd_sec_failures': 0,
				'ip_rcvd_total': 17780,
				'ip_rcvd_unknwn_protocol': 0,
				'ip_rcvd_with_optns': 12717,
				'ip_sent_forwarded': 1654728,
				'ip_sent_generated': 85543},
			'icmp_statistics': {
				'icmp_received_checksum_errors': 0,
            	'icmp_received_echo': 284,
            	'icmp_received_echo_reply': 9,
            	'icmp_received_format_errors': 0,
            	'icmp_received_info_replies': 0,
            	'icmp_received_info_request': 0,
            	'icmp_received_irdp_advertisements': 0,
            	'icmp_received_irdp_solicitations': 0,
            	'icmp_received_mask_replies': 0,
            	'icmp_received_mask_requests': 0,
            	'icmp_received_other': 0,
            	'icmp_received_parameter': 0,
            	'icmp_received_quench': 0,
            	'icmp_received_redirects': 0,
            	'icmp_received_time_exceeded': 0,
            	'icmp_received_timestamp': 0,
            	'icmp_received_timestamp_replies': 0,
            	'icmp_received_unreachable': 0,
            	'icmp_sent_echo': 9,
            	'icmp_sent_echo_reply': 134,
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
            	'icmp_sent_timestamp_replies': 0,
            	'icmp_sent_unreachable': 14},
			'udp_statistics': {
				'udp_received_finput': 0,
                'udp_received_no_port': 15906,
                'udp_received_total': 62515,
                'udp_received_udp_checksum_errors': 0,
                'udp_sent_fwd_broadcasts': 0,
                'udp_sent_total': 41486},
			'pimv2_statistics': {
				'pimv2_asserts': '0/697',
	            'pimv2_bootstraps': '2088/2438',
	            'pimv2_candidate_rp_advs': '350/0',
	            'pimv2_checksum_errors': 0,
	            'pimv2_format_errors': 0,
	            'pimv2_grafts': '0/2',
	            'pimv2_hellos': '5011/5008',
	            'pimv2_join_prunes': '5/712',
	            'pimv2_non_rp': 0,
	            'pimv2_non_sm_group': 0,
	            'pimv2_queue_drops': 0,
	            'pimv2_registers': '1/1',
	            'pimv2_registers_stops': '1/1',
	            'pimv2_state_refresh': '0/0',
	            'pimv2_total': '7458/8859'},
			'ospf_statistics': {
				'ospf_received_checksum_errors': 0,
	            'ospf_received_database_desc': 20,
	            'ospf_received_hello': 15153,
	            'ospf_received_link_state_req': 2,
	            'ospf_received_lnk_st_acks': 688,
	            'ospf_received_lnk_st_updates': 359,
	            'ospf_received_total': 16222,
	            'ospf_sent_database_desc': 30,
	            'ospf_sent_hello': 8887,
	            'ospf_sent_lnk_st_acks': 239,
	            'ospf_sent_lnk_st_updates': 299,
	            'ospf_sent_total': 9456,
	            'ospf_traffic_cntrs_clear': 'never'},
			'igmp_statistics': {
				'igmp_checksum_errors': '0/0',
	            'igmp_dvmrp': '0/0',
	            'igmp_format_errors': '0/0',
	            'igmp_host_leaves': '0/5',
	            'igmp_host_queries': '2475/1414',
	            'igmp_host_reports': '357/3525',
	            'igmp_pim': '0/0',
	            'igmp_queue_drops': 0,
	            'igmp_total': '2832/4946'},
			'tcp_statistics': {
				'tcp_received_checksum_errors': 0,
	            'tcp_received_no_port': 0,
	            'tcp_received_total': 15396,
	            'tcp_sent_total': 19552},
			'eigrp_ipv4_statistics': {
				'eigrp_ipv4_received_total': 4612,
	            'eigrp_ipv4_sent_total': 4611},
			'bgp_statistics': {
				'bgp_received_keepalives': 2167,
                'bgp_received_notifications': 0,
                'bgp_received_opens': 6,
                'bgp_received_route_refresh': 0,
                'bgp_received_total': 2185,
                'bgp_received_unrecognized': 0,
                'bgp_received_updates': 12,
                'bgp_sent_keepalives': 2296,
                'bgp_sent_notifications': 2,
                'bgp_sent_opens': 6,
                'bgp_sent_route_refresh': 0,
                'bgp_sent_total': 2304,
                'bgp_sent_updates': 0},
		}

		golden_output = {'execute.return_value': '''
				R1#show ip traffic 
				IP statistics:
					Rcvd:  17780 total, 110596 local destination
								 0 format errors, 0 checksum errors, 0 bad hop count
								 0 unknown protocol, 5 not a gateway
								 0 security failures, 0 bad options, 12717 with options
					Opts:  0 end, 0 nop, 0 basic security, 0 loose source route
								 0 timestamp, 0 extended security, 0 record route
								 0 stream ID, 0 strict source route, 12717 alert, 0 cipso, 0 ump
								 0 other, 0 ignored
					Frags: 0 reassembled, 0 timeouts, 0 couldn't reassemble
								 1 fragmented, 5 fragments, 0 couldn't fragment
								 0 invalid hole
					Bcast: 33324 received, 5 sent
					Mcast: 144833 received, 66274 sent
					Sent:  85543 generated, 1654728 forwarded
					Drop:  8 encapsulation failed, 0 unresolved, 20 no adjacency
								 19 no route, 0 unicast RPF, 0 forced drop, 0 unsupported-addr
								 0 options denied, 0 source IP address zero

				ICMP statistics:
					Rcvd: 0 format errors, 0 checksum errors, 0 redirects, 0 unreachable
								284 echo, 9 echo reply, 0 mask requests, 0 mask replies, 0 quench
								0 parameter, 0 timestamp, 0 timestamp replies, 0 info request, 0 other
								0 irdp solicitations, 0 irdp advertisements
								0 time exceeded, 0 info replies
					Sent: 0 redirects, 14 unreachable, 9 echo, 134 echo reply
								0 mask requests, 0 mask replies, 0 quench, 0 timestamp, 0 timestamp replies
								0 info reply, 0 time exceeded, 0 parameter problem
								0 irdp solicitations, 0 irdp advertisements

				UDP statistics:
					Rcvd: 62515 total, 0 checksum errors, 15906 no port 0 finput
					Sent: 41486 total, 0 forwarded broadcasts

				OSPF statistics:
					Last clearing of OSPF traffic counters never
					Rcvd: 16222 total, 0 checksum errors
						15153 hello, 20 database desc, 2 link state req
						359 link state updates, 688 link state acks
					Sent: 9456 total
						8887 hello, 30 database desc, 8 link state req
						299 link state updates, 239 link state acks

				PIMv2 statistics: Sent/Received
					Total: 7458/8859, 0 checksum errors, 0 format errors
					Registers: 1/1 (0 non-rp, 0 non-sm-group), Register Stops: 1/1,  Hellos: 5011/5008
					Join/Prunes: 5/712, Asserts: 0/697, grafts: 0/2
					Bootstraps: 2088/2438, Candidate_RP_Advertisements: 350/0
					Queue drops: 0
					State-Refresh: 0/0

				IGMP statistics: Sent/Received
					Total: 2832/4946, Format errors: 0/0, Checksum errors: 0/0
					Host Queries: 2475/1414, Host Reports: 357/3525, Host Leaves: 0/5 
					DVMRP: 0/0, PIM: 0/0
					Queue drops: 0

				TCP statistics:
					Rcvd: 15396 total, 0 checksum errors, 0 no port
					Sent: 19552 total

				EIGRP-IPv4 statistics:
					Rcvd: 4612 total
					Sent: 4611 total

				BGP statistics:
					Rcvd: 2185 total, 6 opens, 0 notifications, 12 updates
								2167 keepalives, 0 route-refresh, 0 unrecognized
					Sent: 2304 total, 6 opens, 2 notifications, 0 updates
								2296 keepalives, 0 route-refresh

				ARP statistics:
					Rcvd: 2020 requests, 764 replies, 0 reverse, 0 other
					Sent: 29 requests, 126 replies (2 proxy), 0 reverse
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


# =================================================
# Parser for 'show arp application'
# =================================================
class test_show_arp_application(unittest.TestCase):

    device = Device(name='aDevice')
    empty_output = {'execute.return_value': ''}
    
    golden_parsed_output = {
        'num_of_clients_registered': 16,
        'applications': {
            'VRRS': {
                'id': 200,
                'num_of_subblocks': 0
            },
            'ARP Backup': {
                'id': 201,
                'num_of_subblocks': 0
            },
            'DHCPD': {
                'id': 202,
                'num_of_subblocks': 0
            },
            'ARP HA': {
                'id': 203,
                'num_of_subblocks': 0
            },
            'ASR1000-RP SPA Ethernet': {
                'id': 204,
                'num_of_subblocks': 0
            },
            'VRRS_L3CTRL': {
                'id': 205,
                'num_of_subblocks': 0
            },
            'IP ARP Adj Conn ID': {
                'id': 206,
                'num_of_subblocks': 0
            },
            'IP ARP VLAN ID': {
                'id': 215,
                'num_of_subblocks': 100204
            },
            'IP ARP Adjacency': {
                'id': 214,
                'num_of_subblocks': 100204
            }
        }
    }

    golden_output = {'execute.return_value': '''\
        Number of clients registered: 16

        Application                 ID      Num of Subblocks
        VRRS                        200     0
        ARP Backup                  201     0
        DHCPD                       202     0
        ARP HA                      203     0
        ASR1000-RP SPA Ethernet     204     0
        VRRS_L3CTRL                 205     0
        IP ARP Adj Conn ID          206     0
        IP ARP VLAN ID              215     100204
        IP ARP Adjacency            214     100204
        '''
    }   

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

# ==========================================
# Parser for 'show arp summary'
# ==========================================

class test_show_arp_summary(unittest.TestCase):

    device = Device('aDevice')
    empty_output = {'execute.return_value':''}
    
    golden_parsed_output = {
        'total_num_of_entries': {
            'arp_table_entries': 100409,
            'dynamic_arp_entries': 100204,
            'incomplete_arp_entries': 0,
            'interface_arp_entries': 205,
            'static_arp_entries': 0,
            'alias_arp_entries': 0,
            'simple_application_arp_entries': 0
        },
        'interface_entries': {
            'GigabitEthernet0': 4,
            'TenGigabitEthernet0/2/0': 1,
            'GigabitEthernet0/0/1.1143': 3
        }
    }

    golden_output = {'execute.return_value': '''\
        Total number of entries in the ARP table: 100409.
        Total number of Dynamic ARP entries: 100204.
        Total number of Incomplete ARP entries: 0.
        Total number of Interface ARP entries: 205.
        Total number of Static ARP entries: 0.
        Total number of Alias ARP entries: 0.
        Total number of Simple Application ARP entries: 0.
        Interface           Entry Count
        GigabitEthernet0        4
        Te0/2/0                 1
        Gi0/0/1.1143            3
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

if __name__ == '__main__':
    unittest.main()
