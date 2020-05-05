"""show_interface.py

JunOS parsers for the following show commands:
    * show interfaces terse
    * show interfaces terse | match <interface>
    * show interfaces terse {interface}
    * show interfaces {interface} terse
    * show interfaces descriptions
"""

# python
import re

# metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Use, SchemaTypeError

# import parser utils
from genie.libs.parser.utils.common import Common


# =======================================================
# Schema for 'show interfaces terse [| match <interface>]
# =======================================================
class ShowInterfacesTerseSchema(MetaParser):
    """Schema for show interfaces terse [| match <interface>]"""

    schema = {
        Any(): {
            'oper_status': str,
            Optional('link_state'): str,
            Optional('admin_state'): str,
            Optional('phys_address'): str,
            'enabled': bool,
            Optional('protocol'): {
                Any():{
                    Optional(Any()): {
                        'local': str,
                        Optional('remote'): str,
                    },
                },
            },
        }
    }

# =======================================================
# Parser for 'show interfaces terse [| match <interface>]
# =======================================================
class ShowInterfacesTerse(ShowInterfacesTerseSchema):
    """ Parser for:
            - show interfaces terse
            - show interfaces {interface} terse
            - show interfaces terse {interface}
    """

    cli_command = [
        'show interfaces terse',
        'show interfaces {interface} terse'
    ]

    exclude = [
        'duration'
    ]

    def cli(self, interface=None, output=None):
        # execute the command
        if output is None:
            if interface:
                cmd = self.cli_command[1]
                cmd = cmd.format(interface=interface)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        ret_dict = {}

        # Interface               Admin Link Proto    Local                 Remote
        # lo0.0                   up    up   inet     10.1.1.1            --> 0/0
        # em1.0                   up    up   inet     10.0.0.4/8
        # fxp0                    up    up
        p1 =  re.compile(r'^(?P<interface>\S+) +(?P<admin_state>\w+) +(?P<link_state>\w+) *'
                          '(?P<protocol>\S+)? *(?P<local>[\w\.\:\/]+)?( *'
                          '[\-\>]+? *(?P<remote>[\w\.\:\/]+))?$')


        #                                             172.16.64.1/2
        #                                    inet6    fe80::250:56ff:fe82:ba52/64
        #                                             2001:db8:8d82:0:a::4/64
        #                                    tnp      0x4
        #                                             10.11.11.11         --> 0/0
        p2 =  re.compile(r'^((?P<protocol>\S+) +)?(?P<local>((\d+\.[\d\.\/]+)|(\w+\:[\w\:\/]+)|(0x\d+))+)'
                          ' *(([\-\>]+) *(?P<remote>[\w\.\:\/]+))?$')
        #                                    multiservice
        p3 = re.compile(r'^((?P<protocol>\S+))$')



        for line in out.splitlines():
            line = line.replace('\t', '    ')
            line = line.strip()

            if 'show interfaces terse' in line:
                continue


            # fxp0                    up    up
            # em1.0                   up    up   inet     10.0.0.4/8
            # lo0.0                   up    up   inet     10.1.1.1            --> 0/0
            m = p1.match(line)
            if m:
                groups = m.groupdict()
                interface = groups['interface']
                intf_dict = ret_dict.setdefault(interface, {})
                intf_dict.update({'admin_state': groups['admin_state'],
                                  'link_state': groups['link_state'],
                                  'oper_status': groups['link_state'],
                                  'enabled': 'up' in groups['admin_state']})
                if groups['protocol']:
                    protocol = groups['protocol']
                    pro_dict = intf_dict.setdefault('protocol', {}).setdefault(groups['protocol'], {})
                if groups['local']:
                    pro_dict = pro_dict.setdefault(groups['local'], {})
                    pro_dict['local'] = groups['local']
                    if groups['remote']:
                        pro_dict['remote'] = groups['remote']
                continue


            #                                             172.16.64.1/2
            #                                    inet6    fe80::250:56ff:fe82:ba52/64
            #                                             2001:db8:8d82:0:a::4/64
            #                                    tnp      0x4
            #                                             10.11.11.11         --> 0/0
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                try:
                    protocol = groups['protocol'] or protocol
                except Exception:
                    continue
                pro_dict = intf_dict.setdefault('protocol', {}).setdefault(protocol, {}).setdefault(groups['local'], {})
                pro_dict['local'] = groups['local']
                if groups['remote']:
                    pro_dict['remote'] = groups['remote']
                continue

            #                                    multiservice
            m = p3.match(line)
            if m:
                groups = m.groupdict()
                protocol = m.groupdict()['protocol']
                pro_dict = intf_dict.setdefault('protocol', {}).setdefault(protocol, {})
                continue
        return ret_dict

class ShowInterfacesTerseMatch(ShowInterfacesTerse):
    """ Parser for:
            - show interfaces terse | match {interface}
    """

    cli_command = 'show interfaces terse | match {interface}'

    def cli(self, interface, output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(interface=interface))
        else:
            out = output

        return super().cli(output=out)

class ShowInterfacesTerseInterface(ShowInterfacesTerse):
    """ Parser for:
            - 'show interfaces terse {interface}'
    """

    cli_command = 'show interfaces terse {interface}'

    def cli(self, interface, output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(interface=interface))
        else:
            out = output

        return super().cli(output=out)

class ShowInterfacesDescriptionsSchema(MetaParser):
    """ Schema for:
            * show interfaces descriptions
    """
    def validate_physical_interface_list(value):
        if not isinstance(value, list):
            raise SchemaTypeError('physical-interface is not a list')
        entry_schema = Schema(
            {
                "admin-status": str,
                "description": str,
                "name": str,
                "oper-status": str
            }
        )
        for item in value:
            entry_schema.validate(item)
        return value

    schema = {
        "interface-information": {
            "physical-interface": Use(validate_physical_interface_list)
        }
    }

class ShowInterfacesDescriptions(ShowInterfacesDescriptionsSchema):
    """ Parser for:
            * show interfaces descriptions
    """
    cli_command = 'show interfaces descriptions'


    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # Interface       Admin Link Description
        p1 = re.compile(r'^Interface +Admin +Link +Description$')

        # ge-0/0/0        up    up   none/100G/in/hktGCS002_ge-0/0/0
        p2 = re.compile(r'^(?P<name>\S+) +(?P<admin_status>\S+) +(?P<oper_status>\S+) +(?P<description>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # Interface       Admin Link Description
            m = p1.match(line)
            if m:
                continue

            # ge-0/0/0        up    up   none/100G/in/hktGCS002_ge-0/0/0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                entry_list = ret_dict.setdefault("interface-information", {}).setdefault("physical-interface", [])
                entry = {}
                for group_key, group_value in group.items():
                    entry_key = group_key.replace('_','-')
                    entry[entry_key] = group_value
                entry_list.append(entry)
                continue

        return ret_dict