"""
    show_interface.py
    IOSXE parsers for the following show commands:

    * show interfaces
    * show ip interfaces <interface>
    * show ip interface brief
    * show ip interface brief | include Vlan
    * show interfaces switchport
    * show ip interface
    * show interfaces <interface>
    * show ipv6 interface
    * show interfaces accounting
"""

import os
import logging
import pprint
import re
import unittest
from genie import parsergen
from collections import defaultdict

from ats.log.utils import banner
import xmltodict
try:
    import iptools
    from cnetconf import testmodel
except (ImportError, OSError):
    pass

try:
    from ats import tcl
except Exception:
    pass

from genie.metaparser import MetaParser
from genie.metaparser.util import merge_dict, keynames_convert
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


class ShowInterfacesSchema(MetaParser):
    """schema for show interfaces
                  show interfaces <interface>"""

    schema = {
            Any(): {
                'oper_status': str,
                Optional('line_protocol'): str,
                'enabled': bool,
                Optional('connected'): bool,
                Optional('description'): str,
                'type': str,
                Optional('link_state'): str,
                Optional('port_speed'): str,
                Optional('duplex_mode'): str,
                Optional('link_type'): str,
                Optional('media_type'): str,
                'mtu': int,
                Optional('medium'): str,
                Optional('reliability'): str,
                Optional('txload'): str,
                Optional('rxload'): str,
                Optional('mac_address'): str,
                Optional('phys_address'): str,
                Optional('delay'): int,
                Optional('carrier_delay'): int,
                Optional('carrier_delay_up'): int,
                Optional('carrier_delay_down'): int,
                Optional('keepalive'): int,
                Optional('auto_negotiate'): bool,
                Optional('arp_type'): str,
                Optional('arp_timeout'): str,
                Optional('last_input'): str,
                Optional('last_output'): str,
                Optional('output_hang'): str, 
                Optional('queues'): {             
                    Optional('input_queue_size'): int,
                    Optional('input_queue_max'): int,
                    Optional('input_queue_drops'): int,
                    Optional('input_queue_flushes'): int,
                    Optional('total_output_drop'): int,
                    Optional('queue_strategy'): str,
                    Optional('output_queue_size'): int,
                    Optional('output_queue_max'): int
                },
                Optional('flow_control'):
                    {Optional('receive'): bool,
                    Optional('send'): bool,
                },
                Optional('port_channel'):
                    {Optional('port_channel_member'): bool,
                    Optional('port_channel_int'): str,
                    Optional('port_channel_member_intfs'): list,
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
                    Optional('in_multicast_pkts'): int,
                    Optional('in_broadcast_pkts'): int,
                    Optional('in_crc_errors'): int,
                    Optional('in_giants'): int,
                    Optional('in_pkts'): int,
                    Optional('in_frame'): int,
                    Optional('in_runts'): int,
                    Optional('in_overrun'): int,
                    Optional('in_ignored'): int,
                    Optional('in_watchdog'): int,
                    Optional('in_with_dribble'): int,
                    Optional('in_octets'): int,
                    Optional('in_errors'): int,
                    Optional('in_abort'): int,
                    Optional('in_no_buffer'): int,
                    Optional('in_throttles'): int,
                    Optional('in_mac_pause_frames'): int,
                    Optional('out_pkts'): int,
                    Optional('out_octets'): int,
                    Optional('out_multicast_pkts'): int,
                    Optional('out_broadcast_pkts'): int,
                    Optional('out_errors'): int,
                    Optional('out_collision'): int,
                    Optional('out_interface_resets'): int,
                    Optional('out_unknown_protocl_drops'): int,
                    Optional('out_babbles'): int,
                    Optional('out_deferred'): int,
                    Optional('out_underruns'): int,
                    Optional('out_late_collision'): int,
                    Optional('out_lost_carrier'): int,
                    Optional('out_no_carrier'): int,
                    Optional('out_babble'): int,
                    Optional('out_mac_pause_frames'): int,
                    Optional('out_buffer_failure'): int,
                    Optional('out_buffers_swapped'): int,
                    Optional('last_clear'): str,
                    },
                Optional('encapsulations'):
                    {Optional('encapsulation'): str,
                     Optional('first_dot1q'): str,
                     Optional('second_dot1q'): str,
                     Optional('native_vlan'): int,
                    },
                Optional('ipv4'):
                    {Any():
                        {Optional('ip'): str,
                         Optional('prefix_length'): str,
                         Optional('secondary'): bool
                    },
                    Optional('unnumbered'): {
                        'interface_ref': str,
                },
            },
        },
    }


class ShowInterfaces(ShowInterfacesSchema):
    """parser for show interfaces
                  show interfaces <interface>"""

    cli_command = ['show interfaces','show interfaces {interface}']

    def cli(self,interface="",output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[1].format(interface=interface)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        interface_dict = {}
        unnumbered_dict = {}
        for line in out.splitlines():
            line = line.strip()

            # GigabitEthernet1 is up, line protocol is up 
            # Port-channel12 is up, line protocol is up (connected)
            # Vlan1 is administratively down, line protocol is down , Autostate Enabled
            p1 =  re.compile(r'^(?P<interface>[\w\/\.\-]+) +is'
                              ' +(?P<enabled>[\w\s]+),'
                              ' +line +protocol +is +(?P<line_protocol>\w+)'
                              '( *\((?P<attribute>\S+)\))?$')
            p1_1 =  re.compile(r'^(?P<interface>[\w\/\.\-]+) +is'
                              ' +(?P<enabled>[\w\s]+),'
                              ' +line +protocol +is +(?P<line_protocol>\w+)'
                              '( *, *(?P<attribute>[\w\s]+))?$')
            m = p1.match(line)
            m1 = p1_1.match(line)
            m = m if m else m1
            if m:
                interface = m.groupdict()['interface']
                enabled = m.groupdict()['enabled']
                line_protocol = m.groupdict()['line_protocol']
                connected = m.groupdict()['attribute']

                if interface not in interface_dict:
                    interface_dict[interface] = {}
                    interface_dict[interface]['port_channel'] = {}
                    interface_dict[interface]['port_channel']\
                        ['port_channel_member'] = False

                if enabled and 'up' in enabled:
                    interface_dict[interface]['enabled'] = True
                else:
                    interface_dict[interface]['enabled'] = False

                if line_protocol:
                    interface_dict[interface]\
                                ['line_protocol'] = line_protocol
                    interface_dict[interface]\
                                ['oper_status'] = line_protocol

                if connected:
                    if connected == 'connected':
                        interface_dict[interface]['connected'] = True
                    else:
                        interface_dict[interface]['connected'] = False
                continue

            # Hardware is Gigabit Ethernet, address is 0057.d228.1a64 (bia 0057.d228.1a64)
            # Hardware is Loopback
            p2 = re.compile(r'^Hardware +is +(?P<type>[a-zA-Z0-9\-\/\s\+]+)'
                            '(, *address +is +(?P<mac_address>[a-z0-9\.]+)'
                            ' *\(bia *(?P<phys_address>[a-z0-9\.]+)\))?$')
            # Hardware is LTE Adv CAT6 - Multimode LTE/DC-HSPA+/HSPA+/HSPA/UMTS/EDGE/GPRS 
            p2_2 = re.compile(r'Hardware +is +(?P<type>[a-zA-Z0-9\-\/\+ ]+)(?P<mac_address>.*)(?P<phys_address>.*)')
            m = p2.match(line)
            m1 = p2_2.match(line)
            m = m if m else m1
            if m:
                types = m.groupdict()['type']
                mac_address = m.groupdict()['mac_address']
                phys_address = m.groupdict()['phys_address']
                interface_dict[interface]['type'] = types
                if mac_address:
                    interface_dict[interface]['mac_address'] = mac_address
                if phys_address:
                    interface_dict[interface]['phys_address'] = phys_address
                continue

            # Description: desc
            # Description: Pim Register Tunnel (Encap) for RP 10.186.1.1
            p3 = re.compile(r'^Description: *(?P<description>.*)$')
            m = p3.match(line)
            if m:
                description = m.groupdict()['description']

                interface_dict[interface]['description'] = description
                continue

            # Secondary address 10.2.2.2/24
            p4 = re.compile(r'^Secondary +Address +is +(?P<ipv4>(?P<ip>[0-9\.]+)'
                             '\/(?P<prefix_length>[0-9]+))$')
            m = p4.match(line)
            if m:
                ip_sec = m.groupdict()['ip']
                prefix_length_sec = m.groupdict()['prefix_length']
                address_sec = m.groupdict()['ipv4']

                if 'ipv4' not in interface_dict[interface]:
                    interface_dict[interface]['ipv4'] = {}
                if address_sec not in interface_dict[interface]['ipv4']:
                    interface_dict[interface]['ipv4'][address_sec] = {}

                interface_dict[interface]['ipv4'][address_sec]\
                    ['ip'] = ip_sec
                interface_dict[interface]['ipv4'][address_sec]\
                    ['prefix_length'] = prefix_length_sec
                interface_dict[interface]['ipv4'][address_sec]\
                    ['secondary'] = True
                continue

            # Internet Address is 10.4.4.4/24
            # Internet address is 10.4.4.4/24
            p5 = re.compile(r'^Internet +[A|a]ddress +is +(?P<ipv4>(?P<ip>[0-9\.]+)'
                             '\/(?P<prefix_length>[0-9]+))$')
            m = p5.match(line)
            if m:
                ip = m.groupdict()['ip']
                prefix_length = m.groupdict()['prefix_length']
                address = m.groupdict()['ipv4']

                if 'ipv4' not in interface_dict[interface]:
                    interface_dict[interface]['ipv4'] = {}
                if address not in interface_dict[interface]['ipv4']:
                    interface_dict[interface]['ipv4'][address] = {}

                interface_dict[interface]['ipv4'][address]\
                ['ip'] = ip
                interface_dict[interface]['ipv4'][address]\
                ['prefix_length'] = prefix_length
                continue
            
            # MTU 1500 bytes, BW 768 Kbit/sec, DLY 3330 usec,
            # MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec, 
            p6 = re.compile(r'^MTU +(?P<mtu>[0-9]+) +bytes, +BW'
                             ' +(?P<bandwidth>[0-9]+) +Kbit(/sec)?, +DLY'
                             ' +(?P<delay>[0-9]+) +usec,$')
            m = p6.match(line)
            if m:
                mtu = m.groupdict()['mtu']
                bandwidth = m.groupdict()['bandwidth']
                if m.groupdict()['delay']:
                    interface_dict[interface]['delay'] = int(m.groupdict()['delay'])
                if mtu:
                    interface_dict[interface]['mtu'] = int(mtu)
                if bandwidth:
                    interface_dict[interface]['bandwidth'] = int(bandwidth)
                continue

            # reliability 255/255, txload 1/255, rxload 1/255
            p7 = re.compile(r'^reliability +(?P<reliability>[\d\/]+),'
                             ' +txload +(?P<txload>[\d\/]+), +rxload'
                             ' +(?P<rxload>[\d\/]+)$')
            m = p7.match(line)
            if m:
                reliability = m.groupdict()['reliability']
                txload = m.groupdict()['txload']
                rxload = m.groupdict()['rxload']
                interface_dict[interface]['reliability'] = reliability
                interface_dict[interface]['txload'] = txload
                interface_dict[interface]['rxload'] = rxload
                continue

            # Encapsulation LOOPBACK, loopback not set
            # Encapsulation 802.1Q Virtual LAN, Vlan ID 20, medium is p2p
            # Encapsulation ARPA, medium is broadcast
            # Encapsulation QinQ Virtual LAN, outer ID  10, inner ID 20
            # Encapsulation 802.1Q Virtual LAN, Vlan ID  1., loopback not set
            p8 = re.compile(r'^Encapsulation +(?P<encapsulation>[\w\s\.]+),'
                             ' +(?P<rest>.*)$')
            m = p8.match(line)
            if m:
                encapsulation = m.groupdict()['encapsulation']
                encapsulation = m.groupdict()['encapsulation'].lower()
                encapsulation = encapsulation.replace("802.1q virtual lan","dot1q")
                if 'encapsulations' not in interface_dict[interface]:
                    interface_dict[interface]['encapsulations'] = {}

                interface_dict[interface]['encapsulations']\
                    ['encapsulation'] = encapsulation

                rest = m.groupdict()['rest']
                # Vlan ID 20, medium is p2p
                m1 = re.compile(r'(Vlan +ID +(?P<first_dot1q>[0-9]+),)?'
                                 ' *medium +is +(?P<medium>[a-z0-9]+)$').match(rest)
                # will update key when output is valid
                m2 = re.compile(r'loopback +(?P<loopback>[\w\s]+)$').match(rest)

                #  outer ID  10, inner ID 20
                m3 = re.compile(r'outer +ID +(?P<first>[0-9]+), +'
                                 'inner +ID (?P<second>[0-9]+)$').match(rest)

                #  Vlan ID  1., loopback not set
                m4 = re.compile(r'Vlan +ID +(?P<first_dot1q>[0-9]+).?, +'
                                 '(?P<rest>.+)$').match(rest)
                if m1:
                    first_dot1q = m1.groupdict()['first_dot1q']
                    if first_dot1q:
                        interface_dict[interface]['encapsulations']\
                            ['first_dot1q'] = first_dot1q
                    interface_dict[interface]['medium'] = medium
                elif m3:
                    first_dot1q = m3.groupdict()['first']
                    second_dot1q = m3.groupdict()['second']
                    interface_dict[interface]['encapsulations']\
                        ['first_dot1q'] = first_dot1q
                    interface_dict[interface]['encapsulations']\
                        ['second_dot1q'] = second_dot1q
                elif m4:
                    first_dot1q = m4.groupdict()['first_dot1q']
                    if first_dot1q:
                        interface_dict[interface]['encapsulations']\
                            ['first_dot1q'] = first_dot1q
                continue

            # reliability 255/255, txload 1/255, rxload 1/255
            p9 = re.compile(r'^reliability +(?P<reliability>[0-9]+),'
                             ' +txload +(?P<txload>[0-9]+), +rxload'
                             ' +(?P<rxload>[0-9]+)$')
            m = p9.match(line)
            if m:
                reliability = m.groupdict()['reliability']
                txload = m.groupdict()['txload']
                rxload = m.groupdict()['rxload']
                interface_dict[interface]['reliability'] = reliability
                interface_dict[interface]['txload'] = txload
                interface_dict[interface]['rxload'] = rxload
                continue

            # Keepalive set (10 sec)
            p10 = re.compile(r'^Keepalive +set +\((?P<keepalive>[0-9]+)'
                             ' +sec\)$')
            m = p10.match(line)
            if m:
                keepalive = m.groupdict()['keepalive']
                if keepalive:
                    interface_dict[interface]['keepalive'] = int(keepalive)
                continue

            # Auto-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
            # Full-duplex, 1000Mb/s, link type is auto, media type is
            # Full Duplex, 1000Mbps, link type is auto, media type is RJ45
            # Full Duplex, Auto Speed, link type is auto, media type is RJ45
            p11 = re.compile(r'^(?P<duplex_mode>\w+)[\-\s]+[d|D]uplex, +'
                              '(?P<port_speed>\d+|Auto-(S|s)peed|Auto (S|s)peed)(?: *(Mbps|Mb/s))?,'
                              '( *link +type +is +(?P<link_type>\w+),)?'
                              ' *media +type +is *(?P<media_type>[\w\/]+)?$')
            m = p11.match(line)
            if m:
                duplex_mode = m.groupdict()['duplex_mode'].lower()
                port_speed = m.groupdict()['port_speed'].lower().replace('-speed', '')
                link_type = m.groupdict()['link_type']
                media_type = m.groupdict()['media_type']
                interface_dict[interface]['duplex_mode'] = duplex_mode
                interface_dict[interface]['port_speed'] = port_speed
                if link_type:
                    interface_dict[interface]['link_type'] = link_type
                    if 'auto' in link_type:
                        interface_dict[interface]['auto_negotiate'] = True
                    else:
                        interface_dict[interface]['auto_negotiate'] = False
                if media_type:
                    interface_dict[interface]['media_type'] = media_type
                continue

            # input flow-control is off, output flow-control is unsupported
            p12 = re.compile(r'^(input|output) +flow-control +is +(?P<receive>\w+), +'
                              '(output|input) +flow-control +is +(?P<send>\w+)$')
            m = p12.match(line)
            if m:
                receive = m.groupdict()['receive'].lower()
                send = m.groupdict()['send'].lower()
                if 'flow_control' not in interface_dict[interface]:
                    interface_dict[interface]['flow_control'] = {}
                if 'on' in receive:
                    interface_dict[interface]['flow_control']['receive'] = True
                elif 'off' in receive or 'unsupported' in receive:
                    interface_dict[interface]['flow_control']['receive'] = False

                if 'on' in send:
                    interface_dict[interface]['flow_control']['send'] = True
                elif 'off' in send or 'unsupported' in send:
                    interface_dict[interface]['flow_control']['send'] = False
                continue

            # Carrier delay is 10 sec
            p_cd = re.compile(r'^Carrier +delay +is +(?P<carrier_delay>\d+).*$')
            m = p_cd.match(line)
            if m:
                group = m.groupdict()
                sub_dict = interface_dict.setdefault(interface, {})
                sub_dict['carrier_delay'] = int(group['carrier_delay'])

            # Asymmetric Carrier-Delay Up Timer is 2 sec
            # Asymmetric Carrier-Delay Down Timer is 10 sec
            p_cd_2 = re.compile(r'^Asymmetric +Carrier-Delay +(?P<type>Down|Up)'
                                 ' +Timer +is +(?P<carrier_delay>\d+).*$')
            m = p_cd_2.match(line)
            if m:
                group = m.groupdict()
                tp = group['type'].lower()
                sub_dict = interface_dict.setdefault(interface, {})
                if tp == 'up':
                    sub_dict['carrier_delay_up'] = int(group['carrier_delay'])
                else:
                    sub_dict['carrier_delay_down'] = int(group['carrier_delay'])

            # ARP type: ARPA, ARP Timeout 04:00:00
            p13 = re.compile(r'^ARP +type: +(?P<arp_type>\w+), +'
                              'ARP +Timeout +(?P<arp_timeout>[\w\:\.]+)$')
            m = p13.match(line)
            if m:
                arp_type = m.groupdict()['arp_type'].lower()
                arp_timeout = m.groupdict()['arp_timeout']
                interface_dict[interface]['arp_type'] = arp_type
                interface_dict[interface]['arp_timeout'] = arp_timeout
                continue

            # Last input never, output 00:01:05, output hang never
            p14 = re.compile(r'^Last +input +(?P<last_input>[\w\.\:]+), +'
                              'output +(?P<last_output>[\w\.\:]+), '
                              'output +hang +(?P<output_hang>[\w\.\:]+)$')
            m = p14.match(line)
            if m:
                last_input = m.groupdict()['last_input']
                last_output = m.groupdict()['last_output']
                output_hang = m.groupdict()['output_hang']
                interface_dict[interface]['last_input'] = last_input
                interface_dict[interface]['last_output'] = last_output
                interface_dict[interface]['output_hang'] = output_hang
                continue

            # Members in this channel: Gi1/0/2
            # Members in this channel: Fo1/0/2 Fo1/0/4
            p15 = re.compile(r'^Members +in +this +channel: +'
                              '(?P<port_channel_member_intfs>[\w\/\.\s\,]+)$')
            m = p15.match(line)
            if m:
                interface_dict[interface]['port_channel']\
                    ['port_channel_member'] = True
                intfs = m.groupdict()['port_channel_member_intfs'].split(' ')
                intfs = [Common.convert_intf_name(i.strip()) for i in intfs]
                interface_dict[interface]['port_channel']\
                    ['port_channel_member_intfs'] = intfs

                # build connected interface port_channel
                for intf in intfs:
                    if intf not in interface_dict:
                        interface_dict[intf] = {}
                    if 'port_channel' not in interface_dict[intf]:
                        interface_dict[intf]['port_channel'] = {}
                    interface_dict[intf]['port_channel']['port_channel_member'] = True
                    interface_dict[intf]['port_channel']['port_channel_int'] = interface
                continue

            # Last clearing of "show interface" counters 1d02h
            p16 = re.compile(r'^Last +clearing +of +\"show +interface\" +counters +'
                              '(?P<last_clear>[\w\:\.]+)$')
            m = p16.match(line)
            if m:                
                last_clear = m.groupdict()['last_clear']
                continue

            # Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
            p17 = re.compile(r'^Input +queue: +(?P<size>\d+)\/(?P<max>\d+)\/'
                              '(?P<drops>\d+)\/(?P<flushes>\d+) +'
                              '\(size\/max\/drops\/flushes\); +'
                              'Total +output +drops: +(?P<output_drop>\d+)$')
            m = p17.match(line)
            if m:
                if 'queues' not in interface_dict[interface]:
                    interface_dict[interface]['queues'] = {}

                interface_dict[interface]['queues']['input_queue_size'] = \
                    int(m.groupdict()['size'])
                interface_dict[interface]['queues']['input_queue_max'] = \
                    int(m.groupdict()['max'])
                interface_dict[interface]['queues']['input_queue_drops'] = \
                    int(m.groupdict()['drops'])
                interface_dict[interface]['queues']['input_queue_flushes'] = \
                    int(m.groupdict()['flushes'])
                interface_dict[interface]['queues']['total_output_drop'] = \
                    int(m.groupdict()['output_drop'])
                continue

            # Queueing strategy: fifo
            p18 = re.compile(r'^Queueing +strategy: +(?P<queue_strategy>\w+)$')
            m = p18.match(line)
            if m:
                if 'queues' not in interface_dict[interface]:
                    interface_dict[interface]['queues'] = {}
                interface_dict[interface]['queues']['queue_strategy'] = \
                    m.groupdict()['queue_strategy']
                continue

            # Output queue: 0/0 (size/max)
            p19 = re.compile(r'^Output +queue: +(?P<size>\d+)\/(?P<max>\d+)'
                              ' +\(size\/max\)$')
            m = p19.match(line)
            if m:
                if 'queues' not in interface_dict[interface]:
                    interface_dict[interface]['queues'] = {}
                interface_dict[interface]['queues']['output_queue_size'] = \
                    int(m.groupdict()['size'])
                interface_dict[interface]['queues']['output_queue_max'] = \
                    int(m.groupdict()['max'])
                continue

            # 5 minute input rate 0 bits/sec, 0 packets/sec
            p20 = re.compile(r'^(?P<load_interval>[0-9\#]+)'
                              ' *(?P<unit>(minute|second|minutes|seconds)) *input *rate'
                              ' *(?P<in_rate>[0-9]+) *bits/sec,'
                              ' *(?P<in_rate_pkts>[0-9]+) *packets/sec$')
            m = p20.match(line)
            if m:
                load_interval = int(m.groupdict()['load_interval'])
                in_rate = int(m.groupdict()['in_rate'])
                in_rate_pkts = int(m.groupdict()['in_rate_pkts'])
                unit = m.groupdict()['unit']
                # covert minutes to seconds
                if 'minute' in unit:
                    load_interval = load_interval * 60

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
                    
                if 'last_clear' not in interface_dict[interface]['counters']:
                    try:
                        last_clear
                    except Exception:
                        pass
                    else:
                        interface_dict[interface]['counters']\
                            ['last_clear'] = last_clear
                continue

            # 5 minute output rate 0 bits/sec, 0 packets/sec
            p21 = re.compile(r'^(?P<load_interval>[0-9\#]+)'
                              ' *(minute|second|minutes|seconds) *output *rate'
                              ' *(?P<out_rate>[0-9]+) *bits/sec,'
                              ' *(?P<out_rate_pkts>[0-9]+) *packets/sec$')
            m = p21.match(line)
            if m:
                out_rate = int(m.groupdict()['out_rate'])
                out_rate_pkts = int(m.groupdict()['out_rate_pkts'])

                interface_dict[interface]['counters']['rate']\
                    ['out_rate'] = out_rate
                interface_dict[interface]['counters']['rate']\
                    ['out_rate_pkts'] = out_rate_pkts
                continue

            # 0 packets input, 0 bytes, 0 no buffer
            p22 = re.compile(r'^(?P<in_pkts>[0-9]+) +packets +input,'
                              ' +(?P<in_octets>[0-9]+) +bytes,'
                              ' +(?P<in_no_buffer>[0-9]+) +no +buffer$')
            m = p22.match(line)
            if m:
                if 'counters' not in interface_dict[interface]:
                    interface_dict[interface]['counters'] = {}

                interface_dict[interface]['counters']['in_pkts'] = \
                    int(m.groupdict()['in_pkts'])
                interface_dict[interface]['counters']['in_octets'] = \
                    int(m.groupdict()['in_octets'])
                interface_dict[interface]['counters']['in_no_buffer'] = \
                    int(m.groupdict()['in_no_buffer'])
                continue

            # Received 4173 broadcasts (0 IP multicasts)
            # Received 535996 broadcasts (535961 multicasts)
            p23 = re.compile(r'^Received +(?P<in_broadcast_pkts>\d+) +broadcasts +'
                              '\((?P<in_multicast_pkts>\d+) *(IP)? *multicasts\)$')
            m = p23.match(line)
            if m:
                interface_dict[interface]['counters']['in_multicast_pkts'] = \
                    int(m.groupdict()['in_broadcast_pkts'])
                interface_dict[interface]['counters']['in_broadcast_pkts'] = \
                    int(m.groupdict()['in_multicast_pkts'])
                continue

            # 0 runts, 0 giants, 0 throttles
            p24 = re.compile(r'^(?P<in_runts>[0-9]+) *runts,'
                              ' *(?P<in_giants>[0-9]+) *giants,'
                              ' *(?P<in_throttles>[0-9]+) *throttles$')
            m = p24.match(line)
            if m:
                interface_dict[interface]['counters']['in_runts'] = \
                    int(m.groupdict()['in_runts'])
                interface_dict[interface]['counters']['in_giants'] = \
                    int(m.groupdict()['in_giants'])
                interface_dict[interface]['counters']['in_throttles'] = \
                    int(m.groupdict()['in_throttles'])
                continue

            # 0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
            # 0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
            p25 = re.compile(r'^(?P<in_errors>[0-9]+) +input +errors, +'
                              '(?P<in_crc_errors>[0-9]+) +CRC, +'
                              '(?P<in_frame>[0-9]+) +frame, +'
                              '(?P<in_overrun>[0-9]+) +overrun, +'
                              '(?P<in_ignored>[0-9]+) +ignored'
                              '(, *(?P<in_abort>[0-9]+) +abort)?$')
            m = p25.match(line)
            if m:
                interface_dict[interface]['counters']['in_errors'] = \
                    int(m.groupdict()['in_errors'])
                interface_dict[interface]['counters']['in_crc_errors'] = \
                    int(m.groupdict()['in_crc_errors'])
                interface_dict[interface]['counters']['in_frame'] = \
                    int(m.groupdict()['in_frame'])
                interface_dict[interface]['counters']['in_overrun'] = \
                    int(m.groupdict()['in_overrun'])
                interface_dict[interface]['counters']['in_ignored'] = \
                    int(m.groupdict()['in_ignored'])
                if m.groupdict()['in_abort']:
                    interface_dict[interface]['counters']['in_abort'] = \
                        int(m.groupdict()['in_abort'])
                continue

            # 0 watchdog, 535961 multicast, 0 pause input
            p26 = re.compile(r'^(?P<in_watchdog>[0-9]+) +watchdog, +'
                              '(?P<in_multicast_pkts>[0-9]+) +multicast, +'
                              '(?P<in_pause_input>[0-9]+) +pause +input$')
            m = p26.match(line)
            if m:
                interface_dict[interface]['counters']['in_watchdog'] = \
                    int(m.groupdict()['in_watchdog'])
                interface_dict[interface]['counters']['in_multicast_pkts'] = \
                    int(m.groupdict()['in_multicast_pkts'])
                interface_dict[interface]['counters']['in_mac_pause_frames'] = \
                    int(m.groupdict()['in_pause_input'])
                continue

            # 0 input packets with dribble condition detected
            p27 = re.compile(r'^(?P<in_with_dribble>[0-9]+) +input +packets +with +'
                              'dribble +condition +detected$')
            m = p27.match(line)
            if m:
                interface_dict[interface]['counters']['in_with_dribble'] = \
                    int(m.groupdict()['in_with_dribble'])
                continue

            # 23376 packets output, 3642296 bytes, 0 underruns
            p28 = re.compile(r'^(?P<out_pkts>[0-9]+) +packets +output,'
                              ' +(?P<out_octets>[0-9]+) +bytes,'
                              ' +(?P<out_underruns>[0-9]+) +underruns$')
            m = p28.match(line)
            if m:
                interface_dict[interface]['counters']['out_pkts'] = \
                    int(m.groupdict()['out_pkts'])
                interface_dict[interface]['counters']['out_octets'] = \
                    int(m.groupdict()['out_octets'])
                interface_dict[interface]['counters']['out_underruns'] = \
                    int(m.groupdict()['out_underruns'])
                continue

            # Received 4173 broadcasts (0 IP multicasts)
            # Received 535996 broadcasts (535961 multicasts)
            p29 = re.compile(r'^Received +(?P<out_broadcast_pkts>\d+) +broadcasts +'
                              '\((?P<out_multicast_pkts>\d+) *(IP)? *multicasts\)$')
            m = p29.match(line)
            if m:
                interface_dict[interface]['counters']['out_broadcast_pkts'] = \
                    int(m.groupdict()['out_broadcast_pkts'])
                interface_dict[interface]['counters']['out_multicast_pkts'] = \
                    int(m.groupdict()['out_multicast_pkts'])
                continue

            # 0 output errors, 0 collisions, 2 interface resets
            # 0 output errors, 0 interface resets
            p30 = re.compile(r'^(?P<out_errors>[0-9]+) +output +errors,'
                              '( *(?P<out_collision>[0-9]+) +collisions,)? +'
                              '(?P<out_interface_resets>[0-9]+) +interface +resets$')
            m = p30.match(line)
            if m:
                interface_dict[interface]['counters']['out_errors'] = \
                    int(m.groupdict()['out_errors'])
                interface_dict[interface]['counters']['out_interface_resets'] = \
                    int(m.groupdict()['out_interface_resets'])
                if m.groupdict()['out_collision']:
                    interface_dict[interface]['counters']['out_collision'] = \
                        int(m.groupdict()['out_collision'])
                continue

            # 0 unknown protocol drops
            p31 = re.compile(r'^(?P<out_unknown_protocl_drops>[0-9]+) +'
                              'unknown +protocol +drops$')
            m = p31.match(line)
            if m:
                interface_dict[interface]['counters']['out_unknown_protocl_drops'] = \
                    int(m.groupdict()['out_unknown_protocl_drops'])
                continue

            # 0 babbles, 0 late collision, 0 deferred
            p32 = re.compile(r'^(?P<out_babble>[0-9]+) +babbles, +'
                              '(?P<out_late_collision>[0-9]+) +late +collision, +'
                              '(?P<out_deferred>[0-9]+) +deferred$')
            m = p32.match(line)
            if m:
                interface_dict[interface]['counters']['out_babble'] = \
                    int(m.groupdict()['out_babble'])
                interface_dict[interface]['counters']['out_late_collision'] = \
                    int(m.groupdict()['out_late_collision'])
                interface_dict[interface]['counters']['out_deferred'] = \
                    int(m.groupdict()['out_deferred'])
                continue

            # 0 lost carrier, 0 no carrier, 0 pause output
            p33 = re.compile(r'^(?P<out_lost_carrier>[0-9]+) +lost +carrier, +'
                              '(?P<out_no_carrier>[0-9]+) +no +carrier, +'
                              '(?P<out_pause_output>[0-9]+) +pause +output$')
            m = p33.match(line)
            if m:
                interface_dict[interface]['counters']['out_lost_carrier'] = \
                    int(m.groupdict()['out_lost_carrier'])
                interface_dict[interface]['counters']['out_no_carrier'] = \
                    int(m.groupdict()['out_no_carrier'])
                interface_dict[interface]['counters']['out_mac_pause_frames'] = \
                    int(m.groupdict()['out_pause_output'])
                continue

            # 0 output buffer failures, 0 output buffers swapped out
            p34 = re.compile(r'^(?P<out_buffer_failure>[0-9]+) +output +buffer +failures, +'
                              '(?P<out_buffers_swapped>[0-9]+) +output +buffers +swapped +out$')
            m = p34.match(line)
            if m:
                interface_dict[interface]['counters']['out_buffer_failure'] = \
                    int(m.groupdict()['out_buffer_failure'])
                interface_dict[interface]['counters']['out_buffers_swapped'] = \
                    int(m.groupdict()['out_buffers_swapped'])
                continue

            # Interface is unnumbered. Using address of Loopback0 (10.4.1.1)
            # Interface is unnumbered. Using address of GigabitEthernet0/2.1 (192.168.154.1)
            p35 = re.compile(r'^Interface +is +unnumbered. +Using +address +of +'
                              '(?P<unnumbered_intf>[\w\/\.]+) +'
                              '\((?P<unnumbered_ip>[\w\.\:]+)\)$')
            m = p35.match(line)
            if m:
                unnumbered_dict[interface] = {}
                unnumbered_dict[interface]['unnumbered_intf'] = m.groupdict()['unnumbered_intf']
                unnumbered_dict[interface]['unnumbered_ip'] = m.groupdict()['unnumbered_ip']
                continue

        # create strucutre for unnumbered interface
        if not unnumbered_dict:
            return(interface_dict)

        for intf in unnumbered_dict:
            unnumbered_intf = unnumbered_dict[intf]['unnumbered_intf']
            unnumbered_ip = unnumbered_dict[intf]['unnumbered_ip']
            if unnumbered_intf in interface_dict:
                if 'ipv4' in interface_dict[unnumbered_intf]:
                    for ip in interface_dict[unnumbered_intf]['ipv4']:
                        if unnumbered_ip in ip:
                            if 'ipv4' not in interface_dict[intf]:
                                interface_dict[intf]['ipv4'] = {}
                            if ip not in interface_dict[intf]['ipv4']:
                                interface_dict[intf]['ipv4'][ip] = {}
                            m = re.search('([\w\.\:]+)\/(\d+)', ip)
                            interface_dict[intf]['ipv4'][ip]['ip'] = m.groups()[0]
                            interface_dict[intf]['ipv4'][ip]['prefix_length'] = m.groups()[1]
                            interface_dict[intf]['ipv4']['unnumbered'] = {}
                            interface_dict[intf]['ipv4']['unnumbered']\
                                ['interface_ref'] = unnumbered_intf
        return(interface_dict)


# parser using parsergen
# ----------------------
class ShowIpInterfaceBriefSchema(MetaParser):
    """Parser for show ip interface brief"""
    schema = {'interface':
                {Any():
                    {Optional('vlan_id'):
                        {Optional(Any()):
                                {'ip_address': str,
                                 Optional('interface_is_ok'): str,
                                 Optional('method'): str,
                                 Optional('status'): str,
                                 Optional('protocol'): str}
                        },
                     Optional('ip_address'): str,
                     Optional('interface_is_ok'): str,
                     Optional('method'): str,
                     Optional('status'): str,
                     Optional('protocol'): str}
                },
            }

class ShowIpInterfaceBrief(ShowIpInterfaceBriefSchema):
    """Parser for:
     show ip interface brief
     parser class implements detail parsing mechanisms for cli and yang output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    def __init__ (self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    cli_command = ['show ip interface brief {interface}','show ip interface brief']

    def cli(self, interface='',output=None):
        """parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        """
        parsed_dict = {}

        if output is None:
            if interface:
                cmd = self.cli_command[0].format(interface=interface)
            else:
                cmd = self.cli_command[1]

            out = self.device.execute(cmd)
        else:
            out = output

        if out:
            res = parsergen.oper_fill_tabular(device_output=out,
                                              device_os='iosxe',
                                              table_terminal_pattern=r"^\n",
                                              header_fields=
                                               [ "Interface",
                                                 "IP-Address",
                                                 "OK\?",
                                                 "Method",
                                                 "Status",
                                                 "Protocol" ],
                                              label_fields=
                                               [ "Interface",
                                                 "ip_address",
                                                 "interface_is_ok",
                                                 "method",
                                                 "status",
                                                 "protocol" ],
                                              index=[0])

            # Building the schema out o fthe parsergen output
            if res.entries:
                for intf in res.entries:
                    del res.entries[intf]['Interface']

                parsed_dict['interface'] = res.entries
        return (parsed_dict)

    def yang(self):
        """ parsing mechanism: yang

        Function yang() defines the yang type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        """
        pass

    def yang_cli(self):
        cli_output = self.cli()
        yang_output = self.yang()
        merged_output = _merge_dict(yang_output,cli_output)
        return merged_output

class ShowIpInterfaceBriefPipeVlan(ShowIpInterfaceBrief):
    """Parser for:
     show ip interface brief | include Vlan
     parser class implements detail parsing mechanisms for cli and yang output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    cli_command = "show ip interface brief | include Vlan"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cmd = self.cli_command

    def cli(self):
        super(ShowIpInterfaceBriefPipeVlan, self).cli()

    def yang(self):
        """parsing mechanism: yang

        Function yang() defines the yang type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        """

        ret = {}
        cmd = '''<native><interface><Vlan/></interface></native>'''
        output = self.device.get(('subtree', cmd))

        for data in output.data:
            for native in data:
                for interface in native:
                    vlan_id = None
                    interface_name = None
                    ip_address = None
                    ip_mask = None
                    for vlan in interface:
                        # Remove the namespace
                        text = vlan.tag[vlan.tag.find('}')+1:]
                        #ydk.models.ned_edison.ned.Native.Interface.Vlan.name
                        #ydk.models.xe_recent_edison.Cisco_IOS_XE_native.Native.Interface.Vlan.name
                        if text == 'name':
                            vlan_id = vlan.text
                            interface_name = 'Vlan' + str(vlan_id)
                            continue
                        if text == 'ip':
                            for ip in vlan:
                                text = ip.tag[ip.tag.find('}')+1:]
                                #ydk.models.ned_edison.ned.Native.Interface.Vlan.ip.address
                                #ydk.models.xe_recent_edison.Cisco_IOS_XE_native.Native.Interface.Vlan.ip.address
                                if text == 'address':
                                    for address in ip:
                                        text = address.tag[address.tag.find('}')+1:]
                                        #ydk.models.ned_edison.ned.Native.Interface.Vlan.ip.address.primary
                                        #ydk.models.xe_recent_edison.Cisco_IOS_XE_native.Native.Interface.Vlan.ip.address.primary
                                        if text == 'primary':
                                            for primary in address:
                                                # Remove the namespace
                                                text = primary.tag[primary.tag.find('}')+1:]
                                                #ydk.models.ned_edison.ned.Native.Interface.Vlan.ip.address.primary.address
                                                #ydk.models.xe_recent_edison.Cisco_IOS_XE_native.Native.Interface.Vlan.ip.address.primary.address
                                                if text == 'address':
                                                    ip_address = primary.text
                                                    continue
                                                #ydk.models.ned_edison.ned.Native.Interface.Vlan.ip.address.primary.mask
                                                #ydk.models.xe_recent_edison.Cisco_IOS_XE_native.Native.Interface.Vlan.ip.address.primary.mask
                                                if text == 'mask':
                                                    ip_mask = primary.text
                                                    continue
                    # Let's build it now
                    if 'interface' not in ret:
                        ret['interface'] = {}
                    if interface_name is not None:
                        ret['interface'][interface_name] = {}
                        if vlan_id is not None:
                            ret['interface'][interface_name]['vlan_id'] = {}
                            ret['interface'][interface_name]['vlan_id'][vlan_id] = {}
                            if ip_address is not None:
                                ret['interface'][interface_name]['vlan_id'][vlan_id]['ip_address'] = ip_address
                            else:
                                ret['interface'][interface_name]['vlan_id'][vlan_id]['ip_address'] = 'unassigned'

        return ret

    def yang_cli(self):
        super(ShowIpInterfaceBriefPipeVlan, self).yang_cli()


class ShowIpInterfaceBriefPipeIpSchema(MetaParser):
    """Schema for show ip interface brief | include <WORD>"""
    schema = {'interface':
                {Any():
                    {Optional('ip_address'): str,
                    Optional('interface_ok'): str,
                    Optional('method'): str,
                    Optional('interface_status'): str,
                    Optional('protocol_status'): str}
                },
            }


class ShowIpInterfaceBriefPipeIp(ShowIpInterfaceBriefPipeIpSchema):
    """Parser for:
     show ip interface brief | include <WORD>
     parser class implements detail parsing mechanisms for cli and yang output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    cli_command = 'show ip interface brief | include {ip}'
    def cli(self, ip,output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(ip=ip))
        else:
            out = output
        interface_dict = {}

        # GigabitEthernet0/0     10.1.18.80      YES manual up                    up
        p = re.compile(r'^\s*(?P<interface>[a-zA-Z0-9\/\.\-]+) '
            '+(?P<ip_address>[a-z0-9\.]+) +(?P<interface_ok>[A-Z]+) '
            '+(?P<method>[a-zA-Z]+) +(?P<interface_status>[a-z\s]+) '
            '+(?P<protocol_status>[a-z]+)$')

        for line in out.splitlines():
            line = line.strip()

            m = p.match(line)
            if m:
                interface = m.groupdict()['interface']
                if 'interface' not in interface_dict:
                    interface_dict['interface'] = {}
                if interface not in interface_dict['interface']:
                    interface_dict['interface'][interface] = {}

                interface_dict['interface'][interface]['ip_address'] = \
                    m.groupdict()['ip_address']
                interface_dict['interface'][interface]['interface_ok'] = \
                    m.groupdict()['interface_ok']
                interface_dict['interface'][interface]['method'] = \
                    m.groupdict()['method']
                interface_dict['interface'][interface]['interface_status'] = \
                    m.groupdict()['interface_status'].strip()
                interface_dict['interface'][interface]['protocol_status'] = \
                    m.groupdict()['protocol_status']

                continue

        return interface_dict

class ShowInterfacesSwitchportSchema(MetaParser):
    """Schema for show interfaces switchport"""
    schema = {
                Any(): {
                    'switchport_enable': bool,
                    'switchport_mode': str,
                    Optional('operational_mode'): str,
                    Optional('port_channel'): {
                        Optional('port_channel_int'): str,
                        Optional('port_channel_member_intfs'): list,
                        Optional('port_channel_member'): bool,
                    },
                    Optional('encapsulation'): {
                        Optional('administrative_encapsulation'): str,
                        Optional('operational_encapsulation'): str,
                        Optional('native_vlan'): str,
                    },
                    Optional('negotiation_of_trunk'): bool,
                    Optional('access_vlan'): str,
                    Optional('native_vlan_tagging'): bool,
                    Optional('private_vlan'): {
                        Optional('host_association'): str,
                        Optional('mapping'): str,
                        Optional('native_vlan'): str,
                        Optional('native_vlan_tagging'): bool,
                        Optional('encapsulation'): str,
                        Optional('normal_vlans'): str,
                        Optional('associations'): str,
                        Optional('trunk_mappings'): str,
                        Optional('operational'): str,
                    },
                    Optional('trunk_vlans'): str,
                    Optional('pruning_vlans'): str,
                    Optional('capture_mode'): bool,
                    Optional('capture_vlans'): str,
                    Optional('protected'): bool,
                    Optional('unknown_unicast_blocked'): bool,
                    Optional('unknown_multicast_blocked'): bool,
                    Optional('appliance_trust'): str,
                },
            }

class ShowInterfacesSwitchport(ShowInterfacesSwitchportSchema):
    """parser for show interfaces switchport"""

    cli_command = 'show interfaces switchport'

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}
        private_trunk_mappings = None
        private_operational = None
        for line in out.splitlines():
            line = line.strip()

            # Name: Gi1/0/2
            p1 =  re.compile(r'^Name: +(?P<intf>[\w\/\.\-]+)$')
            m = p1.match(line)
            if m:
                intf = Common.convert_intf_name(m.groupdict()['intf'])
                if intf not in ret_dict:
                    ret_dict[intf] = {}
                continue

            # Switchport: Enabled
            p2 =  re.compile(r'^Switchport: +(?P<switchport_enable>\w+)$')
            m = p2.match(line)
            if m:
                if m.groupdict()['switchport_enable'].lower() == 'enabled':
                    ret_dict[intf]['switchport_enable'] = True
                else:
                    ret_dict[intf]['switchport_enable'] = False
                continue

            # Administrative Mode: trunk
            p3 =  re.compile(r'^Administrative +Mode: +(?P<switchport_mode>[\w\s]+)$')
            m = p3.match(line)
            if m:
                ret_dict[intf]['switchport_mode'] = m.groupdict()['switchport_mode']
                continue

            # Operational Mode: trunk (member of bundle Po12)
            # Operational Mode: down (suspended member of bundle Po12)
            p4 =  re.compile(r'^Operational +Mode: +(?P<operational_mode>[\w\s]+)'
                              '( +\((?P<dummy>[\w\s]+)? *member +of +bundle +(?P<port_channel_int>[\w\/\.\-]+)\))?$')
            m = p4.match(line)
            if m:
                ret_dict[intf]['operational_mode'] = m.groupdict()['operational_mode']

                bundle_intf = m.groupdict()['port_channel_int']
                if bundle_intf:
                    if 'port_channel' not in ret_dict[intf]:
                        ret_dict[intf]['port_channel'] = {}
                    bundle_intf = Common.convert_intf_name(bundle_intf)

                    ret_dict[intf]['port_channel']['port_channel_int'] = bundle_intf
                    ret_dict[intf]['port_channel']['port_channel_member'] = True

                    # bundle interface is port_channel interface as well
                    if bundle_intf not in ret_dict:
                        ret_dict[bundle_intf] = {}
                    if 'port_channel' not in ret_dict[bundle_intf]:
                        ret_dict[bundle_intf]['port_channel'] = {}

                    ret_dict[bundle_intf]['port_channel']['port_channel_member'] = True

                    # append the list
                    if 'port_channel_member_intfs' in ret_dict[bundle_intf]['port_channel']:
                        port_list = ret_dict[bundle_intf]['port_channel']['port_channel_member_intfs']
                        port_list.append(intf)
                        ret_dict[bundle_intf]['port_channel']['port_channel_member_intfs'] = port_list
                    else:
                        ret_dict[bundle_intf]['port_channel']['port_channel_member_intfs'] = [intf]
                continue

            # Administrative Trunking Encapsulation: dot1q
            p5 =  re.compile(r'^Administrative +Trunking +Encapsulation: +'
                              '(?P<encapsulation>\w+)$')
            m = p5.match(line)
            if m:
                if 'encapsulation' not in ret_dict[intf]:
                    ret_dict[intf]['encapsulation'] = {}
                ret_dict[intf]['encapsulation']['administrative_encapsulation'] = \
                    m.groupdict()['encapsulation'].lower()
                continue

            # Operational Trunking Encapsulation: dot1q
            p6 =  re.compile(r'^Operational +Trunking +Encapsulation: +'
                              '(?P<encapsulation>\w+)$')
            m = p6.match(line)
            if m:
                if 'encapsulation' not in ret_dict[intf]:
                    ret_dict[intf]['encapsulation'] = {}
                ret_dict[intf]['encapsulation']['operational_encapsulation'] = \
                    m.groupdict()['encapsulation'].lower()
                continue

            # Negotiation of Trunking: On
            p7 =  re.compile(r'^Negotiation +of +Trunking: +(?P<negotiation_of_trunk>\w+)$')
            m = p7.match(line)
            if m:
                negotiation_of_trunk = m.groupdict()['negotiation_of_trunk'].lower()
                if 'on' in negotiation_of_trunk:
                    ret_dict[intf]['negotiation_of_trunk'] = True
                elif 'off' in negotiation_of_trunk:
                    ret_dict[intf]['negotiation_of_trunk'] = False                    
                continue

            # Access Mode VLAN: 1 (default)
            p8 =  re.compile(r'^Access +Mode +VLAN: +(?P<access_vlan>[\d\-]+)'
                              '( *\((?P<dummy>\w+)\))?$')
            m = p8.match(line)
            if m:
                ret_dict[intf]['access_vlan'] = m.groupdict()['access_vlan']
                continue

            # Trunking Native Mode VLAN: 1 (default)
            p9 =  re.compile(r'^Trunking +Native +Mode +VLAN: +(?P<native_vlan>[\d\-]+)'
                              '( *\((?P<dummy>\w+)\))?$')
            m = p9.match(line)
            if m:
                if 'encapsulation' not in ret_dict[intf]:
                    ret_dict[intf]['encapsulation'] = {}
                ret_dict[intf]['encapsulation']['native_vlan'] = m.groupdict()['native_vlan']
                continue

            # Administrative Native VLAN tagging: enabled
            p10 =  re.compile(r'^Administrative +Native +VLAN +tagging: +'
                               '(?P<tagging>\w+)$')
            m = p10.match(line)
            if m:
                if 'enable' in m.groupdict()['tagging'].lower():
                    ret_dict[intf]['native_vlan_tagging'] = True
                else:
                    ret_dict[intf]['native_vlan_tagging'] = False
                continue

            # Voice VLAN: none
            p11 =  re.compile(r'^Voice +VLAN: +(?P<vlan>[\d\-]+)$')
            m = p11.match(line)
            if m:
                ret_dict[intf]['voice_vlan'] = m.groupdict()['vlan']
                continue

            # Administrative private-vlan host-association: none 
            p12 =  re.compile(r'^Administrative +private-vlan +'
                               'host-association: +(?P<ret>[\w\-]+)$')
            m = p12.match(line)
            if m:
                if 'private_vlan' not in ret_dict[intf]:
                    ret_dict[intf]['private_vlan'] = {}
                ret = m.groupdict()['ret'].lower()
                if ret != 'none':
                    ret_dict[intf]['private_vlan']['host_association'] = m.groupdict()['ret']
                continue

            # Administrative private-vlan mapping: none 
            p13 =  re.compile(r'^Administrative +private-vlan +'
                               'mapping: +(?P<ret>[\w\-]+)$')
            m = p13.match(line)
            if m:
                if 'private_vlan' not in ret_dict[intf]:
                    ret_dict[intf]['private_vlan'] = {}
                ret = m.groupdict()['ret'].lower()
                if ret != 'none':
                    ret_dict[intf]['private_vlan']['mapping'] = m.groupdict()['ret']
                continue

            # Administrative private-vlan trunk native VLAN: none
            p14 =  re.compile(r'^Administrative +private-vlan +'
                               'trunk +native +VLAN: +(?P<ret>[\w\-]+)$')
            m = p14.match(line)
            if m:
                if 'private_vlan' not in ret_dict[intf]:
                    ret_dict[intf]['private_vlan'] = {}
                ret = m.groupdict()['ret'].lower()
                if ret != 'none':
                    ret_dict[intf]['private_vlan']['native_vlan'] = m.groupdict()['ret']
                continue

            # Administrative private-vlan trunk Native VLAN tagging: enabled
            p15 =  re.compile(r'^Administrative +private-vlan +'
                               'trunk +Native +VLAN +tagging: +(?P<ret>[\w\-]+)$')
            m = p15.match(line)
            if m:
                if 'private_vlan' not in ret_dict[intf]:
                    ret_dict[intf]['private_vlan'] = {}
                ret = m.groupdict()['ret'].lower()
                if 'enable' in ret:
                    ret_dict[intf]['private_vlan']['native_vlan_tagging'] = True
                else:
                    ret_dict[intf]['private_vlan']['native_vlan_tagging'] = False                    
                continue

            # Administrative private-vlan trunk encapsulation: dot1q
            p16 =  re.compile(r'^Administrative +private-vlan +'
                               'trunk +encapsulation: +(?P<ret>[\w\-]+)$')
            m = p16.match(line)
            if m:
                if 'private_vlan' not in ret_dict[intf]:
                    ret_dict[intf]['private_vlan'] = {}
                ret = m.groupdict()['ret'].lower()
                if ret != 'none':
                    ret_dict[intf]['private_vlan']['encapsulation'] = m.groupdict()['ret']
                continue

            # Administrative private-vlan trunk normal VLANs: none
            p17 =  re.compile(r'^Administrative +private-vlan +'
                               'trunk +normal +VLANs: +(?P<ret>[\w\-]+)$')
            m = p17.match(line)
            if m:
                if 'private_vlan' not in ret_dict[intf]:
                    ret_dict[intf]['private_vlan'] = {}
                ret = m.groupdict()['ret'].lower()
                if ret != 'none':
                    ret_dict[intf]['private_vlan']['normal_vlans'] = m.groupdict()['ret']
                continue

            # Administrative private-vlan trunk associations: none
            p18 =  re.compile(r'^Administrative +private-vlan +'
                               'trunk +associations: +(?P<ret>[\w\-]+)$')
            m = p18.match(line)
            if m:
                if 'private_vlan' not in ret_dict[intf]:
                    ret_dict[intf]['private_vlan'] = {}
                ret = m.groupdict()['ret'].lower()
                if ret != 'none':
                    ret_dict[intf]['private_vlan']['associations'] = m.groupdict()['ret']
                continue

            # Administrative private-vlan trunk mappings: none
            # Administrative private-vlan trunk mappings:
            p19 =  re.compile(r'^Administrative +private-vlan +'
                               'trunk +mappings:( *(?P<ret>[\w\-]+))?$')
            m = p19.match(line)
            if m:
                if 'private_vlan' not in ret_dict[intf]:
                    ret_dict[intf]['private_vlan'] = {}
                private_trunk_mappings = m.groupdict()['ret']
                if private_trunk_mappings and private_trunk_mappings.lower() != 'none':
                    ret_dict[intf]['private_vlan']['trunk_mappings'] = private_trunk_mappings
                private_trunk_mappings = ''
                continue

            # 10 (VLAN0010) 100 (VLAN0100)
            if isinstance(private_trunk_mappings, str):
                p19_1 =  re.compile(r'^(?P<mappings>[\w\(\)\s]+)$')
                m = p19_1.match(line)
                if m:
                    ret = m.groupdict()['mappings']
                    private_trunk_mappings += ' {}'.format(ret)
                    ret_dict[intf]['private_vlan']['trunk_mappings'] = private_trunk_mappings.strip()
                # reset private_trunk_mappings
                private_trunk_mappings = None
                continue

            # Operational private-vlan: none
            # Operational private-vlan:
            p20 =  re.compile(r'^Operational +private-vlan:'
                               '( *(?P<private_operational>[\w\-]+))?$')
            m = p20.match(line)
            if m:
                if 'private_vlan' not in ret_dict[intf]:
                    ret_dict[intf]['private_vlan'] = {}
                private_operational = m.groupdict()['private_operational']
                if private_operational and private_operational.lower() != 'none':
                    ret_dict[intf]['private_vlan']['operational'] = private_operational
                private_operational = ''
                continue

            # 10 (VLAN0010) 100 (VLAN0100)
            if isinstance(private_operational, str):
                p20_1 =  re.compile(r'^(?P<private_operational>[\w\(\)\s]+)$')
                m = p20_1.match(line)
                if m:
                    ret = m.groupdict()['private_operational']
                    private_operational += ' {}'.format(ret)
                    ret_dict[intf]['private_vlan']['operational'] = private_operational.strip()
                # reset private_trunk_mappings
                private_operational = None
                continue

            # Trunking VLANs Enabled: 200-211
            # Trunking VLANs Enabled: 1,2
            p21 =  re.compile(r'^Trunking +VLANs +Enabled: +(?P<trunk_vlans>[\w\-\,\s]+)$')
            m = p21.match(line)
            if m:
                ret_dict[intf]['trunk_vlans'] = m.groupdict()['trunk_vlans'].lower()
                continue

            # Pruning VLANs Enabled: 2-1001
            p22 =  re.compile(r'^Pruning +VLANs +Enabled: +(?P<pruning_vlans>[\w\-]+)$')
            m = p22.match(line)
            if m:
                ret_dict[intf]['pruning_vlans'] = m.groupdict()['pruning_vlans'].lower()
                continue

            # Capture Mode Disabled
            p23 =  re.compile(r'^Capture +Mode +(?P<mode>\w+)$')
            m = p23.match(line)
            if m:
                mode = m.groupdict()['mode'].lower()
                if 'disabled' in mode:
                    ret_dict[intf]['capture_mode'] = False
                else:
                    ret_dict[intf]['capture_mode'] = True
                continue

            # Capture VLANs Allowed: ALL
            p24 =  re.compile(r'^Capture +VLANs +Allowed: +(?P<capture_vlans>[\w\-]+)$')
            m = p24.match(line)
            if m:
                ret_dict[intf]['capture_vlans'] = m.groupdict()['capture_vlans'].lower()
                continue

            # Protected: false
            p25 =  re.compile(r'^Protected: +(?P<protected>\w+)$')
            m = p25.match(line)
            if m:
                if 'false' in m.groupdict()['protected'].lower():
                    ret_dict[intf]['protected'] = False
                else:
                    ret_dict[intf]['protected'] = True
                continue

            # Unknown unicast blocked: disabled
            p26 =  re.compile(r'^Unknown +unicast +blocked: +(?P<block>\w+)$')
            m = p26.match(line)
            if m:
                if 'disabled' in m.groupdict()['block'].lower():
                    ret_dict[intf]['unknown_unicast_blocked'] = False
                else:
                    ret_dict[intf]['unknown_unicast_blocked'] = True
                continue

            # Unknown multicast blocked: disabled
            p21 =  re.compile(r'^Unknown +multicast +blocked: +(?P<block>\w+)$')
            m = p21.match(line)
            if m:
                if 'disabled' in m.groupdict()['block'].lower():
                    ret_dict[intf]['unknown_multicast_blocked'] = False
                else:
                    ret_dict[intf]['unknown_multicast_blocked'] = True
                continue

            # Appliance trust: none
            p21 =  re.compile(r'^Appliance +trust: +(?P<trust>[\w\-]+)$')
            m = p21.match(line)
            if m:
                if  m.groupdict()['trust'] != 'none':
                    ret_dict[intf]['appliance_trust'] = m.groupdict()['trust']
                continue
        return ret_dict


class ShowIpInterfaceSchema(MetaParser):
    """Schema for show ip interface
                  show ip interface <interface>"""
    schema = {
                Any(): {
                    'enabled': bool,
                    'oper_status': str,
                    Optional('ipv4'): {
                        Any(): {
                            'ip': str,
                            Optional('prefix_length'): str,
                            Optional('secondary'): bool,
                            Optional('broadcase_address'): str,
                        },
                    },
                    Optional('mtu'): int,
                    Optional('address_determined_by'): str,
                    Optional('helper_address'): str,
                    Optional('directed_broadcast_forwarding'): bool,
                    Optional('out_common_access_list'): str,
                    Optional('out_access_list'): str,
                    Optional('inbound_common_access_list'): str,
                    Optional('inbound_access_list'): str,
                    Optional('proxy_arp'): bool,
                    Optional('local_proxy_arp'): bool,
                    Optional('sevurity_level'): str,
                    Optional('split_horizon'): bool,
                    Optional('icmp'): {
                        Optional('redirects'): str,
                        Optional('unreachables'): str,
                        Optional('mask_replies'): str,
                    },
                    Optional('wccp'): {
                        Optional('redirect_outbound'): bool,
                        Optional('redirect_inbound'): bool,
                        Optional('redirect_exclude'): bool,
                    },
                    Optional('ip_fast_switching'): bool,
                    Optional('ip_flow_switching'): bool,
                    Optional('ip_cef_switching'): bool,
                    Optional('ip_cef_switching_turbo_vector'): bool,
                    Optional('ip_null_turbo_vector'): bool,
                    Optional('vrf'): str,
                    Optional('unicast_routing_topologies'): {
                        'topology': {
                            Any(): {
                                'status': str,
                            }
                        },                       
                    },
                    Optional('ip_multicast_fast_switching'): bool,
                    Optional('ip_multicast_distributed_fast_switching'): bool,
                    Optional('ip_route_cache_flags'): list,
                    Optional('router_discovery'): bool,
                    Optional('ip_output_packet_accounting'): bool,
                    Optional('ip_access_violation_accounting'): bool,
                    Optional('tcp_ip_header_compression'): bool,
                    Optional('rtp_ip_header_compression'): bool,
                    Optional('probe_proxy_name_replies'): bool,
                    Optional('policy_routing'): bool,
                    Optional('network_address_translation'): bool,
                    Optional('bgp_policy_mapping'): bool,
                    Optional('input_features'): list,
                    Optional('multicast_groups'): list,
                },
            }

class ShowIpInterface(ShowIpInterfaceSchema):
    """Parser for show ip interface
                  show ip interface <interface>"""

    cli_command = ['show ip interface','show ip interface {interface}']

    def cli(self,interface="",output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[1].format(interface=interface)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        interface_dict = {}
        unnumbered_dict = {}
        for line in out.splitlines():
            line = line.strip()

            # Vlan211 is up, line protocol is up
            # GigabitEthernet2 is administratively down, line protocol is down
            p1 =  re.compile(r'^(?P<interface>[\w\/\.\-]+) +is'
                              ' +(?P<enabled>[\w\s]+),'
                              ' +line +protocol +is +(?P<oper_status>\w+)$')
            m = p1.match(line)
            if m:
                interface = m.groupdict()['interface']
                enabled = m.groupdict()['enabled'].lower()
                if interface not in interface_dict:
                    interface_dict[interface] = {}
                if 'down' in enabled or 'delete' in enabled:
                    interface_dict[interface]['enabled'] = False
                else:
                    interface_dict[interface]['enabled'] = True
                interface_dict[interface]['oper_status'] = \
                    m.groupdict()['oper_status'].lower()

                # initial variables
                multicast_groups = []
                continue

            # Internet address is 192.168.76.1/24
            p2 = re.compile(r'^Internet +[A|a]ddress +is +(?P<ipv4>(?P<ip>[0-9\.]+)'
                             '\/(?P<prefix_length>[0-9]+))$')
            m = p2.match(line)
            if m:
                ip = m.groupdict()['ip']
                prefix_length = m.groupdict()['prefix_length']
                address = m.groupdict()['ipv4']

                if 'ipv4' not in interface_dict[interface]:
                    interface_dict[interface]['ipv4'] = {}
                if address not in interface_dict[interface]['ipv4']:
                    interface_dict[interface]['ipv4'][address] = {}

                interface_dict[interface]['ipv4'][address]\
                    ['ip'] = ip
                interface_dict[interface]['ipv4'][address]\
                    ['prefix_length'] = prefix_length
                interface_dict[interface]['ipv4'][address]\
                    ['secondary'] = False
                continue

            # Secondary address 10.2.2.2/24
            p2_1 = re.compile(r'^Secondary +address +(?P<ipv4>(?P<ip>[0-9\.]+)'
                             '\/(?P<prefix_length>[0-9]+))$')
            m = p2_1.match(line)
            if m:
                ip = m.groupdict()['ip']
                prefix_length = m.groupdict()['prefix_length']
                address = m.groupdict()['ipv4']

                if 'ipv4' not in interface_dict[interface]:
                    interface_dict[interface]['ipv4'] = {}
                if address not in interface_dict[interface]['ipv4']:
                    interface_dict[interface]['ipv4'][address] = {}

                interface_dict[interface]['ipv4'][address]\
                    ['ip'] = ip
                interface_dict[interface]['ipv4'][address]\
                    ['prefix_length'] = prefix_length
                interface_dict[interface]['ipv4'][address]\
                    ['secondary'] = True
                continue

            # Broadcast address is 255.255.255.255
            p3 = re.compile(r'^Broadcast +address +is +(?P<address>[\w\.\:]+)$')
            m = p3.match(line)
            if m:
                interface_dict[interface]['ipv4'][address]['broadcase_address'] = \
                    m.groupdict()['address']
                continue

            # Address determined by configuration file
            # Address determined by non-volatile memory
            p36 = re.compile(r'^Address +determined +by +(?P<file>[\w\s\-]+)$')
            m = p36.match(line)
            if m:
                interface_dict[interface]['address_determined_by'] = \
                    m.groupdict()['file']
                continue

            # MTU is 1500 bytes
            p4 = re.compile(r'^MTU +is +(?P<mtu>\d+) +bytes$')
            m = p4.match(line)
            if m:
                interface_dict[interface]['mtu'] = \
                    int(m.groupdict()['mtu'])
                continue

            # Helper address is not set
            p5 = re.compile(r'^Helper +address +is +(?P<address>[\w\.\:\s]+)$')
            m = p5.match(line)
            if m:
                if 'not set' not in m.groupdict()['address']:
                    interface_dict[interface]['helper_address'] = \
                        m.groupdict()['address']
                continue

            # Directed broadcast forwarding is disabled
            p6 = re.compile(r'^Directed +broadcast +forwarding +is +(?P<status>\w+)$')
            m = p6.match(line)
            if m:
                if 'disabled' in m.groupdict()['status']:
                    interface_dict[interface]['directed_broadcast_forwarding'] = False
                else:
                    interface_dict[interface]['directed_broadcast_forwarding'] = True                    
                continue

            # Multicast reserved groups joined: 224.0.0.1 224.0.0.2 224.0.0.22 224.0.0.13
            p41 = re.compile(r'^Multicast +reserved +groups +joined: +(?P<multicast_groups>[\w\s\.]+)$')
            m = p41.match(line)
            if m:
                multicast_groups_address = str(m.groupdict()['multicast_groups'])

                #Split string of addressed into a list
                multicast_groups = multicast_groups_address.split()

                interface_dict[interface]['multicast_groups']\
                 = sorted(multicast_groups)                              
                continue

            # Multicast reserved groups joined: 224.0.0.1 224.0.0.2 224.0.0.22 224.0.0.13
            p41_1 = re.compile(r'(?P<multicast_groups>\d+\.\d+\.\d+\.\d+)')
            m = p41_1.findall(line)
            if m and multicast_groups:
                multicast_groups.extend(m)
                interface_dict[interface]['multicast_groups']\
                 = sorted(multicast_groups)                              
                continue

            # Outgoing Common access list is not set 
            p7 = re.compile(r'^Outgoing +Common +access +list +is +'
                             '(?P<access_list>[\w\s]+)$')
            m = p7.match(line)
            if m:
                if 'not set' not in m.groupdict()['access_list']:
                    interface_dict[interface]['out_common_access_list'] = \
                        m.groupdict()['access_list']
                continue

            # Outgoing access list is not set
            p8 = re.compile(r'^Outgoing +access +list +is +'
                             '(?P<access_list>[\w\s]+)$')
            m = p8.match(line)
            if m:
                if 'not set' not in m.groupdict()['access_list']:
                    interface_dict[interface]['out_access_list'] = \
                        m.groupdict()['access_list']
                continue

            # Inbound Common access list is not set
            p9 = re.compile(r'^Inbound +Common +access +list +is +'
                             '(?P<access_list>[\w\s]+)$')
            m = p9.match(line)
            if m:
                if 'not set' not in m.groupdict()['access_list']:
                    interface_dict[interface]['inbound_common_access_list'] = \
                        m.groupdict()['access_list']
                continue

            # Inbound  access list is not set
            p10 = re.compile(r'^Outgoing +access +list +is +'
                             '(?P<access_list>[\w\s]+)$')
            m = p10.match(line)
            if m:
                if 'not set' not in m.groupdict()['access_list']:
                    interface_dict[interface]['inbound_access_list'] = \
                        m.groupdict()['access_list']
                continue

            # Proxy ARP is enabled
            p11 = re.compile(r'^Proxy +ARP +is +'
                             '(?P<status>\w+)$')
            m = p11.match(line)
            if m:
                if 'disabled' in m.groupdict()['status']:
                    interface_dict[interface]['proxy_arp'] = False
                else:
                    interface_dict[interface]['proxy_arp'] = True
                continue

            # Local Proxy ARP is disabled
            p12 = re.compile(r'^Local +Proxy +ARP +is +'
                             '(?P<status>\w+)$')
            m = p12.match(line)
            if m:
                if 'disabled' in m.groupdict()['status']:
                    interface_dict[interface]['local_proxy_arp'] = False
                else:
                    interface_dict[interface]['local_proxy_arp'] = True
                continue

            # Security level is default
            p13 = re.compile(r'^Security +level +is +'
                             '(?P<level>\w+)$')
            m = p13.match(line)
            if m:
                interface_dict[interface]['sevurity_level'] = m.groupdict()['level']
                continue

            # Split horizon is enabled
            p14 = re.compile(r'^Split +horizon +is +'
                             '(?P<status>\w+)$')
            m = p14.match(line)
            if m:
                if 'disabled' in m.groupdict()['status']:
                    interface_dict[interface]['split_horizon'] = False
                else:
                    interface_dict[interface]['split_horizon'] = True
                continue

            # ICMP redirects are always sent
            p15 = re.compile(r'^ICMP +redirects +are +'
                             '(?P<sent>[\w\s]+)$')
            m = p15.match(line)
            if m:
                if 'icmp' not in interface_dict[interface]:
                    interface_dict[interface]['icmp'] = {}
                if 'not set' not in m.groupdict()['sent']:
                    interface_dict[interface]['icmp']['redirects'] = \
                        m.groupdict()['sent']
                continue

            # ICMP unreachables are always sent
            p16 = re.compile(r'^ICMP +unreachables +are +'
                             '(?P<sent>[\w\s]+)$')
            m = p16.match(line)
            if m:
                if 'icmp' not in interface_dict[interface]:
                    interface_dict[interface]['icmp'] = {}
                if 'not set' not in m.groupdict()['sent']:
                    interface_dict[interface]['icmp']['unreachables'] = \
                        m.groupdict()['sent']
                continue

            # ICMP mask replies are never sent
            p17 = re.compile(r'^ICMP +mask +replies +are +'
                             '(?P<sent>[\w\s]+)$')
            m = p17.match(line)
            if m:
                if 'icmp' not in interface_dict[interface]:
                    interface_dict[interface]['icmp'] = {}
                if 'not set' not in m.groupdict()['sent']:
                    interface_dict[interface]['icmp']['mask_replies'] = \
                        m.groupdict()['sent']
                continue

            # IP fast switching is enabled
            p18 = re.compile(r'^IP +fast +switching +is +'
                             '(?P<status>\w+)$')
            m = p18.match(line)
            if m:
                if 'disabled' in m.groupdict()['status']:
                    interface_dict[interface]['ip_fast_switching'] = False
                else:
                    interface_dict[interface]['ip_fast_switching'] = True
                continue

            # IP Flow switching is disabled
            p19 = re.compile(r'^IP +Flow +switching +is +'
                             '(?P<status>\w+)$')
            m = p19.match(line)
            if m:
                if 'disabled' in m.groupdict()['status']:
                    interface_dict[interface]['ip_flow_switching'] = False
                else:
                    interface_dict[interface]['ip_flow_switching'] = True
                continue

            # IP CEF switching is enabled
            p20 = re.compile(r'^IP +CEF +switching +is +'
                             '(?P<status>\w+)$')
            m = p20.match(line)
            if m:
                if 'disabled' in m.groupdict()['status']:
                    interface_dict[interface]['ip_cef_switching'] = False
                else:
                    interface_dict[interface]['ip_cef_switching'] = True
                continue

            # IP CEF switching turbo vector
            p21 = re.compile(r'^IP +CEF +switching +turbo +vector$')
            m = p21.match(line)
            if m:
                interface_dict[interface]['ip_cef_switching_turbo_vector'] = True
                continue

            # IP Null turbo vector
            p22 = re.compile(r'^IP +Null +turbo +vector$')
            m = p22.match(line)
            if m:
                interface_dict[interface]['ip_null_turbo_vector'] = True
                continue

            # VPN Routing/Forwarding "Mgmt-vrf"
            p23 = re.compile(r'^VPN +Routing\/Forwarding +\"(?P<vrf>[\w\-]+)\"$')
            m = p23.match(line)
            if m:
                interface_dict[interface]['vrf'] = m.groupdict()['vrf']
                continue

            # Associated unicast routing topologies:
            #     Topology "base", operation state is UP
            p24 = re.compile(r'^Associated +unicast +routing +topologies:$')
            m = p24.match(line)
            if m:
                if 'unicast_routing_topologies' not in interface_dict[interface]:
                    interface_dict[interface]['unicast_routing_topologies'] = {}
                continue

            p24_1 = re.compile(r'^Topology +\"(?P<topo>\w+)\", +'
                                'operation +state +is +(?P<topo_status>\w+)$')
            m = p24_1.match(line)
            if m:
                if 'unicast_routing_topologies' in interface_dict[interface]:
                    if 'topology' not in interface_dict[interface]\
                      ['unicast_routing_topologies']:
                        interface_dict[interface]['unicast_routing_topologies']['topology'] = {}
                    topo = m.groupdict()['topo']
                    if topo not in interface_dict[interface]\
                      ['unicast_routing_topologies']['topology']:
                        interface_dict[interface]['unicast_routing_topologies']\
                            ['topology'][topo] = {}
                    interface_dict[interface]['unicast_routing_topologies']\
                        ['topology'][topo]['status'] = m.groupdict()['topo_status'].lower()
                continue

            # IP multicast fast switching is disabled
            p25 = re.compile(r'^IP +multicast +fast +switching +is +'
                             '(?P<status>\w+)$')
            m = p25.match(line)
            if m:
                if 'disabled' in m.groupdict()['status']:
                    interface_dict[interface]['ip_multicast_fast_switching'] = False
                else:
                    interface_dict[interface]['ip_multicast_fast_switching'] = True
                continue

            # IP multicast distributed fast switching is disabled
            p25 = re.compile(r'^IP +multicast +distributed +fast +switching +is +'
                             '(?P<status>\w+)$')
            m = p25.match(line)
            if m:
                if 'disabled' in m.groupdict()['status']:
                    interface_dict[interface]['ip_multicast_distributed_fast_switching'] = False
                else:
                    interface_dict[interface]['ip_multicast_distributed_fast_switching'] = True
                continue

            # IP route-cache flags are Fast, CEF
            p26 = re.compile(r'^IP +route\-cache +flags +are +(?P<flags>[\w\s\,]+)$')
            m = p26.match(line)
            if m:
                ret = m.groupdict()['flags'].split(',')
                ret = [i.strip() for i in ret]
                interface_dict[interface]['ip_route_cache_flags'] = sorted(ret)                    
                continue

            # Router Discovery is disabled
            p27 = re.compile(r'^Router +Discovery +is +'
                             '(?P<status>\w+)$')
            m = p27.match(line)
            if m:
                if 'disabled' in m.groupdict()['status']:
                    interface_dict[interface]['router_discovery'] = False
                else:
                    interface_dict[interface]['router_discovery'] = True
                continue

            # IP output packet accounting is disabled
            p28 = re.compile(r'^IP +output +packet +accounting +is +'
                             '(?P<status>\w+)$')
            m = p28.match(line)
            if m:
                if 'disabled' in m.groupdict()['status']:
                    interface_dict[interface]['ip_output_packet_accounting'] = False
                else:
                    interface_dict[interface]['ip_output_packet_accounting'] = True
                continue

            # IP access violation accounting is disabled
            p29 = re.compile(r'^IP +access +violation +accounting +is +'
                             '(?P<status>\w+)$')
            m = p29.match(line)
            if m:
                if 'disabled' in m.groupdict()['status']:
                    interface_dict[interface]['ip_access_violation_accounting'] = False
                else:
                    interface_dict[interface]['ip_access_violation_accounting'] = True
                continue

            # TCP/IP header compression is disabled
            p30 = re.compile(r'^TCP\/IP +header +compression +is +'
                             '(?P<status>\w+)$')
            m = p30.match(line)
            if m:
                if 'disabled' in m.groupdict()['status']:
                    interface_dict[interface]['tcp_ip_header_compression'] = False
                else:
                    interface_dict[interface]['tcp_ip_header_compression'] = True
                continue

            # RTP/IP header compression is disabled
            p31 = re.compile(r'^RTP\/IP +header +compression +is +'
                             '(?P<status>\w+)$')
            m = p31.match(line)
            if m:
                if 'disabled' in m.groupdict()['status']:
                    interface_dict[interface]['rtp_ip_header_compression'] = False
                else:
                    interface_dict[interface]['rtp_ip_header_compression'] = True
                continue

            # Probe proxy name replies are disabled
            p32 = re.compile(r'^Probe +proxy +name +replies +are +'
                             '(?P<status>\w+)$')
            m = p32.match(line)
            if m:
                if 'disabled' in m.groupdict()['status']:
                    interface_dict[interface]['probe_proxy_name_replies'] = False
                else:
                    interface_dict[interface]['probe_proxy_name_replies'] = True
                continue

            # Policy routing is disabled
            p33 = re.compile(r'^Policy +routing +is +'
                             '(?P<status>\w+)$')
            m = p33.match(line)
            if m:
                if 'disabled' in m.groupdict()['status']:
                    interface_dict[interface]['policy_routing'] = False
                else:
                    interface_dict[interface]['policy_routing'] = True
                continue

            # Network address translation is disabled
            p34 = re.compile(r'^Network +address +translation +is +'
                             '(?P<status>\w+)$')
            m = p34.match(line)
            if m:
                if 'disabled' in m.groupdict()['status']:
                    interface_dict[interface]['network_address_translation'] = False
                else:
                    interface_dict[interface]['network_address_translation'] = True
                continue

            # BGP Policy Mapping is disabled
            p35 = re.compile(r'^BGP +Policy +Mapping +is +'
                             '(?P<status>\w+)$')
            m = p35.match(line)
            if m:
                if 'disabled' in m.groupdict()['status']:
                    interface_dict[interface]['bgp_policy_mapping'] = False
                else:
                    interface_dict[interface]['bgp_policy_mapping'] = True
                continue

            # Input features: MCI Check
            # Input features: QoS Classification, QoS Marking, MCI Check
            p36 = re.compile(r'^Input +features: +(?P<input_feature>[\w\s\,]+)$')
            m = p36.match(line)
            if m:
                features = m.groupdict()['input_feature'].split(',')
                features = [i.strip() for i in features]
                interface_dict[interface]['input_features'] = sorted(features)
                continue

            # IPv4 WCCP Redirect outbound is disable
            p37 = re.compile(r'^IPv4 +WCCP +Redirect +outbound +is +(?P<status>\w+)$')
            m = p37.match(line)
            if m:
                if 'wccp' not in interface_dict[interface]:
                    interface_dict[interface]['wccp'] = {}
                if 'disabled' in m.groupdict()['status']:
                    interface_dict[interface]['wccp']\
                        ['redirect_outbound'] = False
                else:
                    interface_dict[interface]['wccp']\
                        ['redirect_outbound'] = True
                continue

            # IPv4 WCCP Redirect inbound is disabled
            p38 = re.compile(r'^IPv4 +WCCP +Redirect +inbound +is +(?P<status>\w+)$')
            m = p38.match(line)
            if m:
                if 'wccp' not in interface_dict[interface]:
                    interface_dict[interface]['wccp'] = {}
                if 'disabled' in m.groupdict()['status']:
                    interface_dict[interface]['wccp']\
                        ['redirect_inbound'] = False
                else:
                    interface_dict[interface]['wccp']\
                        ['redirect_inbound'] = True

            # IPv4 WCCP Redirect exclude is disabled
            p39 = re.compile(r'^IPv4 +WCCP +Redirect +exclude +is +(?P<status>\w+)$')
            m = p39.match(line)
            if m:
                if 'wccp' not in interface_dict[interface]:
                    interface_dict[interface]['wccp'] = {}
                if 'disabled' in m.groupdict()['status']:
                    interface_dict[interface]['wccp']\
                        ['redirect_exclude'] = False
                else:
                    interface_dict[interface]['wccp']\
                        ['redirect_exclude'] = True

            # Interface is unnumbered. Using address of Loopback11 (192.168.151.1)
            p40 = re.compile(r'^Interface +is +unnumbered. +Using +address +of +'
                              '(?P<unnumbered_intf>[\w\/\-\.]+) +'
                              '\((?P<unnumbered_ip>[\w\.\:]+)\)$')
            m = p40.match(line)
            if m:
                unnumbered_dict[interface] = {}
                unnumbered_intf = m.groupdict()['unnumbered_intf']
                unnumbered_ip = m.groupdict()['unnumbered_ip']
                unnumbered_dict[interface]['unnumbered_intf'] = unnumbered_intf
                unnumbered_dict[interface]['unnumbered_ip'] = unnumbered_ip

                if unnumbered_intf in interface_dict:
                    if 'ipv4' in interface_dict[unnumbered_intf]:
                        for address in interface_dict[unnumbered_intf]['ipv4']:
                            if unnumbered_ip in address:
                                ip_dict = interface_dict[interface].\
                                    setdefault('ipv4', {}).setdefault(address, {})
                                m = re.search('([\w\.\:]+)\/(\d+)', address)
                                ip_dict['ip'] = m.groups()[0]
                                ip_dict['prefix_length'] = m.groups()[1]
                                ip_dict['secondary'] = False
                                break
                else:
                    address = unnumbered_ip 
                    if 'ipv4' not in interface_dict[interface]:
                        interface_dict[interface]['ipv4'] = {}
                    if address not in interface_dict[interface]['ipv4']:
                        interface_dict[interface]['ipv4'][address] = {}
                    interface_dict[interface]['ipv4'][address]['ip'] = address
                continue

        return interface_dict



class ShowIpv6InterfaceSchema(MetaParser):
    """Schema for show ipv6 interface"""
    schema = {
                Any(): {
                    'oper_status': str,
                    'enabled': bool,
                    Optional('autoconf'): bool,
                    'ipv6': {
                        Any(): {
                            'ip': str,
                            Optional('prefix_length'): str,
                            Optional('status'): str,
                            Optional('origin'): str,
                            Optional('anycast'): bool,
                            Optional('eui_64'): bool,
                            Optional('virtual'): bool,
                            Optional('autoconf'): {
                                'valid_lifetime': int,
                                'preferred_lifetime': int,
                            },
                        },
                        'enabled': bool,
                        Optional('icmp'): {
                            Optional('error_messages_limited'): int,
                            Optional('redirects'): bool,
                            Optional('unreachables'): str,
                        },
                        Optional('nd'): {
                            Optional('dad_enabled'): bool,
                            Optional('dad_attempts'): int,
                            Optional('reachable_time'): int,
                            Optional('using_time'): int,
                            Optional('ns_retransmit_interval'): int,
                            Optional('advertised_reachable_time'): int,
                            Optional('advertised_retransmit_interval'): int,
                            Optional('router_advertisements_interval'): int,
                            Optional('router_advertisements_live'): int,
                            Optional('advertised_default_router_preference'): str, 
                            Optional('advertised_retransmit_interval_unspecified'): bool,
                            Optional('advertised_reachable_time_unspecified'): bool,
                        },
                        Optional('unnumbered'): {
                            'interface_ref': str,
                        },
                    },
                    Optional('mtu'): int,
                    Optional('vrf'): str,
                    Optional('addresses_config_method'): str,
                    Optional('joined_group_addresses'): list,
                },
            }

class ShowIpv6Interface(ShowIpv6InterfaceSchema):
    """Parser for show ipv6 interface"""
    cli_command = ['show ipv6 interface {interface}','show ipv6 interface']

    def cli(self, interface='',output=None):
        if output is None:
            if not interface:
                cmd = self.cli_command[1]
            else:
                cmd = self.cli_command[0].format(interface=interface)
            out = self.device.execute(cmd)
        else:
            out = output

        ret_dict = {}
        ipv6 = False
        joined_group = []
        # status code dict:
        status_code = {'ten': 'tentative',
                       'dep': 'duplicate',
                       'pre': 'preferre'}
        for line in out.splitlines():
            line = line.strip()

            # Vlan211 is up, line protocol is up
            # GigabitEthernet1/0/1 is administratively down, line protocol is down
            p1 =  re.compile(r'^(?P<interface>[\w\/\.\-]+) +is'
                              ' +(?P<enabled>[\w\s]+),'
                              ' +line +protocol +is +(?P<oper_status>\w+)$')
            m = p1.match(line)
            if m:
                intf = m.groupdict()['interface']
                enabled = m.groupdict()['enabled'].lower()
                if intf not in ret_dict:
                    ret_dict[intf] = {}
                if 'down' in enabled:
                    ret_dict[intf]['enabled'] = False
                else:
                    ret_dict[intf]['enabled'] = True

                ret_dict[intf]['oper_status'] = \
                    m.groupdict()['oper_status'].lower()

                # initial list variable again for new interface
                joined_group = []
                continue

            # IPv6 is enabled, link-local address is FE80::257:D2FF:FE28:
            # IPv6 is tentative, link-local address is FE80::257:D2FF:FE28:1A64 [TEN]
            # IPv6 is tentative, link-local address is FE80::257:D2FF:FE28:1A64 [UNA/TEN]
            p2 =  re.compile(r'^IPv6 +is +(?P<status>\w+), +'
                              'link-local +address +is +(?P<link_local>[\w\:]+)'
                              '( *\[(?P<type>[\w\/]+)\])?$')
            m = p2.match(line)
            if m:
                status = m.groupdict()['status']
                link_addr = m.groupdict()['link_local']

                if 'ipv6' not in ret_dict[intf]:
                    ret_dict[intf]['ipv6'] = {}

                if link_addr not in ret_dict[intf]['ipv6']:
                    ret_dict[intf]['ipv6'][link_addr] = {}

                ret_dict[intf]['ipv6'][link_addr]['ip'] = link_addr
                ret_dict[intf]['ipv6'][link_addr]['origin'] = 'link_layer'

                if status.lower() in ['preferred', 'deprecated', 'invalid',
                                      'inaccessible', 'unknown', 'tentative',
                                      'duplicate', 'optimistic']:
                    ret_dict[intf]['ipv6'][link_addr]['status'] = status.lower()
                else:
                    ret_dict[intf]['ipv6'][link_addr]['status'] = 'valid'
                continue

            # No Virtual link-local address(es):
            # Virtual link-local address(es):
            # FE80::5:73FF:FEA0:16 [UNA/OOD]
            p21 =  re.compile(r'^Virtual +link\-local +address\(es\)\:$')
            m = p21.match(line)
            if m:
                ipv6 = True
                continue

            p21_1 =  re.compile(r'^(?P<ipv6>[\w\:]+)'
                             '( *\[(?P<type>[\w\/]+)\])?$')
            m = p21_1.match(line)
            if m and ipv6:
                if 'ipv6' not in ret_dict[intf]:
                    ret_dict[intf]['ipv6'] = {}
                address = '{ip}'.format(ip=m.groupdict()['ipv6'])
                if address not in ret_dict[intf]['ipv6']:
                    ret_dict[intf]['ipv6'][address] = {}
                ret_dict[intf]['ipv6'][address]['ip'] = m.groupdict()['ipv6']
                ret_dict[intf]['ipv6'][address]['virtual'] = True

                ip_type = m.groupdict()['type']
                if ip_type and 'any' in ip_type.lower():
                    ret_dict[intf]['ipv6'][address]['anycast'] = True
                elif ip_type and 'eui' in ip_type.lower():
                    ret_dict[intf]['ipv6'][address]['eui_64'] = True
                elif ip_type:
                    for code in ip_type.lower().split('/'):
                        if code in status_code:
                            ret_dict[intf]['ipv6'][address]['status'] = status_code[code]
                        else:
                            ret_dict[intf]['ipv6'][address]['status'] = 'valid'
                continue

            # Stateless address autoconfig enabled
            p3 =  re.compile(r'^Stateless +address +autoconfig +enabled$')
            m = p3.match(line)
            if m:
                ret_dict[intf]['autoconf'] = True
                continue

            # Global unicast address(es):
            #   2001:10::14:1, subnet is 2001:10::14:0/112 
            #   2001:DB8:3:3::3, subnet is 2001:DB8:3:3::/64 [ANY/TEN]
            p4 =  re.compile(r'^Global +unicast +address\(es\):$')
            m = p4.match(line)
            if m:
                ipv6 = True
                continue

            p4_1 =  re.compile(r'^(?P<ipv6>[\w\:]+), +subnet +is +(?P<dum1>(?P<dum2>[\w\:]+)'
                             '\/(?P<prefix_length>[0-9]+))'
                             '( *\[(?P<type>[\w\/]+)\])?$')
            m = p4_1.match(line)
            if m and ipv6:
                if 'ipv6' not in ret_dict[intf]:
                    ret_dict[intf]['ipv6'] = {}
                address = '{ip}/{mask}'.format(ip=m.groupdict()['ipv6'],
                                               mask=m.groupdict()['prefix_length'])
                if address not in ret_dict[intf]['ipv6']:
                    ret_dict[intf]['ipv6'][address] = {}
                ret_dict[intf]['ipv6'][address]['ip'] = m.groupdict()['ipv6']

                ret_dict[intf]['ipv6'][address]['prefix_length'] = \
                    m.groupdict()['prefix_length']

                try:
                    status
                except Exception:
                    pass
                else:
                    if status.lower() in ['preferred', 'deprecated', 'invalid',
                                          'inaccessible', 'unknown', 'tentative',
                                          'duplicate', 'optimistic']:
                        ret_dict[intf]['ipv6'][address]['status'] = status.lower()
                    else:
                        ret_dict[intf]['ipv6'][address]['status'] = 'valid'
                    ret_dict[intf]['ipv6']['enabled'] = True

                ip_type = m.groupdict()['type']
                if ip_type and 'any' in ip_type.lower():
                    ret_dict[intf]['ipv6'][address]['anycast'] = True
                elif ip_type and 'eui' in ip_type.lower():
                    ret_dict[intf]['ipv6'][address]['eui_64'] = True
                elif ip_type:
                    for code in ip_type.lower().split('/'):
                        if code in status_code:
                            ret_dict[intf]['ipv6'][address]['status'] = status_code[code]
                        else:
                            ret_dict[intf]['ipv6'][address]['status'] = 'valid'
                continue

            #     valid lifetime 2591911 preferred lifetime 604711
            p4_2 =  re.compile(r'^valid +lifetime +(?P<valid>\d+) +'
                                'preferred +lifetime +(?P<preferred>\d+)$')
            m = p4_2.match(line)
            if m and ipv6:
                try:
                    address
                except Exception:
                    pass
                else:
                    if 'autoconf' not in ret_dict[intf]['ipv6'][address]:
                        ret_dict[intf]['ipv6'][address]['autoconf'] = {}
                    ret_dict[intf]['ipv6'][address]['autoconf']\
                        ['valid_lifetime'] = int(m.groupdict()['valid'])
                    ret_dict[intf]['ipv6'][address]['autoconf']\
                        ['preferred_lifetime'] = int(m.groupdict()['preferred'])
                continue

            # Joined group address(es):
            #   FF02::1
            #   FF02::1:FF14:1
            #   FF02::1:FF28:1A71
            p5 =  re.compile(r'^Joined +group +address\(es\):$')
            m = p5.match(line)
            if m:
                ipv6 = False
                continue

            p5_1 =  re.compile(r'^(?P<address>[\w\:]+)$')
            m = p5_1.match(line)
            if m and not ipv6:
                joined_group.append(m.groupdict()['address'])
                ret_dict[intf]['joined_group_addresses'] = sorted(joined_group)
                continue

            # MTU is 1500 bytes
            p6 =  re.compile(r'^MTU +is +(?P<mtu>\d+) +bytes$')
            m = p6.match(line)
            if m:
                ret_dict[intf]['mtu'] = int(m.groupdict()['mtu'])                    
                continue

            # VPN Routing/Forwarding "VRF1"
            p6 =  re.compile(r'^VPN +Routing\/Forwarding +\"(?P<vrf>[\w\-]+)\"$')
            m = p6.match(line)
            if m:
                ret_dict[intf]['vrf'] = m.groupdict()['vrf']
                continue

            # ICMP error messages limited to one every 100 milliseconds
            p7 =  re.compile(r'^ICMP +error +messages +limited +to +one +'
                              'every +(?P<limited>\d+) +milliseconds$')
            m = p7.match(line)
            if m:
                if 'ipv6' not in ret_dict[intf]:
                    ret_dict[intf]['ipv6'] = {}
                if 'icmp' not in ret_dict[intf]['ipv6']:
                    ret_dict[intf]['ipv6']['icmp'] = {}
                ret_dict[intf]['ipv6']['icmp']['error_messages_limited'] = \
                    int(m.groupdict()['limited'])                    
                continue

            # ICMP redirects are enabled
            p8 =  re.compile(r'^ICMP +redirects +are +(?P<status>\w+)$')
            m = p8.match(line)
            if m:
                if 'ipv6' not in ret_dict[intf]:
                    ret_dict[intf]['ipv6'] = {}
                if 'icmp' not in ret_dict[intf]['ipv6']:
                    ret_dict[intf]['ipv6']['icmp'] = {}
                if 'enabled' in m.groupdict()['status']:
                    ret_dict[intf]['ipv6']['icmp']['redirects'] = True
                else:
                    ret_dict[intf]['ipv6']['icmp']['redirects'] = False
                continue

            # ICMP unreachables are sent
            p9 =  re.compile(r'^ICMP +unreachables +are +(?P<status>[\w\s]+)$')
            m = p9.match(line)
            if m:
                if 'ipv6' not in ret_dict[intf]:
                    ret_dict[intf]['ipv6'] = {}
                if 'icmp' not in ret_dict[intf]['ipv6']:
                    ret_dict[intf]['ipv6']['icmp'] = {}
                if 'not sent' not in m.groupdict()['status']:
                    ret_dict[intf]['ipv6']['icmp']['unreachables'] = m.groupdict()['status']
                continue

            # ND DAD is enabled, number of DAD attempts: 1
            p10 =  re.compile(r'^ND +DAD +is +(?P<status>\w+), +'
                               'number +of +DAD +attempts: +(?P<attempts>\d+)$')
            m = p10.match(line)
            if m:
                if 'ipv6' not in ret_dict[intf]:
                    ret_dict[intf]['ipv6'] = {}
                if 'nd' not in ret_dict[intf]['ipv6']:
                    ret_dict[intf]['ipv6']['nd'] = {}
                if 'enabled' in m.groupdict()['status']:
                    ret_dict[intf]['ipv6']['nd']['dad_enabled'] = True
                else:
                    ret_dict[intf]['ipv6']['nd']['dad_enabled'] = False

                ret_dict[intf]['ipv6']['nd']['dad_attempts'] = int(m.groupdict()['attempts'])
                continue

            # ND reachable time is 30000 milliseconds (using 30000)
            p11 =  re.compile(r'^ND +reachable +time +is (?P<time>\d+) +milliseconds'
                               ' +\(using +(?P<use>\d+)\)$')
            m = p11.match(line)
            if m:
                if 'ipv6' not in ret_dict[intf]:
                    ret_dict[intf]['ipv6'] = {}
                if 'nd' not in ret_dict[intf]['ipv6']:
                    ret_dict[intf]['ipv6']['nd'] = {}
                ret_dict[intf]['ipv6']['nd']['reachable_time'] = int(m.groupdict()['time'])
                ret_dict[intf]['ipv6']['nd']['using_time'] = int(m.groupdict()['use'])
                continue

            # ND NS retransmit interval is 1000 milliseconds
            p12 =  re.compile(r'^ND +NS +retransmit +interval +is'
                               ' +(?P<interval>\d+) +milliseconds$')
            m = p12.match(line)
            if m:
                if 'ipv6' not in ret_dict[intf]:
                    ret_dict[intf]['ipv6'] = {}
                if 'nd' not in ret_dict[intf]['ipv6']:
                    ret_dict[intf]['ipv6']['nd'] = {}
                ret_dict[intf]['ipv6']['nd']['ns_retransmit_interval'] = \
                    int(m.groupdict()['interval'])
                continue

            # ND advertised reachable time is 0 (unspecified)
            p13 =  re.compile(r'^ND +advertised +reachable +time +is +(?P<time>\d+)'
                               ' +\((?P<dummy>\S+)\)$')
            m = p13.match(line)
            if m:
                if 'ipv6' not in ret_dict[intf]:
                    ret_dict[intf]['ipv6'] = {}
                if 'nd' not in ret_dict[intf]['ipv6']:
                    ret_dict[intf]['ipv6']['nd'] = {}
                ret_dict[intf]['ipv6']['nd']['advertised_reachable_time'] = \
                    int(m.groupdict()['time'])
                if m.groupdict()['dummy'] == 'unspecified':
                    ret_dict[intf]['ipv6']['nd']\
                        ['advertised_reachable_time_unspecified'] = True
                else:
                    ret_dict[intf]['ipv6']['nd']\
                        ['advertised_reachable_time_unspecified'] = False
                continue

            # ND advertised retransmit interval is 0 (unspecified)
            p14 =  re.compile(r'^ND +advertised +retransmit +interval +is +(?P<time>\d+)'
                               ' +\((?P<dummy>\S+)\)$')
            m = p14.match(line)
            if m:
                if 'ipv6' not in ret_dict[intf]:
                    ret_dict[intf]['ipv6'] = {}
                if 'nd' not in ret_dict[intf]['ipv6']:
                    ret_dict[intf]['ipv6']['nd'] = {}
                ret_dict[intf]['ipv6']['nd']['advertised_retransmit_interval'] = \
                    int(m.groupdict()['time'])
                if m.groupdict()['dummy'] == 'unspecified':
                    ret_dict[intf]['ipv6']['nd']\
                        ['advertised_retransmit_interval_unspecified'] = True
                else:
                    ret_dict[intf]['ipv6']['nd']\
                        ['advertised_retransmit_interval_unspecified'] = False
                continue

            # ND router advertisements are sent every 200 seconds
            p15 =  re.compile(r'^ND +router +advertisements +are +sent +'
                               'every +(?P<time>\d+) +seconds$')
            m = p15.match(line)
            if m:
                if 'ipv6' not in ret_dict[intf]:
                    ret_dict[intf]['ipv6'] = {}
                if 'nd' not in ret_dict[intf]['ipv6']:
                    ret_dict[intf]['ipv6']['nd'] = {}
                ret_dict[intf]['ipv6']['nd']['router_advertisements_interval'] = \
                    int(m.groupdict()['time'])
                continue

            # ND router advertisements live for 1800 seconds
            p16 =  re.compile(r'^ND +router +advertisements +live +for +'
                               '(?P<time>\d+) +seconds$')
            m = p16.match(line)
            if m:
                if 'ipv6' not in ret_dict[intf]:
                    ret_dict[intf]['ipv6'] = {}
                if 'nd' not in ret_dict[intf]['ipv6']:
                    ret_dict[intf]['ipv6']['nd'] = {}
                ret_dict[intf]['ipv6']['nd']['router_advertisements_live'] = \
                    int(m.groupdict()['time'])
                continue

            # ND advertised default router preference is Medium
            p17 =  re.compile(r'^ND +advertised +default +router +preference +'
                               'is +(?P<prefer>\w+)$')
            m = p17.match(line)
            if m:
                if 'ipv6' not in ret_dict[intf]:
                    ret_dict[intf]['ipv6'] = {}
                if 'nd' not in ret_dict[intf]['ipv6']:
                    ret_dict[intf]['ipv6']['nd'] = {}
                ret_dict[intf]['ipv6']['nd']['advertised_default_router_preference'] = \
                    m.groupdict()['prefer']
                continue

            # Hosts use stateless autoconfig for addresses.
            p18 =  re.compile(r'^Hosts +use +(?P<addr_conf_method>[\w\s]+) +for +addresses.$')
            m = p18.match(line)
            if m:
                ret_dict[intf]['addresses_config_method'] = \
                    m.groupdict()['addr_conf_method']
                continue

            # Interface is unnumbered. Using address of Loopback0
            p19 =  re.compile(r'^Interface +is +unnumbered. +Using +address +of'
                               ' +(?P<unnumbered_intf>[\w\/\.]+)$')
            m = p19.match(line)
            if m:
                if 'ipv6' not in ret_dict[intf]:
                    ret_dict[intf]['ipv6'] = {}
                if 'unnumbered' not in ret_dict[intf]['ipv6']:
                    ret_dict[intf]['ipv6']['unnumbered'] = {}
                ret_dict[intf]['ipv6']['unnumbered']['interface_ref'] = \
                    Common.convert_intf_name(m.groupdict()['unnumbered_intf'])
                continue

            # No global unicast address is configured
            p20 =  re.compile(r'^No +global +unicast +address +is +configured$')
            m = p20.match(line)
            if m:
                if 'ipv6' not in ret_dict[intf]:
                    ret_dict[intf]['ipv6'] = {}

                ret_dict[intf]['ipv6']['enabled'] = False
                continue
        return ret_dict


class ShowInterfacesTrunkSchema(MetaParser):
    """Schema for show interfaces trunk"""
    schema = {
        'interface': {
            Any(): {
                'name': str,
                'mode': str,
                'encapsulation': str,
                'status': str,
                'native_vlan': str,
                'vlans_allowed_on_trunk': str,
                'vlans_allowed_active_in_mgmt_domain': str,
                'vlans_in_stp_forwarding_not_pruned': str
            }
        }
    }

class ShowInterfacesTrunk(ShowInterfacesTrunkSchema):
    """parser for show interfaces trunk"""
    cli_command = 'show interfaces trunk'

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial regexp pattern
        p1 = re.compile(r'^(?P<name>[\w\-\/\.]+) +(?P<mode>\w+) +(?P<encapsulation>[\w\.]+) +'
                         '(?P<status>\w+) +(?P<native_vlan>\d+)$')
        p2 = re.compile('^Port +Vlans +allowed +on +trunk$')
        p3 = re.compile('^Port +Vlans +allowed +and +active +in +management +domain$')
        p4 = re.compile('^Port +Vlans +in +spanning +tree +forwarding +state +and +not +pruned$')
        p5 = re.compile('^(?P<name>[\w\-\/\.]+) +(?P<vlans>[\d\-\,\s]+)$')
        # initial variables
        ret_dict = {}
        vlan_list_type = None

        for line in out.splitlines():
            line = line.strip()

            # Gi1/0/4     on               802.1q         trunking      1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                intf = Common.convert_intf_name(group.pop('name'))
                intf_dict = ret_dict.setdefault('interface', {}).setdefault(intf, {})
                intf_dict['name'] = intf
                intf_dict.update({k:v for k,v in group.items()})
                continue

            # Port        Vlans allowed on trunk
            if p2.match(line):
                vlan_list_type = 'vlans_allowed_on_trunk'
                continue

            # Port        Vlans allowed and active in management domain
            if p3.match(line):
                vlan_list_type = 'vlans_allowed_active_in_mgmt_domain'
                continue

            # Port        Vlans in spanning tree forwarding state and not pruned
            if p4.match(line):
                vlan_list_type = 'vlans_in_stp_forwarding_not_pruned'
                continue

            # Gi1/0/4     200-211
            m = p5.match(line)
            if m:
                group = m.groupdict()
                intf = Common.convert_intf_name(group['name'])
                intf_dict = ret_dict.setdefault('interface', {}).setdefault(intf, {})
                intf_dict.setdefault(vlan_list_type, group['vlans']) if group['vlans'] else None
                continue
        return ret_dict


class ShowInterfacesCountersSchema(MetaParser):
    """Schema for show interfaces <WORD> counters"""
    schema = {
        'interface': {
            Any(): {
                Any(): {  # in or out
                    'octets': int,
                    'ucast_pkts': int,
                    'mcast_pkts': int,
                    'bcast_pkts': int,
                    'name': str
                },
            },
        }
    }

class ShowInterfacesCounters(ShowInterfacesCountersSchema):
    """parser for show interfaces <WORD> counters"""

    cli_command = 'show interfaces {interface} counters'

    def cli(self, interface,output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(interface=interface))
        else:
            out = output

        # initial regexp pattern
        p1 = re.compile(r'^(?P<name>[\w\-\/\.]+) +(?P<octets>\d+) +(?P<ucast_pkts>\d+) +'
                         '(?P<mcast_pkts>\d+) +(?P<bcast_pkts>\d+)$')
        p2 = re.compile(r'Port +InOctets +InUcastPkts +InMcastPkts +InBcastPkts')
        p2_1 = re.compile(r'Port +OutOctets +OutUcastPkts +OutMcastPkts +OutBcastPkts')

        # initial variables
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # decide the in or out packets
            if p2.match(line):
                in_out = 'in'
                continue

            if p2_1.match(line):
                in_out = 'out'
                continue

            # Gi1/0/4     on               802.1q         trunking      1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                intf = Common.convert_intf_name(group.pop('name'))
                intf_dict = ret_dict.setdefault('interface', {}).setdefault(intf, {}).setdefault(in_out, {})
                intf_dict['name'] = intf
                intf_dict.update({k:int(v) for k,v in group.items()})
                continue
        return ret_dict


class ShowInterfacesAccountingSchema(MetaParser):
    """Schema for show interfaces accounting"""
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
    cli_command = ['show interfaces {intf} accounting','show interfaces accounting']

    def cli(self, intf=None,output=None):
        if output is None:
            if not intf:
                cmd = self.cli_command[1]
            else:
                cmd = self.cli_command[0].format(intf=intf)
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return disctionary
        ret_dict = {}

        # initial regexp pattern
        # GigabitEthernet0/0/0/0
        p1 = re.compile(r'^(?P<interface>[a-zA-Z\-\d\/\.]+)$')

        # Tunnel0 Pim Register Tunnel (Encap) for RP 10.186.1.1
        p1_1 = re.compile(r'^(?P<interface>Tunnel\d+) +Pim +Register +'
                           'Tunnel +\(Encap\) +for +RP +(?P<rp>[\w\.]+)$')

        #   IPV4_UNICAST             9943           797492           50             3568
        p2 = re.compile(r'^(?P<protocol>[\w\_\-\s]+)\s+(?P<pkts_in>\d+)\s+'
                         '(?P<chars_in>\d+)\s+(?P<pkts_out>\d+)\s+'
                         '(?P<chars_out>\d+)')
        for line in out.splitlines():
            if line:
                line = line.strip()
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
                protocol = protocol_dict.pop('protocol').lower().strip()
                ret_dict.setdefault(intf, {}).\
                    setdefault('accounting', {}).setdefault(protocol, {})
                ret_dict[intf]['accounting'][protocol].update({k: int(v) \
                    for k, v in protocol_dict.items()})
                continue

        return ret_dict


# ====================================================
#  schema for show interfaces stats
# ====================================================
class ShowInterfacesStatsSchema(MetaParser):
    """Schema for:
        show interfaces <interface> stats
        show interfaces stats"""

    schema = {
        Any(): {
            'switching_path': {
                Any(): {
                    'pkts_in': int, 
                    'pkts_out': int, 
                    'chars_in': int, 
                    'chars_out': int, 
                },
            }
        },
    }


# ====================================================
#  parser for show interfaces stats
# ====================================================
class ShowInterfacesStats(ShowInterfacesStatsSchema):
    """Parser for :
        show interfaces <interface> stats
        show interfaces stats"""

    cli_command = ['show interfaces stats' ,'show interfaces {interface} stats']

    def cli(self, interface="", output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[1].format(interface=interface)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        # initialize result dict
        result_dict = {}
        
        # GigabitEthernet0/0/0
        p1 = re.compile(r'^\s*(?P<interface>[\w./]+)$')

        #    Switching path    Pkts In   Chars In   Pkts Out  Chars Out
        #         Processor         33       2507         33       2490
        p2 = re.compile(r'^\s*(?P<path>[\w\- ]*?) +(?P<pkts_in>[\d]+) +(?P<chars_in>[\d]+)'
                        ' +(?P<pkts_out>[\d]+) +(?P<chars_out>[\d]+)$')

        for line in out.splitlines():
            line = line.rstrip()

            m = p1.match(line)
            if m:
                interface = m.groupdict()['interface']
                path_dict = result_dict.setdefault(interface, {}).setdefault('switching_path', {})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                path = group.pop('path').replace(" ", "_").replace("-", "_").lower()
                tmp_dict = path_dict.setdefault(path, {})
                tmp_dict.update({k: int(v) for k, v in group.items()})
                continue

        return result_dict
