"""ping.py

JunOS parsers for the following show commands:
    * 
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Any, 
        Optional, Use, SchemaTypeError, Schema)

class MonitorInterfaceTrafficSchema(MetaParser):
    schema = {
        "interface": {
            Any(): {
                "link": str,
                "input-packets": int,
                Optional("input-pps"): int,
                "output-packets": int,
                Optional("output-pps"): int,
            }
        } 
    }

class MonitorInterfaceTraffic(MonitorInterfaceTrafficSchema):
    
    cli_command = ['monitor interface traffic']

    def cli(self, output=None, timeout=3):
        if not output:
            self.device.sendline(self.cli_command[0])
            out = self.device.expect([r'Interface[\S\s]+Down=\^D'], 
                timeout=timeout).match_output
            ansi_escape = re.compile(r'(\x9B|\x1B\[)[0-?]*[ -\/]*[@-~]')
            out = ansi_escape.sub('\t', out)
            self.device.sendline('q')
        else:
            out = output

        ret_dict = {}
        
        p1 = re.compile(r'^(?P<interface>\S+)\s+(?P<link>Up|Down)\s+'
            r'(?P<input_packets>\d+)(\s+\((?P<input_pps>\d+)\))?\s+'
            r'(?P<output_packets>\d+)(\s+\((?P<output_pps>\d+)\))?$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface_dict = ret_dict.setdefault('interface', {}). \
                    setdefault(group['interface'], {})
                interface_dict.update({'link': group['link']})
                interface_dict.update({'input-packets': int(group['input_packets'])})
                input_pps = group['input_pps']
                if input_pps:
                    interface_dict.update({'input-pps': int(input_pps)})
                interface_dict.update({'output-packets': int(group['output_packets'])})
                output_pps = group['output_pps']
                if output_pps:
                    interface_dict.update({'output-pps': int(output_pps)})
                continue
        
        return ret_dict