''' show_interface_summary.py

ASA parserr for the following show commands:
	* show interface summary
	* show interface ip brief
	* show interface details
'''
	

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional



# =============================================
# Parser for 'show interface summary'
# =============================================

class ShowInterfaceSummarySchema(MetaParser):
    """Schema for 
    	* show interface summary
    """

    schema = {
        'interfaces': {
            Any(): {
           			Optional('name'): str,
                    Optional('oper_status'): str,
                    Optional('protocol_status'): str,
                    Optional('mac_address'): str,
                    Optional('mtu'): int,
                    Optional('ip_address'): str,
                    Optional('subnet'): str 
	                },
	            }
	        }
	    

class showInterfaceSummary(ShowInterfaceSummarySchema):

    cli_command = 'show interface summary'
    def cli(self,output=None):
        if output is None:
            # excute command to get output
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}


        # Interface Vlan1000 "pod100", is up, line protocol is up
        p1 = re.compile(r'^Interface +(?P<interface>\w+) +"(?P<name>\w+)", is (?P<oper_status>(up|down)), line protocol is (?P<protocol_status>(up|down))$')
        
        # MAC address 286f.7fb1.032c, MTU 1500
        p2 = re.compile(r'^MAC address +(?P<mac_address>[\w\.]+), +MTU +(?P<mtu>\d+)$')

        # IP address 172.16.100.251, subnet mask 255.255.255.0
        p3 = re.compile(r'^IP address +(?P<ip_address>[\w\.]+), subnet mask +(?P<subnet>[\w\.]+)$')


        for line in out.splitlines():
        	line = line.strip()

        	# Interface Vlan1000 "pod100", is up, line protocol is up 
        	m = p1.match(line)
    		if m:

    			groups = m.groupdict()
				interface = groups['interface']

    			instance_dict = ret_dict.setdefault('interfaces', {}). \
    				setdefault(interface, {})

    			instance_dict.update({'name': groups['name']})
    			instance_dict.update({'oper_status': groups['oper_status']})
    			instance_dict.update({'protocol_status': groups['protocol_status']})
    			continue

       		# MAC address 286f.7fb1.032c, MTU 1500
    		m = p2.match(line)
    		if m:
    			groups = m.groupdict()
    			instance_dict.update({'mac_address': groups['mac_address']})
    			instance_dict.update({'mtu': int(groups['mtu'])})
    			continue

    		# IP address 172.16.100.251, subnet mask 255.255.255.0
    		m = p3.match(line)
    		if m:
    			groups = m.groupdict()
    			instance_dict.update({'ip_address': groups['ip_address']})
    			instance_dict.update({'subnet': groups['subnet']})

    		return ret_dict






