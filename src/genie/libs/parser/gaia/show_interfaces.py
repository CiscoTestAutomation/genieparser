
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional
import re

class ShowInterfacesSchema(MetaParser):
    schema = {'interfaces': list}

class ShowInterfaces(ShowInterfacesSchema):
    """parser for show interface <interface>"""
        # 'show interfaces'
    
    cli_command = ['show interfaces']    
    
    def cli(self,interface="",output=None):
        if output is None:
            cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        interface_list = {}

        #p1 = re.compile(r'^(?P<interface>.*)$')
        p1 = re.compile(r'^Interface\s(?P<interface>\w+)\n\s+state (?P<state>\w+)\n\s+mac-addr (?P<mac_addr>.*)\n\s+type (?P<type>.*)\n\s+link-state (?P<link_state>.*)\n\s+mtu (?P<mtu>.*)\n\s+auto-negotiation (?P<auto_negotiation>.*)\n\s+speed (?P<speed>.*)\n\s+ipv6-autoconfig (?P<ipv6_autoconfig>.*)\n\s+duplex (?P<duplex>.*)\n\s+monitor-mode (?P<monitor_mode>.*)\n\s+link-speed (?P<link_speed>.*)\n\s+comments\s*(?P<comments>.*)\n\s+ipv4-address (?P<ipv4_address>.*)\n\s+ipv6-address (?P<ipv6_address>.*)\n\s+ipv6-local-link-address (?P<ipv6_local_link_address>.*)\n\nStatistics:\n\s+TX bytes:(?P<tx_bytes>\d+) packets:(?P<tx_packets>\d+) errors:(?P<tx_error>\d+) dropped:(?P<tx_dropped>\d+) overruns:(?P<tx_overruns>\d+) carrier:(?P<tx_carrier>\d+)\n\s+RX bytes:(?P<rx_bytes>\d+) packets:(?P<rx_packets>\d+) errors:(?P<rx_error>\d+) dropped:(?P<rx_dropped>\d+) overruns:(?P<rx_overruns>\d+) frame:(?P<rx_frame>\d+)')
        
        for line in out.splitlines():
            interface_list.setdefault('interfaces',[])

            m = p1.match(line)
            if m:
                interface_list['interfaces'].append(m.groupdict()['interface'])

        return interface_list
        