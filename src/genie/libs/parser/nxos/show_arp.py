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
from genie.libs.parser.utils.common import Common


# =====================================
# Schema for 'show ip arp'
# =====================================
class ShowIpArpSchema(MetaParser):
	"""Schema for show ip arp"""

	schema = {
		Optional('statistics'): {
			Optional('entries_total'): int
		},
		'interfaces': {
			Any(): {
				'ipv4': {
					'neighbors': {
						Any(): {
							'ip': str,
							'link_layer_address': str,
							'age': str,
							'origin': str,
							'physical_interface': str,
							Optional('encap_type'): str,
							Optional('flags'): str
						}
					}
				}
			}
		}
	}


# =====================================
# Parser for:
# 	show ip arp
# 	show ip arp vrf {vrf}
# 	show ip arp vrf all
# =====================================
class ShowIpArp(ShowIpArpSchema):
	"""Parser for:
		show ip arp
		show ip arp vrf {vrf}
		show ip arp vrf all
	"""
	cli_command = ['show ip arp', 'show ip arp vrf {vrf}']
	exclude = ['age']

	def cli(self, vrf='', output=None):
		if vrf:
			cmd = self.cli_command[1].format(vrf=vrf)
		else:
			cmd = self.cli_command[0]
			vrf = 'default'

		if output is None:
			out = self.device.execute(cmd)
		else:
			out = output

		res_dict = {}

		# IP ARP Table for all contexts
		# IP ARP Table for context vni_10100
		# IP ARP Table for context default
		p1 = re.compile(r'^IP +ARP +Table +for +(context +)?(?P<vrf>[\S]+)( +contexts)?$')

		# Total number of entries: 11
		p2 = re.compile(r'^Total +number +of +entries:\s+(?P<num_entries>\d+)$')

		# 192.168.16.226 0 0006.d6ff.632b ARPA GigabitEthernet1/1
		# 10.111.1.3     00:09:20  fa16.3eff.0987  Vlan101         +
		# 10.111.1.4     00:01:53  fa16.3eff.c271  Vlan101
        # 10.23.90.2      00:01:05  fa16.3eff.f80e  Ethernet1/1.390
		p3 = re.compile(r'^(?P<ip_address>[\d\.]+)\s+(?P<age>[\d:-]+)\s+(?P<mac_address>[\w\.]+)\s+'
						r'((?P<encap_type>ARPA)\s+)?(?P<interface>\S+)(\s+(?P<flags>\S))?$')

		for line in out.splitlines():
			line = line.strip()

			# IP ARP Table for all contexts
			# IP ARP Table for context vni_10100
			# IP ARP Table for context default
			m = p1.match(line)
			if m:
				if 'interfaces' not in res_dict:
					interfaces_dict = res_dict.setdefault('interfaces', {})
				continue

			# Total number of entries: 11
			m = p2.match(line)
			if m:
				if 'statistics' not in res_dict:
					statistics_dict = res_dict.setdefault('statistics', {})

				groups = m.groupdict()
				statistics_dict.update({'entries_total': int(groups['num_entries'])})
				continue

			# 192.168.16.226 0 0006.d6ff.632b ARPA GigabitEthernet1/1
			# 10.111.1.3     00:09:20  fa16.3eff.0987  Vlan101         +
			# 10.111.1.4     00:01:53  fa16.3eff.c271  Vlan101
			m = p3.match(line)
			if m:
				# Rare case (but found through run_parsers) - Only used to 
				# setup data structure when output lines never match p1
				if 'interfaces' not in res_dict:
					interfaces_dict = res_dict.setdefault('interfaces', {})

				groups = m.groupdict()
				interface = groups['interface']
				ip_address = groups['ip_address']
				mac_address = groups['mac_address']
				age = groups['age']

				interface_dict = interfaces_dict.setdefault(interface, {})
				neighbors_dict = interface_dict.setdefault('ipv4', {}).setdefault('neighbors', {})
				ip_dict = neighbors_dict.setdefault(ip_address, {})
				ip_dict.update({'ip': ip_address})
				ip_dict.update({'link_layer_address': mac_address})
				ip_dict.update({'physical_interface': interface})

				if '-' in age:
					origin = 'static'
				else:
					origin = 'dynamic'

				ip_dict.update({'origin': origin})
				ip_dict.update({'age': age})

				if groups['encap_type']:
					ip_dict.update({'encap_type': groups['encap_type']})

				if groups['flags']:
					ip_dict.update({'flags': groups['flags']})
		
		return res_dict


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
							'physical_interface': str,
							Optional('flag'): str,
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

	cli_command = ['show ip arp detail vrf {vrf}', 'show ip arp detail']
	exclude = ['age']

	def cli(self, vrf=None, output=None):

		if vrf:
			cmd = self.cli_command[0].format(vrf=vrf)
		else:
			cmd = self.cli_command[1]

		# execute command to get output
		if output is None:
			out = self.device.execute(cmd)
		else:
			out = output

		# initial variables
		ret_dict = {}

		# Address         Age       MAC Address     Interface        Physical Interface  Flags
		# 10.1.7.1        00:17:15  0012.7fff.04d7  mgmt0            mgmt0
		# 172.16.23.22    00:13:48  00a0.98ff.16cc  Vlan651          port-channel1050    +
		# 172.16.8.178    00:00:04  INCOMPLETE      Vlan392          Vlan392
		p1 = re.compile(r'^(?P<address>[\d\.]+) +(?P<age>[\d+\-\:]+) '
						r'+(?P<mac>[\w\.]+) +(?P<interface>\S+) '
						r'+(?P<physical_interface>\S+)'
						r'( +(?P<flag>[\*\w\+\#]+))?$')

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
				final_dict['physical_interface'] = group['physical_interface']
				if group['age'] == '-':
					final_dict['origin'] = 'static'
				else:
					final_dict['origin'] = 'dynamic'

				flag = self.FLAG_MAP.get(group['flag'])

				if flag:
					final_dict['flag'] = flag

				continue

		return ret_dict

# ========================================
# Schema for 'show ip arp summary vrf all'
# ========================================
class ShowIpArpSummaryVrfAllSchema(MetaParser):
	"""Schema for show ip arp summary vrf all"""

	schema = {
		'resolved': int,
		'incomplete': int,
		'throttled': int,
		'unknown': int,
		'total': int,
	  }

# ========================================
# Parser for 'show ip arp summary vrf all'
# ========================================
class ShowIpArpSummaryVrfAll(ShowIpArpSummaryVrfAllSchema):
	"""Parser for:
		show ip arp summary vrf all
		parser class - implements detail parsing mechanisms for cli,xml and yang output.
	"""
	cli_command = ['show ip arp summary vrf {vrf}', 'show ip arp summary']

	def cli(self, vrf=None, output=None):
		if output is None:
			if vrf:
				cmd = self.cli_command[0].format(vrf=vrf)
			else:
				cmd = self.cli_command[1]
			out = self.device.execute(cmd)
		else:
			out = output

		# initial variables
		ret_dict = {}

		# Resolved   : 12
		p1 = re.compile(r'^\s*Resolved +: +(?P<resolved>[\d]+)$')

		# Incomplete : 0 (Throttled : 0)
		p2 = re.compile(r'^\s*Incomplete +: +(?P<incomplete>\w+)'
			' +\(Throttled +: +(?P<throttled>\w+)\)$')

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
				ret_dict['resolved'] = int(m.groupdict()['resolved'])
				continue

			m = p2.match(line)
			if m:
				ret_dict['incomplete'] = int(m.groupdict()['incomplete'])
				ret_dict['throttled'] = int(m.groupdict()['throttled'])
				continue

			m = p3.match(line)
			if m:
				ret_dict['unknown'] = int(m.groupdict()['unknown'])
				continue

			m = p4.match(line)
			if m:
				ret_dict['total'] = int(m.groupdict()['total'])
				continue

		return ret_dict

# ===========================================
# Schema for 'show ip arp statistics vrf all'
# ===========================================
class ShowIpArpstatisticsVrfAllSchema(MetaParser):
	"""Schema for show ip arp statistics vrf all"""

	schema = {
		'statistics': {
			'sent':{
				'total': int,
				'requests': int,
				'replies': int,
				'l2_requests': int,
				'l2_replies': int,
				'gratuitous': int,
				'tunneled': int,
				'dropped': int,
				'drops_details': {
					'mbuf_operation_failed': int,
					Optional('context_not_created'): int,
					Optional('invalid_context'): int,
					Optional('invalid_ifindex'): int,
					Optional('invalid_src_ip'): int,
					Optional('invalid_dest_ip'): int,
					Optional('destnination_is_our_own_ip'): int,
					Optional('unattached_ip'): int,
					Optional('adjacency_couldnt_be_added'): int,
					Optional('null_source_ip'): int,
					Optional('null_source_mac'): int,
					Optional('client_enqueue_failed'): int,
					Optional('dest_not_reachable_for_proxy_arp'): int,
					Optional('dest_unreachable_for_enhanced_proxy'): int,
					Optional('destnination_on_l2_port_tracked'): int,
					Optional('invalid_local_proxy_arp'): int,
					Optional('invalid_proxy_arp'): int,
					Optional('vip_is_not_active'): int,
					Optional('arp_refresh_skipped_over_core_and_flooded'): int,
				}
			},
			'received':{
				'total': int,
				'requests': int,
				'replies': int,
				'l2_requests': int,
				'l2_replies': int,
				'proxy_arp': int,
				'local_proxy_arp': int,
				Optional('enhanced_proxy_arp'): int,
				Optional('anycast_proxy_arp'): int,
				Optional('l2_port_track_proxy_arp'): int,
				'tunneled': int,
				Optional('fastpath'): int,
				Optional('snooped'): int,
				'dropped': int,
				Optional('dropped_server_port'): int,
				'drops_details': {
					'context_not_created': int,
					'invalid_context': int,
					Optional('invalid_hardwaretype'): int,
					'invalid_layer2_address_length': int,
					'invalid_source_ip_address': int,
					'no_mem_to_create_per_intf_structure': int,
					'invalid_layer3_address_length': int,
					'source_address_mismatch_with_subnet': int,
					'directed_broadcast_source': int,
					'invalid_destination_ip_address': int,
					'non_local_destination_ip_address': int,
					'invalid_source_mac_address': int,
					'source_mac_address_is_our_own': int,
					'received_before_arp_initialization': int,
					'l2_packet_on_untrusted_l2_port': int,
					'packet_with_vip_on_standby_fhrp': int,
					'requests_came_for_exising_entries': int,
					'requests_came_on_a_l2_interface': int,
					'l2fm_query_failed_for_a_l2address': int,
					'dropping_due_to_tunneling_failures': int,
					Optional('glean_requests_recv_count'): int,
					Optional('arp_refresh_requests_received_from_clients'): int,
					Optional('number_of_signals_received_from_l2rib'): int,
					'non_active_fhrp_dest_ip': int,
					'grat_arp_received_on_proxy': int,
					'invalid_protocol_packet': int,
					'appeared_on_a_wrong_interface': int,
					'incorrect_length': int,
					Optional('source_ip_address_is_our_own'): int,
				}
			},
			'adjacency':{
				'adjacency_adds': int,
				'adjacency_deletes': int,
				'adjacency_timeouts': int,
				Optional('failed_due_to_limits'): int,
				}
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
	cli_command = ['show ip arp statistics vrf {vrf}', 'show ip arp statistics']

	def cli(self, vrf=None, output=None):
		if output is None:
			if vrf:
				cmd = self.cli_command[0].format(vrf=vrf)
			else:
				cmd = self.cli_command[1]
			out = self.device.execute(cmd)
		else:
			out = output

		# initial variables
		ret_dict = {}
		direction = ''
		prefix = ''
		key = ''

		#  Sent:
		p1 = re.compile(r'^\s*Sent:$')

		#  Received:
		p1_1 = re.compile(r'^\s*Received:$')

		# Total 0, Requests 22632, Replies 6582, Requests on L2 0, Replies on L2 0,
		p2 = re.compile(r'^\s*Total +(?P<total>[\w]+), +Requests '
			r'+(?P<requests>[\w]+), +Replies +(?P<replies>[\w]+), '
			r'+Requests +on +L2 +(?P<l2_requests>[\w]+), +Replies +on +L2 '
			r'+(?P<l2_replies>[\w]+)(,)?$')

		# Gratuitous 58, Tunneled 0, Dropped 0
		p3 = re.compile(r'^\s*Gratuitous +(?P<gratuitous>[\w]+), +Tunneled '
			'+(?P<tunneled>[\w]+), +Dropped +(?P<dropped>[\w]+)$')

		# Proxy arp 0, Local-Proxy arp 0,  Enhanced Proxy arp 0, Anycast proxy Proxy arp 0,  L2 Port-track Proxy arp 0,  Tunneled 0, Fastpath 0, Snooped 0, Dropped 28218  on Server Port 0 
		# Proxy arp 0, Local-Proxy arp 0, Tunneled 0, Fastpath 0, Snooped 0, Dropped 4
		p4 = re.compile(r'^Proxy +arp +(?P<proxy_arp>[\w]+), +Local-Proxy +'
			r'arp +(?P<local_proxy_arp>[\w]+),( +Enhanced +Proxy +arp +'
			r'(?P<enhanced_proxy_arp>[\w]+),)?( +Anycast +proxy +Proxy +'
			r'arp +(?P<anycast_proxy_arp>[\w]+),)?( +L2 +Port-track +Proxy +'
			r'arp +(?P<l2_port_track_proxy_arp>[\w]+),?)?( +Tunneled +'
			r'(?P<tunneled>[\w]+))?,?( +Fastpath +(?P<fastpath>[\w]+))?,?'
			r'( +Snooped +(?P<snooped>[\w]+))?,?( +Dropped +(?P<dropped>[\w]+))'
			r'?,?( +on +Server +Port +(?P<dropped_server_port>[\w]+))?')

		# MBUF operation failed               : 0
		p5 = re.compile(r'^\s*MBUF +operation +failed +: '
						r'+(?P<mbuf_operation_failed>[\d]+)$')

		# Context not yet created             : 0
		p6 = re.compile(r'^\s*Context +not +yet +created +: '
						r'+(?P<context_not_created>[\d]+)$')

		# Invalid context                     : 0
		p7 = re.compile(r'^\s*Invalid +context +: +(?P<invalid_context>[\d]+)$')

		# Invalid ifindex                     : 0
		p8 = re.compile(r'^\s*Invalid +ifindex +: +(?P<invalid_ifindex>[\d]+)$')

		# Invalid SRC IP                      : 0
		p9 = re.compile(r'^\s*Invalid +SRC +IP +: +(?P<invalid_src_ip>[\d]+)$')

		# Invalid DEST IP                     : 0
		p10 = re.compile(r'^\s*Invalid +DEST +IP +: +(?P<invalid_dest_ip>[\d]+)$')

		# Destination is our own IP           :  26
		p11 = re.compile(r'^\s*Destination +is +our +own +IP +: '
						 r'+(?P<destnination_is_our_own_ip>[\d]+)$')

		# Unattached IP                       :  0
		p12 = re.compile(r'^\s*Unattached +IP +: +(?P<unattached_ip>[\d]+)$')

		# Adjacency Couldn't be added         :  0
		p13 = re.compile(r'^\s*Adjacency +Couldn\'t +be +added +: '
						 r'+(?P<adjacency_couldnt_be_added>[\d]+)$')

		# Null Source IP                      :  0
		p14 = re.compile(r'^\s*Null +Source +IP +: +(?P<null_source_ip>[\d]+)$')

		# Null Source MAC                     :  0
		p15 = re.compile(r'^\s*Null +Source +MAC +: +(?P<null_source_mac>[\d]+)$')

		# Client Enqueue Failed               :  0
		p16 = re.compile(r'^\s*Client +Enqueue +Failed +: +(?P<client_enqueue_failed>[\d]+)$')

		# Dest. not reachable for proxy arp   :  0
		p17 = re.compile(r'^\s*Dest. +not +reachable +for +proxy +arp +: '
						 r'+(?P<dest_not_reachable_for_proxy_arp>[\d]+)$')

		# Dest. unreachable for enhanced proxy:  0
		# Dest. unreachable for enhanced proxy :  0
		p18 = re.compile(r'^\s*Dest. +unreachable +for +enhanced +proxy( +)?: '
						 r'+(?P<dest_unreachable_for_enhanced_proxy>[\d]+)$')

		# Dest. on L2 port being tracked      :  0
		p19 = re.compile(r'^\s*Dest. +on +L2 +port +being +tracked +: '
						 r'+(?P<destnination_on_l2_port_tracked>[\d]+)$')

		# Invalid Local proxy arp             :  0
		p20 = re.compile(r'^\s*Invalid +Local +proxy +arp +: '
						 r'+(?P<invalid_local_proxy_arp>[\d]+)$')

		# Invalid proxy arp                   :  0
		p21 = re.compile(r'^\s*Invalid +proxy +arp +: +(?P<invalid_proxy_arp>[\d]+)$')

		# VIP is not active                   :  0
		p22 = re.compile(r'^\s*VIP +is +not +active +: +(?P<vip_is_not_active>[\d]+)$')

		# ARP refresh skipped over core and flooded on server :  0
		p23 = re.compile(r'^\s*ARP +refresh +skipped +over +core +and +flooded '
						 r'+on +server +: +(?P<arp_refresh_skipped_over_core_'
						 r'and_flooded>[\d]+)$')

		# Appeared on a wrong interface :  0
		p24 = re.compile(r'^\s*Appeared +on +a +wrong +interface +: '
					 	 r'+(?P<appeared_on_a_wrong_interface>[\d]+)$')

		# Incorrect length                    : 0
		p25 = re.compile(r'^\s*Incorrect +length +: +(?P<incorrect_length>[\d]+)$')

		# Invalid protocol packet                    : 0
		p26 = re.compile(r'^\s*Invalid +protocol +packet +: '
						 r'+(?P<invalid_protocol_packet>[\d]+)$')

		# Invalid Hardware type                  : 0
		p27 = re.compile(r'^\s*Invalid +Hardware +type +: '
						 r'+(?P<invalid_hardwaretype>[\d]+)$')

		# ARP adjacency statistics
		p27_1 = re.compile(r'^\s*ARP adjacency statistics$')

		# Invalid layer 2 address length      : 0
		p30 = re.compile(r'^\s*Invalid +layer +2 +address +length +: '
						 r'+(?P<invalid_layer2_address_length>[\d]+)$')

		# Invalid source IP address           : 28
		p31 = re.compile(r'^\s*Invalid +source +IP +address +: '
						 r'+(?P<invalid_source_ip_address>[\d]+)$')

		# Source IP address is our own        : 0
		p32 = re.compile(r'^\s*Source +IP +address +is +our +own +: '
						 r'+(?P<source_ip_address_is_our_own>[\d]+)$')

		# No mem to create per intf structure : 0
		p32 = re.compile(r'^\s*No +mem +to +create +per +intf +structure +: '
						 r'+(?P<no_mem_to_create_per_intf_structure>[\d]+)$')

		# Invalid layer 3 address length      : 0
		p33 = re.compile(r'^\s*Invalid +layer +3 +address +length +: '
						 r'+(?P<invalid_layer3_address_length>[\d]+)$')

		# Source address mismatch with subnet : 0
		p34 = re.compile(r'^\s*Source +address +mismatch +with +subnet +: '
						 r'+(?P<source_address_mismatch_with_subnet>[\d]+)$')

		# Directed broadcast source           : 0
		p35 = re.compile(r'^\s*Directed +broadcast +source +: '
						 r'+(?P<directed_broadcast_source>[\d]+)$')

		# Invalid destination IP address      : 0
		p36 = re.compile(r'^\s*Invalid +destination +IP +address +: '
						 r'+(?P<invalid_destination_ip_address>[\d]+)$')

		# Non-local destination IP address    : 20421
		p37 = re.compile(r'^\s*Non-local +destination +IP +address +: '
						 r'+(?P<non_local_destination_ip_address>[\d]+)$')

		# Invalid source MAC address          : 0
		p38 = re.compile(r'^\s*Invalid +source +MAC +address +: '
						 r'+(?P<invalid_source_mac_address>[\d]+)$')

		# Source MAC address is our own       : 0
		p39 = re.compile(r'^\s*Source +MAC +address +is +our +own +: '
						 r'+(?P<source_mac_address_is_our_own>[\d]+)$')

		# Received before arp initialization  : 0
		p40 = re.compile(r'^\s*Received +before +arp +initialization +: '
						 r'+(?P<received_before_arp_initialization>[\d]+)$')

		# L2 packet on untrusted L2 port      : 0
		p41 = re.compile(r'^\s*L2 +packet +on +untrusted +L2 +port +: '
						 r'+(?P<l2_packet_on_untrusted_l2_port>[\d]+)$')

		# Packet with VIP on standby FHRP     : 0
		p42 = re.compile(r'^\s*Packet +with +VIP +on +standby +FHRP +: '
						 r'+(?P<packet_with_vip_on_standby_fhrp>[\d]+)$')

		# Requests came for exising entries   : 15
		p43 = re.compile(r'^\s*Requests +came +for +exising +entries +: '
						 r'+(?P<requests_came_for_exising_entries>[\d]+)$')

		# Requests came on a L2 interface     : 0
		# Requests came on a l2 interface     : 0
		p44 = re.compile(r'^\s*Requests +came +on +a +(l|L)2 +interface +: '
						 r'+(?P<requests_came_on_a_l2_interface>[\d]+)$')

		# L2FM query failed for a L2 Address  : 0
		p45 = re.compile(r'^\s*L2FM +query +failed +for +a +L2 +Address +: '
						 r'+(?P<l2fm_query_failed_for_a_l2address>[\d]+)$')

		# Dropping due to tunneling failures  : 0
		p46 = re.compile(r'^\s*Dropping due to tunneling failures +: '
						 r'+(?P<dropping_due_to_tunneling_failures>[\d]+)$')

		# Glean requests recv count : 71
		p47 = re.compile(r'^\s*Glean +requests +recv +count +: '
						 r'+(?P<glean_requests_recv_count>[\d]+)$')

		# ARP refresh requests received from clients: 0
		p48 = re.compile(r'^\s*ARP +refresh +requests +received +from +clients: '
					 	 r'+(?P<arp_refresh_requests_received_from_clients>[\d]+)$')

		# Number of Signals received from L2rib : 0
		p49 = re.compile(r'^\s*Number +of +Signals +received +from +L2rib +: '
						 r'+(?P<number_of_signals_received_from_l2rib>[\d]+)$')

		# Adds 43, Deletes 12, Timeouts 12
		p50 = re.compile(r'^\s*Adds +(?P<adjacency_adds>[\w]+), +Deletes '
						 r'+(?P<adjacency_deletes>[\w]+), +Timeouts '
						 r'+(?P<adjacency_timeouts>[\w]+)$')

		# Failed due to limits: 0
		p51 = re.compile(r'^\s*Failed +due +to +limits: '
						 r'+(?P<failed_due_to_limits>[\d]+)$')

		# Non-active FHRP dest IP address. Learn and drop
		p52 = re.compile(r'^\s*Non-active +FHRP +dest +IP +address. '
						 r'+Learn +and +drop$')

		# Grat arp received on proxy-arp-enabled interface
		p53 = re.compile(r'^\s*Grat +arp +received +on +proxy-arp-enabled '
						 r'+interface$')

		#                                     : 0
		p54 = re.compile(r'^\s*: +(?P<statistic_number>[\d]+)$')

		# 0, Snooped 0, Dropped 181721798, on Server Port 0
		p55 = re.compile(r'(?P<fastpath>[\w]+)\,( +Snooped +(?P<snooped>[\w]+))'
						 r'?\,?( +Dropped +(?P<dropped>[\w]+))\,?( +on +Server '
						 r'+Port +(?P<dropped_server_port>[\w]+))')
		
		# Source IP address is our own        : 1
		p56 = re.compile(r'^Source +IP +address +is +our +own +\: '
						 r'+(?P<source_ip_address_is_our_own>\d+)$')

		for line in out.splitlines():
			line = line.strip()
			if not line: 
				continue

			m = p1.match(line)
			if m:
				ret_dict.setdefault('statistics', {}).setdefault('sent', {})
				direction = 'sent'
				continue

			m = p1_1.match(line)
			if m:
				ret_dict['statistics'].setdefault('received', {})
				direction = 'received'
				continue

			m = p27_1.match(line)
			if m:
				ret_dict['statistics'].setdefault('adjacency', {})
				continue

			m = p2.match(line)
			if m:
				groups = m.groupdict()
				# total, requests, replies, l2_requests, l2_replies
				ret_dict['statistics'][direction].update({k: \
					int(v) for k, v in groups.items()})
				continue

			m = p3.match(line)
			if m:
				groups = m.groupdict()
				# gratuitous, tunneled, dropped
				ret_dict['statistics']['sent'].update({k: \
					int(v) for k, v in groups.items()})
				continue

			m = p4.match(line)
			if m:
				groups = m.groupdict()
				# proxy_arp, local_proxy_arp, enhanced_proxy_arp, anycast_proxy_arp
				# l2_port_track_proxy_arp, tunneled, fastpath, snooped, dropped
				# dropped_server_port
				ret_dict['statistics']['received'].update({k: \
					int(v) for k, v in groups.items() if v})
				continue

			m = p5.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['sent'].setdefault('drops_details', {})
				ret_dict['statistics']['sent']['drops_details']\
					['mbuf_operation_failed'] = int(
						groups['mbuf_operation_failed'])
				continue

			m = p6.match(line)
			if m and direction=='sent':
				groups = m.groupdict()
				ret_dict['statistics']['sent']['drops_details']\
					['context_not_created'] = int(groups['context_not_created'])
				continue
			elif m:
				groups = m.groupdict()
				ret_dict['statistics']['received']['drops_details']\
					['context_not_created'] = int(groups['context_not_created'])
				continue

			m = p7.match(line)
			if m and direction=='sent':
				groups = m.groupdict()
				ret_dict['statistics']['sent']['drops_details']\
					['invalid_context'] = int(groups['invalid_context'])
				continue
			elif m:
				groups = m.groupdict()
				ret_dict['statistics']['received']['drops_details']\
					['invalid_context'] = int(groups['invalid_context'])
				continue

			m = p8.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['sent']['drops_details']\
					['invalid_ifindex'] = int(groups['invalid_ifindex'])
				continue

			m = p9.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['sent']['drops_details']\
					['invalid_src_ip'] = int(groups['invalid_src_ip'])
				continue

			m = p10.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['sent']['drops_details']\
					['invalid_dest_ip'] = int(groups['invalid_dest_ip'])
				continue

			m = p11.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['sent']['drops_details']\
					['destnination_is_our_own_ip'] = int(
						groups['destnination_is_our_own_ip'])
				continue

			m = p12.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['sent']['drops_details']\
					['unattached_ip'] = int(groups['unattached_ip'])
				continue

			m = p13.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['sent']['drops_details']\
					['adjacency_couldnt_be_added'] = int(
						groups['adjacency_couldnt_be_added'])
				continue

			m = p14.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['sent']['drops_details']\
					['null_source_ip'] = int(groups['null_source_ip'])
				continue

			m = p15.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['sent']['drops_details']\
					['null_source_mac'] = int(groups['null_source_mac'])
				continue

			m = p16.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['sent']['drops_details']\
					['client_enqueue_failed'] = int(
						groups['client_enqueue_failed'])
				continue

			m = p17.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['sent']['drops_details']\
					['dest_not_reachable_for_proxy_arp'] = int(
						groups['dest_not_reachable_for_proxy_arp'])
				continue

			m = p18.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['sent']['drops_details']\
					['dest_unreachable_for_enhanced_proxy'] = int(
						groups['dest_unreachable_for_enhanced_proxy'])
				continue

			m = p19.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['sent']['drops_details']\
					['destnination_on_l2_port_tracked'] = int(
						groups['destnination_on_l2_port_tracked'])
				continue

			m = p20.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['sent']['drops_details']\
					['invalid_local_proxy_arp'] = int(
						groups['invalid_local_proxy_arp'])
				continue

			m = p21.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['sent']['drops_details']\
					['invalid_proxy_arp'] = int(groups['invalid_proxy_arp'])
				continue

			m = p22.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['sent']['drops_details']\
					['vip_is_not_active'] = int(groups['vip_is_not_active'])
				continue

			m = p23.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['sent']['drops_details']\
					['arp_refresh_skipped_over_core_and_flooded'] = int(
						groups['arp_refresh_skipped_over_core_and_flooded'])
				continue

			m = p24.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['received'].setdefault('drops_details', {})
				ret_dict['statistics']['received']['drops_details']\
					['appeared_on_a_wrong_interface'] = int(
						groups['appeared_on_a_wrong_interface'])
				continue

			m = p25.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['received']['drops_details']\
					['incorrect_length'] = int(groups['incorrect_length'])
				continue

			m = p26.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['received']['drops_details']\
					['invalid_protocol_packet'] = int(
					groups['invalid_protocol_packet'])
				continue

			m = p27.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['received']['drops_details']\
					['invalid_hardwaretype'] = int(
						groups['invalid_hardwaretype'])
				continue

			m = p30.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['received']['drops_details']\
					['invalid_layer2_address_length'] = \
					int(groups['invalid_layer2_address_length'])
				continue

			m = p31.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['received']['drops_details']\
					['invalid_source_ip_address'] = int(
					groups['invalid_source_ip_address'])
				continue

			m = p32.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['received']['drops_details']\
					['no_mem_to_create_per_intf_structure'] = \
					int(groups['no_mem_to_create_per_intf_structure'])
				continue

			m = p33.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['received']['drops_details']\
					['invalid_layer3_address_length'] = \
					int(groups['invalid_layer3_address_length'])
				continue

			m = p34.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['received']['drops_details']\
					['source_address_mismatch_with_subnet'] = \
					int(groups['source_address_mismatch_with_subnet'])
				continue

			m = p35.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['received']['drops_details']\
					['directed_broadcast_source'] = int(
					groups['directed_broadcast_source'])
				continue

			m = p36.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['received']['drops_details']\
					['invalid_destination_ip_address'] = \
					int(groups['invalid_destination_ip_address'])
				continue

			m = p37.match(line)
			if m:
				groups = m.groupdict()

				ret_dict['statistics']['received']['drops_details']\
					['non_local_destination_ip_address'] = \
					int(groups['non_local_destination_ip_address'])
				continue

			m = p38.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['received']['drops_details']\
					['invalid_source_mac_address'] = int(
					groups['invalid_source_mac_address'])
				continue

			m = p39.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['received']['drops_details']\
					['source_mac_address_is_our_own'] = int(
					groups['source_mac_address_is_our_own'])
				continue

			m = p40.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['received']['drops_details']\
					['received_before_arp_initialization'] = \
					int(groups['received_before_arp_initialization'])
				continue

			m = p41.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['received']['drops_details']\
					['l2_packet_on_untrusted_l2_port'] = \
					int(groups['l2_packet_on_untrusted_l2_port'])
				continue

			m = p42.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['received']['drops_details']\
					['packet_with_vip_on_standby_fhrp'] = \
					int(groups['packet_with_vip_on_standby_fhrp'])
				continue

			m = p43.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['received']['drops_details']\
					['requests_came_for_exising_entries'] = \
					int(groups['requests_came_for_exising_entries'])
				continue

			m = p44.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['received']['drops_details']\
					['requests_came_on_a_l2_interface'] = \
					int(groups['requests_came_on_a_l2_interface'])
				continue

			m = p45.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['received']['drops_details']\
					['l2fm_query_failed_for_a_l2address'] \
					= int(groups['l2fm_query_failed_for_a_l2address'])
				continue

			m = p46.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['received']['drops_details']\
					['dropping_due_to_tunneling_failures'] = \
					int(groups['dropping_due_to_tunneling_failures'])
				continue

			m = p47.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['received']['drops_details']\
					['glean_requests_recv_count'] = int(
					groups['glean_requests_recv_count'])
				continue

			m = p48.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['received']['drops_details']\
					['arp_refresh_requests_received_from_clients'] = int(
						groups['arp_refresh_requests_received_from_clients'])
				continue

			m = p49.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['received']['drops_details']\
					['number_of_signals_received_from_l2rib'] = int(
						groups['number_of_signals_received_from_l2rib'])
				continue

			m = p50.match(line)
			if m:
				groups = m.groupdict()
				# adjacency_adds, adjacency_deletes, adjacency_timeouts
				ret_dict['statistics']['adjacency'].update({k: int(v) \
					for k, v in groups.items()})
				continue

			m = p51.match(line)
			if m:
				groups = m.groupdict()
				ret_dict['statistics']['adjacency']['failed_due_to_limits'] = \
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
				ret_dict['statistics']['received']['drops_details'][key] = \
					int(m.groupdict()['statistic_number'])
				key = ''
				continue
			
			m55 = p55.match(line)
			if m55:
				group = m55.groupdict()
				received_dict = ret_dict['statistics']['received']
				received_dict.update({k:
                                    int(v) for k, v in group.items() if v})
				
				continue
			
			m56 = p56.match(line)
			if m56:
				drop_dict = ret_dict['statistics']['received']['drops_details']
				drop_dict.update({'source_ip_address_is_our_own': int(
					m56.groupdict()['source_ip_address_is_our_own'])})

				continue

		return ret_dict
