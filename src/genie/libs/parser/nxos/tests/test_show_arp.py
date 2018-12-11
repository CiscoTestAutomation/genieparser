# Python
import unittest
from unittest.mock import Mock

# ATS
from ats.topology import Device

# Metaparset
from genie.metaparser.util.exceptions import SchemaEmptyParserError, \
											 SchemaMissingKeyError

# Parser
from genie.libs.parser.nxos.show_arp import ShowIpArpDetailVrfAll, \
											ShowIpArpSummaryVrfAll, \
											ShowIpArpstatisticsVrfAll


#=========================================================
# Unit test for show ip arp detail vrf all
#=========================================================
class test_show_ip_arp_detail_vrf_all(unittest.TestCase):

	device = Device(name='aDevice')
	empty_output = {'execute.return_value': ''}

	golden_parsed_output = {
		'interfaces': {
			'Ethernet1/1': {
				'ipv4': {
					'neighbors': {
						'10.1.3.5': {
							'age': '-',
                            'ip': '10.1.3.5',
                            'link_layer_address': 'aaaa.bbbb.cccc',
                            'origin': 'static'}
                    }
                }
            },
            'Ethernet1/1.1': {
            	'ipv4': {
            		'neighbors': {
            			'201.0.1.2': {
            				'age': '00:01:53',
                           	'ip': '201.0.1.2',
                           	'link_layer_address': '000c.292a.1eaf',
                           	'origin': 'dynamic'}
                    }
                }
            },
            'Ethernet1/1.2': {
            	'ipv4': {
            		'neighbors': {
            			'201.1.1.2': {
            				'age': '00:00:47',
                           	'ip': '201.1.1.2',
                           	'link_layer_address': '000c.292a.1eaf',
                           	'origin': 'dynamic'}
                    }
                }
            },
            'Ethernet1/1.4': {
            	'ipv4': {
            		'neighbors': {
            			'201.4.1.2': {
            				'age': '00:08:42',
                           	'ip': '201.4.1.2',
                           	'link_layer_address': '000c.292a.1eaf',
                           	'origin': 'dynamic'}
                    }
                }
            },
            'Ethernet1/2.1': {
            	'ipv4': {
            		'neighbors': {
            			'201.0.2.2': {
            				'age': '00:18:24',
                           	'ip': '201.0.2.2',
                           	'link_layer_address': '000c.2904.5840',
                           	'origin': 'dynamic'}
                    }
                }
            },
            'Ethernet1/2.2': {
            	'ipv4': {
            		'neighbors': {
            			'201.1.2.2': {
            				'age': '00:05:21',
                           	'ip': '201.1.2.2',
                           	'link_layer_address': '000c.2904.5840',
                           	'origin': 'dynamic'}
                    }
                }
            },
            'Ethernet1/2.4': {
            	'ipv4': {
            		'neighbors': {
            			'201.4.2.2': {
            				'age': '00:10:51',
                           	'ip': '201.4.2.2',
                           	'link_layer_address': '000c.2904.5840',
                           	'origin': 'dynamic'}
                    }
                }
            },
            'Ethernet1/4.100': {
            	'ipv4': {
            		'neighbors': {
            			'50.1.1.101': {
            				'age': '00:01:28',
                          	'ip': '50.1.1.101',
                          	'link_layer_address': '0000.71c7.6e61',
                          	'origin': 'dynamic'}
                    }
                }
            },
            'Ethernet1/4.101': {
            	'ipv4': {
            		'neighbors': {
            			'50.2.1.101': {
            				'age': '00:01:28',
                          	'ip': '50.2.1.101',
                          	'link_layer_address': '0000.71c7.75c1',
                          	'origin': 'dynamic'}
                    }
                }
            },
            'Ethernet1/4.200': {
            	'ipv4': {
            		'neighbors': {
            			'55.1.1.101': {
            				'age': '00:01:28',
                          	'ip': '55.1.1.101',
                          	'link_layer_address': '0000.0068.ce6f',
                          	'origin': 'dynamic'}
                    }
                }
            },
            'mgmt0': {
            	'ipv4': {
            		'neighbors': {
            			'10.1.7.1': {
            				'age': '00:17:15',
                          	'ip': '10.1.7.1',
                          	'link_layer_address': '0012.7f57.ac80',
                          	'origin': 'dynamic'},
                     	'10.1.7.250': {
                     		'age': '00:14:24',
                            'ip': '10.1.7.250',
                            'link_layer_address': '0050.5682.7915',
                            'origin': 'dynamic'},
                     	'10.1.7.253': {
                     		'age': '00:10:22',
                            'ip': '10.1.7.253',
                            'link_layer_address': '0050.56a4.a9fc',
                            'origin': 'dynamic'}
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
		10.1.7.1        00:17:15  0012.7f57.ac80  mgmt0            mgmt0               
		10.1.7.250      00:14:24  0050.5682.7915  mgmt0            mgmt0               
		10.1.7.253      00:10:22  0050.56a4.a9fc  mgmt0            mgmt0               
		10.1.3.5           -      aaaa.bbbb.cccc  Ethernet1/1      Ethernet1/1              
		201.0.1.2       00:01:53  000c.292a.1eaf  Ethernet1/1.1    Ethernet1/1.1       
		201.1.1.2       00:00:47  000c.292a.1eaf  Ethernet1/1.2    Ethernet1/1.2       
		201.4.1.2       00:08:42  000c.292a.1eaf  Ethernet1/1.4    Ethernet1/1.4       
		201.0.2.2       00:18:24  000c.2904.5840  Ethernet1/2.1    Ethernet1/2.1       
		201.1.2.2       00:05:21  000c.2904.5840  Ethernet1/2.2    Ethernet1/2.2       
		201.4.2.2       00:10:51  000c.2904.5840  Ethernet1/2.4    Ethernet1/2.4       
		50.1.1.101      00:01:28  0000.71c7.6e61  Ethernet1/4.100  Ethernet1/4.100     
		50.2.1.101      00:01:28  0000.71c7.75c1  Ethernet1/4.101  Ethernet1/4.101     
		55.1.1.101      00:01:28  0000.0068.ce6f  Ethernet1/4.200  Ethernet1/4.200  
	'''
	}


	def test_empty(self):
		self.device = Mock(**self.empty_output)
		obj = ShowIpArpDetailVrfAll(device=self.device)
		with self.assertRaises(SchemaEmptyParserError):
			parsed_output = obj.parse()

	def test_golden(self):
		self.maxDiff = None
		self.device = Mock(**self.golden_output)
		obj = ShowIpArpDetailVrfAll(device=self.device)
		parsed_output = obj.parse()
		self.assertEqual(parsed_output, self.golden_parsed_output)

#=========================================================
# Unit test for show ip arp summary vrf all
#=========================================================
class test_show_ip_arp_summary_vrf_all(unittest.TestCase):

	device = Device(name='aDevice')
	empty_output = {'execute.return_value': ''}

	golden_parsed_output = {
		'incomplete': '0 (Throttled : 0)',
		'resolved': '12',
		'total': '12',
		'unknown': '0'}

	golden_output = {'execute.return_value': '''
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

#=========================================================
# Unit test for show ip arp statistics vrf all
#=========================================================
class test_show_ip_arp_statistics_vrf_all(unittest.TestCase):

	device = Device(name='aDevice')
	empty_output = {'execute.return_value': ''}

	golden_parsed_output = {
		'statistics': {
			'adjacency_adds': 43,
			'adjacency_deletes': 12,
			'adjacency_timeouts': 12,
			'failed_due_to_limits': 0,
			'in_anycast_proxy_arp': 0,
			'in_appeared_on_a_wrong_interface': 0,
			'in_arp_refresh_requests_received_from_clients': 0,
			'in_arp_refresh_skipped_over_core_and_flooded': 0,
			'in_client_enqueue_failed': 0,
			'in_context_not_created': 0,
			'in_dest_not_reachable_for_proxy_arp': 0,
			'in_dest_unreachable_for_enhanced_proxy': 0,
			'in_destnination_is_our_own_ip': 26,
			'in_destnination_on_l2_port_tracked': 0,
			'in_directed_broadcast_source': 0,
			'in_dropped_server_port': 0,
			'in_dropping_due_to_tunneling_failures': 0,
			'in_drops': 28218,
			'in_enhanced_proxy_arp': 0,
			'in_fastpath': 0,
			'in_glean_requests_recv_count': 71,
			'in_grat_arp_received_on_proxy': 0,
			'in_incorrect_length': 0,
			'in_invalid_context': 0,
			'in_invalid_destination_ip_address': 0,
			'in_invalid_hardwaretype': 0,
			'in_invalid_ifindex': 0,
			'in_invalid_layer2_address_length': 0,
			'in_invalid_layer3_address_length': 0,
			'in_invalid_local_proxy_arp': 0,
			'in_invalid_protocol_packet': 0,
			'in_invalid_proxy_arp': 0,
			'in_invalid_source_ip_address': 28,
			'in_invalid_source_mac_address': 0,
			'in_invalid_src_ip': 0,
			'in_l2_packet_on_untrusted_l2_port': 0,
			'in_l2_port_track_proxy_arp': 0,
			'in_l2_replies': 0,
			'in_l2_requests': 0,
			'in_l2fm_query_failed_for_a_l2address': 0,
			'in_local_proxy_arp': 0,
			'in_mbuf_operation_failed': 0,
			'in_no_mem_to_create_per_intf_structure': 0,
			'in_non_active_fhrp_dest_ip': 0,
			'in_non_local_destination_ip_address': 20421,
			'in_null_source_ip': 0,
			'in_null_source_mac': 0,
			'in_number_of_signals_received_from_l2rib': 0,
			'in_packet_with_vip_on_standby_fhrp': 0,
			'in_proxy_arp': 0,
			'in_received_before_arp_initialization': 0,
			'in_replies_pkts': 998,
			'in_requests_came_for_exising_entries': 15,
			'in_requests_came_on_a_l2_interface': 0,
			'in_requests_pkts': 2102,
			'in_snooped': 0,
			'in_source_address_mismatch_with_subnet': 0,
			'in_source_mac_address_is_our_own': 0,
			'in_total': 3158,
			'in_tunneled_pkts': 0,
			'in_unattached_ip': 0,
			'in_vip_is_not_active': 0,
			'out_adjacency_couldnt_be_added': 0,
			'out_context_not_created': 0,
			'out_drops': 0,
			'out_gratuitous_pkts': 58,
			'out_invalid_context': 0,
			'out_invalid_dest_ip': 0,
			'out_l2_replies': 0,
			'out_l2_requests': 0,
			'out_replies_pkts': 6582,
			'out_requests_pkts': 22632,
			'out_total': 0,
			'out_tunneled_pkts': 0}
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


if __name__ == '__main__':
	unittest.main()