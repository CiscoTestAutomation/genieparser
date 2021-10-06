'''show_bfd.py
IOSXE parser for the following show command
	* show bfd neighbors details
	* show bfd neighbors client {client} details
'''

# Python
import re
import pprint

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
											Optional,\
											Any

# parser utils
from genie.libs.parser.utils.common import Common

# ==============================================================
# Parser for the following show commands:
# 	* 'show bfd neighbors details'
#	* 'show bfd neighbors client {client} details'
#   * 'show bfd neighbors interface {interface} details'
# ==============================================================
class ShowBfdNeighborsDetailsSchema(MetaParser):
	"""
	Schema for the following show commands:
		* show bfd neighbors details
		* show bfd neighbors client {client} details
        * show bfd neighbors interface {interface} details
	"""

	schema = {
		'our_address': {
			Any(): {
				'neighbor_address': {
					Any(): {
						Optional('ld_rd'): str,
						Optional('ld'): int,
						Optional('rd'): int,
						Optional('rh_rs'): str,
						Optional('holdown_timer'): int,
						Optional('holdown_timer_multiplier'): int,
						Optional('state'): str,
						Optional('interface'): str,
						Optional('session'): {
							'state': str,
							'echo_function': bool,
							Optional('echo_interval_ms'): int
						},
						Optional('session_host'): str,
						Optional('handle'): int,
						Optional('local_diag'): int,
						Optional('demand_mode'): int,
						Optional('poll_bit'): int,
						Optional('min_tx_int'): int,
						Optional('min_rx_int'): int,
						Optional('multiplier'): int,
						Optional('received_min_rx_int'): int,
						Optional('received_multiplier'): int,
						Optional('holddown'): int,
						Optional('holddown_hits'): int,
						Optional('hello'): int,
						Optional('hello_hits'): int,
						Optional('rx'): {
							Optional('count'): int,
							Optional('min_int_ms'): int,
							Optional('max_int_ms'): int,
							Optional('avg_int_ms'): int,
							Optional('last_ms_ago'): int
						},
						Optional('tx'): {
							Optional('count'): int,
							Optional('min_int_ms'): int,
							Optional('max_int_ms'): int,
							Optional('avg_int_ms'): int,
							Optional('last_ms_ago'): int
						},
						Optional('echo_tx'): {
							Optional('count'): int,
							Optional('min_int_ms'): int,
							Optional('max_int_ms'): int,
							Optional('avg_int_ms'): int,
							Optional('last_ms_ago'): int
						},
						Optional('echo_rx'): {
							Optional('count'): int,
							Optional('min_int_ms'): int,
							Optional('max_int_ms'): int,
							Optional('avg_int_ms'): int,
							Optional('last_ms_ago'): int
						},
						Optional('elapsed_time_watermarks'): str,
						Optional('elapsed_time_watermarks_last'): int,
						Optional('registered_protocols'): list,
						Optional('up_time'): str,
						Optional('last_packet'): {
							Optional('version'): int,
							Optional('diagnostic'): int,
							Optional('state_bit'): str,
							Optional('i_hear_you_bit'): str,
							Optional('demand_bit'): int,
							Optional('poll_bit'): int,
							Optional('final_bit'): int,
							Optional('c_bit'): int,
							Optional('multiplier'): int,
							Optional('length'): int,
							Optional('my_discr'): int,
							Optional('your_discr'): int,
							Optional('min_tx_int'): int,
							Optional('min_rx_int'): int,
							Optional('min_echo_int'): int			
						},
						Optional('cleanup_timer_hits'): int,
						Optional('sso_cleanup_timer_called'): int,
						Optional('sso_cleanup_action_taken'): int,
						Optional('pseudo_preemtive_process'): {
							Optional('count'): int,
							Optional('min'): int,
							Optional('max'): int,
							Optional('avg'): int,
							Optional('last_ms_ago'): int,
						},
						Optional('ipc_tx_failure_count'): int,
						Optional('ipc_rx_failure_count'): int,
						Optional('total_adjs_found'): int,
						Optional('holddown_negotiated'): int,
						Optional('holddown_adjusted'): int,
					}
				}
			}
		}
	}	


class ShowBfdNeighborsDetails(ShowBfdNeighborsDetailsSchema):
	""" Parser for the following commands:
			* 'show bfd neighbors details'
			* 'show bfd neighbors client {client} details'
			* 'show bfd neighbors interface {interface} details'
			* 'show bfd neighbors ipv4 {ipv4_address} details',
			* 'show bfd neighbors ipv6 {ipv6_address} details'
	"""

	cli_command = ['show bfd neighbors details',
				   'show bfd neighbors client {client} details',
				   'show bfd neighbors interface {interface} details',
				   'show bfd neighbors ipv4 {ipv4_address} details',
				   'show bfd neighbors ipv6 {ipv6_address} details']

	def cli(self, client='', interface=None, ipv4_address=None, ipv6_address=None, output= None):
		if output is None:
			# execute command to get output
			if client:
				out = self.device.execute(self.cli_command[1].format(client=client))
			elif interface:
				out = self.device.execute(self.cli_command[2].format(interface=interface))
			elif ipv4_address:
				out = self.device.execute(self.cli_command[3].format(
					ipv4_address=ipv4_address))
			elif ipv6_address:
				out = self.device.execute(self.cli_command[4].format(
					ipv6_address=ipv6_address))
			else:
				out = self.device.execute(self.cli_command[0])
		else:
			out = output

		# initial variables
		ret_dict = {}
		neighbors_found = False

		# 172.16.10.1	172.16.10.2		1/2		1		532 (3 )		Up 		Gig0/0/0
		# 2001:DB8:B947:0:251:57EF:FF8D:E8CC      2001:DB8:B947:0:251:57EF:FF8D:E8CB          1/17         Up        Up        Gi2
		p1 = re.compile(r'^(?P<our_address>[\w\.\:]+)\s+(?P<our_neighbor>[\w\.\:]+' \
			')\s+(?P<ld_rd>\d+\/\d+)\s+(?P<rh_rs>\S+)\s+(?P<holdown_timer>\d+)' \
			'\s+\((?P<holdown_timer_multiplier>\d+)\s+\)\s+(?P<state>\w+)' \
			'\s+(?P<interface>[\w\W]+)$')

		# 172.16.1.1	172.16.1.3
		# # 2001:DB8:B947:0:251:57EF:FF8D:E8CC 
		p2 = re.compile(r'^(?P<our_address>[\w\.\:]+) +(?P<our_neighbor>'\
			'[\w\.\:]+)$')

		# 		5/2		1(RH)	150 (3)		Up 		Gig0/0/1
		p3 = re.compile(r'^(?P<ld_rd>\d+\/\d+)\s+(?P<rh_rs>\S+)\s+' \
			'(?P<holdown_timer>\d+)\s+\((?P<holdown_timer_multiplier>\d+)\s+\)' \
			'\s+(?P<state>\w+)\s+(?P<interface>[\w\W]+)')

		# 10.169.197.93 					4097/4097		Up 		Up 	Gi0/0/0
		# 2001:DB8:B947:0:251:57EF:FF8D:E8CC                1/17         Up        Up        Gi2
		p4 = re.compile(r'^(?P<our_neighbor>[\w\.\:]+)\s+(?P<ld_rd>\d+'\
			'\/\d+)\s+(?P<rh_rs>\S+)\s+(?P<state>\w+)\s+(?P<interface>'\
			'[\w\W]+)$')

		# 5/2
		p4_1 = re.compile(r'^(?P<ld>\d+)\/(?P<rd>\d+)$')

		# OurAddr: 10.186.213.12
		p5 = re.compile(r'^OurAddr:\s+(?P<our_address>[\w\.\:]+)$')

		# Session state is UP and using echo function with 500 ms interval.
		p6 = re.compile(r'^\s*Session +state +is +(?P<state>\S+) +and +using'\
			r' +(?P<echo_function>\S+) +function +with +(?P<interval_in_ms>\d+)'\
			r' +ms +interval\.$')
		
		# Session state is UP and not using echo function.
		p7 = re.compile(r'^\s*Session +state +is +(?P<state>\S+) +and +not '\
			'+using +echo +function\.$')

		# Session Host: Software
		p8 = re.compile(r'^\s*Session\s+Host:\s+(?P<session_host>\S+)$')

		# Handle: 1
		p10 = re.compile(r'^\s*Handle: +(?P<handle>\d+)$')

		# Local Diag: 0, Demand mode: 0, Poll bit: 0
		p11 = re.compile(r'^\s*Local +Diag: +(?P<local_diag>\d+), +Demand +'\
			'mode: +(?P<demand_mode>\d+), +Poll +bit: +(?P<poll_bit>\d+)$')

		# MinTxInt: 50000, MinRxInt: 50000, Multiplier: 3 Received MinRxInt: 50000, Received Multiplier: 3 Holddown (hits): 150(0), Hello (hits): 50(2223) Rx Count: 2212, Rx Count: 2212, Rx Interval (ms) 
		# min/max/avg: 8/68/49 last: 0 ms ago Tx Count: 2222, Tx Interval (ms) min/max/avg: 40/60/49 last: 20 ms ago Elapsed time watermarks: 0 0 (last: 0) Registered protocols: CEF Stub
		p12 = re.compile(r'^\s*MinTxInt:\s+(?P<min_tx_interface>\d+),\s+'\
			'MinRxInt:\s+(?P<min_rx_interface>\d+),\s+Multiplier:\s+'\
			'(?P<multiplier>\d+)\s*Received\s+MinRxInt:\s+'\
			'(?P<received_min_rx_interface>\d+),\s+Received\s+Multiplier:\s'\
			'+(?P<received_multiplier>\d+)\s+Hold(d)?own\s+\(hits\):\s+'\
			'(?P<holddown>\d+)\((?P<holddown_hits>\d+)\),\s+Hello\s+\(hits\)'\
			':\s+(?P<hello>\d+)\((?P<hello_hits>\d+)\)\s+Rx +Count:\s+'\
			'(?P<rx_count>\d+),\s+Rx\s+Interval\s+\(ms\)\s+min\/max\/avg:\s+'\
			'(?P<rx_min_interval_in_ms>\d+)\/(?P<rx_max_interval_in_ms>\d+)'\
			'\/(?P<rx_avg_interval_in_ms>\d+) +last:\s+'\
			'(?P<rx_last_interval_in_ms>\d+) +ms +ago\s*Tx\s+Count: +'\
			'(?P<tx_count>\d+),\s+Tx\s+Interval\s+\(ms\)\s+min\/max\/avg:'\
			'\s+(?P<tx_min_interval_in_ms>\d+)\/(?P<tx_max_interval_in_ms>'\
			'\d+)\/(?P<tx_avg_interval_in_ms>\d+)\s+last:\s+'\
			'(?P<tx_last_interval_in_ms>\d+)\s+ms\s+ago\s*Elapsed\s+time\s+'\
			'watermarks:\s+(?P<elapsed_time_watermarks>\d+\s+\d+) +\('\
			'last:\s+(?P<elapsed_time_watermarks_last>\d+)\)\s*'\
			'Registered\s+protocols:\s+(?P<registered_protocols>[\w\W]+)$')
		
		# MinTxInt: 100000, MinRxInt: 100000, Multiplier: 6
		p13 = re.compile(r'^\s*MinTxInt: +(?P<min_tx_interface>\d+), +MinRxInt' \
			': +(?P<min_rx_interface>\d+), +Multiplier: +(?P<multiplier>\d+)$')

		# Received MinRxInt: 100000, Received Multiplier: 6
		p14 = re.compile(r'^\s*Received +MinRxInt:\s+'\
			r'(?P<received_min_rx_interface>\d+),\s+Received\s+Multiplier:'\
			r'\s+(?P<received_multiplier>\d+)$')

		# Holdown (hits): 1000(0), Hello (hits): 200(5995)
		p15 = re.compile(r'^\s*Hold(d)?own +\(hits\): +' \
			r'(?P<holddown>\d+)\((?P<holddown_hits>\d+)\), +Hello +\(hits\): +' \
			r'(?P<hello>\d+)\((?P<hello_hits>\d+)\)$')

		# Rx Count: 1940, Rx Interval (ms) min/max/avg: 1/1003/879 last: 182 ms ago
		p16 = re.compile(r'^\s*Rx +Count: +(?P<count>\d+), +Rx +' \
			r'Interval +\(ms\) +min\/max\/avg: +(?P<min_int_ms>\d+)' \
			r'\/(?P<max_int_ms>\d+)\/(?P<avg_int_ms>\d+) +' \
			r'last: +(?P<last_ms_ago>\d+) +ms +ago$')

		# Echo Rx Count: 20777, Echo Rx Interval (ms) min/max/avg: 1505/2003/1751 last: 721 ms ago
		p16_1 = re.compile(r'^Echo Rx Count: +(?P<count>\d+), '
						   r'+Echo Rx Interval \(ms\) min\/max\/avg: '
						   r'+(?P<min_int_ms>\d+)\/(?P<max_int_ms>\d+)\/(?P<avg_int_ms>\d+)'
						   r' +last: +(?P<last_ms_ago>\d+) ms ago$')

		# Rx Count: 5052
		p17 = re.compile(r'^\s*Rx +Count: +(?P<count>\d+)$')

		# Tx Count: 1940, Tx Interval (ms) min/max/avg: 1/1003/879 last: 742 ms ago
		p18 = re.compile(r'^\s*Tx +Count: +(?P<count>\d+), +Tx +Interval +' \
			'\(ms\) +min\/max\/avg: +(?P<min_int_ms>\d+)\/(?P<max_int_ms>\d+)'\
			'\/(?P<avg_int_ms>\d+) +last: +(?P<last_ms_ago>\d+) +ms +ago$')

		# Echo Tx Count: 20777, Echo Tx Interval (ms) min/max/avg: 1506/2003/1751 last: 722 ms ago
		p18_1 = re.compile(r'^Echo Tx Count: +(?P<count>\d+), '
						   r'+Echo Tx Interval \(ms\) min\/max\/avg: '
						   r'+(?P<min_int_ms>\d+)\/(?P<max_int_ms>\d+)\/(?P<avg_int_ms>\d+) '
						   r'+last: +(?P<last_ms_ago>\d+) ms ago$')

		# Tx Count: 7490
		p19 = re.compile(r'^\s*Tx +Count: +(?P<count>\d+)$')
		
		# Elapsed time watermarks: 0 0 (last: 0)
		p20 = re.compile(r'^\s*Elapsed +time +watermarks: +' \
			'(?P<elapsed_time_watermarks>\d+ +\d+) +\(last: +' \
			'(?P<elapsed_time_watermarks_last>\d+)\)$')

		# Registered protocols: OSPF CEF
		p21 = re.compile(r'^\s*Registered +protocols: +' \
			'(?P<registered_protocols>[\w\W]+)$')

		# Uptime: 00:28:03
		p22 = re.compile(r'^\s*Uptime: +(?P<up_time>\S+)$')
		
		# Last packet: Version: 1		- Diagnostic: 0
		p23 = re.compile(r'^\s*Last\s+packet:\s+Version:\s+(?P<version>\d+)'\
			'\s+\-\s+Diagnostic:\s+(?P<diagnostic>\d+)$')

		# Last packet: Version: 0
		p24 = re.compile(r'\s*Last\s+packet:\sVersion:\s+(?P<version>\d+)$')
		
		# - Diagnostic: 0
		p25 = re.compile(r'\s*\-\s+Diagnostic:\s+(?P<diagnostic>\d+)$')
		
		# State bit: Up				- Demand bit: 0
		p26 = re.compile(r'^\s*State +bit: +(?P<state_bit>\S+)\s+\-\s+' \
			'Demand +bit:\s+(?P<demand_bit>\d+)$')

		p27 = re.compile(r'^\s*I +Hear +You +bit: +(?P<i_hear_you_bit>\S+)'\
			'\s+\-\s+Demand +bit:\s+(?P<demand_bit>\d+)$')
		# Poll bit: 0 				- Final bit: 0
		p28 = re.compile(r'^\s*Poll\s+bit:\s+(?P<poll_bit>\d+)\s+\-\s+'\
			'Final\s+bit:\s+(?P<final_bit>\d+)$')
		
		# C bit: 0
		p29 = re.compile(r'^\s*C +bit: +(?P<c_bit>\d+)$')

		# Multiplier: 6			- Length: 24
		p30 = re.compile(r'^\s*Multiplier: +(?P<multiplier>\d+)\s+\-\s+' \
			'Length:\s+(?P<length>\d+)$')
		
		# My Discr.: 4097		- Your Discr.: 4097
		p31 = re.compile(r'^\s*My +Discr\.: +(?P<my_discr>\d+)\s+\-\s+' \
			'Your +Discr\.:\s+(?P<your_discr>\d+)')
		
		# Min tx interval: 1000000	- Min rx interval: 1000000
		p32 = re.compile(r'^\s*Min +tx +interval: +(?P<min_tx_interval>\d+)'\
			'\s+\-\s+Min +rx +interval:\s+(?P<min_rx_interval>\d+)$')

		# Min Echo interval: 3000000
		p33 = re.compile(r'^\s*Min\s+Echo\s+interval:\s+' \
			'(?P<min_echo_interval>\d+)$')
		
		# Cleanup timer hits: 0
		p34 = re.compile(r'^\s*Cleanup +timer +hits: +'\
			'(?P<cleanup_timer_hits>\d+)$')

		# SSO Cleanup Timer called: 0
		p35 = re.compile(r'^\s*SSO +Cleanup +Timer +called: +'\
			'(?P<sso_cleanup_timer_called>\d+)$')

		# SSO Cleanup Action Taken: 0
		p36 = re.compile(r'^\s*SSO +Cleanup +Action +Taken: +'\
			'(?P<sso_cleanup_action_taken>\d+)$')

		# Pseudo pre-emptive process count: 239103 min/max/avg: 8/16/8 last: 0 ms ago
		p37 = re.compile(r'^\s*Pseudo +pre-emptive +process +count: +'\
			'(?P<count>\d+) +min\/max\/avg: +(?P<min>\d+)\/(?P<max>\d+)'\
			'\/(?P<avg>\d+) +last: +(?P<last_ms_ago>\d+) +ms +ago$')

		# IPC Tx Failure Count: 0
		p38 = re.compile(r'^\s*IPC +Tx +Failure +Count: +'\
			'(?P<ipc_tx_failure_count>\d+)$')

		# IPC Rx Failure Count: 0
		p39 = re.compile(r'^\s*IPC +Rx +Failure +Count: +'\
			'(?P<ipc_rx_failure_count>\d+)$')

		# Total Adjs Found: 1
		p40 = re.compile(r'^\s*Total +Adjs +Found: +'\
			'(?P<total_adjs_found>\d+)$')

		# Holddown - negotiated: 510000         adjusted: 0
		p41 = re.compile(r'^\s*Hol(d)?down +\- +negotiated: +'\
			'(?P<holddown_negotiated>\d+) +adjusted: +'\
			'(?P<holddown_adjusted>\d+)$')
		
		# IPv4 Sessions
		# IPv6 Sessions
		p42 = re.compile(r'^IPv(4|6) +Sessions$')

		for line in out.splitlines():
			line = line.strip()
			
			# IPv4 Sessions
			# IPv6 Sessions
			m = p42.match(line)
			if m:
				continue

			# 172.16.10.1	172.16.10.2		1/2		1		532 (3 )		Up 		Gig0/0/0
			m = p1.match(line)
			if m:
				group = m.groupdict()
				our_address = ret_dict.setdefault('our_address', {}). \
					setdefault(group['our_address'], {})
				our_neighbor = our_address.setdefault('neighbor_address', \
					{}).setdefault(group['our_neighbor'], {})
				our_neighbor.update({'ld_rd' : group['ld_rd']})
				our_neighbor.update({'rh_rs' : group['rh_rs']})
				our_neighbor.update({'holdown_timer' : \
					int(group['holdown_timer'])})
				our_neighbor.update({'holdown_timer_multiplier' : \
					int(group['holdown_timer_multiplier'])})
				our_neighbor.update({'state' : group['state']})
				our_neighbor.update({'interface' : \
				 Common.convert_intf_name(group['interface'])})
				continue

			# 		5/2		1(RH)	150 (3)		Up 		Gig0/0/1
			m = p3.match(line)
			if m:
				group = m.groupdict()
				our_neighbor.update({'ld_rd' : group['ld_rd']})
				our_neighbor.update({'rh_rs' : group['rh_rs']})
				our_neighbor.update({'holdown_timer' : \
					int(group['holdown_timer'])})
				our_neighbor.update({'holdown_timer_multiplier' : \
					int(group['holdown_timer_multiplier'])})
				our_neighbor.update({'state' : group['state']})
				our_neighbor.update({'interface' : \
					Common.convert_intf_name(group['interface'])})

				# gets separated ld and rd values
				s = p4_1.match(group['ld_rd'])
				our_neighbor.update({'ld': int(s.groupdict()['ld'])})
				our_neighbor.update({'rd': int(s.groupdict()['rd'])})
				continue

			# 10.169.197.93 					4097/4097		Up 		Up 	Gi0/0/0
			m = p4.match(line)
			if m:
				group = m.groupdict()
				neighbor = {}
				our_neighbor = neighbor.setdefault(group['our_neighbor'], {})
				our_neighbor.update({'ld_rd': group['ld_rd']})
				our_neighbor.update({'rh_rs': group['rh_rs']})
				our_neighbor.update({'state': group['state']})
				our_neighbor.update({'interface': Common.convert_intf_name(group['interface'])})

				# gets separated ld and rd values
				s = p4_1.match(group['ld_rd'])
				our_neighbor.update({'ld': int(s.groupdict()['ld'])})
				our_neighbor.update({'rd': int(s.groupdict()['rd'])})
				continue

			# OurAddr: 10.186.213.12
			m = p5.match(line)
			if m:
				group = m.groupdict()
				our_address = ret_dict.setdefault('our_address', {}). \
					setdefault(group['our_address'], {})
				our_address.update({'neighbor_address' : neighbor})
				continue
			
			# Session state is UP and using echo function with 500 ms interval.
			m = p6.match(line)
			if m:
				group = m.groupdict()
				session = our_neighbor.setdefault('session', {})
				session.update({'state' : group['state']})
				session.update({'echo_function' : True})
				session.update({'echo_interval_ms' : 
					int(group['interval_in_ms'])})
				continue

			# Session state is UP and not using echo function.
			m = p7.match(line)
			if m:
				group = m.groupdict()
				session = our_neighbor.setdefault('session', {})
				session.update({'state' : group['state']})
				session.update({'echo_function' : False})

			# Session Host: Software
			m = p8.match(line)
			if m:
				group = m.groupdict()
				our_neighbor.update({'session_host' : group['session_host']})
				continue

			# Handle: 1
			m = p10.match(line)
			if m:
				group = m.groupdict()
				our_neighbor.update({'handle' : int(group['handle'])})
				continue

			# Local Diag: 0, Demand mode: 0, Poll bit: 0
			m = p11.match(line)
			if m:
				group = m.groupdict()
				our_neighbor.update({k: int(v) for k, v in group.items()})
				continue

			# MinTxInt: 50000, MinRxInt: 50000, Multiplier: 3 Received MinRxInt: 50000, Received Multiplier: 3 Holddown (hits): 150(0), Hello (hits): 50(2223) Rx Count: 2212, Rx Count: 2212, Rx Interval (ms) 
			# min/max/avg: 8/68/49 last: 0 ms ago Tx Count: 2222, Tx Interval (ms) min/max/avg: 40/60/49 last: 20 ms ago Elapsed time watermarks: 0 0 (last: 0) Registered protocols: CEF Stub
			m = p12.match(line)
			if m:
				group = m.groupdict()
				our_neighbor.update({'min_tx_int' : \
					int(group['min_tx_interface'])})
				our_neighbor.update({'min_rx_int' : \
					int(group['min_rx_interface'])})
				our_neighbor.update({'multiplier' : \
					int(group['multiplier'])}) 
				our_neighbor.update({'received_min_rx_int' : \
					int(group['received_min_rx_interface'])})
				our_neighbor.update({'received_multiplier' : \
					int(group['received_multiplier'])})
				our_neighbor.update({'holddown' : \
					int(group['holddown'])})
				our_neighbor.update({'holddown_hits' : \
					int(group['holddown_hits'])})
				our_neighbor.update({'hello' : int(group['hello'])})
				our_neighbor.update({'hello_hits' : int(group['hello_hits'])})
				rx = our_neighbor.setdefault('rx', {})
				rx.update({'count' : int(group['rx_count'])})
				rx.update({'min_int_ms' : int(group['rx_min_interval_in_ms'])})
				rx.update({'max_int_ms' : int(group['rx_max_interval_in_ms'])})
				rx.update({'avg_int_ms' : int(group['rx_avg_interval_in_ms'])})
				rx.update({'last_ms_ago' : \
					int(group['rx_last_interval_in_ms'])})
				tx = our_neighbor.setdefault('tx', {})
				tx.update({'count' : int(group['tx_count'])})
				tx.update({'min_int_ms' : int(group['tx_min_interval_in_ms'])})
				tx.update({'max_int_ms' : int(group['tx_max_interval_in_ms'])})
				tx.update({'avg_int_ms' : int(group['tx_avg_interval_in_ms'])})
				tx.update({'last_ms_ago' : \
					int(group['tx_last_interval_in_ms'])})
				our_neighbor.update({'elapsed_time_watermarks' : \
					group['elapsed_time_watermarks']})
				our_neighbor.update({'elapsed_time_watermarks_last' : \
					int(group['elapsed_time_watermarks_last'])})
				our_neighbor.update({'registered_protocols' : \
					list(group['registered_protocols'].strip().split(' '))})
				continue

			# MinTxInt: 100000, MinRxInt: 100000, Multiplier: 6
			m = p13.match(line)
			if m:
				group = m.groupdict()
				our_neighbor.update({'min_tx_int' : \
					int(group['min_tx_interface'])}) 
				our_neighbor.update({'min_rx_int' : \
					int(group['min_rx_interface'])}) 
				our_neighbor.update({'multiplier' : \
					int(group['multiplier'])})
				continue

			# Received MinRxInt: 100000, Received Multiplier: 6
			m = p14.match(line)
			if m:
				group = m.groupdict()
				our_neighbor.update({'received_min_rx_int' : \
					int(group['received_min_rx_interface'])})
				our_neighbor.update({'received_multiplier' : \
					int(group['received_multiplier'])})
				continue

			# Holddown (hits): 0(0), Hello (hits): 1000(1939)
			m = p15.match(line)
			if m:
				group = m.groupdict()
				our_neighbor.update({k: int(v) for k, v in group.items()})
				continue

			# Rx Count: 1940, Rx Interval (ms) min/max/avg: 1/1003/879 last: 182 ms ago
			m = p16.match(line)
			if m:
				group = m.groupdict()
				rx = our_neighbor.setdefault('rx', {})
				rx.update({k: int(v) for k, v in group.items()})
				continue

			# Echo Rx Count: 20777, Echo Rx Interval (ms) min/max/avg: 1505/2003/1751 last: 721 ms ago
			m = p16_1.match(line)
			if m:
				group = m.groupdict()
				echo_rx = our_neighbor.setdefault('echo_rx', {})
				echo_rx.update({k: int(v) for k, v in group.items()})
				continue

			# Rx Count: 5052
			m = p17.match(line)
			if m:
				group = m.groupdict()
				rx = our_neighbor.setdefault('rx', {})
				rx.update({k: int(v) for k, v in group.items()})
				continue

			# Tx Count: 1940, Tx Interval (ms) min/max/avg: 1/1003/879 last: 742 ms ago
			m = p18.match(line)
			if m:
				group = m.groupdict()
				tx = our_neighbor.setdefault('tx', {})
				tx.update({k: int(v) for k, v in group.items()})
				continue

			# Echo Tx Count: 20777, Echo Tx Interval (ms) min/max/avg: 1506/2003/1751 last: 722 ms ago
			m = p18_1.match(line)
			if m:
				group = m.groupdict()
				echo_tx = our_neighbor.setdefault('echo_tx', {})
				echo_tx.update({k: int(v) for k, v in group.items()})
				continue

			# Tx Count: 7490
			m = p19.match(line)
			if m:
				group = m.groupdict()
				tx = our_neighbor.setdefault('tx', {})
				tx.update({k: int(v) for k, v in group.items()})
				continue

			# Elapsed time watermarks: 0 0 (last: 0)
			m = p20.match(line)
			if m:
				group = m.groupdict()
				our_neighbor.update({'elapsed_time_watermarks' : 
					group['elapsed_time_watermarks']})
				our_neighbor.update({'elapsed_time_watermarks_last' : 
					int(group['elapsed_time_watermarks_last'])})
				continue

			# Registered protocols: OSPF CEF
			m = p21.match(line)
			if m:
				group = m.groupdict()
				our_neighbor.update({'registered_protocols' : 
					list(group['registered_protocols'].strip().split(' '))})
				continue

			# Uptime: 00:28:03
			m = p22.match(line)
			if m:
				group = m.groupdict()
				our_neighbor.update({'up_time' : group['up_time']})
				continue

			# Last packet: Version: 1		- Diagnostic: 0
			m = p23.match(line)
			if m:
				group = m.groupdict()
				last_packet = our_neighbor.setdefault('last_packet', {})
				last_packet.update({'version' : int(group['version'])})
				last_packet.update({'diagnostic' : int(group['diagnostic'])})
				continue

			# Last packet: Version: 1
			m = p24.match(line)
			if m:
				group = m.groupdict()
				last_packet = our_neighbor.setdefault('last_packet', {})
				last_packet.update({'version' : int(group['version'])})
				continue

			# 					- Diagnostic: 0
			m = p25.match(line)
			if m:
				group = m.groupdict()
				last_packet.update({'diagnostic' : int(group['diagnostic'])})
				continue

			# State bit: Up				- Demand bit: 0
			m = p26.match(line)
			if m:
				group = m.groupdict()
				last_packet.update({'state_bit' : group['state_bit']})
				last_packet.update({'demand_bit' : int(group['demand_bit'])})
				continue

			# I Hear You bit: 1				- Demand bit: 0
			m = p27.match(line)
			if m:
				group = m.groupdict()
				last_packet.update({'i_hear_you_bit' : group['i_hear_you_bit']})
				last_packet.update({'demand_bit' : int(group['demand_bit'])})
				continue

			# Poll bit: 0 				- Final bit: 0
			m = p28.match(line)
			if m:
				group = m.groupdict()
				last_packet.update({'poll_bit' : int(group['poll_bit'])})
				last_packet.update({'final_bit' : int(group['final_bit'])})
				continue

			# C bit: 0
			m = p29.match(line)
			if m:
				group = m.groupdict()
				last_packet.update({'c_bit' : int(group['c_bit'])})
				continue

			# Multiplier: 6			- Length: 24
			m = p30.match(line)
			if m:
				group = m.groupdict()
				last_packet.update({'multiplier' : int(group['multiplier'])})
				last_packet.update({'length' : int(group['length'])})
				continue

			# My Discr.: 4097		- Your Discr.: 4097
			m = p31.match(line)
			if m:
				group = m.groupdict()
				last_packet.update({'my_discr' : int(group['my_discr'])})
				last_packet.update({'your_discr' : int(group['your_discr'])})
				continue

			# Min tx interval: 1000000	- Min rx interval: 1000000
			m = p32.match(line)
			if m:
				group = m.groupdict()
				last_packet.update({'min_tx_int' : 
					int(group['min_tx_interval'])})
				last_packet.update({'min_rx_int' : 
					int(group['min_rx_interval'])})
				continue

			# Min Echo interval: 3000000
			m = p33.match(line)
			if m:
				group = m.groupdict()
				last_packet.update({'min_echo_int' : 
					int(group['min_echo_interval'])})
				continue

			# Cleanup timer hits: 0
			m = p34.match(line)
			if m:
				group = m.groupdict()
				our_neighbor.update({'cleanup_timer_hits': \
					int(group['cleanup_timer_hits'])})
				continue

			# SSO Cleanup Timer called: 0
			m = p35.match(line)
			if m:
				group = m.groupdict()
				our_neighbor.update({'sso_cleanup_timer_called': \
					int(group['sso_cleanup_timer_called'])})
				continue

			# SSO Cleanup Action Taken: 0
			m = p36.match(line)
			if m:
				group = m.groupdict()
				our_neighbor.update({'sso_cleanup_action_taken': \
					int(group['sso_cleanup_action_taken'])})
				continue

			# Pseudo pre-emptive process count: 239103 min/max/avg: 8/16/8 last: 0 ms ago
			m = p37.match(line)
			if m:
				group = m.groupdict()
				pseudo_preemtive_process = our_neighbor.setdefault \
				('pseudo_preemtive_process', {})
				pseudo_preemtive_process.update({k: \
					int(v) for k, v in group.items()})
				continue

			# IPC Tx Failure Count: 0
			m = p38.match(line)
			if m:
				group = m.groupdict()
				our_neighbor.update({'ipc_tx_failure_count': \
					int(group['ipc_tx_failure_count'])})
				continue

			# SSO Cleanup Timer called: 0
			m = p39.match(line)
			if m:
				group = m.groupdict()
				our_neighbor.update({'ipc_rx_failure_count': \
					int(group['ipc_rx_failure_count'])})
				continue

			# Total Adjs Found: 1
			m = p40.match(line)
			if m:
				group = m.groupdict()
				our_neighbor.update({'total_adjs_found': \
					int(group['total_adjs_found'])})
				continue

			# Holddown - negotiated: 510000         adjusted: 0
			m = p41.match(line)
			if m:
				group = m.groupdict()
				our_neighbor.update({'holddown_negotiated': \
					int(group['holddown_negotiated'])})
				our_neighbor.update({'holddown_adjusted': \
					int(group['holddown_adjusted'])})
				continue

			# 172.16.1.1	172.16.1.3
			m = p2.match(line)
			if m:
				group = m.groupdict()
				our_address = ret_dict.setdefault('our_address', {}). \
					setdefault(group['our_address'], {})
				our_neighbor = our_address.setdefault('neighbor_address', \
					{}).setdefault(group['our_neighbor'], {})
				continue

		return ret_dict
