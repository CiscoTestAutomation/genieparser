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
		  'neighbors_address': {
				Any(): {
					'ld_rd': str,
					'rh_rs': str,
					'state': str,
					'interface': str				
				}			
			},
			'session': {
				'state': str,
				'function_used': str,
				'interval_in_ms': int
			},
			'session_host': str,
			'our_address': str,
			'handle': int,
			'local_diag': int,
			'demand_mode': int,
			'poll_bit': int,
			'min_tx_interface': int,
			'min_rx_interface': int,
			'multiplier': int,
			'received_min_rx_interface': int,
			'received_multiplier': int,
			'holddown_hits': str,
			'hello_hits': str,
			'rx': {
				'count': int,
				'min_interval_in_ms': int,
				'max_interval_in_ms': int,
				'avg_interval_in_ms': int,
				'last_interval_in_ms': int
			},
			'tx': {
				'count': int,
				'min_interval_in_ms': int,
				'max_interval_in_ms': int,
				'avg_interval_in_ms': int,
				'last_interval_in_ms': int
			},
			'elapsed_time_watermarks': str,
			'elapsed_time_watermarks_last': int,
			'registered_protocols': str,
			'up_time': str,
			'last_packet': {
				'version': int,
				'diagnostic': int,
				'state_bit': str,
				'demand_bit': int,
				'poll_bit': int,
				'final_bit': int,
				'c_bit': int,
				'multiplier': int,
				'length': int,
				'my_discr': int,
				'your_discr': int,
				'min_tx_interval': int,
				'min_rx_interval': int,
				'min_echo_interval': int			
			}
		}
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
		
		# NeighAddr	LD/RD	RH/RS	State	Int		
		p1 = re.compile(r'^\s*NeighAddr\s+LD\/RD\s+RH\/RS\s+State\s+Int$')
				
		# 106.162.197.93	4097/4097	Up	Up	Gi0/0/0
		p2 = re.compile(r'^\s*(?P<neighbor_address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s+(?P<ld_rd>\S+)\s+(?P<rh_rs>\S+)\s+(?P<state>\S+)\s+(?P<interface>\S+)$')

		# Session state is UP and using echo function with 500 ms interval.
		p3 = re.compile(r'^\s*Session +state +is +(?P<state>\S+) +and +using +(?P<function_used>\S+) +function +with +(?P<interval_in_ms>\d+) +ms +interval\.$')

		# Session Host: Software
		p4 = re.compile(r'^\s*Session +Host: +(?P<session_host>\S+)$')
		
		# OurAddr: 106.162.197.94
		p5 = re.compile(r'^\s*OurAddr: +(?P<our_address>\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})$')

		# Handle: 1
		p6 = re.compile(r'^\s*Handle: +(?P<handle>\d+)$')

		# Local Diag: 0, Demand mode: 0, Poll bit: 0
		p7 = re.compile(r'^\s*Local +Diag: +(?P<local_diag>\d+), +Demand +mode: +(?P<demand_mode>\d+), +Poll +bit: +(?P<poll_bit>\d+)$')

		# MinTxInt: 100000, MinRxInt: 100000, Multiplier: 6
		p8 = re.compile(r'^\s*MinTxInt: +(?P<min_tx_interface>\d+), +MinRxInt: +(?P<min_rx_interface>\d+), +Multiplier: +(?P<multiplier>\d+)$')

		# Received MinRxInt: 100000, Received Multiplier: 6
		p9 = re.compile(r'^\s*Received +MinRxInt: +(?P<received_min_rx_interface>\d+), +Received +Multiplier: +(?P<received_multiplier>\d+)$')

		# Holddown (hits): 0(0), Hello (hits): 1000(1939)
		p10 = re.compile(r'^\s*Holddown +\(hits\): +(?P<holddown_hits>\d+\(\d+\)), +Hello +\(hits\): +(?P<hello_hits>\d+\(\d+\))$')

		# Rx Count: 1940, Rx Interval (ms) min/max/avg: 1/1003/879 last: 182 ms ago
		p11 = re.compile(r'^\s*Rx +Count: +(?P<count>\d+), +Rx +Interval +\(ms\) +min\/max\/avg: +(?P<min_interval_in_ms>\d+)\/(?P<max_interval_in_ms>\d+)\/(?P<avg_interval_in_ms>\d+) +last: +(?P<last_interval_in_ms>\d+) +ms +ago$')

		# Tx Count: 1940, Tx Interval (ms) min/max/avg: 1/1003/879 last: 742 ms ago
		p12 = re.compile(r'^\s*Tx +Count: +(?P<count>\d+), +Tx +Interval +\(ms\) +min\/max\/avg: +(?P<min_interval_in_ms>\d+)\/(?P<max_interval_in_ms>\d+)\/(?P<avg_interval_in_ms>\d+) +last: +(?P<last_interval_in_ms>\d+) +ms +ago$')
		
		# Elapsed time watermarks: 0 0 (last: 0)
		p13 = re.compile(r'^\s*Elapsed +time +watermarks: +(?P<elapsed_time_watermarks>\d+ +\d+) +\(last: +(?P<elapsed_time_watermarks_last>\d+)\)$')

		# Registered protocols: OSPF CEF
		p14 = re.compile(r'^\s*Registered +protocols: +(?P<registered_protocols>[\w\W]+)$')

		# Uptime: 00:28:03
		p15 = re.compile(r'^\s*Uptime: +(?P<up_time>\S+)$')
		
		# Last packet: Version: 1		- Diagnostic: 0
		p16 = re.compile(r'^\s*Last\s+packet:\s+Version:\s+(?P<version>\d+)\s+\-\s+Diagnostic:\s+(?P<diagnostic>\d+)$')

		# State bit: Up				- Demand bit: 0
		p17 = re.compile(r'^\s*State +bit: +(?P<state_bit>\S+)\s+\-\s+Demand +bit:\s+(?P<demand_bit>\d+)$')

		# Poll bit: 0 				- Final bit: 0
		p18 = re.compile(r'^\s*Poll +bit: +(?P<poll_bit>\d+)\s+\-\s+Final +bit:\s+(?P<final_bit>\d+)$')
		
		# C bit: 0
		p19 = re.compile(r'^\s*C +bit: +(?P<c_bit>\d+)$')

		# Multiplier: 6			- Length: 24
		p20 = re.compile(r'^\s*Multiplier: +(?P<multiplier>\d+)\s+\-\s+Length:\s+(?P<length>\d+)$')
		
		# My Discr.: 4097		- Your Discr.: 4097
		p21 = re.compile(r'^\s*My +Discr\.: +(?P<my_discr>\d+)\s+\-\s+Your +Discr\.:\s+(?P<your_discr>\d+)')
		
		# Min tx interval: 1000000	- Min rx interval: 1000000
		p22 = re.compile(r'^\s*Min +tx +interval: +(?P<min_tx_interval>\d+)\s+\-\s+Min +rx +interval:\s+(?P<min_rx_interval>\d+)$')

		# Min Echo interval: 3000000
		p23 = re.compile(r'^\s*Min\s+Echo\s+interval:\s+(?P<min_echo_interval>\d+)$')
		
		for line in out.splitlines():
			line = line.strip()
			m = p1.match(line)
			if m:
				neighbors_found = True
				bfd_neighbors = ret_dict.setdefault('bfd_neighbors',{})
				neighbors_address = bfd_neighbors.setdefault('neighbors_address',{})
				continue
			
			if neighbors_found:
				m = p2.match(line)
				if m:
					group = m.groupdict()
					neighbor_address = neighbors_address.setdefault(group['neighbor_address'] , {})					
					neighbor_address['ld_rd'] = group['ld_rd']
					neighbor_address['rh_rs'] = group['rh_rs']
					neighbor_address['state'] = group['state']
					neighbor_address['interface'] = group['interface']
					continue
				else:
					neighbors_found = False

			m = p3.match(line)
			if m:
				group = m.groupdict()
				bfd_neighbors['session'] = {}
				bfd_neighbors['session']['state'] = group['state']
				bfd_neighbors['session']['function_used'] = group['function_used']
				bfd_neighbors['session']['interval_in_ms'] = int(group['interval_in_ms'])
				continue
			
			m = p4.match(line)
			if m:
				group = m.groupdict()
				bfd_neighbors['session_host'] = group['session_host']
				continue

			m = p5.match(line)
			if m:
				group = m.groupdict()
				bfd_neighbors['our_address'] = group['our_address']
				continue

			m = p6.match(line)
			if m:
				group = m.groupdict()
				bfd_neighbors['handle'] = int(group['handle'])
				continue

			m = p7.match(line)
			if m:
				group = m.groupdict()
				bfd_neighbors['local_diag'] = int(group['local_diag'])
				bfd_neighbors['demand_mode'] = int(group['demand_mode'])
				bfd_neighbors['poll_bit'] = int(group['poll_bit'])
				continue

			m = p8.match(line)
			if m:
				group = m.groupdict()
				bfd_neighbors['min_tx_interface'] = int(group['min_tx_interface'])
				bfd_neighbors['min_rx_interface'] = int(group['min_rx_interface'])
				bfd_neighbors['multiplier'] = int(group['multiplier'])
				continue

			m = p9.match(line)
			if m:
				group = m.groupdict()
				bfd_neighbors['received_min_rx_interface'] = int(group['received_min_rx_interface'])
				bfd_neighbors['received_multiplier'] = int(group['received_multiplier'])
				continue

			m = p10.match(line)
			if m:
				group = m.groupdict()
				bfd_neighbors['holddown_hits'] = group['holddown_hits']
				bfd_neighbors['hello_hits'] = group['hello_hits']
				continue

			m = p11.match(line)
			if m:
				group = m.groupdict()
				bfd_neighbors['rx'] = {}
				bfd_neighbors['rx']['count'] = int(group['count'])
				bfd_neighbors['rx']['min_interval_in_ms'] = int(group['min_interval_in_ms'])
				bfd_neighbors['rx']['max_interval_in_ms'] = int(group['max_interval_in_ms'])
				bfd_neighbors['rx']['avg_interval_in_ms'] = int(group['avg_interval_in_ms'])
				bfd_neighbors['rx']['last_interval_in_ms'] = int(group['last_interval_in_ms'])
				continue

			m = p12.match(line)
			if m:
				group = m.groupdict()
				bfd_neighbors['tx'] = {}
				bfd_neighbors['tx']['count'] = int(group['count'])
				bfd_neighbors['tx']['min_interval_in_ms'] = int(group['min_interval_in_ms'])
				bfd_neighbors['tx']['max_interval_in_ms'] = int(group['max_interval_in_ms'])
				bfd_neighbors['tx']['avg_interval_in_ms'] = int(group['avg_interval_in_ms'])
				bfd_neighbors['tx']['last_interval_in_ms'] = int(group['last_interval_in_ms'])
				continue

			m = p13.match(line)
			if m:
				group = m.groupdict()
				bfd_neighbors['elapsed_time_watermarks'] = group['elapsed_time_watermarks']
				bfd_neighbors['elapsed_time_watermarks_last'] = int(group['elapsed_time_watermarks_last'])
				continue

			m = p14.match(line)
			if m:
				group = m.groupdict()
				bfd_neighbors['registered_protocols'] = group['registered_protocols']
				continue

			m = p15.match(line)
			if m:
				group = m.groupdict()
				bfd_neighbors['up_time'] = group['up_time']
				continue

			m = p16.match(line)
			if m:
				group = m.groupdict()
				bfd_neighbors['last_packet'] = {}
				bfd_neighbors['last_packet']['version'] = int(group['version'])
				bfd_neighbors['last_packet']['diagnostic'] = int(group['diagnostic'])
				continue

			m = p17.match(line)
			if m:
				group = m.groupdict()
				bfd_neighbors['last_packet']['state_bit'] = group['state_bit']
				bfd_neighbors['last_packet']['demand_bit'] = int(group['demand_bit'])
				continue

			m = p18.match(line)
			if m:
				group = m.groupdict()
				bfd_neighbors['last_packet']['poll_bit'] = int(group['poll_bit'])
				bfd_neighbors['last_packet']['final_bit'] = int(group['final_bit'])
				continue

			m = p19.match(line)
			if m:
				group = m.groupdict()
				bfd_neighbors['last_packet']['c_bit'] = int(group['c_bit'])
				continue

			m = p20.match(line)
			if m:
				group = m.groupdict()
				bfd_neighbors['last_packet']['multiplier'] = int(group['multiplier'])
				bfd_neighbors['last_packet']['length'] = int(group['length'])
				continue

			m = p21.match(line)
			if m:
				group = m.groupdict()
				bfd_neighbors['last_packet']['my_discr'] = int(group['my_discr'])
				bfd_neighbors['last_packet']['your_discr'] = int(group['your_discr'])
				continue

			m = p22.match(line)
			if m:
				group = m.groupdict()
				bfd_neighbors['last_packet']['min_tx_interval'] = int(group['min_tx_interval'])
				bfd_neighbors['last_packet']['min_rx_interval'] = int(group['min_rx_interval'])
				continue

			m = p23.match(line)
			if m:
				group = m.groupdict()
				bfd_neighbors['last_packet']['min_echo_interval'] = int(group['min_echo_interval'])
				continue
		return ret_dict


class ShowBfdNeighborsClientOSPFDetails(ShowBfdNeighborsDetails):
	""" Parser for 'show bfd neighbors client ospf details' """
	
	cli_command = 'show bfd neighbors client ospf details'
	def cli(self, output=None):
		return super().cli(cmd=self.cli_command, output=output)