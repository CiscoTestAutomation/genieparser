from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any
import re

# ======================================================
# Schema for 'show router arp dynamic'
# ======================================================

class ShowRouterArpDynamicSchema(MetaParser):
	"""Schema for show router arp dynamic"""
	schema = {
		'router': {
			Any(): {
				"entries" : int,
				'ip_address': {
					Any(): {
						'interface': str,
						'mac_add': str,
						'expiry': str,
						'type':str
					}
				}
			}
		}
	}

class ShowRouterArpDynamic(ShowRouterArpDynamicSchema):
	""" Parser for show router arp dynamic """
	cli_command = 'show router arp dynamic'

	def cli(self, output=None):

		if output is None:
			out = self.device.execute(self.cli_command)
		else:
			out = output
		
		parsed_dict = {}

		#ARP Table Router: (Base)
		p0 = re.compile(r'^ARP Table Router: \((?P<router>\S+)\)$')

		#No. of ARP Entries: 4
		p1 = re.compile(r'^No. of ARP Entries: (?P<entries>\d+)$')

		#10.4.1.1         00:fe:c8:ff:db:6d 02h34m12s Dyn[I] To-ASR5.5K
		p2 = re.compile(r'^(?P<ip_address>\S+) +(?P<mac_add>\S+) +(?P<expiry>\S+) +(?P<type>\S+) +(?P<interface>\S+)$')
		
		for line in out.splitlines():
			line= line.strip()

			#ARP Table Router: (Base)
			m = p0.match(line)
			if m:
				router_dict = parsed_dict.setdefault('router', {}).setdefault(m.groupdict()['router'], {})
				continue

			#No. of ARP Entries: 4
			m = p1.match(line)
			if m:
				router_dict["entries"] = int(m.groupdict()['entries'])
				continue
			
			#10.4.1.1         00:fe:c8:ff:db:6d 02h34m12s Dyn[I] To-ASR5.5K
			m = p2.match(line)
			if m:
				group = m.groupdict()
				ip_address = group['ip_address']
				mac_add = group['mac_add']
				expiry = group['expiry']
				type_mac = group['type']
				interface = group['interface']
				
				interface_dict = router_dict.setdefault('ip_address', {}).setdefault(ip_address, {})
				
				interface_dict["interface"] = interface
				interface_dict["mac_add"] = mac_add
				interface_dict["expiry"] = expiry
				interface_dict["type"] = type_mac
				continue

		return parsed_dict