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
    
    cli_command = ['show macro auto device {device_name}', 'show macro auto device']

    def cli(self, device_name=None, output=None):
        if output is None:
            if device_name:
                output = self.device.execute(self.cli_command[0].format(device_name=device_name))
            else:
                output = self.device.execute(self.cli_command[1])
        
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


class ShowMacroAutoAddressgroupSchema(MetaParser):
    '''Schema for show macro auto address-group {address_group_name}'''
    schema = {
        'index': {
            Any(): {
                'group_name': str,
                'oui': str,
                'mac_address': str,
            },
        },
    }


class ShowMacroAutoAddressgroup(ShowMacroAutoAddressgroupSchema):
    '''Parser for show macro auto address-group {address_group_name}'''

    cli_command =  "show macro auto address-group {address_group_name}"

    def cli(self, address_group_name="", output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(address_group_name=address_group_name))
        
        # MAC Address Group Configuration:

        # Group Name                      OUI         MAC ADDRESS
        # --------------------------------------------------------------
        # test_add                                    1111.2222.3333
        p1 = re.compile(r'^(?P<group_name>\S+)\s+(?P<oui>\S*)\s+(?P<mac_address>\S+)$')
        
        ret_dict= dict()
        
        index = 1
        index_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # MAC Address Group Configuration:

            # Group Name                      OUI         MAC ADDRESS
            # --------------------------------------------------------------
            # test_add                                    1111.2222.3333
            m = p1.match(line)
            if m:
                group = m.groupdict()
                index_dict = ret_dict.setdefault('index', {}).setdefault(index,{})
                index_dict['group_name'] = group['group_name']
                index_dict['oui'] = group['oui']
                index_dict['mac_address'] = group['mac_address']
                index += 1
                continue
    
        return ret_dict