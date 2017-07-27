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
                {'ethernet':
                    {Any():
                        {'vlan': str,
                         'type': str,
                         'mode': str,
                         'status': str,
                         'speed': str,
                         'reason': str,
                         'port_ch': str}
                    },
                Optional('port'):
                    {Any():
                        {Optional('vrf'): str,
                         Optional('status'): str,
                         Optional('ip_address'): str,
                         Optional('speed'): str,
                         Optional('mtu'): str}
                    },
                Optional('port_channel'):
                    {Any():
                        {Optional('vlan'): str,
                         Optional('type'): str,
                         Optional('mode'): str,
                         Optional('status'): str,
                         Optional('speed'): str,
                         Optional('reason'): str,
                         Optional('protocol'): str}
                    },
                Optional('loopback'):
                    {Any():
                        {Optional('status'): str,
                         Optional('description'): str}
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

#############################################################################
# Parser For Show Interface
#############################################################################


class ShowInterfaceSchema(MetaParser):

    schema = {
        Any(): 
            {Optional('description'): str,
            'types': str,
            Optional('parent_interface'): str,
            'oper_status': str,
            Optional('link_state'): str,
            'phys_address': str,
            Optional('port_speed'): str,
            'mtu': int,
            'enabled': bool,
            'mac_address': str,
            Optional('auto_negotiate'): bool,
            Optional('duplex_mode'): str,
            'port_mode': str,
            Optional('auto_mdix'): str,
            Optional('switchport_monitor'): str,
            Optional('efficient_ethernet'): str,
            Optional('last_linked_flapped'): str,
            Optional('last_clearing'): str,
            Optional('interface_reset'): int,
            Optional('ethertype'): str,
            Optional('beacon'): str,
            Optional('medium'): str,
            'reliability': str,
            'txload': str,
            'rxload': str,
            'delay': int,
            Optional('flow_control'):
                {Optional('flow_control_receive'): bool,
                Optional('flow_control_send'): bool,
            },
            'bandwidth': int,
            Optional('counters'):
                {Optional('rate'):
                   {Optional('load_interval'): int,
                    Optional('in_rate'): int,
                    Optional('in_rate_pkts'): int,
                    Optional('out_rate'): int,
                    Optional('out_rate_pkts'): int,
                    Optional('in_rate_bps'): int,
                    Optional('in_rate_pps'): int,
                    Optional('out_rate_bps'): int,
                    Optional('out_rate_pps'): int,
                    },
                Optional('in_unicast_pkts'): int,
                Optional('in_multicast_pkts'): int,
                Optional('in_broadcast_pkts'): int,
                Optional('in_discards'): int,
                Optional('in_crc_errors'): int,
                Optional('in_oversize_frames'): int,
                Optional('in_pkts'): int,
                Optional('in_mac_pause_frames'): int,
                Optional('in_jumbo_packets'): int,
                Optional('in_storm_suppression_packets'): int,
                Optional('in_runts'): int,
                Optional('in_giant'): int,
                Optional('in_overrun'): int,
                Optional('in_underrun'): int,
                Optional('in_ignored'): int,
                Optional('in_watchdog'): int,
                Optional('in_bad_etype_drop'): int,
                Optional('in_bad_proto_drop'): int,
                Optional('in_if_down_drop'): int,
                Optional('in_with_dribble'): int,
                Optional('in_discard'): int,
                Optional('in_bytes'): int,
                Optional('in_error'): int,
                Optional('in_short_frame'): int,
                Optional('in_no_buffer'): int,
                Optional('out_pkts'): int,
                Optional('out_unicast_pkts'): int,
                Optional('out_multicast_pkts'): int,
                Optional('out_broadcast_pkts'): int,
                Optional('out_discard'): int,
                Optional('out_bytes'): int,
                Optional('out_jumbo_packets'): int,
                Optional('out_error'): int,
                Optional('out_collision'): int,
                Optional('out_deferred'): int,
                Optional('out_late_collision'): int,
                Optional('out_lost_carrier'): int,
                Optional('out_no_carrier'): int,
                Optional('out_babble'): int,
                Optional('out_mac_pause_frames'): int,
                },
            Optional('encapsulations'):
                {Optional('encapsulation'): str,
                 Optional('first_dot1q'): str,
                 Optional('native_vlan'): int,
                },
            Optional('ipv4'):
                {Any():
                    {Optional('ipv4'): str,
                     Optional('prefix_length'): str,
                     Optional('secondary'): bool,
                     Optional('route_tag'): int
                    },
                },
            },
        }


class ShowInterface(ShowInterfaceSchema):

    def cli(self):
        out = self.device.execute('show interface')

        interface_dict = {}

        for line in out.splitlines():
            line = line.rstrip()

            # Ethernet2/1.10 is down (Administratively down)
            p1 =  re.compile(r'^\s*(?P<interface>[a-zA-Z0-9\/\.]+) *is'
                              ' *(?P<enabled>(down))'
                              '( *\((?P<link_state>[a-zA-Z\s]+)\))?$')
            m = p1.match(line)
            if m:
                interface = m.groupdict()['interface']
                enabled = m.groupdict()['enabled']
                link_state = m.groupdict()['link_state']

                if interface not in interface_dict:
                    interface_dict[interface] = {}
                interface_dict[interface]\
                            ['link_state'] = link_state

                interface_dict[interface]['enabled'] = False
                continue

            p1_1 =  re.compile(r'^\s*(?P<interface>[a-zA-Z0-9\/\.]+) *is'
                              ' *(?P<enabled>(up))'
                              '( *\((?P<link_state>[a-zA-Z\s]+)\))?$')
            m = p1_1.match(line)
            if m:
                interface = m.groupdict()['interface']
                enabled = m.groupdict()['enabled']
                link_state = str(m.groupdict()['link_state'])

                if interface not in interface_dict:
                    interface_dict[interface] = {}
                interface_dict[interface]\
                            ['link_state'] = link_state

                interface_dict[interface]['enabled'] = True
                continue

            #admin state is up
            p2 = re.compile(r'^\s*admin *state *is (?P<oper_status>[a-z\,]+)'
                             '( *Dedicated *Interface)?$')
            m = p2.match(line)
            if m:
                oper_status = m.groupdict()['oper_status']
        
                interface_dict[interface]['oper_status'] = oper_status
                continue

            #admin state is down, Dedicated Interface, [parent interface is Ethernet2/1]
            p2_1 = re.compile(r'^\s*admin *state *is (?P<oper_status>[a-z\,]+)'
                               ' *Dedicated *Interface, \[parent *interface *is'
                               ' *(?P<parent_interface>[a-zA-Z0-9\/\.]+)\]$')
            m = p2_1.match(line)
            if m:
                oper_status = m.groupdict()['oper_status']
                parent_interface = m.groupdict()['parent_interface']

                interface_dict[interface]\
                        ['oper_status'] = oper_status
                interface_dict[interface]\
                ['parent_interface'] = parent_interface
                continue

            #Hardware: Ethernet, address: 5254.00c9.d26e (bia 5254.00c9.d26e)
            p3 = re.compile(r'^\s*Hardware: *(?P<types>[a-zA-Z0-9\/\s]+),'
                            ' *address: *(?P<mac_address>[a-z0-9\.]+)'
                            ' *\(bia *(?P<phys_address>[a-z0-9\.]+)\)$')
            m = p3.match(line)
            if m:
                types = m.groupdict()['types']
                mac_address = m.groupdict()['mac_address']
                phys_address = m.groupdict()['phys_address']

                interface_dict[interface]['types'] = types
                interface_dict[interface]\
                            ['mac_address'] = mac_address
                interface_dict[interface]\
                            ['phys_address'] = phys_address
                continue

            #Description: desc
            p4 = re.compile(r'^\s*Description: *(?P<description>[a-z]+)$')
            m = p4.match(line)
            if m:
                description = m.groupdict()['description']

                interface_dict[interface]['description'] = description
                continue

            #Internet Address is 10.4.4.4/24 secondary tag 10
            p5 = re.compile(r'^\s*Internet *Address *is *(?P<ipv4>[0-9\.]+)'
                             '\/(?P<prefix_length>[0-9]+)'
                             ' *(?P<secondary>(secondary)) *tag'
                             ' *(?P<route_tag>[0-9]+)$')
            m = p5.match(line)
            if m:
                ipv4 = m.groupdict()['ipv4']
                prefix_length = str(m.groupdict()['prefix_length'])
                secondary = m.groupdict()['secondary']
                route_tag = int(m.groupdict()['route_tag'])
                #address = ipv4+prefix_length
                address = ipv4 + '/' + prefix_length
                if 'ipv4' not in interface_dict[interface]:
                    interface_dict[interface]['ipv4'] = {}
                if address not in interface_dict[interface]['ipv4']:
                    interface_dict[interface]['ipv4'][address] = {}

                interface_dict[interface]['ipv4'][address]\
                ['ipv4'] = ipv4
                interface_dict[interface]['ipv4'][address]\
                ['prefix_length'] = prefix_length

                interface_dict[interface]['ipv4'][address]\
                ['secondary'] = True
                interface_dict[interface]['ipv4'][address]\
                ['route_tag'] = route_tag
                continue
            
            #MTU 1600 bytes, BW 768 Kbit, DLY 3330 usec
            p6 = re.compile(r'^\s*MTU *(?P<mtu>[0-9]+) *bytes, *BW'
                             ' *(?P<bandwidth>[0-9]+) *Kbit, *DLY'
                             ' *(?P<delay>[0-9]+) *usec$')
            m = p6.match(line)
            if m:
                mtu = int(m.groupdict()['mtu'])
                bandwidth = int(m.groupdict()['bandwidth'])
                delay = int(m.groupdict()['delay'])
                
                interface_dict[interface]['mtu'] = mtu
                interface_dict[interface]['bandwidth'] = bandwidth
                interface_dict[interface]['delay'] = delay
                continue

            #reliability 255/255, txload 1/255, rxload 1/255
            p7 = re.compile(r'^\s*reliability *(?P<reliability>[0-9\/]+),'
                             ' *txload *(?P<txload>[0-9\/]+),'
                             ' *rxload *(?P<rxload>[0-9\/]+)$')
            m = p7.match(line)
            if m:
                reliability = m.groupdict()['reliability']
                txload = m.groupdict()['txload']
                rxload = m.groupdict()['rxload']

                interface_dict[interface]['reliability'] = reliability
                interface_dict[interface]['txload'] = txload
                interface_dict[interface]['rxload'] = rxload
                continue

            #Encapsulation 802.1Q Virtual LAN, Vlan ID 10, medium is broadcast
            #Encapsulation 802.1Q Virtual LAN, Vlan ID 20, medium is p2p
            #Encapsulation ARPA, medium is broadcast

            p8 = re.compile(r'^\s*Encapsulation *(?P<encapsulation>[a-zA-Z0-9\.\s]+),'
                             ' *medium *is *(?P<medium>[a-zA-Z]+)$')
            m = p8.match(line)
            if m:
                encapsulation = m.groupdict()['encapsulation']
                encapsulation = encapsulation.replace("802.1Q Virtual LAN","dot1q")
                medium = m.groupdict()['medium']

                if 'encapsulations' not in interface_dict[interface]:
                    interface_dict[interface]['encapsulations'] = {}

                interface_dict[interface]['encapsulations']\
                ['encapsulation'] = encapsulation
                interface_dict[interface]\
                ['medium'] = medium
                continue

            p8_1 = re.compile(r'^\s*Encapsulation *(?P<encapsulation>[a-zA-Z0-9\.\s]+),'
                               ' *vlan *ID *(?P<first_dot1q>[0-9]+),'
                               ' *medium *is *(?P<medium>[a-z0-9]+)$')
            m = p8_1.match(line)
            if m:
                encapsulation = m.groupdict()['encapsulation']
                encapsulation = encapsulation.replace("802.1Q Virtual LAN","dot1q")
                first_dot1q = str(m.groupdict()['first_dot1q'])
                medium = m.groupdict()['medium']

                if 'encapsulations' not in interface_dict[interface]:
                    interface_dict[interface]['encapsulations'] = {}

                interface_dict[interface]['encapsulations']\
                ['encapsulation'] = encapsulation
                interface_dict[interface]['encapsulations']\
                ['first_dot1q'] = first_dot1q
                interface_dict[interface]['medium'] = medium
                continue

            #Port mode is routed
            p9 = re.compile(r'^\s*Port *mode *is *(?P<port_mode>[a-z]+)$')
            m = p9.match(line)
            if m:
                port_mode = m.groupdict()['port_mode']

                interface_dict[interface]['port_mode'] = port_mode
                continue

            #full-duplex, 1000 Mb/s
            p10 = re.compile(r'^\s*(?P<duplex_mode>[a-z\-]+),'
                              ' *(?P<port_speed>[0-9]+) *Mb/s$')
            m = p10.match(line)
            if m:
                duplex_mode = m.groupdict()['duplex_mode']
                port_speed = m.groupdict()['port_speed']

                interface_dict[interface]['duplex_mode'] = duplex_mode
                interface_dict[interface]['port_speed'] = port_speed
                continue

            #Beacon is turned off
            p11 = re.compile(r'^\s*Beacon *is *turned *(?P<beacon>[a-z]+)$')
            m = p11.match(line)
            if m:
                beacon = m.groupdict()['beacon']

                interface_dict[interface]['beacon'] = beacon
                continue

            #Auto-Negotiation is turned off
            p12 = re.compile(r'^\s*Auto-Negotiation *is *turned'
                              ' *(?P<auto_negotiate>(off))$')
            m = p12.match(line)
            if m:
                auto_negotiation = m.groupdict()['auto_negotiate']

                interface_dict[interface]['auto_negotiate'] = False
                continue

            p12_1 = re.compile(r'^\s*Auto-Negotiation *is *turned'
                              ' *(?P<auto_negotiate>(on))$')
            m = p12_1.match(line)
            if m:
                auto_negotiation = m.groupdict()['auto_negotiate']

                interface_dict[interface]['auto_negotiate'] = True
                continue

            #Input flow-control is off, output flow-control is off
            p13 = re.compile(r'^\s*Input *flow-control *is *(?P<flow_control_receive>(off)+),'
                              ' *output *flow-control *is *(?P<flow_control_send>(off)+)$')
            m = p13.match(line)
            if m:
                flow_control_receive = m.groupdict()['flow_control_receive']
                flow_control_send = m.groupdict()['flow_control_send']

                if 'flow_control' not in interface_dict[interface]:
                    interface_dict[interface]['flow_control'] = {}

                interface_dict[interface]['flow_control']['flow_control_receive'] = False
                interface_dict[interface]['flow_control']['flow_control_send'] = False
                continue

            p13_1 = re.compile(r'^\s*Input *flow-control *is *(?P<flow_control_receive>(on)+),'
                                ' *output *flow-control *is *(?P<flow_control_send>(on)+)$')
            m = p13_1.match(line)
            if m:
                flow_control_receive = m.groupdict()['flow_control_receive']
                flow_control_send = m.groupdict()['flow_control_send']

                if 'flow_control' not in interface_dict[interface]:
                    interface_dict[interface]['flow_control'] = {}

                interface_dict[interface]['flow_control']['flow_control_receive'] = True
                interface_dict[interface]['flow_control']['flow_control_send'] = True
                continue

            #Auto-mdix is turned off
            p14 = re.compile(r'^\s*Auto-mdix *is *turned *(?P<auto_mdix>[a-z]+)$')
            m = p14.match(line)
            if m:
                auto_mdix = m.groupdict()['auto_mdix']

                interface_dict[interface]['auto_mdix'] = auto_mdix
                continue

            #Switchport monitor is off 
            p15 = re.compile(r'^\s*Switchport *monitor *is *(?P<switchport_monitor>[a-z]+)$')
            m = p15.match(line)
            if m:
                switchport_monitor = m.groupdict()['switchport_monitor']

                interface_dict[interface]['switchport_monitor'] = switchport_monitor
                continue

            #EtherType is 0x8100 
            p16 = re.compile(r'^\s*Ethertype *is *(?P<ethertype>[a-z0-9]+)$')
            m = p16.match(line)
            if m:
                ethertype = m.groupdict()['ethertype']

                interface_dict[interface]['ethertype'] = ethertype
                continue

            #EEE (efficient-ethernet) : n/a
            p17 = re.compile(r'^\s*EEE *\(efficient-ethernet\) *:'
                              ' *(?P<efficient_ethernet>[A-Za-z\/]+)$')
            m = p17.match(line)
            if m:
                efficient_ethernet = m.groupdict()['efficient_ethernet']

                interface_dict[interface]['efficient_ethernet'] = efficient_ethernet
                continue

            #Last link flapped 00:07:28
            p18 = re.compile(r'^\s*Last *link *flapped'
                              ' *(?P<last_linked_flapped>[0-9\:]+)$')
            m = p18.match(line)
            if m:
                last_linked_flapped = m.groupdict()['last_linked_flapped']

                interface_dict[interface]['last_linked_flapped']\
                 = last_linked_flapped
                continue

            #Last clearing of "show interface" counters never
            p19 = re.compile(r'^\s*Last *clearing *of *\"show *interface\"'
                              ' *counters *(?P<last_clearing>[a-z]+)$')
            m = p19.match(line)
            if m:
                last_clearing = m.groupdict()['last_clearing']

                interface_dict[interface]['last_clearing'] = last_clearing
                continue

            #1 interface resets
            p20 = re.compile(r'^\s*(?P<interface_reset>[0-9]+) *interface'
                              ' *resets$')
            m = p20.match(line)
            if m:
                interface_reset = int(m.groupdict()['interface_reset'])

                interface_dict[interface]['interface_reset'] = interface_reset
                continue

            #1 minute input rate 0 bits/sec, 0 packets/sec  
            p21 = re.compile(r'^\s*(?P<load_interval>[0-9\#]+)'
                              ' *(minute|second|minutes|seconds) *input *rate'
                              ' *(?P<in_rate>[0-9]+) *bits/sec,'
                              ' *(?P<in_rate_pkts>[0-9]+) *packets/sec$')
            m = p21.match(line)
            if m:

                load_interval = int(m.groupdict()['load_interval'])
                in_rate = int(m.groupdict()['in_rate'])
                in_rate_pkts = int(m.groupdict()['in_rate_pkts'])

                if 'counters' not in interface_dict[interface]:
                    interface_dict[interface]['counters'] = {}
                if 'rate' not in interface_dict[interface]['counters']:
                    interface_dict[interface]['counters']['rate'] = {}
                
                interface_dict[interface]['counters']['rate']\
                ['load_interval'] = load_interval
                interface_dict[interface]['counters']['rate']\
                ['in_rate'] = in_rate
                interface_dict[interface]['counters']['rate']\
                ['in_rate_pkts'] = in_rate_pkts
                continue

            #1 minute output rate 24 bits/sec, 0 packets/sec
            p22 = re.compile(r'^\s*(?P<load_interval>[0-9\#]+)'
                              ' *(minute|second|minutes|seconds) *output'
                              ' *rate *(?P<out_rate>[0-9]+)'
                              ' *bits/sec, *(?P<out_rate_pkts>[0-9]+)'
                              ' *packets/sec$')
            m = p22.match(line)
            if m:
                load_interval = int(m.groupdict()['load_interval'])
                out_rate = int(m.groupdict()['out_rate'])
                out_rate_pkts = int(m.groupdict()['out_rate_pkts'])

                interface_dict[interface]['counters']['rate']\
                ['load_interval'] = load_interval
                interface_dict[interface]['counters']['rate']\
                ['out_rate'] = out_rate
                interface_dict[interface]['counters']['rate']\
                ['out_rate_pkts'] = out_rate_pkts
                continue

            #input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
            p23 = re.compile(r'^\s*input *rate *(?P<in_rate_bps>[0-9]+) *bps,'
                              ' *(?P<in_rate_pps>[0-9]+) *pps; *output *rate'
                              ' *(?P<out_rate_bps>[0-9]+) *bps,'
                              ' *(?P<out_rate_pps>[0-9]+) *pps$')
            m = p23.match(line)
            if m:
                in_rate_bps = int(m.groupdict()['in_rate_bps'])
                in_rate_pps = int(m.groupdict()['in_rate_pps'])
                out_rate_bps = int(m.groupdict()['out_rate_bps'])
                out_rate_pps = int(m.groupdict()['out_rate_pps'])

                if 'counters' not in interface_dict[interface]:
                    interface_dict[interface]['counters'] = {}
                if 'rate' not in interface_dict[interface]['counters']:
                    interface_dict[interface]['counters']['rate'] = {}

                interface_dict[interface]['counters']['rate']\
                ['in_rate_bps'] = in_rate_bps
                interface_dict[interface]['counters']['rate']\
                ['in_rate_pps'] = in_rate_pps
                interface_dict[interface]['counters']['rate']\
                ['out_rate_bps'] = out_rate_bps
                interface_dict[interface]['counters']['rate']\
                ['out_rate_pps'] = out_rate_pps
                continue

            #0 unicast packets  0 multicast packets  0 broadcast packets
            p24 = re.compile(r'^\s*(?P<in_unicast_pkts>[0-9]+) +unicast +packets'
                              ' +(?P<in_multicast_pkts>[0-9]+) +multicast +packets'
                              ' +(?P<in_broadcast_pkts>[0-9]+) +broadcast +packets$')
            m = p24.match(line)
            if m:
                in_unicast_pkts = int(m.groupdict()['in_unicast_pkts'])
                in_multicast_pkts = int(m.groupdict()['in_multicast_pkts'])
                in_broadcast_pkts = int(m.groupdict()['in_broadcast_pkts'])
        
                interface_dict[interface]['counters']['in_unicast_pkts'] = in_unicast_pkts
                interface_dict[interface]['counters']['in_multicast_pkts'] = in_multicast_pkts
                interface_dict[interface]['counters']['in_broadcast_pkts'] = in_broadcast_pkts
                continue

            #0 input packets  0 bytes
            p25 = re.compile(r'^\s*(?P<in_pkts>[0-9]+) +input +packets'
                              ' +(?P<in_bytes>[0-9]+) +bytes$')
            m = p25.match(line)
            if m:
                in_pkts = int(m.groupdict()['in_pkts'])
                in_bytes = int(m.groupdict()['in_bytes'])

                interface_dict[interface]['counters']['in_pkts'] = in_pkts
                interface_dict[interface]['counters']['in_bytes'] = in_bytes
                continue

            #0 jumbo packets  0 storm suppression packets
            p26 = re.compile(r'^\s*(?P<in_jumbo_packets>[0-9]+) +jumbo +packets'
                              ' *(?P<in_storm_suppression_packets>[0-9]+)'
                              ' *storm *suppression *packets$')
            m = p26.match(line)
            if m:
                in_jumbo_packets = int(m.groupdict()['in_jumbo_packets'])
                in_storm_suppression_packets = int(m.groupdict()['in_storm_suppression_packets'])

                interface_dict[interface]['counters']['in_jumbo_packets']\
                 = in_jumbo_packets
                interface_dict[interface]['counters']\
                ['in_storm_suppression_packets'] = in_storm_suppression_packets
                continue

            #0 runts  0 giants  0 CRC/FCS  0 no buffer
            p27 = re.compile(r'^\s*(?P<in_runts>[0-9]+) *runts'
                              ' *(?P<in_giant>[0-9]+) *giants'
                              ' *(?P<in_crc_errors>[0-9]+) *CRC/FCS'
                              ' *(?P<in_no_buffer>[0-9]+) *no *buffer$')
            m = p27.match(line)
            if m:
                in_runts = int(m.groupdict()['in_runts'])
                in_giant = int(m.groupdict()['in_giant'])
                in_crc_errors = int(m.groupdict()['in_crc_errors'])
                in_no_buffer = int(m.groupdict()['in_no_buffer'])

                interface_dict[interface]['counters']['in_runts'] = in_runts
                interface_dict[interface]['counters']['in_giant'] = in_giant
                interface_dict[interface]['counters']['in_crc_errors'] = in_crc_errors
                interface_dict[interface]['counters']['in_no_buffer'] = in_no_buffer
                continue

            #0 input error  0 short frame  0 overrun   0 underrun  0 ignored
            p28 = re.compile(r'^\s*(?P<in_error>[0-9]+) *input *error'
                              ' *(?P<in_short_frame>[0-9]+) *short *frame'
                              ' *(?P<in_overrun>[0-9]+) *overrun *(?P<in_underrun>[0-9]+)'
                              ' *underrun *(?P<in_ignored>[0-9]+) *ignored$')
            m = p28.match(line)
            if m:
                in_error = int(m.groupdict()['in_error'])
                in_short_frame = int(m.groupdict()['in_short_frame'])
                in_overrun = int(m.groupdict()['in_overrun'])
                in_underrun = int(m.groupdict()['in_underrun'])
                in_ignored = int(m.groupdict()['in_ignored'])

                interface_dict[interface]['counters']['in_error'] = in_error
                interface_dict[interface]['counters']['in_short_frame'] = in_short_frame
                interface_dict[interface]['counters']['in_overrun'] = in_overrun
                interface_dict[interface]['counters']['in_underrun'] = in_underrun
                interface_dict[interface]['counters']['in_ignored'] = in_ignored
                continue

            #0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
            p29 = re.compile(r'^\s*(?P<in_watchdog>[0-9]+) *watchdog'
                              ' *(?P<in_bad_etype_drop>[0-9]+)'
                              ' *bad *etype *drop *(?P<in_bad_proto_drop>[0-9]+)'
                              ' *bad *proto'
                              ' *drop *(?P<in_if_down_drop>[0-9]+) *if *down *drop$')
            m = p29.match(line)
            if m:
                in_watchdog = int(m.groupdict()['in_watchdog'])
                in_bad_etype_drop = int(m.groupdict()['in_bad_etype_drop'])
                in_bad_proto_drop = int(m.groupdict()['in_bad_proto_drop'])
                in_if_down_drop = int(m.groupdict()['in_if_down_drop'])

                interface_dict[interface]['counters']['in_watchdog'] = in_watchdog
                interface_dict[interface]['counters']['in_bad_etype_drop'] = in_bad_etype_drop
                interface_dict[interface]['counters']['in_bad_proto_drop'] = in_bad_proto_drop
                interface_dict[interface]['counters']['in_if_down_drop'] = in_if_down_drop
                continue

            p30 = re.compile(r'^\s*(?P<in_with_dribble>[0-9]+) *input *with'
                              ' *dribble *(?P<in_discard>[0-9]+) *input *discard$')
            m = p30.match(line)
            if m:
                in_with_dribble = int(m.groupdict()['in_with_dribble'])
                in_discard = int(m.groupdict()['in_discard'])

                interface_dict[interface]['counters']['in_with_dribble'] = in_with_dribble
                interface_dict[interface]['counters']['in_discard'] = in_discard
                continue

            p31 = re.compile(r'^\s*(?P<in_mac_pause_frames>[0-9]+) *Rx *pause$')
            m = p31.match(line)
            if m:
                in_mac_pause_frames = int(m.groupdict()['in_mac_pause_frames'])

                interface_dict[interface]['counters']['in_mac_pause_frames'] = in_mac_pause_frames
                continue

            #0 unicast packets  0 multicast packets  0 broadcast packets
            p32 = re.compile(r'^\s*(?P<out_unicast_pkts>[0-9]+) *unicast *packets'
                              ' *(?P<out_multicast_pkts>[0-9]+) *multicast *packets'
                              ' *(?P<out_broadcast_pkts>[0-9]+) *broadcast *packets$')
            m = p32.match(line)
            if m:
                out_unicast_pkts = int(m.groupdict()['out_unicast_pkts'])
                out_multicast_pkts = int(m.groupdict()['out_multicast_pkts'])
                out_broadcast_pkts = int(m.groupdict()['out_broadcast_pkts'])

                interface_dict[interface]['counters']['out_unicast_pkts'] = out_unicast_pkts
                interface_dict[interface]['counters']['out_multicast_pkts'] = out_multicast_pkts
                interface_dict[interface]['counters']['out_broadcast_pkts'] = out_broadcast_pkts
                continue

            #0 output packets  0 bytes
            p33 = re.compile(r'^\s*(?P<out_pkts>[0-9]+) *output *packets'
                              ' *(?P<out_bytes>[0-9]+) *bytes$')
            m = p33.match(line)
            if m:
                out_pkts = int(m.groupdict()['out_pkts'])
                out_bytes = int(m.groupdict()['out_bytes'])

                interface_dict[interface]['counters']['out_pkts'] = out_pkts
                interface_dict[interface]['counters']['out_bytes'] = out_bytes
                continue

            #0 jumbo packets
            p34 = re.compile(r'^\s*(?P<out_jumbo_packets>[0-9]+) *jumbo *packets$')
            m = p34.match(line)
            if m:
                out_jumbo_packets = int(m.groupdict()['out_jumbo_packets'])

                interface_dict[interface]['counters']['out_jumbo_packets'] = out_jumbo_packets
                continue

            #0 output error  0 collision  0 deferred  0 late collision
            p35 = re.compile(r'^\s*(?P<out_error>[0-9]+) *output *error'
                              ' *(?P<out_collision>[0-9]+) *collision'
                              ' *(?P<out_deferred>[0-9]+) *deferred'
                              ' *(?P<out_late_collision>[0-9]+)'
                              ' *late *collision$')
            m = p35.match(line)
            if m:
                out_error = int(m.groupdict()['out_error'])
                out_collision = int(m.groupdict()['out_collision'])
                out_deferred = int(m.groupdict()['out_deferred'])
                out_late_collision = int(m.groupdict()['out_late_collision'])

                interface_dict[interface]['counters']['out_error'] = out_error
                interface_dict[interface]['counters']['out_collision'] = out_collision
                interface_dict[interface]['counters']['out_deferred'] = out_deferred
                interface_dict[interface]['counters']['out_late_collision'] = out_late_collision
                continue
            #0 lost carrier  0 no carrier  0 babble  0 output discard
            p36 = re.compile(r'^\s*(?P<out_lost_carrier>[0-9]+) *lost *carrier'
                              ' *(?P<out_no_carrier>[0-9]+) *no *carrier'
                              ' *(?P<out_babble>[0-9]+) *babble'
                              ' *(?P<out_discard>[0-9]+) *output *discard$')
            m = p36.match(line)
            if m:
                out_lost_carrier = int(m.groupdict()['out_lost_carrier'])
                out_no_carrier = int(m.groupdict()['out_no_carrier'])
                out_babble = int(m.groupdict()['out_babble'])
                out_discard = int(m.groupdict()['out_discard'])

                interface_dict[interface]['counters']['out_lost_carrier'] = out_lost_carrier
                interface_dict[interface]['counters']['out_no_carrier'] = out_no_carrier
                interface_dict[interface]['counters']['out_babble'] = out_babble
                interface_dict[interface]['counters']['out_discard'] = out_discard
                continue

            #0 Tx pause
            p37 = re.compile(r'^\s*(?P<out_mac_pause_frames>[0-9]+) *Tx *pause$')
            m = p37.match(line)
            if m:
                out_mac_pause_frames = int(m.groupdict()['out_mac_pause_frames'])

                interface_dict[interface]['counters']['out_mac_pause_frames'] = out_mac_pause_frames
                continue

        return interface_dict


#############################################################################
# Parser For Show Ip Interface Vrf All
#############################################################################


class ShowIpInterfaceVrfAllSchema(MetaParser):

    schema = {
        Any():
            {'vrf': str,
             'interface_status': str,
             'iod': int,
             Optional('ipv4'):
                {Any():
                    {Optional('ipv4'): str,
                     Optional('prefix_length'): str,
                     Optional('secondary'): bool,
                     Optional('route_tag'): int,
                     Optional('ip_subnet'): str,
                    },
                },
            'broadcast_address': str,
            'multicast_groups': str,
            'mtu': int,
            'route_preference': int,
            'proxy_arp': str,
            'local_proxy_arp': str,
            'multicast_routing': str,
            'icmp_redirects': str,
            'directed_broadcast': str,
            'ip_forwarding': str,
            'icmp_unreachable': str,
            'icmp_port_unreachable': str,
            'unicast_reverse_path': str,
            'load_sharing': str,
            'int_stat_last_reset': str,
            'int_software_stats': str,
            'unicast_packets': str,
            'unicast_bytes': str,
            'multicast_packets': str,
            'multicast_bytes': str,
            'broadcast_packets': str,
            'broadcast_bytes': str,
            'labeled_packets': str,
            'labeled_bytes': str,
            'wccp_redirect_outbound': str,
            'wccp_redirect_inbound': str,
            'wccp_redirect_exclude': str
            },
        }   

class ShowIpInterfaceVrfAll(ShowIpInterfaceVrfAllSchema):

    def cli(self):
        out = self.device.execute('show ip interface vrf all')

        ip_interface_vrf_all_dict = {}

        for line in out.splitlines():
            line = line.rstrip()

            #IP Interface Status for VRF "VRF1"
            p1 = re.compile(r'^\s*IP *Interface *Status *for *VRF'
                             ' *(?P<vrf>[a-zA-Z0-9\"]+)$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                vrf = vrf.replace('"',"")
                continue

            #Ethernet2/1, Interface status: protocol-up/link-up/admin-up, iod: 36,
            p2 = re.compile(r'^\s*(?P<interface>[a-zA-Z0-9\/]+), *Interface'
                             ' *status: *(?P<interface_status>[a-z\-\/\s]+),'
                             ' *iod: *(?P<iod>[0-9]+),$')
            m = p2.match(line)
            if m:
                interface = m.groupdict()['interface']
                interface_status = m.groupdict()['interface_status']
                iod = int(m.groupdict()['iod'])

                if interface not in ip_interface_vrf_all_dict:
                    ip_interface_vrf_all_dict[interface] = {}

                ip_interface_vrf_all_dict[interface]['interface_status']\
                 = interface_status
                ip_interface_vrf_all_dict[interface]['iod'] = iod
                ip_interface_vrf_all_dict[interface]['vrf'] = vrf
                continue

            #IP address: 10.4.4.4, IP subnet: 10.4.4.0/24 secondary
            p3 = re.compile(r'^\s*IP *address: *(?P<ipv4>[0-9\.]+), *IP'
                             ' *subnet: *(?P<ip_subnet>[a-z0-9\.]+)\/'
                             '(?P<prefix_length>[0-9]+)'
                             ' *(?P<secondary>(secondary))$')
            m = p3.match(line)
            if m:
                ipv4 = m.groupdict()['ipv4']
                ip_subnet = m.groupdict()['ip_subnet']
                prefix_length = m.groupdict()['prefix_length']
                secondary = m.groupdict()['secondary']

                address = ipv4 + '/' + prefix_length
                if 'ipv4' not in ip_interface_vrf_all_dict[interface]:
                    ip_interface_vrf_all_dict[interface]['ipv4'] = {}
                if address not in ip_interface_vrf_all_dict[interface]['ipv4']:
                    ip_interface_vrf_all_dict[interface]['ipv4'][address] = {}

                ip_interface_vrf_all_dict[interface]['ipv4'][address]\
                ['ipv4'] = ipv4
                ip_interface_vrf_all_dict[interface]['ipv4'][address]\
                ['ip_subnet'] = ip_subnet
                ip_interface_vrf_all_dict[interface]['ipv4'][address]\
                ['prefix_length'] = prefix_length
                ip_interface_vrf_all_dict[interface]['ipv4'][address]\
                ['secondary'] = True
                continue

            #IP address: 10.4.4.4, IP subnet: 10.4.4.0/24
            p3_1 = re.compile(r'^\s*IP *address: *(?P<ipv4>[0-9\.]+), *IP'
                               ' *subnet: *(?P<ip_subnet>[a-z0-9\.]+)\/'
                               '(?P<prefix_length>[0-9]+)$')
            m = p3_1.match(line)
            if m:
                ipv4 = m.groupdict()['ipv4']
                ip_subnet = m.groupdict()['ip_subnet']
                prefix_length = m.groupdict()['prefix_length']

                address = ipv4 + '/' + prefix_length
                if 'ipv4' not in ip_interface_vrf_all_dict[interface]:
                    ip_interface_vrf_all_dict[interface]['ipv4'] = {}
                if address not in ip_interface_vrf_all_dict[interface]['ipv4']:
                    ip_interface_vrf_all_dict[interface]['ipv4'][address] = {}

                ip_interface_vrf_all_dict[interface]['ipv4'][address]\
                ['ipv4'] = ipv4
                ip_interface_vrf_all_dict[interface]['ipv4'][address]\
                ['ip_subnet'] = ip_subnet
                ip_interface_vrf_all_dict[interface]['ipv4'][address]\
                ['prefix_length'] = prefix_length
                continue

            #IP broadcast address: 255.255.255.255
            p4 = re.compile(r'^\s*IP *broadcast *address:'
                             ' *(?P<broadcast_address>[0-9\.]+)$')
            m = p4.match(line)
            if m:
                broadcast_address = m.groupdict()['broadcast_address']

                ip_interface_vrf_all_dict[interface]['broadcast_address']\
                 = broadcast_address
                continue
            
            #IP multicast groups locally joined: none
            p5 = re.compile(r'^\s*IP *multicast *groups *locally *joined:'
                             ' *(?P<multicast_groups>[a-z]+)$')
            m = p5.match(line)
            if m:
                multicast_groups = m.groupdict()['multicast_groups']

                ip_interface_vrf_all_dict[interface]['multicast_groups']\
                = multicast_groups
                continue

            #IP MTU: 1600 bytes (using link MTU)
            p6 = re.compile(r'^\s*IP *MTU: *(?P<mtu>[0-9]+)'
                             ' *bytes *\(using *link *MTU\)$')
            m = p6.match(line)
            if m:
                mtu = int(m.groupdict()['mtu'])

                ip_interface_vrf_all_dict[interface]['mtu'] = mtu
                continue

            #IP primary address route-preference: 0, tag: 0
            p7 = re.compile(r'^\s*IP *primary *address *route-preference:'
                             ' *(?P<route_preference>[0-9]+), *tag:'
                             ' *(?P<route_tag>[0-9]+)$')
            m = p7.match(line)
            if m:
                route_preference = int(m.groupdict()['route_preference'])
                route_tag = int(m.groupdict()['route_tag'])

                ip_interface_vrf_all_dict[interface]['route_preference']\
                 = route_preference
                ip_interface_vrf_all_dict[interface]['ipv4'][address]\
                ['route_tag'] = route_tag
                continue

            #IP proxy ARP : disabled
            p8 = re.compile(r'^\s*IP *proxy *ARP *: *(?P<proxy_arp>[a-z]+)$')
            m = p8.match(line)
            if m:
                proxy_arp = m.groupdict()['proxy_arp']

                ip_interface_vrf_all_dict[interface]['proxy_arp'] = proxy_arp
                continue

            #IP Local Proxy ARP : disabled
            p9 = re.compile(r'^\s*IP *Local *Proxy *ARP *:'
                             ' *(?P<local_proxy_arp>[a-z]+)$')
            m = p9.match(line)
            if m:
                local_proxy_arp = m.groupdict()['local_proxy_arp']

                ip_interface_vrf_all_dict[interface]['local_proxy_arp']\
                 = local_proxy_arp
                continue

            #IP multicast routing: disabled
            p10 = re.compile(r'^\s*IP *multicast *routing:'
                              ' *(?P<multicast_routing>[a-z]+)$')
            m = p10.match(line)
            if m:
                multicast_routing = m.groupdict()['multicast_routing']

                ip_interface_vrf_all_dict[interface]['multicast_routing']\
                 = multicast_routing
                continue

            #IP icmp redirects: disabled
            p11 = re.compile(r'^\s*IP *icmp *redirects:'
                              ' *(?P<icmp_redirects>[a-z]+)$')
            m = p11.match(line)
            if m:
                icmp_redirects = m.groupdict()['icmp_redirects']

                ip_interface_vrf_all_dict[interface]['icmp_redirects']\
                 = icmp_redirects
                continue

            #IP directed-broadcast: disabled
            p12 = re.compile(r'^\s*IP directed-broadcast:'
                              ' *(?P<directed_broadcast>[a-z]+)$')
            m = p12.match(line)
            if m:
                directed_broadcast = m.groupdict()['directed_broadcast']

                ip_interface_vrf_all_dict[interface]['directed_broadcast']\
                 = directed_broadcast
                continue

            #IP Forwarding: disabled
            p13 = re.compile(r'^\s*IP *Forwarding: *(?P<ip_forwarding>[a-z]+)$') 
            m = p13.match(line)
            if m:
                ip_forwarding = m.groupdict()['ip_forwarding']

                ip_interface_vrf_all_dict[interface]['ip_forwarding']\
                 = ip_forwarding
                continue

            #IP icmp unreachables (except port): disabled
            p14 = re.compile(r'^\s*IP *icmp *unreachables *\(except *port\):'
                              ' *(?P<icmp_unreachable>[a-z]+)$')
            m = p14.match(line)
            if m:
                icmp_unreachable = m.groupdict()['icmp_unreachable']

                ip_interface_vrf_all_dict[interface]['icmp_unreachable']\
                 = icmp_unreachable
                continue

            #IP icmp port-unreachable: enabled
            p15 = re.compile(r'^\s*IP *icmp *port-unreachable:'
                              ' *(?P<icmp_port_unreachable>[a-z]+)$')
            m = p15.match(line)
            if m:
                icmp_port_unreachable = m.groupdict()['icmp_port_unreachable']

                ip_interface_vrf_all_dict[interface]['icmp_port_unreachable']\
                 = icmp_port_unreachable
                continue

            #IP unicast reverse path forwarding: none
            p16 = re.compile(r'^\s*IP *unicast *reverse *path *forwarding:'
                              ' *(?P<unicast_reverse_path>[a-z]+)$')
            m = p16.match(line)
            if m:
                unicast_reverse_path = m.groupdict()['unicast_reverse_path']

                ip_interface_vrf_all_dict[interface]['unicast_reverse_path']\
                 = unicast_reverse_path
                continue

            #IP load sharing: none 
            p17 = re.compile(r'^\s*IP *load *sharing: *(?P<load_sharing>[a-z]+)$')
            m = p17.match(line)
            if m:
                load_sharing = m.groupdict()['load_sharing']

                ip_interface_vrf_all_dict[interface]['load_sharing']\
                 = load_sharing
                continue

            #IP interface statistics last reset: never
            p18 = re.compile(r'^\s*IP *interface *statistics *last *reset:'
                              ' *(?P<int_stat_last_reset>[a-z]+)')
            m = p18.match(line)
            if m:
                int_stat_last_reset = m.groupdict()['int_stat_last_reset']

                ip_interface_vrf_all_dict[interface]['int_stat_last_reset']\
                 = int_stat_last_reset
                continue

            #IP interface software stats: (sent/received/forwarded/originated/consumed)
            p19 = re.compile(r'^\s*IP *interface *software *stats:'
                              ' *(?P<int_software_stats>[a-z\/\(\)\s]+)')
            m = p19.match(line)
            if m:
                int_software_stats = m.groupdict()['int_software_stats']

                ip_interface_vrf_all_dict[interface]['int_software_stats']\
                 = int_software_stats
                continue

            #Unicast packets    : 0/0/0/0/0
            p20 = re.compile(r'^\s*Unicast *packets *:'
                              ' *(?P<unicast_packets>[0-9\/]+)$')
            m = p20.match(line)
            if m:
                unicast_packets = m.groupdict()['unicast_packets']

                ip_interface_vrf_all_dict[interface]['unicast_packets']\
                 = unicast_packets
                continue

            #Unicast bytes      : 0/0/0/0/0
            p21 = re.compile(r'^\s*Unicast *bytes *:'
                              ' *(?P<unicast_bytes>[0-9\/]+)$')
            m = p21.match(line)
            if m:
                unicast_bytes = m.groupdict()['unicast_bytes']

                ip_interface_vrf_all_dict[interface]['unicast_bytes']\
                 = unicast_bytes
                continue

            #Multicast packets  : 0/0/0/0/0
            p22 = re.compile(r'^\s*Multicast *packets *:'
                              ' *(?P<multicast_packets>[0-9\/]+)$')
            m = p22.match(line)
            if m:
                multicast_packets = m.groupdict()['multicast_packets']

                ip_interface_vrf_all_dict[interface]['multicast_packets']\
                 = multicast_packets
                continue

            #Multicast bytes    : 0/0/0/0/0
            p23 = re.compile(r'^\s*Multicast *bytes *:'
                              ' *(?P<multicast_bytes>[0-9\/]+)$')
            m = p23.match(line)
            if m:
                multicast_bytes = m.groupdict()['multicast_bytes']

                ip_interface_vrf_all_dict[interface]['multicast_bytes']\
                 = multicast_bytes
                continue

            #Broadcast packets  : 0/0/0/0/0
            p24 = re.compile(r'^\s*Broadcast *packets *:'
                              ' *(?P<broadcast_packets>[0-9\/]+)$')
            m = p24.match(line)
            if m:
                broadcast_packets = m.groupdict()['broadcast_packets']

                ip_interface_vrf_all_dict[interface]['broadcast_packets']\
                 = broadcast_packets
                continue

            #Broadcast bytes    : 0/0/0/0/0
            p25 = re.compile(r'^\s*Broadcast *bytes *:'
                              ' *(?P<broadcast_bytes>[0-9\/]+)$')
            m = p25.match(line)
            if m:
                broadcast_bytes = m.groupdict()['broadcast_bytes']

                ip_interface_vrf_all_dict[interface]['broadcast_bytes']\
                 = broadcast_bytes
                continue

            #Labeled packets    : 0/0/0/0/0
            p26 = re.compile(r'^\s*Labeled *packets *:'
                              ' *(?P<labeled_packets>[0-9\/]+)$')
            m = p26.match(line)
            if m:
                labeled_packets = m.groupdict()['labeled_packets']

                ip_interface_vrf_all_dict[interface]['labeled_packets']\
                 = labeled_packets
                continue

            #Labeled bytes      : 0/0/0/0/0
            p27 = re.compile(r'^\s*Labeled *bytes *:'
                              ' *(?P<labeled_bytes>[0-9\/]+)$')
            m = p27.match(line)
            if m:
                labeled_bytes = m.groupdict()['labeled_bytes']

                ip_interface_vrf_all_dict[interface]['labeled_bytes']\
                 = labeled_bytes
                continue

            #WCCP Redirect outbound: disabled
            p28 = re.compile(r'^\s*WCCP *Redirect *outbound:'
                              ' *(?P<wccp_redirect_outbound>[a-z]+)$')
            m = p28.match(line)
            if m:
                wccp_redirect_outbound = m.groupdict()['wccp_redirect_outbound']

                ip_interface_vrf_all_dict[interface]['wccp_redirect_outbound']\
                 = wccp_redirect_outbound
                continue

            #WCCP Redirect inbound: disabled
            p29 = re.compile(r'^\s*WCCP *Redirect *inbound:'
                              ' *(?P<wccp_redirect_inbound>[a-z]+)$')
            m = p29.match(line)
            if m:
                wccp_redirect_inbound = m.groupdict()['wccp_redirect_inbound']

                ip_interface_vrf_all_dict[interface]['wccp_redirect_inbound']\
                 = wccp_redirect_inbound
                continue

            #WCCP Redirect exclude: disabled
            p30 = re.compile(r'^\s*WCCP *Redirect *exclude:'
                              ' *(?P<wccp_redirect_exclude>[a-z]+)$')
            m = p30.match(line)
            if m:
                wccp_redirect_exclude = m.groupdict()['wccp_redirect_exclude']

                ip_interface_vrf_all_dict[interface]['wccp_redirect_exclude']\
                 = wccp_redirect_exclude
                continue

        return ip_interface_vrf_all_dict


#############################################################################
# Parser For Show Vrf All Interface
#############################################################################

class ShowVrfAllInterfaceSchema(MetaParser):

    schema = { 
                Any():
                    {'vrf': str,
                     'vrf_id': str,
                     'site_of_origin': str
                    },
                }
            

class ShowVrfAllInterface(ShowVrfAllInterfaceSchema):

    def cli(self):
        out = self.device.execute('show vrf all interface')

        vrf_all_interface_dict = {}

        for line in out.splitlines():
            line = line.rstrip()

            p1 = re.compile(r'^\s*(?P<interface>[a-zA-Z0-9\.\/]+)'
                             ' *(?P<vrf>[a-zA-Z0-9]+)'
                             ' *(?P<vrf_id>[0-9]+)'
                             ' *(?P<site_of_origin>[a-zA-Z\-]+)$')

            m = p1.match(line)
            if m:

                interface = m.groupdict()['interface']
                vrf = m.groupdict()['vrf']
                vrf_id = m.groupdict()['vrf_id']
                site_of_origin = m.groupdict()['site_of_origin']

                if interface not in vrf_all_interface_dict:
                    vrf_all_interface_dict[interface] = {}
                vrf_all_interface_dict[interface]['vrf'] = vrf
                vrf_all_interface_dict[interface]['vrf_id'] = vrf_id
                vrf_all_interface_dict[interface]\
                ['site_of_origin'] = site_of_origin

        return vrf_all_interface_dict

#############################################################################
# Parser For Show Ip Interface Switchport
#############################################################################


class ShowIpInterfaceSwitchportSchema(MetaParser):

    schema = {
        Any():
            {'switchport_status': str,
             'switchport_monitor': str,
             'switchport_mode': str,
             'access_vlan': int,
             'access_vlan_mode': str,
             'native_vlan': int,
             'native_vlan_mode': str,
             'trunk_vlans': str,
             'admin_priv_vlan_primary_host_assoc': str,
             'admin_priv_vlan_secondary_host_assoc': str,
             'admin_priv_vlan_primary_mapping': str,
             'admin_priv_vlan_secondary_mapping': str,
             'admin_priv_vlan_trunk_native_vlan': str,
             'admin_priv_vlan_trunk_encapsulation': str,
             'admin_priv_vlan_trunk_normal_vlans': str,
             'admin_priv_vlan_trunk_private_vlans': str,
             'operational_private_vlan': str
            },
        }
                    

class ShowIpInterfaceSwitchport(ShowIpInterfaceSwitchportSchema):

    def cli(self):
        out = self.device.execute('show ip interface switchport')

        ip_interface_switchport_dict = {}

        for line in out.splitlines():
            line = line.rstrip()

            #Name: Ethernet2/2
            p1 = re.compile(r'^\s*Name: *(?P<interface>[a-zA-Z0-9\/]+)$')
            m = p1.match(line)
            if m:
                interface = m.groupdict()['interface']

                if interface not in ip_interface_switchport_dict:
                    ip_interface_switchport_dict[interface] = {}
                    continue

            #Switchport: Enabled
            p2 = re.compile(r'^\s*Switchport: *(?P<switchport_status>[a-zA-Z\s]+)$')
            m = p2.match(line)
            if m:    
                switchport_status = m.groupdict()['switchport_status']

                ip_interface_switchport_dict[interface]['switchport_status'] = switchport_status  
                continue

            #Switchport Monitor: Not enabled
            p3 = re.compile(r'^\s*Switchport *Monitor: *(?P<switchport_monitor>[a-zA-Z\s]+)$')
            m = p3.match(line)
            if m:
                switchport_monitor = m.groupdict()['switchport_monitor']

                ip_interface_switchport_dict[interface]['switchport_monitor'] = switchport_monitor
                continue

            #Operational Mode: trunk
            p4 = re.compile(r'^\s*Operational *Mode: *(?P<switchport_mode>[a-z]+)$')
            m = p4.match(line)
            if m:
                switchport_mode = m.groupdict()['switchport_mode']
                if switchport_status == 'Enabled' and switchport_mode == 'trunk':
                    operation_mode = 'trunk' 

                    ip_interface_switchport_dict[interface]['switchport_mode'] = switchport_mode 
                    continue

            p4_1 = re.compile(r'^\s*Operational *Mode: *(?P<switchport_mode>[a-z]+)$')
            m = p4_1.match(line)
            if m:
                switchport_mode = m.groupdict()['switchport_mode']
                if switchport_status == 'Enabled' and switchport_mode == 'access':
                    operation_mode = 'access' 

                    ip_interface_switchport_dict[interface]['switchport_mode'] = switchport_mode 
                    continue

            p4_2 = re.compile(r'^\s*Operational *Mode: *(?P<switchport_mode>[a-z]+)$')
            m = p4_2.match(line)
            if m:
                switchport_mode = m.groupdict()['switchport_mode']
                if switchport_status == 'Disabled' and switchport_mode == 'access':
                    operation_mode = 'Disabled' 

                    ip_interface_switchport_dict[interface]['switchport_mode'] = switchport_mode 
                    continue

            p4_3 = re.compile(r'^\s*Operational *Mode: *(?P<switchport_mode>[a-z]+)$')
            m = p4_3.match(line)
            if m:
                switchport_mode = m.groupdict()['switchport_mode']
                if switchport_status == 'Disabled' and switchport_mode == 'access':
                    operation_mode = 'Disabled' 

                    ip_interface_switchport_dict[interface]['switchport_mode'] = switchport_mode 
                    continue

            #Access Mode VLAN: 1 (default)
            p5 = re.compile(r'^\s*Access *Mode *VLAN: *(?P<access_vlan>[0-9]+)'
                             ' *\((?P<access_vlan_mode>[a-zA-Z\s]+)\)$')
            m = p5.match(line)
            if m:
                access_vlan = int(m.groupdict()['access_vlan'])
                access_vlan_mode = m.groupdict()['access_vlan_mode']

                ip_interface_switchport_dict[interface]\
                ['access_vlan'] = access_vlan
                ip_interface_switchport_dict[interface]\
                ['access_vlan_mode'] = access_vlan_mode
                continue

            #Trunking Native Mode VLAN: 1 (default)
            p6 = re.compile(r'^\s*Trunking *Native *Mode *VLAN:'
                             ' *(?P<native_vlan>[0-9]+)'
                             ' *\((?P<native_vlan_mode>[a-z]+)\)$')
            m = p6.match(line)
            if m:
                native_vlan = int(m.groupdict()['native_vlan'])
                native_vlan_mode = m.groupdict()['native_vlan_mode']

                ip_interface_switchport_dict[interface]\
                ['native_vlan'] = native_vlan
                ip_interface_switchport_dict[interface]\
                ['native_vlan_mode'] = native_vlan_mode
                continue

            #Trunking VLANs Allowed: 100,300
            p7 = re.compile(r'^\s*Trunking *VLANs *Allowed: *(?P<trunk_vlans>[0-9\,\-]+)$')
            m = p7.match(line)
            if m:
                trunk_vlans = m.groupdict()['trunk_vlans']

                ip_interface_switchport_dict[interface]['trunk_vlans'] = trunk_vlans
                continue

            #Administrative private-vlan primary host-association: none
            p8 = re.compile(r'^\s*Administrative *private-vlan *primary'
                             ' *host-association:'
                             ' *(?P<admin_priv_vlan_primary_host_assoc>[a-z]+)$')
            m = p8.match(line)
            if m:
                admin_priv_vlan_primary_host_assoc = m.groupdict()['admin_priv_vlan_primary_host_assoc']

                ip_interface_switchport_dict[interface]['admin_priv_vlan_primary_host_assoc'] = admin_priv_vlan_primary_host_assoc
                continue

            #Administrative private-vlan secondary host-association: none
            p9 = re.compile(r'^\s*Administrative *private-vlan *secondary'
                             ' *host-association:'
                             ' *(?P<admin_priv_vlan_secondary_host_assoc>[a-z]+)$')
            m = p9.match(line)
            if m:
                admin_priv_vlan_secondary_host_assoc\
                 = m.groupdict()['admin_priv_vlan_secondary_host_assoc']

                ip_interface_switchport_dict[interface]\
                ['admin_priv_vlan_secondary_host_assoc'] = admin_priv_vlan_secondary_host_assoc
                continue

            #Administrative private-vlan primary mapping: none
            p10 = re.compile(r'^\s*Administrative *private-vlan *primary'
                             ' *mapping:'
                             ' *(?P<admin_priv_vlan_primary_mapping>[a-z]+)$')
            m = p10.match(line)
            if m:
                admin_priv_vlan_primary_mapping\
                 = m.groupdict()['admin_priv_vlan_primary_mapping']

                ip_interface_switchport_dict[interface]\
                ['admin_priv_vlan_primary_mapping']\
                 = admin_priv_vlan_primary_mapping
                continue

            #Administrative private-vlan secondary mapping: none
            p11 = re.compile(r'^\s*Administrative *private-vlan *secondary'
                             ' *mapping:'
                             ' *(?P<admin_priv_vlan_secondary_mapping>[a-z]+)$')
            m = p11.match(line)
            if m:
                admin_priv_vlan_secondary_mapping = m.groupdict()['admin_priv_vlan_secondary_mapping']

                ip_interface_switchport_dict[interface]['admin_priv_vlan_secondary_mapping'] = admin_priv_vlan_secondary_mapping
                continue

            #Administrative private-vlan trunk native VLAN: none
            p12 = re.compile(r'^\s*Administrative *private-vlan *trunk *native'
                             ' *VLAN:'
                             ' *(?P<admin_priv_vlan_trunk_native_vlan>[a-z]+)$')
            m = p12.match(line)
            if m:
                admin_priv_vlan_trunk_native_vlan = m.groupdict()['admin_priv_vlan_trunk_native_vlan']

                ip_interface_switchport_dict[interface]['admin_priv_vlan_trunk_native_vlan'] = admin_priv_vlan_trunk_native_vlan
                continue

            #Administrative private-vlan trunk encapsulation: dot1q
            p13 = re.compile(r'^\s*Administrative *private-vlan *trunk'
                             ' *encapsulation:'
                             ' *(?P<admin_priv_vlan_trunk_encapsulation>[a-z0-9]+)$')
            m = p13.match(line)
            if m:
                admin_priv_vlan_trunk_encapsulation = m.groupdict()['admin_priv_vlan_trunk_encapsulation']

                ip_interface_switchport_dict[interface]['admin_priv_vlan_trunk_encapsulation'] = admin_priv_vlan_trunk_encapsulation
                continue

            #Administrative private-vlan trunk normal VLANs: none
            p14 = re.compile(r'^\s*Administrative *private-vlan *trunk'
                             ' *normal VLANs:'
                             ' *(?P<admin_priv_vlan_trunk_normal_vlans>[a-z]+)$')
            m = p14.match(line)
            if m:
                admin_priv_vlan_trunk_normal_vlans = m.groupdict()['admin_priv_vlan_trunk_normal_vlans']

                ip_interface_switchport_dict[interface]['admin_priv_vlan_trunk_normal_vlans'] = admin_priv_vlan_trunk_normal_vlans
                continue

            #Administrative private-vlan trunk private VLANs: none
            p15 = re.compile(r'^\s*Administrative *private-vlan *trunk'
                             ' *private VLANs:'
                             ' *(?P<admin_priv_vlan_trunk_private_vlans>[a-z]+)$')
            m = p15.match(line)
            if m:
                admin_priv_vlan_trunk_private_vlans = m.groupdict()['admin_priv_vlan_trunk_private_vlans']

                ip_interface_switchport_dict[interface]['admin_priv_vlan_trunk_private_vlans'] = admin_priv_vlan_trunk_private_vlans
                continue

            #Operational private-vlan: none
            p16 = re.compile(r'^\s*Operational *private-vlan:'
                             ' *(?P<operational_private_vlan>[a-z]+)$')
            m = p16.match(line)
            if m:
                operational_private_vlan = m.groupdict()['operational_private_vlan']

                ip_interface_switchport_dict[interface]['operational_private_vlan'] = operational_private_vlan
                continue

        return ip_interface_switchport_dict











            














