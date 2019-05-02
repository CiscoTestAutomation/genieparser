'''
show_ip.py

IOSXE parsers for the following show commands:
    * show ip alias
	* show ip aliases default-vrf
	* show ip aliases vrf {vrf}
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional

# parser utils
from genie.libs.parser.utils.common import Common

# ==============================
# Schema for 'show ip alias', 'show ip aliases default-vrf', 'show ip aliases vrf {vrf}'
# ==============================
class ShowIPAliasSchema(MetaParser):
    ''' 
	Schema for:
	show ip alias 
	show ip aliases default-vrf
	sshow ip aliases vrf {vrf}
	'''
    schema = {
        'vrf': {
            Any(): {
                'index': {
                    Any(): { # just incrementing 1, 2, 3, ... per entry
                        'address_type': str,
                        'ip_address': str,
                        Optional('port'): int,
                    },
                },
            },
        },
    }

# ==============================
# Parser for 'show ip alias', 'show ip aliases default-vrf', 'show ip aliases vrf {vrf}'
# ==============================
class ShowIPAlias(ShowIPAliasSchema):
	''' 
	Parser for:
	show ip alias 
	show ip aliases default-vrf
	show ip aliases vrf {vrf}
	'''
	cli_command = ['show ip alias', 'show ip aliases default-vrf', 'show ip aliases vrf {vrf}']

	def cli(self, vrf = '', output = None):
		if output is None:
			out = self.device.execute(self.cli_command)
		else:
			out = output
 
		# Init vars
		parsed_dict = {}

		print("Address Type             IP Address      Port")

		# Address Type             IP Address      Port
		# Interface                106.162.197.94
		p1 = re.compile(r'(?P<address_type>(\S+)) +(?P<ip_address>(\S+)) +(?P<port>(\d+))$')
		
		for line in out.splitlines():
			line = line.strip()
 
			# Interface                106.162.197.94
			m = p1.match(line)
			if m:
				group = m.groupdict()
				
				vrf = group['vrf']
				vrf_dict = parsed_dict.setdefault('vrf', {}).setdefault(vrf, {}).setdefault('index', {})

				address_type = group['address_type']
				address_type_dict = vrf_dict.setdefault('address_type', {}).setdefault(address_type, {})
				address_type_dict['ip_address'] = group['ip_address']
				address_type_dict['port'] = int(group['port'])
				
				continue

		return parsed_dict
