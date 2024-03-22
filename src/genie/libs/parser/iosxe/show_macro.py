"""
    show_macro.py
    IOSXE parsers for the following show commands:

    * show macro auto device
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any


class ShowMacroAutoDeviceSchema(MetaParser):
    '''Schema for show macro auto device'''
    schema = {
        'device': {
            Any(): {
                'macro': {
                    'default': str,
                    'current': str
                },
                'parameters': {
                    'configurable': str,
                    'defaults': str,
                    'current': str
                }
            }
        }
    }


class ShowMacroAutoDevice(ShowMacroAutoDeviceSchema):
    '''Parser for show macro auto device'''

    cli_command = 'show macro auto device'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)
        
        # Device:access-point
        p1 = re.compile(r'^Device:(?P<device>\S+)$')

        # Default Macro:CISCO_AP_AUTO_SMARTPORT
        p2 = re.compile(r'^Default Macro:(?P<default>\S+)$')
        
        # Current Macro:CISCO_AP_AUTO_SMARTPORT
        p3 = re.compile(r'^Current Macro:(?P<current>\S+)$')

        # Configurable Parameters:NATIVE_VLAN
        p4 = re.compile(r'^Configurable Parameters:(?P<configurable>.+)$')

        # Defaults Parameters:NATIVE_VLAN=1
        p5 = re.compile(r'^Defaults Parameters:(?P<defaults>.+)$')

        # Current Parameters:NATIVE_VLAN=1
        p6 = re.compile(r'^Current Parameters:(?P<current>.+)$')

        ret_dict= dict()

        for line in output.splitlines():
            line = line.strip()

            # Device:access-point
            m = p1.match(line)
            if m:
                dev_dict = ret_dict.setdefault('device', {}).setdefault(m.groupdict()['device'], {})
                macro_dict = dev_dict.setdefault('macro', {})
                param_dict = dev_dict.setdefault('parameters', {})
                continue

            # Default Macro:CISCO_AP_AUTO_SMARTPORT
            m = p2.match(line)
            if m:
                macro_dict.update(m.groupdict())
                continue

            # Current Macro:CISCO_AP_AUTO_SMARTPORT
            m = p3.match(line)
            if m:
                macro_dict.update(m.groupdict())
                continue

            # Configurable Parameters:NATIVE_VLAN
            m = p4.match(line)
            if m:
                param_dict.update(m.groupdict())
                continue

            # Defaults Parameters:NATIVE_VLAN=1
            m = p5.match(line)
            if m:
                param_dict.update(m.groupdict())
                continue

            # Current Parameters:NATIVE_VLAN=1
            m = p6.match(line)
            if m:
                param_dict.update(m.groupdict())
                continue

        return ret_dict
