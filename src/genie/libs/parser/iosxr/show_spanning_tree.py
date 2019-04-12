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
                'root_hops': int,
                'root_transmit_hold_count': int,
                'cist_root_priority': int,
                'cist_root_address': str,
                'cist_root_cost': int,
                'interfaces': {
	                Any(): {
			            'name':str,
			            'cost': int, 
			            'port_priority': int, 
			            'port_num': int, 
			            'role': str, 
			            'port_state': str,
			            'designated_bridge_priority': int,
			            'designated_bridge_address': int,
			            'designated_port_priority': int,
			            'designated_port_num': int,
			        }
			    }
			}
		}
	}

class ShowSpanningTreeMstagSchema(MetaParser):
	schema = {
		'mstag': {
			Any(): {
				'domain': str,
				'interfaces': {
					Any(): {
						'interface': str,
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
		p6 = re.compile(r'^Root\s+ID +Priority\s+(?P<cist_root_priority>\d+)')
		# Int Cost    0
		p7 = re.compile(r'^Int\s+Cost\s+(?P<root_cost>\d+)$')
		# Max Age 20 sec, Forward Delay 15 sec
		p8 = re.compile(r'^Max\s+Age\s+(?P<max_age>\d+)\s+sec,\s+Forward\s+Delay\s+(?P<forward_delay>\d+)\s+sec$')
		# Max Hops 20, Transmit Hold count    6
		p9 = re.compile(r'^Max\s+Hops\s+(?P<root_hops>\d+),\s+Transmit\s+Hold\s+count\s+(?P<root_transmit_hold_count>\d+)$')
		# Te0/0/0/16   128.1   2000      ROOT FWD   32768 0021.1bfd.1007 128.1
		p10 = re.compile(r'^(?P<name>\S+)\s+(?P<port_num>\d+)\.(?P<port_priority>\d+)\s+(?P<cost>\d+)\s+(?P<role>\w+)\s+(?P<port_state>\w+)\s+(?P<designated_bridge_priority>\d+)\s+(?P<designated_bridge_address>[\w\.]+)\s+(?P<designated_port_num>\d+)\.(?P<designated_port_priority>\d+)$')

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
		    	group = m.groupdict()
		    	mst_instances.update({k:int(v) for k, v in group.items()})
		    	continue

		   	# Address     0021.1bfd.1007
		    m = p4.match(line)
		    if m:
		    	group = m.groupdict()

		    	if mst_instances.get('cist_root_priority', None) is not None and mst_instances.get('cist_root_address', None) is None:
		    		mst_instances.update({'cist_root_address' : group['address']})
		    	else:
		    		mst_instances.update({k:v for k, v in group.items()})
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
		    	group = m.groupdict()
		    	mst_instances.update({k:v for k, v in group.items()})
		    	continue

		    # Int Cost    0
		    m = p7.match(line)
		    if m:
		    	group = m.groupdict()
		    	mst_instances.update({k:v for k, v in group.items()})
		    	continue

		    # Max Age 20 sec, Forward Delay 15 sec
		    m = p8.match(line)
		    if m:
		    	group = m.groupdict()
		    	mst_instances.update({k:int(v) for k, v in group.items()})
		    	continue

		    # Max Hops 20, Transmit Hold count    6
		    m = p9.match(line)
		    if m:
		    	group = m.groupdict()
		    	mst_instances.update({k:int(v) for k, v in group.items()})
		    	continue

		    # Te0/0/0/16   128.1   2000      ROOT FWD   32768 0021.1bfd.1007 128.1
		    m = p10.match(line)
		    if m:
		    	group = m.groupdict()
		    	interfaces = mst_instances.setdefault('interfaces' , {}). \
		    		setdefault(group['name'], {})
		    	interfaces.update({k:v for k, v in group.items()})
		    	continue
		from genie.libs.parser.utils.common import format_output
		print(format_output(ret_dict))
		return ret_dict


class ShowSpanningTreeMstag(ShowSpanningTreeMstagSchema):
	"""Parser for 'show spanning-tree mstag <mag_domain>'"""
	cli_command = 'show spanning-tree mstag {mag_domain}'