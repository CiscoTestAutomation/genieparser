
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

        p1 = re.compile(r'^(?P<interface>.*)$')
        for line in out.splitlines():
            interface_list.setdefault('interfaces',[])

            m = p1.match(line)
            if m:
                interface_list['interfaces'].append(m.groupdict()['interface'])

        return interface_list
        