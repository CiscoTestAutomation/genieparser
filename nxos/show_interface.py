''' show_interface.py

Example parser class

'''

import os
import logging
import pprint
import re
import unittest
from collections import defaultdict

from ats import tcl
from ats.tcl.keyedlist import KeyedList
from ats.log.utils import banner
import xmltodict
try:
    import iptools
    from cnetconf import testmodel
except ImportError:
    pass

from metaparser import MetaParser
from metaparser.util import merge_dict, keynames_convert
from metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional, \
                                         Or, \
                                         And, \
                                         Default, \
                                         Use

logger = logging.getLogger(__name__)


def regexp(expression):
    def match(value):
        if re.match(expression,value):
            return value
        else:
            raise TypeError("Value '%s' doesnt match regex '%s'"
                              %(value, expression))
    return match


class ShowIpInterfaceBriefSchema(MetaParser):
    schema = {'interface':
                {Any():
                    {Optional('vlan_id'):
                        {Optional(Any()):
                                {'ip_address': str,
                                 'interface_status': str,
                                 Optional('ipaddress_extension'): str}
                        },
                    Optional('ip_address'): str,
                    Optional('interface_status'): str,
                    Optional('ipaddress_extension'): str}
                },
            }


class ShowIpInterfaceBrief(ShowIpInterfaceBriefSchema):
    """ parser class - implements detail parsing mechanisms for cli, xml, and
    yang output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cmd = 'show ip interface brief'.format()

    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        '''

        out = self.device.execute(self.cmd)
        interface_dict = {}
        for line in out.splitlines():
            line = line.rstrip()
            p1 = re.compile(r'^\s*Interface +IP Address +Interface Status$')
            m = p1.match(line)
            if m:
                continue

            p2 = re.compile(r'^\s*(?P<interface>[a-zA-Z0-9\/\.\-]+) +(?P<ip_address>[a-z0-9\.]+) +(?P<interface_status>[a-z\-\/]+)$')
            m = p2.match(line)
            if m:
                interface = m.groupdict()['interface']
                if 'interface' not in interface_dict:
                    interface_dict['interface'] = {}
                if interface not in interface_dict['interface']:
                    interface_dict['interface'][interface] = {}
                if 'Vlan' in interface:
                    vlan_id = str(int(re.search(r'\d+', interface).group()))
                    if 'vlan_id' not in interface_dict['interface'][interface]:
                        interface_dict['interface'][interface]['vlan_id'] = {}
                    if vlan_id not in interface_dict['interface'][interface]['vlan_id']:
                        interface_dict['interface'][interface]['vlan_id'][vlan_id] = {}
                    interface_dict['interface'][interface]['vlan_id'][vlan_id]['ip_address'] = \
                        m.groupdict()['ip_address']
                    interface_dict['interface'][interface]['vlan_id'][vlan_id]['interface_status'] = \
                        m.groupdict()['interface_status']
                else:
                    interface_dict['interface'][interface]['ip_address'] = \
                        m.groupdict()['ip_address']
                    interface_dict['interface'][interface]['interface_status'] = \
                        m.groupdict()['interface_status']
                continue

            p3 = re.compile(r'^\s*(?P<ipaddress_extension>\([a-z0-9]+\))$')
            m = p3.match(line)
            if m:
                ipaddress_extension = m.groupdict()['ipaddress_extension']
                if 'Vlan' in interface:
                    new_ip_address = interface_dict['interface']\
                        [interface]['vlan_id'][vlan_id]['ip_address'] + ipaddress_extension
                    interface_dict['interface'][interface]['vlan_id'][vlan_id]['ip_address'] = \
                        new_ip_address
                else:
                    new_ip_address = interface_dict['interface']\
                        [interface]['ip_address'] + ipaddress_extension
                    interface_dict['interface'][interface]['ip_address'] = new_ip_address
                continue

        return interface_dict


class ShowIpInterfaceBriefPipeVlan(ShowIpInterfaceBrief):
    """ parser class - implements detail parsing mechanisms for cli, xml, and
    yang output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cmd = 'show ip interface brief | include Vlan'.format()


# switchport administrative mode is what's configured on the switch port while operational mode is what is actually functioning at the moment.
class ShowInterfaceSwitchportSchema(MetaParser):
    schema = {'interface':
                {Any():
                    {Optional('switchport_mode'): 
                        {Optional(Any()):
                            {Optional('vlan_id'):
                                {Optional(Any()):
                                    {Optional('admin_trunking_encapsulation'): str}
                                },
                            }
                        },
                     Optional('operational_trunking_encapsulation'): str}
                },
            }


class ShowInterfaceSwitchport(ShowInterfaceSwitchportSchema):
    """ parser class - implements detail parsing mechanisms for cli, xml, and
    yang output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        '''
        cmd = 'show interface switchport'.format()
        out = self.device.execute(cmd)
        intf_dict = {}
        trunk_section = False
        access_section = False
        private_vlan_section = False
        trunk_encapsulation = ''
        for line in out.splitlines():
            line = line.rstrip()
            p1 = re.compile(r'^\s*Name:\s*(?P<interface_name>[a-zA-Z0-9\/\-]+)$')
            m = p1.match(line)
            if m:
                interface_name = m.groupdict()['interface_name']
                if 'interface' not in intf_dict:
                    intf_dict['interface'] = {}
                if interface_name not in intf_dict['interface']:
                    intf_dict['interface'][interface_name] = {}
                continue

            p2 = re.compile(r'^\s*Operational Mode:\s*(?P<operational_mode>[a-z\s*]+)$')
            m = p2.match(line)
            if m:
                operational_mode = m.groupdict()['operational_mode']
                if any(word in operational_mode for word in ['trunk', 'access']):
                    if 'switchport_mode' not in intf_dict['interface']:
                        intf_dict['interface'][interface_name]['switchport_mode'] = {}
                    if operational_mode not in intf_dict['interface'][interface_name]['switchport_mode']:
                        intf_dict['interface'][interface_name]['switchport_mode'][operational_mode] = {}

                if 'trunk' in operational_mode:
                    trunk_section = True
                    access_section = False
                elif 'access' in operational_mode:
                    access_section = True
                    trunk_section = False
                continue

            p3 = re.compile(r'^\s*Trunking Native Mode VLAN:\s*(?P<trunking_native_vlan>[0-9]+)( \([a-zA-Z]+\))*$')
            m = p3.match(line)
            if m:
                vlan_id = m.groupdict()['trunking_native_vlan']
                if any(word in operational_mode for word in ['trunk', 'access']):
                    if 'vlan_id' not in intf_dict['interface']\
                        [interface_name]['switchport_mode'][operational_mode]:
                        intf_dict['interface'][interface_name]['switchport_mode'][operational_mode]['vlan_id'] = {}
                    if vlan_id not in intf_dict['interface']\
                        [interface_name]['switchport_mode'][operational_mode]['vlan_id']:
                        intf_dict['interface'][interface_name]['switchport_mode'][operational_mode]['vlan_id'][vlan_id] = {}
                continue

            p4 = re.compile(r'^\s*Access Mode VLAN:\s*(?P<access_mode_vlan_id>[a-z0-9]+)( \([a-zA-Z]+\))*$')
            m = p4.match(line)
            if m:
                vlan_id = m.groupdict()['access_mode_vlan_id']
                if any(word in operational_mode for word in ['trunk', 'access']):
                    if 'vlan_id' not in intf_dict['interface']\
                        [interface_name]['switchport_mode'][operational_mode]:
                        intf_dict['interface'][interface_name]['switchport_mode'][operational_mode]['vlan_id'] = {}
                    if vlan_id not in intf_dict['interface']\
                        [interface_name]['switchport_mode'][operational_mode]['vlan_id']:
                        intf_dict['interface'][interface_name]['switchport_mode'][operational_mode]['vlan_id'][vlan_id] = {}
                continue

            p5 = re.compile(r'^\s*Administrative private-vlan trunk native VLAN:\s*(?P<admin_private_native_vlan>[0-9]+)$')
            m = p5.match(line)
            if m:
                vlan_id = m.groupdict()['admin_private_native_vlan']
                if any(word in admin_mode for word in ['trunk', 'access']):
                    if 'vlan_id' not in intf_dict['interface']\
                        [interface_name]['switchport_mode'][operational_mode]:
                        intf_dict['interface'][interface_name]['switchport_mode'][operational_mode]['vlan_id'] = {}
                    if vlan_id not in intf_dict['interface']\
                        [interface_name]['switchport_mode'][operational_mode]['vlan_id']:
                        intf_dict['interface'][interface_name]['switchport_mode'][operational_mode]['vlan_id'][vlan_id] = {}
                continue

        return intf_dict

class ShowInterfaceBriefSchema(MetaParser):
    schema = {'interface':
                {'port':
                    {Any():
                        {'vrf': str,
                         'status': str,
                         'ip_address': str,
                         'speed': str,
                         'mtu': str}
                    },
                'ethernet':
                    {Any():
                        {'vlan': str,
                         'type': str,
                         'mode': str,
                         'status': str,
                         'speed': str,
                         'reason': str,
                         'port_ch': str}
                    },
                'port_channel':
                    {Any():
                        {'vlan': str,
                         'type': str,
                         'mode': str,
                         'status': str,
                         'speed': str,
                         'reason': str,
                         'protocol': str}
                    },
                'loopback':
                    {Any():
                        {'status': str,
                         'description': str}
                    },
                }
            }


class ShowInterfaceBrief(ShowInterfaceBriefSchema):
    """ parser class - implements detail parsing mechanisms for cli, xml, and
    yang output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cmd = 'show interface brief'.format()

    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        '''

        out = self.device.execute(self.cmd)
        interface_dict = {}
        for line in out.splitlines():
            line = line.rstrip()
            p1 = re.compile(r'^\s*Port +VRF +Status +IP Address +Speed +MTU$')
            m = p1.match(line)
            if m:
                if 'interface' not in interface_dict:
                    interface_dict['interface'] = {}
                if 'port' not in interface_dict['interface']:
                    interface_dict['interface']['port'] = {}
                continue

            p2 = re.compile(r'^\s*(?P<port>[a-zA-Z0-9]+)'
                             ' +(?P<vrf>[a-zA-Z0-9\-]+)'
                             ' +(?P<status>[a-zA-Z]+) +(?P<ip_address>[0-9\.]+)'
                             ' +(?P<speed>[0-9]+) +(?P<mtu>[0-9]+)$')
            m = p2.match(line)
            if m:
                port = m.groupdict()['port']
                if port not in interface_dict['interface']['port']:
                    interface_dict['interface']['port'][port] = {}
                interface_dict['interface']['port'][port]['vrf'] = \
                    m.groupdict()['vrf']
                interface_dict['interface']['port'][port]['status'] = \
                    m.groupdict()['status']
                interface_dict['interface']['port'][port]['ip_address'] = \
                    m.groupdict()['ip_address']
                interface_dict['interface']['port'][port]['speed'] = \
                    m.groupdict()['speed']
                interface_dict['interface']['port'][port]['mtu'] = \
                    m.groupdict()['mtu']
                continue

            p3 = re.compile(r'^\s*Ethernet +VLAN +Type +Mode +Status'
                             ' +Reason +Speed +Port$')
            m = p3.match(line)
            if m:
                if 'interface' not in interface_dict:
                    interface_dict['interface'] = {}
                if 'ethernet' not in interface_dict['interface']:
                    interface_dict['interface']['ethernet'] = {}
                continue

            p4 = re.compile(r'^\s*(?P<interface>[a-zA-Z0-9\/]+)'
                             ' +(?P<vlan>[a-zA-Z0-9\-]+)'
                             ' +(?P<type>[a-zA-Z]+) +(?P<mode>[a-z]+)'
                             ' +(?P<status>[a-z]+) +(?P<reason>[a-zA-Z\s]+)'
                             ' +(?P<speed>[0-9a-zA-Z\(\)\s]+)'
                             ' +(?P<port>[0-9\-]+)$')
            m = p4.match(line)
            if m:
                interface = m.groupdict()['interface']
                if interface not in interface_dict['interface']['ethernet']:
                    interface_dict['interface']['ethernet'][interface] = {}
                interface_dict['interface']['ethernet'][interface]['vlan'] =\
                    m.groupdict()['vlan']
                interface_dict['interface']['ethernet'][interface]['type'] =\
                    m.groupdict()['type']
                interface_dict['interface']['ethernet'][interface]['mode'] =\
                    m.groupdict()['mode']
                interface_dict['interface']['ethernet'][interface]['status'] =\
                    m.groupdict()['status']
                interface_dict['interface']['ethernet'][interface]['reason'] =\
                    m.groupdict()['reason']
                interface_dict['interface']['ethernet'][interface]['speed'] =\
                    m.groupdict()['speed']
                interface_dict['interface']['ethernet'][interface]['port_ch'] =\
                    m.groupdict()['port']
                continue

            p5 = re.compile(r'^\s*Port-channel +VLAN +Type +Mode +Status'
                             ' +Reason +Speed +Protocol$')
            m = p5.match(line)
            if m:
                if 'interface' not in interface_dict:
                    interface_dict['interface'] = {}
                if 'port_channel' not in interface_dict['interface']:
                    interface_dict['interface']['port_channel'] = {}
                continue

            p6 = re.compile(r'^\s*(?P<interface>[a-zA-Z0-9\/]+)'
                             ' +(?P<vlan>[a-zA-Z0-9\-]+)'
                             ' +(?P<type>[a-zA-Z]+) +(?P<mode>[a-z]+)'
                             ' +(?P<status>[a-z]+) +(?P<reason>[a-zA-Z\s]+)'
                             ' +(?P<speed>[0-9a-zA-Z\(\)\s]+)'
                             ' +(?P<protocol>[a-zA-Z0-9\-]+)$')
            m = p6.match(line)
            if m:
                interface = m.groupdict()['interface']
                if interface not in interface_dict['interface']['port_channel']:
                    interface_dict['interface']['port_channel'][interface] = {}
                interface_dict['interface']['port_channel'][interface]['vlan'] = \
                    m.groupdict()['vlan']
                interface_dict['interface']['port_channel'][interface]['type'] = \
                    m.groupdict()['type']
                interface_dict['interface']['port_channel'][interface]['mode'] = \
                    m.groupdict()['mode']
                interface_dict['interface']['port_channel'][interface]['status'] = \
                    m.groupdict()['status']
                interface_dict['interface']['port_channel'][interface]['reason'] = \
                    m.groupdict()['reason']
                interface_dict['interface']['port_channel'][interface]['speed'] = \
                    m.groupdict()['speed']
                interface_dict['interface']['port_channel'][interface]['protocol'] = \
                    m.groupdict()['protocol']
                continue


            p7 = re.compile(r'^\s*Interface +Status +Description$')
            m = p7.match(line)
            if m:
                if 'interface' not in interface_dict:
                    interface_dict['interface'] = {}
                if 'loopback' not in interface_dict['interface']:
                    interface_dict['interface']['loopback'] = {}
                continue

            p8 = re.compile(r'^\s*(?P<interface>[a-zA-Z0-9\/]+)'
                             ' +(?P<status>[a-z]+)'
                             ' +(?P<description>[a-zA-Z\s\-]+)$')
            m = p8.match(line)
            if m:
                interface = m.groupdict()['interface']
                if interface not in interface_dict['interface']['loopback']:
                    interface_dict['interface']['loopback'][interface] = {}
                interface_dict['interface']['loopback'][interface]['status'] = \
                    m.groupdict()['status']
                interface_dict['interface']['loopback'][interface]['description'] = \
                    m.groupdict()['description']
                continue

        return interface_dict
