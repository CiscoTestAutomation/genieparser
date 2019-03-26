'''show_service.py
IOSXE parser for the following show command
	* show service-group state
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
												Any

# ==============================================================
# Parser for 'show service-group state'
# ==============================================================
class ShowServiceGroupStateSchema(MetaParser):
	"""
	Schema for show service-group state
	"""

	schema = {
		'group': {
			Any() : {
				'state' : str
			}
		}
	}

class ShowServiceGroupState(ShowServiceGroupStateSchema):
	"""
	Parser for 'show service-group state'
	"""

	cli_command = 'show service-group state'
	
	def cli(self, output= None):
		if output is None:
			#execute command to get output
			out = self.device.execute(self.cli_command)
		else:
			out = output

		# initial variables
		ret_dict = {}

		#     1            Up
		p1 = re.compile(r'^\s*(?P<group_number>\d+) +(?P<state>\S+)$')

		for line in out.splitlines():
			line = line.strip()
			#     1            Up
			m = p1.match(line)
			if m:
				group = m.groupdict()
				service_group_state = ret_dict.setdefault(
					'group', {}).setdefault(group['group_number'], {}). \
					setdefault('state' , group['state'])
				continue
				service_group_state
		return ret_dict
