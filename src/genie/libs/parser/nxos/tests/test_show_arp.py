# Python
import unittest
from unittest.mock import Mock

# ATS
from pyats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
											 SchemaMissingKeyError

# Parser
from genie.libs.parser.nxos.show_arp import ShowIpArpDetailVrfAll, \
											ShowIpArpSummaryVrfAll, \
											ShowIpArpstatisticsVrfAll, \
											ShowIpArp


#=========================================================
# Unit test for show ip arp detail vrf all
#=========================================================
class TestShowIpArpDetailVrfAll(unittest.TestCase):

	device = Device(name='aDevice')
	maxDiff = None
	empty_output = {'execute.return_value': ''}

	golden_parsed_output = {
		'interfaces': {
			'Ethernet1/1': {
				'ipv4': {
					'neighbors': {
						'10.1.3.5': {
							'age': '-',
							'ip': '10.1.3.5',
							'link_layer_address': 'aaaa.bbff.8888',
							'origin': 'static',
							'physical_interface': 'Ethernet1/1'}
					}
				}
			},
			'Ethernet1/1.1': {
				'ipv4': {
					'neighbors': {
						'192.168.4.2': {
							'age': '00:01:53',
							'ip': '192.168.4.2',
							'link_layer_address': '000c.29ff.48d9',
							'origin': 'dynamic',
							'physical_interface': 'Ethernet1/1.1'}
					}
				}
			},
			'Ethernet1/1.2': {
				'ipv4': {
					'neighbors': {
						'192.168.154.2': {
							'age': '00:00:47',
							'ip': '192.168.154.2',
							'link_layer_address': '000c.29ff.48d9',
							'origin': 'dynamic',
							'physical_interface': 'Ethernet1/1.2'}
					}
				}
			},
			'Ethernet1/1.4': {
				'ipv4': {
					'neighbors': {
						'192.168.106.2': {
							'age': '00:08:42',
							'ip': '192.168.106.2',
							'link_layer_address': '000c.29ff.48d9',
							'origin': 'dynamic',
							'physical_interface': 'Ethernet1/1.4'}
					}
				}
			},
			'Ethernet1/2.1': {
				'ipv4': {
					'neighbors': {
						'192.168.154.2': {
							'age': '00:18:24',
							'ip': '192.168.154.2',
							'link_layer_address': '000c.29ff.5c44',
							'origin': 'dynamic',
							'physical_interface': 'Ethernet1/2.1'}
					}
				}
			},
			'Ethernet1/2.2': {
				'ipv4': {
					'neighbors': {
						'192.168.51.2': {
							'age': '00:05:21',
							'ip': '192.168.51.2',
							'link_layer_address': '000c.29ff.5c44',
							'origin': 'dynamic',
							'physical_interface': 'Ethernet1/2.2'}
					}
				}
			},
			'Ethernet1/2.4': {
				'ipv4': {
					'neighbors': {
						'192.168.9.2': {
							'age': '00:10:51',
							'ip': '192.168.9.2',
							'link_layer_address': '000c.29ff.5c44',
							'origin': 'dynamic',
							'physical_interface': 'Ethernet1/2.4'}
					}
				}
			},
			'Ethernet1/4.100': {
				'ipv4': {
					'neighbors': {
						'10.51.1.101': {
							'age': '00:01:28',
							'ip': '10.51.1.101',
							'link_layer_address': '0000.71ff.3629',
							'origin': 'dynamic',
							'physical_interface': 'Ethernet1/4.100'}
					}
				}
			},
			'Ethernet1/4.101': {
				'ipv4': {
					'neighbors': {
						'10.154.1.101': {
							'age': '00:01:28',
							'ip': '10.154.1.101',
							'link_layer_address': '0000.71ff.3d89',
							'origin': 'dynamic',
							'physical_interface': 'Ethernet1/4.101'}
					}
				}
			},
			'Ethernet1/4.200': {
				'ipv4': {
					'neighbors': {
						'10.76.1.101': {
							'age': '00:01:28',
							'ip': '10.76.1.101',
							'link_layer_address': '0000.00ff.37d7',
							'origin': 'dynamic',
							'physical_interface': 'Ethernet1/4.200'}
					}
				}
			},
			'mgmt0': {
				'ipv4': {
					'neighbors': {
						'10.1.7.1': {
							'age': '00:17:15',
							'ip': '10.1.7.1',
							'link_layer_address': '0012.7fff.04d7',
							'origin': 'dynamic',
							'physical_interface': 'mgmt0'},
						'10.1.7.250': {
							'age': '00:14:24',
							'ip': '10.1.7.250',
							'link_layer_address': '0050.56ff.fb97',
							'origin': 'dynamic',
							'physical_interface': 'mgmt0'},
						'10.1.7.253': {
							'age': '00:10:22',
							'ip': '10.1.7.253',
							'link_layer_address': '0050.56ff.4ea1',
							'origin': 'dynamic',
							'physical_interface': 'mgmt0'}
					}
				}
			}
		}
	}

	golden_output = {'execute.return_value': '''
		N95_1# show ip arp detail vrf all 

		Flags: * - Adjacencies learnt on non-active FHRP router
			   + - Adjacencies synced via CFSoE
			   # - Adjacencies Throttled for Glean
			   CP - Added via L2RIB, Control plane Adjacencies
			   PS - Added via L2RIB, Peer Sync
			   RO - Re-Originated Peer Sync Entry

		IP ARP Table for all contexts
		Total number of entries: 12
		Address         Age       MAC Address     Interface        Physical Interface  Flags
		10.1.7.1        00:17:15  0012.7fff.04d7  mgmt0            mgmt0               
		10.1.7.250      00:14:24  0050.56ff.fb97  mgmt0            mgmt0               
		10.1.7.253      00:10:22  0050.56ff.4ea1  mgmt0            mgmt0               
		10.1.3.5           -      aaaa.bbff.8888  Ethernet1/1      Ethernet1/1              
		192.168.4.2       00:01:53  000c.29ff.48d9  Ethernet1/1.1    Ethernet1/1.1       
		192.168.154.2       00:00:47  000c.29ff.48d9  Ethernet1/1.2    Ethernet1/1.2       
		192.168.106.2       00:08:42  000c.29ff.48d9  Ethernet1/1.4    Ethernet1/1.4       
		192.168.154.2       00:18:24  000c.29ff.5c44  Ethernet1/2.1    Ethernet1/2.1       
		192.168.51.2       00:05:21  000c.29ff.5c44  Ethernet1/2.2    Ethernet1/2.2       
		192.168.9.2       00:10:51  000c.29ff.5c44  Ethernet1/2.4    Ethernet1/2.4       
		10.51.1.101      00:01:28  0000.71ff.3629  Ethernet1/4.100  Ethernet1/4.100     
		10.154.1.101      00:01:28  0000.71ff.3d89  Ethernet1/4.101  Ethernet1/4.101     
		10.76.1.101      00:01:28  0000.00ff.37d7  Ethernet1/4.200  Ethernet1/4.200  
	'''
	}

	golden_output_2 = {'execute.return_value': '''
	show ip arp detail vrf all
	
	
	Flags: * - Adjacencies learnt on non-active FHRP router
		   + - Adjacencies synced via CFSoE
		   # - Adjacencies Throttled for Glean
		   CP - Added via L2RIB, Control plane Adjacencies
		   PS - Added via L2RIB, Peer Sync
		   RO - Re-Originated Peer Sync Entry
	
	IP ARP Table for all contexts
	Total number of entries: 4
	Address         Age       MAC Address     Interface        Physical Interface  Flags	
	172.16.8.178    00:00:04  INCOMPLETE      Vlan392          Vlan392             
	172.16.8.183    00:13:47  0050.56ff.ece6  Vlan392          port-channel105     
	172.16.8.185    00:08:55  0050.56ff.c11c  Vlan392          port-channel110     + 
	172.16.10.1        -      0000.0cff.9129  Vlan393          -    	
	'''}

	golden_parsed_output_2 = {
		'interfaces': {
			'Vlan392': {
				'ipv4': {
					'neighbors': {
						'172.16.8.178': {
							'age': '00:00:04',
							'ip': '172.16.8.178',
							'link_layer_address': 'INCOMPLETE',
							'origin': 'dynamic',
							'physical_interface': 'Vlan392',
						},
						'172.16.8.183': {
							'age': '00:13:47',
							'ip': '172.16.8.183',
							'link_layer_address': '0050.56ff.ece6',
							'origin': 'dynamic',
							'physical_interface': 'port-channel105',
						},
						'172.16.8.185': {
							'age': '00:08:55',
							'flag': 'Adjacencies synced via CFSoE',
							'ip': '172.16.8.185',
							'link_layer_address': '0050.56ff.c11c',
							'origin': 'dynamic',
							'physical_interface': 'port-channel110',
						},
					},
				},
			},
			'Vlan393': {
				'ipv4': {
					'neighbors': {
						'172.16.10.1': {
							'age': '-',
							'ip': '172.16.10.1',
							'link_layer_address': '0000.0cff.9129',
							'origin': 'static',
							'physical_interface': '-',
						},
					},
				},
			},
		},
	}

	def test_empty(self):
		self.device = Mock(**self.empty_output)
		obj = ShowIpArpDetailVrfAll(device=self.device)
		with self.assertRaises(SchemaEmptyParserError):
			parsed_output = obj.parse()

	def test_golden(self):
		self.device = Mock(**self.golden_output)
		obj = ShowIpArpDetailVrfAll(device=self.device)
		parsed_output = obj.parse()
		self.assertEqual(parsed_output, self.golden_parsed_output)

	def test_golden2(self):
		self.device = Mock(**self.golden_output_2)
		obj = ShowIpArpDetailVrfAll(device=self.device)
		parsed_output = obj.parse()
		self.assertEqual(parsed_output, self.golden_parsed_output_2)


#=========================================================
# Unit test for show ip arp summary vrf all
#=========================================================
class TestShowIpArpSummaryVrfAll(unittest.TestCase):

	device = Device(name='aDevice')
	empty_output = {'execute.return_value': ''}

	golden_parsed_output = {
		'incomplete': 0,
		'throttled': 0,
		'resolved': 12,
		'total': 12,
		'unknown': 0}

	golden_output = {'execute.return_value': '''
		N95_1# show ip arp summary

		IP ARP Table - Adjacency Summary

		  Resolved   : 12
		  Incomplete : 0 (Throttled : 0)
		  Unknown    : 0
		  Total      : 12
	'''
	}

	golden_parsed_output_1 = {
		'incomplete': 0,
		'throttled': 0,
		'resolved': 12,
		'total': 12,
		'unknown': 0}

	golden_output_1 = {'execute.return_value': '''
		N95_1# show ip arp summary vrf all

		IP ARP Table - Adjacency Summary

		  Resolved   : 12
		  Incomplete : 0 (Throttled : 0)
		  Unknown    : 0
		  Total      : 12
	'''
	}

	def test_empty(self):
		self.device = Mock(**self.empty_output)
		obj = ShowIpArpSummaryVrfAll(device=self.device)
		with self.assertRaises(SchemaEmptyParserError):
			parsed_output = obj.parse()

	def test_golden(self):
		self.maxDiff = None
		self.device = Mock(**self.golden_output)
		obj = ShowIpArpSummaryVrfAll(device=self.device)
		parsed_output = obj.parse()
		self.assertEqual(parsed_output, self.golden_parsed_output)

	def test_golden_1(self):
		self.maxDiff = None
		self.device = Mock(**self.golden_output_1)
		obj = ShowIpArpSummaryVrfAll(device=self.device)
		parsed_output = obj.parse(vrf='all')
		self.assertEqual(parsed_output, self.golden_parsed_output_1)


#=========================================================
# Unit test for show ip arp statistics vrf all
#=========================================================
class TestShowIpArpStatisticsVrfAll(unittest.TestCase):
	device = Device(name='aDevice')
	empty_output = {'execute.return_value': ''}

	golden_parsed_output = {
		'statistics': {
			'adjacency': {
				'adjacency_adds': 43,
				'adjacency_deletes': 12,
				'adjacency_timeouts': 12,
				'failed_due_to_limits': 0},
			'received': {
				'anycast_proxy_arp': 0,
				'dropped': 28218,
				'dropped_server_port': 0,
				'drops_details': {
					'appeared_on_a_wrong_interface': 0,
					'arp_refresh_requests_received_from_clients': 0,
					'context_not_created': 0,
					'directed_broadcast_source': 0,
					'dropping_due_to_tunneling_failures': 0,
					'glean_requests_recv_count': 71,
					'grat_arp_received_on_proxy': 0,
					'incorrect_length': 0,
					'invalid_context': 0,
					'invalid_destination_ip_address': 0,
					'invalid_hardwaretype': 0,
					'invalid_layer2_address_length': 0,
					'invalid_layer3_address_length': 0,
					'invalid_protocol_packet': 0,
					'invalid_source_ip_address': 28,
					'invalid_source_mac_address': 0,
					'l2_packet_on_untrusted_l2_port': 0,
					'l2fm_query_failed_for_a_l2address': 0,
					'no_mem_to_create_per_intf_structure': 0,
					'non_active_fhrp_dest_ip': 0,
					'non_local_destination_ip_address': 20421,
					'number_of_signals_received_from_l2rib': 0,
					'packet_with_vip_on_standby_fhrp': 0,
					'received_before_arp_initialization': 0,
					'requests_came_for_exising_entries': 15,
					'requests_came_on_a_l2_interface': 0,
					'source_address_mismatch_with_subnet': 0,
					'source_mac_address_is_our_own': 0,
					'source_ip_address_is_our_own': 0},
				'enhanced_proxy_arp': 0,
				'fastpath': 0,
				'l2_port_track_proxy_arp': 0,
				'l2_replies': 0,
				'l2_requests': 0,
				'local_proxy_arp': 0,
				'proxy_arp': 0,
				'replies': 6582,
				'requests': 22632,
				'snooped': 0,
				'total': 0,
				'tunneled': 0},
			'sent': {
				'dropped': 0,
				'drops_details': {
					'adjacency_couldnt_be_added': 0,
					'arp_refresh_skipped_over_core_and_flooded': 0,
					'client_enqueue_failed': 0,
					'context_not_created': 0,
					'dest_not_reachable_for_proxy_arp': 0,
					'dest_unreachable_for_enhanced_proxy': 0,
					'destnination_is_our_own_ip': 26,
					'destnination_on_l2_port_tracked': 0,
					'invalid_context': 0,
					'invalid_dest_ip': 0,
					'invalid_ifindex': 0,
					'invalid_local_proxy_arp': 0,
					'invalid_proxy_arp': 0,
					'invalid_src_ip': 0,
					'mbuf_operation_failed': 0,
					'null_source_ip': 0,
					'null_source_mac': 0,
					'unattached_ip': 0,
					'vip_is_not_active': 0},
				'gratuitous': 58,
				'l2_replies': 0,
				'l2_requests': 0,
				'replies': 998,
				'requests': 2102,
				'total': 3158,
				'tunneled': 0}
		}
	}

	golden_output = {'execute.return_value': '''
		N95_1# show ip arp statistics vrf all
		ARP State Machine Stats

		ARP packet statistics for all contexts
		 Sent:
		 Total 3158, Requests 2102, Replies 998, Requests on L2 0, Replies on L2 0,
		 Gratuitous 58, Tunneled 0, Dropped 0
		 Send packet drops details:
			MBUF operation failed               : 0
			Context not yet created             : 0
			Invalid context                     : 0
			Invalid ifindex                     : 0
			Invalid SRC IP                      : 0
			Invalid DEST IP                     : 0
			Destination is our own IP           :  26
			Unattached IP                       :  0
			Adjacency Couldn't be added         :  0
			Null Source IP                      :  0
			Null Source MAC                     :  0
			Client Enqueue Failed               :  0
			Dest. not reachable for proxy arp   :  0
			Dest. unreachable for enhanced proxy :  0
			Dest. on L2 port being tracked      :  0
			Invalid Local proxy arp             :  0
			Invalid proxy arp                   :  0
		   VIP is not active                   :  0
		   ARP refresh skipped over core and flooded on server :  0
		 Received:
		 Total 0, Requests 22632, Replies 6582, Requests on L2 0, Replies on L2 0
		 Proxy arp 0, Local-Proxy arp 0,  Enhanced Proxy arp 0, Anycast proxy Proxy arp 0,  L2 Port-track Proxy arp 0,  Tunneled 0, Fastpath 0, Snooped 0, Dropped 28218  on Server Port 0 
		 Received packet drops details:
			Appeared on a wrong interface       : 0
			Incorrect length                    : 0
			Invalid protocol packet             : 0
		 Invalid Hardware type                  : 0
			Invalid context                     : 0
			Context not yet created             : 0
			Invalid layer 2 address length      : 0
			Invalid layer 3 address length      : 0
			Invalid source IP address           : 28
			Source IP address is our own        : 0
			No mem to create per intf structure : 0
			Source address mismatch with subnet : 0
			Directed broadcast source           : 0
			Invalid destination IP address      : 0
			Non-local destination IP address    : 20421
			Non-active FHRP dest IP address. Learn and drop
												: 0
			Invalid source MAC address          : 0
			Source MAC address is our own       : 0
			Received before arp initialization  : 0
			L2 packet on proxy-arp-enabled interface
												: 0
			L2 packet on untrusted L2 port      : 0
			Packet with VIP on standby FHRP     : 0
			Grat arp received on proxy-arp-enabled interface
												: 0
			Requests came for exising entries   : 15
			Requests came on a L2 interface     : 0
			L2FM query failed for a L2 Address  : 0
			Dropping due to tunneling failures  : 0
			Glean requests recv count : 71
			ARP refresh requests received from clients: 0
			Number of Signals received from L2rib : 0

		 ARP adjacency statistics

			Adds 43, Deletes 12, Timeouts 12
			 Failed due to limits: 0
	'''
	}

	golden_parsed_output_1 = {'statistics': {'adjacency': {'adjacency_adds': 5,
                              'adjacency_deletes': 0,
                              'adjacency_timeouts': 0},
                'received': {'anycast_proxy_arp': 0,
                             'dropped': 7,
                             'dropped_server_port': 0,
                             'drops_details': {'appeared_on_a_wrong_interface': 0,
                                               'context_not_created': 0,
                                               'directed_broadcast_source': 0,
                                               'dropping_due_to_tunneling_failures': 0,
                                               'grat_arp_received_on_proxy': 0,
                                               'incorrect_length': 0,
                                               'invalid_context': 0,
                                               'invalid_destination_ip_address': 0,
                                               'invalid_hardwaretype': 0,
                                               'invalid_layer2_address_length': 0,
                                               'invalid_layer3_address_length': 0,
                                               'invalid_protocol_packet': 0,
                                               'invalid_source_ip_address': 0,
                                               'invalid_source_mac_address': 0,
                                               'l2_packet_on_untrusted_l2_port': 0,
                                               'l2fm_query_failed_for_a_l2address': 0,
                                               'no_mem_to_create_per_intf_structure': 0,
                                               'non_active_fhrp_dest_ip': 0,
                                               'non_local_destination_ip_address': 7,
                                               'packet_with_vip_on_standby_fhrp': 0,
                                               'received_before_arp_initialization': 0,
                                               'requests_came_for_exising_entries': 0,
                                               'requests_came_on_a_l2_interface': 0,
                                               'source_address_mismatch_with_subnet': 0,
                                               'source_ip_address_is_our_own': 0,
                                               'source_mac_address_is_our_own': 0},
                             'enhanced_proxy_arp': 0,
                             'fastpath': 0,
                             'l2_port_track_proxy_arp': 0,
                             'l2_replies': 0,
                             'l2_requests': 0,
                             'local_proxy_arp': 0,
                             'proxy_arp': 0,
                             'replies': 55,
                             'requests': 5,
                             'snooped': 0,
                             'total': 67,
                             'tunneled': 0},
                'sent': {'dropped': 0,
                         'drops_details': {'adjacency_couldnt_be_added': 0,
                                           'client_enqueue_failed': 0,
                                           'context_not_created': 0,
                                           'dest_not_reachable_for_proxy_arp': 0,
                                           'dest_unreachable_for_enhanced_proxy': 0,
                                           'destnination_is_our_own_ip': 0,
                                           'destnination_on_l2_port_tracked': 0,
                                           'invalid_context': 0,
                                           'invalid_dest_ip': 0,
                                           'invalid_ifindex': 0,
                                           'invalid_local_proxy_arp': 0,
                                           'invalid_proxy_arp': 0,
                                           'invalid_src_ip': 0,
                                           'mbuf_operation_failed': 0,
                                           'null_source_ip': 0,
                                           'null_source_mac': 0,
                                           'unattached_ip': 0,
                                           'vip_is_not_active': 0},
                         'gratuitous': 2,
                         'l2_replies': 0,
                         'l2_requests': 0,
                         'replies': 5,
                         'requests': 57,
                         'total': 64,
                         'tunneled': 0}}}

	golden_output_1 = {'execute.return_value': '''
		nx-osv9000-1# show ip arp statistics

		ARP packet statistics for context default
		 Sent:
		 Total 64, Requests 57, Replies 5, Requests on L2 0, Replies on L2 0,
		 Gratuitous 2, Tunneled 0, Dropped 0
		 Send packet drops details:
		    MBUF operation failed               : 0
		    Context not yet created             : 0
		    Invalid context                     : 0
		    Invalid ifindex                     : 0
		    Invalid SRC IP                      : 0
		    Invalid DEST IP                     : 0
		    Destination is our own IP           :  0
		    Unattached IP                       :  0
		    Adjacency Couldn't be added         :  0
		    Null Source IP                      :  0
		    Null Source MAC                     :  0
		    Client Enqueue Failed               :  0
		    Dest. not reachable for proxy arp   :  0
		    Dest. unreachable for enhanced proxy:  0
		    Dest. on L2 port being tracked      :  0
		    Invalid Local proxy arp             :  0
		    Invalid proxy arp                   :  0
		   VIP is not active                   :  0
		 Received:
		 Total 67, Requests 5, Replies 55, Requests on L2 0, Replies on L2 0
		 Proxy arp 0, Local-Proxy arp 0,  Enhanced Proxy arp 0, Anycast proxy Proxy arp 0,  L2 Port-track Proxy arp 0,  Tunneled 0, Fastpath 0, Snooped 0, Dropped 7, on Server Port 0
		 Received packet drops details:
		    Appeared on a wrong interface       : 0
		    Incorrect length                    : 0
		    Invalid protocol packet             : 0
		 Invalid Hardware type                  : 0
		    Invalid context                     : 0
		    Context not yet created             : 0
		    Invalid layer 2 address length      : 0
		    Invalid layer 3 address length      : 0
		    Invalid source IP address           : 0
		    Source IP address is our own        : 0
		    No mem to create per intf structure : 0
		    Source address mismatch with subnet : 0
		    Directed broadcast source           : 0
		    Invalid destination IP address      : 0
		    Non-local destination IP address    : 7
		    Non-active FHRP dest IP address. Learn and drop
		                                        : 0
		    Invalid source MAC address          : 0
		    Source MAC address is our own       : 0
		    Received before arp initialization  : 0
		    L2 packet on proxy-arp-enabled interface
		                                        : 0
		    L2 packet on untrusted L2 port      : 0
		    Packet with VIP on standby FHRP     : 0
		    Grat arp received on proxy-arp-enabled interface
		                                        : 0
		    Requests came for exising entries   : 0
		    Requests came on a l2 interface     : 0
		    L2FM query failed for a L2 Address  : 0
		    Dropping due to tunneling failures  : 0

		 ARP adjacency statistics

		 Adds 5, Deletes 0, Timeouts 0

		nx-osv9000-1# 
	'''
	}

	golden_output_customer = {'execute.return_value': '''
		# show ip arp statistics
		ARP packet statistics for context default
		Sent:
		Total 125449722, Requests 41815694, Replies 83633906, Requests on L2 0, Replies on L2 0,
		Gratuitous 122, Tunneled 0, Dropped 0
		Send packet drops details:
			MBUF operation failed               : 0
			Context not yet created             : 0
			Invalid context                     : 0
			Invalid ifindex                     : 0
			Invalid SRC IP                      : 0
			Invalid DEST IP                     : 0
			Destination is our own IP           :  0
			Unattached IP                       :  0
		Adjacency Couldn't be added         :  0
			Null Source IP                      :  0
			Null Source MAC                     :  0
			Client Enqueue Failed               :  0
			Dest. not reachable for proxy arp   :  0
			Dest. unreachable for enhanced proxy:  0
			Dest. on L2 port being tracked      :  0
			Invalid Local proxy arp             :  0
			Invalid proxy arp                   :  0
		VIP is not active                   :  0
		Received:
		Total 268933895, Requests 83633906, Replies 3578191, Requests on L2 0, Replies on L2 0
		Proxy arp 0, Local-Proxy arp 0,  Enhanced Proxy arp 0, Anycast proxy Proxy arp 0,  L2 Port-track Proxy arp 0,  Tunneled 0, Fastpath
		0, Snooped 0, Dropped 181721798, on Server Port 0
		Received packet drops details:
			Appeared on a wrong interface       : 0
			Incorrect length                    : 0
			Invalid protocol packet             : 0
			Invalid context                     : 0
			Context not yet created             : 0
			Invalid layer 2 address length      : 0
			Invalid layer 3 address length      : 0
			Invalid source IP address           : 65347
			Source IP address is our own        : 1
			No mem to create per intf structure : 0
			Source address mismatch with subnet : 2804
			Directed broadcast source           : 0
			Invalid destination IP address      : 77
			Non-local destination IP address    : 181653418
			Non-active FHRP dest IP address. Learn and drop
												: 151
			Invalid source MAC address          : 0
			Source MAC address is our own       : 0
			Received before arp initialization  : 0
			L2 packet on proxy-arp-enabled interface
												: 0
			L2 packet on untrusted L2 port      : 0
			Packet with VIP on standby FHRP     : 0
			Grat arp received on proxy-arp-enabled interface
												: 0
			Requests came for exising entries   : 152075
			Requests came on a l2 interface     : 0
			L2FM query failed for a L2 Address  : 0
			Dropping due to tunneling failures  : 0
		
		ARP adjacency statistics
		
		Adds 9546429, Deletes 9546204, Timeouts 9546204
	'''}

	golden_parsed_output_customer = {
		'statistics': {
			'adjacency': {
				'adjacency_adds': 9546429,
				'adjacency_deletes': 9546204,
				'adjacency_timeouts': 9546204
			},
			'received': {
				'anycast_proxy_arp': 0,
				'dropped': 181721798,
				'dropped_server_port': 0,
				'drops_details': {
					'appeared_on_a_wrong_interface': 0,
					'context_not_created': 0,
					'directed_broadcast_source': 0,
					'dropping_due_to_tunneling_failures': 0,
					'grat_arp_received_on_proxy': 0,
					'incorrect_length': 0,
					'invalid_context': 0,
					'invalid_destination_ip_address': 77,
					'invalid_layer2_address_length': 0,
					'invalid_layer3_address_length': 0,
					'invalid_protocol_packet': 0,
					'invalid_source_ip_address': 65347,
					'invalid_source_mac_address': 0,
					'l2_packet_on_untrusted_l2_port': 0,
					'l2fm_query_failed_for_a_l2address': 0,
					'no_mem_to_create_per_intf_structure': 0,
					'non_active_fhrp_dest_ip': 151,
					'non_local_destination_ip_address': 181653418,
					'packet_with_vip_on_standby_fhrp': 0,
					'received_before_arp_initialization': 0,
					'requests_came_for_exising_entries': 152075,
					'requests_came_on_a_l2_interface': 0,
					'source_address_mismatch_with_subnet': 2804,
					'source_ip_address_is_our_own': 1,
					'source_mac_address_is_our_own': 0
				},
				'enhanced_proxy_arp': 0,
				'fastpath': 0,
				'l2_port_track_proxy_arp': 0,
				'l2_replies': 0,
				'l2_requests': 0,
				'local_proxy_arp': 0,
				'proxy_arp': 0,
				'replies': 3578191,
				'requests': 83633906,
				'snooped': 0,
				'total': 268933895,
				'tunneled': 0
			},
			'sent': {
				'dropped': 0,
				'drops_details': {
					'adjacency_couldnt_be_added': 0,
					'client_enqueue_failed': 0,
					'context_not_created': 0,
					'dest_not_reachable_for_proxy_arp': 0,
					'dest_unreachable_for_enhanced_proxy': 0,
					'destnination_is_our_own_ip': 0,
					'destnination_on_l2_port_tracked': 0,
					'invalid_context': 0,
					'invalid_dest_ip': 0,
					'invalid_ifindex': 0,
					'invalid_local_proxy_arp': 0,
					'invalid_proxy_arp': 0,
					'invalid_src_ip': 0,
					'mbuf_operation_failed': 0,
					'null_source_ip': 0,
					'null_source_mac': 0,
					'unattached_ip': 0,
					'vip_is_not_active': 0
				},
				'gratuitous': 122,
				'l2_replies': 0,
				'l2_requests': 0,
				'replies': 83633906,
				'requests': 41815694,
				'total': 125449722,
				'tunneled': 0
			}
		}
	}

	def test_empty(self):
		self.device = Mock(**self.empty_output)
		obj = ShowIpArpstatisticsVrfAll(device=self.device)
		with self.assertRaises(SchemaEmptyParserError):
			parsed_output = obj.parse()

	def test_golden(self):
		self.maxDiff = None
		self.device = Mock(**self.golden_output)
		obj = ShowIpArpstatisticsVrfAll(device=self.device)
		parsed_output = obj.parse()
		self.assertEqual(parsed_output, self.golden_parsed_output)

	def test_golden_1(self):
		self.maxDiff = None
		self.device = Mock(**self.golden_output_1)
		obj = ShowIpArpstatisticsVrfAll(device=self.device)
		parsed_output = obj.parse()
		self.assertEqual(parsed_output, self.golden_parsed_output_1)

	def test_golden_customer(self):
		self.maxDiff = None
		self.device = Mock(**self.golden_output_customer)
		obj = ShowIpArpstatisticsVrfAll(device=self.device)
		parsed_output = obj.parse()
		self.assertEqual(parsed_output,self.golden_parsed_output_customer)


# =============================
# Unit tests for:
# 	show ip arp
# 	show ip arp vrf {vrf}
# 	show ip arp vrf all
# =============================
class TestShowIpArp(unittest.TestCase):
	device = Device(name='aDevice')
	empty_output = {'execute.return_value': ''}

	golden_output = {'execute.return_value': ''' \
		R2# show ip arp

		Flags: * - Adjacencies learnt on non-active FHRP router
			+ - Adjacencies synced via CFSoE
			# - Adjacencies Throttled for Glean
			CP - Added via L2RIB, Control plane Adjacencies
			PS - Added via L2RIB, Peer Sync
			RO - Re-Originated Peer Sync Entry
			D - Static Adjacencies attached to down interface

		IP ARP Table for context default
		Total number of entries: 2
		Address         Age       MAC Address     Interface       Flags
		10.2.4.4        00:13:42  5e00.00ff.030a  Ethernet1/1
        10.2.4.5           -      aaaa.bbff.8888  Ethernet1/1      
		10.2.5.5        00:00:04  5e00.00ff.040b  Ethernet1/2
	'''}

	golden_parsed_output = {
		'interfaces':{  
			'Ethernet1/1':{  
				'ipv4':{  
					'neighbors':{  
						'10.2.4.4':{  
							'ip':'10.2.4.4',
							'link_layer_address':'5e00.00ff.030a',
							'physical_interface':'Ethernet1/1',
							'origin':'dynamic',
							'age':'00:13:42'
						},
						'10.2.4.5': {
							'ip':'10.2.4.5',
							'link_layer_address':'aaaa.bbff.8888',
							'physical_interface':'Ethernet1/1',
							'origin':'static',
							'age':'-'
						}
					}
				}
			},
			'Ethernet1/2':{  
				'ipv4':{  
					'neighbors':{  
						'10.2.5.5':{  
							'ip':'10.2.5.5',
							'link_layer_address':'5e00.00ff.040b',
							'physical_interface':'Ethernet1/2',
							'origin':'dynamic',
							'age':'00:00:04'
						}
					}
				}
			}
		},
		'statistics':{  
			'entries_total':2
		}
	}

	golden_output_2 = {'execute.return_value': '''
		R2# show ip arp vrf vni_10100

		Flags: * - Adjacencies learnt on non-active FHRP router
			+ - Adjacencies synced via CFSoE
			# - Adjacencies Throttled for Glean
			CP - Added via L2RIB, Control plane Adjacencies
			PS - Added via L2RIB, Peer Sync
			RO - Re-Originated Peer Sync Entry
			D - Static Adjacencies attached to down interface

		IP ARP Table for context vni_10100
		Total number of entries: 6
		Address         Age       MAC Address     Interface       Flags
		10.111.1.3     00:10:42  fa16.3eff.0987  Vlan101         + 
	'''}

	golden_parsed_output_2 = {
		'statistics': {
			'entries_total': 6
		},
		'interfaces': {
			'Vlan101': {
				'ipv4': {
					'neighbors': {
						'10.111.1.3': {
							'ip': '10.111.1.3',
							'link_layer_address': 'fa16.3eff.0987',
							'age': '00:10:42',
							'origin': 'dynamic',
							'physical_interface': 'Vlan101',
							'flags': '+'
						}
					}
				}
			}
		}
	}

	golden_output_3 = {'execute.return_value': '''
		R2# show ip arp vrf all

		Flags: * - Adjacencies learnt on non-active FHRP router
			+ - Adjacencies synced via CFSoE
			# - Adjacencies Throttled for Glean
			CP - Added via L2RIB, Control plane Adjacencies
			PS - Added via L2RIB, Peer Sync
			RO - Re-Originated Peer Sync Entry
			D - Static Adjacencies attached to down interface

		IP ARP Table for all contexts
		Total number of entries: 11
		Address         Age       MAC Address     Interface       Flags
		10.255.8.99     00:00:22  5e00.00ff.0909  mgmt0           
		10.2.4.4        00:13:47  5e00.00ff.030a  Ethernet1/1     
		10.2.5.5        00:00:09  5e00.00ff.040b  Ethernet1/2     
		10.1.3.3        00:00:09  5e00.00ff.0209  Ethernet1/6     
		10.111.1.3     00:09:20  fa16.3eff.0987  Vlan101         + 
		10.111.1.4     00:01:53  fa16.3eff.c271  Vlan101         
		10.111.2.3     00:09:20  fa16.3eff.58b9  Vlan101         
		10.111.2.4     00:17:48  fa16.3eff.e478  Vlan101         
		10.111.3.3     00:18:09  fa16.3eff.229b  Vlan101         + 
		10.111.3.4     00:00:37  fa16.3eff.947c  Vlan101         + 
		192.168.16.4     00:17:48  fa16.3eff.e478  Vlan202         
	'''}

	golden_parsed_output_3 = {
		'interfaces':{  
    		'mgmt0':{  
				'ipv4':{  
					'neighbors':{  
						'10.255.8.99':{  
							'ip':'10.255.8.99',
							'link_layer_address':'5e00.00ff.0909',
							'physical_interface':'mgmt0',
							'origin':'dynamic',
							'age':'00:00:22'
						}
					}
				}
			},
			'Ethernet1/1':{  
				'ipv4':{  
					'neighbors':{  
						'10.2.4.4':{  
							'ip':'10.2.4.4',
							'link_layer_address':'5e00.00ff.030a',
							'physical_interface':'Ethernet1/1',
							'origin':'dynamic',
							'age':'00:13:47'
						}
					}
				}
			},
			'Ethernet1/2':{  
				'ipv4':{  
					'neighbors':{  
						'10.2.5.5':{  
							'ip':'10.2.5.5',
							'link_layer_address':'5e00.00ff.040b',
							'physical_interface':'Ethernet1/2',
							'origin':'dynamic',
							'age':'00:00:09'
						}
					}
				}
			},
			'Ethernet1/6':{  
				'ipv4':{  
					'neighbors':{  
						'10.1.3.3':{  
							'ip':'10.1.3.3',
							'link_layer_address':'5e00.00ff.0209',
							'physical_interface':'Ethernet1/6',
							'origin':'dynamic',
							'age':'00:00:09'
						}
					}
				}
			},
			'Vlan101':{  
				'ipv4':{  
					'neighbors':{  
						'10.111.1.3':{  
							'ip':'10.111.1.3',
							'link_layer_address':'fa16.3eff.0987',
							'physical_interface':'Vlan101',
							'origin':'dynamic',
							'age':'00:09:20',
							'flags':'+'
						},
						'10.111.1.4':{  
							'ip':'10.111.1.4',
							'link_layer_address':'fa16.3eff.c271',
							'physical_interface':'Vlan101',
							'origin':'dynamic',
							'age':'00:01:53'
						},
						'10.111.2.3':{  
							'ip':'10.111.2.3',
							'link_layer_address':'fa16.3eff.58b9',
							'physical_interface':'Vlan101',
							'origin':'dynamic',
							'age':'00:09:20'
						},
						'10.111.2.4':{  
							'ip':'10.111.2.4',
							'link_layer_address':'fa16.3eff.e478',
							'physical_interface':'Vlan101',
							'origin':'dynamic',
							'age':'00:17:48'
						},
						'10.111.3.3':{  
							'ip':'10.111.3.3',
							'link_layer_address':'fa16.3eff.229b',
							'physical_interface':'Vlan101',
							'origin':'dynamic',
							'age':'00:18:09',
							'flags':'+'
						},
						'10.111.3.4':{  
							'ip':'10.111.3.4',
							'link_layer_address':'fa16.3eff.947c',
							'physical_interface':'Vlan101',
							'origin':'dynamic',
							'age':'00:00:37',
							'flags':'+'
						}
					}
				}
			},
			'Vlan202':{  
				'ipv4':{  
					'neighbors':{  
						'192.168.16.4':{  
							'ip':'192.168.16.4',
							'link_layer_address':'fa16.3eff.e478',
							'physical_interface':'Vlan202',
							'origin':'dynamic',
							'age':'00:17:48'
						}
					}
				}
			}
		},
		'statistics':{  
			'entries_total':11
		}
	}

	def test_empty(self):
		self.device = Mock(**self.empty_output)
		obj = ShowIpArp(device=self.device)
		with self.assertRaises(SchemaEmptyParserError):
			parsed_output = obj.parse()

	def test_golden(self):
		self.device = Mock(**self.golden_output)
		obj = ShowIpArp(device=self.device)
		parsed_output = obj.parse()
		self.assertEqual(parsed_output, self.golden_parsed_output)

	def test_golden_vrf(self):
		self.device = Mock(**self.golden_output_2)
		obj = ShowIpArp(device=self.device)
		parsed_output = obj.parse(vrf='vni_10100')
		self.assertEqual(parsed_output, self.golden_parsed_output_2)

	def test_golden_all(self):
		self.device = Mock(**self.golden_output_3)
		obj = ShowIpArp(device=self.device)
		parsed_output = obj.parse(vrf='all')
		self.assertEqual(parsed_output, self.golden_parsed_output_3)


if __name__ == '__main__':
	unittest.main()
