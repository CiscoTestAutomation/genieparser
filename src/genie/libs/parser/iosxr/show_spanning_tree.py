"""show_spanning_tree.py
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

class ShowSpanningTreeMstSchema(MetaParser):
	schema = {
		'mst_instances': {
			Any(): {
				'mst_id': str,
				'vlan': str,
                'bridge_priority': int,
                'bridge_address': str,
                'bridge_max_age': int,
                'bridge_forward_delay': int,
                'bridge_max_hops': int,
                'bridge_transmit_hold_count': int, 
                'designated_root_priority': int,
                'designated_root_address': str,
                'root_cost': int,
                'root_max_age': int,
                'root_forward_delay': int,
                'cist_root_priority': int,
                'cist_root_address': str,
                'cist_root_cost': int,
                'sys_id_ext': int,
                'interfaces': {
	                Any(): {
			            'name':str,
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
			}
		}
	}


class ShowSpanningTreePvrstSchema(MetaParser):
	schema = {
		'pvst': {
			Any(): {
				'pvst_id': str,
				'vlans': {
					Any(): {
						'vlan_id': int,
						'designated_root_priority': int,
						'designated_root_address': int,
						'designated_root_max_age': int,
						'designated_root_forward_delay': int,
						'bridge_priority': int,
						'bridge_address': str,
						'bridge_forward_delay': int,
						'bridge_transmit_hold_count': int,
						'sys_id_ext': int,
					},
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
				}
			}
		}
	}

class ShowSpanningTreePvrstagSchema(MetaParser):
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
								'active': str,
								'counters': {
									'bdpu_sent': int,
									'topology_changes': int,
								}
							}
						}
					}
				}
			}
		}
	}

class ShowSpanningTreeMst(ShowSpanningTreeMstSchema):
	"""Parser for 'show spanning-tree mst <mst_id>'"""
	cli_command = 'show spanning-tree mst {mst_id}'
	def cli(self,output=None):
		if output is None:
		    # get output from device
		    out = self.device.execute(self.cli_command)
		else:
		    out = output

		# initial return dictionary
		ret_dict = {}

		# MSTI 0 (CIST):
		p1 = re.compile(r'^MSTI +(?P<mst_id>\d+)([\s\S]+)?:$')
		# VLANS Mapped: 1-4094
		p2 = re.compile(r'^VLANS +Mapped: +(?P<vlan>\S+)$')
		# CIST Root  Priority    32768
		p3 = re.compile(r'^CIST\s+Root\s+Priority\s+(?P<cist_root_priority>\d+)')
		# Address     0021.1bfd.1007
		p4 = re.compile(r'^Address\s+(?P<address>[\w\.]+)$')
		# Ext Cost    2000
		p5 = re.compile(r'^Ext\s+Cost\s+(?P<cist_root_cost>\d+)$')
		# Root ID    Priority    32768
		p6 = re.compile(r'^Root\s+ID\s+Priority\s+(?P<designated_root_priority>\d+)')
		# Int Cost    0
		p7 = re.compile(r'^Int\s+Cost\s+(?P<root_cost>\d+)$')
		# Max Age 20 sec, Forward Delay 15 sec
		p8 = re.compile(r'^Max\s+Age\s+(?P<max_age>\d+)\s+sec,\s+Forward\s+Delay\s+(?P<forward_delay>\d+)\s+sec$')
		# Max Hops 20, Transmit Hold count    6
		p9 = re.compile(r'^Max\s+Hops\s+(?P<bridge_max_hops>\d+),\s+Transmit\s+Hold\s+count\s+(?P<bridge_transmit_hold_count>\d+)$')
		# Bridge ID Priority 32768 (priority 32768 sys-id-ext 0)
		p10 = re.compile(r'^Bridge\s+ID\s+Priority\s+(?P<bridge_priority>\d+)(\s+\(priority\s+\d+\s+sys\-id\-ext\s+(?P<sys_id_ext>\d+)\))?')
		# Te0/0/0/16   128.1   2000      ROOT FWD   32768 0021.1bfd.1007 128.1
		p11 = re.compile(r'^(?P<name>\S+)\s+(?P<port_num>\d+)\.(?P<port_priority>\d+)\s+(?P<cost>\d+)\s+(?P<role>\w+)\s+(?P<port_state>\w+)\s+(?P<designated_bridge_priority>\d+)\s+(?P<designated_bridge_address>[\w\.]+)\s+(?P<designated_port_num>\d+)\.(?P<designated_port_priority>\d+)$')

		for line in out.splitlines():
		    line = line.strip()

		    # MSTI 0 (CIST):
		    m = p1.match(line)
		    if m:
		    	group = m.groupdict()
		    	mst_id = group['mst_id']
		    	mst_instances = ret_dict.setdefault('mst_instances', {}).setdefault(mst_id, {})
		    	mst_instances.update({'mst_id' : mst_id})
		    	continue

		    # VLANS Mapped: 1-4094
		    m = p2.match(line)
		    if m:
		    	group = m.groupdict()
		    	mst_instances.update({'vlan' : group['vlan']})
		    	continue

		    # CIST Root  Priority    32768
		    m = p3.match(line)
		    if m:
		    	address_type = 'cist_root_address'
		    	group = m.groupdict()
		    	mst_instances.update({k:int(v) for k, v in group.items()})
		    	continue

		   	# Address     0021.1bfd.1007
		    m = p4.match(line)
		    if m:
		    	group = m.groupdict()
		    	mst_instances.update({address_type : group['address']})
		    	continue
		    
		    # Ext Cost    2000
		    m = p5.match(line)
		    if m:
		    	group = m.groupdict()
		    	mst_instances.update({k:int(v) for k, v in group.items()})
		    	continue

		    # Root ID    Priority    32768
		    m = p6.match(line)
		    if m:
		    	address_type = 'designated_root_address'
		    	group = m.groupdict()
		    	mst_instances.update({k:int(v) for k, v in group.items()})
		    	continue

		    # Int Cost    0
		    m = p7.match(line)
		    if m:
		    	group = m.groupdict()
		    	mst_instances.update({k:int(v) for k, v in group.items()})
		    	continue

		    # Max Age 20 sec, Forward Delay 15 sec
		    m = p8.match(line)
		    if m:
		    	group = m.groupdict()
		    	if address_type is 'designated_root_address':
		    		mst_instances.update({'root_max_age' : int(group['max_age'])})
		    		mst_instances.update({'root_forward_delay' : int(group['forward_delay'])})
		    	if address_type is 'bridge_address':
		    		mst_instances.update({'bridge_max_age' : int(group['max_age'])})
		    		mst_instances.update({'bridge_forward_delay' : int(group['forward_delay'])})
		    	continue

		    # Max Hops 20, Transmit Hold count    6
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

		    # Te0/0/0/16   128.1   2000      ROOT FWD   32768 0021.1bfd.1007 128.1
		    m = p11.match(line)
		    if m:
		    	group = m.groupdict()
		    	interfaces = mst_instances.setdefault('interfaces' , {}). \
		    		setdefault(group['name'], {})
		    	interfaces.update({'name' : group['name']})
		    	interfaces.update({'cost' : int(group['cost'])})
		    	interfaces.update({'role' : group['role']})
		    	interfaces.update({'port_priority' : int(group['port_priority'])})
		    	interfaces.update({'port_num' : int(group['port_num'])})
		    	interfaces.update({'port_state' : group['port_state']})
		    	interfaces.update({'designated_bridge_priority' : int(group['designated_bridge_priority'])})
		    	interfaces.update({'designated_bridge_address' : group['designated_bridge_address']})
		    	interfaces.update({'designated_port_priority' : int(group['designated_port_priority'])})
		    	interfaces.update({'designated_port_num' : int(group['designated_port_num'])})
		    	continue
		return ret_dict

class ShowSpanningTreeMstagSchema(MetaParser):
	schema = {
		'mstag': {
			Any(): {
				'domain': str,
				'interfaces': {
					Any(): {
						'interface': str,
						'preempt_delay': bool,
						'preempt_delay_state': str,
						'name': str,
						'revision': int,
						'max_age': int,
						'provider_bridge': str,
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

	def cli(self,mag_domain, output=None):
		if output is None:
		    # get output from device
		    out = self.device.execute(self.cli_command.format(mag_domain=mag_domain))
		else:
		    out = output

		# initial return dictionary
		ret_dict = {}

		# Bundle-Ether10.0
		p1 = re.compile(r'^Bundle\-(?P<mag_interface>\S+)$$')
		# Pre-empt delay is disabled
		p2 = re.compile(r'^Pre\-empt +delay +is +(?P<preempt_delay_state>\w+)$')
		# Name:            risc
		p3 = re.compile(r'^Name: (\S+)$')
		# Revision: 1
		p4 = re.compile(r'^Revision: +(?P<revision>\d+)$')
		# Max Age: 20
		p5 = re.compile(r'^Max Age: +(?P<max_age>\d+)$')
		# Provider Bridge: no
		p6 = re.compile(r'^Provider +Bridge: +(?P<provider_bridge>\w+)$')
		# Bridge ID:       0000.0000.0002
		p7 = re.compile(r'^Bridge +ID: +(?P<bridge_id>[\w\.]+)$')
		# Port ID:         1
		p8 = re.compile(r'^Port +ID: +(?P<port_id>\d+)$')
		# External Cost:   0
		p9 = re.compile(r'^External +Cost: +(?P<external_cost>\d+)$')
		# Hello Time:      2
		p10 = re.compile(r'^Hello +Time: +(?P<hello_time>\d+)$')
		# Active:          yes
		p11 = re.compile(r'^Active: +(?P<active>\w+)$')
		# BPDUs sent:      39921
		p12 = re.compile(r'^BPDUs +sent: +(?P<bdpu_sent>\d+)$')
		# MSTI 0 (CIST):
		p13 = re.compile(r'^MSTI +(?P<mst_id>\d+)( +\(CIST\))?:$')
		#     VLAN IDs:         1-2,4-4094
		p14 = re.compile(r'^VLAN +IDs: +(?P<vlans>\S+)$')
		#     Bridge Priority:  8192
		p15 = re.compile(r'^Bridge +Priority: +(?P<bridge_priority>\d+)$')
		#     Port Priority:    128
		p16 = re.compile(r'^Port +Priority: +(?P<port_priority>\d+)$')
		#     Cost:             0
		p17 = re.compile(r'^Cost: +(?P<cost>\d+)$')
		#     Root Bridge:      0000.0000.0001
		p18 = re.compile(r'^Root +Bridge: +(?P<root_bridge>[\w\.]+)$')
		#     Root Priority:    4096
		p19 = re.compile(r'^Root +Priority: +(?P<root_priority>\d+)$')
		#     Topology Changes: 31
		p20 = re.compile(r'^Topology +Changes: +(?P<topology_changes>\d+)$')

		for line in out.splitlines():
            line = line.strip()

            # Bundle-Ether10.0
            m = p1.match(line)
            if m:
            	group = m.groupdict()
            	mstag = ret_dict.setdefault('mstag', {}).\
            		.setdefault(mag_domain, {})
            	mstag.update({'domain' : mag_domain})
            	interface = mstag.setdefault('interfaces', {}).\
            		.setdefault(group['mag_interface'], {})
            	interface.update({'interface' : group['mag_interface']})
            	continue

            # Pre-empt delay is disabled
            m = p2.match(line)
            if m:
            	group = m.groupdict()
            	preempt_delay_state = group['preempt_delay_state']
        		interface.update({'preempt_delay' : (preempt_delay_state != 'disabled')})
        		interface.update({'preempt_delay_state' : preempt_delay_statee})
            	continue
            # Name:            risc
           	m = p3.match(line)
           	if m:
           		group = m.groupdict()
           		interface.update({'name' : group['name']})
           		continue

           	# Name:            risc
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
           		interface.update({k:v for k, v in group.items()})
           		continue

           	# Bridge ID:       0000.0000.0002
           	m = p7.match(line)
           	if m:
           		group = m.groupdict()
           		interface.update({k:v for k, v in group.items()})
           		continue

           	# Port ID:         1
           	m = p8.match(line)
           	if m:
           		group = m.groupdict()
           		interface.update({k:int(v) for k, v in group.items()})
           		continue

           	# External Cost:   0
           	m = p9.match(line)
           	if m:
           		group = m.groupdict()
           		interface.update({k:int(v) for k, v in group.items()})
           		continue

           	# Hello Time:      2
           	m = p10.match(line)
           	if m:
           		group = m.groupdict()
           		interface.update({k:int(v) for k, v in group.items()})
           		continue

           	# Active:          yes
           	m = p11.match(line)
           	if m:
           		group = m.groupdict()
           		interface.update({'active': (group['active'] == 'yes')})
           		continue

           	# BPDUs sent:      39921
           	m = p12.match(line)
           	if m:
           		group = m.groupdict()
           		bdpu_sent = {'bdpu_sent' : group['bdpu_sent']}
           		interface.update({'counters': bdpu_sent})
           		continue

           	# MSTI 0 (CIST):
           	m = p13.match(line)
           	if m:
           		group = m.groupdict()
           		instances = interface.setdefault('instances', {}).\
           			setdefault(group['mst_id'], {})
           		instances.update({'instance': group['mst_id']})
           		continue

           	#     VLAN IDs:         1-2,4-4094
           	m = p14.match(line)
           	if m:
           		group = m.groupdict()
           		instances.update({k:v for k, v in group.items()})
           		continue

           	#     Bridge Priority:  8192
           	m = p15.match(line)
           	if m:
           		group = m.groupdict()
           		instances.update({k:int(v) for k, v in group.items()})
           		continue

           	#     Port Priority:    128
           	m = p16.match(line)
           	if m:
           		group = m.groupdict()
           		instances.update({k:int(v) for k, v in group.items()})
           		continue

           	#     Cost:             0
           	m = p17.match(line)
           	if m:
           		group = m.groupdict()
           		instances.update({k:int(v) for k, v in group.items()})
           		continue

           	#     Root Bridge:      0000.0000.0001
           	m = p18.match(line)
           	if m:
           		group = m.groupdict()
           		instances.update({k:v for k, v in group.items()})
           		continue

           	#     Root Priority:    4096
           	m = p19.match(line)
           	if m:
           		group = m.groupdict()
           		instances.update({k:int(v) for k, v in group.items()})
           		continue

           	#     Topology Changes: 31
           	m = p20.match(line)
           	if m:
           		group = m.groupdict()
           		topology_changes = {'topology_changes' : group['topology_changes']}
           		instances.update({'counters': topology_changes})
           		continue
        
        return ret_dict












