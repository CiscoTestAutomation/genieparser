"""show_arp.py

NXOS parsers for the following show commands:
	* 'show ip arp'
	* 'show ip arp detail vrf all'
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, And,\
										 Default, Use
from genie import parsergen

# =====================================
# Schema for 'show ip arp'
# =====================================
class ShowIpArpSchema(MetaParser):
	"""Schema for show ip arp"""

	schema = {
		Any():
		  {'Age': str,
		   'MAC Address': str,
		   'Interface': str,
		   'Address': str,
		   Optional('Flags'): str}}

# =====================================
# Parser for 'show ip arp'
# =====================================
class ShowIpArp(ShowIpArpSchema):
	"""Parser for:
		show ip arp
		parser class - implements detail parsing mechanisms for cli,xml and yang output.
	"""

	def cli(self):
		output = self.device.execute('show ip arp')
		 
		if not 'Flags' not in output:
			header = ['Address', 'Age', 'MAC Address', 'Interface']
		else:
			header = ['Address', 'Age', 'MAC Address', 'Interface', 'Flags']
		result = parsergen.oper_fill_tabular(
					  device_output=output,
					  device_os= 'nxos',
					  header_fields= header,
					  index= [0])
		return result.entries

# =======================================
# Schema for 'show ip arp detail vrf all'
# =======================================
class ShowIpArpDetailVrfAllSchema(MetaParser):
	"""Schema for show ip arp detail vrf all"""

	schema = {
		'interfaces': {
			Any(): {
				'ipv4': {
					'neighbors': {     
						Any(): {
							'ip': str,
							'link_layer_address': str,
							'origin': str,
							'age': str,
						},
					}
				}
			},
		}
	}

# =======================================
# Parser for 'show ip arp detail vrf all'
# =======================================
class ShowIpArpDetailVrfAll(ShowIpArpDetailVrfAllSchema):
	"""Parser for:
		show ip arp detail vrf all
		parser class - implements detail parsing mechanisms for cli,xml and yang output.
	"""

	FLAG_MAP = {'*': 'Adjacencies learnt on non-active FHRP router',
				'+': 'Adjacencies synced via CFSoE',
				'#': 'Adjacencies Throttled for Glean',
				'CP': 'Added via L2RIB, Control plane Adjacencies',
				'PS': 'Added via L2RIB, Peer Sync',
				'RO': 'Re-Originated Peer Sync Entry'}

	def cli(self):

		# excute command to get output
		out = self.device.execute('show ip arp detail vrf all')

		# initial variables
		ret_dict = {}

		# 10.1.7.1        00:17:15  0012.7f57.ac80  mgmt0            mgmt0
		p1 = re.compile(r'^(?P<address>[\d\.]+) +(?P<age>[\d+\-\:]+) '
		  '+(?P<mac>[\w\.]+) +(?P<interface>[\w\/\.]+) '
		  '+(?P<physical_interface>[\w\/\.]+)( +(?P<flag>[\*\w\+\#]+))?$')

		for line in out.splitlines():
			line = line.strip()
			if not line: 
				continue

			m = p1.match(line)
			if m:
				group = m.groupdict()
				address = group['address']
				interface = group['interface']
				final_dict = ret_dict.setdefault('interfaces', {}).setdefault(
					interface, {}).setdefault('ipv4', {}).setdefault(
					'neighbors', {}).setdefault(address, {})
				
				final_dict['ip'] = address
				final_dict['link_layer_address'] = group['mac']
				final_dict['age'] = group['age']
				if group['age'] == '-':
					final_dict['origin'] = 'static'
				else:
					final_dict['origin'] = 'dynamic'

				continue

		return ret_dict

# ========================================
# Schema for 'show ip arp summary vrf all'
# ========================================
class ShowIpArpSummaryVrfAllSchema(MetaParser):
	"""Schema for show ip arp summary vrf all"""

	schema = {
		'resolved': str,
		'incomplete': str,
		'unknown': str,
		'total': str,
	  }

# ========================================
# Parser for 'show ip arp summary vrf all'
# ========================================
class ShowIpArpSummaryVrfAll(ShowIpArpSummaryVrfAllSchema):
	"""Parser for:
		show ip arp summary vrf all
		parser class - implements detail parsing mechanisms for cli,xml and yang output.
	"""

	def cli(self):

		# excute command to get output
		out = self.device.execute('show ip arp summary vrf all')

		# initial variables
		ret_dict = {}

		# Resolved   : 12
		p1 = re.compile(r'^\s*Resolved +: +(?P<resolved>[\d]+)$')

		# Incomplete : 0 (Throttled : 0)
		p2 = re.compile(r'^\s*Incomplete +: +(?P<incomplete>[\w\(\)\:\s]+)$')

		# Unknown    : 0
		p3 = re.compile(r'^\s*Unknown +: +(?P<unknown>[\d]+)$')

		# Total      : 12
		p4 = re.compile(r'^\s*Total +: +(?P<total>[\d]+)$')

		for line in out.splitlines():
			line = line.strip()
			if not line: 
				continue

			m = p1.match(line)
			if m:
				ret_dict['resolved'] = m.groupdict()['resolved']
				continue

			m = p2.match(line)
			if m:
				ret_dict['incomplete'] = m.groupdict()['incomplete']
				continue

			m = p3.match(line)
			if m:
				ret_dict['unknown'] = m.groupdict()['unknown']
				continue

			m = p4.match(line)
			if m:
				ret_dict['total'] = m.groupdict()['total']
				continue

		return ret_dict

# ===========================================
# Schema for 'show ip arp statistics vrf all'
# ===========================================
class ShowIpArpstatisticsVrfAllSchema(MetaParser):
	"""Schema for show ip arp statistics vrf all"""

	schema = {
		'statistics':
			{'in_total': int,
			 'out_total': int,
			 'in_replies_pkts': int,
			 'out_replies_pkts': int,
			 'in_requests_pkts': int,
			 'out_requests_pkts': int,
			 'in_l2_requests': int,
			 'out_l2_requests': int,
			 'in_l2_replies': int,
			 'out_l2_replies': int,
			 Optional('in_gratuitous_pkts'): int,
			 'out_gratuitous_pkts': int,
			 'in_drops': int,
			 'out_drops': int,
			 'in_tunneled_pkts': int,
			 'out_tunneled_pkts': int,
			 'in_proxy_arp': int,
			 'in_local_proxy_arp': int,
			 'in_enhanced_proxy_arp': int,
			 'in_anycast_proxy_arp': int,
			 'in_l2_port_track_proxy_arp': int,
			 'in_fastpath': int,
			 'in_snooped': int,
			 'in_dropped_server_port': int,
			 'in_mbuf_operation_failed': int,
			 'in_context_not_created': int,
			 'out_context_not_created': int,
			 'in_invalid_context': int,
			 'out_invalid_context': int,
			 'in_invalid_ifindex': int,
			 'in_invalid_src_ip': int,
			 'out_invalid_dest_ip': int,
			 'in_destnination_is_our_own_ip': int,
			 'in_unattached_ip': int,
			 'out_adjacency_couldnt_be_added': int,
			 'in_null_source_ip': int,
			 'in_null_source_mac': int,
			 'in_client_enqueue_failed': int,
			 'in_dest_not_reachable_for_proxy_arp': int,
			 'in_dest_unreachable_for_enhanced_proxy': int,
			 'in_destnination_on_l2_port_tracked': int,
			 'in_invalid_local_proxy_arp': int,
			 'in_invalid_proxy_arp': int,
			 'in_vip_is_not_active': int,
			 'in_arp_refresh_skipped_over_core_and_flooded': int,
			 'in_appeared_on_a_wrong_interface': int,
			 'in_incorrect_length': int,
			 'in_invalid_protocol_packet': int,
			 'in_invalid_hardwaretype': int,
			 'in_invalid_context': int,
			 'in_invalid_layer2_address_length': int,
			 'in_invalid_source_ip_address': int,
			 'in_no_mem_to_create_per_intf_structure': int,
			 'in_invalid_layer3_address_length': int,
			 'in_source_address_mismatch_with_subnet': int,
			 'in_directed_broadcast_source': int,
			 'in_invalid_destination_ip_address': int,
			 'in_non_local_destination_ip_address': int,
			 'in_invalid_source_mac_address': int,
			 'in_source_mac_address_is_our_own': int,
			 'in_received_before_arp_initialization': int,
			 'in_l2_packet_on_untrusted_l2_port': int,
			 'in_packet_with_vip_on_standby_fhrp': int,
			 'in_requests_came_for_exising_entries': int,
			 'in_requests_came_on_a_l2_interface': int,
			 'in_l2fm_query_failed_for_a_l2address': int,
			 'in_dropping_due_to_tunneling_failures': int,
			 'in_glean_requests_recv_count': int,
			 'in_arp_refresh_requests_received_from_clients': int,
			 'in_number_of_signals_received_from_l2rib': int,
			 'adjacency_adds': int,
			 'adjacency_deletes': int,
			 'adjacency_timeouts': int,
			 'failed_due_to_limits': int,
			 'in_non_active_fhrp_dest_ip': int,
			 'in_grat_arp_received_on_proxy': int,
			 }
		}

# ===========================================
# Parser for 'show ip arp statistics vrf all'
# ===========================================
class ShowIpArpstatisticsVrfAll(ShowIpArpstatisticsVrfAllSchema):
	"""Parser for:
		show ip arp statistics vrf all
		parser class - implements detail parsing mechanisms for cli,xml and yang output.
	"""

	def cli(self):

		# excute command to get output
		out = self.device.execute('show ip arp statistics vrf all')

		# initial variables
		ret_dict = {}
		prefix = ''
		key = ''

		#  Sent:
		#  Received:
		p1 = re.compile(r'^\s*(?P<direction>[Sent|Received]+):$')

		# Total 0, Requests 22632, Replies 6582, Requests on L2 0, Replies on L2 0,
		p2 = re.compile(r'^\s*Total +(?P<total>[\w]+), +Requests '
			'+(?P<requests_pkts>[\w]+), +Replies +(?P<replies_pkts>[\w]+), '
			'+Requests +on +L2 +(?P<l2_requests>[\w]+), +Replies +on +L2 '
			'+(?P<l2_replies>[\w]+)(,)?$')

		# Gratuitous 58, Tunneled 0, Dropped 0
		p3 = re.compile(r'^\s*Gratuitous +(?P<gratuitous_pkts>[\w]+), +Tunneled '
			'+(?P<tunneled_pkts>[\w]+), +Dropped +(?P<drops>[\w]+)$')

		# Proxy arp 0, Local-Proxy arp 0,  Enhanced Proxy arp 0, Anycast proxy Proxy arp 0,  L2 Port-track Proxy arp 0,  Tunneled 0, Fastpath 0, Snooped 0, Dropped 28218  on Server Port 0 
		p4 = re.compile(r'^\s*Proxy +arp +(?P<proxy_arp>[\w]+), +Local-Proxy +arp '
			'+(?P<local_proxy_arp>[\w]+), +Enhanced +Proxy +arp +(?P<enhanced_proxy_arp>[\w]+), '
			'+Anycast +proxy +Proxy +arp +(?P<anycast_proxy_arp>[\w]+), +L2 +Port-track +Proxy +arp '
			'+(?P<l2_port_track_proxy_arp>[\w]+),'
			' +Tunneled +(?P<tunneled_pkts>[\w]+), +Fastpath +(?P<fastpath>[\w]+),'
			' +Snooped +(?P<snooped>[\w]+), +Dropped +(?P<drops>[\w]+)'
			' +on +Server +Port +(?P<dropped_server_port>[\w]+)$')

		# MBUF operation failed               : 0
		p5 = re.compile(r'^\s*MBUF +operation +failed +: +(?P<mbuf_operation_failed>[\d]+)$')

		# Context not yet created             : 0
		p6 = re.compile(r'^\s*Context +not +yet +created +: +(?P<context_not_created>[\d]+)$')

		# Invalid context                     : 0
		p7 = re.compile(r'^\s*Invalid +context +: +(?P<invalid_context>[\d]+)$')

		# Invalid ifindex                     : 0
		p8 = re.compile(r'^\s*Invalid +ifindex +: +(?P<invalid_ifindex>[\d]+)$')

		# Invalid SRC IP                      : 0
		p9 = re.compile(r'^\s*Invalid +SRC +IP +: +(?P<invalid_src_ip>[\d]+)$')

		# Invalid DEST IP                     : 0
		p10 = re.compile(r'^\s*Invalid +DEST +IP +: +(?P<out_invalid_dest_ip>[\d]+)$')

		# Destination is our own IP           :  26
		p11 = re.compile(r'^\s*Destination +is +our +own +IP +: +(?P<destnination_is_our_own_ip>[\d]+)$')

		# Unattached IP                       :  0
		p12 = re.compile(r'^\s*Unattached +IP +: +(?P<unattached_ip>[\d]+)$')

		# Adjacency Couldn't be added         :  0
		p13 = re.compile(r'^\s*Adjacency +Couldn\'t +be +added +: +(?P<adjacency_couldnt_be_added>[\d]+)$')

		# Null Source IP                      :  0
		p14 = re.compile(r'^\s*Null +Source +IP +: +(?P<null_source_ip>[\d]+)$')

		# Null Source MAC                     :  0
		p15 = re.compile(r'^\s*Null +Source +MAC +: +(?P<null_source_mac>[\d]+)$')

		# Client Enqueue Failed               :  0
		p16 = re.compile(r'^\s*Client +Enqueue +Failed +: +(?P<client_enqueue_failed>[\d]+)$')

		# Dest. not reachable for proxy arp   :  0
		p17 = re.compile(r'^\s*Dest. +not +reachable +for +proxy +arp +: +(?P<dest_not_reachable_for_proxy_arp>[\d]+)$')

		# Dest. unreachable for enhanced proxy :  0
		p18 = re.compile(r'^\s*Dest. +unreachable +for +enhanced +proxy +: +(?P<dest_unreachable_for_enhanced_proxy>[\d]+)$')

		# Dest. on L2 port being tracked      :  0
		p19 = re.compile(r'^\s*Dest. +on +L2 +port +being +tracked +: +(?P<destnination_on_l2_port_tracked>[\d]+)$')

		# Invalid Local proxy arp             :  0
		p20 = re.compile(r'^\s*Invalid +Local +proxy +arp +: +(?P<invalid_local_proxy_arp>[\d]+)$')

		# Invalid proxy arp                   :  0
		p21 = re.compile(r'^\s*Invalid +proxy +arp +: +(?P<invalid_proxy_arp>[\d]+)$')

		# VIP is not active                   :  0
		p22 = re.compile(r'^\s*VIP +is +not +active +: +(?P<vip_is_not_active>[\d]+)$')

		# ARP refresh skipped over core and flooded on server :  0
		p23 = re.compile(r'^\s*ARP +refresh +skipped +over +core +and +flooded +on +server +: +(?P<arp_refresh_skipped_over_core_and_flooded>[\d]+)$')

		# Appeared on a wrong interface :  0
		p24 = re.compile(r'^\s*Appeared +on +a +wrong +interface +: +(?P<appeared_on_a_wrong_interface>[\d]+)$')

		# Incorrect length                    : 0
		p25 = re.compile(r'^\s*Incorrect +length +: +(?P<incorrect_length>[\d]+)$')

		# Invalid protocol packet                    : 0
		p26 = re.compile(r'^\s*Invalid +protocol +packet +: +(?P<invalid_protocol_packet>[\d]+)$')

		# Invalid Hardware type                  : 0
		p27 = re.compile(r'^\s*Invalid +Hardware +type +: +(?P<invalid_hardwaretype>[\d]+)$')

		# Invalid layer 2 address length      : 0
		p30 = re.compile(r'^\s*Invalid +layer +2 +address +length +: +(?P<invalid_layer2_address_length>[\d]+)$')

		# Invalid source IP address           : 28
		p31 = re.compile(r'^\s*Invalid +source +IP +address +: +(?P<invalid_source_ip_address>[\d]+)$')

		# Source IP address is our own        : 0
		p32 = re.compile(r'^\s*Source +IP +address +is +our +own +: +(?P<source_ip_address_is_our_own>[\d]+)$')

		# No mem to create per intf structure : 0
		p32 = re.compile(r'^\s*No +mem +to +create +per +intf +structure +: +(?P<no_mem_to_create_per_intf_structure>[\d]+)$')

		# Invalid layer 3 address length      : 0
		p33 = re.compile(r'^\s*Invalid +layer +3 +address +length +: +(?P<invalid_layer3_address_length>[\d]+)$')

		# Source address mismatch with subnet : 0
		p34 = re.compile(r'^\s*Source +address +mismatch +with +subnet +: +(?P<source_address_mismatch_with_subnet>[\d]+)$')

		# Directed broadcast source           : 0
		p35 = re.compile(r'^\s*Directed +broadcast +source +: +(?P<directed_broadcast_source>[\d]+)$')

		# Invalid destination IP address      : 0
		p36 = re.compile(r'^\s*Invalid +destination +IP +address +: +(?P<invalid_destination_ip_address>[\d]+)$')

		# Non-local destination IP address    : 20421
		p37 = re.compile(r'^\s*Non-local +destination +IP +address +: +(?P<non_local_destination_ip_address>[\d]+)$')

		# Invalid source MAC address          : 0
		p38 = re.compile(r'^\s*Invalid +source +MAC +address +: +(?P<invalid_source_mac_address>[\d]+)$')

		# Source MAC address is our own       : 0
		p39 = re.compile(r'^\s*Source +MAC +address +is +our +own +: +(?P<source_mac_address_is_our_own>[\d]+)$')

		# Received before arp initialization  : 0
		p40 = re.compile(r'^\s*Received +before +arp +initialization +: +(?P<received_before_arp_initialization>[\d]+)$')

		# L2 packet on untrusted L2 port      : 0
		p41 = re.compile(r'^\s*L2 +packet +on +untrusted +L2 +port +: +(?P<l2_packet_on_untrusted_l2_port>[\d]+)$')

		# Packet with VIP on standby FHRP     : 0
		p42 = re.compile(r'^\s*Packet +with +VIP +on +standby +FHRP +: +(?P<packet_with_vip_on_standby_fhrp>[\d]+)$')

		# Requests came for exising entries   : 15
		p43 = re.compile(r'^\s*Requests +came +for +exising +entries +: +(?P<requests_came_for_exising_entries>[\d]+)$')

		# Requests came on a L2 interface     : 0
		p44 = re.compile(r'^\s*Requests +came +on +a +L2 +interface +: +(?P<requests_came_on_a_l2_interface>[\d]+)$')

		# L2FM query failed for a L2 Address  : 0
		p45 = re.compile(r'^\s*L2FM +query +failed +for +a +L2 +Address +: +(?P<l2fm_query_failed_for_a_l2address>[\d]+)$')

		# Dropping due to tunneling failures  : 0
		p46 = re.compile(r'^\s*Dropping due to tunneling failures +: +(?P<dropping_due_to_tunneling_failures>[\d]+)$')

		# Glean requests recv count : 71
		p47 = re.compile(r'^\s*Glean +requests +recv +count +: +(?P<glean_requests_recv_count>[\d]+)$')

		# ARP refresh requests received from clients: 0
		p48 = re.compile(r'^\s*ARP +refresh +requests +received +from +clients: +(?P<arp_refresh_requests_received_from_clients>[\d]+)$')

		# Number of Signals received from L2rib : 0
		p49 = re.compile(r'^\s*Number +of +Signals +received +from +L2rib +: +(?P<number_of_signals_received_from_l2rib>[\d]+)$')

		# Adds 43, Deletes 12, Timeouts 12
		p50 = re.compile(r'^\s*Adds +(?P<adjacency_adds>[\w]+), +Deletes '
			'+(?P<adjacency_deletes>[\w]+), +Timeouts +(?P<adjacency_timeouts>[\w]+)$')

		# Failed due to limits: 0
		p51 = re.compile(r'^\s*Failed +due +to +limits: +(?P<failed_due_to_limits>[\d]+)$')

		# Non-active FHRP dest IP address. Learn and drop
		p52 = re.compile(r'^\s*Non-active +FHRP +dest +IP +address. +Learn +and +drop$')

		# Grat arp received on proxy-arp-enabled interface
		p53 = re.compile(r'^\s*Grat +arp +received +on +proxy-arp-enabled +interface$')

		#                                     : 0
		p54 = re.compile(r'^\s*: +(?P<statistic_number>[\d]+)$')

		for line in out.splitlines():
			line = line.strip()
			if not line: 
				continue

			m = p1.match(line)
			if m:
				direction = m.groupdict()['direction']
				if direction == 'Sent':
					prefix = 'in'
				else:
					prefix = 'out'

				if 'statistics' not in ret_dict:
					ret_dict.setdefault('statistics', {})

				continue

			m = p2.match(line)
			if m:
				groups = m.groupdict()
				# total, requests, replies, reqs_l2, replies_l2
				ret_dict['statistics'].update({'{}_{}'.format(prefix, k): \
					int(v) for k, v in groups.items()})
				continue

			m = p3.match(line)
			if m:
				groups = m.groupdict()
				# gratuitous, tunneled, dropped
				ret_dict['statistics'].update({'out_{}'.format(k): \
					int(v) for k, v in groups.items()})
				continue

			m = p4.match(line)
			if m:
				groups = m.groupdict()
				# proxy_arp, local_proxy_arp, enhanced_proxy_arp, anycast_proxy_arp
				# l2_port_track_proxy_arp, tunneled, fastpath, snooped, dropped
				# dropped_server_port
				ret_dict['statistics'].update({'in_{}'.format(k): \
					int(v) for k, v in groups.items()})
				continue

			m = p5.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['{}_mbuf_operation_failed'.format(
					prefix)] = int(groups['mbuf_operation_failed'])
				continue

			m = p6.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['{}_context_not_created'.format(
					prefix)] = int(groups['context_not_created'])
				continue

			m = p7.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['{}_invalid_context'.format(prefix)] = \
					int(groups['invalid_context'])
				continue

			m = p8.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['{}_invalid_ifindex'.format(prefix)] = \
					int(groups['invalid_ifindex'])
				continue

			m = p9.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['{}_invalid_src_ip'.format(prefix)] = \
					int(groups['invalid_src_ip'])
				continue

			m = p10.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['out_invalid_dest_ip'] = \
					int(groups['out_invalid_dest_ip'])
				continue

			m = p11.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['{}_destnination_is_our_own_ip'.\
					format(prefix)] = int(groups['destnination_is_our_own_ip'])
				continue

			m = p12.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['{}_unattached_ip'.format(prefix)] = \
					int(groups['unattached_ip'])
				continue

			m = p13.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['out_adjacency_couldnt_be_added'] = int(
					groups['adjacency_couldnt_be_added'])
				continue

			m = p14.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['{}_null_source_ip'.format(prefix)] = \
					int(groups['null_source_ip'])
				continue

			m = p15.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['{}_null_source_mac'.format(prefix)] = \
					int(groups['null_source_mac'])
				continue

			m = p16.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['{}_client_enqueue_failed'.format(
					prefix)] = int(groups['client_enqueue_failed'])
				continue

			m = p17.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['{}_dest_not_reachable_for_proxy_arp'.\
					format(prefix)] = int(
						groups['dest_not_reachable_for_proxy_arp'])
				continue

			m = p18.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['{}_dest_unreachable_for_enhanced_proxy'.\
					format(prefix)] = int(
						groups['dest_unreachable_for_enhanced_proxy'])
				continue

			m = p19.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['{}_destnination_on_l2_port_tracked'.\
					format(prefix)] = int(
						groups['destnination_on_l2_port_tracked'])
				continue

			m = p20.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['{}_invalid_local_proxy_arp'.format(
					prefix)] = int(groups['invalid_local_proxy_arp'])
				continue

			m = p21.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['{}_invalid_proxy_arp'.format(
					prefix)] = int(groups['invalid_proxy_arp'])
				continue

			m = p22.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['{}_vip_is_not_active'.format(
					prefix)] = int(groups['vip_is_not_active'])
				continue

			m = p23.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']\
					['{}_arp_refresh_skipped_over_core_and_flooded'.format(
						prefix)] = int(
						groups['arp_refresh_skipped_over_core_and_flooded'])
				continue

			m = p24.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['in_appeared_on_a_wrong_interface'] = \
					int(groups['appeared_on_a_wrong_interface'])
				continue

			m = p25.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['in_incorrect_length'] = \
					int(groups['incorrect_length'])
				continue

			m = p26.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['in_invalid_protocol_packet'] = int(
					groups['invalid_protocol_packet'])
				continue

			m = p27.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['in_invalid_hardwaretype'] = int(
					groups['invalid_hardwaretype'])
				continue

			m = p30.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['in_invalid_layer2_address_length'] = \
					int(groups['invalid_layer2_address_length'])
				continue

			m = p31.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['in_invalid_source_ip_address'] = int(
					groups['invalid_source_ip_address'])
				continue

			m = p32.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['in_no_mem_to_create_per_intf_structure'] = \
					int(groups['no_mem_to_create_per_intf_structure'])
				continue

			m = p33.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['in_invalid_layer3_address_length'] = \
					int(groups['invalid_layer3_address_length'])
				continue

			m = p34.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['in_source_address_mismatch_with_subnet'] = \
					int(groups['source_address_mismatch_with_subnet'])
				continue

			m = p35.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['in_directed_broadcast_source'] = int(
					groups['directed_broadcast_source'])
				continue

			m = p36.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['in_invalid_destination_ip_address'] = \
					int(groups['invalid_destination_ip_address'])
				continue

			m = p37.match(line)
			if m:
				groups = m.groupdict()

				ret_dict['statistics']['in_non_local_destination_ip_address'] = \
					int(groups['non_local_destination_ip_address'])
				continue

			m = p38.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['in_invalid_source_mac_address'] = int(
					groups['invalid_source_mac_address'])
				continue

			m = p39.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['in_source_mac_address_is_our_own'] = int(
					groups['source_mac_address_is_our_own'])
				continue

			m = p40.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['in_received_before_arp_initialization'] = \
					int(groups['received_before_arp_initialization'])
				continue

			m = p41.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['in_l2_packet_on_untrusted_l2_port'] = \
					int(groups['l2_packet_on_untrusted_l2_port'])
				continue

			m = p42.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['in_packet_with_vip_on_standby_fhrp'] = \
					int(groups['packet_with_vip_on_standby_fhrp'])
				continue

			m = p43.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['in_requests_came_for_exising_entries'] = \
					int(groups['requests_came_for_exising_entries'])
				continue

			m = p44.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['in_requests_came_on_a_l2_interface'] = \
					int(groups['requests_came_on_a_l2_interface'])
				continue

			m = p45.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['in_l2fm_query_failed_for_a_l2address'] \
					= int(groups['l2fm_query_failed_for_a_l2address'])
				continue

			m = p46.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['in_dropping_due_to_tunneling_failures'] = \
					int(groups['dropping_due_to_tunneling_failures'])
				continue

			m = p47.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['in_glean_requests_recv_count'] = int(
					groups['glean_requests_recv_count'])
				continue

			m = p48.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']\
					['in_arp_refresh_requests_received_from_clients'] = int(
						groups['arp_refresh_requests_received_from_clients'])
				continue

			m = p49.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']\
					['in_number_of_signals_received_from_l2rib'] = int(
						groups['number_of_signals_received_from_l2rib'])
				continue

			m = p50.match(line)
			if m:
				groups = m.groupdict()
				if 'statistics' not in ret_dict:
					ret_dict.setdefault('statistics', {})
				# adjacency_adds, adjacency_deletes, adjacency_timeouts
				ret_dict['statistics'].update({k: int(v) \
					for k, v in groups.items()})
				continue

			m = p51.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['failed_due_to_limits'] = \
					int(groups['failed_due_to_limits'])
				continue

			m = p52.match(line)
			if m:
				key = 'non_active_fhrp_dest_ip'
				continue

			m = p53.match(line)
			if m:
				key = 'grat_arp_received_on_proxy'
				continue

			m = p54.match(line)
			if m and key:
				ret_dict['statistics']['in_{}'.format(key)] = \
					int(m.groupdict()['statistic_number'])
				key = ''
				continue

		return ret_dict