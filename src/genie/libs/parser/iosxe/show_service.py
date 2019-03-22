"""show_service.py
     *  show service-group stats
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any

# import parser utils
from genie.libs.parser.utils.common import Common

# ==============================================================
# Parser for 'show service-group stats'
# ==============================================================
class ShowServiceGroupStatsSchema(MetaParser):
	"""
	Schema for show service-group stats
	"""

	schema = {
		'service_group_statistics':{
			'global': {
			'num_of_groups' : int,
			'num_of_members' : int
			},
			Any() : {
				'num_of_interfaces' : int,
				'num_of_members' : int,
				Any(): int,
				'members_joined': int,
				'members_left': int
			}
		}
	}

class ShowServiceGroupStats(ShowServiceGroupStatsSchema):
	""" Parser for 'show service-group stats"""

	cli_command = 'show service-group stats'
	
	def cli(self, output= None):
		if output is None:
			#execute command to get output
			out = self.device.execute(self.cli_command)
		else:
			out = output

		# initial variables
		ret_dict = {}
		global_statistics_found = False
		group_statistics_found = False

		# Service Group global statistics:
		p1 = re.compile(r'^\s*Service +Group +global +statistics:$')

		# Number of groups:          1
		p2 = re.compile(r'^\s*Number +of +groups: +(?P<num_of_groups>\d+)$')

		# Number of members:
		p3 = re.compile(r'^\s*Number +of +members: +(?P<num_of_members>\d+)$')

		# Service Group 1 statistics:
		p4 = re.compile(r'^\s*Service +Group +(?P<group_statistics>\d+) +statistics:$')

		# Number of Interfaces:      1
		p5 = re.compile(r'^\s*Number +of +Interfaces: +(?P<num_of_interfaces>\d+)$')

		#  Number of members:         2
		p6 = re.compile(r'^\s*Number +of +members: +(?P<num_of_members>\d+)$')

		#    Sub-interface:           2
		p7 = re.compile(r'^\s*(?P<interface_name>[\S\s]+): +(?P<sub_interface>\d+)$')

		# Members joined:            103
		p8 = re.compile(r'^\s*Members +joined: +(?P<members_joined>\d+)$')

		# Members left:              101
		p9 = re.compile(r'^\s*Members +left: +(?P<members_left>\d+)$')

		for line in out.splitlines():
			line = line.strip()
			if not global_statistics_found:
				# Service Group global statistics:
				m = p1.match(line)
				if m:
					service_group_statistics = ret_dict.setdefault( \
						'service_group_statistics', {})
					global_statistics = service_group_statistics.setdefault( \
						'global', {})
					global_statistics_found = True
					group_statistics_found = False
					continue
			else:
				# Number of groups:          1
				m = p2.match(line)
				if m:
					group = m.groupdict()
					global_statistics.update({k:
						int(v) for k, v in group.items()})
					continue

 				# Number of members:         2
				m = p3.match(line)
				if m:
					group = m.groupdict()
					global_statistics.update({k:
						int(v) for k, v in group.items()})
					continue

			if not group_statistics_found:
            	# Service Group 1 statistics:
				m = p4.match(line)
				if m:
					group = m.groupdict()
					group_statistics = service_group_statistics.setdefault( \
						group['group_statistics'], {})
					group_statistics_found = True
					global_statistics_found = False
					continue

			else:
				# Number of Interfaces:          1
				m = p5.match(line)
				if m:
					group = m.groupdict()
					group_statistics.update({k:
						int(v) for k, v in group.items()})
					continue

 				# Number of members:         2
				m = p6.match(line)
				if m:
					group = m.groupdict()
					group_statistics.update({k:
						int(v) for k, v in group.items()})
					continue

                # Members joined:         103
				m = p8.match(line)
				if m:
					group = m.groupdict()
					group_statistics.update({k:
						int(v) for k, v in group.items()})
					continue

                # Members left:         101
				m = p9.match(line)
				if m:
					group = m.groupdict()
					group_statistics.update({k:
						int(v) for k, v in group.items()})
					group_statistics_found = False
					continue

				# Sub-Interface:         2
				m = p7.match(line)
				if m:
					group = m.groupdict()
					group_statistics.update(
						{group['interface_name']: int(group['sub_interface'])})
					continue
				
		return ret_dict