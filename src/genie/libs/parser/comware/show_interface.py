'''
Author: Renato Almeida de Oliveira
Contact: renato.almeida.oliveira@gmail.com
'''

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Optional
from genie.libs.parser.utils.common import Common
from genie import parsergen
from genie.libs.parser.iosxe.show_interface import ShowInterfacesSchema
import re

# ======================================================
# Schema for 'display ip interface'
# ======================================================


class DisplayInterfaceSchema(MetaParser):
    """schema for display interface
       display interface <interface>
    """
    schema = {
                Any(): {
                    'oper_status': str,
                    'enabled': bool,
                    Optional('description'): str,
                    'type': str,
                    Optional('frame_type'): str,
                    Optional('ipv6_frame_type'): str,
                    Optional('port_speed'): str,
                    Optional('duplex_mode'): str,
                    Optional('media_type'): str,
                    Optional('port_type'): str,
                    Optional('mtu'): int,
                    Optional('max_frame_length'): int,
                    Optional('pvid'): int,
                    Optional('mac_address'): str,
                    Optional('ipv6_mac_address'): str,
                    Optional('auto_negotiate'): bool,
                    Optional('priority'): int,
                    Optional('counters'):
                        {Optional('rate'):
                           {Optional('load_interval'): int,
                            Optional('in_rate_pkts'): int,
                            Optional('out_rate_pkts'): int,
                            Optional('in_rate_bytes'): int,
                            Optional('out_rate_bytes'): int,
                            },
                        Optional('normal'):
                           {Optional('in_pkts'): int,
                            Optional('in_octets'): int,
                            Optional('out_pkts'): int,
                            Optional('out_octets'): int,
                            Optional('in_unicast_pkts'): int,
                            Optional('in_broadcast_pkts'): int,
                            Optional('in_multicast_pkts'): int,
                            Optional('in_mac_pause_frames'): int,
                            Optional('out_unicast_pkts'): int,
                            Optional('out_broadcast_pkts'): int,
                            Optional('out_multicast_pkts'): int,
                            Optional('out_mac_pause_frames'): int,
                            },
                        Optional('out_unicast_pkts'): int,
                        Optional('out_errors'): int,
                        Optional('out_collision'): int,
                        Optional('out_lost_carrier'): int,
                        Optional('out_no_carrier'): int,
                        Optional('in_multicast_pkts'): int,
                        Optional('in_unicast_pkts'): int,
                        Optional('out_broadcast_pkts'): int,
                        Optional('out_abort'): int,
                        Optional('in_errors'): int,
                        Optional('in_parity_errors'): int,
                        Optional('in_ignored'): int,
                        Optional('in_throttles'): int,
                        Optional('in_overrun'): int,
                        Optional('out_mac_pause_frames'): int,
                        Optional('out_deferred'): int,
                        Optional('in_mac_pause_frames'): int,
                        Optional('out_octets'): int,
                        Optional('in_octets'): int,
                        Optional('in_runts'): int,
                        Optional('out_multicast_pkts'): int,
                        Optional('in_frame'): int,
                        Optional('in_broadcast_pkts'): int,
                        Optional('out_buffer_failure'): int,
                        Optional('out_pkts'): int,
                        Optional('out_late_collision'): int,
                        Optional('in_giants'): int,
                        Optional('out_underruns'): int,
                        Optional('in_crc_errors'): int,
                        Optional('in_abort'): int,
                        Optional('in_pkts'): int,
                        Optional('last_clear'): str,
                        },
                    Optional('switchport'): {
                        Optional('mode'): str,
                        Optional('tagged'): int,
                        Optional('untagged'): int,
                        Optional('vlan_passing'): list,
                        Optional('vlan_permitted'): list,
                        Optional('encapsulation'): str,
                    },
                    Optional('ipv4'):
                        {Any():
                            {Optional('ip'): str,
                             Optional('prefix_length'): str,
                             Optional('secondary'): bool
                        }
                    },
                }
    }


class DisplayInterfaces(DisplayInterfaceSchema):
    """parser for display interface
       display interface <interface>
    """
    ##########################################################
    #      Other Plataforms equivalent command
    ##########################################################
    platform_equivalent_cli = ['show interfaces',
                               'show interfaces {interface}']
    ##########################################################
    #      HP Comware command
    ##########################################################
    platform_cli = ['display interface',
                    'display interface {interface}']

    cli_command = platform_equivalent_cli + platform_cli

    exclude = []

    def cli(self, interface="", output=None):
        if output is None:
            if interface:
                cmd = self.platform_cli[1].format(interface=interface)
            else:
                cmd = self.platform_cli[0]
            out = self.device.execute(cmd)
        else:
            out = output

        # GigabitEthernet3/8/0/38 current state: DOWN
        p1 = re.compile(r'^ *(?P<interface>[\w\/\.\-]+) current state: (?P<enabled>[\(?\w\s\)?]+)$')

        # IP Packet Frame Type: PKTFMT_ETHNT_2, Hardware Address: aaaa-bbbb-cccc
        p2_0 = re.compile(r'^IP Packet Frame Type: (?P<frame_type>\w+), +Hardware Address: (?P<mac_address>[a-z0-9-]+)$')

        # IPv6 Packet Frame Type: PKTFMT_ETHNT_2, Hardware Address: aaaa-bbbb-cccc
        p2_1 = re.compile(r'^IPv6 Packet Frame Type: (?P<frame_type>\w+), +Hardware Address: (?P<mac_address>[a-z0-9-]+)$')

        # Description:
        p3 = re.compile(r'^Description: *(?P<description>.*)$')

        # Media type is twisted pair
        p4 = re.compile(r'^Media type is (?P<media_type>.*?)($|,.*$)')

        # Port hardware type is  1000_BASE_T
        p5 = re.compile(r'Port hardware type is\s+(?P<port_type>[\w+_?]+)')

        #  Unknown-speed mode, unknown-duplex mode
        p6 = re.compile(r'^(?P<port_speed>\w+[Mbps]?)-speed mode, (?P<duplex_mode>\w+)[\-\s]+[d|D]uplex mode$')

        # Link speed type is autonegotiation, link duplex type is autonegotiation
        p7 = re.compile(r'^Link speed type is (?P<speed_type>\w+), link duplex type is (?P<duplex_type>\w+)$')

        # The Maximum Frame Length is 9216
        p8_0 = re.compile(r'^The Maximum Frame Length is (?P<max_frame_length>\d+)$')
        p8_1 = re.compile(r'^The Maximum Transmit Unit is (?P<mtu>\d+)$')

        # Internet Address is 192.168.0.1/24 Primary
        p9 = re.compile(r'^Internet *Address *is *(?P<ipv4>(?P<ip>[0-9\.x]+)\/(?P<prefix_length>[0-9]+)) (?P<type>\w+)$')

        # PVID: 17
        p10 = re.compile(r'^PVID: *(?P<pvid>\d+)$')

        # Port link-type: access
        p11 = re.compile(r'^\s*Port link-type: (?P<switchport_mode>\w+)$')

        # Tagged   VLAN ID : none
        p12 = re.compile(r'^Tagged +VLAN ID : (?P<tagged>\w+)$')

        # Untagged VLAN ID : 123
        p13 = re.compile(r'^Untagged +VLAN ID : (?P<untagged>\w+)$')

        # VLAN passing  : 1(default vlan), 3, 5, 7, 9
        p14 = re.compile(r'^ *VLAN passing *: (?P<passing>(.*))$')

        # VLAN permitted  : 1(default vlan), 3, 5, 7, 9
        p15 = re.compile(r'^ *VLAN permitted *: (?P<permitted>(.*))$')

        # Trunk port encapsulation: IEEE 802.1q
        p16 = re.compile(r'^ *Trunk port encapsulation: (?P<encapsulation>.*)$')

        # Port priority: 0
        p17 = re.compile(r'^ *Port priority: (?P<priority>\d+)$')

        #  Last clearing of counters:  Never
        p18 = re.compile(r'^ *Last clearing of counters: *(?P<last_clear>.*)$')

        # Last 300 seconds input:  0 packets/sec 0 bytes/sec -%
        p19 = re.compile(r'Last (?P<load_interval>[0-9\#]+) *(?P<unit>(minute|second|minutes|seconds)) input: *(?P<in_rate_pkts>[0-9]+) packets\/sec *(?P<in_rate_bytes>[0-9]+) *bytes\/sec *.*%$')

        # Last 300 seconds output:  0 packets/sec 0 bytes/sec -%
        p20 = re.compile(r'Last (?P<load_interval>[0-9\#]+) *(?P<unit>(minute|second|minutes|seconds)) output: *(?P<out_rate_pkts>[0-9]+) packets\/sec *(?P<out_rate_bytes>[0-9]+) *bytes\/sec *.*%$')

        # Input (total):  7446905 packets, 10280397282 bytes
        p21_0 = re.compile(r'^ *Input \((?P<type>\w+)\): *(?P<packets>.*) packets, (?P<bytes>.*) bytes$')

        # Output (total): 40981139 packets, 44666966188 bytes
        p21_1 = re.compile(r'^ *Output \((?P<type>\w+)\): *(?P<packets>.*) packets, (?P<bytes>.*) bytes$')

        # 7426948 unicasts, 1093 broadcasts, 18864 multicasts, 0 pauses
        p22 = re.compile(r'^ *(?P<unicasts>.*) unicasts, (?P<broadcasts>.*) broadcasts, (?P<multicasts>.*) multicasts, (?P<pauses>.*) pauses$')

        # Input:  0 input errors, 0 runts, 0 giants, 0 throttles
        p23 = re.compile(r'^ *Input: *(?P<in_errors>.*) input errors, (?P<in_runts>.*) runts, (?P<in_giants>.*) giants, (?P<in_throttles>.*) throttles$')

        # 0 CRC, 0 frame, - overruns, 0 aborts
        p24 = re.compile(r'^ *(?P<in_crc_errors>.*) CRC, (?P<in_frame>.*) frame, (?P<in_overrun>.*) overruns, (?P<in_abort>.*) aborts$')

        #        - ignored, - parity errors
        p25 = re.compile(r'^ *(?P<in_ignored>.*) ignored, (?P<in_parity_errors>.*) parity errors$')

        # Output: 0 output errors, - underruns, - buffer failures
        p26 = re.compile(r'^ *Output: *(?P<out_errors>.*) output errors, (?P<out_underruns>.*) underruns, (?P<out_buffer_failure>.*) buffer failures$')

        #  aborts, 0 deferred, 0 collisions, 0 late collisions
        p27 = re.compile(r'^ *(?P<out_abort>.*) aborts, (?P<out_deferred>.*) deferred, (?P<out_collision>.*) collisions, (?P<out_late_collision>.*) late collisions$')

        #          0 lost carrier, - no carrier
        p28 = re.compile(r'^ *(?P<out_lost_carrier>.*) lost carrier, (?P<out_no_carrier>.*) no carrier$')

        interface_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # r'^ *(?P<interface>[\w\/\.\-]+) current state: (?P<enabled>[\(?\w\s\)?]+)$'
            m = p1.match(line)
            if m:
                interface = m.groupdict()['interface']
                if interface not in interface_dict:
                    interface_dict[interface] = {}
                p_type = re.compile(r'(?P<type>[a-zA-Z\-\s\+]+)')
                m_type = p_type.match(interface)
                if_type = m_type.groupdict()['type']
                interface_dict[interface]['type'] = if_type
                enabled = m.groupdict()['enabled']
                if 'DOWN ( Administratively )' in enabled:
                    interface_dict[interface]['enabled'] = False
                    interface_dict[interface]['oper_status'] = 'DOWN'
                else:
                    interface_dict[interface]['enabled'] = True
                    interface_dict[interface]['oper_status'] = enabled
                continue

            # r'^IP Packet Frame Type: (?P<frame_type>\w+), +Hardware Address: (?P<mac_address>[a-z0-9-]+)$'
            m = p2_0.match(line)
            if m:
                frame_type = m.groupdict()['frame_type']
                mac_address = m.groupdict()['mac_address']

                interface_dict[interface]['frame_type'] = frame_type
                interface_dict[interface]['mac_address'] = mac_address
                continue

            # r'^IPv6 Packet Frame Type: (?P<frame_type>\w+), +Hardware Address: (?P<mac_address>[a-z0-9-]+)$'
            m = p2_1.match(line)
            if m:
                frame_type = m.groupdict()['frame_type']
                mac_address = m.groupdict()['mac_address']

                interface_dict[interface]['ipv6_frame_type'] = frame_type
                interface_dict[interface]['ipv6_mac_address'] = mac_address
                continue

            # r'^Description: *(?P<description>.*)$'
            m = p3.match(line)
            if m:
                description = m.groupdict()['description']
                interface_dict[interface]['description'] = description
                continue

            # r'^Media type is (?P<media_type>.*?)($|,.*$)'
            m = p4.match(line)
            if m:
                media_type = m.groupdict()['media_type']
                interface_dict[interface]['media_type'] = media_type
                continue

            # r'Port hardware type is\s+(?<port_type>[\w+_?]+)'
            m = p5.match(line)
            if m:
                port_type = m.groupdict()['port_type']
                interface_dict[interface]['port_type'] = port_type
                continue

            # r'^(?<port_speed>\w+[Mbps]?)-speed mode, (?P<duplex_mode>\w+)[\-\s]+[d|D]uplex mode$'
            m = p6.match(line)
            if m:
                port_speed = m.groupdict()['port_speed'].lower()
                duplex_mode = m.groupdict()['duplex_mode'].lower()

                interface_dict[interface]['duplex_mode'] = duplex_mode
                interface_dict[interface]['port_speed'] = port_speed
                continue

            # r'^Link speed type is (?P<speed_type>\w+), link duplex type is (?P<duplex_type>\w+)$'
            m = p7.match(line)
            if m:
                speed_type = m.groupdict()['speed_type'].lower()
                duplex_type = m.groupdict()['duplex_type'].lower()

                if speed_type == 'autonegotiation' :
                    interface_dict[interface]['auto_negotiate'] = True
                else:
                    interface_dict[interface]['auto_negotiate'] = False
                continue

            # r'^The Maximum Frame Length is (?P<max_frame_length>\d+)$'
            m = p8_0.match(line)
            if m:
                max_frame_length = m.groupdict()['max_frame_length']
                interface_dict[interface]['max_frame_length'] = int(max_frame_length)
                continue

            # r'^The Maximum Transmit Unit is (?P<mtu>\d+)$'
            m = p8_1.match(line)
            if m:
                mtu = m.groupdict()['mtu']
                interface_dict[interface]['mtu'] = int(mtu)
                continue

            # ^Internet *Address *is *(?P<ipv4>(?P<ip>[0-9\.x]+)\/(?P<prefix_length>[0-9]+)) (?P<type>\w+)$
            m = p9.match(line)
            if m:
                ip_sec = m.groupdict()['ip']
                prefix_length_sec = m.groupdict()['prefix_length']
                address_sec = m.groupdict()['ipv4']
                address_type = m.groupdict()['type']
                if 'ipv4' not in interface_dict[interface]:
                    interface_dict[interface]['ipv4'] = {}
                if address_sec not in interface_dict[interface]['ipv4']:
                    interface_dict[interface]['ipv4'][address_sec] = {}
                if address_type != 'Primary':
                    interface_dict[interface]['ipv4'][address_sec]['secondary'] = True
                interface_dict[interface]['ipv4'][address_sec]['ip'] = ip_sec
                interface_dict[interface]['ipv4'][address_sec]['prefix_length'] = prefix_length_sec
                continue

            # r'^PVID: *(?P<pvid>\d+)$'
            m = p10.match(line)
            if m:
                pvid = m.groupdict()['pvid']
                interface_dict[interface]['pvid'] = int(pvid)
                continue

            # r'^\s*Port link-type: (?P<switchport_mode>\w+)$'
            m = p11.match(line)
            if m:
                switchport_mode = m.groupdict()['switchport_mode']
                if 'switchport' not in interface_dict[interface]:
                    interface_dict[interface]['switchport'] = {}
                interface_dict[interface]['switchport']['mode'] = switchport_mode
                continue

            # r'^Tagged +VLAN ID : (?P<tagged>\w+)$'
            m = p12.match(line)
            if m:
                tagged = m.groupdict()['tagged']
                if(tagged != 'none'):
                    interface_dict[interface]['switchport']['tagged'] = int(tagged)
                continue

            # r'^Untagged +VLAN ID : (?P<untagged>\w+)$'
            m = p13.match(line)
            if m:
                untagged = m.groupdict()['untagged']
                if(untagged != 'none'):
                    interface_dict[interface]['switchport']['untagged'] = int(untagged)
                continue

            # r'VLAN passing *: (?P<passing>(.*))'
            # VLAN passing  : 1(default vlan), 2-4, 9-11, 17-18, 20, 23, 28-36
            m = p14.match(line)
            if m:
                passing = m.groupdict()['passing']
                passing = passing.split(', ')
                vlans = []
                for vlan in passing:
                    if (re.search('default vlan', vlan)):
                        vlans.append(1)
                    elif (re.search('-', vlan)):
                        init = int(vlan.split('-')[0])
                        end = int(vlan.split('-')[1]) + 1
                        vlans.extend(list(range(init, end)))
                    else:
                        vlans.append(int(vlan))

                interface_dict[interface]['switchport']['vlan_passing'] = vlans
                continue

            # r'^ *VLAN permitted +: (?P<permitted>(.*))$'
            m = p15.match(line)
            if m:
                permitted = m.groupdict()['permitted']
                permitted = permitted.split(', ')
                vlans = []
                for vlan in permitted:
                    if (re.search('default vlan', vlan)):
                        vlans.append(1)
                    elif (re.search('-', vlan)):
                        init = int(vlan.split('-')[0])
                        end = int(vlan.split('-')[1]) + 1
                        vlans.extend(list(range(init, end)))
                    else:
                        vlans.append(int(vlan))

                interface_dict[interface]['switchport']['vlan_permitted'] = vlans
                continue

            # r'^ *Trunk port encapsulation: (?P<encapsulation>.*)$'
            m = p16.match(line)
            if m:
                encapsulation = m.groupdict()['encapsulation']
                interface_dict[interface]['switchport']['encapsulation'] = encapsulation
                continue

            # r'^ *Port priority: (?P<priority>\d+)$'
            m = p17.match(line)
            if m:
                priority = m.groupdict()['priority']
                interface_dict[interface]['priority'] = int(priority)
                continue

            # r'^ *Last clearing of counters: *(?P<last_clear>.*)$'
            m = p18.match(line)
            if m:
                last_clear = m.groupdict()['last_clear']
                if 'counters' not in interface_dict[interface]:
                    interface_dict[interface]['counters'] = {}
                interface_dict[interface]['counters']['last_clear'] = last_clear
                continue

            # r'Last (?P<load_interval>[0-9\#]+) *(?P<unit>(minute|second|minutes|seconds)) input: *(?P<in_rate_pkts>[0-9]+) packets\/sec *(?P<in_rate_bytes>[0-9]+) *bytes\/sec *.*%$'
            m = p19.match(line)
            if m:
                load_interval = m.groupdict()['load_interval']
                in_rate_pkts = m.groupdict()['in_rate_pkts']
                in_rate_bytes = m.groupdict()['in_rate_bytes']
                if 'counters' not in interface_dict[interface]:
                    interface_dict[interface]['counters'] = {}
                if 'rate' not in interface_dict[interface]['counters']:
                    interface_dict[interface]['counters']['rate'] = {}
                interface_dict[interface]['counters']['rate']['load_interval'] = int(load_interval)
                interface_dict[interface]['counters']['rate']['in_rate_pkts'] = int(in_rate_pkts)
                interface_dict[interface]['counters']['rate']['in_rate_bytes'] = int(in_rate_bytes)
                continue

            # r'Last (?P<load_interval>[0-9\#]+) *(?P<unit>(minute|second|minutes|seconds)) output: *(?P<out_rate_pkts>[0-9]+) packets\/sec *(?P<out_rate_bytes>[0-9]+) *bytes\/sec *.*%$'
            m = p20.match(line)
            if m:
                out_rate_pkts = m.groupdict()['out_rate_pkts']
                out_rate_bytes = m.groupdict()['out_rate_bytes']
                if 'counters' not in interface_dict[interface]:
                    interface_dict[interface]['counters'] = {}
                if 'rate' not in interface_dict[interface]['counters']:
                    interface_dict[interface]['counters']['rate'] = {}
                interface_dict[interface]['counters']['rate']['out_rate_pkts'] = int(out_rate_pkts)
                interface_dict[interface]['counters']['rate']['out_rate_bytes'] = int(out_rate_bytes)
                continue

            # r'^ *Input \((?P<type>\w+)\): *(?P<packets>.*) packets, (?P<bytes>.*) bytes$'
            m = p21_0.match(line)
            if m:
                inout = 'in'
                inout_type = m.groupdict()['type']

                packets = m.groupdict()['packets']
                octets = m.groupdict()['bytes']
                
                if(packets == '-'):
                    packets = 0
                if(octets == '-'):
                    octets = 0

                if 'counters' not in interface_dict[interface]:
                    interface_dict[interface]['counters'] = {}
                if inout_type == 'total':
                    interface_dict[interface]['counters'][inout + "_pkts"] = int(packets)
                    interface_dict[interface]['counters'][inout + "_octets"] = int(octets)
                elif inout_type == 'normal':
                    if 'normal' not in interface_dict[interface]['counters']:
                        interface_dict[interface]['counters']['normal'] = {}

                    interface_dict[interface]['counters']['normal'][inout + "_pkts"] = int(packets)
                    interface_dict[interface]['counters']['normal'][inout + "_octets"] = int(octets)

                continue

            # r'^ *Output \((?P<type>\w+)\): *(?P<packets>.*) packets, (?P<bytes>.*) bytes$'
            m = p21_1.match(line)
            if m:
                inout = 'out'
                inout_type = m.groupdict()['type']
                packets = m.groupdict()['packets']
                octets = m.groupdict()['bytes']

                if(packets == '-'):
                    packets = 0
                if(octets == '-'):
                    octets = 0

                if 'counters' not in interface_dict[interface]:
                    interface_dict[interface]['counters'] = {}
                if inout_type == 'total':
                    interface_dict[interface]['counters'][inout + "_pkts"] = int(packets)
                    interface_dict[interface]['counters'][inout + "_octets"] = int(octets)
                elif inout_type == 'normal':
                    if 'normal' not in interface_dict[interface]['counters']:
                        interface_dict[interface]['counters']['normal'] = {}

                    interface_dict[interface]['counters']['normal'][inout + "_pkts"] = int(packets)
                    interface_dict[interface]['counters']['normal'][inout + "_octets"] = int(octets)
                continue

            # r'^ *(?P<unicasts>.*) unicasts, (?P<broadcasts>.*) broadcasts, (?P<multicasts>.*) multicasts, (?P<pauses>.*) pauses$'
            m = p22.match(line)
            if m:
                unicasts = m.groupdict()['unicasts']
                broadcasts = m.groupdict()['broadcasts']
                multicasts = m.groupdict()['multicasts']
                pauses = m.groupdict()['pauses']

                if(unicasts == '-'):
                    unicasts = 0
                if(broadcasts == '-'):
                    broadcasts = 0
                if(multicasts == '-'):
                    multicasts = 0
                if(pauses == '-'):
                    pauses = 0

                if inout_type == 'total':
                    interface_dict[interface]['counters'][inout + "_unicast_pkts"] = int(unicasts)
                    interface_dict[interface]['counters'][inout + "_broadcast_pkts"] = int(broadcasts)
                    interface_dict[interface]['counters'][inout + "_multicast_pkts"] = int(multicasts)
                    interface_dict[interface]['counters'][inout + "_mac_pause_frames"] = int(pauses)
                elif inout_type == 'normal':
                    interface_dict[interface]['counters']['normal'][inout + "_unicast_pkts"] = int(unicasts)
                    interface_dict[interface]['counters']['normal'][inout + "_broadcast_pkts"] = int(broadcasts)
                    interface_dict[interface]['counters']['normal'][inout + "_multicast_pkts"] = int(multicasts)
                    interface_dict[interface]['counters']['normal'][inout + "_mac_pause_frames"] = int(pauses)
                continue

            # r'^ *Input: *(?P<in_errors>.*) input errors, (?P<in_runts>.*) runts, (?P<in_giants>.*) giants, (?P<in_throttles>.*) throttles$'
            m = p23.match(line)
            if m:
                in_errors = m.groupdict()['in_errors']
                in_runts = m.groupdict()['in_runts']
                in_giants = m.groupdict()['in_giants']
                in_throttles = m.groupdict()['in_throttles']

                if(in_errors == '-'):
                    in_errors = 0
                if(in_runts == '-'):
                    in_runts = 0
                if(in_giants == '-'):
                    in_giants = 0
                if(in_throttles == '-'):
                    in_throttles = 0

                interface_dict[interface]['counters']["in_errors"] = int(in_errors)
                interface_dict[interface]['counters']["in_runts"] = int(in_runts)
                interface_dict[interface]['counters']["in_giants"] = int(in_giants)
                interface_dict[interface]['counters']["in_throttles"] = int(in_throttles)
                continue

            # r'^ *(?P<in_crc_errors>.*) CRC, (?P<in_frame>.*) frame, (?P<in_overrun>.*) overruns, (?P<in_abort>.*) aborts$'
            m = p24.match(line)
            if m:
                in_crc_errors = m.groupdict()['in_crc_errors']
                in_frame = m.groupdict()['in_frame']
                in_overrun = m.groupdict()['in_overrun']
                in_abort = m.groupdict()['in_abort']

                if(in_crc_errors == '-'):
                    in_crc_errors = 0
                if(in_frame == '-'):
                    in_frame = 0
                if(in_overrun == '-'):
                    in_overrun = 0
                if(in_abort == '-'):
                    in_abort = 0

                interface_dict[interface]['counters']["in_crc_errors"] = int(in_crc_errors)
                interface_dict[interface]['counters']["in_frame"] = int(in_frame)
                interface_dict[interface]['counters']["in_overrun"] = int(in_overrun)
                interface_dict[interface]['counters']["in_abort"] = int(in_abort)
                continue

            # r'^ *(?P<in_ignored>.*) ignored, (?P<in_parity_errors>.*) parity errors$'
            m = p25.match(line)
            if m:
                in_ignored = m.groupdict()['in_ignored']
                in_parity_errors = m.groupdict()['in_parity_errors']

                if(in_ignored == '-'):
                    in_ignored = 0
                if(in_parity_errors == '-'):
                    in_parity_errors = 0

                interface_dict[interface]['counters']["in_ignored"] = int(in_ignored)
                interface_dict[interface]['counters']["in_parity_errors"] = int(in_parity_errors)
                continue

            # r'^ *Output: *(?P<out_errors>.*) output errors, (?P<out_underruns>.*) underruns, (?P<out_buffer_failure>.*) buffer failures$'
            m = p26.match(line)
            if m:
                out_errors = m.groupdict()['out_errors']
                out_underruns = m.groupdict()['out_underruns']
                out_buffer_failure = m.groupdict()['out_buffer_failure']

                if(out_errors == '-'):
                    out_errors = 0
                if(out_underruns == '-'):
                    out_underruns = 0
                if(out_buffer_failure == '-'):
                    out_buffer_failure = 0

                interface_dict[interface]['counters']["out_errors"] = int(out_errors)
                interface_dict[interface]['counters']["out_underruns"] = int(out_underruns)
                interface_dict[interface]['counters']["out_buffer_failure"] = int(out_buffer_failure)
                continue

            # ^ *(?P<out_abort>.*) aborts, (?P<out_deferred>.*) deferred, (?P<out_collision>.*) collisions, (?P<out_late_collision>.*) late collisions$
            m = p27.match(line)
            if m:
                out_abort = m.groupdict()['out_abort']
                out_deferred = m.groupdict()['out_deferred']
                out_collision = m.groupdict()['out_collision']
                out_late_collision = m.groupdict()['out_late_collision']

                if(out_abort == '-'):
                    out_abort = 0
                if(out_deferred == '-'):
                    out_deferred = 0
                if(out_collision == '-'):
                    out_collision = 0
                if(out_late_collision == '-'):
                    out_late_collision = 0

                interface_dict[interface]['counters']["out_abort"] = int(out_abort)
                interface_dict[interface]['counters']["out_deferred"] = int(out_deferred)
                interface_dict[interface]['counters']["out_collision"] = int(out_collision)
                interface_dict[interface]['counters']["out_late_collision"] = int(out_late_collision)
                continue

            # '^ *(?P<out_lost_carrier>.*) lost carrier, (?P<out_no_carrier>.*) no carrier$'
            m = p28.match(line)
            if m:
                out_lost_carrier = m.groupdict()['out_lost_carrier']
                out_no_carrier = m.groupdict()['out_no_carrier']

                if(out_lost_carrier == '-'):
                    out_lost_carrier = 0
                if(out_no_carrier == '-'):
                    out_no_carrier = 0

                interface_dict[interface]['counters']["out_lost_carrier"] = int(out_lost_carrier)
                interface_dict[interface]['counters']["out_no_carrier"] = int(out_no_carrier)
                continue

        return interface_dict


class DisplayIpInterfaceBriefSchema(MetaParser):
    """Parser for display ip interface brief"""
    schema = {
            Optional('route'):
            {
                Any():
                {
                    Optional('ip_address'): str,
                    Optional('link'): str,
                    Optional('protocol'): str,
                    Optional('description'): str
                }
            },
            Optional('bridge'):
            {
                Any():
                {
                    Optional('link'): str,
                    Optional('speed'): str,
                    Optional('duplex'): str,
                    Optional('type'): str,
                    Optional('pvid'): str,
                    Optional('description'): str
                }
            }
    }


class DisplayInterfacesBrief(DisplayIpInterfaceBriefSchema):
    """parser for display interface brief
    """
    ##########################################################
    #      Other Plataforms equivalent command
    ##########################################################
    platform_equivalent_cli = ['show interface brief']
    ##########################################################
    #      HP Comware command
    ##########################################################
    platform_cli = ['display interface brief']

    cli_command = platform_equivalent_cli + platform_cli

    def cli(self, output=None):

        route_dict = {}
        bridge_dict = {}
        parsed_dict = {}

        if output is None:
            cmd = self.platform_cli[0]

            out = self.device.execute(cmd)
        else:
            out = output

        route_out = ''
        bridge_out = ''
        table = ''

        if out:
            for line in out.splitlines():
                if re.search('under route', line):
                    table = 'route'
                if re.search('under bridge', line):
                    table = 'bridge'
                if table == 'route':
                    route_out = route_out + line + "\n"
                elif table == 'bridge':
                    bridge_out = bridge_out + line + "\n"

            if (route_out != ''):
                res = parsergen.oper_fill_tabular(device_output=route_out,
                                                  device_os='hp_comware',
                                                  table_terminal_pattern=r"^\n",
                                                  header_fields=['Interface',
                                                                 'Link',
                                                                 'Protocol',
                                                                 'Main IP',
                                                                 'Description'],
                                                  label_fields=['Interface',
                                                                'link',
                                                                'protocol',
                                                                'ip_address',
                                                                'description'],
                                                  index=[0])
                if res.entries:
                    for intf, intf_dict in res.entries.items():
                        intf = Common.convert_intf_name(intf)
                        del intf_dict['Interface']
                        route_dict.setdefault('route', {}).update({intf: intf_dict})
            if (bridge_out != ''):
                res = parsergen.oper_fill_tabular(device_output=bridge_out,
                                                  device_os='hp_comware',
                                                  table_terminal_pattern=r"^\n",
                                                  header_fields=['Interface',
                                                                 'Link',
                                                                 'Speed',
                                                                 'Duplex',
                                                                 'Type',
                                                                 'PVID',
                                                                 'Description'],
                                                  label_fields=['Interface',
                                                                'link',
                                                                'speed',
                                                                'duplex',
                                                                'type',
                                                                'pvid',
                                                                'description'],
                                                  index=[0])
                if res.entries:
                    for intf, intf_dict in res.entries.items():
                        intf = Common.convert_intf_name(intf)
                        del intf_dict['Interface']
                        bridge_dict.setdefault('bridge', {}).update({intf: intf_dict})

            if(route_dict != {}):
                parsed_dict.update(route_dict)
            if(bridge_dict != {}):
                parsed_dict.update(bridge_dict)

        return parsed_dict

