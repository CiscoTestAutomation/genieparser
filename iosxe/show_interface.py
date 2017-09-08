''' show_interface.py

Example parser class

'''

import os
import logging
import pprint
import re
import unittest
from collections import defaultdict

from ats.log.utils import banner
import xmltodict
try:
    import iptools
    from ats import tcl
    import parsergen
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
        if re.match(expression, value):
            return value
        else:
            raise TypeError("Value '%s' doesnt match regex '%s'"
                            % (value, expression))
    return match

def convert_intf_name(intf):
    # Please add more when face other type of interface
    convert = {'Eth': 'Ethernet',
               'Lo': 'Loopback',
               'Po': 'Port-channel',
               'Null': 'Null',
               'Gi': 'GigabitEthernet',
               'Te': 'TenGigabitEthernet',
               'mgmt': 'mgmt'}
    int_type = re.search('([a-zA-Z]+)', intf).group(0)
    int_port = re.search('([\d\/\.]+)', intf).group(0)
    if int_type in convert.keys():
        return(convert[int_type] + int_port)
    else:
        return(intf)


class ShowInterfacesSchema(MetaParser):

    #schema for show interfaces

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
                    Optional('in_pause_input'): int,
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
                    Optional('out_pause_output'): int,
                    Optional('out_buffer_failure'): int,
                    Optional('out_buffers_swapped'): int,
                    Optional('last_clear'): str,
                    },
                Optional('encapsulations'):
                    {Optional('encapsulation'): str,
                     Optional('first_dot1q'): str,
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

    #parser for show interfaces

    def cli(self):
        out = self.device.execute('show interfaces')
        interface_dict = {}
        unnumbered_dict = {}
        for line in out.splitlines():
            line = line.strip()

            # GigabitEthernet1 is up, line protocol is up 
            # Port-channel12 is up, line protocol is up (connected)
            p1 =  re.compile(r'^(?P<interface>[\w\/\.\-]+) +is'
                              ' +(?P<enabled>[\w\s]+),'
                              ' +line +protocol +is +(?P<line_protocol>\w+)'
                              '( *\((?P<attribute>\S+)\))?$')
            m = p1.match(line)
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

                if enabled and 'down' in enabled:
                    interface_dict[interface]['enabled'] = False
                elif enabled and 'up' in enabled:
                    interface_dict[interface]['enabled'] = True

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
            p2 = re.compile(r'^Hardware +is +(?P<type>[a-zA-Z0-9\/\s]+)'
                            '(, *address +is +(?P<mac_address>[a-z0-9\.]+)'
                            ' *\(bia *(?P<phys_address>[a-z0-9\.]+)\))?$')
            m = p2.match(line)
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
            p3 = re.compile(r'^Description: *(?P<description>\S+)$')
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
            p6 = re.compile(r'^MTU +(?P<mtu>[0-9]+) +bytes, +BW'
                             ' +(?P<bandwidth>[0-9]+) +Kbit/sec, +DLY'
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
            p8 = re.compile(r'^Encapsulation +(?P<encapsulation>\w+),'
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
                m1 = re.compile(r'(Vlan +ID +(?P<first_dot1q>[0-9]+),)?'
                                 ' *medium +is +(?P<medium>[a-z0-9]+)$').match(rest)
                # will update key when output is valid
                m2 = re.compile(r'loopback +(?P<loopback>[\w\s]+)$').match(rest)
                if m1:
                    first_dot1q = m1.groupdict()['first_dot1q']
                    if first_dot1q:
                        interface_dict[interface]['encapsulations']\
                            ['first_dot1q'] = first_dot1q
                        interface_dict[interface]['medium'] = medium
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
            p11 = re.compile(r'^(?P<duplex_mode>\w+)[\-\s]+[d|D]uplex, +'
                              '(?P<port_speed>[0-9]+)(?: *Mb/s)?,'
                              '( *link +type +is +(?P<link_type>\w+),)?'
                              ' *media +type +is *(?P<media_type>[\w\/]+)?$')
            m = p11.match(line)
            if m:
                duplex_mode = m.groupdict()['duplex_mode'].lower()
                port_speed = m.groupdict()['port_speed']
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
            p15 = re.compile(r'^Members +in +this +channel: +(?P<port_channel_member_intfs>[\w\/\.]+)$')
            m = p15.match(line)
            if m:
                # will check with Takashi about the keys.
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
                    except:
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
                interface_dict[interface]['counters']['in_pause_input'] = \
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
                interface_dict[interface]['counters']['out_pause_output'] = \
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

            # Interface is unnumbered. Using address of Loopback0 (1.1.1.1)
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

        res = parsergen.oper_fill_tabular(device=self.device,
                                          show_command=self.cmd,
                                          header_fields=
                                           [ "Interface",
                                             "IP-Address",
                                             "OK\?",
                                             "Method",
                                             "Status",
                                             "Protocol" ],
                                          label_fields=
                                           [ "Interface",
                                             "IP-Address",
                                             "OK?",
                                             "Method",
                                             "Status",
                                             "Protocol" ],
                                          index=[0])
        return (res)

    def yang(self):
        ''' parsing mechanism: yang

        Function yang() defines the yang type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        pass

    def yang_cli(self):
        cli_output = self.cli()
        yang_output = self.yang()
        merged_output = _merge_dict(yang_output,cli_output)
        return merged_output

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

    def cli(self):
        super(ShowIpInterfaceBriefPipeVlan, self).cli()

    def yang(self):
        ''' parsing mechanism: yang

        Function yang() defines the yang type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''

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

