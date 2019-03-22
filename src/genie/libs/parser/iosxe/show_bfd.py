'''show_bfd.py
IOSXE parser for the following show command
	* show bfd neighbors client ospf details
	* show bfd neighbors details
'''

# Python
import re
import pprint
# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
						Optional,\
						Any

# ==============================================================
# Parser for 'show bfd neighbors details'
# ==============================================================
class ShowBfdNeighborsDetailsSchema(MetaParser):
	"""
	Schema for show bfd neighbors details
	"""

	schema = {
		'bfd_neighbors' : {
				Any(): {
					Any():{
						'ld_rd': str,
						'rh_rs': str,
						Optional('holddown_mult'): Any(),
						'state': str,
						'interface': str,
						Optional('session'): {
							'state': str,
							'function_used': str,
							'interval_in_ms': int
						},
						Optional('session_host'): str,
						Optional('our_address'): str,
						Optional('handle'): int,
						Optional('local_diag'): int,
						Optional('demand_mode'): int,
						Optional('poll_bit'): int,
						Optional('min_tx_interface'): int,
						Optional('min_rx_interface'): int,
						Optional('multiplier'): int,
						Optional('received_min_rx_interface'): int,
						Optional('received_multiplier'): int,
						Optional('holddown_hits'): str,
						Optional('hello_hits'): str,
						Optional('rx'): {
							Optional('rx_count'): int,
							Optional('rx_min_interval_in_ms'): int,
							Optional('rx_max_interval_in_ms'): int,
							Optional('rx_avg_interval_in_ms'): int,
							Optional('rx_last_interval_in_ms'): int
						},
						Optional('tx'): {
							Optional('tx_count'): int,
							Optional('tx_min_interval_in_ms'): int,
							Optional('tx_max_interval_in_ms'): int,
							Optional('tx_avg_interval_in_ms'): int,
							Optional('tx_last_interval_in_ms'): int
						},
						Optional('elapsed_time_watermarks'): str,
						Optional('elapsed_time_watermarks_last'): int,
						Optional('registered_protocols'): str,
						Optional('up_time'): str,
						Optional('last_packet'): {
							Optional('version'): int,
							Optional('diagnostic'): int,
							Optional('state_bit'): str,
							Optional('demand_bit'): int,
							Optional('poll_bit'): int,
							Optional('final_bit'): int,
							Optional('c_bit'): int,
							Optional('multiplier'): int,
							Optional('length'): int,
							Optional('my_discr'): int,
							Optional('your_discr'): int,
							Optional('min_tx_interval'): int,
							Optional('min_rx_interval'): int,
							Optional('min_echo_interval'): int			
						}	
						}		
				}			
			},
	}


class ShowBfdNeighborsDetails(ShowBfdNeighborsDetailsSchema):
	""" Parser for 'show bfd neighbors details' """
	
	cli_command = 'show bfd neighbors details'
	
	def cli(self, cmd='', output= None):
		if output is None:
			#execute command to get output
			if cmd:
				out = self.device.execute(cmd)
			else:
				out = self.device.execute(self.cli_command)
		else:
			out = output

		# initial variables
		ret_dict = {}
		neighbors_found = False

		# ALL values
		p1 = re.compile(r'^(?P<our_address>[\d\.]+)\s+(?P<our_neighbor>[\d\.]+)\s+(?P<ld_rd>\d+\/\d+)\s+(?P<rh_rs>\S+)\s+(?P<holddown_mult>\d+\s+\(\d+\s+\))\s+(?P<state>\w+)\s+(?P<interface>[\w\W]+)$')

		# All values in multiple line : IP
		p2 = re.compile(r'^(?P<our_address>[\d\.]+) +(?P<our_neighbor>[\d\.]+)$')

		# All values in multiple line : Body
		p3 = re.compile(r'^(?P<ld_rd>\d+\/\d+)\s+(?P<rh_rs>\S+)\s+(?P<holddown_mult>\d+\s+\(\d+ +\))\s+(?P<state>\w+)\s+(?P<interface>[\w\W]+)$')

		# Without Our Address
		p4 = re.compile(r'^(?P<our_neighbor>[\d\.]+)\s+(?P<ld_rd>\d+\/\d+)\s+(?P<rh_rs>\S+)\s+(?P<state>\w+)\s+(?P<interface>[\w\W]+)$')

		# OurAddr: 123.213.213.12
		p5 = re.compile(r'^OurAddr:\s+(?P<our_address>[\d\.]+)$')

		# Session state is UP and using echo function with 500 ms interval.
		p6 = re.compile(r'^\s*Session +state +is +(?P<state>\S+) +and( +not)? +using' \
			' +(?P<function_used>\S+) +function +with +(?P<interval_in_ms>\d+)' \
			' +ms +interval\.$')

		# Session Host: Software
		p7 = re.compile(r'^\s*Session\s+Host:\s+(?P<session_host>\S+)$')
		
		# OurAddr: 106.162.197.94
		p8 = re.compile(r'^\s*OurAddr: +(?P<our_address>' \
			'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$')

		# Handle: 1
		p9 = re.compile(r'^\s*Handle: +(?P<handle>\d+)$')

		# Local Diag: 0, Demand mode: 0, Poll bit: 0
		p10 = re.compile(r'^\s*Local +Diag: +(?P<local_diag>\d+), +Demand +' \
			'mode: +(?P<demand_mode>\d+), +Poll +bit: +(?P<poll_bit>\d+)$')


		p10_1 = re.compile(r'^\s*MinTxInt:\s+(?P<min_tx_interface>\d+),\s+MinRxInt:\s+(?P<min_rx_interface>\d+),\s+Multiplier:\s+(?P<multiplier>\d+)\s*Received\s+MinRxInt:\s+(?P<received_min_rx_interface>\d+),\s+Received\s+Multiplier:\s+(?P<received_multiplier>\d+)\s+Hold(d)?own\s+\(hits\):\s+(?P<holddown_hits>\d+\(\d+\)),\s+Hello\s+\(hits\):\s+(?P<hello_hits>\d+\(\d+\))\s+Rx +Count:\s+(?P<rx_count>\d+),\s+Rx\s+Interval\s+\(ms\)\s+min\/max\/avg:\s+(?P<rx_min_interval_in_ms>\d+)\/(?P<rx_max_interval_in_ms>\d+)\/(?P<rx_avg_interval_in_ms>\d+) +last:\s+(?P<rx_last_interval_in_ms>\d+) +ms +ago\s*Tx\s+Count: +(?P<tx_count>\d+),\s+Tx\s+Interval\s+\(ms\)\s+min\/max\/avg:\s+(?P<tx_min_interval_in_ms>\d+)\/(?P<tx_max_interval_in_ms>\d+)\/(?P<tx_avg_interval_in_ms>\d+)\s+last:\s+(?P<tx_last_interval_in_ms>\d+)\s+ms\s+ago\s*Elapsed\s+time\s+watermarks:\s+(?P<elapsed_time_watermarks>\d+\s+\d+) +\(last:\s+(?P<elapsed_time_watermarks_last>\d+)\)\s*Registered\s+protocols:\s+(?P<registered_protocols>[\w\W]+)$')
		# MinTxInt: 100000, MinRxInt: 100000, Multiplier: 6
		p11 = re.compile(r'^\s*MinTxInt: +(?P<min_tx_interface>\d+), +MinRxInt' \
			': +(?P<min_rx_interface>\d+), +Multiplier: +(?P<multiplier>\d+)$')

		# Received MinRxInt: 100000, Received Multiplier: 6
		p12 = re.compile(r'^\s*Received +MinRxInt:\s+(?P<received_min_rx_interface>\d+),\s+Received\s+Multiplier:\s+(?P<received_multiplier>\d+)$')

		# Holddown (hits): 0(0), Hello (hits): 1000(1939)
		p13 = re.compile(r'^\s*Holddown +\(hits\): +' \
			'(?P<holddown_hits>\d+\(\d+\)), +Hello +\(hits\): +' \
			'(?P<hello_hits>\d+\(\d+\))$')

		# Rx Count: 1940, Rx Interval (ms) min/max/avg: 1/1003/879 last: 182 ms ago
		p14 = re.compile(r'^\s*Rx +Count: +(?P<rx_count>\d+), +Rx +' \
			'Interval +\(ms\) +min\/max\/avg: +(?P<rx_min_interval_in_ms>\d+)' \
			'\/(?P<rx_max_interval_in_ms>\d+)\/(?P<rx_avg_interval_in_ms>\d+) +' \
			'last: +(?P<rx_last_interval_in_ms>\d+) +ms +ago$')

		p14_1 = re.compile(r'^\s*Rx +Count: +(?P<rx_count>\d+)$')

		# Tx Count: 1940, Tx Interval (ms) min/max/avg: 1/1003/879 last: 742 ms ago
		p15 = re.compile(r'^\s*Tx +Count: +(?P<tx_count>\d+), +Tx +Interval +' \
			'\(ms\) +min\/max\/avg: +(?P<tx_min_interval_in_ms>\d+)\/(?P<tx_max_interval_in_ms>\d+)\/(?P<tx_avg_interval_in_ms>\d+) +last: +(?P<tx_last_interval_in_ms>\d+) +ms +ago$')
		p15_1 = re.compile(r'^\s*Tx +Count: +(?P<tx_count>\d+)$')
		
		# Elapsed time watermarks: 0 0 (last: 0)
		p16 = re.compile(r'^\s*Elapsed +time +watermarks: +' \
			'(?P<elapsed_time_watermarks>\d+ +\d+) +\(last: +' \
			'(?P<elapsed_time_watermarks_last>\d+)\)$')

		# Registered protocols: OSPF CEF
		p17 = re.compile(r'^\s*Registered +protocols: +' \
			'(?P<registered_protocols>[\w\W]+)$')

		# Uptime: 00:28:03
		p18 = re.compile(r'^\s*Uptime: +(?P<up_time>\S+)$')
		
		# Last packet: Version: 1		- Diagnostic: 0
		p19 = re.compile(r'^\s*Last\s+packet:\s+Version:\s+(?P<version>\d+)\s+\-\s+Diagnostic:\s+(?P<diagnostic>\d+)$')

		p19_1 = re.compile(r'\s*Last\s+packet:\sVersion:\s+(?P<version>\d+)$')
		p19_2 = re.compile(r'\s*\-\s+Diagnostic:\s+(?P<diagnostic>\d+)$')
		# State bit: Up				- Demand bit: 0
		p20 = re.compile(r'^\s*State +bit: +(?P<state_bit>\S+)\s+\-\s+' \
			'Demand +bit:\s+(?P<demand_bit>\d+)$')

		# Poll bit: 0 				- Final bit: 0
		p21 = re.compile(r'^\s*Poll\s+bit:\s+(?P<poll_bit>\d+)\s+\-\s+Final\s+bit:\s+(?P<final_bit>\d+)$')
		
		# C bit: 0
		p22 = re.compile(r'^\s*C +bit: +(?P<c_bit>\d+)$')

		# Multiplier: 6			- Length: 24
		p23 = re.compile(r'^\s*Multiplier: +(?P<multiplier>\d+)\s+\-\s+' \
			'Length:\s+(?P<length>\d+)$')
		
		# My Discr.: 4097		- Your Discr.: 4097
		p24 = re.compile(r'^\s*My +Discr\.: +(?P<my_discr>\d+)\s+\-\s+' \
			'Your +Discr\.:\s+(?P<your_discr>\d+)')
		
		# Min tx interval: 1000000	- Min rx interval: 1000000
		p25 = re.compile(r'^\s*Min +tx +interval: +(?P<min_tx_interval>\d+)' \
			'\s+\-\s+Min +rx +interval:\s+(?P<min_rx_interval>\d+)$')

		# Min Echo interval: 3000000
		p26 = re.compile(r'^\s*Min\s+Echo\s+interval:\s+' \
			'(?P<min_echo_interval>\d+)$')
		
		for line in out.splitlines():
			line = line.strip()
			# NeighAddr	LD/RD	RH/RS	State	Int	
			m = p1.match(line)
			if m:
				
				group = m.groupdict()
				bfd_neighbors = ret_dict.setdefault('bfd_neighbors',{})
				our_address = bfd_neighbors.setdefault(group['our_address'], {})
				our_neighbor = our_address.setdefault(group['our_neighbor'], {})
				our_neighbor.update({'ld_rd' : group['ld_rd']})
				our_neighbor.update({'rh_rs' : group['rh_rs']})
				our_neighbor.update({'holddown_mult' : group['holddown_mult']})
				our_neighbor.update({'state' : group['state']})
				our_neighbor.update({'interface' : group['interface']})
				continue

			m = p2.match(line)
			if m:
				
				group = m.groupdict()
				bfd_neighbors = ret_dict.setdefault('bfd_neighbors',{})
				our_address = bfd_neighbors.setdefault(group['our_address'], {})
				our_neighbor = our_address.setdefault(group['our_neighbor'], {})
				continue

			m = p3.match(line)
			if m:
				
				group = m.groupdict()
				our_neighbor.update({'ld_rd' : group['ld_rd']})
				our_neighbor.update({'rh_rs' : group['rh_rs']})
				our_neighbor.update({'holddown_mult' : group['holddown_mult']})
				our_neighbor.update({'state' : group['state']})
				our_neighbor.update({'interface' : group['interface']})
				continue

			m = p4.match(line)
			if m:
				
				group = m.groupdict()
				bfd_neighbors = ret_dict.setdefault('bfd_neighbors',{})
				neighbor = {}
				our_neighbor = neighbor.setdefault(group['our_neighbor'], {})
				our_neighbor.update({'ld_rd' : group['ld_rd']})
				our_neighbor.update({'rh_rs' : group['rh_rs']})
				our_neighbor.update({'state' : group['state']})
				our_neighbor.update({'interface' : group['interface']})
				continue

			m = p5.match(line)
			if m:
				
				group = m.groupdict()
				bfd_neighbors.setdefault(group['our_address'], neighbor)

				continue
			# Session state is UP and using echo function with 500 ms interval.
			m = p6.match(line)
			if m:
				
				group = m.groupdict()
				session = our_neighbor.setdefault('session', {})
				session.update({'state' : group['state']})
				session.update({'function_used' : group['function_used']})
				session.update({'interval_in_ms' : 
					int(group['interval_in_ms'])})
				continue

			# Session Host: Software
			m = p7.match(line)
			if m:
				
				group = m.groupdict()
				our_neighbor.update({'session_host' : group['session_host']})
				continue
			
			# OurAddr: 106.162.197.94
			m = p8.match(line)
			if m:
				
				group = m.groupdict()
				our_neighbor.update({'our_address' : group['our_address']})
				continue

			# Handle: 1
			m = p9.match(line)
			if m:
				
				group = m.groupdict()
				our_neighbor.update({'handle' : int(group['handle'])})
				continue

			# Local Diag: 0, Demand mode: 0, Poll bit: 0
			m = p10.match(line)
			if m:
				
				group = m.groupdict()
				our_neighbor.update({k: int(v) for k, v in group.items()})
				continue

			# MinTxInt: 100000, MinRxInt: 100000, Multiplier: 6
			m = p10_1.match(line)
			if m:
				
				group = m.groupdict()
				our_neighbor.update({'min_rx_interface' : int(group['min_rx_interface'])})
				our_neighbor.update({'multiplier' : int(group['multiplier'])})
				our_neighbor.update({'received_min_rx_interface' : int(group['received_min_rx_interface'])})
				our_neighbor.update({'received_multiplier' : int(group['min_rx_interface'])})
				our_neighbor.update({'holddown_hits' : group['holddown_hits']})
				our_neighbor.update({'hello_hits' : group['hello_hits']})
				rx = our_neighbor.setdefault('rx', {})
				rx.update({'rx_count' : int(group['rx_count'])})
				rx.update({'rx_min_interval_in_ms' : int(group['rx_min_interval_in_ms'])})
				rx.update({'rx_min_interval_in_ms' : int(group['rx_min_interval_in_ms'])})
				rx.update({'rx_avg_interval_in_ms' : int(group['rx_avg_interval_in_ms'])})
				rx.update({'rx_last_interval_in_ms' : int(group['min_rx_interface'])})
				tx = our_neighbor.setdefault('tx', {})
				tx.update({'tx_count' : int(group['tx_count'])})
				tx.update({'tx_min_interval_in_ms' : int(group['tx_min_interval_in_ms'])})
				tx.update({'tx_max_interval_in_ms' : int(group['tx_max_interval_in_ms'])})
				tx.update({'tx_avg_interval_in_ms' : int(group['tx_avg_interval_in_ms'])})
				tx.update({'tx_last_interval_in_ms' : int(group['tx_last_interval_in_ms'])})
				our_neighbor.update({'elapsed_time_watermarks' : group['elapsed_time_watermarks']})
				our_neighbor.update({'elapsed_time_watermarks_last' : int(group['elapsed_time_watermarks_last'])})
				our_neighbor.update({'registered_protocols' : group['registered_protocols']})

				continue

			# MinTxInt: 100000, MinRxInt: 100000, Multiplier: 6
			m = p11.match(line)
			if m:
				
				group = m.groupdict()
				our_neighbor.update({k: int(v) for k, v in group.items()})
				continue

			# Received MinRxInt: 100000, Received Multiplier: 6
			m = p12.match(line)
			if m:
				
				group = m.groupdict()
				our_neighbor.update({k: int(v) for k, v in group.items()})
				continue

			# Holddown (hits): 0(0), Hello (hits): 1000(1939)
			m = p13.match(line)
			if m:
				
				group = m.groupdict()
				our_neighbor.update({k: v for k, v in group.items()})
				continue

			# Rx Count: 1940, Rx Interval (ms) min/max/avg: 1/1003/879 last: 182 ms ago
			m = p14.match(line)
			if m:
				
				group = m.groupdict()
				rx = our_neighbor.setdefault('rx', {})
				rx.update({k: int(v) for k, v in group.items()})
				continue

			# Rx Count: 1940, Rx Interval (ms) min/max/avg: 1/1003/879 last: 182 ms ago
			m = p14_1.match(line)
			if m:
				
				group = m.groupdict()
				rx = our_neighbor.setdefault('rx', {})
				rx.update({k: int(v) for k, v in group.items()})
				continue

			# Tx Count: 1940, Tx Interval (ms) min/max/avg: 1/1003/879 last: 742 ms ago
			m = p15.match(line)
			if m:
				
				group = m.groupdict()
				tx = our_neighbor.setdefault('tx', {})
				tx.update({k: int(v) for k, v in group.items()})
				continue

			# Tx Count: 1940, Tx Interval (ms) min/max/avg: 1/1003/879 last: 742 ms ago
			m = p15_1.match(line)
			if m:
				
				group = m.groupdict()
				tx = our_neighbor.setdefault('tx', {})
				tx.update({k: int(v) for k, v in group.items()})
				continue
			# Elapsed time watermarks: 0 0 (last: 0)
			m = p16.match(line)
			if m:
				
				group = m.groupdict()
				our_neighbor.update({'elapsed_time_watermarks' : 
					group['elapsed_time_watermarks']})
				our_neighbor.update({'elapsed_time_watermarks_last' : 
					int(group['elapsed_time_watermarks_last'])})
				continue

			# Registered protocols: OSPF CEF
			m = p17.match(line)
			if m:
				
				group = m.groupdict()
				our_neighbor.update({'registered_protocols' : 
					group['registered_protocols']})
				continue

			# Last packet: Version: 1		- Diagnostic: 0
			m = p18.match(line)
			if m:
				
				group = m.groupdict()
				our_neighbor.update({'up_time' : group['up_time']})
				continue

			# Last packet: Version: 1		- Diagnostic: 0
			m = p19.match(line)
			if m:
				
				group = m.groupdict()
				last_packet = our_neighbor.setdefault('last_packet', {})
				last_packet.update({'version' : int(group['version'])})
				last_packet.update({'diagnostic' : int(group['diagnostic'])})
				continue

			# Last packet: Version: 1		- Diagnostic: 0
			m = p19_1.match(line)
			if m:
				
				group = m.groupdict()
				last_packet = our_neighbor.setdefault('last_packet', {})
				last_packet.update({'version' : int(group['version'])})
				
				continue

			# Last packet: Version: 1		- Diagnostic: 0
			m = p19_2.match(line)
			if m:
				
				group = m.groupdict()
				
				last_packet.update({'diagnostic' : int(group['diagnostic'])})
				continue

			# State bit: Up				- Demand bit: 0
			m = p20.match(line)
			if m:
				
				group = m.groupdict()
				last_packet.update({'state_bit' : group['state_bit']})
				last_packet.update({'demand_bit' : int(group['demand_bit'])})
				continue

			# Poll bit: 0 				- Final bit: 0
			m = p21.match(line)
			if m:
				
				group = m.groupdict()
				last_packet.update({'poll_bit' : int(group['poll_bit'])})
				last_packet.update({'final_bit' : int(group['final_bit'])})
				continue

			# C bit: 0
			m = p22.match(line)
			if m:
				
				group = m.groupdict()
				last_packet.update({'c_bit' : int(group['c_bit'])})
				continue

			# Multiplier: 6			- Length: 24
			m = p23.match(line)
			if m:
				
				group = m.groupdict()
				last_packet.update({'multiplier' : int(group['multiplier'])})
				last_packet.update({'length' : int(group['length'])})
				continue

			# My Discr.: 4097		- Your Discr.: 4097
			m = p24.match(line)
			if m:
				
				group = m.groupdict()
				last_packet.update({'my_discr' : int(group['my_discr'])})
				last_packet.update({'your_discr' : int(group['your_discr'])})
				continue

			# Min tx interval: 1000000	- Min rx interval: 1000000
			m = p25.match(line)
			if m:
				
				group = m.groupdict()
				last_packet.update({'min_tx_interval' : 
					int(group['min_tx_interval'])})
				last_packet.update({'min_rx_interval' : 
					int(group['min_rx_interval'])})
				continue

			# Min Echo interval: 3000000
			m = p26.match(line)
			if m:
				
				group = m.groupdict()
				last_packet.update({'min_echo_interval' : 
					int(group['min_echo_interval'])})
				continue
		return ret_dict


class ShowBfdNeighborsClientOSPFDetails(ShowBfdNeighborsDetails):
	""" Parser for 'show bfd neighbors client ospf details' """
	
	cli_command = 'show bfd neighbors client ospf details'
	def cli(self, output=None):
		return super().cli(cmd=self.cli_command, output=output)