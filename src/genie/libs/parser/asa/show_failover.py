'''show_failover.py
ASA parsers for for the following commands:
    * show failover
    * show failover interface
'''

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


class ShowFailoverInterfaceSchema(MetaParser):
    ''' Schema for:
        * show failover interface
    '''
    schema = {
        Any(): {
            'name': str,
            'interface': str,
            'system_ip': str,
            'my_ip': str,
            'other_ip': str,
        }
    }


class ShowFailoverInterface(ShowFailoverInterfaceSchema):

    cli_command = 'show failover interface'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(cli_command)
        else:
            out = output
        
        # interface folink GigabitEthernet0/1
        p1 = re.compile(r'^interface\s+(?P<name>\w+)\s+(?P<interface>[A-Za-z]+\s*[\.\d\/]+)$')

        # System IP Address: 2001:db8:cafe:ffee::a/127
        p2 = re.compile(r'^System +IP +Address:\s+(?P<ip>\S+)$')

        # My IP Address    : 2001:db8:cafe:ffee::a
        p3 = re.compile(r'^My +IP +Address\s+:\s+(?P<ip>\S+)$')

        # Other IP Address : 2001:db8:cafe:ffee::b
        p4 = re.compile(r'^Other +IP +Address\s+:\s+(?P<ip>\S+)$')

        parsed_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # interface folink GigabitEthernet0/1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface_dict = parsed_dict.setdefault(group['name'], {})
                interface_dict.update({'interface': group['interface']})
                interface_dict.update({'name': group['name']})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({'system_ip': group['ip']})
                continue
                
            m = p3.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({'my_ip': group['ip']})
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({'other_ip': group['ip']})
                continue

        return parsed_dict
        

