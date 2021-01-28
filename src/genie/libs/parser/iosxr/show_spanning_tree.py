"""show_spanning_tree.py

IOSXR parser for the following show commands:
	* show spanning-tree mst {mst_id}
	* show spanning-tree mstag {mag_domain}
	* show spanning-tree pvrst {pvst_id}
	* show spanning-tree pvrstag {pvrstag_domain}
	* show spanning-tree pvstag {pvstag_domain}
"""

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
										 Any, \
										 Optional, \
										 Or, \
										 And, \
										 Default, \
										 Use

# import parser utils
from genie.libs.parser.utils.common import Common

"""Schema for 'show spanning-tree mst {mst_id}'"""
class ShowSpanningTreeMstSchema(MetaParser):
	schema = {
		'mstp': {
			Any(): {
				'mst_instances': {
					Any(): {
						'mst_id': str,
						Optional('vlan'): str,
						Optional('this_bridge_is'): str,
						Optional('bridge_priority'): int,
						Optional('bridge_address'): str,
						Optional('bridge_max_age'): int,
						Optional('bridge_forward_delay'): int,
						Optional('bridge_max_hops'): int,
						Optional('bridge_transmit_hold_count'): int, 
						Optional('designated_root_priority'): int,
						Optional('designated_root_address'): str,
						Optional('root_cost'): int,
						Optional('root_max_age'): int,
						Optional('root_forward_delay'): int,
						Optional('cist_root_priority'): int,
						Optional('cist_root_address'): str,
						Optional('cist_root_cost'): int,
						Optional('sys_id_ext'): int,
						'interfaces': {
							Any(): {
								'name':str,
								'cost': int, 
								'port_priority': int, 
								'port_num': int, 
								'role': str, 
								'port_state': str,
								Optional('designated_cost'): int,
								'designated_bridge_priority': int,
								'designated_bridge_address': str,
								'designated_port_priority': int,
								'designated_port_num': int,
							}
						}
					}
				}
			}
		}
	}

# ======================================
# Parser for:
#   * 'show spanning-tree mst {mst_id}'
# ======================================
class ShowSpanningTreeMst(ShowSpanningTreeMstSchema):
	'''Parser for:
		* 'show spanning-tree mst {mst_id}'
	'''
	cli_command = 'show spanning-tree mst {mst}'

	def cli(self, mst, output=None):
		if output is None:
			# get output from device
			out = self.device.execute(self.cli_command.format(mst=mst))
		else:
			out = output

		# initial return dictionary
		ret_dict = {}
		# MSTI 0 (CIST):
		p1 = re.compile(r'^MSTI +(?P<mst_id>\d+)([\s\S]+)?:$')
		# VLANS Mapped: 1-4094
		p2 = re.compile(r'^VLANS +Mapped: +(?P<vlan>\S+)$')
		# CIST Root  Priority	32768
		p3 = re.compile(r'^CIST\s+Root\s+Priority\s+'
			'(?P<cist_root_priority>\d+)')
		# Address	 0021.1bff.0e05
		p4 = re.compile(r'^Address\s+(?P<address>[\w\.]+)$')
		# Ext Cost    2000
		p5 = re.compile(r'^Ext\s+Cost\s+(?P<cist_root_cost>\d+)$')
		# Root ID    Priority    32768
		p6 = re.compile(r'^Root\s+ID\s+Priority\s+(?P<designated_root_priority>'
			'\d+)')
		# Int Cost    0
		p7 = re.compile(r'^Int\s+Cost\s+(?P<root_cost>\d+)$')
		# Max Age 20 sec, Forward Delay 15 sec
		p8 = re.compile(r'^Max\s+Age\s+(?P<max_age>\d+)\s+sec,'
			'\s+Forward\s+Delay\s+(?P<forward_delay>\d+)\s+sec$')
		# Max Hops 20, Transmit Hold count	6
		p9 = re.compile(r'^Max\s+Hops\s+(?P<bridge_max_hops>\d+),'
			'\s+Transmit\s+Hold\s+count\s+(?P<bridge_transmit_hold_count>\d+)$')
		# Bridge ID Priority 32768 (priority 32768 sys-id-ext 0)
		p10 = re.compile(r'^Bridge\s+ID\s+Priority\s+(?P<bridge_priority>\d+)'
			'(\s+\(priority\s+\d+\s+sys\-id\-ext\s+(?P<sys_id_ext>\d+)\))?')
		# Te0/0/0/16   128.1   2000      ROOT FWD   32768 0021.1bff.0e05 128.1  
		p11 = re.compile(r'^(?P<name>\S+)\s+(?P<port_priority>\d+)\.'
			'(?P<port_num>\d+)\s+(?P<cost>\d+)\s+(?P<role>\w+)\s+'
			'(?P<port_state>\w+)\s+((?P<designated_cost>\d+)\s+)?'
			'(?P<designated_bridge_priority>\d+)\s+(?P<designated_bridge_address>'
			'[\w\.]+)\s+(?P<designated_port_priority>\d+)\.'
			'(?P<designated_port_num>\d+)$')
		# This bridge is the root
		p12 = re.compile(r'This +bridge +is +(?P<this_bridge_is>[\w ]+)$')
		
		for line in out.splitlines():
			line = line.strip()

			# MSTI 0 (CIST):
			m = p1.match(line)
			if m:
				group = m.groupdict()
				mst_instances = ret_dict.setdefault('mstp', {}). \
					setdefault(mst, {}). \
					setdefault('mst_instances', {}).setdefault(group['mst_id'], {})
				mst_instances.update({'mst_id' : group['mst_id']})
				continue

			# VLANS Mapped: 1-4094
			m = p2.match(line)
			if m:
				group = m.groupdict()
				mst_instances.update({'vlan' : group['vlan']})
				continue

			# CIST Root  Priority    32768
			m = p3.match(line)
			if m:
				address_type = 'cist_root_address'
				group = m.groupdict()
				mst_instances.update({k:int(v) for k, v in group.items()})
				continue

		   	# Address     0021.1bff.0e05
			m = p4.match(line)
			if m:
				group = m.groupdict()
				mst_instances.update({address_type : group['address']})
				continue
			
			# Ext Cost    2000
			m = p5.match(line)
			if m:
				group = m.groupdict()
				mst_instances.update({k:int(v) for k, v in group.items()})
				continue

			# Root ID    Priority    32768
			m = p6.match(line)
			if m:
				address_type = 'designated_root_address'
				group = m.groupdict()
				mst_instances.update({k:int(v) for k, v in group.items()})
				continue

			# Int Cost    0
			m = p7.match(line)
			if m:
				group = m.groupdict()
				mst_instances.update({k:int(v) for k, v in group.items()})
				continue

			# Max Age 20 sec, Forward Delay 15 sec
			m = p8.match(line)
			if m:
				group = m.groupdict()
				if address_type == 'designated_root_address':
					mst_instances.update({
						'root_max_age' : int(group['max_age'])})
					mst_instances.update({
						'root_forward_delay' : int(group['forward_delay'])})
				if address_type == 'bridge_address':
					mst_instances.update({
						'bridge_max_age' : int(group['max_age'])})
					mst_instances.update({
						'bridge_forward_delay' : int(group['forward_delay'])})
				continue

			# Max Hops 20, Transmit Hold count	6
			m = p9.match(line)
			if m:
				group = m.groupdict()
				mst_instances.update({k:int(v) for k, v in group.items()})
				continue

			# Bridge ID Priority 32768 (priority 32768 sys-id-ext 0)
			m = p10.match(line)
			if m:
				address_type = 'bridge_address'
				group = m.groupdict()
				mst_instances.update({k:int(v) for k, v in group.items()})
				continue

			# Te0/0/0/16   128.1   2000	  ROOT FWD   32768 0021.1bff.0e05 128.1
			m = p11.match(line)
			if m:
				group = m.groupdict()
				interfaces = mst_instances.setdefault('interfaces' , {}). \
					setdefault(Common.convert_intf_name(group['name']), {})
				interfaces.update({'name' : Common.convert_intf_name(group['name'])})
				interfaces.update({'cost' : int(group['cost'])})
				interfaces.update({'role' : group['role']})
				interfaces.update({'port_priority' : int(group['port_priority'])})
				interfaces.update({'port_num' : int(group['port_num'])})
				interfaces.update({'port_state' : group['port_state']})
				interfaces.update({
					'designated_bridge_priority' : int(group['designated_bridge_priority']
						)})
				interfaces.update({
					'designated_bridge_address' : group['designated_bridge_address']})
				interfaces.update({
					'designated_port_priority' : int(group['designated_port_priority'])})
				interfaces.update({
					'designated_port_num' : int(group['designated_port_num'])})
				continue

			# This bridge is the root
			m = p12.match(line)
			if m:
				group = m.groupdict()
				mst_instances.update({k:v for k, v in group.items()})
				continue
		return ret_dict

"""Schema for 'show spanning-tree mstag <mag_domain>'"""
class ShowSpanningTreeMstagSchema(MetaParser):
	schema = {
		'mstag': {
			Any(): {
				'domain': str,
				'interfaces': {
					Any(): {
						'interface': str,
						'preempt_delay': bool,
						Optional('preempt_delay_state'): str,
						'name': str,
						'revision': int,
						'max_age': int,
						'provider_bridge': bool,
						'bridge_id': str,
						'port_id': int,
						'external_cost': int,
						'hello_time': int,
						'active': bool,
						'counters': {
							'bdpu_sent': int,
						}
					},
					'instances': {
						Any(): {
							'instance': int,
							'vlans': str,
							'priority': int,
							'root_bridge': str,
							'root_priority': int,
							'port_priority': int,
							'cost': int,
							'counters': {
								'topology_changes': int
							}
						}
					}
				}
			}
		}
	}

class ShowSpanningTreeMstag(ShowSpanningTreeMstagSchema):
	"""Parser for 'show spanning-tree mstag <mag_domain>'"""
	cli_command = 'show spanning-tree mstag {mag_domain}'
	exclude = [
		'hello_time',
		'bdpu_sent'
	]
	def cli(self,mag_domain, output=None):
		if output is None:
			# get output from device
			out = self.device.execute(self.cli_command.\
				format(mag_domain=mag_domain))
		else:
			out = output

		# initial return dictionary
		ret_dict = {}

		# Bundle-Ether10.0
		p1 = re.compile(r'^(?P<mag_interface>\S+)$')
		# Pre-empt delay is disabled
		# Preempt delay is disabled.
		p2 = re.compile(r'^Pre(\-)?empt +delay +is +(?P<preempt_delay>\w+)\.?'
			'( +)?(?P<preempt_delay_state>Sending +(startup|standard) '
			'+BPDU( +until \S+)?)?')
		# Name:            risc
		p3 = re.compile(r'^Name:\s+(?P<name>\S+)$')
		# Revision: 1
		p4 = re.compile(r'^Revision:\s+(?P<revision>\d+)$')
		# Max Age: 20
		p5 = re.compile(r'^Max Age:\s+(?P<max_age>\d+)$')
		# Provider Bridge: no
		p6 = re.compile(r'^Provider +Bridge:\s+(?P<provider_bridge>\w+)$')
		# Bridge ID:       0000.00ff.0002
		p7 = re.compile(r'^Bridge +ID:\s+(?P<bridge_id>[\w\.]+)$')
		# Port ID:         1
		p8 = re.compile(r'^Port +ID:\s+(?P<port_id>\d+)$')
		# External Cost:   0
		p9 = re.compile(r'^External +Cost:\s+(?P<external_cost>\d+)$')
		# Hello Time:      2
		p10 = re.compile(r'^Hello +Time:\s+(?P<hello_time>\d+)$')
		# Active:          yes
		p11 = re.compile(r'^Active:\s+(?P<active>\w+)$')
		# BPDUs sent:      39921
		p12 = re.compile(r'^BPDUs +sent:\s+(?P<bdpu_sent>\d+)$')
		# MSTI 0 (CIST):
		p13 = re.compile(r'^MSTI +(?P<mst_id>\d+)( +\(CIST\))?:?$')
		#     VLAN IDs:         1-2,4-4094
		p14 = re.compile(r'^VLAN +IDs:\s+(?P<vlans>\S+)$')
		#     Bridge Priority:  8192
		p15 = re.compile(r'^Bridge +Priority:\s+(?P<priority>\d+)$')
		#     Port Priority:    128
		p16 = re.compile(r'^Port +Priority:\s+(?P<port_priority>\d+)$')
		#     Cost:             0
		p17 = re.compile(r'^Cost:\s+(?P<cost>\d+)$')
		#     Root Bridge:      0000.00ff.0001
		p18 = re.compile(r'^Root +Bridge:\s+(?P<root_bridge>[\w\.]+)$')
		#     Root Priority:    4096
		p19 = re.compile(r'^Root +Priority:\s+(?P<root_priority>\d+)$')
		#     Topology Changes: 31
		p20 = re.compile(r'^Topology +Changes:\s+(?P<topology_changes>\d+)$')

		for line in out.splitlines():
			line = line.strip()

			# Bundle-Ether10.0
			m = p1.match(line)
			if m:
				group = m.groupdict()
				mstag = ret_dict.setdefault('mstag', {}). \
					setdefault(mag_domain, {})
				mstag.update({'domain' : mag_domain})
				interfaces = mstag.setdefault('interfaces', {})
				interface = interfaces.setdefault(
					Common.convert_intf_name(group['mag_interface']), {})
				interface.update({
					'interface' : Common.convert_intf_name(group['mag_interface'])})
				continue

			# Pre-empt delay is disabled
			m = p2.match(line)
			if m:
				group = m.groupdict()
				preempt_delay = group['preempt_delay']
				interface.update({'preempt_delay' : (preempt_delay != 'disabled')})
				if group['preempt_delay_state']:
					interface.update({
						'preempt_delay_state' : group['preempt_delay_state']})
				continue
			# Name:            risc
			m = p3.match(line)
			if m:
				group = m.groupdict()
				interface.update({'name' : Common.convert_intf_name(group['name'])})
				continue

			# Name:            risc
			m = p3.match(line)
			if m:
				group = m.groupdict()
				interface.update({k:v for k, v in group.items()})
				continue

			# Revision: 1
			m = p4.match(line)
			if m:
				group = m.groupdict()
				interface.update({k:int(v) for k, v in group.items()})
				continue

			# Max Age: 20
			m = p5.match(line)
			if m:
				group = m.groupdict()
				interface.update({k:int(v) for k, v in group.items()})
				continue

			# Provider Bridge: no
			m = p6.match(line)
			if m:
				group = m.groupdict()
				interface.update({
					'provider_bridge':(group['provider_bridge'].lower() == 'yes')})
				continue

			# Bridge ID:       0000.00ff.0002
			m = p7.match(line)
			if m:
				group = m.groupdict()
				interface.update({k:v for k, v in group.items()})
				continue

			# Port ID:         1
			m = p8.match(line)
			if m:
				group = m.groupdict()
				interface.update({k:int(v) for k, v in group.items()})
				continue

			# External Cost:   0
			m = p9.match(line)
			if m:
				group = m.groupdict()
				interface.update({k:int(v) for k, v in group.items()})
				continue

			# Hello Time:      2
			m = p10.match(line)
			if m:
				group = m.groupdict()
				interface.update({k:int(v) for k, v in group.items()})
				continue

			# Active:          yes
			m = p11.match(line)
			if m:
				group = m.groupdict()
				interface.update({'active': (group['active'] == 'yes')})
				continue

			# BPDUs sent:      39921
			m = p12.match(line)
			if m:
				group = m.groupdict()
				bdpu_sent = {'bdpu_sent' : int(group['bdpu_sent'])}
				interface.update({'counters': bdpu_sent})
				continue

			# MSTI 0 (CIST):
			m = p13.match(line)
			if m:
				group = m.groupdict()
				instances = interfaces.setdefault('instances', {}). \
					setdefault(group['mst_id'], {})
				instances.update({'instance': int(group['mst_id'])})
				continue

			#     VLAN IDs:         1-2,4-4094
			m = p14.match(line)
			if m:
				group = m.groupdict()
				instances.update({k:v for k, v in group.items()})
				continue

			#     Bridge Priority:  8192
			m = p15.match(line)
			if m:
				group = m.groupdict()
				instances.update({k:int(v) for k, v in group.items()})
				continue

			#     Port Priority:    128
			m = p16.match(line)
			if m:
				group = m.groupdict()
				instances.update({k:int(v) for k, v in group.items()})
				continue

			#     Cost:             0
			m = p17.match(line)
			if m:
				group = m.groupdict()
				instances.update({k:int(v) for k, v in group.items()})
				continue

			#     Root Bridge:      0000.00ff.0001
			m = p18.match(line)
			if m:
				group = m.groupdict()
				instances.update({k:v for k, v in group.items()})
				continue

			#     Root Priority:    4096
			m = p19.match(line)
			if m:
				group = m.groupdict()
				instances.update({k:int(v) for k, v in group.items()})
				continue

			#     Topology Changes: 31
			m = p20.match(line)
			if m:
				group = m.groupdict()
				topology_changes = {
					'topology_changes' : int(group['topology_changes'])}
				instances.update({'counters': topology_changes})
				continue
		return ret_dict

"""Schema for 'show spanning-tree pvrst <pvst_id>'"""
class ShowSpanningTreePvrstSchema(MetaParser):
	schema = {
		'pvst': {
			Any(): {
				'pvst_id': str,
				'vlans': {
					Any(): {
						'vlan_id': int,
						'designated_root_priority': int,
						'designated_root_address': str,
						'designated_root_max_age': int,
						'designated_root_forward_delay': int,
						'bridge_priority': int,
						'bridge_address': str,
						'bridge_max_age': int,
						'bridge_forward_delay': int,
						'bridge_transmit_hold_count': int,
						'sys_id_ext': int,
						'interface': {
							Any(): {
								'name': str,
								'cost': int,
								'port_priority': int,
								'port_num': int,
								'role': str,
								'port_state': str,
								'designated_bridge_priority': int,
								'designated_bridge_address': str,
								'designated_port_priority': int,
								'designated_port_num': int,
								}
						}
					},
				}
			}
		}
	}

class ShowSpanningTreePvrst(ShowSpanningTreePvrstSchema):
	"""Parser for 'show spanning-tree pvrst <pvst_id>'"""
	cli_command = 'show spanning-tree pvrst {pvst_id}'
	def cli(self,pvst_id, output=None):
		if output is None:
			# get output from device
			out = self.device.execute(self.cli_command.format(pvst_id=pvst_id))
		else:
			out = output

		# initial return dictionary
		ret_dict = {}

		# VLAN 2:
		p1 = re.compile(r'^VLAN +(?P<vlan_id>\d+):$')
		# Root ID    Priority    32768
		p2 = re.compile(r'^Root\s+ID\s+Priority\s+'
			'(?P<designated_root_priority>\d+)')
		# Address     0021.1bff.d973
		p3 = re.compile(r'^Address\s+(?P<address>[\w\.]+)$')
		# Max Age 20 sec, Forward Delay 15 sec
		p4 = re.compile(r'^Max\s+Age\s+(?P<max_age>\d+)\s+sec,'
			'\s+Forward\s+Delay\s+(?P<forward_delay>\d+)\s+sec$')
		# Bridge ID  Priority    32768 (priority 32768 sys-id-ext 0)
		p5 = re.compile(r'^Bridge\s+ID\s+Priority\s+(?P<bridge_priority>\d+)'
			'(\s+\(priority\s+\d+\s+sys\-id\-ext\s+(?P<sys_id_ext>\d+)\))?')
		# Transmit Hold count   6
		p6 = re.compile(r'^Transmit\s+Hold\s+count\s+(?P<bridge_transmit_hold_count>\d+)')
		# Gi0/7/0/0	128.1   20000	 DSGN FWD   32768 8cb6.4fff.6588 128.1
		p7 = re.compile(r'^(?P<name>\S+)\s+(?P<port_priority>\d+)\.'
			'(?P<port_num>\d+)\s+(?P<cost>\d+)\s+(?P<role>\w+)\s+(?P<port_state>'
			'\w+)\s+(?P<designated_bridge_priority>\d+)\s+'
			'(?P<designated_bridge_address>[\w\.]+)\s+'
			'(?P<designated_port_priority>\d+)\.'
			'(?P<designated_port_num>\d+)$')

		for line in out.splitlines():
			line = line.strip()

			# VLAN 2:
			m = p1.match(line)
			if m:
				group = m.groupdict()
				pvst = ret_dict.setdefault('pvst', {}). \
					setdefault(pvst_id, {})
				pvst.update({'pvst_id' : pvst_id})
				vlans = pvst.setdefault('vlans', {})
				vlan = vlans.setdefault(int(group['vlan_id']), {})
				vlan.update({'vlan_id' : int(group['vlan_id'])})
				continue

		   	# Root ID    Priority    32768
			m = p2.match(line)
			if m:
				address_type = 'designated_root_address'
				group = m.groupdict()
				vlan.update({k:int(v) for k, v in group.items()})
				continue

		   	# Address     0021.1bff.d973
			m = p3.match(line)
			if m:
				group = m.groupdict()
				vlan.update({address_type : group['address']})
				continue

			# Max Age 20 sec, Forward Delay 15 sec
			m = p4.match(line)
			if m:
				group = m.groupdict()
				if address_type == 'designated_root_address':
					vlan.update({'designated_root_max_age' : int(group['max_age'])})
					vlan.update({
						'designated_root_forward_delay' : int(group['forward_delay'])})
				if address_type == 'bridge_address':
					vlan.update({'bridge_max_age' : int(group['max_age'])})
					vlan.update({
						'bridge_forward_delay' : int(group['forward_delay'])})
				continue

			# Bridge ID  Priority    32768 (priority 32768 sys-id-ext 0)
			m = p5.match(line)
			if m:
				address_type = 'bridge_address'
				group = m.groupdict()
				vlan.update({k:int(v) for k, v in group.items()})
				continue

			# Transmit Hold count   6
			m = p6.match(line)
			if m:
				group = m.groupdict()
				vlan.update({k:int(v) for k, v in group.items()})
				continue

			# Gi0/7/0/0	128.1   20000	 DSGN FWD   32768 8cb6.4fff.6588 128.1
			m = p7.match(line)
			if m:
				group = m.groupdict()
				interfaces = vlan.setdefault('interface' , {}). \
					setdefault(Common.convert_intf_name(group['name']), {})
				interfaces.update({'name' : Common.convert_intf_name(group['name'])})
				interfaces.update({'cost' : int(group['cost'])})
				interfaces.update({'role' : group['role']})
				interfaces.update({'port_priority' : int(group['port_priority'])})
				interfaces.update({'port_num' : int(group['port_num'])})
				interfaces.update({'port_state' : group['port_state']})
				interfaces.update({
					'designated_bridge_priority':int(group['designated_bridge_priority'])})
				interfaces.update({
					'designated_bridge_address':group['designated_bridge_address']})
				interfaces.update({
					'designated_port_priority':int(group['designated_port_priority'])})
				interfaces.update({
					'designated_port_num':int(group['designated_port_num'])})
				continue
		return ret_dict

"""Schema for 'show spanning-tree pvrstag <pvrstag_domain>'"""
class ShowSpanningTreePvrsTagSchema(MetaParser):
	schema = {
		'pvrstag': {
			Any(): {
				'domain': str,
				'interfaces': {
					Any(): {
						'interface': str,
						'vlans': {
							Any(): {
								'preempt_delay': bool,
								Optional('preempt_delay_state'): str,
								'sub_interface': str,
								'sub_interface_state': str,
								'max_age': int,
								'root_priority': int,
								'root_bridge': str,
								'root_cost': int,
								'bridge_priority': int,
								'bridge_id': str,
								'port_priority': int,
								'port_id': int,
								'hello_time': int,
								'active': bool,
								'counters': {
									'bdpu_sent': int,
									'topology_changes': int,
								}
							}
						}
					}
				}
			}
		},
	}

class ShowSpanningTreePvrsTag(ShowSpanningTreePvrsTagSchema):
	"""Parser for 'show spanning-tree pvrstag <pvrstag_domain>'"""
	cli_command = 'show spanning-tree pvrstag {pvrstag_domain}'
	exclude = [
		'hello_time',
		'bdpu_sent']
	def cli(self,pvrstag_domain, output=None):
		if output is None:
			# get output from device
			out = self.device.execute(self.cli_command.\
				format(pvrstag_domain=pvrstag_domain))
		else:
			out = output

		# initial return dictionary
		ret_dict = {}

		# VLAN 2:
		p1 = re.compile(r'^VLAN\s+(?P<vlan_id>\d+)$')
		# Pre-empt delay is enabled. Sending startup BPDU until 13:38:03
		# Pre-empt delay is enabled. Sending standard BPDU
		# Pre-empt delay is disabled
		p2 = re.compile(r'^Pre\-empt +delay +is +(?P<preempt_delay>\w+)'
			'\.?( +)?(?P<preempt_delay_state>Sending +'
			'(startup|standard) +BPDU( +until \S+)?)?')
		# Sub-interface:	GigabitEthernet0/0/0/1.5 (Up)
		# Sub-interface:	Bundle-Ether1000.2100 (Up)
		p3 = re.compile(r'^Sub\-interface:\s+(?P<sub_interface>\S+)\s+'
			'\((?P<sub_interface_state>\w+)\)$')
		# Max Age:			20
		p4 = re.compile(r'^Max\s+Age:\s+(?P<max_age>\d+)$')
		# Root Priority:    0
		p5 = re.compile(r'^Root\s+Priority:\s+(?P<root_priority>\d+)$')
		# Root Bridge: 0000.0000.0000
		p6 = re.compile(r'^Root\s+Bridge:\s+(?P<root_bridge>[\w\.]+)$')
		# Cost:             1
		p7 = re.compile(r'^Cost:\s+(?P<root_cost>\d+)$')
		# Bridge Priority:  32768
		p8 = re.compile(r'^Bridge\s+Priority:\s+(?P<bridge_priority>\d+)$')
		# Bridge ID:        0255.1dff.3c70
		p9 = re.compile(r'^Bridge\s+ID:\s+(?P<bridge_id>[\w\.]+)$')
		# Port Priority:    128
		p10 = re.compile(r'^Port\s+Priority:\s+(?P<port_priority>\d+)$')
		# Port ID           1
		p11 = re.compile(r'^Port\s+ID:?\s+(?P<port_id>\d+)$')
		# Hello Time:       2
		p12 = re.compile(r'^Hello\s+Time:\s+(?P<hello_time>\d+)$')
		# Active:           Yes
		p13 = re.compile(r'^Active:\s+(?P<active>\w+)$')
		# BPDUs sent:       6
		p14 = re.compile(r'^BPDUs\s+sent:\s+(?P<bdpu_sent>\d+)$')
		# Topology Changes: 0
		p15 = re.compile(r'^Topology\s+Changes:\s+(?P<topology_changes>\d+)$')
		# GigabitEthernet0/0/0/1
		p16 = re.compile(r'^(?P<interface>\S+)$')


		for line in out.splitlines():
			line = line.strip()

			# VLAN 2
			m = p1.match(line)
			if m:
				group = m.groupdict()
				vlan = vlans.setdefault(group['vlan_id'], {})
				continue
			# Pre-empt delay is enabled. Sending startup BPDU until 13:38:03
			# Pre-empt delay is enabled. Sending standard BPDU
			# Pre-empt delay is disabled
			m = p2.match(line)
			if m:
				group = m.groupdict()
				preempt_delay = group['preempt_delay']
				vlan.update({'preempt_delay': (preempt_delay == 'enabled')})
				if group['preempt_delay_state']:
					vlan.update({
						'preempt_delay_state' : group['preempt_delay_state']})
				continue
			# Sub-interface:	GigabitEthernet0/0/0/1.5 (Up)
			# Sub-interface:	Bundle-Ether1000.2100 (Up)
			m = p3.match(line)
			if m:
				group = m.groupdict()
				vlan.update({k:v for k, v in group.items()})
				continue
			# Max Age:			20
			m = p4.match(line)
			if m:
				group = m.groupdict()
				vlan.update({k:int(v) for k, v in group.items()})
				continue
			# Root Priority:    0
			m = p5.match(line)
			if m:
				group = m.groupdict()
				vlan.update({k:int(v) for k, v in group.items()})
				continue
			# Root Bridge: 0000.0000.0000
			m = p6.match(line)
			if m:
				group = m.groupdict()
				vlan.update({k:v for k, v in group.items()})
				continue
			# Cost:             1
			m = p7.match(line)
			if m:
				group = m.groupdict()
				vlan.update({k:int(v) for k, v in group.items()})
				continue
			# Bridge Priority:  32768
			m = p8.match(line)
			if m:
				group = m.groupdict()
				vlan.update({k:int(v) for k, v in group.items()})
				continue
			# Bridge ID:        0255.1dff.3c70
			m = p9.match(line)
			if m:
				group = m.groupdict()
				vlan.update({k:v for k, v in group.items()})
				continue
			# Port Priority:    128
			m = p10.match(line)
			if m:
				group = m.groupdict()
				vlan.update({k:int(v) for k, v in group.items()})
				continue
			# Port ID           1
			m = p11.match(line)
			if m:
				group = m.groupdict()
				vlan.update({k:int(v) for k, v in group.items()})
				continue
			# Hello Time:       2
			m = p12.match(line)
			if m:
				group = m.groupdict()
				vlan.update({k:int(v) for k, v in group.items()})
				continue
			# Active:           Yes
			m = p13.match(line)
			if m:
				group = m.groupdict()
				vlan.update({'active' : (group['active'].lower() == 'yes')})
				continue
			# BPDUs sent:       6
			m = p14.match(line)
			if m:
				group = m.groupdict()
				counters = vlan.setdefault('counters', {})
				counters.update({'bdpu_sent' : int(group['bdpu_sent'])})
				continue
			# Topology Changes: 0
			m = p15.match(line)
			if m:
				group = m.groupdict()
				counters = vlan.setdefault('counters', {})
				counters.update({
					'topology_changes' : int(group['topology_changes'])})
				continue
			# GigabitEthernet0/0/0/0
			m = p16.match(line)
			if m:
				group = m.groupdict()
				pvrstag = ret_dict.setdefault('pvrstag', {}). \
					setdefault(pvrstag_domain, {})
				pvrstag.update({'domain' : pvrstag_domain})
				interface = pvrstag.setdefault('interfaces', {}). \
					setdefault(Common.convert_intf_name(group['interface']), {})
				interface.update({
					'interface' : Common.convert_intf_name(group['interface'])})
				vlans = interface.setdefault('vlans', {})
				continue
		return ret_dict

"""Schema for 'show spanning-tree pvstag <pvstag_domain>'"""
class ShowSpanningTreePvsTagSchema(MetaParser):
	schema = {
		'pvstag': {
			Any(): {
				'domain': str,
				'interfaces': {
					Any(): {
						'interface': str,
						'vlans': {
							Any(): {
								'preempt_delay': bool,
								'sub_interface': str,
								'sub_interface_state': str,
								'max_age': int,
								'root_priority': int,
								'root_bridge': str,
								'root_cost': int,
								'bridge_priority': int,
								'bridge_id': str,
								'port_priority': int,
								'port_id': int,
								'hello_time': int,
								'active': bool,
								'counters': {
									'bdpu_sent': int,
									'topology_changes': int,
								}
							}
						}
					}
				}
			}
		},
	}

class ShowSpanningTreePvsTag(ShowSpanningTreePvsTagSchema):
	"""Parser for 'show spanning-tree pvstag <pvstag_domain>'"""
	cli_command = 'show spanning-tree pvstag {pvstag_domain}'
	exclude = [
		'hello_time',
		'bdpu_sent'
	]
	def cli(self,pvstag_domain, output=None):
		if output is None:
			# get output from device
			out = self.device.execute(self.cli_command.format(pvstag_domain=pvstag_domain))
		else:
			out = output

		# initial return dictionary
		ret_dict = {}

		# VLAN 2:
		p1 = re.compile(r'^VLAN\s+(?P<vlan_id>\d+)$')
		# Pre-empt delay is enabled. Sending startup BPDU until 13:38:03
		# Pre-empt delay is enabled. Sending standard BPDU
		# Pre-empt delay is disabled
		p2 = re.compile(r'^Pre\-empt +delay +is +(?P<preempt_delay>\w+)'
			'\.?( +Sending +(startup|standard) +BPDU( +until \S+)?)?')
		# Sub-interface:	GigabitEthernet0/0/0/1.5 (Up)
		# Sub-interface:	Bundle-Ether1000.2100 (Up)
		p3 = re.compile(r'^Sub\-interface:\s+(?P<sub_interface>\S+)'
			'\s+\((?P<sub_interface_state>\w+)\)$')
		# Max Age:			20
		p4 = re.compile(r'^Max\s+Age:\s+(?P<max_age>\d+)$')
		# Root Priority:    0
		p5 = re.compile(r'^Root\s+Priority:\s+(?P<root_priority>\d+)$')
		# Root Bridge: 0000.0000.0000
		p6 = re.compile(r'^Root\s+Bridge:\s+(?P<root_bridge>[\w\.]+)$')
		# Cost:             1
		p7 = re.compile(r'^Cost:\s+(?P<root_cost>\d+)$')
		# Bridge Priority:  32768
		p8 = re.compile(r'^Bridge\s+Priority:\s+(?P<bridge_priority>\d+)$')
		# Bridge ID:        0255.1dff.3c70
		p9 = re.compile(r'^Bridge\s+ID:\s+(?P<bridge_id>[\w\.]+)$')
		# Port Priority:    128
		p10 = re.compile(r'^Port\s+Priority:\s+(?P<port_priority>\d+)$')
		# Port ID           1
		p11 = re.compile(r'^Port\s+ID:?\s+(?P<port_id>\d+)$')
		# Hello Time:       2
		p12 = re.compile(r'^Hello\s+Time:\s+(?P<hello_time>\d+)$')
		# Active:           Yes
		p13 = re.compile(r'^Active:\s+(?P<active>\w+)$')
		# BPDUs sent:       6
		p14 = re.compile(r'^BPDUs\s+sent:\s+(?P<bdpu_sent>\d+)$')
		# Topology Changes: 0
		p15 = re.compile(r'^Topology\s+Changes:\s+(?P<topology_changes>\d+)$')
		# GigabitEthernet0/0/0/1
		p16 = re.compile(r'^(?P<interface>\S+)$')


		for line in out.splitlines():
			line = line.strip()

			# VLAN 2
			m = p1.match(line)
			if m:
				group = m.groupdict()
				vlan = vlans.setdefault(group['vlan_id'], {})
				continue
			# Pre-empt delay is enabled. Sending startup BPDU until 13:38:03
			# Pre-empt delay is enabled. Sending standard BPDU
			# Pre-empt delay is disabled
			m = p2.match(line)
			if m:
				group = m.groupdict()
				preempt_delay = group['preempt_delay']
				vlan.update({'preempt_delay': (preempt_delay == 'enabled')})
				continue
			# Sub-interface:	GigabitEthernet0/0/0/1.5 (Up)
			# Sub-interface:	Bundle-Ether1000.2100 (Up)
			m = p3.match(line)
			if m:
				group = m.groupdict()
				vlan.update({k:v for k, v in group.items()})
				continue
			# Max Age:			20
			m = p4.match(line)
			if m:
				group = m.groupdict()
				vlan.update({k:int(v) for k, v in group.items()})
				continue
			# Root Priority:    0
			m = p5.match(line)
			if m:
				group = m.groupdict()
				vlan.update({k:int(v) for k, v in group.items()})
				continue
			# Root Bridge:      0000.0000.0000
			m = p6.match(line)
			if m:
				group = m.groupdict()
				vlan.update({k:v for k, v in group.items()})
				continue
			# Cost:             0
			m = p7.match(line)
			if m:
				group = m.groupdict()
				vlan.update({k:int(v) for k, v in group.items()})
				continue
			# Bridge Priority:  32768
			m = p8.match(line)
			if m:
				group = m.groupdict()
				vlan.update({k:int(v) for k, v in group.items()})
				continue
			# Bridge ID:        6c9c.edff.8d95
			m = p9.match(line)
			if m:
				group = m.groupdict()
				vlan.update({k:v for k, v in group.items()})
				continue
			# Port Priority:    128
			m = p10.match(line)
			if m:
				group = m.groupdict()
				vlan.update({k:int(v) for k, v in group.items()})
				continue
			# Port ID           1
			m = p11.match(line)
			if m:
				group = m.groupdict()
				vlan.update({k:int(v) for k, v in group.items()})
				continue
			# Hello Time:       2
			m = p12.match(line)
			if m:
				group = m.groupdict()
				vlan.update({k:int(v) for k, v in group.items()})
				continue
			# Active:           Yes
			m = p13.match(line)
			if m:
				group = m.groupdict()
				vlan.update({'active' : (group['active'].lower() == 'yes')})
				continue
			# BPDUs sent:       10
			m = p14.match(line)
			if m:
				group = m.groupdict()
				counters = vlan.setdefault('counters', {})
				counters.update({
					'bdpu_sent' : int(group['bdpu_sent'])})
				continue
			# Topology Changes: 0
			m = p15.match(line)
			if m:
				group = m.groupdict()
				counters = vlan.setdefault('counters', {})
				counters.update({
					'topology_changes' : int(group['topology_changes'])})
				continue
			# Bundle-Ether1000
			m = p16.match(line)
			if m:
				group = m.groupdict()
				pvrstag = ret_dict.setdefault('pvstag', {}). \
					setdefault(pvstag_domain, {})
				pvrstag.update({'domain' : pvstag_domain})
				interface = pvrstag.setdefault('interfaces', {}). \
					setdefault(
						Common.convert_intf_name(group['interface']), {})
				interface.update(
					{'interface' : Common.convert_intf_name(group['interface'])})
				vlans = interface.setdefault('vlans', {})
				continue

		return ret_dict
