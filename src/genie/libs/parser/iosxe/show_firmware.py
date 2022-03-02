import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

class ShowFirmwareVersionAllSchema(MetaParser):
    """Schema for show firmware version all"""
    
    schema = {
        'index': {
            Any():{
                'name': str,
                'fw_version': str,
            },
        }
    }

class ShowFirmwareVersionAll(ShowFirmwareVersionAllSchema):
    """Parser for show firmware version all"""

    cli_command = [
        'show firmware version all'
    ]

    def cli(self, output=None):
        
        if output is None:
            output = self.device.execute(self.cli_command[0])

        ret_dict = {}
        index = 0
     
        #   PS2       Power Supply (PS PRI, PS_SEC, PS_I2C)   (00.05.01, 00.02.01, N/A)
        p0 = re.compile(
            r'^PS(?P<slot>\w+)\s+Power\s+Supply\s+\(.*\)\s+(?P<version>\(.*\)).*$')

        #  PS5  Fantray                       17012402              N/A                 N/A
        p1 = re.compile(
            r'^(?P<slot>\w+)\s+Fantray\s+(?P<version>\S+).*$')

        #   3    Supervisor Rommon (Active)    17.1.1[FC2]           N/A                 N/A 
        p2 = re.compile(
            r'^(?P<slot>\w+)\s+Supervisor\s+Rommon\s+(\(.*\))?\s+(?P<version>\S+).*$')

        
        for line in output.splitlines():
            line = line.strip()

            #   PS2       Power Supply (PS PRI, PS_SEC, PS_I2C)   (00.05.01, 00.02.01, N/A)
            m = p0.match(line)
            if m:
                index += 1
                group = m.groupdict()
                comp_dict = ret_dict.setdefault('index', {}).setdefault(index, {})
                comp_dict['name'] = "PowerSupplyModule"+group['slot']
                comp_dict['fw_version'] = group['version']
                continue

            #  PS5  Fantray                       17012402              N/A                 N/A
            m = p1.match(line)
            if m:
                index += 1
                group = m.groupdict()
                comp_dict = ret_dict.setdefault('index', {}).setdefault(index, {})
                comp_dict['name'] = "FanTray"
                comp_dict['fw_version'] = group['version']
                continue

            #   3    Supervisor Rommon (Active)    17.1.1[FC2]           N/A                 N/A
            m = p2.match(line)
            if m:
                index += 1
                group = m.groupdict()
                comp_dict = ret_dict.setdefault('index', {}).setdefault(index, {})
                comp_dict['name'] = "Slot "+ group['slot']+" Supervisor"
                comp_dict['fw_version'] = group['version']
                continue

        return ret_dict
