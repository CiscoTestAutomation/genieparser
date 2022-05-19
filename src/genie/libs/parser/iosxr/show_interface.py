"""
    show_interface.py
    IOSXR parsers for the following show commands:

    * show ip interface brief | include {ip}
    * show ip interface brief
    * show ipv4 interface brief | include {ip}
    * show ipv4 interface brief
    * show ip interface brief | include Vlan
    * show interface brief
    * show interface detail
    * show vlan interface
    * show vrf all detail
    * show ipv4 vrf all interface
    * show ipv6 vrf all interface
    * show interfaces accounting
    * show interfaces
    * show interfaces <interface>
"""

# python
import re
import logging

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional, \
                                         Or, \
                                         And, \
                                         Default, \
                                         Use

# import parser utils
from genie.libs.parser.utils.common import Common

logger = logging.getLogger(__name__)


class ShowIpInterfaceBriefSchema(MetaParser):
    """Schema for show ip interface brief"""
    schema = {
        'interface': {
            Any(): {
                Optional('ip_address'): str,
                Optional('interface_status'): str,
                Optional('protocol_status'): str,
                Optional('vrf_name'): str
            }
        },
    }


class ShowIpInterfaceBrief(ShowIpInterfaceBriefSchema):
    """Parser for show ip interface brief"""
    # *************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    cli_command = ['show ip interface brief | include {ip}', 'show ip interface brief']

    def cli(self, ip='', output=None):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        '''
        if output is None:
            if ip:
                cmd = self.cli_command[0].format(ip=ip)
            else:
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)
        else:
            out = output

        # Loopback500                    192.168.220.1       Up              Up       default
        # BVI123                         10.12.34.56         Up              Up       MyOrg-MyGroup_Channel_Zone
        p = re.compile(r'^\s*(?P<interface>[a-zA-Z0-9\/\.\-]+) '
                       r'+(?P<ip_address>[a-z0-9\.]+) +(?P<interface_status>[a-zA-Z]+) '
                       r'+(?P<protocol_status>[a-zA-Z]+)( +(?P<vrf_name>[\w\:-]+))?$')

        interface_dict = {}
        for line in out.splitlines():
            line = line.rstrip()

            m = p.match(line)
            if m:
                group = m.groupdict()
                interface = group.pop('interface')

                if 'interface' not in interface_dict:
                    interface_dict['interface'] = {}
                if interface not in interface_dict['interface']:
                    interface_dict['interface'][interface] = {}

                interface_dict['interface'][interface].update(
                    {k: v for k, v in group.items() if v is not None})

                continue

        return interface_dict


class ShowIpv4InterfaceBrief(ShowIpInterfaceBrief):
    """Parser for
           show ipv4 interface brief | include {ip}
           show ipv4 interface brief
    """

    cli_command = ['show ipv4 interface brief | include {ip}',
                   'show ipv4 interface brief']

    def cli(self, ip='', output=None):
        if output is None:
            if ip:
                cmd = self.cli_command[0].format(ip=ip)
            else:
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)
        else:
            out = output

        return super().cli(output=out)


class ShowIpInterfaceBriefPipeVlan(ShowIpInterfaceBrief):
    """Parser for show ip interface brief | include Vlan"""
    #parser class - implements detail parsing mechanisms for cli output.

    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cmd = 'show ip interface brief | include Vlan'.format()

class ShowInterfaceBriefSchema(MetaParser):
    """Schema for show interface brief"""
    schema = {'interface':
                {Optional('ethernet'):
                    {Any():
                        {Optional('vlan'): str,
                         Optional('type'): str,
                         Optional('mode'): str,
                         'status': str,
                         Optional('speed'): str,
                         Optional('reason'): str,
                         Optional('encap_type'): str,
                         Optional('mtu'): str,
                         Optional('bw'): int,
                         Optional('port_ch'): str}
                    },
                Optional('port'):
                    {Any():
                        {Optional('vrf'): str,
                         Optional('status'): str,
                         Optional('ip_address'): str,
                         Optional('speed'): str,
                         Optional('encap_type'): str,
                         Optional('mtu'): str,
                         Optional('bw'): int,}
                    },
                Optional('port_channel'):
                    {Any():
                        {Optional('vlan'): str,
                         Optional('type'): str,
                         Optional('mode'): str,
                         Optional('status'): str,
                         Optional('speed'): str,
                         Optional('reason'): str,
                         Optional('encap_type'): str,
                         Optional('mtu'): str,
                         Optional('bw'): int,
                         Optional('protocol'): str}
                    },
                Optional('loopback'):
                    {Any():
                        {Optional('status'): str,
                         Optional('encap_type'): str,
                         Optional('mtu'): str,
                         Optional('bw'): int,
                         Optional('description'): str}
                    },
                }
            }


class ShowInterfaceBrief(ShowInterfaceBriefSchema):
    """Parser for show interface brief"""
    # parser class - implements detail parsing mechanisms for cli output.

    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cmd = 'show interface brief'.format()

    cli_command = 'show interface brief'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

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

            p2 = re.compile(r'^\s*(?P<port>[a-zA-Z0-9\/\.]+)'
                             ' +(?P<vrf>[a-zA-Z0-9\-]+)'
                             ' +(?P<status>[a-zA-Z\-]+) +(?P<ip_address>[0-9\.]+)'
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


            p9 = re.compile(r'^\s*(?P<interface>[a-zA-Z0-9\/]+)'
                             ' +(?P<intf_state>[a-zA-Z0-9\-]+)'
                             ' +(?P<line_state>[a-zA-Z0-9\-]+)'
                             ' +(?P<type>[a-zA-Z]+)'
                             ' +(?P<mtu>\d+)'
                             ' +(?P<bw>\d+)$')
            m = p9.match(line)
            if m:
                group = m.groupdict()
                interface = Common.convert_intf_name(group['interface'])
                sub_dict = interface_dict.setdefault('interface', {})
                if 'Lo' in interface:
                    intf_dict = sub_dict.setdefault('loopback', {}).setdefault(interface, {})
                if 'Po' in interface:
                    intf_dict = sub_dict.setdefault('port_channel', {}).setdefault(interface, {})
                if 'Eth' in interface:
                    intf_dict = sub_dict.setdefault('ethernet', {}).setdefault(interface, {})
                else:
                    intf_dict = sub_dict.setdefault('port', {}).setdefault(interface, {})
                intf_dict['status'] = group['intf_state']
                intf_dict['encap_type'] = group['type']
                intf_dict['mtu'] = group['mtu']
                intf_dict['bw'] = int(group['bw'])
                continue


        return interface_dict

################################################################################

#############################################################################
# Parser For Show Interfaces detail
#############################################################################


class ShowInterfacesDetailSchema(MetaParser):
    """Schema for show interfaces detail"""

    schema = {
        Any():
            {Optional('description'): str,
             Optional('types'): str,
             Optional('phys_address'): str,
             Optional('port_speed'): str,
             Optional('mtu'): int,
             Optional('line_protocol'): str,
             Optional('oper_status'): str,
             Optional('enabled'): bool,
             Optional('mac_address'): str,
             Optional('auto_negotiate'): bool,
             Optional('duplex_mode'): str,
             Optional('location'): str,
             Optional('medium'): str,
             Optional('txload'): str,
             Optional('rxload'): str,
             Optional('last_input'): str,
             Optional('last_output'): str,
             Optional('last_link_flapped'): str,
             Optional('arp_type'): str,
             Optional('arp_timeout'): str,
             Optional('loopback_status'): str,
             Optional('reliability'): str,
             Optional('interface_state'): int,
             Optional('carrier_delay'): str,
             Optional('flow_control'):
               {Optional('flow_control_receive'): bool,
                Optional('flow_control_send'): bool,
             },
             Optional('bandwidth'): int,
             Optional('counters'):
                {Optional('rate'):
                    {Optional('load_interval'): int,
                     Optional('in_rate'): int,
                     Optional('in_rate_pkts'): int,
                     Optional('out_rate'): int,
                     Optional('out_rate_pkts'): int,
                    },
                Optional('in_discards'): int,
                Optional('in_unknown_protos'): int,
                Optional('in_octets'): int,
                Optional('in_pkts'): int,
                Optional('in_multicast_pkts'): int,
                Optional('in_broadcast_pkts'): int,
                Optional('in_runts'): int,
                Optional('in_giants'): int,
                Optional('in_throttles'): int,
                Optional('in_parity'): int,
                Optional('in_frame_errors'): int,
                Optional('in_crc_errors'): int,
                Optional('in_frame'): int,
                Optional('in_overrun'): int,
                Optional('in_ignored'): int,
                Optional('in_abort'): int,
                Optional('out_pkts'): int,
                Optional('out_octets'): int,
                Optional('out_discards'): int,
                Optional('out_broadcast_pkts'): int,
                Optional('out_multicast_pkts'): int,
                Optional('out_errors'): int,
                Optional('out_underruns'): int,
                Optional('out_applique'): int,
                Optional('out_resets'): int,
                Optional('out_buffer_failures'): int,
                Optional('out_buffer_swapped_out'): int,
                Optional('last_clear'): str,
                Optional('carrier_transitions'): int,
                },
             Optional('encapsulations'):
                {Optional('encapsulation'): str,
                 Optional('first_dot1q'): str,
                 Optional('second_dot1q'): str
                },
             Optional('ipv4'):
                {Any():
                    {Optional('ip'): str,
                     Optional('prefix_length'): str
                    },
                },
            },
        }


class ShowInterfacesDetail(ShowInterfacesDetailSchema):
    """Parser for show interface detail
                    show interface <interface> detail
    """

    cli_command = ['show interface detail', 'show interface {interface} detail']
    exclude = ['in_octets', 'in_pkts', 'out_octets', 'out_pkts', 'in_rate',
        'in_rate_pkts', 'out_rate', 'out_rate_pkts', 'last_link_flapped', 'in_multicast_pkts',
        'out_multicast_pkts', 'last_input', 'last_output', 'in_crc_errors', 'in_frame_errors',
        'reliability', 'in_discards', 'in_broadcast_pkts', 'out_broadcast_pkts', 'rxload', 'txload',
        'interface_state', 'in_unknown_protos', 'last_clear', 'carrier_transitions', 'in_giants']


    def cli(self, interface='', output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[1].format(interface=interface)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        interface_detail_dict = {}

        # it's supported for NCS500 that output has non utf8 character
        if "non_utf-8_character b'" in out:
            out = out.split("non_utf-8_character b'")[1]

        elif "b'" in out:
            out = out.split("b'")[1]

        for line in out.splitlines():
            line = line.strip()

            # MgmtEth0/0/CPU0/0 is administratively down, line protocol is administratively down
            p1 = re.compile(r'^\s*(?P<interface>[a-zA-Z0-9\/\.\-]+) +is'
                             ' +(?P<enabled>(administratively down|down))(?:,'
                             ' +line +protocol +is +(?P<line_protocol>'
                             '(administratively down|down)))?$')
            m = p1.match(line)
            if m:
                interface = m.groupdict()['interface']
                enabled = m.groupdict()['enabled']
                line_protocol = m.groupdict()['line_protocol']

                if interface not in interface_detail_dict:
                    interface_detail_dict[interface] = {}
                interface_detail_dict[interface]['line_protocol'] = line_protocol
                interface_detail_dict[interface]['oper_status'] = 'down'
                interface_detail_dict[interface]['enabled'] = False
                continue

            p1_1 = re.compile(r'^\s*(?P<interface>[a-zA-Z0-9\/\.\-]+) +is'
                               ' +(?P<enabled>(administratively up|up))(?:,'
                               ' +line +protocol +is +(?P<line_protocol>'
                               '(administratively up|up)))?$')
            m = p1_1.match(line)
            if m:
                interface = m.groupdict()['interface']
                enabled = m.groupdict()['enabled']
                line_protocol = m.groupdict()['line_protocol']

                if interface not in interface_detail_dict:
                    interface_detail_dict[interface] = {}
                interface_detail_dict[interface]['line_protocol'] = line_protocol
                interface_detail_dict[interface]['oper_status'] = 'up'
                interface_detail_dict[interface]['enabled'] = True
                continue

            # Interface state transitions: 1
            p2 = re.compile(r'^\s*Interface +state +transitions:'
                             ' +(?P<interface_state>[0-9]+)$')
            m = p2.match(line)
            if m:
                interface_state = int(m.groupdict()['interface_state'])
                interface_detail_dict[interface]['interface_state'] = interface_state
                continue

            # Hardware is Null interface
            # Hardware is Management Ethernet, address is 5254.00ff.3007 (bia 5254.00ff.3007)

            p3 = re.compile(r'^\s*Hardware is (?P<types>[a-zA-Z\,\s]+)(?:'
                             ' +address +is (?P<mac_address>[a-z0-9\.]+) +\(bia'
                             ' +(?P<phys_address>[a-z0-9\.]+)\))?$')
            m = p3.match(line)
            if m:
                types = m.groupdict()['types'].lower()
                types = types.replace(",","")
                types = types.replace("interface","")
                types = types.strip()
                mac_address = m.groupdict()['mac_address']
                phys_address = m.groupdict()['phys_address']

                interface_detail_dict[interface]['types'] = types
                if mac_address:
                    interface_detail_dict[interface]['mac_address'] = str(m.groupdict()['mac_address'])
                if phys_address:
                    interface_detail_dict[interface]['phys_address'] = str(m.groupdict()['phys_address'])
                continue

            # Hardware is VLAN sub-interface(s), address is aaaa.bbff.8888
            p3_1 = re.compile(r'^\s*Hardware is (?P<types>[\w\W]+) +address'
                               ' +is +(?P<mac_address>[a-z0-9\.]+)$')
            m = p3_1.match(line)
            if m:
                types = m.groupdict()['types'].lower()
                types = types.replace(",","")
                types = types.replace("interface","")
                mac_address = m.groupdict()['mac_address']

                interface_detail_dict[interface]['types'] = types
                if mac_address:
                    interface_detail_dict[interface]['mac_address'] = str(m.groupdict()['mac_address'])
                continue

            #Description: desc
            p3_2 = re.compile(r'^\s*Description: +(?P<description>[\w\W]+)$')
            m = p3_2.match(line)
            if m:
                interface_detail_dict[interface]['description']\
                = str(m.groupdict()['description'])
                continue

            # Internet address is 10.1.1.1/24
            p4 = re.compile(r'^\s*Internet +address +is +(?P<ip>[a-z0-9\.]+)'
                             '(\/(?P<prefix_length>[0-9]+))?$')
            m = p4.match(line)
            if m:
                ip = m.groupdict()['ip']
                prefix_length = m.groupdict()['prefix_length']

                address = ip + '/' + prefix_length
                if 'ipv4' not in interface_detail_dict[interface]:
                    interface_detail_dict[interface]['ipv4'] = {}
                if address not in interface_detail_dict[interface]['ipv4']:
                    interface_detail_dict[interface]['ipv4'][address] = {}

                interface_detail_dict[interface]['ipv4'][address]['ip'] = ip
                interface_detail_dict[interface]['ipv4'][address]\
                ['prefix_length'] = prefix_length
                continue

            # MTU 1500 bytes, BW 0 Kbit (Max: 1000000 Kbit)
            # MTU 6000 bytes, BW 20000000 Kbit (Max: 20000000 Kbit)
            p5 = re.compile(r'^\s*MTU +(?P<mtu>[0-9]+) +bytes, +BW'
                             ' +(?P<bandwidth>[0-9]+) +Kbit(?: *\(Max: +\d+'
                             ' +Kbit\))?$')
            m = p5.match(line)
            if m:
                mtu = int(m.groupdict()['mtu'])
                bandwidth = int(m.groupdict()['bandwidth'])

                interface_detail_dict[interface]['mtu'] = mtu
                interface_detail_dict[interface]['bandwidth'] = bandwidth
                continue

            # reliability 255/255, txload Unknown, rxload Unknown
            p6 = re.compile(r'^\s*reliability +(?P<reliability>[a-zA-Z0-9\/]+),'
                             ' +txload +(?P<txload>[a-zA-Z0-9\/]+), +rxload'
                             ' +(?P<rxload>[a-zA-Z0-9\/]+)$')
            m = p6.match(line)
            if m:
                reliability = m.groupdict()['reliability']
                txload = m.groupdict()['txload'].lower()
                rxload = m.groupdict()['rxload'].lower()

                interface_detail_dict[interface]['reliability'] = reliability
                interface_detail_dict[interface]['txload'] = txload
                interface_detail_dict[interface]['rxload'] = rxload
                continue

            # Encapsulation 802.1Q Virtual LAN, VLAN Id 10, 2nd VLAN Id 10,
            p7 = re.compile(r'^\s*Encapsulation +(?P<encapsulation>[a-zA-Z0-9\.\s]+),'
                             ' +VLAN +Id +(?P<first_dot1q>[0-9]+), +2nd +VLAN'
                             ' +Id +(?P<second_dot1q>[0-9]+),$')
            m = p7.match(line)
            if m:
                encapsulation = str(m.groupdict()['encapsulation']).lower()

                if 'encapsulations' not in interface_detail_dict[interface]:
                    interface_detail_dict[interface]['encapsulations'] = {}

                interface_detail_dict[interface]['encapsulations']\
                ['encapsulation'] = encapsulation
                interface_detail_dict[interface]['encapsulations']\
                ['first_dot1q'] = str(m.groupdict()['first_dot1q'])
                interface_detail_dict[interface]['encapsulations']\
                ['second_dot1q'] = str(m.groupdict()['second_dot1q'])
                continue

            # Encapsulation 802.1Q Virtual LAN, VLAN Id 20,  loopback not set,
            p7_1 = re.compile(r'^\s*Encapsulation +(?P<encapsulation>[a-zA-Z0-9\.\s]+),'
                               ' +VLAN +Id +(?P<first_dot1q>[0-9]+), +loopback'
                               ' +(?P<loopback_status>[a-zA-Z\s]+),$')
            m = p7_1.match(line)
            if m:
                encapsulation = str(m.groupdict()['encapsulation']).lower()
                loopback_status = str(m.groupdict()['loopback_status'])

                if 'encapsulations' not in interface_detail_dict[interface]:
                    interface_detail_dict[interface]['encapsulations'] = {}

                interface_detail_dict[interface]['encapsulations']\
                ['encapsulation'] = encapsulation
                interface_detail_dict[interface]['encapsulations']\
                ['first_dot1q'] = str(m.groupdict()['first_dot1q'])

                if loopback_status != "not set":
                    interface_detail_dict[interface]['loopback_status']\
                    = m.groupdict()['loopback_status']
                continue

            p7_2 = re.compile(r'^\s*Encapsulation +(?P<encapsulation>[a-zA-Z0-9\.\s]+),'
                               ' +VLAN +Id +(?P<first_dot1q>[0-9]+), +2nd +VLAN +Id'
                               ' +(?P<second_dot1q>[0-9]+),(?: +loopback'
                               ' +(?P<loopback_status>[a-zA-Z\s]+),)?$')
            m = p7_2.match(line)
            if m:
                encapsulation = str(m.groupdict()['encapsulation']).lower()
                loopback_status = str(m.groupdict()['loopback_status'])

                if 'encapsulations' not in interface_detail_dict[interface]:
                    interface_detail_dict[interface]['encapsulations'] = {}

                interface_detail_dict[interface]['encapsulations']\
                ['encapsulation'] = encapsulation
                interface_detail_dict[interface]['encapsulations']\
                ['first_dot1q'] = str(m.groupdict()['first_dot1q'])
                interface_detail_dict[interface]['encapsulations']\
                ['second_dot1q'] = str(m.groupdict()['second_dot1q'])

                if loopback_status != "not set":
                    interface_detail_dict[interface]['loopback_status']\
                    = m.groupdict()['loopback_status']
                continue

            # Encapsulation ARPA,
            p7_3 = re.compile(r'^\s*Encapsulation +(?P<encapsulation>[a-zA-Z0-9\.\s]+),$')
            m = p7_3.match(line)
            if m:
                encapsulation = str(m.groupdict()['encapsulation']).lower()

                if 'encapsulations' not in interface_detail_dict[interface]:
                    interface_detail_dict[interface]['encapsulations'] = {}

                interface_detail_dict[interface]['encapsulations']\
                ['encapsulation'] = encapsulation
                continue

            # Encapsulation Null,  loopback not set,
            p7_4 = re.compile(r'^\s*Encapsulation +(?P<encapsulation>[a-zA-Z0-9\.\s]+),'
                               ' +loopback +(?P<loopback_status>[a-zA-Z\s]+),$')
            m = p7_4.match(line)
            if m:
                encapsulation = str(m.groupdict()['encapsulation']).lower()
                loopback_status = str(m.groupdict()['loopback_status'])


                if 'encapsulations' not in interface_detail_dict[interface]:
                    interface_detail_dict[interface]['encapsulations'] = {}

                interface_detail_dict[interface]['encapsulations']\
                ['encapsulation'] = encapsulation

                if loopback_status != "not set":
                    interface_detail_dict[interface]['loopback_status']\
                    = m.groupdict()['loopback_status']
                continue

            # loopback not set,
            p7_5 = re.compile(r'^\s*loopback +(?P<loopback_status>[a-zA-Z\s]+),$')
            m = p7_5.match(line)
            if m:
                loopback_status = str(m.groupdict()['loopback_status'])

                if loopback_status != "not set":
                    interface_detail_dict[interface]['loopback_status']\
                    = m.groupdict()['loopback_status']
                continue

            # Last input never, output never
            p8 = re.compile(r'^\s*Last +input +(?P<last_input>[\w\W]+),'
                             ' +output +(?P<last_output>[\w\W]+)$')
            m = p8.match(line)
            if m:
                interface_detail_dict[interface]['last_input']\
                 = m.groupdict()['last_input']
                interface_detail_dict[interface]['last_output']\
                 = m.groupdict()['last_output']
                continue

            # ARP type ARPA, ARP timeout 04:00:00
            p8_1 = re.compile(r'^\s*ARP +type +(?P<arp_type>\S+), +ARP +timeout'
                               ' +(?P<arp_timeout>\S+)')
            m = p8_1.match(line)
            if m:
                arp_type = str(m.groupdict()['arp_type']).lower()

                interface_detail_dict[interface]['arp_type']\
                 = arp_type
                interface_detail_dict[interface]['arp_timeout']\
                 = m.groupdict()['arp_timeout']
                continue

            p8_2 = re.compile(r'^\s*Last +link +flapped +(?P<last_link_flapped>\S+)$')
            m = p8_2.match(line)
            if m:
                interface_detail_dict[interface]['last_link_flapped']\
                 = m.groupdict()['last_link_flapped']
                continue

            # Last clearing of "show interface" counters never
            p8_3 = re.compile(r'^\s*Last +clearing +of +"show interface"'
                               ' +counters +(?P<last_clear>[\w\W]+)$')
            m = p8_3.match(line)
            if m:
                last_clear = str(m.groupdict()['last_clear'])
                continue

            # 5 minute input rate 0 bits/sec, 0 packets/sec
            p9 = re.compile(r'^\s*(?P<load_interval>[0-9]+) +(?P<timecheck>minute|second|)'
                             ' +input +rate +(?P<in_rate>[0-9]+) +bits/sec,'
                             ' +(?P<in_rate_pkts>[0-9]+) +packets/sec$')
            m = p9.match(line)
            if m:
                load_interval = int(m.groupdict()['load_interval'])
                in_rate = int(m.groupdict()['in_rate'])
                in_rate_pkts = int(m.groupdict()['in_rate_pkts'])
                timecheck = str(m.groupdict()['timecheck'])

                if timecheck == "minute":
                    load_interval = load_interval * 60

                if 'counters' not in interface_detail_dict[interface]:
                    interface_detail_dict[interface]['counters'] = {}
                if 'rate' not in interface_detail_dict[interface]['counters']:
                    interface_detail_dict[interface]['counters']['rate'] = {}

                interface_detail_dict[interface]['counters']['rate']\
                ['load_interval'] = load_interval
                interface_detail_dict[interface]['counters']['rate']\
                ['in_rate'] = in_rate
                interface_detail_dict[interface]['counters']['rate']\
                ['in_rate_pkts'] = in_rate_pkts
                interface_detail_dict[interface]['counters']\
                ['last_clear'] = last_clear
                continue

            # Full-duplex, 1000Mb/s, unknown, link type is autonegotiation
            # Duplex unknown, 0Kb/s, unknown, link type is autonegotiation
            p9_1 = re.compile(r'^\s*(?P<duplex_mode>[\w\W]+), +(?P<port_speed>\S+)(Mb/s|Kb/s|Gb/s),'
                               ' +(?P<location>\S+), +link +type +is'
                               ' +(?P<auto_negotiate>(autonegotiation))$')
            m = p9_1.match(line)
            if m:
                auto_negotiate = m.groupdict()['auto_negotiate']
                duplex_mode = str(m.groupdict()['duplex_mode']).lower()
                duplex_mode = duplex_mode.replace("-duplex","")

                interface_detail_dict[interface]['duplex_mode'] = duplex_mode
                interface_detail_dict[interface]['port_speed'] = str(m.groupdict()['port_speed'])
                interface_detail_dict[interface]['location'] = str(m.groupdict()['location'])
                interface_detail_dict[interface]['auto_negotiate'] = True
                continue

            p9_2 = re.compile(r'^\s*(?P<duplex_mode>[\w\W]+), +(?P<port_speed>\S+),'
                               ' +(?P<location>\S+), +link +type +is +(?P<auto_negotiate>(force-up))$')
            m = p9_2.match(line)
            if m:
                auto_negotiate = m.groupdict()['auto_negotiate']
                duplex_mode = str(m.groupdict()['duplex_mode']).lower()
                duplex_mode = duplex_mode.replace("-duplex","")

                interface_detail_dict[interface]['duplex_mode'] = duplex_mode
                interface_detail_dict[interface]['port_speed'] = str(m.groupdict()['port_speed'])
                interface_detail_dict[interface]['location'] = str(m.groupdict()['location'])
                interface_detail_dict[interface]['auto_negotiate'] = False
                continue

            # output flow control is off, input flow control is off
            p9_3 = re.compile(r'^\s*output +flow +control +is +(?P<flow_control_send>(off)),'
                               ' +input +flow +control +is +(?P<flow_control_receive>(off))$')
            m = p9_3.match(line)
            if m:
                flow_control_send = m.groupdict()['flow_control_send']
                flow_control_receive = m.groupdict()['flow_control_receive']

                if 'flow_control' not in interface_detail_dict[interface]:
                    interface_detail_dict[interface]['flow_control'] = {}

                interface_detail_dict[interface]['flow_control']['flow_control_send'] = False
                interface_detail_dict[interface]['flow_control']['flow_control_receive'] = False
                continue

            p9_4 = re.compile(r'^\s*output +flow +control +is +(?P<flow_control_send>(on)),'
                               ' +input +flow +control +is +(?P<flow_control_receive>(on))$')
            m = p9_4.match(line)
            if m:
                flow_control_send = m.groupdict()['flow_control_send']
                flow_control_receive = m.groupdict()['flow_control_receive']

                if 'flow_control' not in interface_detail_dict[interface]:
                    interface_detail_dict[interface]['flow_control'] = {}

                interface_detail_dict[interface]['flow_control']['flow_control_send'] = True
                interface_detail_dict[interface]['flow_control']['flow_control_receive'] = True
                continue

            p9_5 = re.compile(r'^\s*output +flow +control +is +(?P<flow_control_send>(on)),'
                               ' +input +flow +control +is +(?P<flow_control_receive>(off))$')
            m = p9_5.match(line)
            if m:
                flow_control_send = m.groupdict()['flow_control_send']
                flow_control_receive = m.groupdict()['flow_control_receive']

                if 'flow_control' not in interface_detail_dict[interface]:
                    interface_detail_dict[interface]['flow_control'] = {}

                interface_detail_dict[interface]['flow_control']['flow_control_send'] = True
                interface_detail_dict[interface]['flow_control']['flow_control_receive'] = False
                continue

            p9_6 = re.compile(r'^\s*output +flow +control +is +(?P<flow_control_send>(off)),'
                               ' +input +flow +control +is +(?P<flow_control_receive>(on))$')
            m = p9_6.match(line)
            if m:
                flow_control_send = m.groupdict()['flow_control_send']
                flow_control_receive = m.groupdict()['flow_control_receive']

                if 'flow_control' not in interface_detail_dict[interface]:
                    interface_detail_dict[interface]['flow_control'] = {}

                interface_detail_dict[interface]['flow_control']['flow_control_send'] = False
                interface_detail_dict[interface]['flow_control']['flow_control_receive'] = True
                continue

            # Carrier delay (up) is 10 msec
            p9_7 = re.compile(r'^\s*Carrier +delay +\(up\) +is'
                               ' +(?P<carrier_delay>[0-9]+) +msec$')
            m = p9_7.match(line)
            if m:
                carrier_delay = m.groupdict()['carrier_delay']

                interface_detail_dict[interface]['carrier_delay'] = carrier_delay
                continue

            # 5 minute output rate 0 bits/sec, 0 packets/sec
            p10 = re.compile(r'^\s*(?P<load_interval>[0-9]+) +(?P<timecheck>minute|second|)'
                              ' +output +rate +(?P<out_rate>[0-9]+) +bits/sec,'
                              ' +(?P<out_rate_pkts>[0-9]+) +packets/sec$')
            m = p10.match(line)
            if m:
                load_interval = int(m.groupdict()['load_interval'])
                out_rate = int(m.groupdict()['out_rate'])
                out_rate_pkts = int(m.groupdict()['out_rate_pkts'])
                timecheck = str(m.groupdict()['timecheck'])

                if timecheck == "minute":
                    load_interval = load_interval * 60

                if 'counters' not in interface_detail_dict[interface]:
                    interface_detail_dict[interface]['counters'] = {}
                if 'rate' not in interface_detail_dict[interface]['counters']:
                    interface_detail_dict[interface]['counters']['rate'] = {}

                interface_detail_dict[interface]['counters']['rate']\
                ['load_interval'] = load_interval
                interface_detail_dict[interface]['counters']['rate']\
                ['out_rate'] = out_rate
                interface_detail_dict[interface]['counters']['rate']\
                ['out_rate_pkts'] = out_rate_pkts
                continue

            # 0 packets input, 0 bytes, 0 total input drops
            p11 = re.compile(r'^\s*(?P<in_pkts>[0-9]+) +packets +input,'
                              ' +(?P<in_octets>[0-9]+) +bytes, +(?P<in_discards>[0-9]+)'
                              ' +total +input +drops$')
            m = p11.match(line)
            if m:
                in_pkts = int(m.groupdict()['in_pkts'])
                in_octets = int(m.groupdict()['in_octets'])
                in_discards = int(m.groupdict()['in_discards'])

                interface_detail_dict[interface]['counters']\
                ['in_pkts'] = in_pkts
                interface_detail_dict[interface]['counters']\
                ['in_octets'] = in_octets
                interface_detail_dict[interface]['counters']\
                ['in_discards'] = in_discards
                continue

            # 0 drops for unrecognized upper-level protocol
            p12 = re.compile(r'^\s*(?P<in_unknown_protos>[0-9]+) +drops +for +unrecognized'
                              ' +upper-level +protocol$')
            m = p12.match(line)
            if m:
                interface_detail_dict[interface]['counters']\
                ['in_unknown_protos'] = int(m.groupdict()['in_unknown_protos'])
                continue

            # Received 0 broadcast packets, 0 multicast packets
            p13 = re.compile(r'^\s*Received +(?P<in_broadcast_pkts>[0-9]+)'
                              ' +broadcast +packets, +(?P<in_multicast_pkts>[0-9]+)'
                              ' +multicast +packets$')
            m = p13.match(line)
            if m:
                interface_detail_dict[interface]['counters']\
                ['in_broadcast_pkts'] = int(m.groupdict()['in_broadcast_pkts'])
                interface_detail_dict[interface]['counters']\
                ['in_multicast_pkts'] = int(m.groupdict()['in_multicast_pkts'])
                continue

            # 0 runts, 0 giants, 0 throttles, 0 parity
            p14 = re.compile(r'^\s*(?P<in_runts>[0-9]+) +runts, +(?P<in_giants>[0-9]+)'
                              ' +giants, +(?P<in_throttles>[0-9]+) +throttles,'
                              ' +(?P<in_parity>[0-9]+) parity$')
            m = p14.match(line)
            if m:
                interface_detail_dict[interface]['counters']\
                ['in_runts'] = int(m.groupdict()['in_runts'])
                interface_detail_dict[interface]['counters']\
                ['in_giants'] = int(m.groupdict()['in_giants'])
                interface_detail_dict[interface]['counters']\
                ['in_throttles'] = int(m.groupdict()['in_throttles'])
                interface_detail_dict[interface]['counters']\
                ['in_parity'] = int(m.groupdict()['in_parity'])
                continue

            # 0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
            p15 = re.compile(r'^\s*(?P<in_frame_errors>[0-9]+) +input +errors,'
                              ' +(?P<in_crc_errors>[0-9]+) +CRC,'
                              ' +(?P<in_frame>[0-9]+)'
                              ' +frame, +(?P<in_overrun>[0-9]+) +overrun,'
                              ' +(?P<in_ignored>[0-9]+) +ignored,'
                              ' +(?P<in_abort>[0-9]+) +abort$')
            m = p15.match(line)
            if m:
                interface_detail_dict[interface]['counters']\
                ['in_frame_errors'] = int(m.groupdict()['in_frame_errors'])
                interface_detail_dict[interface]['counters']\
                ['in_crc_errors'] = int(m.groupdict()['in_crc_errors'])
                interface_detail_dict[interface]['counters']\
                ['in_frame'] = int(m.groupdict()['in_frame'])
                interface_detail_dict[interface]['counters']\
                ['in_overrun'] = int(m.groupdict()['in_overrun'])
                interface_detail_dict[interface]['counters']\
                ['in_ignored'] = int(m.groupdict()['in_ignored'])
                interface_detail_dict[interface]['counters']\
                ['in_abort'] = int(m.groupdict()['in_abort'])
                continue

            # 0 packets output, 0 bytes, 0 total output drops
            p16 = re.compile(r'^\s*(?P<out_pkts>[0-9]+) +packets +output,'
                              ' +(?P<out_octets>[0-9]+) +bytes, +(?P<out_discards>[0-9]+)'
                              ' +total +output +drops$')
            m = p16.match(line)
            if m:
                interface_detail_dict[interface].setdefault('counters', {})
                interface_detail_dict[interface]['counters']\
                ['out_pkts'] = int(m.groupdict()['out_pkts'])
                interface_detail_dict[interface]['counters']\
                ['out_octets'] = int(m.groupdict()['out_octets'])
                interface_detail_dict[interface]['counters']\
                ['out_discards'] = int(m.groupdict()['out_discards'])
                continue

            # Output 0 broadcast packets, 0 multicast packets
            p17 = re.compile(r'^\s*Output +(?P<out_broadcast_pkts>[0-9]+)'
                              ' +broadcast +packets, +(?P<out_multicast_pkts>[0-9]+)'
                              ' +multicast +packets$')
            m = p17.match(line)
            if m:
                interface_detail_dict[interface]['counters']\
                ['out_broadcast_pkts'] = int(m.groupdict()['out_broadcast_pkts'])
                interface_detail_dict[interface]['counters']\
                ['out_multicast_pkts'] = int(m.groupdict()['out_multicast_pkts'])
                continue

            # 0 output errors, 0 underruns, 0 applique, 0 resets
            p18 = re.compile(r'^\s*(?P<out_errors>[0-9]+) +output +errors,'
                              ' +(?P<out_underruns>[0-9]+) +underruns,'
                              ' +(?P<out_applique>[0-9]+) +applique,'
                              ' +(?P<out_resets>[0-9]+) +resets$')
            m = p18.match(line)
            if m:
                interface_detail_dict[interface]['counters']\
                ['out_errors'] = int(m.groupdict()['out_errors'])
                interface_detail_dict[interface]['counters']\
                ['out_underruns'] = int(m.groupdict()['out_underruns'])
                interface_detail_dict[interface]['counters']\
                ['out_applique'] = int(m.groupdict()['out_applique'])
                interface_detail_dict[interface]['counters']\
                ['out_resets'] = int(m.groupdict()['out_resets'])
                continue

            # 0 output buffer failures, 0 output buffers swapped out
            p19 = re.compile(r'^\s*(?P<out_buffer_failures>[0-9]+) +output'
                              ' +buffer +failures, +(?P<out_buffer_swapped_out>[0-9]+)'
                              ' +output +buffers +swapped +out$')
            m = p19.match(line)
            if m:
                interface_detail_dict[interface]['counters']\
                ['out_buffer_failures'] = int(m.groupdict()['out_buffer_failures'])
                interface_detail_dict[interface]['counters']\
                ['out_buffer_swapped_out'] = int(m.groupdict()['out_buffer_swapped_out'])
                continue

            # 0 carrier transitions
            p20 = re.compile(r'^\s*(?P<carrier_transitions>[0-9]+) +carrier +transitions$')
            m = p20.match(line)
            if m:
                interface_detail_dict[interface]['counters']\
                ['carrier_transitions'] = int(m.groupdict()['carrier_transitions'])
                continue

        return interface_detail_dict

#############################################################################
# Parser For Show vlan interface
#############################################################################

class ShowVlanInterfaceSchema(MetaParser):
    """Schema for show vlan interface"""

    schema = {
        Any():
            {Optional('encapsulation'): str,
            Optional('outer_vlan'): int,
            Optional('second_vlan'): str,
            Optional('service'): str,
            Optional('mtu'): int,
            Optional('linep_state'): str
            },
        }

class ShowVlanInterface(ShowVlanInterfaceSchema):
    """Parser for show vlan interface"""

    cli_command = 'show vlan interface'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        vlan_interface_dict = {}

        for line in out.splitlines():
            line = line.rstrip()
            p1 = re.compile(r'^\s*(?P<interface>[a-zA-Z0-9\/\.]+)'
                             ' +(?P<encapsulation>[A-Z0-9\.]+)'
                             ' +(?P<outer_vlan>[0-9]+)(?: +(?P<second_vlan>[0-9]+))?'
                             ' +(?P<service>[A-Z0-9]+) +(?P<mtu>[0-9]+)'
                             ' +(?P<linep_state>\S+)$')
            m = p1.match(line)
            if m:
                interface = m.groupdict()['interface']
                encapsulation = str(m.groupdict()['encapsulation'])
                outer_vlan = int(m.groupdict()['outer_vlan'])
                second_vlan = m.groupdict()['second_vlan']
                service = str(m.groupdict()['service'])
                mtu = int(m.groupdict()['mtu'])
                linep_state = str(m.groupdict()['linep_state'])

                if interface not in vlan_interface_dict:
                    vlan_interface_dict[interface] = {}
                vlan_interface_dict[interface]['encapsulation'] = encapsulation
                vlan_interface_dict[interface]['outer_vlan'] = outer_vlan
                if second_vlan:
                    vlan_interface_dict[interface]['second_vlan'] = str(m.groupdict()['second_vlan'])
                vlan_interface_dict[interface]['service'] = service
                vlan_interface_dict[interface]['mtu'] = mtu
                vlan_interface_dict[interface]['linep_state'] = linep_state
                continue

            p1_1 = re.compile(r'^\s*(?P<interface>[a-zA-Z0-9\/\.]+)'
                               ' +(?P<encapsulation>[a-zA-Z]+ [A-Z0-9\.]+)'
                               ' +(?P<outer_vlan>[0-9]+)(?: +(?P<second_vlan>[0-9]+))?'
                               ' +(?P<service>[A-Z0-9]+) +(?P<mtu>[0-9]+)'
                               ' +(?P<linep_state>\S+)$')
            m = p1_1.match(line)
            if m:
                interface = m.groupdict()['interface']
                encapsulation = str(m.groupdict()['encapsulation'])
                outer_vlan = int(m.groupdict()['outer_vlan'])
                second_vlan = m.groupdict()['second_vlan']
                service = str(m.groupdict()['service'])
                mtu = int(m.groupdict()['mtu'])
                linep_state = str(m.groupdict()['linep_state'])

                if interface not in vlan_interface_dict:
                    vlan_interface_dict[interface] = {}
                vlan_interface_dict[interface]['encapsulation'] = encapsulation
                vlan_interface_dict[interface]['outer_vlan'] = outer_vlan
                if second_vlan:
                    vlan_interface_dict[interface]['second_vlan'] = str(m.groupdict()['second_vlan'])
                vlan_interface_dict[interface]['service'] = service
                vlan_interface_dict[interface]['mtu'] = mtu
                vlan_interface_dict[interface]['linep_state'] = linep_state
                continue

        return vlan_interface_dict


#############################################################################
# Parser For show ipv4 vrf all interface
#############################################################################

class ShowIpv4VrfAllInterfaceSchema(MetaParser):
    """Schema for show ipv4 vrf all interface"""

    schema = {
        Any():
            {'oper_status': str,
             'int_status': str,
             'vrf': str,
             'vrf_id': str,
             Optional('multicast_groups'): list,
             Optional('multicast_groups_address'): str,
             Optional('ipv4'):
                {Any():
                    {Optional('ip'): str,
                     Optional('prefix_length'): str,
                     Optional('secondary'): bool,
                     Optional('route_tag'): int,
                     },
                 Optional('mtu'): int,
                 Optional('mtu_available'): int,
                 Optional('helper_address'): str,
                 Optional('broadcast_forwarding'): str,
                 Optional('out_access_list'): str,
                 Optional('in_access_list'): str,
                 Optional('in_common_access_list'): str,
                 Optional('proxy_arp'): str,
                 Optional('icmp_redirects'): str,
                 Optional('icmp_unreachables'): str,
                 Optional('icmp_replies'): str,
                 Optional('table_id'): str,
                 Optional('unnumbered'):
                    {Optional('unnumbered_intf_ref'): str
                    },
                },
            },
        }

class ShowIpv4VrfAllInterface(ShowIpv4VrfAllInterfaceSchema):
    """Parser for show ipv4 vrf all interface
                    show ipv4 vrf <vrf> interface"""

    cli_command = ['show ipv4 vrf {vrf} interface {interface}',
                   'show ipv4 vrf {vrf} interface', 'show ipv4 vrf all interface']

    def cli(self, interface='', vrf='', output=None):
        if output is None:
            if vrf:
                if interface and vrf != 'all':
                    cmd = self.cli_command[0].format(interface=interface, vrf=vrf)
                else:
                    cmd = self.cli_command[1].format(vrf=vrf)
            else:
                cmd = self.cli_command[2]
            out = self.device.execute(cmd)
        else:
            out = output

        ipv4_vrf_all_interface_dict = {}

        for line in out.splitlines():
            line = line.rstrip()

            # GigabitEthernet0/0/0/0 is Shutdown, ipv4 protocol is Down
            p1 = re.compile(r'^\s*(?P<interface>\S+) +is (?P<int_status>\S+),'
                             ' +ipv4 +protocol +is +(?P<oper_status>[a-zA-Z]+)$')
            m = p1.match(line)
            if m:
                interface = m.groupdict()['interface']
                int_status = m.groupdict()['int_status'].lower()
                oper_status = m.groupdict()['oper_status'].lower()

                if interface not in ipv4_vrf_all_interface_dict:
                    ipv4_vrf_all_interface_dict[interface] = {}
                ipv4_vrf_all_interface_dict[interface]['int_status'] = int_status
                ipv4_vrf_all_interface_dict[interface]['oper_status'] = oper_status

                #init multicast groups list to empty for this interface
                multicast_groups = []
                continue

            # Vrf is VRF1 (vrfid 0x60000002)
            p2 = re.compile(r'^\s*Vrf +is +(?P<vrf>\S+) \(vrfid +(?P<vrf_id>[a-z0-9]+)\)$')
            m = p2.match(line)
            if m:
                vrf = str(m.groupdict()['vrf'])
                vrf_id = str(m.groupdict()['vrf_id'])

                ipv4_vrf_all_interface_dict[interface]['vrf'] = vrf
                ipv4_vrf_all_interface_dict[interface]['vrf_id'] = vrf_id
                continue

            # Interface is unnumbered.  Using address of Loopback11 (10.69.111.111/32)
            p2_1 = re.compile(r'^\s*Interface is unnumbered. +Using +address'
                               ' +of +(?P<unnumbered_intf_ref>\S+)'
                               ' +\((?P<ip>[0-9\.]+)\/(?P<prefix_length>[0-9]+)\)$')
            m = p2_1.match(line)
            if m:
                unnumbered_intf_ref = m.groupdict()['unnumbered_intf_ref']
                ip = m.groupdict()['ip']
                prefix_length = str(m.groupdict()['prefix_length'])

                address = ip + '/' + prefix_length
                if 'ipv4' not in ipv4_vrf_all_interface_dict[interface]:
                    ipv4_vrf_all_interface_dict[interface]['ipv4'] = {}
                if 'unnumbered' not in ipv4_vrf_all_interface_dict[interface]['ipv4']:
                    ipv4_vrf_all_interface_dict[interface]['ipv4']['unnumbered'] = {}
                if address not in ipv4_vrf_all_interface_dict[interface]['ipv4']:
                    ipv4_vrf_all_interface_dict[interface]['ipv4'][address] = {}

                ipv4_vrf_all_interface_dict[interface]['ipv4'][address]['ip']= ip
                ipv4_vrf_all_interface_dict[interface]['ipv4'][address]\
                ['prefix_length'] = prefix_length

                try:
                    unnumbered_intf_ref
                except Exception:
                    pass
                else:
                    if 'unnumbered' not in ipv4_vrf_all_interface_dict[interface]['ipv4']:
                        ipv4_vrf_all_interface_dict[interface]['ipv4']['unnumbered'] = {}
                    ipv4_vrf_all_interface_dict[interface]['ipv4']['unnumbered']['unnumbered_intf_ref'] = unnumbered_intf_ref
                continue

            # Internet address is 10.1.1.1/24 with route-tag 50
            p3 = re.compile(r'^\s*Internet +address +is +(?P<ip>[0-9\.]+)\/'
                             '(?P<prefix_length>[0-9]+)(?: +with +route-tag'
                             ' +(?P<route_tag>[0-9]+))?$')
            m = p3.match(line)
            if m:
                ip = m.groupdict()['ip']
                prefix_length = str(m.groupdict()['prefix_length'])
                route_tag = m.groupdict()['route_tag']

                address = ip + '/' + prefix_length
                if 'ipv4' not in ipv4_vrf_all_interface_dict[interface]:
                    ipv4_vrf_all_interface_dict[interface]['ipv4'] = {}
                if address not in ipv4_vrf_all_interface_dict[interface]['ipv4']:
                    ipv4_vrf_all_interface_dict[interface]['ipv4'][address] = {}
                if route_tag:
                    ipv4_vrf_all_interface_dict[interface]['ipv4'][address]\
                    ['route_tag'] = int(m.groupdict()['route_tag'])

                ipv4_vrf_all_interface_dict[interface]['ipv4'][address]['ip']= ip
                ipv4_vrf_all_interface_dict[interface]['ipv4'][address]\
                ['prefix_length'] = prefix_length
                continue

            # Secondary address 10.2.2.2/24
            p4 = re.compile(r'^\s*(?P<secondary>(Secondary)) +address'
                             ' +(?P<ip>[0-9\.]+)\/(?P<prefix_length>[0-9]+)(?:'
                             ' +with +route-tag +(?P<route_tag>[0-9]+))?$')
            m = p4.match(line)
            if m:
                ip = m.groupdict()['ip']
                prefix_length = str(m.groupdict()['prefix_length'])
                route_tag = m.groupdict()['route_tag']

                address = ip + '/' + prefix_length
                if 'ipv4' not in ipv4_vrf_all_interface_dict[interface]:
                    ipv4_vrf_all_interface_dict[interface]['ipv4'] = {}
                if address not in ipv4_vrf_all_interface_dict[interface]['ipv4']:
                    ipv4_vrf_all_interface_dict[interface]['ipv4'][address] = {}
                if route_tag:
                    ipv4_vrf_all_interface_dict[interface]['ipv4'][address]\
                    ['route_tag'] = int(m.groupdict()['route_tag'])

                ipv4_vrf_all_interface_dict[interface]['ipv4'][address]\
                ['ip'] = ip
                ipv4_vrf_all_interface_dict[interface]['ipv4'][address]\
                ['prefix_length'] = prefix_length
                ipv4_vrf_all_interface_dict[interface]['ipv4'][address]\
                ['secondary'] = True
                continue

            # MTU is 1600 (1586 is available to IP)
            p5 = re.compile(r'^\s*MTU is +(?P<mtu>[0-9]+)'
                             ' +\((?P<mtu_available>[0-9]+) +is +available +to'
                             ' +IP\)$')
            m = p5.match(line)
            if m:
                mtu = m.groupdict()['mtu']
                mtu_available = m.groupdict()['mtu_available']

                if mtu:
                    ipv4_vrf_all_interface_dict[interface]['ipv4']\
                    ['mtu'] = int(m.groupdict()['mtu'])
                if mtu_available:
                    ipv4_vrf_all_interface_dict[interface]['ipv4']\
                    ['mtu_available'] = int(m.groupdict()['mtu_available'])
                continue

            # Helper address is not set
            p6 = re.compile(r'^\s*Helper +address +is +(?P<helper_address>[a-z\s]+)$')
            m = p6.match(line)
            if m:
                helper_address = str(m.groupdict()['helper_address'])

                if helper_address != "not set":
                    ipv4_vrf_all_interface_dict[interface]['ipv4']\
                    ['helper_address'] = helper_address
                continue

            # Multicast reserved groups joined: 224.0.0.2 224.0.0.1 224.0.0.2
            p6_1 = re.compile(r'^\s*Multicast +reserved +groups +joined: +(?P<multicast_groups_address>[a-z0-9\.\s]+)$')
            m = p6_1.match(line)
            if m:
                multicast_groups_address = str(m.groupdict()['multicast_groups_address'])

                #Split string of addressed into a list
                multicast_groups_address = [str(i) for i in multicast_groups_address.split()]

                #Add to previous created list
                for mgroup in multicast_groups_address:
                    multicast_groups.append(mgroup)

                ipv4_vrf_all_interface_dict[interface]['multicast_groups'] = multicast_groups
                continue

            # 224.0.0.5 224.0.0.6
            p6_2 = re.compile(r'^\s*(?P<multicast_groups_address>[a-z0-9\.\s]+)$')
            m = p6_2.match(line)
            if m:
                multicast_groups_address = str(m.groupdict()['multicast_groups_address'])

                #Split string of addressed into a list
                multicast_groups_address = [str(i) for i in multicast_groups_address.split()]

                #Add to previous created list
                for mgroup in multicast_groups_address:
                    multicast_groups.append(mgroup)

                ipv4_vrf_all_interface_dict[interface]['multicast_groups'] = multicast_groups
                continue

            # Directed broadcast forwarding is disabled
            p7 = re.compile(r'^\s*Directed +broadcast +forwarding +is'
                             ' +(?P<broadcast_forwarding>[a-zA-Z]+)$')
            m = p7.match(line)
            if m:
                broadcast_forwarding = str(m.groupdict()['broadcast_forwarding'])

                ipv4_vrf_all_interface_dict[interface]['ipv4']\
                ['broadcast_forwarding'] = broadcast_forwarding
                continue

            # Outgoing access list is not set
            p8 = re.compile(r'^\s*Outgoing +access +list +is'
                             ' +(?P<out_access_list>[a-zA-Z\s]+)$')
            m = p8.match(line)
            if m:
                out_access_list = str(m.groupdict()['out_access_list'])

                if out_access_list != "not set":
                    ipv4_vrf_all_interface_dict[interface]['ipv4']\
                    ['out_access_list'] = out_access_list
                continue

            # Inbound  access list is not set
            p9 = re.compile(r'^\s*Inbound +access +list +is'
                             ' +(?P<in_access_list>[a-zA-Z\s]+)$')
            m = p9.match(line)
            if m:
                in_access_list = str(m.groupdict()['in_access_list'])

                if in_access_list != "not set":
                    ipv4_vrf_all_interface_dict[interface]['ipv4']\
                    ['in_access_list'] = in_access_list
                continue

            # Inbound  common access list is not set, access list is not set
            p9_1 = re.compile(r'^\s*Inbound +common +access +list +is'
                               ' +(?P<in_common_access_list>[a-zA-Z\s]+), '
                               '+access +list +is +(?P<in_access_list>[a-zA-Z\s]+)$')
            m = p9_1.match(line)
            if m:
                in_common_access_list = str(m.groupdict()['in_common_access_list'])
                in_access_list = str(m.groupdict()['in_access_list'])

                if in_common_access_list != "not set":
                    ipv4_vrf_all_interface_dict[interface]['ipv4']\
                    ['in_common_access_list'] = in_common_access_list

                if in_access_list != "not set":
                    ipv4_vrf_all_interface_dict[interface]['ipv4']\
                    ['in_access_list'] = in_access_list
                continue

            # Proxy ARP is disabled
            p10 = re.compile(r'^\s*Proxy +ARP +is +(?P<proxy_arp>[a-zA-Z]+)$')
            m = p10.match(line)
            if m:
                proxy_arp = str(m.groupdict()['proxy_arp'])

                ipv4_vrf_all_interface_dict[interface]['ipv4']['proxy_arp'] = proxy_arp
                continue

            # ICMP redirects are never sent
            p11 = re.compile(r'^\s*ICMP +redirects +(are|is) +(?P<icmp_redirects>[a-zA-Z\s]+)$')
            m = p11.match(line)
            if m:
                icmp_redirects = str(m.groupdict()['icmp_redirects'])

                ipv4_vrf_all_interface_dict[interface]['ipv4']['icmp_redirects'] = icmp_redirects
                continue

            # ICMP unreachables are always sent
            p12 = re.compile(r'^\s*ICMP +unreachables +(are|is)'
                              ' +(?P<icmp_unreachables>[a-zA-Z\s]+)$')
            m = p12.match(line)
            if m:
                icmp_unreachables = str(m.groupdict()['icmp_unreachables'])

                ipv4_vrf_all_interface_dict[interface]['ipv4']\
                ['icmp_unreachables'] = icmp_unreachables
                continue

            # ICMP mask replies are never sent
            p13 = re.compile(r'^\s*ICMP +mask +replies +(are|is) +(?P<icmp_replies>[a-zA-Z\s]+)$')
            m = p13.match(line)
            if m:
                icmp_replies = str(m.groupdict()['icmp_replies'])

                ipv4_vrf_all_interface_dict[interface]['ipv4']['icmp_replies'] = icmp_replies
                continue

            # Table Id is 0xe0000011
            p13 = re.compile(r'^\s*Table +Id +is +(?P<table_id>[a-z0-9]+)$')
            m = p13.match(line)
            if m:
                table_id = str(m.groupdict()['table_id'])

                ipv4_vrf_all_interface_dict[interface]['ipv4']['table_id'] = table_id
                continue

        return ipv4_vrf_all_interface_dict


#############################################################################
# Parser For show ipv6 vrf all interface
#############################################################################

class ShowIpv6VrfAllInterfaceSchema(MetaParser):
    """Schema for show ipv6 vrf all interface"""

    schema = {
        Any():
            {'oper_status': str,
             'int_status': str,
             'vrf': str,
             'vrf_id': str,
             'enabled': bool,
             'ipv6_enabled': bool,
             Optional('ipv6'):
                {Any():
                    {Optional('ipv6'): str,
                     Optional('ipv6_prefix_length'): str,
                     Optional('ipv6_status'): str,
                     Optional('ipv6_route_tag'): str,
                     Optional('ipv6_eui64'): bool,
                     Optional('ipv6_subnet'): str,
                    },
                Optional('ipv6_link_local'): str,
                Optional('ipv6_link_local_state'): str,
                Optional('ipv6_group_address'): str,
                Optional('ipv6_groups'): list,
                Optional('ipv6_mtu'): str,
                Optional('ipv6_mtu_available'): str,
                Optional('icmp_redirects'): str,
                Optional('icmp_unreachables'): str,
                Optional('nd_dad'): str,
                Optional('dad_attempts'): str,
                Optional('nd_reachable_time'): str,
                Optional('nd_cache_limit'): str,
                Optional('nd_adv_retrans_int'): str,
                Optional('nd_adv_duration'): str,
                Optional('nd_router_adv'): str,
                Optional('stateless_autoconfig'): bool,
                Optional('out_access_list'): str,
                Optional('in_access_list'): str,
                Optional('in_common_access_list'): str,
                Optional('table_id'): str,
                Optional('complete_protocol_adj'): str,
                Optional('complete_glean_adj'): str,
                Optional('incomplete_protocol_adj'): str,
                Optional('incomplete_glean_adj'): str,
                Optional('dropped_protocol_req'): str,
                Optional('dropped_glean_req'): str
                },
            },
        }

class ShowIpv6VrfAllInterface(ShowIpv6VrfAllInterfaceSchema):
    """Parser for show ipv6 vrf all interface"""

    cli_command = ['show ipv6 vrf {vrf} interface {interface}',
                   'show ipv6 vrf {vrf} interface',
                   'show ipv6 vrf all interface']

    exclude = ['complete_protocol_adj', 'complete_glean_adj', 'ipv6_groups', 'ipv6_link_local']


    def cli(self, interface='', vrf='', output=None):
        if output is None:
            if vrf:
                if interface and vrf != 'all':
                    cmd = self.cli_command[0].format(interface=interface, vrf=vrf)
                else:
                    cmd = self.cli_command[1].format(vrf=vrf)
            else:
                cmd = self.cli_command[2]
            out = self.device.execute(cmd)
        else:
            out = output

        ipv6_vrf_all_interface_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # show ipv6 vrf {vrf} interface {interface}
            # show ipv6 vrf {vrf} interface', 'show ipv6 vrf all interface
            p1 = re.compile(r'^show +[\S\s]+$')
            m = p1.match(line)
            if m:
                continue

            # GigabitEthernet0/0/0/0 is Shutdown, ipv6 protocol is Down, Vrfid is VRF1 (0x60000002)
            # nve100 is Up, ipv6 protocol is Unknown, Vrfid is default (0x60000000)
            p1_1 = re.compile(r'^\s*(?P<interface>\S+) +is +(?P<int_status>[a-zA-Z]+),'
                             ' +ipv6 +protocol +is +(?P<oper_status>[a-zA-Z]+),'
                             ' +Vrfid +is +(?P<vrf>\S+) +\((?P<vrf_id>[a-z0-9]+)\)$')
            m = p1_1.match(line)
            if m:
                interface = m.groupdict()['interface']
                int_status = m.groupdict()['int_status'].lower()
                oper_status = m.groupdict()['oper_status'].lower()
                vrf = m.groupdict()['vrf']
                vrf_id = m.groupdict()['vrf_id']

                if interface not in ipv6_vrf_all_interface_dict:
                    ipv6_vrf_all_interface_dict[interface] = {}

                if oper_status == 'up':
                    ipv6_vrf_all_interface_dict[interface]['ipv6_enabled'] = True
                else:
                    ipv6_vrf_all_interface_dict[interface]['ipv6_enabled'] = False

                ipv6_vrf_all_interface_dict[interface]['int_status'] = int_status
                ipv6_vrf_all_interface_dict[interface]['oper_status'] = oper_status
                ipv6_vrf_all_interface_dict[interface]['vrf'] = vrf
                ipv6_vrf_all_interface_dict[interface]['vrf_id'] = vrf_id

                #init multicast groups list to empty for this interface
                ipv6_groups = []
                continue

            # IPv6 is enabled, link-local address is fe80::a8aa:bbff:feff:8888 [TENTATIVE]
            p2 = re.compile(r'^\s*(?P<enabled>(IPv6 is enabled)), +link-local'
                             ' +address +is +(?P<ipv6_link_local>[a-zA-Z0-9\:]+)'
                             ' +\[(?P<ipv6_link_local_state>[A-Z]+)\]$')
            m = p2.match(line)
            if m:
                enabled = bool(m.groupdict()['enabled'])
                ipv6_link_local = m.groupdict()['ipv6_link_local']
                ipv6_link_local_state = m.groupdict()['ipv6_link_local_state'].lower()

                ipv6_vrf_all_interface_dict[interface]['enabled'] = True
                continue

            # IPv6 is enabled, link-local address is fe80::a8aa:bbff:feff:8888
            p2_1 = re.compile(r'^\s*(?P<enabled>(IPv6 is enabled)), +link-local'
                               ' +address +is +(?P<ipv6_link_local>[a-zA-Z0-9\:]+)$')
            m = p2_1.match(line)
            if m:
                enabled = bool(m.groupdict()['enabled'])
                ipv6_link_local = m.groupdict()['ipv6_link_local']
                ipv6_vrf_all_interface_dict[interface]['enabled'] = True
                continue

            # IPv6 is disabled, link-local address unassigned
            p2_2 = re.compile(r'^\s*(?P<enabled>(IPv6 is disabled)),'
                               ' +link-local +address +(?P<ipv6_link_local>[a-zA-Z]+)$')
            m = p2_2.match(line)
            if m:
                enabled = bool(m.groupdict()['enabled'])
                ipv6_link_local = m.groupdict()['ipv6_link_local']
                ipv6_vrf_all_interface_dict[interface]['enabled'] = False
                continue

            # Global unicast address(es):
            # 2001:db8:3:3:a8aa:bbff:feff:8888, subnet is 2001:db8:3:3::/64 [TENTATIVE]
            p3 = re.compile(r'^\s*(?P<ipv6>(.+)(ff:fe)(.+)), +subnet +is'
                             ' +(?P<ipv6_subnet>[a-zA-Z0-9\:]+)\/(?P<ipv6_prefix_length>[0-9]+)'
                             ' +\[(?P<ipv6_status>[A-Z]+)\](?: +with +route-tag'
                             ' +(?P<ipv6_route_tag>[0-9]+))?$')
            m = p3.match(line)
            if m:
                ipv6 = m.groupdict()['ipv6']
                ipv6_subnet = m.groupdict()['ipv6_subnet']
                ipv6_prefix_length = m.groupdict()['ipv6_prefix_length']
                ipv6_status = m.groupdict()['ipv6_status'].lower()
                ipv6_route_tag = m.groupdict()['ipv6_route_tag']

                address = ipv6 + '/' + ipv6_prefix_length

                if 'ipv6' not in ipv6_vrf_all_interface_dict[interface]:
                    ipv6_vrf_all_interface_dict[interface]['ipv6'] = {}
                if address not in ipv6_vrf_all_interface_dict[interface]['ipv6']:
                    ipv6_vrf_all_interface_dict[interface]['ipv6'][address] = {}
                if ipv6_route_tag:
                    ipv6_vrf_all_interface_dict[interface]['ipv6'][address]\
                    ['ipv6_route_tag'] = str(m.groupdict()['ipv6_route_tag'])

                ipv6_vrf_all_interface_dict[interface]['ipv6'][address]\
                ['ipv6'] = ipv6
                ipv6_vrf_all_interface_dict[interface]['ipv6'][address]\
                ['ipv6_prefix_length'] = ipv6_prefix_length
                ipv6_vrf_all_interface_dict[interface]['ipv6'][address]\
                ['ipv6_status'] = ipv6_status
                ipv6_vrf_all_interface_dict[interface]['ipv6'][address]\
                ['ipv6_subnet'] = ipv6_subnet
                ipv6_vrf_all_interface_dict[interface]['ipv6'][address]\
                ['ipv6_eui64'] = True
                try:
                    ipv6_vrf_all_interface_dict[interface]['ipv6']\
                        ['ipv6_link_local_state'] = ipv6_link_local_state
                    ipv6_vrf_all_interface_dict[interface]['ipv6']\
                        ['ipv6_link_local'] = ipv6_link_local
                    continue
                except Exception:
                    pass

            # Global unicast address(es):
            # 2001:db8:4:4::4, subnet is 2001:db8:4:4::/64 [TENTATIVE] with route-tag 10
            p3_1 = re.compile(r'^\s*(?P<ipv6>[a-zA-Z0-9\:]+), +subnet +is'
                               ' +(?P<ipv6_subnet>[a-zA-Z0-9\:]+)\/'
                               '(?P<ipv6_prefix_length>[0-9]+)'
                               ' +\[(?P<ipv6_status>[A-Z]+)\] +with +route-tag'
                               ' +(?P<ipv6_route_tag>[0-9]+)$')
            m = p3_1.match(line)
            if m:
                ipv6 = m.groupdict()['ipv6']
                ipv6_subnet = m.groupdict()['ipv6_subnet']
                ipv6_prefix_length = m.groupdict()['ipv6_prefix_length']
                ipv6_status = m.groupdict()['ipv6_status'].lower()
                ipv6_route_tag = (m.groupdict()['ipv6_route_tag'])

                address = ipv6 + '/' + ipv6_prefix_length

                if 'ipv6' not in ipv6_vrf_all_interface_dict[interface]:
                    ipv6_vrf_all_interface_dict[interface]['ipv6'] = {}
                if address not in ipv6_vrf_all_interface_dict[interface]['ipv6']:
                    ipv6_vrf_all_interface_dict[interface]['ipv6'][address] = {}

                ipv6_vrf_all_interface_dict[interface]['ipv6'][address]\
                ['ipv6'] = ipv6
                ipv6_vrf_all_interface_dict[interface]['ipv6'][address]\
                ['ipv6_prefix_length'] = ipv6_prefix_length
                ipv6_vrf_all_interface_dict[interface]['ipv6'][address]\
                ['ipv6_status'] = ipv6_status
                ipv6_vrf_all_interface_dict[interface]['ipv6'][address]\
                ['ipv6_route_tag'] = ipv6_route_tag
                ipv6_vrf_all_interface_dict[interface]['ipv6'][address]\
                ['ipv6_subnet'] = ipv6_subnet
                try:
                    ipv6_vrf_all_interface_dict[interface]['ipv6']\
                        ['ipv6_link_local_state'] = ipv6_link_local_state
                    ipv6_vrf_all_interface_dict[interface]['ipv6']\
                        ['ipv6_link_local'] = ipv6_link_local
                    continue
                except Exception:
                    pass

            # Global unicast address(es):
            # 2001:db8:1:1::1, subnet is 2001:db8:1:1::/64 [TENTATIVE]
            p3_2 = re.compile(r'^\s*(?P<ipv6>[a-zA-Z0-9\:]+), +subnet +is'
                               ' +(?P<ipv6_subnet>[a-zA-Z0-9\:]+)\/'
                               '(?P<ipv6_prefix_length>[0-9]+)'
                               ' +\[(?P<ipv6_status>[A-Z]+)\]?$')
            m = p3_2.match(line)
            if m:
                ipv6 = m.groupdict()['ipv6']
                ipv6_subnet = m.groupdict()['ipv6_subnet']
                ipv6_prefix_length = m.groupdict()['ipv6_prefix_length']
                ipv6_status = m.groupdict()['ipv6_status'].lower()

                address = ipv6 + '/' + ipv6_prefix_length

                if 'ipv6' not in ipv6_vrf_all_interface_dict[interface]:
                    ipv6_vrf_all_interface_dict[interface]['ipv6'] = {}
                if address not in ipv6_vrf_all_interface_dict[interface]['ipv6']:
                    ipv6_vrf_all_interface_dict[interface]['ipv6'][address] = {}

                ipv6_vrf_all_interface_dict[interface]['ipv6'][address]\
                ['ipv6'] = ipv6
                ipv6_vrf_all_interface_dict[interface]['ipv6'][address]\
                ['ipv6_prefix_length'] = ipv6_prefix_length
                ipv6_vrf_all_interface_dict[interface]['ipv6'][address]\
                ['ipv6_status'] = ipv6_status
                ipv6_vrf_all_interface_dict[interface]['ipv6'][address]\
                ['ipv6_subnet'] = ipv6_subnet
                try:
                    ipv6_vrf_all_interface_dict[interface]['ipv6']\
                        ['ipv6_link_local_state'] = ipv6_link_local_state
                    ipv6_vrf_all_interface_dict[interface]['ipv6']\
                        ['ipv6_link_local'] = ipv6_link_local
                    continue
                except Exception:
                    pass

            # Global unicast address(es):
            # 2001:db8:1:1::1, subnet is 2001:db8:1:1::/64
            p3_3 = re.compile(r'^\s*(?P<ipv6>[a-zA-Z0-9\:]+), +subnet +is'
                               ' +(?P<ipv6_subnet>[a-zA-Z0-9\:]+)\/'
                               '(?P<ipv6_prefix_length>[0-9]+)$')
            m = p3_3.match(line)
            if m:
                ipv6 = m.groupdict()['ipv6']
                ipv6_subnet = m.groupdict()['ipv6_subnet']
                ipv6_prefix_length = m.groupdict()['ipv6_prefix_length']

                address = ipv6 + '/' + ipv6_prefix_length

                if 'ipv6' not in ipv6_vrf_all_interface_dict[interface]:
                    ipv6_vrf_all_interface_dict[interface]['ipv6'] = {}
                if address not in ipv6_vrf_all_interface_dict[interface]['ipv6']:
                    ipv6_vrf_all_interface_dict[interface]['ipv6'][address] = {}

                ipv6_vrf_all_interface_dict[interface]['ipv6'][address]\
                ['ipv6'] = ipv6
                ipv6_vrf_all_interface_dict[interface]['ipv6'][address]\
                ['ipv6_prefix_length'] = ipv6_prefix_length
                ipv6_vrf_all_interface_dict[interface]['ipv6'][address]\
                ['ipv6_subnet'] = ipv6_subnet
                try:
                    ipv6_vrf_all_interface_dict[interface]['ipv6']\
                        ['ipv6_link_local'] = ipv6_link_local
                    continue
                except Exception:
                    pass

            # Joined group address(es): ff02::1:ff00:1 ff02::1:ffa6:78c5 ff02::2
            #ff02::1
            p4 = re.compile(r'^\s*Joined +group +address\(es\): +(?P<ipv6_group_address>[a-z0-9\:\s]+)$')
            m = p4.match(line)
            if m:
                ipv6_group_address = str(m.groupdict()['ipv6_group_address'])

                #split string of addressed into a list
                ipv6_group_address = [str(i) for i in ipv6_group_address.split()]

                #Add to previous created list
                for group in ipv6_group_address:
                    ipv6_groups.append(group)
                ipv6_vrf_all_interface_dict.setdefault(interface, {}). \
                    setdefault('ipv6', {})
                ipv6_vrf_all_interface_dict[interface]['ipv6']['ipv6_groups'] = ipv6_groups
                continue

            p4_1 = re.compile(r'^\s*(?P<ipv6_group_address>[a-z0-9\:\s]+)$')
            m = p4_1.match(line)
            if m:
                ipv6_group_address = str(m.groupdict()['ipv6_group_address'])

                #split string of addressed into a list
                ipv6_group_address = [str(i) for i in ipv6_group_address.split()]

                #Add to previous created list
                for group in ipv6_group_address:
                    ipv6_groups.append(group)

                ipv6_vrf_all_interface_dict[interface]['ipv6']['ipv6_groups'] = ipv6_groups
                continue

            # MTU is 1600 (1586 is available to IPv6)
            p5 = re.compile(r'^\s*MTU +is +(?P<ipv6_mtu>[0-9]+)'
                             ' +\((?P<ipv6_mtu_available>[0-9]+) +is +available'
                             ' +to +IPv6\)$')
            m = p5.match(line)
            if m:
                ipv6_mtu = m.groupdict()['ipv6_mtu']
                ipv6_mtu_available = m.groupdict()['ipv6_mtu_available']

                ipv6_vrf_all_interface_dict[interface]['ipv6']\
                ['ipv6_mtu'] = ipv6_mtu
                ipv6_vrf_all_interface_dict[interface]['ipv6']\
                ['ipv6_mtu_available'] = ipv6_mtu_available
                continue

            # ICMP redirects are disabled
            p6 = re.compile(r'^\s*ICMP +redirects +are +(?P<icmp_redirects>[a-z]+)$')
            m = p6.match(line)
            if m:
                icmp_redirects = m.groupdict()['icmp_redirects']

                ipv6_vrf_all_interface_dict[interface]['ipv6']\
                ['icmp_redirects'] = icmp_redirects
                continue

            # ICMP unreachables are enabled
            p7 = re.compile(r'^\s*ICMP +unreachables +are'
                             ' +(?P<icmp_unreachables>[a-z]+)$')
            m = p7.match(line)
            if m:
                icmp_unreachables = m.groupdict()['icmp_unreachables']

                ipv6_vrf_all_interface_dict[interface]['ipv6']\
                ['icmp_unreachables'] = icmp_unreachables
                continue

            # ND DAD is enabled, number of DAD attempts 1
            p8 = re.compile(r'^\s*ND +DAD +is +(?P<nd_dad>[a-z]+), +number +of +DAD'
                             ' +attempts +(?P<dad_attempts>[0-9]+)$')
            m = p8.match(line)
            if m:
                nd_dad = m.groupdict()['nd_dad']
                dad_attempts = m.groupdict()['dad_attempts']

                ipv6_vrf_all_interface_dict[interface]['ipv6']\
                ['nd_dad'] = nd_dad
                ipv6_vrf_all_interface_dict[interface]['ipv6']\
                ['dad_attempts'] = dad_attempts
                continue

            # ND reachable time is 0 milliseconds
            p9 = re.compile(r'^\s*ND +reachable +time +is'
                             ' +(?P<nd_reachable_time>[0-9]+) +milliseconds$')
            m = p9.match(line)
            if m:
                nd_reachable_time = m.groupdict()['nd_reachable_time']

                ipv6_vrf_all_interface_dict[interface]['ipv6']\
                ['nd_reachable_time'] = nd_reachable_time
                continue

            # ND cache entry limit is 1000000000
            p10 = re.compile(r'^\s*ND +cache +entry +limit +is'
                              ' +(?P<nd_cache_limit>[0-9]+)$')
            m = p10.match(line)
            if m:
                nd_cache_limit = m.groupdict()['nd_cache_limit']

                ipv6_vrf_all_interface_dict[interface]['ipv6']\
                ['nd_cache_limit'] = nd_cache_limit
                continue

            # ND advertised retransmit interval is 0 milliseconds
            p11 = re.compile(r'^\s*ND +advertised +retransmit +interval +is'
                              ' +(?P<nd_adv_retrans_int>[0-9]+) +milliseconds$')
            m = p11.match(line)
            if m:
                nd_adv_retrans_int = m.groupdict()['nd_adv_retrans_int']

                ipv6_vrf_all_interface_dict[interface]['ipv6']\
                ['nd_adv_retrans_int'] = nd_adv_retrans_int
                continue

            # ND router advertisements are sent every 160 to 240 seconds
            p11_1 = re.compile(r'^\s*ND +router +advertisements +are +sent'
                                ' +every +(?P<nd_adv_duration>[a-z0-9\s]+) +seconds$')
            m = p11_1.match(line)
            if m:
                nd_adv_duration = m.groupdict()['nd_adv_duration']
                nd_adv_duration = nd_adv_duration.replace(" ","")
                nd_adv_duration = nd_adv_duration.replace("to","-")

                ipv6_vrf_all_interface_dict[interface]['ipv6']\
                ['nd_adv_duration'] = nd_adv_duration
                continue

            # ND router advertisements live for 1800 seconds
            p11_2 = re.compile(r'^\s*ND +router +advertisements +live +for'
                                ' +(?P<nd_router_adv>[0-9]+) +seconds$')
            m = p11_2.match(line)
            if m:
                nd_router_adv = m.groupdict()['nd_router_adv']
                ipv6_vrf_all_interface_dict[interface]['ipv6']['nd_router_adv']\
                 = nd_router_adv
                continue

            # Hosts use stateless autoconfig for addresses.
            p12 = re.compile(r'^\s*Hosts +use +(?P<stateless_autoconfig>(stateless))'
                              ' +autoconfig +for +addresses.$')
            m = p12.match(line)
            if m:
                stateless_autoconfig = m.groupdict()['stateless_autoconfig']

                ipv6_vrf_all_interface_dict[interface]['ipv6']\
                ['stateless_autoconfig'] = True
                continue

            # Outgoing access list is not set
            p13 = re.compile(r'^\s*Outgoing +access +list +is'
                              ' +(?P<out_access_list>[a-zA-Z\s]+)$')
            m = p13.match(line)
            if m:
                out_access_list = m.groupdict()['out_access_list']

                if out_access_list != "not set":
                    ipv6_vrf_all_interface_dict[interface]['ipv6']\
                    ['out_access_list'] = out_access_list
                continue

            # Inbound  access list is not set
            p14 = re.compile(r'^\s*Inbound +access +list +is'
                              ' +(?P<in_access_list>[a-zA-Z\s]+)$')
            m = p14.match(line)
            if m:
                in_access_list = m.groupdict()['in_access_list']

                if in_access_list != "not set":
                    ipv6_vrf_all_interface_dict[interface]['ipv6']['in_access_list'] = in_access_list
                continue

            # Inbound  common access list is not set, access list is not set
            p14_1 = re.compile(r'^\s*Inbound +common +access +list +is'
                                ' +(?P<in_common_access_list>[a-zA-Z\s]+),'
                                ' +access +list +is +(?P<in_access_list>[a-zA-Z\s]+)$')
            m = p14_1.match(line)
            if m:
                in_common_access_list = m.groupdict()['in_common_access_list']
                in_access_list = m.groupdict()['in_access_list']

                if in_common_access_list != "not set":
                    ipv6_vrf_all_interface_dict[interface]['ipv6']['in_common_access_list'] = in_common_access_list

                if in_access_list != "not set":
                    ipv6_vrf_all_interface_dict[interface]['ipv6']['in_access_list'] = in_access_list
                continue

            # Table Id is 0xe0800011
            p15 = re.compile(r'^\s*Table +Id +is +(?P<table_id>[a-z0-9]+)$')
            m = p15.match(line)
            if m:
                table_id = m.groupdict()['table_id']

                ipv6_vrf_all_interface_dict[interface]['ipv6']\
                ['table_id'] = table_id
                continue

            # Complete protocol adjacency: 0
            p16 = re.compile(r'^\s*Complete +protocol +adjacency:'
                              ' +(?P<complete_protocol_adj>[0-9]+)$')
            m = p16.match(line)
            if m:
                complete_protocol_adj = m.groupdict()['complete_protocol_adj']

                ipv6_vrf_all_interface_dict[interface]['ipv6']\
                ['complete_protocol_adj'] = complete_protocol_adj
                continue

            #Complete glean adjacency: 0
            p17 = re.compile(r'^\s*Complete +glean +adjacency:'
                              ' +(?P<complete_glean_adj>[0-9]+)$')
            m = p17.match(line)
            if m:
                complete_glean_adj = m.groupdict()['complete_glean_adj']

                ipv6_vrf_all_interface_dict[interface]['ipv6']\
                ['complete_glean_adj'] = complete_glean_adj
                continue

            # Incomplete protocol adjacency: 0
            p18 = re.compile(r'^\s*Incomplete +protocol +adjacency:'
                              ' +(?P<incomplete_protocol_adj>[0-9]+)$')
            m = p18.match(line)
            if m:
                incomplete_protocol_adj = m.groupdict()['incomplete_protocol_adj']

                ipv6_vrf_all_interface_dict[interface]['ipv6']\
                ['incomplete_protocol_adj'] = incomplete_protocol_adj
                continue

            # Incomplete glean adjacency: 0
            p19 = re.compile(r'^\s*Incomplete +glean +adjacency:'
                              ' +(?P<incomplete_glean_adj>[0-9]+)$')
            m = p19.match(line)
            if m:
                incomplete_glean_adj = m.groupdict()['incomplete_glean_adj']

                ipv6_vrf_all_interface_dict[interface]['ipv6']\
                ['incomplete_glean_adj'] = incomplete_glean_adj
                continue

            # Dropped protocol request: 0
            p20 = re.compile(r'^\s*Dropped +protocol +request:'
                              ' +(?P<dropped_protocol_req>[0-9]+)$')
            m = p20.match(line)
            if m:
                dropped_protocol_req = m.groupdict()['dropped_protocol_req']

                ipv6_vrf_all_interface_dict[interface]['ipv6']\
                ['dropped_protocol_req'] = dropped_protocol_req
                continue

            # Dropped glean request: 0
            p21 = re.compile(r'^\s*Dropped +glean +request:'
                              ' +(?P<dropped_glean_req>[0-9]+)$')
            m = p21.match(line)
            if m:
                dropped_glean_req = m.groupdict()['dropped_glean_req']

                ipv6_vrf_all_interface_dict[interface]['ipv6']\
                ['dropped_glean_req'] = dropped_glean_req
                continue

        return ipv6_vrf_all_interface_dict


#############################################################################
# Parser For Show etherent tags
#############################################################################

class ShowEthernetTagsSchema(MetaParser):
    """Schema for show ethernet tags"""

    schema = {
        Any():
            {Optional('status'): str,
            Optional('outer_vlan'): str,
            Optional('vlan_id'): str,
            Optional('inner_vlan'): str,
            Optional('xtra'): str,
            Optional('mtu'): int,
            Optional('rewrite_num_of_tags_pop'): int,
            Optional('rewrite_num_of_tags_push'): int
            },
        }

class ShowEthernetTags(ShowEthernetTagsSchema):
    """Parser for show ethernet tags
    show ethernet tags <interface>"""

    cli_command = ['show ethernet tags', 'show ethernet tags {interface}']

    def cli(self, interface='', output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[1].format(interface=interface)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()
            # Interface               St  MTU  Ly Outer            Inner            Xtra -,+
            # Gi0/0/0/0.501           Up  1518 L3 .1Q:501          -                -    1 0
            p1 = re.compile(r'^(?P<interface>[\w\/\.]+)'
                             ' +(?P<status>\w+)'
                             ' +(?P<mtu>\d+)'
                             ' +(?P<layer>\w+)'
                             ' +(?P<outer_vlan>\S+)'
                             ' +(?P<inner_vlan>\S+)'
                             ' +(?P<xtra>\S+)'
                             ' +(?P<rewrite_num_of_tags_pop>\d+)'
                             ' +(?P<rewrite_num_of_tags_push>\d+)$')
            m = p1.match(line)
            if m:
                interface = Common.convert_intf_name(m.groupdict()['interface'])
                status = m.groupdict()['status']
                outer_vlan = m.groupdict()['outer_vlan']
                mtu = m.groupdict()['mtu']
                layer = m.groupdict()['layer']
                inner_vlan = m.groupdict()['inner_vlan']
                xtra = m.groupdict()['xtra']
                rewrite_num_of_tags_pop = m.groupdict()['rewrite_num_of_tags_pop']
                rewrite_num_of_tags_push = m.groupdict()['rewrite_num_of_tags_push']

                if interface not in ret_dict:
                    ret_dict[interface] = {}

                if status and status != '-':
                    ret_dict[interface]['status'] = status.lower()

                if outer_vlan and outer_vlan != '-':
                    ret_dict[interface]['outer_vlan'] = outer_vlan
                    try:
                        vlan_id = re.match('[\w\.]+:(\d+)', outer_vlan).groups()[0]
                        ret_dict[interface]['vlan_id'] = vlan_id
                    except Exception:
                        pass

                if mtu and mtu != '-':
                    ret_dict[interface]['mtu'] = int(mtu)

                if layer and xtra != '-':
                    ret_dict[interface]['layer'] = layer.lower()

                if inner_vlan and inner_vlan != '-':
                    ret_dict[interface]['inner_vlan'] = inner_vlan

                if xtra and xtra != '-':
                    ret_dict[interface]['xtra'] = xtra

                if rewrite_num_of_tags_pop and rewrite_num_of_tags_pop != '-':
                    ret_dict[interface]['rewrite_num_of_tags_pop'] = int(rewrite_num_of_tags_pop)

                if rewrite_num_of_tags_push and rewrite_num_of_tags_push != '-':
                    ret_dict[interface]['rewrite_num_of_tags_push'] = int(rewrite_num_of_tags_push)

        return ret_dict


#############################################################################
# Parser For show interfaces accounting
#############################################################################

class ShowInterfacesAccountingSchema(MetaParser):
    """Schema for show interface accounting"""
    schema = {
                Any(): {
                    'accounting': {
                        Any(): {
                            'pkts_in': int,
                            'pkts_out': int,
                            'chars_in': int,
                            'chars_out': int,
                        }
                    }
                }
            }


class ShowInterfacesAccounting(ShowInterfacesAccountingSchema):
    """Parser for:
        show interfaces accounting
        show interfaces <interface> accounting
    """
    cli_command = ['show interfaces {interface} accounting','show interfaces accounting']
    exclude = ['pkts_in', 'pkts_out', 'chars_in', 'chars_out']


    def cli(self, interface=None, output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[0].format(interface=interface)
            else:
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return disctionary
        ret_dict = {}

        # initial regexp pattern
        p1 = re.compile(r'^\s*(?P<interface>\S+)\s*$')
        p2 = re.compile(r'^\s*(?P<protocol>\S+)\s+(?P<pkts_in>\d+)\s+'
                         '(?P<chars_in>\d+)\s+(?P<pkts_out>\d+)\s+'
                         '(?P<chars_out>\d+)')
        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            # GigabitEthernet0/0/0/0
            m = p1.match(line)
            if m:
                intf = m.groupdict()['interface']
                continue

            #   IPV4_UNICAST             9943           797492           50             3568
            m = p2.match(line)
            if m:
                protocol_dict = m.groupdict()
                protocol = protocol_dict.pop('protocol').lower()
                ret_dict.setdefault(intf, {}).\
                    setdefault('accounting', {}).setdefault(protocol, {})
                ret_dict[intf]['accounting'][protocol].update({k: int(v) \
                    for k, v in protocol_dict.items()})
                continue

        return ret_dict


class ShowInterfacesSchema(MetaParser):
    """schema for show interfaces
                  show interfaces <interface>"""

    schema = {
        Any(): {
            'oper_status': str,
            Optional('line_protocol'): str,
            'enabled': bool,
            Optional('interface_state_transitions'): int,
            Optional('type'): str,
            Optional('mac_address'): str,
            Optional('phys_address'): str,
            Optional('layer2'): bool,
            Optional('description'): str,
            'mtu': int,
            'bandwidth': int,
            Optional('bandwidth_max'): int,
            Optional('port_speed'): str,
            Optional('duplex_mode'): str,
            Optional('link_type'): str,
            Optional('media_type'): str,
            Optional('reliability'): str,
            Optional('txload'): str,
            Optional('rxload'): str,
            Optional('carrier_delay_up'): int,
            Optional('carrier_delay_down'): int,
            Optional('auto_negotiate'): bool,
            Optional('arp_type'): str,
            Optional('arp_timeout'): str,
            Optional('loopback'): str,
            Optional('last_link_flapped'): str,
            Optional('last_input'): str,
            Optional('last_output'): str,
            Optional('ipv4'): {
                Any(): {
                    Optional('ip'): str,
                    Optional('prefix_length'): str,
                },
            },
            Optional('encapsulations'): {
                Optional('encapsulation'): str,
                Optional('first_dot1q'): str,
                Optional('second_dot1q'): str,
                Optional('outer_match'): str,
                Optional('ethertype'): str,
                Optional('mac_match'): str,
                Optional('dest'): str,
            },
            Optional('flow_control'): {
                Optional('receive'): bool,
                Optional('send'): bool,
            },
            Optional('port_channel'): {
                Optional('member_count'): int,
                Optional('members'): {
                    Any(): {
                        Optional('interface'): str,
                        Optional('duplex_mode'): str,
                        Optional('speed'): str,
                        Optional('state'): str,
                    },
                },
            },
            Optional('counters'): {
                Optional('rate'): {
                    Optional('load_interval'): int,
                    Optional('in_rate'): int,
                    Optional('in_rate_pkts'): int,
                    Optional('out_rate'): int,
                    Optional('out_rate_pkts'): int,
                },
                Optional('in_total_drops'): int,
                Optional('in_unknown_protos'): int,
                Optional('in_octets'): int,
                Optional('in_pkts'): int,
                Optional('in_multicast_pkts'): int,
                Optional('in_broadcast_pkts'): int,
                Optional('in_runts'): int,
                Optional('in_giants'): int,
                Optional('in_throttles'): int,
                Optional('in_parity'): int,
                Optional('in_frame_errors'): int,
                Optional('in_crc_errors'): int,
                Optional('in_frame'): int,
                Optional('in_overrun'): int,
                Optional('in_ignored'): int,
                Optional('in_errors'): int,
                Optional('in_abort'): int,
                Optional('in_drops'): int,
                Optional('in_queue_drops'): int,
                Optional('out_pkts'): int,
                Optional('out_octets'): int,
                Optional('out_total_drops'): int,
                Optional('out_broadcast_pkts'): int,
                Optional('out_multicast_pkts'): int,
                Optional('out_errors'): int,
                Optional('out_underruns'): int,
                Optional('out_applique'): int,
                Optional('out_resets'): int,
                Optional('out_buffer_failure'): int,
                Optional('out_buffers_swapped'): int,
                Optional('out_drops'): int,
                Optional('out_queue_drops'): int,
                Optional('last_clear'): str,
                Optional('carrier_transitions'): int,
            },
        },
    }


class ShowInterfaces(ShowInterfacesSchema):
    """parser for show interfaces
                  show interfaces <interface>"""

    cli_command = ['show interfaces','show interfaces {interface}']
    exclude = []


    def cli(self, interface="", output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[1].format(interface=interface)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        result_dict = {}

        # GigabitEthernet1 is up, line protocol is up
        # TenGigE0/0/0/4 is administratively down, line protocol is administratively down
        p1 = re.compile(r'^(?P<interface>\S+) +is +(?P<enabled>[\w\s]+), '
                         '+line +protocol +is +(?P<line_protocol>[\w\s]+)$')

        # Interface state transitions: 9
        p2 = re.compile(r'^Interface +state +transitions: +(?P<interface_state_transitions>[\d]+)$')

        # Hardware is Loopback
        # Hardware is Gigabit Ethernet, address is 0057.d2ff.428c (bia 0057.d2ff.428c)
        p3 = re.compile(r'^Hardware +is +(?P<type>[\w\-\/\s\+\(\)]+)'
                         '(, *address +is +(?P<mac_address>[\w\.]+))?'
                         '( *\(bia *(?P<phys_address>[\w\.]+)\))?$')

        # Layer 2 Transport Mode
        p4 = re.compile(r'^Layer +2 +Transport +Mode$')

        # Description: to-ML26-BE1
        p5 = re.compile(r'^Description: *(?P<description>.*)$')

        # Internet address is 10.4.4.4/24
        # Internet address is Unknown
        p6 = re.compile(r'^Internet +[A|a]ddress +is +(?P<ipv4>(?P<ip>[\d\.]+)'
                         '\/(?P<prefix_length>[\d]+))?(?P<unknown>Unknown)?$')

        # MTU 1500 bytes, BW 10000 Kbit
        # MTU 1518 bytes, BW 10000000 Kbit (Max: 10000000 Kbit)
        p7 = re.compile(r'^MTU +(?P<mtu>[\d]+) +bytes, +BW +(?P<bandwidth>[\d]+) +Kbit'
                         '(.*Max: +(?P<bandwidth_max>[\d]+).*)?$')

        # reliability 255/255, txload 1/255, rxload 1/255
        # reliability Unknown, txload Unknown, rxload Unknown
        p8 = re.compile(r'^reliability +(?P<reliability>[\w\/]+), '
                         '+txload +(?P<txload>[\w\/]+), +rxload '
                         '+(?P<rxload>[\w\/]+)$')

        # Encapsulation ARPA,
        # Encapsulation 802.1Q Virtual LAN,
        # Encapsulation ARPA,  loopback not set,
        # Encapsulation 802.1Q Virtual LAN, VLAN Id 10,  loopback not set,
        # Encapsulation 802.1Q Virtual LAN, VLAN Id 10, 2nd VLAN Id 10,
        p9 = re.compile(r'^Encapsulation +(?P<encapsulation>[\w\.\s]+),'
                         '( +VLAN +Id +(?P<first_dot1q>\d+),)?'
                         '( +2nd +VLAN +Id +(?P<second_dot1q>\d+),)?'
                         '( +loopback +(?P<loopback>[\w\s]+),)?$')

        # Outer Match: Dot1Q VLAN 300
        p10 = re.compile(r'^Outer +Match: +(?P<outer_match>[\w\s]+)$')

        # Ethertype Any, MAC Match src any, dest any
        p11 = re.compile(r'^Ethertype +(?P<ethertype>\w+), '
                           '+MAC +Match +(?P<mac_match>[\w\s]+), '
                           '+dest +(?P<dest>\w+)$')

        # Full-duplex, 0Kb/s
        # Full-duplex, 1000Mb/s, link type is force-up
        # Full-duplex, Auto Speed, SR, link type is force-up
        # Duplex unknown, 0Kb/s, THD, link type is autonegotiation
        p12 = re.compile(r'^(?P<duplex_mode>[\w\s\-]+([d|D]uplex|unknown)), '
                          '+(?P<port_speed>[\w\s\/]+)(, +(?P<media_type>\S+))?'
                          '(, +link +type +is +(?P<link_type>\S+))?$')

        # output flow control is off, input flow control is off
        # output flow control is off, input flow control is unsupported
        p13 = re.compile(r'^output +flow +control +is +(?P<send>\w+), +'
                          'input +flow +control +is +(?P<receive>\w+)$')

        # Carrier delay (up) is 10 msec
        # Carrier delay (up) is 10 msec, Carrier delay (down) is 60 msec
        p14 = re.compile(r'^Carrier +delay +\(up\) +is +(?P<carrier_delay_up>\d+) +msec'
                '(, +Carrier +delay +\(down\) +is +(?P<carrier_delay_down>\d+) +msec)?$')

        # loopback not set,
        p15 = re.compile(r'^loopback +(?P<loopback>[\w\s]+),$')

        # Last link flapped 5w6d
        p16 = re.compile(r'^Last +link +flapped +(?P<last_link_flapped>\S+)$')

        # ARP type ARPA, ARP timeout 04:00:00
        p17 = re.compile(r'^ARP +type +(?P<arp_type>\w+), +'
                          'ARP +timeout +(?P<arp_timeout>[\w\:\.]+)$')

        # Last input never, output 00:01:05
        p18 = re.compile(r'^Last +input +(?P<last_input>[\w\.\:]+), +'
                          'output +(?P<last_output>[\w\.\:]+)$')

        # No. of members in this bundle: 1
        p19 = re.compile(r'^No\. +of +members +in +this +bundle: +(?P<member_count>\d+)$')

        # TenGigE0/0/0/1               Full-duplex  10000Mb/s    Active
        p20 = re.compile(r'^(?P<interface>[\w\/\.]+) '
                          '+(?P<duplex_mode>[\w\-\s]+([d|D]uplex|unknown)) '
                          '+(?P<speed>[\w\/\s]+?) +(?P<state>\w+)$')

        # Last clearing of "show interface" counters 1d02h
        p21 = re.compile(r'^Last +clearing +of +"show +interface" +counters +'
                          '(?P<last_clear>[\w\:\.]+)$')

        # Input/output data rate is disabled.
        p22 = re.compile(r'^Input\/output +data +rate +is +disabled\.$')

        # 5 minute input rate 0 bits/sec, 0 packets/sec
        p23 = re.compile(r'^(?P<load_interval>[\d\#]+)'
                          ' *(?P<unit>(minute|second|minutes|seconds)) +input +rate'
                          ' +(?P<in_rate>[\d]+) +bits/sec,'
                          ' +(?P<in_rate_pkts>[\d]+) +packets/sec$')

        # 5 minute output rate 0 bits/sec, 0 packets/sec
        p24 = re.compile(r'^(?P<load_interval>[\d\#]+)'
                          ' *(minute|second|minutes|seconds) +output +rate'
                          ' +(?P<out_rate>[\d]+) +bits/sec,'
                          ' +(?P<out_rate_pkts>[\d]+) +packets/sec$')

        # 0 packets input, 0 bytes
        # 0 packets input, 0 bytes, 0 total input drops
        p25 = re.compile(r'^(?P<in_pkts>[\d]+) +packets +input, +(?P<in_octets>[\d]+) +bytes'
                          '(, +(?P<in_total_drops>[\d]+) +total +input +drops)?$')

        # 1258859 drops for unrecognized upper-level protocol
        p26 = re.compile(r'(?P<in_unknown_protos>[\d]+) +drops +for '
                          '+unrecognized +upper-level +protocol$')

        # 0 input drops, 0 queue drops, 0 input errors
        p27 = re.compile(r'(?P<in_drops>[\d]+) +input +drops, '
                          '+(?P<in_queue_drops>[\d]+) +queue +drops, '
                          '+(?P<in_errors>[\d]+) +input +errors$')

        # Received 0 broadcast packets, 0 multicast packets
        p28 = re.compile(r'^Received +(?P<in_broadcast_pkts>\d+) +broadcast +packets, '
                          '+(?P<in_multicast_pkts>\d+) +multicast +packets$')

        # 0 runts, 0 giants, 0 throttles, 0 parity
        p29 = re.compile(r'^(?P<in_runts>[\d]+) +runts, +(?P<in_giants>[\d]+) +giants, '
                          '+(?P<in_throttles>[\d]+) +throttles, +(?P<in_parity>[\d]+) +parity$')

        # 0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
        p30 = re.compile(r'^(?P<in_errors>[\d]+) +input +errors, +'
                          '(?P<in_crc_errors>[\d]+) +CRC, +'
                          '(?P<in_frame>[\d]+) +frame, +'
                          '(?P<in_overrun>[\d]+) +overrun, +'
                          '(?P<in_ignored>[\d]+) +ignored, +'
                          '(?P<in_abort>[\d]+) +abort$')

        # 0 packets output, 0 bytes
        # 0 packets output, 0 bytes, 0 total output drops
        p31 = re.compile(r'^(?P<out_pkts>[\d]+) +packets +output, +(?P<out_octets>[\d]+) +bytes'
                          '(, +(?P<out_total_drops>[\d]+) +total +output +drops)?$')

        # Output 0 broadcast packets, 178045 multicast packets
        p32 = re.compile(r'^Output +(?P<out_broadcast_pkts>\d+) +broadcast +packets, '
                          '+(?P<out_multicast_pkts>\d+) +multicast +packets$')

        # 0 output errors, 0 underruns, 0 applique, 0 resets
        p33 = re.compile(r'^(?P<out_errors>[\d]+) +output +errors, '
                          '+(?P<out_underruns>[\d]+) +underruns, '
                          '+(?P<out_applique>[\d]+) +applique, '
                          '+(?P<out_resets>[\d]+) +resets$')

        # 0 output drops, 0 queue drops, 0 output errors
        p34 = re.compile(r'(?P<out_drops>[\d]+) +output +drops, '
                          '+(?P<out_queue_drops>[\d]+) +queue +drops, '
                          '+(?P<out_errors>[\d]+) +output +errors$')

        # 0 output buffer failures, 0 output buffers swapped out
        p35 = re.compile(r'^(?P<out_buffer_failure>[\d]+) +output +buffer +failures, '
                          '+(?P<out_buffers_swapped>[\d]+) +output +buffers +swapped +out$')

        # 0 carrier transitions
        p36 = re.compile(r'^(?P<carrier_transitions>[\d]+) +carrier +transitions$')

        for line in out.splitlines():
            line = line.strip()

            # GigabitEthernet1 is up, line protocol is up
            # TenGigE0/0/0/4 is administratively down, line protocol is administratively down
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface = group['interface']
                enabled = group['enabled']
                line_protocol = group['line_protocol']

                intf_dict = result_dict.setdefault(interface, {})
                if 'administratively down' in enabled or 'delete' in enabled:
                    intf_dict['enabled'] = False
                else:
                    intf_dict['enabled'] = True

                if line_protocol:
                    intf_dict['line_protocol'] = line_protocol
                    intf_dict['oper_status'] = line_protocol
                continue

            # Interface state transitions: 9
            m = p2.match(line)
            if m:
                interface_state_transitions = int(m.groupdict()['interface_state_transitions'])
                intf_dict['interface_state_transitions'] = interface_state_transitions
                continue

            # Hardware is Loopback
            # Hardware is Gigabit Ethernet, address is 0057.d2ff.428c (bia 0057.d2ff.428c)
            m = p3.match(line)
            if m:
                types = m.groupdict()['type']
                mac_address = m.groupdict()['mac_address']
                phys_address = m.groupdict()['phys_address']
                intf_dict['type'] = types
                if mac_address:
                    intf_dict['mac_address'] = mac_address
                if phys_address:
                    intf_dict['phys_address'] = phys_address
                continue

            # Layer 2 Transport Mode
            m = p4.match(line)
            if m:
                intf_dict['layer2'] = True
                continue

            # Description: desc
            m = p5.match(line)
            if m:
                description = m.groupdict()['description']
                intf_dict['description'] = description
                continue

            # Internet Address is 10.4.4.4/24
            # Internet address is Unknown
            m = p6.match(line)
            if m:
                ipv4 = m.groupdict()['ipv4']
                ip = m.groupdict()['ip']
                prefix_length = m.groupdict()['prefix_length']
                unknown = m.groupdict()['unknown']

                if ipv4 and not unknown:
                    ipv4_dict = intf_dict.setdefault('ipv4', {}).setdefault(ipv4, {})
                    ipv4_dict['ip'] = ip
                    ipv4_dict['prefix_length'] = prefix_length
                continue

            # MTU 1500 bytes, BW 10000 Kbit
            # MTU 1518 bytes, BW 10000000 Kbit (Max: 10000000 Kbit)
            m = p7.match(line)
            if m:
                mtu = m.groupdict()['mtu']
                bandwidth = m.groupdict()['bandwidth']
                bandwidth_max = m.groupdict()['bandwidth_max']

                intf_dict['mtu'] = int(mtu)
                intf_dict['bandwidth'] = int(bandwidth)
                if bandwidth_max:
                    intf_dict['bandwidth_max'] = int(bandwidth_max)
                continue

            # reliability 255/255, txload 1/255, rxload 1/255
            m = p8.match(line)
            if m:
                reliability = m.groupdict()['reliability']
                txload = m.groupdict()['txload']
                rxload = m.groupdict()['rxload']

                intf_dict['reliability'] = reliability
                intf_dict['txload'] = txload
                intf_dict['rxload'] = rxload
                continue

            # Encapsulation ARPA,
            # Encapsulation 802.1Q Virtual LAN, Vlan ID 1, loopback not set
            # Encapsulation 802.1Q Virtual LAN, VLAN Id 10, 2nd VLAN Id 10,
            m = p9.match(line)
            if m:
                group = m.groupdict()
                encapsulation = group['encapsulation'].lower()
                encapsulation = encapsulation.replace("802.1q virtual lan","dot1q")
                first_dot1q = group['first_dot1q']
                second_dot1q = group['second_dot1q']
                loopback = group['loopback']

                encap_dict = intf_dict.setdefault('encapsulations', {})
                encap_dict['encapsulation'] = encapsulation

                if first_dot1q:
                    encap_dict['first_dot1q'] = first_dot1q

                if second_dot1q:
                    encap_dict['second_dot1q'] = second_dot1q

                if loopback:
                    intf_dict['loopback'] = loopback
                continue

            # Outer Match: Dot1Q VLAN 300
            m = p10.match(line)
            if m:
                outer_match = m.groupdict()['outer_match']
                encap_dict['outer_match'] = outer_match
                continue

            # Ethertype Any, MAC Match src any, dest any
            m = p11.match(line)
            if m:
                group = m.groupdict()
                ethertype = group['ethertype']
                mac_match = group['mac_match']
                dest = group['dest']

                encap_dict['ethertype'] = ethertype
                encap_dict['mac_match'] = mac_match
                encap_dict['dest'] = dest
                continue

            # Full-duplex, 0Kb/s
            # Full-duplex, 1000Mb/s, link type is force-up
            # Full-duplex, Auto Speed, SR, link type is force-up
            # Duplex unknown, 0Kb/s, THD, link type is autonegotiation
            m = p12.match(line)
            if m:
                group = m.groupdict()
                duplex_mode = group['duplex_mode'].lower()
                duplex_mode = duplex_mode.replace("duplex", "").replace("-","")
                port_speed = group['port_speed']
                link_type = group['link_type']
                media_type = group['media_type']

                intf_dict['duplex_mode'] = duplex_mode.strip()
                intf_dict['port_speed'] = port_speed
                if link_type:
                    intf_dict['link_type'] = link_type
                    if 'auto' in link_type:
                        intf_dict['auto_negotiate'] = True
                    else:
                        intf_dict['auto_negotiate'] = False
                if media_type:
                    intf_dict['media_type'] = media_type
                continue

            # output flow control is off, input flow control is off
            m = p13.match(line)
            if m:
                receive = m.groupdict()['receive'].lower()
                send = m.groupdict()['send'].lower()
                flow_dict = intf_dict.setdefault('flow_control', {})

                if 'on' in receive:
                    flow_dict['receive'] = True
                elif 'off' in receive or 'unsupported' in receive:
                    flow_dict['receive'] = False

                if 'on' in send:
                    flow_dict['send'] = True
                elif 'off' in send or 'unsupported' in send:
                    flow_dict['send'] = False
                continue

            # Carrier delay (up) is 10 msec
            # Carrier delay (up) is 10 msec, Carrier delay (down) is 60 msec
            m = p14.match(line)
            if m:
                group = m.groupdict()
                carrier_delay_up = group['carrier_delay_up']
                carrier_delay_down = group['carrier_delay_down']

                if carrier_delay_up:
                    intf_dict['carrier_delay_up'] = int(carrier_delay_up)
                if carrier_delay_down:
                    intf_dict['carrier_delay_down'] = int(carrier_delay_down)
                continue

            # loopback not set,
            m = p15.match(line)
            if m:
                loopback = m.groupdict()['loopback']
                intf_dict['loopback'] = loopback
                continue

            # Last link flapped 5w6d
            m = p16.match(line)
            if m:
                last_link_flapped = m.groupdict()['last_link_flapped']
                intf_dict['last_link_flapped'] = last_link_flapped
                continue


            # ARP type ARPA, ARP timeout 04:00:00
            m = p17.match(line)
            if m:
                arp_type = m.groupdict()['arp_type'].lower()
                arp_timeout = m.groupdict()['arp_timeout']
                intf_dict['arp_type'] = arp_type
                intf_dict['arp_timeout'] = arp_timeout
                continue

            # Last input never, output 00:01:05
            m = p18.match(line)
            if m:
                last_input = m.groupdict()['last_input']
                last_output = m.groupdict()['last_output']
                intf_dict['last_input'] = last_input
                intf_dict['last_output'] = last_output
                continue

            # No. of members in this bundle: 1
            m = p19.match(line)
            if m:
                port_dict = intf_dict.setdefault('port_channel', {})
                port_dict['member_count'] = int(m.groupdict()['member_count'])
                continue

            # TenGigE0/0/0/1               Full-duplex  10000Mb/s    Active
            m = p20.match(line)
            if m:
                group = m.groupdict()
                interface = group['interface']
                duplex_mode = group['duplex_mode']
                speed = group['speed']
                state = group['state']

                members_intf_dict = port_dict.setdefault('members', {}).setdefault(interface, {})
                members_intf_dict['interface'] = interface
                members_intf_dict['duplex_mode'] = duplex_mode
                members_intf_dict['speed'] = speed
                members_intf_dict['state'] = state
                continue

            # Last clearing of "show interface" counters 1d02h
            m = p21.match(line)
            if m:
                last_clear = m.groupdict()['last_clear']
                counter_dict = intf_dict.setdefault('counters', {})
                counter_dict['last_clear'] = last_clear
                continue

            # 5 minute input rate 0 bits/sec, 0 packets/sec
            m = p23.match(line)
            if m:
                group = m.groupdict()
                load_interval = int(group['load_interval'])
                in_rate = int(group['in_rate'])
                in_rate_pkts = int(group['in_rate_pkts'])
                unit = group['unit']

                rate_dict = intf_dict.setdefault('counters', {}).setdefault('rate', {})
                # covert minutes to seconds
                if 'minute' in unit:
                    load_interval = load_interval * 60

                rate_dict['load_interval'] = load_interval
                rate_dict['in_rate'] = in_rate
                rate_dict['in_rate_pkts'] = in_rate_pkts
                continue

            # 5 minute output rate 0 bits/sec, 0 packets/sec
            m = p24.match(line)
            if m:
                group = m.groupdict()
                out_rate = int(group['out_rate'])
                out_rate_pkts = int(group['out_rate_pkts'])

                rate_dict = intf_dict.setdefault('counters', {}).setdefault('rate', {})
                rate_dict['out_rate'] = out_rate
                rate_dict['out_rate_pkts'] = out_rate_pkts
                continue

            # 0 packets input, 0 bytes
            # 0 packets input, 0 bytes, 0 total input drops
            m = p25.match(line)
            if m:
                group = m.groupdict()
                counter_dict = intf_dict.setdefault('counters', {})
                for k, v in group.items():
                    if v:
                        counter_dict.update({k: int(v)})
                continue

            # 1258859 drops for unrecognized upper-level protocol
            m = p26.match(line)
            if m:
                counter_dict['in_unknown_protos'] = int(m.groupdict()['in_unknown_protos'])
                continue

            # 0 input drops, 0 queue drops, 0 input errors
            m = p27.match(line)
            if m:
                group = m.groupdict()
                counter_dict.update({k: int(v) for k, v in group.items()})
                continue

            # Received 0 broadcast packets, 0 multicast packets
            m = p28.match(line)
            if m:
                group = m.groupdict()
                counter_dict.update({k: int(v) for k, v in group.items()})
                continue

            # 0 runts, 0 giants, 0 throttles, 0 parity
            m = p29.match(line)
            if m:
                group = m.groupdict()
                counter_dict.update({k: int(v) for k, v in group.items()})
                continue

            # 0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
            m = p30.match(line)
            if m:
                group = m.groupdict()
                counter_dict.update({k: int(v) for k, v in group.items()})
                continue

            # 0 packets output, 0 bytes
            # 0 packets output, 0 bytes, 0 total output drops
            m = p31.match(line)
            if m:
                group = m.groupdict()
                for k, v in group.items():
                    if v:
                        counter_dict.update({k: int(v)})
                continue

            # Output 0 broadcast packets, 178045 multicast packets
            m = p32.match(line)
            if m:
                group = m.groupdict()
                counter_dict.update({k: int(v) for k, v in group.items()})
                continue


            # 0 output errors, 0 underruns, 0 applique, 0 resets
            m = p33.match(line)
            if m:
                group = m.groupdict()
                counter_dict.update({k: int(v) for k, v in group.items()})
                continue

            # 0 output drops, 0 queue drops, 0 output errors
            m = p34.match(line)
            if m:
                group = m.groupdict()
                counter_dict.update({k: int(v) for k, v in group.items()})
                continue

            # 0 output buffer failures, 0 output buffers swapped out
            m = p35.match(line)
            if m:
                group = m.groupdict()
                counter_dict.update({k: int(v) for k, v in group.items()})
                continue

            # 0 carrier transitions
            m = p36.match(line)
            if m:
                group = m.groupdict()
                counter_dict.update({k: int(v) for k, v in group.items()})
                continue

        return result_dict

#############################################################################
# Parser For show interfaces Description
#############################################################################

class ShowInterfacesDescriptionSchema(MetaParser):
    """schema for show interfaces description
    """

    schema = {
        'interfaces': {
            Any(): {
                'status': str,
                'protocol': str,
                Optional('description'): str
            }
        }
    }


class ShowInterfacesDescription(ShowInterfacesDescriptionSchema):
    """parser for show interface description
    """

    cli_command = ['show interfaces description', 'show interfaces {interface} description']

    def cli(self, interface="", output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[1].format(interface=interface)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        result_dict = {}
        index = 1


        # Interface 		Status 		Protocol 	Description
        p1 = re.compile(r'^Interface\s+Status\s+Protocol\s+Description$')

        # PO0/0     		admin down  down 		First POS interface
        p2 = re.compile(r'^(?P<interface>\S+)\s+(?P<status>\S+([\s+](\S+))?)\s+'
                        r'(?P<protocol>\S+)\s*(?: +(?P<description>.*))?$')

        for line in out.splitlines():
            line = line.strip()
            line = line.replace('\t', '')

            # Interface 		Status 		Protocol 	Description
            m = p1.match(line)
            if m:
                result_dict['interfaces'] = {}
                continue


            # Et0/0 		up	 up
            m = p2.match(line)
            if m and "interfaces" in result_dict:
                group = m.groupdict()
                interface = Common.convert_intf_name(group['interface'], os="iosxr")
                intf_dict = result_dict['interfaces'].setdefault(interface, {})
                intf_dict['status'] = group['status']
                intf_dict['protocol'] = group['protocol']
                if group['description'] is not None:
                    intf_dict['description'] = str(group['description'])
                else:
                    intf_dict['description'] = ''
                index += 1
                continue

        return result_dict

class ShowIpv6Interface(ShowIpv6VrfAllInterface):
    """Parser for show ipv6 interface"""

    cli_command = [
                    'show ipv6 interface',
                    'show ipv6 interface {interface}'
                  ]

    def cli(self, interface=None, output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[1].format(interface=interface)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        return super().cli(output=out)


#############################################################################
# Parser For show interface summary
#############################################################################

class ShowInterfaceSummarySchema(MetaParser):
    """schema for show interface summary
    """

    schema = {
        'interface_types': {
            Any(): {
                'total': str,
                'up': str,
                'down': str,
                'admin_down': str,
            }
        }
    }


class ShowInterfaceSummary(ShowInterfaceSummarySchema):
    """parser for show interface summary
    """

    cli_command = 'show interface summary'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # IFT_FORTYGETHERNET      2        1        0        1
        p1 = re.compile(r'^(?P<type>\w+|ALL TYPES)\s+(?P<total>\d+)\s+(?P<up>\d+)\s+(?P<down>\d+)\s+(?P<admin_down>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()

                # Replace whitespaces with _ to create valid dict key (e.g: ALL TYPES => ALL_TYPES)
                interface_type = group['type'].replace(" ", "_")
                total = group['total']
                up = group['up']
                down = group['down']
                admin_down = group['admin_down']

                interface_dict = ret_dict.setdefault('interface_types', {}).setdefault(interface_type, {})

                interface_dict.update({
                    'total': total,
                    'up': up,
                    'down': down,
                    'admin_down': admin_down
                })

        return ret_dict
