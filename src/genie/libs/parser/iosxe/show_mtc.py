"""show_mtc.py

IOSXE parsers for the following show commands:

    * show mgmt-traffic control ipv4
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

class ShowMgmtTrafficControlIpv4Schema(MetaParser):
    """Schema for show mgmt-traffic control ipv4"""

    schema = {
        'interface_list': str,
        Optional('protocol_list'): str,
        Optional('ip_address'): str,
    }

class ShowMgmtTrafficControlIpv4(ShowMgmtTrafficControlIpv4Schema):
    ''' Parser for:
            show mgmt-traffic control ipv4
    '''
    cli_command = 'show mgmt-traffic control ipv4'

    def cli(self, output=None):
        cmd = self.cli_command

        if output is None:
            output = self.device.execute(cmd)

        res_dict = {}

        # Interface List: HundredGigE1/0/3 HundredGigE1/0/4
        p1 = re.compile(r'Interface +List: +(?P<interface_list>[\S+ ]+)')
        # Protocol List: telnet netconf
        p2 = re.compile(r'Protocol +List: +(?P<protocol_list>[\w ]+)')
        # IP Address:  3.3.3.3
        p3 = re.compile(r'IP +Address: +(?P<ip_address>\S+)')

        for line in output.splitlines():
            line = line.strip()
            # Interface List: HundredGigE1/0/3 HundredGigE1/0/4
            m = p1.match(line)
            if m:
                group = m.groupdict()
                res_dict['interface_list'] = group['interface_list']
                continue
            # Protocol List: telnet netconf
            m = p2.match(line)
            if m : 
                group = m.groupdict()
                res_dict['protocol_list'] = group['protocol_list']
                continue
            # IP Address:  3.3.3.3
            m = p3.match(line)
            if m : 
                group = m.groupdict()
                res_dict['ip_address'] = group['ip_address']
                continue

        return res_dict    
