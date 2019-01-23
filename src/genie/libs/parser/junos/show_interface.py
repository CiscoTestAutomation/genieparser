"""show_interface.py

NXOS parsers for the following show commands:
    * show interfaces terse
    * show interfaces terse | match <interface>
"""

# python
import re

# metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional
                                         
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
    """Parser for show interfaces terse [| match <interface>]"""

    cli_command = ['show interfaces terse | match {interface}','show interfaces terse' ]

    def cli(self, interface=None,output=None):
        # execute the command
        if output is None:
            if interface:
                cmd = self.cli_command[0].format(interface=interface)
            else:
                cmd = self.cli_command[1]
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


        #                                             128.0.0.1/2       
        #                                    inet6    fe80::250:56ff:fe82:ba52/64
        #                                             fec0::a:0:0:4/64
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


            #                                             128.0.0.1/2       
            #                                    inet6    fe80::250:56ff:fe82:ba52/64
            #                                             fec0::a:0:0:4/64
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
