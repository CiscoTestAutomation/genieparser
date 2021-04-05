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
				'interfaces': {
					Any(): {
						'ip_add': str,
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
		p0 = re.compile(r'^ARP Table Router: \((?P<router>\S+)\)$')
		p1 = re.compile(r'^No. of ARP Entries: (?P<entries>\d+)$')
		p2 = re.compile(r'^(?P<ip_add>\S+) +(?P<mac_add>\S+) +(?P<expiry>\S+) +(?P<type>\S+) +(?P<interface>\S+)$')
		
		for line in out.splitlines():
			
			m = p0.match(line)
			if m:
				router_dict = parsed_dict.setdefault('router', {}).setdefault(m.groupdict()['router'], {})
				continue
			m = p1.match(line)
			if m:
				router_dict["entries"] = int(m.groupdict()['entries'])
				continue
			
			m = p2.match(line)
			if m:
				group = m.groupdict()
				ip_add = group['ip_add']
				mac_add = group['mac_add']
				expiry = group['expiry']
				type_mac = group['type']
				interface = group['interface']
				
				interface_dict = router_dict.setdefault('interfaces', {}).setdefault(interface, {})
				
				interface_dict["ip_add"] = ip_add
				interface_dict["mac_add"] = mac_add
				interface_dict["expiry"] = expiry
				interface_dict["type"] = type_mac
				continue

		return parsed_dict