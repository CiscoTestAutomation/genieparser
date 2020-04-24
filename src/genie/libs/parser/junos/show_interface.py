"""show_interface.py

JunOS parsers for the following show commands:
    * show interfaces terse
    * show interfaces terse | match <interface>
    * show interfaces terse {interface}
    * show interfaces {interface} terse
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

class ShowInterfacesSchema(MetaParser):
    """ Parser for:
        'show interfaces'
    """
    schema = {}

class ShowInterfaces(ShowInterfacesSchema):
    cli_command = ['show interfaces']

    def cli(self, output=None):

        if not output:
            out = self.device.execute(self.cli_command[0])
        else:
            out = output
        
        ret_dict = {}

        # Physical interface: ge-0/0/0, Enabled, Physical link is Up
        p1 = re.compile(r'^Physical +interface: +\S+, +\S+, +Physical +link +is +\S+$')

        # Interface index: 148, SNMP ifIndex: 526
        p2 = re.compile(r'^Interface +index: +\d+, +SNMP +ifIndex: +\d+$')

        # Description: none/100G/in/hktGCS002_ge-0/0/0
        p3 = re.compile(r'^Description: +\S+$')

        # Link-level type: Ethernet, MTU: 1514, MRU: 1522, LAN-PHY mode, Speed: 1000mbps, BPDU Error: None,
        p4 = re.compile(r'^Link-level +type: +\S+, +MTU: +\d+, +MRU: +\d+, +(\S+) +mode, +Speed: +(\S+), +BPDU +Error: +\S+,$')

        # Loop Detect PDU Error: None, Ethernet-Switching Error: None, MAC-REWRITE Error: None, Loopback: Disabled,
        p5 = re.compile(r'^Loop +Detect +PDU +Error: +\S+, +Ethernet-Switching +Error: +\S+, +MAC-REWRITE +Error: +\S+, +Loopback: +\S+,$')

        # Source filtering: Disabled, Flow control: Enabled, Auto-negotiation: Enabled, Remote fault: Online
        p6 = re.compile(r'^Source +filtering: +\S+, +Flow +control: +\S+, +Auto-negotiation: +\S+, +Remote +fault: +\S+$')

        # Pad to minimum frame size: Disabled
        p7 = re.compile(r'^Pad +to +minimum +frame +size: +\S+$')

        # Device flags   : Present Running
        p8 = re.compile(r'^Device +flags +: +[\S ]+$')

        # Interface flags: SNMP-Traps Internal: 0x4000
        p9 = re.compile(r'^Interface +flags: +\S+ +Internal: +\S+$')

        # Link flags     : None
        p10 = re.compile(r'^Link +flags +: +\S+$')

        # CoS queues     : 8 supported, 8 maximum usable queues
        p11 = re.compile(r'^CoS +queues +: +\d+ supported, +\d+ maximum +usable +queues$')

        # Current address: 00:50:56:8d:c8:29, Hardware address: 00:50:56:8d:c8:29
        p12 = re.compile(r'^Current +address: +\S+, +Hardware +address: +\S+$')

        # Last flapped   : 2019-08-29 09:09:19 UTC (29w6d 18:56 ago)
        p13 = re.compile(r'^Last +flapped +: +[\S ]+$')

        # Input rate     : 2952 bps (5 pps)
        p14 = re.compile(r'^Input +rate +: +\d+ +bps +\(\d+ +pps\)$')

        p15 = re.compile(r'^Output +rate +: +\d+ +bps +\(\d+ +pps\)$')
        return ret_dict