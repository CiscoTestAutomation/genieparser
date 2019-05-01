# Python
import re
 
# ==============================
# Parser for 'show ip alias'
# ==============================
class ShowIPAlias(ShowIPAliasSchema):
	''' Parser for "show ip alias"'''

	cli_command = 'show ip alias'

	def cli(self, output = None):
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
				ip_alias = group['ip_alias']
				ip_alias_dict = parsed_dict.setdefault('ip_alias', {}).setdefault(ip_alias, {})
				ip_alias_dict['address_type'] = group['address_type']
				ip_alias_dict['ip_address'] = group['ip_address']
				ip_alias_dict['port'] = int(group['port'])
				continue

		return parsed_dict