"""
    show_interface.py
    IOSXE parsers for the following show commands:

    * show interfaces
    * show ip interfaces <interface>
    * show ip interface brief
    * show ip interface brief | include Vlan
    * show interfaces switchport
    * show interfaces {interface} switchport
    * show ip interface
    * show interfaces <interface>
    * show ipv6 interface
    * show interfaces accounting
    * show interfaces link
    * show interfaces {interface} link
    * show interfaces status
    * show interfaces {interface} status
    * show interfaces transceiver
    * show interfaces {interface} transceiver
    * show interfaces transceiver detail
    * show interfaces {interface} transceiver detail
    * show macro auto interface
    * show interfaces summary
    * show interfaces {interface} summary
    * show interfaces mtu
    * show interfaces {interface} mtu
    * show interfaces mtu module {mod}
    * show interfaces status module {mod}
    * show pm vp interface {interface} {vlan}
    * show pm port interface {interface}
    * show interfaces transceiver supported-list
    * show interfaces capabilities
    * show interfaces {interface} capabilities
    * show interfaces {interface} vlan mapping
    * show interfaces {interface} human-readable
    * show interfaces transceiver module {mod}
"""

import os
import logging
import pprint
import re
import unittest
from genie import parsergen
from collections import defaultdict

from pyats.log.utils import banner
import xmltodict
try:
    import iptools
    from cnetconf import testmodel
except (ImportError, OSError):
    pass

try:
    from pyats import tcl
except Exception:
    pass

from genie.metaparser import MetaParser
from genie.metaparser.util import merge_dict, keynames_convert
from genie.metaparser.util.exceptions import SchemaEmptyParserError
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
                Optional('oper_status'): str,
                Optional('line_protocol'): str,
                Optional('enabled'): bool,
                Optional('is_deleted'): bool,
                Optional('is_present'): bool,
                Optional('connected'): bool,
                Optional('err_disabled'): bool,
                Optional('suspended'): bool,
                Optional('description'): str,
                Optional('type'): str,
                Optional('link_state'): str,
                Optional('port_speed'): str,
                Optional('duplex_mode'): str,
                Optional('link_type'): str,
                Optional('media_type'): str,
                Optional('mtu'): int,
                Optional('maximum_active_vcs'): str,
                Optional('vcs_per_vp'): str,
                Optional('vc_idle_disconnect_time'): str,
                Optional('vc_auto_creation'): str,
                Optional('current_vccs'): str,
                Optional('aal5_crc_errors'): int,
                Optional('aal5_oversized_sdus'): int,
                Optional('aal5_sar_timeouts'): int,
                Optional('vaccess_status'): str,
                Optional('vaccess_loopback'): str,
                Optional('base_pppoatm'): str,
                Optional('dtr_pulsed'): str,
                Optional('sub_mtu'): int,
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
                Optional('autostate'): bool,
                Optional('tunnel_source_ip'): str,
                Optional('tunnel_source_interface'): str,
                Optional('tunnel_destination_ip'): str,
                Optional('tunnel_protocol'): str,
                Optional('tunnel_ttl'): int,
                Optional('tunnel_transport_mtu'): int,
                Optional('tunnel_transmit_bandwidth'): int,
                Optional('tunnel_receive_bandwidth'): int,
                Optional('tunnel_protection'): str,
                Optional('tunnel_profile'): str,
                Optional('carrier_transitions'): int,
                Optional('queues'): {
                    Optional('input_queue_size'): int,
                    Optional('input_queue_max'): int,
                    Optional('input_queue_drops'): int,
                    Optional('input_queue_flushes'): int,
                    Optional('total_output_drop'): int,
                    Optional('queue_strategy'): str,
                    Optional('output_queue_size'): int,
                    Optional('output_queue_max'): int,
                    Optional('threshold'): int,
                    Optional('drops'): int,
                },
                Optional('flow_control'):
                    {Optional('receive'): bool,
                    Optional('send'): bool,
                },
                Optional('port_channel'):
                    {Optional('port_channel_member'): bool,
                    Optional('port_channel_int'): str,
                    Optional('port_channel_member_intfs'): list,
                    Optional('active_members'): int,
                    Optional('num_of_pf_jumbo_supported_members'): int,
                },
                Optional('bandwidth'): Or(int, str),
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
                    Optional('in_drops'): int,
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
                    Optional('out_drops'): int,
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
            Optional('peer_ip'): str,
            Optional('vc_id'): int
        },
    }


class ShowInterfaces(ShowInterfacesSchema):
    """parser for show interfaces
                  show interfaces <interface>"""

    cli_command = [
        'show interfaces',
        'show interfaces {interface}',
        'show interfaces | include {include}',
        ]
    exclude = ['in_octets', 'in_pkts', 'out_octets', 'out_pkts',
               'in_rate', 'in_rate_pkts', 'out_rate', 'out_rate_pkts',
               'input_queue_size', 'in_broadcast_pkts', 'in_multicast_pkts',
               'last_output', 'out_unknown_protocl_drops', 'last_input',
               'input_queue_drops', 'out_interface_resets', 'rxload',
               'txload', 'last_clear', 'in_crc_errors', 'in_errors',
               'in_giants', 'unnumbered', 'mac_address', 'phys_address',
               'out_lost_carrier', '(Tunnel.*)', 'input_queue_flushes',
               'reliability', 'out_broadcast_pkts']

    def cli(self, interface="", include="", output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[1].format(interface=interface)
            elif include:
                cmd = self.cli_command[2].format(include=include)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        # GigabitEthernet1 is up, line protocol is up
        # Port-channel12 is up, line protocol is up (connected)
        # Vlan1 is administratively down, line protocol is down , Autostate Enabled
        # Dialer1 is up (spoofing), line protocol is up (spoofing)
        # FastEthernet1 is down, line protocol is down (err-disabled)
        # GigabitEthernet1/0/2 is up, line protocol is down (suspended)

        p1 = re.compile(r'^(?P<interface>[\w\/\.\-\:]+) +is +(?P<enabled>[\w\s]+)(?: '
                        r'+\S+)?, +line +protocol +is +(?P<line_protocol>\w+)(?: '
                        r'*\((?P<attribute>\S+)\)|( +\, +Autostate +(?P<autostate>\S+)))?.*$')
        p1_1 = re.compile(r'^(?P<interface>[\w\/\.\-\:]+) +is'
                          r' +(?P<enabled>[\w\s]+),'
                          r' +line +protocol +is +(?P<line_protocol>\w+)'
                          r'( *, *(?P<attribute>[\w\s]+))?$')

        # pseudowire1 is up
        p1_2 = re.compile(r'^(?P<interface>pseudowire\d+) +is +(?P<enabled>\w+)$')

        # Hardware is Gigabit Ethernet, address is 0057.d2ff.428c (bia 0057.d2ff.428c)
        # Hardware is Loopback
        p2 = re.compile(r'^Hardware +is +(?P<type>[a-zA-Z0-9\-\/\s\+]+)'
                        r'(, *address +is +(?P<mac_address>[a-z0-9\.]+)'
                        r' *\(bia *(?P<phys_address>[a-z0-9\.]+)\))?$')

        # Hardware is LTE Adv CAT6 - Multimode LTE/DC-HSPA+/HSPA+/HSPA/UMTS/EDGE/GPRS
        # Hardware is BUILT-IN-4x2_5GE, address is 8c1e.8068.9f6c (bia 8c1e.8068.9f6c)
        p2_2 = re.compile(r'Hardware +is +(?P<type>[a-zA-Z0-9\-\/\\_+ ]+)(, +address +is +(?P<mac_address>[a-f0-9\.]+)( +\(bia +(?P<phys_address>.*)\))?)?')

        # Hardware is not present
        p2_3 = re.compile(r'^Hardware +is +not +present$')

        # Hardware is not present
        p2_3 = re.compile(r'^Hardware +is +not +present$')

        # Description: desc
        # Description: Pim Register Tunnel (Encap) for RP 10.186.1.1
        p3 = re.compile(r'^Description: *(?P<description>.*)$')

        # Secondary address 10.2.2.2/24
        p4 = re.compile(r'^Secondary +Address +is +(?P<ipv4>(?P<ip>[0-9\.]+)'
                        r'\/(?P<prefix_length>[0-9]+))$')

        # Internet address is 10.4.4.4/24
        p5 = re.compile(r'^Internet +[A|a]ddress +is +(?P<ipv4>(?P<ip>[0-9\.x]+)'
                        r'\/(?P<prefix_length>[0-9]+))$')

        # MTU 1500 bytes, BW 768 Kbit/sec, DLY 3330 usec,
        # MTU 1500 bytes, BW 10000 Kbit, DLY 1000 usec,
        # MTU 1600 bytes, sub MTU 1600, BW 3584 Kbit/sec, DLY 410 usec,
        # MTU 1500 bytes, BW 5200 Kbit/sec, RxBW 25000 Kbit/sec, DLY 100 usec,
        p6 = re.compile(r'^MTU +(?P<mtu>\d+) +bytes(, +sub +MTU +'
                        r'(?P<sub_mtu>\d+))?, +BW +(?P<bandwidth>[0-9]+) +Kbit(\/sec)?'
                        r'(, +RxBW +[0-9]+ +Kbit(\/sec)?)?, +'
                        r'DLY +(?P<delay>[0-9]+) +usec,$')

        # MTU 9198 bytes, BW not configured
        p6_1 = re.compile(r'^MTU +(?P<mtu>\d+) +bytes, +BW +(?P<bandwidth>[\w\s]+)$')

        # reliability 255/255, txload 1/255, rxload 1/255
        p7 = re.compile(r'^reliability +(?P<reliability>[\d\/]+),'
                        r' +txload +(?P<txload>[\d\/]+), +rxload'
                        r' +(?P<rxload>[\d\/]+)$')

        # Encapsulation LOOPBACK, loopback not set
        # Encapsulation 802.1Q Virtual LAN, Vlan ID 20, medium is p2p
        # Encapsulation ARPA, medium is broadcast
        # Encapsulation QinQ Virtual LAN, outer ID  10, inner ID 20
        # Encapsulation 802.1Q Virtual LAN, Vlan ID  1., loopback not set
        # Encapsulation 802.1Q Virtual LAN, Vlan ID  105.
        # Encapsulation(s): AAL5
        p8 = re.compile(r'^Encapsulation(\(s\):)? +(?P<encapsulation>[\w\s\.]+)'
                        r'(, +(?P<rest>.*))?$')

        # Keepalive set (10 sec)
        p10 = re.compile(r'^Keepalive +set +\((?P<keepalive>[0-9]+)'
                         r' +sec\)$')

        # Auto-duplex, 1000Mb/s, media type is 10/100/1000BaseTX
        # Full-duplex, 1000Mb/s, link type is auto, media type is
        # Full Duplex, 1000Mbps, link type is auto, media type is RJ45
        # Full Duplex, Auto Speed, link type is auto, media type is RJ45
        # Full Duplex, 10000Mbps, link type is force-up, media type is unknown media type
        # full-duplex, 1000 Mb/s
        # auto-duplex, auto-speed
        # auto-duplex, 10 Gb/s, media type is 10G
        # Full Duplex, 10000Mbps, link type is force-up, media type is SFP-LR
        # Full-duplex, 100Gb/s, link type is force-up, media type is QSFP 100G SR4
        # Full-duplex, 10Gb/s, media type is 100/1000/2.5G/5G/10GBaseTX
        # Full-duplex, 10Gb/s, link type is auto, media type is CVR QSFP SFP10G(SFP-10GBase-SR)
        p11 = re.compile(r'^(?P<duplex_mode>\w+)[\-\s]+[d|D]uplex\, '
                         r'+(?P<port_speed>[\w\s\/]+|[a|A]uto-[S|s]peed|Auto '
                         r'(S|s)peed)(?:(?:\, +link +type +is '
                         r'+(?P<link_type>\S+))?(?:\, *(media +type +is| )'
                         r'*(?P<media_type>[\w\/\-\.() ]+)?)(?: +media +type)?)?$')

        # input flow-control is off, output flow-control is unsupported
        p12 = re.compile(r'^(?P<first>input|output) +flow-control +is +(?P<receive>\w+), +'
                         r'(?P<second>output|input) +flow-control +is +(?P<send>\w+)$')

        # ARP type: ARPA, ARP Timeout 04:00:00
        p13 = re.compile(r'^ARP +type: +(?P<arp_type>\w+), +'
                         r'ARP +Timeout +(?P<arp_timeout>[\w\:\.]+)$')

        # Last input never, output 00:01:05, output hang never
        p14 = re.compile(r'^Last +input +(?P<last_input>[\w\.\:]+), +'
                         r'output +(?P<last_output>[\w\.\:]+), '
                         r'output +hang +(?P<output_hang>[\w\.\:]+)$')

        # Members in this channel: Gi1/0/2
        # Members in this channel: Fo1/0/2 Fo1/0/4
        p15 = re.compile(r'^Members +in +this +channel: +'
                         r'(?P<port_channel_member_intfs>[\w\/\.\s\,]+)$')

        # No. of active members in this channel: 12
        p15_1 = re.compile(r'^No\. +of +active +members +in +this +'
                           r'channel: +(?P<active_members>\d+)$')

        # Member 2 : GigabitEthernet0/0/10 , Full-duplex, 900Mb/s
        p15_2 = re.compile(r'^Member +\d+ +: +(?P<interface>\S+) +,'
                           r' +\S+, +\S+$')

        # No. of PF_JUMBO supported members in this channel : 0
        p15_3 = re.compile(r'^No\. +of +PF_JUMBO +supported +members +'
                           r'in +this +channel +: +(?P<number>\d+)$')

        # Last clearing of "show interface" counters 1d02h
        p16 = re.compile(r'^Last +clearing +of +\"show +interface\" +counters +'
                         r'(?P<last_clear>[\w\:\.]+)$')

        # Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
        p17 = re.compile(r'^Input +queue: +(?P<size>\d+)\/(?P<max>\d+)\/'
                         r'(?P<drops>\d+)\/(?P<flushes>\d+) +'
                         r'\(size\/max\/drops\/flushes\); +'
                         r'Total +output +drops: +(?P<output_drop>\d+)$')

        # Queueing strategy: fifo
        # Queueing strategy: Class-based queueing
        p18 = re.compile(r'^Queueing +strategy: +(?P<queue_strategy>\S+).*$')

        # Output queue: 0/0 (size/max)
        # Output queue: 0/1000/64/0 (size/max total/threshold/drops)
        p19 = re.compile(r'^Output +queue: +(?P<size>\d+)\/(?P<max>\d+)'
                         r'(?:\/(?P<threshold>\d+)\/(?P<drops>\d+))? '
                         r'+\(size\/max(?: +total\/threshold\/drops\))?.*$')

        # 5 minute input rate 0 bits/sec, 0 packets/sec
        p20 = re.compile(r'^(?P<load_interval>[0-9\#]+)'
                         r' *(?P<unit>(minute|second|minutes|seconds)) *input *rate'
                         r' *(?P<in_rate>[0-9]+) *bits/sec,'
                         r' *(?P<in_rate_pkts>[0-9]+) *packets/sec$')

        # 5 minute output rate 0 bits/sec, 0 packets/sec
        p21 = re.compile(r'^(?P<load_interval>[0-9\#]+)'
                         r' *(minute|second|minutes|seconds) *output *rate'
                         r' *(?P<out_rate>[0-9]+) *bits/sec,'
                         r' *(?P<out_rate_pkts>[0-9]+) *packets/sec$')

        # 0 packets input, 0 bytes, 0 no buffer
        # 13350 packets input, 2513375 bytes
        p22 = re.compile(r'^(?P<in_pkts>[0-9]+) +packets +input, +(?P<in_octets>[0-9]+) '
                         r'+bytes(?:, +(?P<in_no_buffer>[0-9]+) +no +buffer)?$')

        # Received 4173 broadcasts (0 IP multicasts)
        # Received 535996 broadcasts (535961 multicasts)
        p23 = re.compile(r'^Received +(?P<in_broadcast_pkts>\d+) +broadcasts +'
                         r'\((?P<in_multicast_pkts>\d+) *(IP)? *multicasts\)$')

        # 0 runts, 0 giants, 0 throttles
        p24 = re.compile(r'^(?P<in_runts>[0-9]+) *runts,'
                         r' *(?P<in_giants>[0-9]+) *giants,'
                         r' *(?P<in_throttles>[0-9]+) *throttles$')

        # 0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored
        # 0 input errors, 0 CRC, 0 frame, 0 overrun, 0 ignored, 0 abort
        p25 = re.compile(r'^(?P<in_errors>[0-9]+) +input +errors, +'
                         r'(?P<in_crc_errors>[0-9]+) +CRC, +'
                         r'(?P<in_frame>[0-9]+) +frame, +'
                         r'(?P<in_overrun>[0-9]+) +overrun, +'
                         r'(?P<in_ignored>[0-9]+) +ignored'
                         r'(, *(?P<in_abort>[0-9]+) +abort)?$')

        # 0 watchdog, 535961 multicast, 0 pause input
        p26 = re.compile(r'^(?P<in_watchdog>[0-9]+) +watchdog, +'
                         r'(?P<in_multicast_pkts>[0-9]+) +multicast, +'
                         r'(?P<in_pause_input>[0-9]+) +pause +input$')

        # 0 input packets with dribble condition detected
        p27 = re.compile(r'^(?P<in_with_dribble>[0-9]+) +input +packets +with +'
                         r'dribble +condition +detected$')

        # 23376 packets output, 3642296 bytes, 0 underruns
        # 13781 packets output, 2169851 bytes
        p28 = re.compile(r'^(?P<out_pkts>[0-9]+) +packets +output, +(?P<out_octets>[0-9]+) '
                         r'+bytes(?:\, +(?P<out_underruns>[0-9]+) +underruns)?$')

        # Output 0 broadcasts (55 multicasts)
        p29 = re.compile(r'^Output +(?P<out_broadcast_pkts>\d+) +broadcasts +'
                         r'\((?P<out_multicast_pkts>\d+) *(IP)? *multicasts\)$')

        # 0 output errors, 0 collisions, 2 interface resets
        # 0 output errors, 0 interface resets
        p30 = re.compile(r'^(?P<out_errors>[0-9]+) +output +errors,'
                         r'( *(?P<out_collision>[0-9]+) +collisions,)? +'
                         r'(?P<out_interface_resets>[0-9]+) +interface +resets$')

        # 0 unknown protocol drops
        p31 = re.compile(r'^(?P<out_unknown_protocl_drops>[0-9]+) +'
                         r'unknown +protocol +drops$')

        # 0 babbles, 0 late collision, 0 deferred
        p32 = re.compile(r'^(?P<out_babble>[0-9]+) +babbles, +'
                         r'(?P<out_late_collision>[0-9]+) +late +collision, +'
                         r'(?P<out_deferred>[0-9]+) +deferred$')

        # 0 lost carrier, 0 no carrier, 0 pause output
        # 0 lost carrier, 0 no carrier
        p33 = re.compile(r'^(?P<out_lost_carrier>\d+) +lost +carrier, +'
                         r'(?P<out_no_carrier>\d+) +no +carrier(, +(?P<out_pause_output>\d+) +'
                         r'pause +output)?$')

        # 0 output buffer failures, 0 output buffers swapped out
        p34 = re.compile(r'^(?P<out_buffer_failure>[0-9]+) +output +buffer +failures, +'
                         r'(?P<out_buffers_swapped>[0-9]+) +output +buffers +swapped +out$')

        # Interface is unnumbered. Using address of Loopback0 (10.4.1.1)
        # Interface is unnumbered. Using address of GigabitEthernet0/2.1 (192.168.154.1)
        p35 = re.compile(r'^Interface +is +unnumbered. +Using +address +of +'
                         r'(?P<unnumbered_intf>[\w\/\.]+) +'
                         r'\((?P<unnumbered_ip>[\w\.\:]+)\)$')

        # 8 maximum active VCs, 1024 VCs per VP, 1 current VCCs
        p36 = re.compile(r'^(?P<maximum_active_vcs>\d+) +maximum +active +VCs, +'
                         r'(?P<vcs_per_vp>\d+) +VCs +per +VP, +(?P<current_vccs>\d+) +current +VCCs$')

        # VC Auto Creation Disabled.
        p37 = re.compile(r'^VC +Auto +Creation +(?P<vc_auto_creation>\S+)\.$')

        # VC idle disconnect time: 300 seconds
        p38 = re.compile(r'^VC +idle +disconnect +time: +(?P<vc_idle_disconnect_time>\d+) +'
                         r'seconds$')

        # AAL5 CRC errors : 0
        p39 = re.compile(r'^(?P<key>\S+ +CRC +errors) +: +(?P<val>\d+)$')

        # AAL5 SAR Timeouts : 0
        p40 = re.compile(r'^(?P<key>\S+ +SAR +Timeouts) +: +(?P<val>\d+)$')

        # AAL5 Oversized SDUs : 0
        p41 = re.compile(r'^(?P<key>\S+ +Oversized +SDUs) +: +(?P<val>\d+)$')

        # LCP Closed
        # LCP Closed, loopback not set
        p42 = re.compile(r'^LCP\s+(?P<state>\S+)(,\s+loopback\s+(?P<loopback>[\S\s]+))?$')

        # Base PPPoATM vaccess
        p43 = re.compile(r'^Base PPPoATM +(?P<base_pppoatm>\S+)$')

        # Vaccess status 0x44, loopback not set
        p44 = re.compile(r'^Vaccess\s+status\s+(?P<status>\S+),\s+'
                         r'loopback\s+(?P<loopback>[\S\s]+)$')

        # DTR is pulsed for 5 seconds on reset
        p45 = re.compile(r'^DTR +is +pulsed +for +(?P<dtr_pulsed>\d+) +'
                         r'seconds +on +reset$')

        # Tunnel source 1.1.10.11
        # Tunnel source 1.1.1.1 (Loopback1)
        # Tunnel source 1.1.10.11, destination 1.1.10.10
        # Tunnel source 172.16.121.201 (GigabitEthernet0/0/1.91), destination 172.16.64.36
        # Tunnel source UNKNOWN, destination 1.2.3.4
        #
        p46 = re.compile(r'^Tunnel +source +(?P<tunnel_source_ip>([a-fA-F\d\:UNKNOWN|0-9\.]+)?),?\s?'
                         r'(?P<tunnel_source_interface>\([\w\d.\/]+\))?,?\s?'
                         r'(destination +)?(?P<tunnel_destination_ip>([a-fA-F\d\:0-9\.]+)?)')

        # Tunnel protocol/transport AURP
        p47 = re.compile(r'^Tunnel +protocol/transport +(?P<tunnel_protocol>[\w\/]+)')

        # Tunnel TTL 255
        p48 = re.compile(r'^Tunnel +TTL +(?P<tunnel_ttl>\d+)')

        # Tunnel transport MTU 1480 bytes
        p49 = re.compile(r'^Tunnel +transport +MTU +(?P<tunnel_transport_mtu>\d+)')

        # Tunnel transmit bandwidth 10000000 (kbps)
        p50 = re.compile(r'^Tunnel +transmit +bandwidth +(?P<tunnel_transmit_bandwidth>\d+)')

        # Tunnel receive bandwidth 10000000 (kbps)
        p51 = re.compile(r'^Tunnel +receive +bandwidth +(?P<tunnel_receive_bandwidth>\d+)')

        # Tunnel Protection profile
        p52 = re.compile(r'^Tunnel +protection +via +(?P<tunnel_protection>[\w]+) +\(profile \"(?P<tunnel_profile>[\w]+)\"\)')

        # 3 carrier transitions
        p53 = re.compile(r'^(?P<carrier_transitions>\d+)\s+carrier transitions$')

        # Carrier delay is 10 sec
        p54 = re.compile(r'^Carrier +delay +is +(?P<carrier_delay>\d+).*$')

        # Asymmetric Carrier-Delay Up Timer is 2 sec
        # Asymmetric Carrier-Delay Down Timer is 10 sec
        p55 = re.compile(r'^Asymmetric +Carrier-Delay +(?P<type>Down|Up)'
                            r' +Timer +is +(?P<carrier_delay>\d+).*$')

        # Peer IP 192.0.2.3, VC ID 1
        p56 = re.compile(r'^Peer IP (?P<peer_ip>[\d\.]+), VC ID (?P<vc_id>\d+)$')

        # RX
        # TX
        p57 = re.compile(r'^(?P<rx_tx>RX|TX)$')

        # 0 packets 0 bytes 0 drops
        p58 = re.compile(r'^(?P<pkts>\d+) packets (?P<octets>\d+) bytes (?P<drops>\d+) drops$')

        interface_dict = {}
        unnumbered_dict = {}
        section_name = None

        for line in out.splitlines():
            line = line.strip()

            # GigabitEthernet1 is up, line protocol is up
            # Port-channel12 is up, line protocol is up (connected)
            # Vlan1 is administratively down, line protocol is down , Autostate Enabled
            # Dialer1 is up (spoofing), line protocol is up (spoofing)
            # FastEthernet1 is down, line protocol is down (err-disabled)
            # GigabitEthernet1/0/2 is up, line protocol is down (suspended)

            m = p1.match(line)
            m1 = p1_1.match(line)
            m2 = p1_2.match(line)
            m = m if m else m1 if m1 else m2
            if m:
                interface = m.groupdict()['interface']
                interface = Common.convert_intf_name(interface)
                enabled = m.groupdict()['enabled']
                line_protocol = m.groupdict().get('line_protocol')
                line_attribute = m.groupdict().get('attribute')
                if m.groupdict().get('autostate'):
                    autostate = m.groupdict()['autostate'].lower()
                else:
                    autostate = None

                if interface not in interface_dict:
                    interface_dict[interface] = {}
                    interface_dict[interface]['port_channel'] = {}
                    interface_dict[interface]['port_channel']\
                        ['port_channel_member'] = False

                if 'deleted' in enabled:
                    interface_dict[interface]['is_deleted'] = True
                else:
                    interface_dict[interface]['is_deleted'] = False

                if 'administratively down' in enabled or 'delete' in enabled:
                    interface_dict[interface]['enabled'] = False
                else:
                    interface_dict[interface]['enabled'] = True

                if line_protocol:
                    interface_dict[interface]\
                                ['line_protocol'] = line_protocol
                    interface_dict[interface]\
                                ['oper_status'] = line_protocol

                if line_attribute:
                    interface_dict[interface]['connected'] = True if line_attribute == 'connected' else False
                    interface_dict[interface]['err_disabled'] = True if line_attribute == 'err-disabled' else False
                    interface_dict[interface]['suspended'] = True if line_attribute == 'suspended' else False

                if autostate:
                    interface_dict[interface]['autostate'] = True if autostate == 'enabled' else False

                continue

            m = p2_3.match(line)
            if m:
                interface_dict[interface]['is_present'] = False
                continue

            # Hardware is Gigabit Ethernet, address is 0057.d2ff.428c (bia 0057.d2ff.428c)
            # Hardware is Loopback
            m = p2.match(line)

            # Hardware is LTE Adv CAT6 - Multimode LTE/DC-HSPA+/HSPA+/HSPA/UMTS/EDGE/GPRS
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
            m = p3.match(line)
            if m:
                description = m.groupdict()['description']

                interface_dict[interface]['description'] = description
                continue

            # Secondary address 10.2.2.2/24
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
            # MTU 9198 bytes, BW not configured
            m = p6.match(line)
            m1 = p6_1.match(line)
            m = m if m else m1
            if m:
                mtu = m.groupdict()['mtu']
                sub_mtu = m.groupdict().get('sub_mtu', None)
                bandwidth = m.groupdict()['bandwidth']
                if m.groupdict().get('delay'):
                    interface_dict[interface]['delay'] = int(m.groupdict()['delay'])
                if mtu:
                    interface_dict[interface]['mtu'] = int(mtu)
                if sub_mtu:
                    interface_dict[interface]['sub_mtu'] = int(sub_mtu)
                if bandwidth:
                    try:
                        interface_dict[interface]['bandwidth'] = int(bandwidth)
                    except ValueError:
                        interface_dict[interface]['bandwidth'] = bandwidth
                continue

            # reliability 255/255, txload 1/255, rxload 1/255
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
            # Encapsulation 802.1Q Virtual LAN, Vlan ID  105.
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
                if not rest:
                    continue
                # Vlan ID 20, medium is p2p
                m1 = re.compile(r'(Vlan +ID +(?P<first_dot1q>[0-9]+),)?'
                                 r' *medium +is +(?P<medium>[a-z0-9]+)$').match(rest)
                # will update key when output is valid
                m2 = re.compile(r'loopback +(?P<loopback>[\w\s]+)$').match(rest)

                #  outer ID  10, inner ID 20
                m3 = re.compile(r'outer +ID +(?P<first>[0-9]+), +'
                                 r'inner +ID (?P<second>[0-9]+)$').match(rest)

                # Vlan ID  1., loopback not set
                # Vlan ID  105.
                m4 = re.compile(r'Vlan +ID +(?P<first_dot1q>\d+).'
                                 r'|(?:,(?P<rest>[\s\w]+))$').match(rest)

                if m1:
                    first_dot1q = m1.groupdict()['first_dot1q']
                    if first_dot1q:
                        interface_dict[interface]['encapsulations']\
                            ['first_dot1q'] = first_dot1q
                    interface_dict[interface]['medium'] = m.groupdict()['medium']
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

            # Keepalive set (10 sec)
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
            # Full Duplex, 10000Mbps, link type is force-up, media type is unknown media type
            # full-duplex, 1000 Mb/s
            # auto-duplex, auto-speed
            # auto-duplex, 10 Gb/s, media type is 10G
            # Full Duplex, 10000Mbps, link type is force-up, media type is SFP-LR
            # Full-duplex, 100Gb/s, link type is force-up, media type is QSFP 100G SR4
            # Full-duplex, 10Gb/s, link type is auto, media type is CVR QSFP SFP10G(SFP-10GBase-SR)
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
                    unknown = re.search(r'[U|u]nknown',media_type)
                    if unknown:
                        interface_dict[interface]['media_type'] = 'unknown'
                    else:
                        interface_dict[interface]['media_type'] = media_type
                continue

            # input flow-control is off, output flow-control is unsupported
            m = p12.match(line)
            if m:
                groups = m.groupdict()
                receive = groups['receive'].lower() if groups['first'] == 'input' else groups['send'].lower()
                send = groups['send'].lower() if groups['second'] == 'output' else groups['receive'].lower()
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
            m = p54.match(line)
            if m:
                group = m.groupdict()
                sub_dict = interface_dict.setdefault(interface, {})
                sub_dict['carrier_delay'] = int(group['carrier_delay'])
                continue

            # Asymmetric Carrier-Delay Up Timer is 2 sec
            # Asymmetric Carrier-Delay Down Timer is 10 sec
            m = p55.match(line)
            if m:
                group = m.groupdict()
                tp = group['type'].lower()
                sub_dict = interface_dict.setdefault(interface, {})
                if tp == 'up':
                    sub_dict['carrier_delay_up'] = int(group['carrier_delay'])
                else:
                    sub_dict['carrier_delay_down'] = int(group['carrier_delay'])
                continue

            # ARP type: ARPA, ARP Timeout 04:00:00
            m = p13.match(line)
            if m:
                arp_type = m.groupdict()['arp_type'].lower()
                arp_timeout = m.groupdict()['arp_timeout']
                interface_dict[interface]['arp_type'] = arp_type
                interface_dict[interface]['arp_timeout'] = arp_timeout
                continue

            # Last input never, output 00:01:05, output hang never
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

            # No. of active members in this channel: 12
            m = p15_1.match(line)
            if m:
                group = m.groupdict()
                active_members = int(group['active_members'])
                interface_dict[interface]['port_channel']\
                    ['port_channel_member'] = True
                interface_dict[interface]['port_channel']\
                    ['active_members'] = active_members
                continue

            # Member 2 : GigabitEthernet0/0/10 , Full-duplex, 900Mb/s
            m = p15_2.match(line)
            if m:
                group = m.groupdict()
                intf = group['interface']
                if 'port_channel_member_intfs' not in interface_dict[interface]['port_channel']:
                    interface_dict[interface]['port_channel']\
                            ['port_channel_member_intfs'] = []

                interface_dict[interface]['port_channel']\
                    ['port_channel_member_intfs'].append(intf)

                continue

            # No. of PF_JUMBO supported members in this channel : 0
            m = p15_3.match(line)
            if m:
                group = m.groupdict()
                number = int(group['number'])
                interface_dict[interface]['port_channel']\
                    ['num_of_pf_jumbo_supported_members'] = number
                continue

            # Last clearing of "show interface" counters 1d02h
            m = p16.match(line)
            if m:
                last_clear = m.groupdict()['last_clear']
                continue

            # Input queue: 0/375/0/0 (size/max/drops/flushes); Total output drops: 0
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
            # Queueing strategy: Class-based queueing
            m = p18.match(line)
            if m:
                if 'queues' not in interface_dict[interface]:
                    interface_dict[interface]['queues'] = {}
                interface_dict[interface]['queues']['queue_strategy'] = \
                    m.groupdict()['queue_strategy']
                continue

            # Output queue: 0/0 (size/max)
            # Output queue: 0/1000/64/0 (size/max total/threshold/drops)
            m = p19.match(line)
            if m:
                if 'queues' not in interface_dict[interface]:
                    interface_dict[interface]['queues'] = {}
                interface_dict[interface]['queues']['output_queue_size'] = \
                    int(m.groupdict()['size'])
                interface_dict[interface]['queues']['output_queue_max'] = \
                    int(m.groupdict()['max'])
                if m.groupdict()['threshold'] and m.groupdict()['drops']:
                    interface_dict[interface]['queues']['threshold'] = \
                        int(m.groupdict()['threshold'])
                    interface_dict[interface]['queues']['drops'] = \
                        int(m.groupdict()['drops'])
                continue

            # 5 minute input rate 0 bits/sec, 0 packets/sec
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
            m = p21.match(line)
            if m:
                if 'counters' not in interface_dict[interface]:
                    interface_dict[interface]['counters'] = {}
                    interface_dict[interface]['counters']['rate'] = {}

                out_rate = int(m.groupdict()['out_rate'])
                out_rate_pkts = int(m.groupdict()['out_rate_pkts'])

                interface_dict[interface]['counters']['rate']\
                    ['out_rate'] = out_rate
                interface_dict[interface]['counters']['rate']\
                    ['out_rate_pkts'] = out_rate_pkts
                continue

            # 0 packets input, 0 bytes, 0 no buffer
            m = p22.match(line)
            if m:
                if 'counters' not in interface_dict[interface]:
                    interface_dict[interface]['counters'] = {}

                interface_dict[interface]['counters']['in_pkts'] = \
                    int(m.groupdict()['in_pkts'])
                interface_dict[interface]['counters']['in_octets'] = \
                    int(m.groupdict()['in_octets'])
                if m.groupdict()['in_no_buffer']:
                    interface_dict[interface]['counters']['in_no_buffer'] = \
                        int(m.groupdict()['in_no_buffer'])
                continue

            # Received 4173 broadcasts (0 IP multicasts)
            # Received 535996 broadcasts (535961 multicasts)
            m = p23.match(line)
            if m:
                interface_dict[interface]['counters']['in_multicast_pkts'] = \
                    int(m.groupdict()['in_multicast_pkts'])
                interface_dict[interface]['counters']['in_broadcast_pkts'] = \
                    int(m.groupdict()['in_broadcast_pkts'])
                continue

            # 0 runts, 0 giants, 0 throttles
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
            m = p27.match(line)
            if m:
                interface_dict[interface]['counters']['in_with_dribble'] = \
                    int(m.groupdict()['in_with_dribble'])
                continue

            # 23376 packets output, 3642296 bytes, 0 underruns
            m = p28.match(line)
            if m:
                interface_dict[interface]['counters']['out_pkts'] = \
                    int(m.groupdict()['out_pkts'])
                interface_dict[interface]['counters']['out_octets'] = \
                    int(m.groupdict()['out_octets'])
                if m.groupdict()['out_underruns']:
                    interface_dict[interface]['counters']['out_underruns'] = \
                        int(m.groupdict()['out_underruns'])
                continue

            # Output 0 broadcasts (55 multicasts)
            m = p29.match(line)
            if m:
                interface_dict[interface]['counters']['out_broadcast_pkts'] = \
                    int(m.groupdict()['out_broadcast_pkts'])
                interface_dict[interface]['counters']['out_multicast_pkts'] = \
                    int(m.groupdict()['out_multicast_pkts'])
                continue

            # 0 output errors, 0 collisions, 2 interface resets
            # 0 output errors, 0 interface resets
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
            m = p31.match(line)
            if m:
                interface_dict[interface]['counters']['out_unknown_protocl_drops'] = \
                    int(m.groupdict()['out_unknown_protocl_drops'])
                continue

            # 0 babbles, 0 late collision, 0 deferred
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
            m = p33.match(line)
            if m:
                interface_dict[interface]['counters']['out_lost_carrier'] = \
                    int(m.groupdict()['out_lost_carrier'])
                interface_dict[interface]['counters']['out_no_carrier'] = \
                    int(m.groupdict()['out_no_carrier'])
                out_pause_output = m.groupdict().get('out_pause_output', None)
                if out_pause_output:
                    interface_dict[interface]['counters']['out_mac_pause_frames'] = \
                        int(m.groupdict()['out_pause_output'])
                continue

            # 0 output buffer failures, 0 output buffers swapped out
            m = p34.match(line)
            if m:
                interface_dict[interface]['counters']['out_buffer_failure'] = \
                    int(m.groupdict()['out_buffer_failure'])
                interface_dict[interface]['counters']['out_buffers_swapped'] = \
                    int(m.groupdict()['out_buffers_swapped'])
                continue

            # Interface is unnumbered. Using address of Loopback0 (10.4.1.1)
            # Interface is unnumbered. Using address of GigabitEthernet0/2.1 (192.168.154.1)
            m = p35.match(line)
            if m:
                unnumbered_dict[interface] = {}
                unnumbered_dict[interface]['unnumbered_intf'] = m.groupdict()['unnumbered_intf']
                unnumbered_dict[interface]['unnumbered_ip'] = m.groupdict()['unnumbered_ip']
                continue

            # 8 maximum active VCs, 1024 VCs per VP, 1 current VCCs
            m = p36.match(line)
            if m:
                group = m.groupdict()
                maximum_active_vcs = group['maximum_active_vcs']
                vcs_per_vp = group['vcs_per_vp']
                current_vccs = group['current_vccs']
                interface_dict[interface].update({'maximum_active_vcs': maximum_active_vcs})
                interface_dict[interface].update({'vcs_per_vp': vcs_per_vp})
                interface_dict[interface].update({'current_vccs': current_vccs})
                continue

            # VC Auto Creation Disabled.
            m = p37.match(line)
            if m:
                group = m.groupdict()
                vc_auto_creation = group['vc_auto_creation']
                interface_dict[interface].update({'vc_auto_creation': vc_auto_creation})
                continue

            # VC idle disconnect time: 300 seconds
            m = p38.match(line)
            if m:
                group = m.groupdict()
                vc_idle_disconnect_time = group['vc_idle_disconnect_time']
                interface_dict[interface].update({'vc_idle_disconnect_time': vc_idle_disconnect_time})
                continue

            # AAL5 CRC errors : 0
            m = p39.match(line)
            if m:
                group = m.groupdict()
                interface_dict[interface].update({'aal5_crc_errors': int(group['val'])})
                continue

            # AAL5 SAR Timeouts : 0
            m = p40.match(line)
            if m:
                group = m.groupdict()
                interface_dict[interface].update({'aal5_oversized_sdus': int(group['val'])})
                continue

            # AAL5 Oversized SDUs : 0
            m = p41.match(line)
            if m:
                group = m.groupdict()
                interface_dict[interface].update({'aal5_sar_timeouts': int(group['val'])})
                continue

            # LCP Closed
            m = p42.match(line)
            if m:
                group = m.groupdict()
                interface_dict[interface].update({'lcp_state': group['state']})
                loopback = group.get('loopback', None)
                if loopback:
                    interface_dict[interface].update({'lcp_loopack': loopback})
                continue

            # Base PPPoATM vaccess
            m = p43.match(line)
            if m:
                group = m.groupdict()
                interface_dict[interface].update({'base_pppoatm': group['base_pppoatm']})
                continue

            # Vaccess status 0x44, loopback not set
            m = p44.match(line)
            if m:
                group = m.groupdict()
                interface_dict[interface].update({'vaccess_status': group['status']})
                interface_dict[interface].update({'vaccess_loopback': group['loopback']})
                continue

            # DTR is pulsed for 5 seconds on reset
            m = p45.match(line)
            if m:
                group = m.groupdict()
                interface_dict[interface].update({'dtr_pulsed': group['dtr_pulsed']})
                continue

            # Tunnel source 1.1.10.11
            # Tunnel source 1.1.1.1 (Loopback1)
            # Tunnel source 1.1.10.11, destination 1.1.10.10
            # Tunnel source 172.16.121.201 (GigabitEthernet0/0/1.91), destination 172.16.64.36
            # Tunnel source UNKNOWN, destination 1.2.3.4
            m = p46.match(line)
            if m:
                group = m.groupdict()
                interface_dict[interface].update({'tunnel_source_ip': group['tunnel_source_ip']})
                if group['tunnel_source_interface']:
                    interface_dict[interface].update({'tunnel_source_interface': (group['tunnel_source_interface']).strip('()')})
                if group['tunnel_destination_ip']:
                    interface_dict[interface].update({'tunnel_destination_ip': group['tunnel_destination_ip']})
                continue

            # Tunnel protocol/transport AURP
            m = p47.match(line)
            if m:
                group = m.groupdict()
                interface_dict[interface].update({'tunnel_protocol': group['tunnel_protocol']})
                continue

            # Tunnel TTL 255
            m = p48.match(line)
            if m:
                group = m.groupdict()
                interface_dict[interface].update({'tunnel_ttl': int(group['tunnel_ttl'])})
                continue

            # Tunnel transport MTU 1480 bytes
            m = p49.match(line)
            if m:
                group = m.groupdict()
                interface_dict[interface].update({'tunnel_transport_mtu': int(group['tunnel_transport_mtu'])})
                continue

            # Tunnel transmit bandwidth 10000000 (kbps)
            m = p50.match(line)
            if m:
                group = m.groupdict()
                interface_dict[interface].update({'tunnel_transmit_bandwidth': int(group['tunnel_transmit_bandwidth'])})
                continue

            # Tunnel receive bandwidth 10000000 (kbps)
            m = p51.match(line)
            if m:
                group = m.groupdict()
                interface_dict[interface].update({'tunnel_receive_bandwidth': int(group['tunnel_receive_bandwidth'])})
                continue

            m = p52.match(line)
            if m:
                group = m.groupdict()
                if group['tunnel_protection']:
                    interface_dict[interface].update({'tunnel_protection': group['tunnel_protection']})
                if group['tunnel_profile']:
                    interface_dict[interface].update({'tunnel_profile': group['tunnel_profile']})
                continue

            # 3 carrier transitions
            m = p53.match(line)
            if m:
                group = m.groupdict()
                interface_dict[interface]['carrier_transitions'] = int(group['carrier_transitions'])
                continue

            # Peer IP 192.0.2.3, VC ID 1
            m = p56.match(line)
            if m:
                group = m.groupdict()
                interface_dict[interface]['peer_ip'] = group['peer_ip']
                interface_dict[interface]['vc_id'] = int(group['vc_id'])
                continue

            # RX
            # TX
            m = p57.match(line)
            if m:
                group = m.groupdict()
                section_name = group['rx_tx'].lower()
                continue

            # 0 packets 0 bytes 0 drops
            # re.compile(r'^(?P<pkts>\d+) packets (?P<octets>\d+) bytes (?P<drops>\d+) drops$')
            m = p58.match(line)
            if m:
                group = m.groupdict()
                coutners_dict = interface_dict[interface].setdefault('counters', {})
                direction = 'in' if section_name == 'rx' else 'out'
                coutners_dict[f'{direction}_pkts'] = int(group['pkts'])
                coutners_dict[f'{direction}_octets'] = int(group['octets'])
                coutners_dict[f'{direction}_drops'] = int(group['drops'])
                continue

        # create strucutre for unnumbered interface
        if not unnumbered_dict:
            return (interface_dict)

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
                            m = re.search(r'([\w\.\:]+)\/(\d+)', ip)
                            interface_dict[intf]['ipv4'][ip]['ip'] = m.groups()[0]
                            interface_dict[intf]['ipv4'][ip]['prefix_length'] = m.groups()[1]
                            interface_dict[intf]['ipv4']['unnumbered'] = {}
                            interface_dict[intf]['ipv4']['unnumbered']\
                                ['interface_ref'] = unnumbered_intf

        return (interface_dict)


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
    exclude = ['method', '(Tunnel.*)']

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
                                                 r"OK\?",
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

            # Building the schema out of the parsergen output
            if res.entries:
                for intf, intf_dict in res.entries.items():
                    intf = Common.convert_intf_name(intf)
                    del intf_dict['Interface']
                    parsed_dict.setdefault('interface', {}).update({intf: intf_dict})

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
        merged_output = merge_dict(yang_output,cli_output)
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
            r'+(?P<ip_address>[a-z0-9\.]+) +(?P<interface_ok>[A-Z]+) '
            r'+(?P<method>[a-zA-Z]+) +(?P<interface_status>[a-z\s]+) '
            r'+(?P<protocol_status>[a-z]+)$')

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
    """Schema for:
        * show interfaces switchport
        * show interfaces {interface} switchport
    """
    schema = {
            Any(): {
                'switchport_enable': bool,
                Optional('switchport_mode'): str,
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
                    Optional('native_vlan_name'): str,
                },
                Optional('negotiation_of_trunk'): bool,
                Optional('access_vlan'): str,
                Optional('access_vlan_name'): str,
                Optional('voice_vlan'): str,
                Optional('voice_vlan_name'): str,
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
                Optional('admin_ethertype'): str,
                Optional('oper_ethertype'): str,
            },
        }


class ShowInterfacesSwitchport(ShowInterfacesSwitchportSchema):
    """
    parser for show interfaces switchport

    """

    cli_command = ['show interfaces switchport', 'show interfaces {interface} switchport']

    def cli(self, interface='', output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[1].format(interface=interface)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        # Name: Gi1/0/2
        p1 = re.compile(r'^Name: +(?P<intf>[\w\/\.\-]+)$')

        # Switchport: Enabled
        p2 = re.compile(r'^Switchport: +(?P<switchport_enable>\w+)$')

        # Administrative Mode: trunk
        p3 = re.compile(r'^Administrative +Mode: +(?P<switchport_mode>[\w\s]+)$')

        # Operational Mode: trunk (member of bundle Po12)
        # Operational Mode: down (suspended member of bundle Po12)
        p4 = re.compile(r'^Operational +Mode: +(?P<operational_mode>[\w\s]+)'
                        r'( +\((?P<dummy>[\w\s]+)? *member +of +bundle '
                        r'+(?P<port_channel_int>[\w\/\.\-]+)\))?$')

        # Administrative Trunking Encapsulation: dot1q
        p5 = re.compile(r'^Administrative +Trunking +Encapsulation: +'
                        r'(?P<encapsulation>\w+)$')

        # Operational Trunking Encapsulation: dot1q
        p6 = re.compile(r'^Operational +Trunking +Encapsulation: +'
                        r'(?P<encapsulation>\w+)$')

        # Negotiation of Trunking: On
        p7 = re.compile(r'^Negotiation +of +Trunking: +(?P<negotiation_of_trunk>\w+)$')

        # Access Mode VLAN: 1 (default)
        # Access Mode VLAN: 100 (Falback-Data)
        p8 = re.compile(r'^Access +Mode +VLAN: +(?P<access_vlan>[\d\-]+)'
                        r'( *\((?P<access_vlan_name>.+)\))?$')

        # Trunking Native Mode VLAN: 1 (default)
        p9 = re.compile(r'^Trunking +Native +Mode +VLAN: +(?P<native_vlan>[\d\-]+)'
                        r'( *\((?P<native_vlan_name>.+)\))?$')

        # Administrative Native VLAN tagging: enabled
        p10 = re.compile(r'^Administrative +Native +VLAN +tagging: +'
                         r'(?P<tagging>\w+)$')

        # Voice VLAN: none
        # Voice VLAN: 100 (Fallback-Voice)
        p11 = re.compile(r'^Voice +VLAN: +(?P<vlan>[\d\-]+)'
                         r'( *\((?P<voice_vlan_name>.+)\))?$')

        # Administrative private-vlan host-association: none
        p12 = re.compile(r'^Administrative +private-vlan +'
                         r'host-association: +(?P<ret>[\w\-]+)$')

        # Administrative private-vlan mapping: none
        p13 = re.compile(r'^Administrative +private-vlan +'
                         r'mapping: +(?P<ret>[\w\-]+)$')

        # Administrative private-vlan trunk native VLAN: none
        p14 = re.compile(r'^Administrative +private-vlan +'
                         r'trunk +native +VLAN: +(?P<ret>[\w\-]+)$')

        # Administrative private-vlan trunk Native VLAN tagging: enabled
        p15 = re.compile(r'^Administrative +private-vlan +'
                         r'trunk +Native +VLAN +tagging: +(?P<ret>[\w\-]+)$')

        # Administrative private-vlan trunk encapsulation: dot1q
        p16 = re.compile(r'^Administrative +private-vlan +'
                         r'trunk +encapsulation: +(?P<ret>[\w\-]+)$')

        # Administrative private-vlan trunk normal VLANs: none
        p17 = re.compile(r'^Administrative +private-vlan +'
                         r'trunk +normal +VLANs: +(?P<ret>[\w\-]+)$')

        # Administrative private-vlan trunk associations: none
        p18 = re.compile(r'^Administrative +private-vlan +'
                         r'trunk +associations: +(?P<ret>[\w\-]+)$')

        # Administrative private-vlan trunk mappings: none
        # Administrative private-vlan trunk mappings:
        p19 = re.compile(r'^Administrative +private-vlan +'
                         r'trunk +mappings:( *(?P<ret>[\w\-]+))?$')

        # Operational private-vlan: none
        # Operational private-vlan:
        p20 = re.compile(r'^Operational +private-vlan:'
                         r'( *(?P<private_operational>[\w\-]+))?$')

        # Trunking VLANs Enabled: 200-211
        # Trunking VLANs Enabled: 100,101,110-120,121,130,170,180,
        p21 = re.compile(r'^Trunking +VLANs +Enabled: +(?P<trunk_vlans>[\w\-\,\s]+)$')

        # 1111,2222,3333, 500-55,
        p21_1 = re.compile(r'^(?P<trunk_vlans>[\d\,\-]+)$')

        # Pruning VLANs Enabled: 2-1001
        p22 = re.compile(r'^Pruning +VLANs +Enabled: +(?P<pruning_vlans>[\w\-]+)$')

        # Capture Mode Disabled
        p23 = re.compile(r'^Capture +Mode +(?P<mode>\w+)$')

        # Capture VLANs Allowed: ALL
        p24 = re.compile(r'^Capture +VLANs +Allowed: +(?P<capture_vlans>[\w\-]+)$')

        # Protected: false
        p25 = re.compile(r'^Protected: +(?P<protected>\w+)$')

        # Unknown unicast blocked: disabled
        p26 = re.compile(r'^Unknown +unicast +blocked: +(?P<block>\w+)$')

        # Unknown multicast blocked: disabled
        p27 = re.compile(r'^Unknown +multicast +blocked: +(?P<block>\w+)$')

        # Appliance trust: none
        p28 = re.compile(r'^Appliance +trust: +(?P<trust>[\w\-]+)$')

        #Administrative Dot1q Ethertype: 0x9100
        p29 = re.compile(r'^Administrative +Dot1q +Ethertype: +(?P<admin_ethertype>\w+)$')

        #Operational Dot1q Ethertype: 0x9100
        p30 = re.compile(r'^Operational +Dot1q +Ethertype: +(?P<oper_ethertype>\w+)$')

        ret_dict = {}
        private_trunk_mappings = None
        private_operational = None
        for line in out.splitlines():
            line = line.strip()

            # Name: Gi1/0/2
            m = p1.match(line)
            if m:
                intf = Common.convert_intf_name(m.groupdict()['intf'])
                if intf not in ret_dict:
                    ret_dict[intf] = {}
                continue

            # Switchport: Enabled
            m = p2.match(line)
            if m:
                if m.groupdict()['switchport_enable'].lower() == 'enabled':
                    ret_dict[intf]['switchport_enable'] = True
                else:
                    ret_dict[intf]['switchport_enable'] = False

                continue

            # Administrative Mode: trunk
            m = p3.match(line)
            if m:
                ret_dict[intf]['switchport_mode'] = m.groupdict()['switchport_mode']
                continue

            # Operational Mode: trunk (member of bundle Po12)
            # Operational Mode: down (suspended member of bundle Po12)
            m = p4.match(line)
            if m:
                if interface:
                    ret_dict[intf]['operational_mode'] = m.groupdict()['operational_mode']

                    bundle_intf = m.groupdict()['port_channel_int']
                    if bundle_intf:
                        port_channel_dict = ret_dict[intf].setdefault('port_channel', {})
                        bundle_intf = Common.convert_intf_name(bundle_intf)

                        port_channel_dict.update({
                            'port_channel_int': bundle_intf,
                            'port_channel_member': True
                        })
                else:
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
            m = p5.match(line)
            if m:
                if 'encapsulation' not in ret_dict[intf]:
                    ret_dict[intf]['encapsulation'] = {}
                ret_dict[intf]['encapsulation']['administrative_encapsulation'] = \
                    m.groupdict()['encapsulation'].lower()
                continue

            # Operational Trunking Encapsulation: dot1q
            m = p6.match(line)
            if m:
                if 'encapsulation' not in ret_dict[intf]:
                    ret_dict[intf]['encapsulation'] = {}
                ret_dict[intf]['encapsulation']['operational_encapsulation'] = \
                    m.groupdict()['encapsulation'].lower()
                continue

            # Negotiation of Trunking: On
            m = p7.match(line)
            if m:
                negotiation_of_trunk = m.groupdict()['negotiation_of_trunk'].lower()
                if 'on' in negotiation_of_trunk:
                    ret_dict[intf]['negotiation_of_trunk'] = True
                elif 'off' in negotiation_of_trunk:
                    ret_dict[intf]['negotiation_of_trunk'] = False
                continue

            # Access Mode VLAN: 1 (default)
            # Access Mode VLAN: 100 (Falback-Data)
            m = p8.match(line)
            if m:
                ret_dict[intf]['access_vlan'] = m.groupdict()['access_vlan']
                if m.groupdict()['access_vlan_name']:
                    ret_dict[intf]['access_vlan_name'] = m.groupdict()['access_vlan_name']
                continue

            # Trunking Native Mode VLAN: 1 (default)
            m = p9.match(line)
            if m:
                if 'encapsulation' not in ret_dict[intf]:
                    ret_dict[intf]['encapsulation'] = {}
                ret_dict[intf]['encapsulation']['native_vlan'] = m.groupdict()['native_vlan']
                if m.groupdict()['native_vlan_name']:
                    ret_dict[intf]['encapsulation']['native_vlan_name'] = m.groupdict()['native_vlan_name']
                continue

            # Administrative Native VLAN tagging: enabled
            m = p10.match(line)
            if m:
                if 'enable' in m.groupdict()['tagging'].lower():
                    ret_dict[intf]['native_vlan_tagging'] = True
                else:
                    ret_dict[intf]['native_vlan_tagging'] = False
                continue

            # Voice VLAN: none
            # Voice VLAN: 100 (Fallback-Voice)
            m = p11.match(line)
            if m:
                ret_dict[intf]['voice_vlan'] = m.groupdict()['vlan']
                if m.groupdict()['voice_vlan_name']:
                    ret_dict[intf]['voice_vlan_name'] = m.groupdict()['voice_vlan_name']
                continue

            # Administrative private-vlan host-association: none
            m = p12.match(line)
            if m:
                if 'private_vlan' not in ret_dict[intf]:
                    ret_dict[intf]['private_vlan'] = {}
                ret = m.groupdict()['ret'].lower()
                if ret != 'none':
                    ret_dict[intf]['private_vlan']['host_association'] = m.groupdict()['ret']
                continue

            # Administrative private-vlan mapping: none
            m = p13.match(line)
            if m:
                if 'private_vlan' not in ret_dict[intf]:
                    ret_dict[intf]['private_vlan'] = {}
                ret = m.groupdict()['ret'].lower()
                if ret != 'none':
                    ret_dict[intf]['private_vlan']['mapping'] = m.groupdict()['ret']
                continue

            # Administrative private-vlan trunk native VLAN: none
            m = p14.match(line)
            if m:
                if 'private_vlan' not in ret_dict[intf]:
                    ret_dict[intf]['private_vlan'] = {}
                ret = m.groupdict()['ret'].lower()
                if ret != 'none':
                    ret_dict[intf]['private_vlan']['native_vlan'] = m.groupdict()['ret']
                continue

            # Administrative private-vlan trunk Native VLAN tagging: enabled
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
            m = p16.match(line)
            if m:
                if 'private_vlan' not in ret_dict[intf]:
                    ret_dict[intf]['private_vlan'] = {}
                ret = m.groupdict()['ret'].lower()
                if ret != 'none':
                    ret_dict[intf]['private_vlan']['encapsulation'] = m.groupdict()['ret']
                continue

            # Administrative private-vlan trunk normal VLANs: none
            m = p17.match(line)
            if m:
                if 'private_vlan' not in ret_dict[intf]:
                    ret_dict[intf]['private_vlan'] = {}
                ret = m.groupdict()['ret'].lower()
                if ret != 'none':
                    ret_dict[intf]['private_vlan']['normal_vlans'] = m.groupdict()['ret']
                continue

            # Administrative private-vlan trunk associations: none
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
                p19_1 = re.compile(r'^(?P<mappings>[\w\(\)\s]+)$')
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
            m = p20.match(line)
            if m:
                if 'private_vlan' not in ret_dict[intf]:
                    ret_dict[intf]['private_vlan'] = {}
                private_operational = m.groupdict()['private_operational']
                if private_operational and private_operational.lower() != 'none':
                    ret_dict[intf]['private_vlan']['operational'] = private_operational
                private_operational = ''
                continue

            # Trunking VLANs Enabled: 200-211
            # Trunking VLANs Enabled: 100,101,110-120,121,130,170,180,
            m = p21.match(line)
            if m:
                ret_dict[intf]['trunk_vlans'] = m.groupdict()['trunk_vlans'].lower()
                private_operational = None
                continue

            # 10 (VLAN0010) 100 (VLAN0100)
            if isinstance(private_operational, str):
                p20_1 = re.compile(r'^(?P<private_operational>[\w\(\)\s]+)$')
                m = p20_1.match(line)
                if m:
                    ret = m.groupdict()['private_operational']
                    private_operational += ' {}'.format(ret)
                    ret_dict[intf]['private_vlan']['operational'] = private_operational.strip()
                # reset private_trunk_mappings
                private_operational = None
                continue

            # 1111,2222,3333, 500-55,
            m = p21_1.match(line)
            if m:
                ret_dict[intf]['trunk_vlans'] += m.groupdict()['trunk_vlans'].lower()
                continue

            # Pruning VLANs Enabled: 2-1001
            m = p22.match(line)
            if m:
                ret_dict[intf]['pruning_vlans'] = m.groupdict()['pruning_vlans'].lower()
                continue

            # Capture Mode Disabled
            m = p23.match(line)
            if m:
                mode = m.groupdict()['mode'].lower()
                if 'disabled' in mode:
                    ret_dict[intf]['capture_mode'] = False
                else:
                    ret_dict[intf]['capture_mode'] = True
                continue

            # Capture VLANs Allowed: ALL
            m = p24.match(line)
            if m:
                ret_dict[intf]['capture_vlans'] = m.groupdict()['capture_vlans'].lower()
                continue

            # Protected: false
            m = p25.match(line)
            if m:
                if 'false' in m.groupdict()['protected'].lower():
                    ret_dict[intf]['protected'] = False
                else:
                    ret_dict[intf]['protected'] = True
                continue

            # Unknown unicast blocked: disabled
            m = p26.match(line)
            if m:
                if 'disabled' in m.groupdict()['block'].lower():
                    ret_dict[intf]['unknown_unicast_blocked'] = False
                else:
                    ret_dict[intf]['unknown_unicast_blocked'] = True
                continue

            # Unknown multicast blocked: disabled
            m = p27.match(line)
            if m:
                if 'disabled' in m.groupdict()['block'].lower():
                    ret_dict[intf]['unknown_multicast_blocked'] = False
                else:
                    ret_dict[intf]['unknown_multicast_blocked'] = True
                continue

            # Appliance trust: none
            m = p28.match(line)
            if m:
                if m.groupdict()['trust'] != 'none':
                    ret_dict[intf]['appliance_trust'] = m.groupdict()['trust']
                continue

            # Administrative Dot1q Ethertype: 0x9100
            m = p29.match(line)
            if m:
                admin_ethertype = m.groupdict()['admin_ethertype']
                ret_dict[intf]['admin_ethertype'] = admin_ethertype

            # Operational Dot1q Ethertype: 0x9100
            m = p30.match(line)
            if m:
                oper_ethertype = m.groupdict()['oper_ethertype']
                ret_dict[intf]['oper_ethertype'] = oper_ethertype

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
                            Optional('broadcast_address'): str,
                        },
                    },
                    Optional('mtu'): int,
                    Optional('address_determined_by'): str,
                    Optional('helper_address'): Or(str, list),
                    Optional('directed_broadcast_forwarding'): bool,
                    Optional('outbound_common_access_list'): str,
                    Optional('outbound_access_list'): str,
                    Optional('inbound_common_access_list'): str,
                    Optional('inbound_access_list'): str,
                    Optional('proxy_arp'): bool,
                    Optional('local_proxy_arp'): bool,
                    Optional('security_level'): str,
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

    cli_command = [
        'show ip interface',
        'show ip interface {interface}',
        'show ip interface | include {include}',
    ]
    exclude = ['unnumbered', 'address_determined_by', '(Tunnel.*)', 'joins', 'leaves']

    def cli(self, interface="", include=None, output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[1].format(interface=interface)
            elif include:
                cmd = self.cli_command[2].format(include=include)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        read_multicast_reserved_lines = False
        multicast_groups = []
        interface_dict = {}
        unnumbered_dict = {}
        for line in out.splitlines():
            line = line.strip()

            # Vlan211 is up, line protocol is up
            # GigabitEthernet2 is administratively down, line protocol is down
            p1 =  re.compile(r'^(?P<interface>[\w\/\.\-\:]+) +is'
                            r' +(?P<enabled>[\w\s]+),'
                            r' +line +protocol +is +(?P<oper_status>\w+)$')
            m = p1.match(line)
            if m:
                interface = m.groupdict()['interface']
                enabled = m.groupdict()['enabled'].lower()
                if interface not in interface_dict:
                    interface_dict[interface] = {}
                if 'administratively down' in enabled or 'delete' in enabled:
                    interface_dict[interface]['enabled'] = False
                else:
                    interface_dict[interface]['enabled'] = True
                interface_dict[interface]['oper_status'] = \
                    m.groupdict()['oper_status'].lower()

                continue

            # Internet address is 192.168.76.1/24
            p2 = re.compile(r'^Internet +[A|a]ddress +is +(?P<ipv4>(?P<ip>[0-9\.]+)'
                            r'\/(?P<prefix_length>[0-9]+))$')
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

            # Interface is unnumbered. Using address of GigabitEthernet0/0.101 (10.1.98.10)
            p2_0 = re.compile(r'^Interface +is +unnumbered. +Using +address +of +(\S+)'
                              r' +\((?P<ipv4>(?P<ip>[0-9\.]+))\)$')
            m = p2_0.match(line)
            if m:
                ip = m.groupdict()['ip']
                address = m.groupdict()['ipv4']

                if 'ipv4' not in interface_dict[interface]:
                    interface_dict[interface]['ipv4'] = {}
                if address not in interface_dict[interface]['ipv4']:
                    interface_dict[interface]['ipv4'][address] = {}

                interface_dict[interface]['ipv4'][address]\
                    ['ip'] = ip
                interface_dict[interface]['ipv4'][address]\
                    ['secondary'] = False
                continue

            # Secondary address 10.2.2.2/24
            p2_1 = re.compile(r'^Secondary +address +(?P<ipv4>(?P<ip>[0-9\.]+)'
                              r'\/(?P<prefix_length>[0-9]+))$')
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
            # Internet address will be negotiated using DHCP
            # Internet address will be negotiated using IPCP
            p2_2 = re.compile(r'^Internet +[A|a]ddress +will +be +negotiated '
                              r'+using +(?P<negotiated>DHCP|IPCP)$')
            m = p2_2.match(line)
            if m:
                negotiated_holder = m.groupdict()
                if 'DHCP' in negotiated_holder.get('negotiated'):
                    address='dhcp_negotiated'
                if 'IPCP' in negotiated_holder.get('negotiated'):
                    address='ipcp_negotiated'
                ipv4_dict = interface_dict[interface].setdefault('ipv4',{})
                ipv4_dict.setdefault(address, {})
                ipv4_dict[address]['ip'] = address
                continue

            # Broadcast address is 255.255.255.255
            p3 = re.compile(r'^Broadcast +address +is +(?P<address>[\w\.\:]+)$')
            m = p3.match(line)
            if m:
                if 'ipv4' in interface_dict[interface]:
                    if address in interface_dict[interface]['ipv4']:
                        interface_dict[interface]['ipv4'][address]['broadcast_address'] = \
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
            p5 = re.compile(r'^Helper +address +is +not +set$')
            m = p5.match(line)
            if m:
                continue

            # Helper address is 10.1.1.1
            p5_0 = re.compile(r'^Helper +address +is +(?P<address>[\d\.]+)$')
            m = p5_0.match(line)
            if m:
                interface_dict[interface]['helper_address'] = \
                    [m.groupdict()['address']]
                continue

            # Helper addresses are 10.1.1.1
            p5_1 = re.compile(r'^Helper +addresses +are +(?P<address>[\w\.\:\s]+)$')
            m = p5_1.match(line)
            if m:
                helper_flag = True
                if 'not set' not in m.groupdict()['address']:
                    helper_list = []
                    helper_list.append(m.groupdict()['address'])
                    interface_dict[interface]['helper_address'] = \
                        helper_list
                continue

            # 10.2.2.2
            p5_2 = re.compile(r'^(?P<address>[\d\.]+)$')
            m = p5_2.match(line)
            if m:
                if helper_flag:
                    helper_list.append(m.groupdict()['address'])
                    continue
            else:
                helper_flag = False

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

                interface_dict[interface]['multicast_groups'] = multicast_groups
                read_multicast_reserved_lines = True
                continue

            # Multicast reserved groups joined: 224.0.0.1 224.0.0.2 224.0.0.22 224.0.0.13
            #       224.0.0.5  <----- this extra line
            if read_multicast_reserved_lines:
                if not re.match(r"[^\d. ]", line):
                    p41_1 = re.compile(r'(?P<multicast_groups>\d+\.\d+\.\d+\.\d+)')
                    m = p41_1.findall(line)
                    multicast_groups.extend(m)
                    continue
                else:
                    interface_dict[interface]['multicast_groups'] \
                        = sorted(interface_dict[interface]['multicast_groups'])
                    read_multicast_reserved_lines = False

            # Outgoing Common access list is not set
            p7 = re.compile(r'^Outgoing +Common +access +list +is +'
                            r'(?P<access_list>.+)$')
            m = p7.match(line)
            if m:
                if 'not set' not in m.groupdict()['access_list']:
                    interface_dict[interface]['outbound_common_access_list'] = \
                        m.groupdict()['access_list']
                continue

            # Outgoing access list is not set
            p8 = re.compile(r'^Outgoing +access +list +is +'
                            r'(?P<access_list>.+)$')
            m = p8.match(line)
            if m:
                if 'not set' not in m.groupdict()['access_list']:
                    interface_dict[interface]['outbound_access_list'] = \
                        m.groupdict()['access_list']
                continue

            # Inbound Common access list is not set
            p9 = re.compile(r'^Inbound +Common +access +list +is +'
                            r'(?P<access_list>.+)$')
            m = p9.match(line)
            if m:
                if 'not set' not in m.groupdict()['access_list']:
                    interface_dict[interface]['inbound_common_access_list'] = \
                        m.groupdict()['access_list']
                continue

            # Inbound  access list is not set
            p10 = re.compile(r'^Inbound +access +list +is +'
                            r'(?P<access_list>.+)$')
            m = p10.match(line)
            if m:
                if 'not set' not in m.groupdict()['access_list']:
                    interface_dict[interface]['inbound_access_list'] = \
                        m.groupdict()['access_list']
                continue

            # Proxy ARP is enabled
            p11 = re.compile(r'^Proxy +ARP +is +'
                            r'(?P<status>\w+)$')
            m = p11.match(line)
            if m:
                if 'disabled' in m.groupdict()['status']:
                    interface_dict[interface]['proxy_arp'] = False
                else:
                    interface_dict[interface]['proxy_arp'] = True
                continue

            # Local Proxy ARP is disabled
            p12 = re.compile(r'^Local +Proxy +ARP +is +'
                            r'(?P<status>\w+)$')
            m = p12.match(line)
            if m:
                if 'disabled' in m.groupdict()['status']:
                    interface_dict[interface]['local_proxy_arp'] = False
                else:
                    interface_dict[interface]['local_proxy_arp'] = True
                continue

            # Security level is default
            p13 = re.compile(r'^Security +level +is +'
                            r'(?P<level>\w+)$')
            m = p13.match(line)
            if m:
                interface_dict[interface]['security_level'] = m.groupdict()['level']
                continue

            # Split horizon is enabled
            p14 = re.compile(r'^Split +horizon +is +'
                            r'(?P<status>\w+)$')
            m = p14.match(line)
            if m:
                if 'disabled' in m.groupdict()['status']:
                    interface_dict[interface]['split_horizon'] = False
                else:
                    interface_dict[interface]['split_horizon'] = True
                continue

            # ICMP redirects are always sent
            p15 = re.compile(r'^ICMP +redirects +are +'
                            r'(?P<sent>[\w\s]+)$')
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
                             r'(?P<sent>[\w\s]+)$')
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
                             r'(?P<sent>[\w\s]+)$')
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
                             r'(?P<status>\w+)$')
            m = p18.match(line)
            if m:
                if 'disabled' in m.groupdict()['status']:
                    interface_dict[interface]['ip_fast_switching'] = False
                else:
                    interface_dict[interface]['ip_fast_switching'] = True
                continue

            # IP Flow switching is disabled
            p19 = re.compile(r'^IP +Flow +switching +is +'
                             r'(?P<status>\w+)$')
            m = p19.match(line)
            if m:
                if 'disabled' in m.groupdict()['status']:
                    interface_dict[interface]['ip_flow_switching'] = False
                else:
                    interface_dict[interface]['ip_flow_switching'] = True
                continue

            # IP CEF switching is enabled
            p20 = re.compile(r'^IP +CEF +switching +is +'
                             r'(?P<status>\w+)$')
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
                            r'operation +state +is +(?P<topo_status>\w+)$')
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
                             r'(?P<status>\w+)$')
            m = p25.match(line)
            if m:
                if 'disabled' in m.groupdict()['status']:
                    interface_dict[interface]['ip_multicast_fast_switching'] = False
                else:
                    interface_dict[interface]['ip_multicast_fast_switching'] = True
                continue

            # IP multicast distributed fast switching is disabled
            p25 = re.compile(r'^IP +multicast +distributed +fast +switching +is +'
                             r'(?P<status>\w+)$')
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
                             r'(?P<status>\w+)$')
            m = p27.match(line)
            if m:
                if 'disabled' in m.groupdict()['status']:
                    interface_dict[interface]['router_discovery'] = False
                else:
                    interface_dict[interface]['router_discovery'] = True
                continue

            # IP output packet accounting is disabled
            p28 = re.compile(r'^IP +output +packet +accounting +is +'
                             r'(?P<status>\w+)$')
            m = p28.match(line)
            if m:
                if 'disabled' in m.groupdict()['status']:
                    interface_dict[interface]['ip_output_packet_accounting'] = False
                else:
                    interface_dict[interface]['ip_output_packet_accounting'] = True
                continue

            # IP access violation accounting is disabled
            p29 = re.compile(r'^IP +access +violation +accounting +is +'
                             r'(?P<status>\w+)$')
            m = p29.match(line)
            if m:
                if 'disabled' in m.groupdict()['status']:
                    interface_dict[interface]['ip_access_violation_accounting'] = False
                else:
                    interface_dict[interface]['ip_access_violation_accounting'] = True
                continue

            # TCP/IP header compression is disabled
            p30 = re.compile(r'^TCP\/IP +header +compression +is +'
                             r'(?P<status>\w+)$')
            m = p30.match(line)
            if m:
                if 'disabled' in m.groupdict()['status']:
                    interface_dict[interface]['tcp_ip_header_compression'] = False
                else:
                    interface_dict[interface]['tcp_ip_header_compression'] = True
                continue

            # RTP/IP header compression is disabled
            p31 = re.compile(r'^RTP\/IP +header +compression +is +'
                             r'(?P<status>\w+)$')
            m = p31.match(line)
            if m:
                if 'disabled' in m.groupdict()['status']:
                    interface_dict[interface]['rtp_ip_header_compression'] = False
                else:
                    interface_dict[interface]['rtp_ip_header_compression'] = True
                continue

            # Probe proxy name replies are disabled
            p32 = re.compile(r'^Probe +proxy +name +replies +are +'
                             r'(?P<status>\w+)$')
            m = p32.match(line)
            if m:
                if 'disabled' in m.groupdict()['status']:
                    interface_dict[interface]['probe_proxy_name_replies'] = False
                else:
                    interface_dict[interface]['probe_proxy_name_replies'] = True
                continue

            # Policy routing is disabled
            p33 = re.compile(r'^Policy +routing +is +'
                             r'(?P<status>\w+)$')
            m = p33.match(line)
            if m:
                if 'disabled' in m.groupdict()['status']:
                    interface_dict[interface]['policy_routing'] = False
                else:
                    interface_dict[interface]['policy_routing'] = True
                continue

            # Network address translation is disabled
            p34 = re.compile(r'^Network +address +translation +is +'
                             r'(?P<status>\w+)$')
            m = p34.match(line)
            if m:
                if 'disabled' in m.groupdict()['status']:
                    interface_dict[interface]['network_address_translation'] = False
                else:
                    interface_dict[interface]['network_address_translation'] = True
                continue

            # BGP Policy Mapping is disabled
            p35 = re.compile(r'^BGP +Policy +Mapping +is +'
                             r'(?P<status>\w+)$')
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
                             r'(?P<unnumbered_intf>[\w\/\-\.]+) +'
                             r'\((?P<unnumbered_ip>[\w\.\:]+)\)$')
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
                                m = re.search(r'([\w\.\:]+)\/(\d+)', address)
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
                            Optional('suppress'): bool,
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
    cli_command = [
        'show ipv6 interface',
        'show ipv6 interface {interface}',
        'show ipv6 interface | include {include}'
    ]

    def cli(self, interface='', include=None, output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[1].format(interface=interface)
            elif include:
                cmd = self.cli_command[2].format(include=include)
            else:
                cmd = self.cli_command[0]
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
            p1 =  re.compile(r'^(?P<interface>[\w\/\.\-\:]+) +is'
                             r' +(?P<enabled>[\w\s]+),'
                             r' +line +protocol +is +(?P<oper_status>\w+)$')
            m = p1.match(line)
            if m:
                intf = m.groupdict()['interface']
                enabled = m.groupdict()['enabled'].lower()
                if intf not in ret_dict:
                    ret_dict[intf] = {}
                if 'administratively down' in enabled:
                    ret_dict[intf]['enabled'] = False
                else:
                    ret_dict[intf]['enabled'] = True

                ret_dict[intf]['oper_status'] = \
                    m.groupdict()['oper_status'].lower()

                # initial list variable again for new interface
                joined_group = []
                continue

            # IPv6 is enabled, link-local address is FE80::257:D2FF:FE28:
            # IPv6 is tentative, link-local address is FE80::257:D2FF:FEFF:428C [TEN]
            # IPv6 is tentative, link-local address is FE80::257:D2FF:FEFF:428C [UNA/TEN]
            p2 = re.compile(r'^IPv6 +is +(?P<status>\w+), +'
                             r'link-local +address +is +(?P<link_local>[\w\:]+)'
                             r'( *\[(?P<type>[\w\/]+)\])?$')
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
            p21 = re.compile(r'^Virtual +link\-local +address\(es\)\:$')
            m = p21.match(line)
            if m:
                ipv6 = True
                continue

            p21_1 = re.compile(r'^(?P<ipv6>[\w\:]+)'
                                r'( *\[(?P<type>[\w\/]+)\])?$')
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
            p3 = re.compile(r'^Stateless +address +autoconfig +enabled$')
            m = p3.match(line)
            if m:
                ret_dict[intf]['autoconf'] = True
                continue

            # Global unicast address(es):
            #   2001:10::14:1, subnet is 2001:10::14:0/112
            #   2001:DB8:3:3::3, subnet is 2001:DB8:3:3::/64 [ANY/TEN]
            p4 = re.compile(r'^Global +unicast +address\(es\):$')
            m = p4.match(line)
            if m:
                ipv6 = True
                continue

            p4_1 = re.compile(r'^(?P<ipv6>[\w\:]+), +subnet +is +(?P<dum1>(?P<dum2>[\w\:]+)'
                               r'\/(?P<prefix_length>[0-9]+))'
                               r'( *\[(?P<type>[\w\/]+)\])?$')
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
            p4_2 = re.compile(r'^valid +lifetime +(?P<valid>\d+) +'
                               r'preferred +lifetime +(?P<preferred>\d+)$')
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
            p5 = re.compile(r'^Joined +group +address\(es\):$')
            m = p5.match(line)
            if m:
                ipv6 = False
                continue

            p5_1 = re.compile(r'^(?P<address>[\w\:]+)$')
            m = p5_1.match(line)
            if m and not ipv6:
                joined_group.append(m.groupdict()['address'])
                ret_dict[intf]['joined_group_addresses'] = sorted(joined_group)
                continue

            # MTU is 1500 bytes
            p6 = re.compile(r'^MTU +is +(?P<mtu>\d+) +bytes$')
            m = p6.match(line)
            if m:
                ret_dict[intf]['mtu'] = int(m.groupdict()['mtu'])
                continue

            # VPN Routing/Forwarding "VRF1"
            p6 = re.compile(r'^VPN +Routing\/Forwarding +\"(?P<vrf>[\w\-]+)\"$')
            m = p6.match(line)
            if m:
                ret_dict[intf]['vrf'] = m.groupdict()['vrf']
                continue

            # ICMP error messages limited to one every 100 milliseconds
            p7 = re.compile(r'^ICMP +error +messages +limited +to +one +'
                             r'every +(?P<limited>\d+) +milliseconds$')
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
            p8 = re.compile(r'^ICMP +redirects +are +(?P<status>\w+)$')
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
            p9 = re.compile(r'^ICMP +unreachables +are +(?P<status>[\w\s]+)$')
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
            p10 = re.compile(r'^ND +DAD +is +(?P<status>\w+), +'
                              r'number +of +DAD +attempts: +(?P<attempts>\d+)$')
            m = p10.match(line)
            if m:
                nd_dict = ret_dict.setdefault(intf, {}).setdefault('ipv6', {}).setdefault('nd', {})
                nd_dict.setdefault('suppress', False)

                if 'enabled' in m.groupdict()['status']:
                    nd_dict['dad_enabled'] = True
                else:
                    nd_dict['dad_enabled'] = False

                nd_dict['dad_attempts'] = int(m.groupdict()['attempts'])
                continue

            # ND reachable time is 30000 milliseconds (using 30000)
            p11 = re.compile(r'^ND +reachable +time +is (?P<time>\d+) +milliseconds'
                              r' +\(using +(?P<use>\d+)\)$')
            m = p11.match(line)
            if m:
                nd_dict = ret_dict.setdefault(intf, {}).setdefault('ipv6', {}).setdefault('nd', {})
                nd_dict.setdefault('suppress', False)
                nd_dict['reachable_time'] = int(m.groupdict()['time'])
                nd_dict['using_time'] = int(m.groupdict()['use'])
                continue

            # ND NS retransmit interval is 1000 milliseconds
            p12 = re.compile(r'^ND +NS +retransmit +interval +is'
                              r' +(?P<interval>\d+) +milliseconds$')
            m = p12.match(line)
            if m:
                nd_dict = ret_dict.setdefault(intf, {}).setdefault('ipv6', {}).setdefault('nd', {})
                nd_dict.setdefault('suppress', False)
                nd_dict['ns_retransmit_interval'] = int(m.groupdict()['interval'])
                continue

            # ND advertised reachable time is 0 (unspecified)
            p13 = re.compile(r'^ND +advertised +reachable +time +is +(?P<time>\d+)'
                              r' +\((?P<dummy>\S+)\)$')
            m = p13.match(line)
            if m:
                nd_dict = ret_dict.setdefault(intf, {}).setdefault('ipv6', {}).setdefault('nd', {})
                nd_dict.setdefault('suppress', False)
                nd_dict['advertised_reachable_time'] = int(m.groupdict()['time'])
                if m.groupdict()['dummy'] == 'unspecified':
                    nd_dict['advertised_reachable_time_unspecified'] = True
                else:
                    nd_dict['advertised_reachable_time_unspecified'] = False
                continue

            # ND advertised retransmit interval is 0 (unspecified)
            p14 = re.compile(r'^ND +advertised +retransmit +interval +is +(?P<time>\d+)'
                              r' +\((?P<dummy>\S+)\)$')
            m = p14.match(line)
            if m:
                nd_dict = ret_dict.setdefault(intf, {}).setdefault('ipv6', {}).setdefault('nd', {})
                nd_dict.setdefault('suppress', False)
                nd_dict['advertised_retransmit_interval'] = int(m.groupdict()['time'])
                if m.groupdict()['dummy'] == 'unspecified':
                    nd_dict['advertised_retransmit_interval_unspecified'] = True
                else:
                    nd_dict['advertised_retransmit_interval_unspecified'] = False
                continue

            # ND router advertisements are sent every 200 seconds
            p15 = re.compile(r'^ND +router +advertisements +are +sent +'
                              r'every +(?P<time>\d+) +seconds$')
            m = p15.match(line)
            if m:
                nd_dict = ret_dict.setdefault(intf, {}).setdefault('ipv6', {}).setdefault('nd', {})
                nd_dict.setdefault('suppress', False)
                nd_dict['router_advertisements_interval'] = int(m.groupdict()['time'])
                continue

            # ND router advertisements live for 1800 seconds
            p16 = re.compile(r'^ND +router +advertisements +live +for +'
                              r'(?P<time>\d+) +seconds$')
            m = p16.match(line)
            if m:
                nd_dict = ret_dict.setdefault(intf, {}).setdefault('ipv6', {}).setdefault('nd', {})
                nd_dict.setdefault('suppress', False)
                nd_dict['router_advertisements_live'] = int(m.groupdict()['time'])
                continue

            # ND advertised default router preference is Medium
            p17 = re.compile(r'^ND +advertised +default +router +preference +'
                              r'is +(?P<prefer>\w+)$')
            m = p17.match(line)
            if m:
                nd_dict = ret_dict.setdefault(intf, {}).setdefault('ipv6', {}).setdefault('nd', {})
                nd_dict.setdefault('suppress', False)
                nd_dict['advertised_default_router_preference'] = m.groupdict()['prefer']
                continue

            # ND RAs are suppressed (periodic)
            p17_1 = re.compile(r'^ND +RAs +are +suppressed.*$')
            m = p17_1.match(line)
            if m:
                nd_dict = ret_dict.setdefault(intf, {}).setdefault('ipv6', {}).setdefault('nd', {})
                nd_dict.update({'suppress': True})
                continue

            # Hosts use stateless autoconfig for addresses.
            p18 = re.compile(r'^Hosts +use +(?P<addr_conf_method>[\w\s]+) +for +addresses.$')
            m = p18.match(line)
            if m:
                ret_dict[intf]['addresses_config_method'] = \
                    m.groupdict()['addr_conf_method']
                continue

            # Hosts use DHCP to obtain routable addresses.
            p18_1 = re.compile(r'^Hosts +use +(?P<addr_conf_method>[\w\s]+) +to +obtain +routable +addresses.$')
            m = p18_1.match(line)
            if m:
                ret_dict[intf]['addresses_config_method'] = \
                    m.groupdict()['addr_conf_method']
                continue

            # Interface is unnumbered. Using address of Loopback0
            p19 = re.compile(r'^Interface +is +unnumbered. +Using +address +of'
                              r' +(?P<unnumbered_intf>[\w\/\.]+)$')
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
            p20 = re.compile(r'^No +global +unicast +address +is +configured$')
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
        p1 = re.compile(r'^(?P<name>[\w\-\/\.]+) +(?P<mode>\w+) +(?P<encapsulation>\S+) +'
                         r'(?P<status>\w+) +(?P<native_vlan>\d+)$')
        p2 = re.compile(r'^Port +Vlans +allowed +on +trunk$')
        p3 = re.compile(r'^Port +Vlans +allowed +and +active +in +management +domain$')
        p4 = re.compile(r'^Port +Vlans +in +spanning +tree +forwarding +state +and +not +pruned$')
        p5 = re.compile(r'^(?P<name>[\w\-\/\.]+) +(?P<vlans>none\s*|[\d\-\,\s]+)$')
        # initial variables
        ret_dict = {}
        vlan_list_type = None

        for line in out.splitlines():
            line = line.strip()

            # Gi1/0/4     on               802.1q         trunking      1
            # Gi1/0/4     auto             n-isl          trunking      1
            # Gi1/0/23    on               isl            trunking      1
            # Gi1/0/24    on               802.1q         trunking      1
            # Po12        auto             n-802.1q       trunking      1
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
                         r'(?P<mcast_pkts>\d+) +(?P<bcast_pkts>\d+)$')
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

class ShowInterfacesCountersEtherchannel(ShowInterfacesCounters):
    """parser for show interfaces <WORD> counter etherchannel"""

    cli_command = 'show interfaces {interface} counter etherchannel'

    def cli(self, interface,output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(interface=interface))

        return super().cli(interface=interface, output=output)

class ShowInterfacesAccountingSchema(MetaParser):
    """Schema for show interfaces accounting"""
    schema = {
        Any(): {
            Optional('description'): str,
            'accounting': {
                Any(): {
                    'pkts_in': int,
                    'pkts_out': int,
                    'chars_in': int,
                    'chars_out': int,
                    Optional('rxbs'): int,
                    Optional('rxps'): int,
                    Optional('txbs'): int,
                    Optional('txps'): int
                }
            }
        }
    }


class ShowInterfacesAccounting(ShowInterfacesAccountingSchema):
    """Parser for:
        show interfaces accounting
        show interfaces <interface> accounting
    """
    cli_command = [
        'show interfaces {interface} accounting', 'show interfaces accounting'
    ]
    exclude = [
        'pkts_in', 'pkts_out', 'chars_in', 'chars_out', 'rxbs', 'rxps', 'txbs',
        'txps'
    ]

    def cli(self, interface=None, output=None):
        if output is None:
            if not interface:
                cmd = self.cli_command[1]
            else:
                cmd = self.cli_command[0].format(interface=interface)
            out = self.device.execute(cmd)
        else:
            out = output

        # initial return disctionary
        ret_dict = {}

        # initial regexp pattern
        # GigabitEthernet0/0/0/0
        # GigabitEthernet11 OOB Net
        # (need to exclude below line)
        # -------------------------------------------------------------------------------------------------------------------------
        p1 = re.compile(
            r'^(?!-)(?P<interface>[a-zA-Z\-\d\/\.]+)(?P<description>( (\S)+)*)$'
        )

        # Tunnel0 Pim Register Tunnel (Encap) for RP 10.186.1.1
        p1_1 = re.compile(
            r'^(?P<interface>Tunnel\d+) +Pim +Register +Tunnel +\(Encap\) +for +RP +(?P<rp>[\w\.]+)$'
        )

        #   IPV4_UNICAST             9943           797492           50             3568
        #   DEC MOP          2        154          2        154
        #   Other           15          900          861       370708           0            0            0            0
        p2 = re.compile(
            r'^(?P<protocol>\S+(\s\S+)?)\s+(?P<pkts_in>\d+)\s+(?P<chars_in>\d+)\s+(?P<pkts_out>\d+)\s+(?P<chars_out>\d+)(\s+(?P<rxbs>\d+)\s+(?P<rxps>\d+)\s+(?P<txbs>\d+)\s+(?P<txps>\d+))?'
        )

        # No traffic sent or received on this interface.
        p3 = re.compile(
            r'^No +traffic +sent +or +received +on +this +interface\.$')

        for line in out.splitlines():
            if line:
                line = line.strip()
            else:
                continue

            m = p3.match(line)
            if m:
                continue

            # GigabitEthernet0/0/0/0
            # GigabitEthernet11 OOB Net
            # (need to exclude below line)
            # -------------------------------------------------------------------------------------------------------------------------
            m = p1.match(line)
            if m:
                intf = m.groupdict()['interface']
                description = m.groupdict()['description']
                continue

            #   IPV4_UNICAST             9943           797492           50             3568
            #   DEC MOP          2        154          2        154
            #   Other           15          900          861       370708           0            0            0            0
            m = p2.match(line)
            if m:
                protocol_dict = m.groupdict()
                protocol = protocol_dict.pop('protocol').lower().strip()
                ret_dict.setdefault(intf, {}).\
                    setdefault('accounting', {}).setdefault(protocol, {})
                ret_dict[intf]['accounting'][protocol].update({k: int(v) \
                    for k, v in protocol_dict.items() if v is not None})
                if description:
                    ret_dict[intf].setdefault('description',
                                              description.strip())
                continue

        return ret_dict

# ====================================================
#  schema for show interfaces link
# ====================================================
class ShowInterfacesLinkSchema(MetaParser):
    """Schema for:
        show interfaces link
        show interfaces {interface} link"""

    schema = {
        'interfaces': {
            Any(): {
                Optional('name'): str,
                'down_time': str,
                Optional('up_time'): str,
            }
        }
    }


# ====================================================
#  parser for show interfaces link
# ====================================================
class ShowInterfacesLink(ShowInterfacesLinkSchema):
    """parser for
            * show interfaces link
            * show interfaces {interface} link
        """

    cli_command = ['show interfaces link',
                   'show interfaces {interface} link']

    def cli(self, interface=None, output=None):
        if output is None:
            if interface:
                out = self.device.execute(self.cli_command[1].format(interface=interface))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        result_dict = {}

        # Port           Name               Down Time      Up Time
        # Gi1/0/1        Foo                 00:00:00       4w5d
        # Gi1/0/2        foo bar             00:07:00

        p1 = re.compile(r'^(?P<interface>\S+)'
                        r'(?:(?P<name>.+?(?=(\d+[dw]\d+[dh])|(\d{2}:\d{2}:\d{2}))))?'
                        r'(?P<down_time>(\d+[dw]\d+[dh])|(\d{2}:\d{2}:\d{2}))'
                        r'(?:\s+(?P<up_time>(\d+[dw]\d+[dh])|(\d{2}:\d{2}:\d{2})))?$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)

            if m:
                group = m.groupdict()

                intf_dict = result_dict.setdefault('interfaces', {}).\
                                        setdefault(Common.convert_intf_name(group['interface']), {})

                name_val = group['name'].strip()
                if len(name_val):
                    intf_dict['name'] = name_val

                keys = ['down_time',
                        'up_time']

                for k in keys:
                    if group[k]:
                        intf_dict[k] = group[k].strip()
                continue

        return result_dict


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
    exclude = ['chars_in' , 'chars_out', 'pkts_in', 'pkts_out']

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
                        r' +(?P<pkts_out>[\d]+) +(?P<chars_out>[\d]+)$')

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


# ====================================================
#  parser for show interfaces description
# ====================================================
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
    """parser for show interfaces description
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

        #Interface                      Status         Protocol Description
        #Gi0/0                          up             up
        #Gi0/1                          admin down     down     to router2
        p1 = re.compile(r'(?P<interface>(\S+)) +(?P<status>(\S+)([\s+](\S+))?) +(?P<protocol>(\S+))(?: +(?P<description>(.*)))?$')

        for line in out.splitlines():
            line = line.strip()
            #Interface                      Status         Protocol Description
            #Gi0/0                          up             up
            #Gi0/1                          admin down     down     to router2
            m = p1.match(line)
            if m and m.groupdict()['protocol'] != 'Protocol':
                group = m.groupdict()
                interface = Common.convert_intf_name(group['interface'])
                intf_dict = result_dict.setdefault('interfaces', {}).setdefault(interface, {})
                intf_dict['status'] = group['status']
                intf_dict['protocol'] = group['protocol']
                if group['description'] is not None:
                    intf_dict['description'] = str(group['description'])
                else:
                    intf_dict['description'] = ""
                index += 1
                continue

        return result_dict


# =====================================
#  schema for "show interfaces status"
# =====================================
class ShowInterfacesStatusSchema(MetaParser):
    """Schema for:
        * show interfaces status
        * show interfaces {interface} status
    """

    schema = {
        'interfaces': {
            Any(): {
                Optional('name'): str,
                'status': str,
                'vlan': str,
                'duplex_code': str,
                'port_speed': str,
                Optional('type'): str,
            }
        }
    }


# ====================================================
#  parser for show interfaces status
# ====================================================
class ShowInterfacesStatus(ShowInterfacesStatusSchema):
    """parser for
            * show interfaces status
            * show interfaces {interface} status
        """

    cli_command = ['show interfaces status',
                   'show interfaces {interface} status']

    def cli(self, interface="", output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[1].format(interface=interface)
            else:
                cmd = self.cli_command[0]
            output = self.device.execute(cmd)

        result_dict = {}

        # Port      Name               Status       Vlan       Duplex  Speed Type
        # Gi1/2     TelenlqPOIU        notconnect   125          full    100 10/100/1000-TX
        # Gi1/3     SE                 connected    132        a-full a-1000 10/100/1000-TX
        # Gi1/7                        notconnect   99           auto   auto 10/100/1000-TX
        # Gi1/10    To cft123          connected    trunk      a-full a-1000 10/100/1000-TX
        # Gi1/1/0/1 FAST-HELLO         connected    4094       a-full a-1000 10/100/1000BaseTX
        # Te1/1/2   VSL                connected    trunk        full  a-10G 10GBase-SR
        # Te2/1/20                     disabled     1            full   auto No XCVR
        # Te2/1/21  VSL LINK1          disabled     1            full   auto No XCVR
        # Po10      VSL LINK2          connected    trunk      a-full  a-10G

        p1 = re.compile(r'^(?P<interfaces>\S+)(?:\s+(?P<name>([\S\s]+)))?'
                        r'\s+(?P<status>(connected|notconnect|suspended|inactive|disabled|err-disabled|monitoring))'
                        r'\s+(?P<vlan>\S+)\s+(?P<duplex_code>[\S\-]+)\s+(?P<port_speed>[\S\-]+)(\s+(?P<type>.+))?$')

        for line in output.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:

                group = m.groupdict()

                intf_dict = result_dict.setdefault('interfaces', {}).\
                                        setdefault(Common.convert_intf_name(group['interfaces']), {})

                name_val = group['name'].strip()
                if len(name_val)>0 :
                    intf_dict['name'] = name_val

                keys = ['status',
                        'vlan', 'duplex_code', 'port_speed',
                        'type']

                for k in keys:
                    if group[k]:
                        intf_dict[k] = group[k].strip()
                continue

        return result_dict


# ====================================================
#  schema for show interfaces status err-disabled
# ====================================================
class ShowInterfacesStatusErrDisabledSchema(MetaParser):
    """Schema for:
        show interfaces status err-disabled"""

    schema = {
        'interfaces': {
            Any(): {
                Optional('name'): str,
                'status': str,
                'reason': str,
                Optional('err_disabled_vlans'): str
            }
        }
    }


# ====================================================
#  parser for show interfaces status err-disabled
# ====================================================
class ShowInterfacesStatusErrDisabled(ShowInterfacesStatusErrDisabledSchema):
    """parser for
            * show interfaces status err-disabled
        """

    cli_command = 'show interfaces status err-disabled'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        # Fi1/7/0/13     Hello World  err-disabled loopdetect
        # Fi1/7/0/14                  err-disabled loopdetect
        p1= re.compile(r'^(?P<interfaces>\S+)\s+(?P<name>.+?)?\s+(?P<status>err-disabled)\s+(?P<reason>\S+)\s*(?P<err_disabled_vlans>.*)$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                intf_dict = ret_dict.setdefault('interfaces', {}).\
                                        setdefault(Common.convert_intf_name(group['interfaces']), {})

                # Update intf_dict, ignore None or '' empty values. Ignore 'interfaces' key
                intf_dict.update({k:v for k, v in group.items() if v and k != 'interfaces'})
                continue

        return ret_dict
# ==========================================================
#  Parser for show interface {interface} transceiver detail
# ==========================================================
class ShowInterfacesTransceiverDetailSchema(MetaParser):
    """Schema for:
        show interfaces {interface} transceiver detail"""

    schema = {
        'interfaces': {
            Any(): {  # interface name
                Optional('transceiver'): str,
                Optional('type'): str,
                Optional('name'): str,
                Optional('part_number'): str,
                'Temperature': {
                    'Value': Or(float, str),
                    Optional('Lane'): str,
                    'HighAlarmThreshold': float,
                    'HighWarnThreshold': float,
                    'LowWarnThreshold': float,
                    'LowAlarmThreshold': float
                },
                'Voltage': {
                    'Value': Or(float, str),
                    Optional('Lane'): str,
                    'HighAlarmThreshold': float,
                    'HighWarnThreshold': float,
                    'LowWarnThreshold': float,
                    'LowAlarmThreshold': float
                },
                'Current': {
                    'Value': Or(float, str),
                    Optional('Lane'): str,
                    'HighAlarmThreshold': float,
                    'HighWarnThreshold': float,
                    'LowWarnThreshold': float,
                    'LowAlarmThreshold': float
                },
                'OpticalTX': {
                    'Value': Or(float, str),
                    Optional('Lane'): str,
                    'HighAlarmThreshold': float,
                    'HighWarnThreshold': float,
                    'LowWarnThreshold': float,
                    'LowAlarmThreshold': float
                },
                'OpticalRX': {
                    'Value': Or(float, str),
                    Optional('Lane'): str,
                    'HighAlarmThreshold': float,
                    'HighWarnThreshold': float,
                    'LowWarnThreshold': float,
                    'LowAlarmThreshold': float
                },
            }
        }
    }


class ShowInterfacesTransceiverDetail(ShowInterfacesTransceiverDetailSchema):
    """parser for
            * show interfaces transceiver detail
            * show interfaces {interface} transceiver detail
        """

    cli_command = ['show interfaces {interface} transceiver detail',
                   'show interfaces transceiver detail']

    def cli(self, interface=None, output=None):
        if output is None:
            if interface:
                out = self.device.execute(self.cli_command[0].format(interface=interface))
            else:
                out = self.device.execute(self.cli_command[1])
        else:
            out = output

        # transceiver is present
        # type is 10Gbase-LR
        # name is CISCO-FINISAR
        # part number is FTLX1474D3BCL-CS
        p1 = re.compile(r'^(?P<key>[Tt]ransceiver|[Tt]ype|[Nn]ame|[Pp]art +[Nn]umber) +is +(?P<value>[\S\s]+)$')

        # Voltage            Threshold   Threshold  Threshold  Threshold
        p3_0 = re.compile(r'(?P<statistic>(Temperature|Voltage|Current|Transmit Power|Receive Power)) +Threshold +Threshold +Threshold +Threshold$')

        # Twe2/1/1     25.5                   90.0       85.0       -5.0      -10.0
        # Twe2/1/1   N/A    5.7                 50.0       40.0        2.0        1.0
        # Twe2/1/1   N/A    N/A                 50.0       40.0        2.0        1.0
        p3_1 = re.compile(r'^(?P<port>(\S+)) +(?P<lane>(\S+))? +(?P<value>(\S+)) '
                          r'+(?P<HAT>(-?[\d\.]+)) +(?P<HWT>(-?[\d\.]+)) +(?P<LWT>(-?[\d\.]+)) +(?P<LAT>(-?[\d\.]+))$')

        result_dict = {}
        is_dict = {}
        stat = None
        for line in out.splitlines():
            line = line.strip()

            # transceiver is present
            # type is 10Gbase-LR
            m = p1.match(line)
            if m:
                group = m.groupdict()
                key = group['key'].lower().replace('the', '').strip()
                key = key.replace(' ', '_')
                value = group['value'].strip()
                is_dict[key] = value
                continue

            m = p3_0.match(line)
            if m:
                stat = m.groupdict()['statistic']
                if stat == 'Transmit Power':
                    stat = 'OpticalTX'
                elif stat == 'Receive Power':
                    stat = 'OpticalRX'
                continue

            if stat:
                m = p3_1.match(line)
                if m:
                    interface = m.groupdict()['port']
                    interface = Common.convert_intf_name(interface)
                    intf_dict = result_dict.setdefault('interfaces', {}).setdefault(interface, {})

                    intf_dict.update(is_dict)
                    is_dict = {}

                    intf_dict[stat] = {}
                    try:
                        intf_dict[stat]['Value'] = float(m.groupdict()['value'])
                    except ValueError:
                        intf_dict[stat]['Value'] = m.groupdict()['value']

                    if m.groupdict()['lane'] is not None:
                        intf_dict[stat]['Lane'] = m.groupdict()['lane']
                    intf_dict[stat]['HighAlarmThreshold'] = float(m.groupdict()['HAT'])
                    intf_dict[stat]['HighWarnThreshold'] = float(m.groupdict()['HWT'])
                    intf_dict[stat]['LowWarnThreshold'] = float(m.groupdict()['LWT'])
                    intf_dict[stat]['LowAlarmThreshold'] = float(m.groupdict()['LAT'])
                    continue
        return result_dict


# ==========================================================
#  Parser for show interface {interface} transceiver
# ==========================================================
class ShowInterfacesTransceiverSchema(MetaParser):
    """Schema for:
        * show interfaces {interface} transceiver
    """

    schema = {
        'interfaces': {
            Any(): {  # interface name
                Optional('port'): str,
                Optional('temp'): str,
                Optional('voltage'): str,
                Optional('current'): str,
                Optional('opticaltx'): str,
                Optional('opticalrx'): str,
                Optional('max_power'): str
            }
        }
    }


class ShowInterfacesTransceiver(ShowInterfacesTransceiverSchema):
    """
    parser for
        * show interfaces transceiver
        * show interfaces {interface} transceiver
    """

    cli_command = ['show interfaces {interface} transceiver', 'show interfaces transceiver']

    def cli(self, interface=None, output=None):
        if output is None:
            if interface:
                out = self.device.execute(self.cli_command[0].format(interface=interface))
            else:
                out = self.device.execute(self.cli_command[1])

        else:
            out = output

        # Gi1/1      40.6       5.09       0.4     -25.2      N/A
        # Gi1/1      40.6       5.09       0.4     -25.2      -31.00    Max
        p = re.compile(r'^(?P<port>([\d\/A-Za-z]+)) +(?P<temp>([\d\.-]+)) '
                        r'+(?P<voltage>([\d\.-]+)) +(?P<current>([\d\.-]+)) '
                        r'+(?P<opticaltx>(\S+)) +(?P<opticalrx>(\S+))(\s+(?P<max_power>.*))?$')

        result_dict = {}
        for line in out.splitlines():
            line = line.strip()

            m = p.match(line)
            if m:
                group = m.groupdict()
                intf_dict = result_dict.setdefault('interfaces', {}).setdefault(group['port'], {})
                intf_dict['temp'] = group['temp']
                intf_dict['voltage'] = group['voltage']
                intf_dict['current'] = group['current']
                intf_dict['opticaltx'] = group['opticaltx']
                intf_dict['opticalrx'] = group['opticalrx']
                if group['max_power']:
                    intf_dict['max_power'] = group['max_power']
                continue

        return result_dict


# ====================================================
#  schema for show macro auto interfaces
# ====================================================
class ShowMacroAutoInterfaceSchema(MetaParser):
    """Schema for:
        show macro auto interface"""

    schema = {
        'asp_status': str,
        'fallback': {
            'type': str,
            'status': str
        },
        'interfaces': {
            Any(): {
                'asp': str,
                'fallback': str,
                'macro': str
            },
        }
    }
# ==========================================================
#  Parser for show macro auto interface
# ==========================================================
class ShowMacroAutoInterface(ShowMacroAutoInterfaceSchema):
    """
    parser for
            * show macro auto interface
    """

    cli_command = ['show macro auto interface {interface}', 'show macro auto interface']

    def cli(self, interface=None, output=None):
        if output is None:
            if interface:
                out = self.device.execute(self.cli_command[0].format(interface=interface))
            else:
                out = self.device.execute(self.cli_command[1])
        else:
            out = output

        ret_dict = {}

        # Auto Smart Ports Enabled
        p1 = re.compile(r'^Auto Smart Ports+\s(?P<asp_status>\S+)')
        # Fallback : CDP  Disabled
        p2 = re.compile(r'Fallback :\s+(?P<type>\S+)\s+(?P<status>\S+)')
        # Gi2/0/21      TRUE              None        CISCO_IPVSC_EVENT
        p3 = re.compile(
            r'^(?P<interface>\S+\d+\/\d+\/\d+|\S+)\s+(?P<asp>\w+)\s\s+(?P<fallback>\w+)\s+(?P<macro>\S+|\S+(?:\s+)?\S+(?:\s+)?\S+)$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['asp_status'] = group['asp_status']

            m = p2.match(line)
            if m:
                group = m.groupdict()
                fallback_dict = ret_dict.setdefault('fallback',{})
                fallback_dict['type'] = group['type']
                fallback_dict['status'] = group['status']


            m = p3.match(line)
            if m:
                group = m.groupdict()
                interface = Common.convert_intf_name\
                        (intf=group['interface'].strip())
                intf_dict = ret_dict.setdefault('interfaces', {}).setdefault(interface, {})
                intf_dict['asp'] = group['asp']
                intf_dict['fallback'] = group['fallback']
                intf_dict['macro'] = group['macro']

        return ret_dict
# =============================================
# Schema for 'show interface summary vlan'
# =============================================
class ShowInterfaceSummaryVlanSchema(MetaParser):
    """ Schema for
        * show interface summary vlan
    """
    schema = {
        'Total_vlan_interface': int,
        'Configured_vlan_interfaces' : str
    }
# ==========================================================
#  Parser for 'show interface summary vlan'
# ==========================================================

class ShowInterfaceSummaryVlan(ShowInterfaceSummaryVlanSchema):
    """ Parser for
        * show interface summary vlan
    """

    cli_command = 'show interface summary vlan'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        #Total number of Vlan interfaces: 256
        p1 = re.compile(r'Total\s+number\s+of\s+Vlan\s+interfaces:\s+(?P<total_number>\d+)')

        #Vlan interfaces configured:
        #1,10-264
        p2 = r'Vlan\s+interfaces\s+configured:\s*(?P<vlan_int>\S+)'
        #p2 = re.compile(r'Vlan\s+interfaces\s+configured:\s+(?P<vlan_int>\S+)')
        #p2 = re.compile(r'Vlan\s+interfaces\s+configured:\n(?P<vlan_int>\S+)')
        for line in output.splitlines():
            line = line.strip()
            m1 = p1.match(line)
            if m1:
                group = m1.groupdict()
                ret_dict["Total_vlan_interface"] = int(group["total_number"])
        #m2 = p2.match(output)
        m2 = re.search(p2,output,re.M|re.I)
        if m2:
           group = m2.groupdict()
           ret_dict["Configured_vlan_interfaces"] = group["vlan_int"]
        return ret_dict

# ===================================================
# Schema for 'show interfaces {interface} summary'
# ===================================================
class ShowInterfacesSummarySchema(MetaParser):
    """ Schema for
        * show interfaces summary
        * show interfaces {interface} summary
    """
    schema = {
        'interfaces': {
            Any(): {
                'up': bool,
                'ihq': int,
                'iqd': int,
                'ohq': int,
                'oqd': int,
                'rxbs': int,
                'rxps': int,
                'txbs': int,
                'txps': int,
                'trtl': int,
                'name': str
            },
        }
    }

# ==========================================================
#  Parser for 'show interfaces {interface} summary'
# ==========================================================
class ShowInterfacesSummary(ShowInterfacesSummarySchema):
    """ Parser for
        * show interfaces summary
        * show interfaces {interface} summary
    """

    cli_command = ['show interfaces summary',
                   'show interfaces {interface} summary']

    def cli(self, interface=None, output=None):
        if output is None:
            if interface:
                output = self.device.execute(self.cli_command[1].format(interface=interface))
            else:
                output = self.device.execute(self.cli_command[0])

        # initial regexp pattern
        # * GigabitEthernet1/0/9          0         0         0         0         0         0         0         0         0
        #   GigabitEthernet1/0/10          0         0         0         0         0         0         0         0         0
        p = re.compile(r'^(?P<up>\*?) *(?P<name>[\w\-\/\.]+) +'
                       r'(?P<ihq>\d+) +(?P<iqd>\d+) +(?P<ohq>\d+) +'
                       r'(?P<oqd>\d+) +(?P<rxbs>\d+) +(?P<rxps>\d+) +'
                       r'(?P<txbs>\d+) +(?P<txps>\d+) +(?P<trtl>\d+)$')

        # initial variables
        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # * GigabitEthernet1/0/9          0         0         0         0         0         0         0         0         0
            #   GigabitEthernet1/0/10          0         0         0         0         0         0         0         0         0
            m = p.match(line)
            if m:
                group = m.groupdict()
                intf = Common.convert_intf_name(group.pop('name'))
                intf_dict = ret_dict.setdefault('interfaces', {}).setdefault(intf, {})
                intf_dict['name'] = intf
                intf_dict['up'] = True if group.pop('up') == '*' else False
                intf_dict.update({k: int(v) for k, v in group.items()})
                continue
        return ret_dict


# ====================================================
#  schema for show interfaces mtu
# ====================================================
class ShowInterfacesMtuSchema(MetaParser):
    """Schema for:
        show interfaces mtu
        show interfaces {interface} mtu
        show interfaces mtu module {mod}"""

    schema = {
        'interfaces': {
            Any(): {
                Optional('name'): str,
                'mtu': int
            }
        }
    }


# ====================================================
#  parser for show interfaces mtu
# ====================================================
class ShowInterfacesMtu(ShowInterfacesMtuSchema):
    """parser for
            * show interfaces mtu
            * show interfaces {interface} mtu
            * show interfaces mtu module {mod}
        """

    cli_command = ['show interfaces mtu',
                   'show interfaces {interface} mtu',
                   'show interfaces mtu module {mod}']

    def cli(self, interface=None, mod=None, output=None):

        if output is None:
            if mod:
                out = self.device.execute(self.cli_command[2].format(mod=mod))
            elif interface:
                out = self.device.execute(self.cli_command[1].format(interface=interface))
            else:
                out = self.device.execute(self.cli_command[0])

        result_dict = {}

        #Port          Name                        MTU
        #Fo1/0/1       Interface1                  1500
        #Fo1/0/2       Interface2                  1500

        p1 = re.compile(r'^(?P<interfaces>\S+)\s+(?P<name>.+?)?\s+(?P<mtu>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()

                intf_dict = result_dict.setdefault('interfaces', {}).\
                                        setdefault(Common.convert_intf_name(group['interfaces']), {})

                intf_dict.update({k:v for k, v in group.items() if v and k != 'interfaces'})
                intf_dict['mtu'] = int(intf_dict['mtu'])
                continue

        return result_dict

# ====================================================
#  schema for show interfaces status module {mod}
# ====================================================


class ShowInterfacesStatusModuleSchema(MetaParser):

    """
    Schema for show interfaces status module {mod}

    """

    schema = {
        Optional('interfaces'): {
            Any(): {
                Optional('name'): str,
                'status': str,
                'vlan': str,
                'duplex_code': str,
                'port_speed': str,
                Optional('type'): str,
            }
        },
        Optional('var') : str,
    }
#====================================================
#  parser for show interfaces status module {mod}
# ====================================================

class ShowInterfacesStatusModule(ShowInterfacesStatusModuleSchema):

    ''' Parser for :
        'show interfaces status module {mod}'
    '''
    cli_command = ['show interfaces status module {mod}']
    def cli(self, mod="", output = None):

        output = self.device.execute(self.cli_command[0].format(mod=mod))

        result_dict = {}

        p0 = re.compile(r'(?P<var>%.*)')

            # Port         Name               Status       Vlan       Duplex  Speed Type
            # Hu1/0/1                         connected    1            full    40G QSFP 40G AOC5M
            # Twe4/0/2                        connected    routed       full    10G SFP-10GBase-CX1
        p1 = re.compile(r'^(?P<interfaces>\S+)(?:\s+(?P<name>(.+)))?'
                r'\s+(?P<status>(connected|notconnect|suspended|inactive|disabled|err-disabled|monitoring))'
                r'\s+(?P<vlan>\S+)\s+(?P<duplex_code>[\S\-]+)\s+(?P<port_speed>[\S\-]+)(\s+(?P<type>.+))?$')


        # %Module1 is not Present

        m = p0.match(output)
        if m:

            var = m.groupdict()['var']
            result_dict['var'] = var


        for line in output.splitlines():
            line = line.strip()

            # Port         Name               Status       Vlan       Duplex  Speed Type
            # Hu1/0/1                         connected    1            full    40G QSFP 40G AOC5M

            m = p1.match(line)
            if m:
                group = m.groupdict()

                intf_dict = result_dict.setdefault('interfaces', {}).\
                                        setdefault(Common.convert_intf_name(group['interfaces']), {})

                name_val = group['name'].strip()
                if len(name_val)>0 :
                    intf_dict['name'] = name_val

                keys = ['status',
                        'vlan', 'duplex_code', 'port_speed',
                        'type']

                for k in keys:
                    if group[k]:
                        intf_dict[k] = group[k].strip()
                continue

        return result_dict


#======================================================
# Schema for 'show pm vp interface <interface> <vlan> '
# ======================================================

class ShowPmVpInterfaceVlanSchema(MetaParser):
    """Schema for show pm vp interface <interface> <vlan>"""

    schema = {
        'pm_vp_info': {
            Optional('vp'): str,
            Optional('es'): str,
            Optional('sm'): str,
            Optional('running'): str,
            Optional('state'): str,
            Optional('last_transition'): str,
        },

    }

# ======================================================
# Parser for 'show pm vp interface <interface> <vlan> '
# ======================================================
class ShowPmVpInterfaceVlan(ShowPmVpInterfaceVlanSchema):
    """Parser for show pm vp interface <interface> <vlan>"""

    cli_command = 'show pm vp interface {interface} {vlan}'

    def cli(self, interface=None, vlan=None, output=None):
        if output is None:
            cmd = self.cli_command.format(interface=interface, vlan=vlan)
            output = self.device.execute(cmd)

        # vp: 0x50823F64: 3/3(1001) es: 0, stp forwarding, link up, fwd yes
        p1 = re.compile(r"^vp:\s+(?P<vp>\S+\s+\S+)\s+es:\s+(?P<es>\S+\s+\S+\s+\S+\s+\S+\s+\S+\s+\S+\s+\S+)$")
        # sm(pm_vp 3/3(1001)), running yes, state forwarding
        p1_1 = re.compile(r"^sm\((?P<sm>\S+\s+\S+)\),\s+running\s+(?P<running>\w+),\s+state\s+(?P<state>\w+)$")
        # Last transition recorded: (linkup)-> authentication (linkup)-> authentication (authen_enable)-> authen_fail (authen_success)-> notforwarding (forward_notnotify)-> forwarding
        p1_2 = re.compile(r"^Last\s+transition\s+recorded:\s+(?P<last_transition>\S+\s+\S+\s+\S+\s+\S+\s+\S+\s+\S+\s+\S+\s+\S+\s+\S+\s+\S+)$")


        ret_dict = {}

        for line in output.splitlines():

            # vp: 0x50823F64: 3/3(1001) es: 0, stp forwarding, link up, fwd yes
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                if 'pm_vp_info' not in ret_dict:
                    pm_vp_info = ret_dict.setdefault('pm_vp_info', {})
                pm_vp_info['vp'] = dict_val['vp']
                pm_vp_info['es'] = dict_val['es']
                continue

            # sm(pm_vp 3/3(1001)), running yes, state forwarding
            m = p1_1.match(line)
            if m:
                dict_val = m.groupdict()
                if 'pm_vp_info' not in ret_dict:
                    pm_vp_info = ret_dict.setdefault('pm_vp_info', {})
                pm_vp_info['sm'] = dict_val['sm']
                pm_vp_info['running'] = dict_val['running']
                pm_vp_info['state'] = dict_val['state']
                continue

            # Last transition recorded: (linkup)-> authentication (linkup)-> authentication (authen_enable)-> authen_fail (authen_success)-> notforwarding (forward_notnotify)-> forwarding
            m = p1_2.match(line)
            if m:
                dict_val = m.groupdict()
                if 'pm_vp_info' not in ret_dict:
                    pm_vp_info = ret_dict.setdefault('pm_vp_info', {})
                pm_vp_info['last_transition'] = dict_val['last_transition']
                continue

        return ret_dict

# ====================================================
#  schema for show interfaces transceiver supported-list
# ====================================================

class ShowInterfacesTransceiverSupportedlistSchema(MetaParser):
    """Schema for:
        * show interfaces transceiver supported-list
    """

    schema = {
        'transceiver_type': {
            Any() : {
                'cisco_pin_min_version_supporting_dom' : str,
            },
        },
    }

#====================================================
#  parser for show interfaces transceiver supported-list
# ====================================================

class ShowInterfacesTransceiverSupportedlist(ShowInterfacesTransceiverSupportedlistSchema):
    """parser for show interfaces transceiver supported-list
    """

    cli_command = 'show interfaces transceiver supported-list'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output


        transceivers_supported_list = {}

        #------------------       -------------------------
        #p1 will match dashes pattern used to create dict that to start adiing the transceiver types
        p1 = re.compile(r"\-+\s+\-+")

        #   GLC-FE-100FX-RGD         ALL
        #   GLC-SX-MM                NONE
        p2 = re.compile(r"^(?P<transceiver>[\w-]+)\s+(?P<pin_version>(ALL|NONE))")

        for line in out.splitlines():
            line = line.strip()

            #------------------       -------------------------
            m1 = p1.match(line)
            if m1:
                transceiver_dict = transceivers_supported_list.setdefault('transceiver_type',{})

            #   GLC-FE-100FX-RGD         ALL
            #   GLC-SX-MM                NONE
            m2 = p2.match(line)
            if m2:
                transceiver_dict.update({m2.groupdict()['transceiver'] :
                                        { "cisco_pin_min_version_supporting_dom" :
                                        m2.groupdict()['pin_version']}})

        return transceivers_supported_list


# ======================================================
# Schema for 'show pm  port interface <interface> '
# ======================================================

class ShowPmPortInterfaceSchema(MetaParser):
    """Schema for show pm port interface <interface>"""

    schema = {
        'pm_port_info': {
            'port': str,
            'pd': str,
            'sw_idb': str,
            'sb': str,
            'hw_idb': str,
            'if_num': int,
            'hw_if_index': int,
            'snmp_if_index': str,
            'ptrunk_group': str,
            'admin': str,
            'line': str,
            'oper_err': str,
            'port_mac': str,
            'idb_port_vlan': int,
            'def_vlan_id': int,
            'internal_vlan': str,
            'dtp_special': str,
            'pagp_special': str,
            'speed': str,
            'duplex': str,
            'mode': str,
            'encap': str,
            'dtp_nonego': str,
            'flow_ctrl_receive': str,
            'flow_ctrl_send': str,
            'link_flap_cnt': int,
            'dtp_flap_cnt': int,
            'pagp_flap_cnt': int,
            'unidirectional': str,
            'oper_vlan': int,
            'flag': int,
            'sm': str,
            'running': str,
            'state': str,
            'last_transition': str,
            'vp': str,
            'vlans': str,
            'trunk_vlans': str,
            'fwd_vlans': int,
            'current_pruned_vlans': str,
            'previous_pruned_vlans': str,
            'protocols': str,
        },
        'config_values': {
            'access_mode': str,
            'access_vlan_id': int,
            'native_vlan_id': int,
            'trunk_vlans': str,
            'prune_vlans': str,
            'primary_host_vlan': int,
            'sec_host_vlan': int,
            'pri_promiscuous_vlan': int,
            'sec_prom_vlan': str,
            'speed': str,
            'speed_auto': str,
            'duplex': str,
            'mode': str,
            'encap': str,
            'nonego': str,
            'jumbo_cap': str,
            'jumbo': str,
            'mtu': int,
            'sync_delay': int,
            'hol': str,
            'bcast_sup_level': int,
            'mcast_sup_level': int,
            'ucast_sup_level': int,
            'disl': str,
            'dtp_nonego': str,
            'media': str,
            'dualmode': int,
            'tdr_ever_run': str,
            'tdr_in_progress': str,
            'tdr_result_valid': str,
            'tdr_error_code': int,
            'prbs_err_code': int,
            'prbs': str,

        },
    }

# ======================================================
# Parser for 'show pm  port interface <interface> '
# ======================================================

class ShowPmPortInterface(ShowPmPortInterfaceSchema):
    """Parser for show pm port interface <interface>"""

    cli_command = 'show pm port interface {interface}'

    def cli(self, interface=None, output=None):
        if output is None:
            cmd = self.cli_command.format(interface=interface)
            output = self.device.execute(cmd)

        # port 1/24  pd 0x7F837FEABD78 swidb 0x7F837EBFA020(switch)  sb 0x7F837EBFCA40
        p1 = re.compile(r"^port\s+(?P<port>\S+)\s+pd\s+(?P<pd>\S+)\s+swidb\s+"
             r"(?P<sw_idb>\S+)\s+sb\s+(?P<sb>\S+)$")
        #  hwidb 0x7F837EBF8C38
        p1_1 = re.compile(r"^hwidb\s+(?P<hw_idb>\S+)$")
        # if_number = 32 hw_if_index = 31 snmp_if_index = 32(32) ptrunkgroup = 0(port)
        p1_2 = re.compile(r"^if_number\s+=\s+(?P<if_num>\d+)\s+hw_if_index\s+="
               r"\s+(?P<hw_if_index>\d+)\s+snmp_if_index\s+=\s+(?P<snmp_if_index>\S+)"
               r"\s+ptrunkgroup\s+=\s+(?P<ptrunk_group>\S+)$")
        # admin up(up)  line up(up)  operErr none
        p1_3 = re.compile(r"^admin\s+(?P<admin>\S+)\s+line\s+(?P<line>\S+)\s+"
               r"operErr\s+(?P<oper_err>\w+)$")
        # port assigned mac address 683b.78f3.3118
        p1_4 = re.compile(r"^port\s+assigned\s+mac\s+address\s+(?P<port_mac>\S+)$")
        # idb port vlan id 1  default vlan id 1
        p1_5 = re.compile(r"^idb\s+port\s+vlan\s+id\s+(?P<idb_port_vlan>\d+)\s+"
               r"default\s+vlan\s+id\s+(?P<def_vlan_id>\d+)$")
        # internalVlan 0x0  remapVlan 0x0
        p1_6 = re.compile(r"^internalVlan\s+(?P<internal_vlan>\S+)\s+remapVlan\s+0x0$")
        # dtp special no  pagp special no
        p1_7 = re.compile(r"^dtp\s+special\s+(?P<dtp_special>\w+)\s+pagp\s+"
               r"special\s+(?P<pagp_special>\w+)$")
        # speed: 100M   duplex: full   mode: access   encap: native
        p1_8 = re.compile(r"^speed:\s+(?P<speed>\S+)\s+duplex:\s+(?P<duplex>\w+)"
               r"\s+mode:\s+(?P<mode>\w+)\s+encap:\s+(?P<encap>\w+)$")
        # dtp nonegotiate: FALSE
        p1_9 = re.compile(r"^dtp\s+nonegotiate:\s+(?P<dtp_nonego>\w+)$")
        # flowcontrol receive: on   flowcontrol send: off
        p1_10 = re.compile(r"^flowcontrol\s+receive:\s+(?P<flow_ctrl_receive>\w+)"
                r"\s+flowcontrol\s+send:\s+(?P<flow_ctrl_send>\w+)$")
        # linkflapcnt: 0  dtpflapcnt: 0  pagpflapcnt: 0
        p1_11 = re.compile(r"^linkflapcnt:\s+(?P<link_flap_cnt>\d+)\s+dtpflapcnt:"
                r"\s+(?P<dtp_flap_cnt>\d+)\s+pagpflapcnt:\s+(?P<pagp_flap_cnt>\d+)$")
        # unidirectional: off
        p1_12 = re.compile(r"^unidirectional:\s+(?P<unidirectional>\w+)$")
        # operVlan: 0
        p1_13 = re.compile(r"^operVlan:\s+(?P<oper_vlan>\d+)$")
        # flag:     0
        p1_14 = re.compile(r"^flag:\s+(?P<flag>\d+)$")
        # sm(pm_port 1/24), running yes, state access_multi
        p1_15 = re.compile(r"^sm\((?P<sm>\S+\s+\S+)\),\s+running\s+"
                r"(?P<running>\w+),\s+state\s+(?P<state>\S+)$")
        # Last transition recorded: (cfg_access_vvlanid)-> pagp_port_cleanup (cfg_access_vvlanid)-> pagp (cfg_access_vvlanid)-> pre_pagp_may_suspend (cfg_access_vvlanid)-> pagp_may_suspend (pagp_continue)-> start_pagp (pagp_continue)-> pagp (dont_bundle)-> pre_post_pagp (dont_bundle)-> post_pagp (dtp_access_multi)-> access_multi (bulk_sync)-> access_multi
        p1_16 = re.compile(r"^Last\s+transition\s+recorded:\s+"
                r"(?P<last_transition>\S+\s+\S+\s+\S+\s+\S+\s+\S+\s+\S+\s+\S+\s+"
                r"\S+\s+\S+\s+\S+\s+\S+\s+\S+\s+\S+\s+\S+\s+\S+\s+\S+\s+\S+\s+\S+"
                r"\s+\S+\s+\S+)$")
        # vp:  1 100
        p1_17 = re.compile(r"^vp:\s+(?P<vp>\S+\s+\S+)$")
        # vlans:  1 100
        p1_18 = re.compile(r"^vlans:\s+(?P<vlans>\S+\s+\S+)$")
        # trunkVlans:  1 100
        p1_19 = re.compile(r"^trunkVlans:\s+(?P<trunk_vlans>\S+\s+\S+)$")
        # fwdVlans:  100
        p1_20 = re.compile(r"^fwdVlans:\s+(?P<fwd_vlans>\d+)$")
        # currentlyPrunedVlans:  none
        p1_21 = re.compile(r"^currentlyPrunedVlans:\s+(?P<current_pruned_vlans>\w+)$")
        # previouslyPrunedVlans:  none
        p1_22 = re.compile(r"^previouslyPrunedVlans:\s+(?P<previous_pruned_vlans>\w+)$")
        # protocols: ip=on ipx=on misc=on other=on
        p1_23 = re.compile(r"^protocols:\s+(?P<protocols>\S+\s+\S+\s+\S+\s+\S+)$")
        # access mode: unknown   access vlanid: 1   native vlanid: 1
        p2 = re.compile(r"^access\s+mode:\s+(?P<access_mode>\w+)\s+"
             r"access\s+vlanid:\s+(?P<access_vlan_id>\d+)\s+native\s+vlanid:\s+"
             r"(?P<native_vlan_id>\d+)$")
        # trunkVlans:  1-4094
        p2_1 = re.compile(r"^trunkVlans:\s+(?P<trunk_vlans>\S+)$")
        # pruneVlans:  2-1001primary host vlanid: 32767    secondary host vlanid: 32767
        p2_2 = re.compile(r"^pruneVlans:\s+(?P<prune_vlans>\S+)primary\s+host\s+"
               r"vlanid:\s+(?P<primary_host_vlan>\d+)\s+secondary\s+host\s+"
               r"vlanid:\s+(?P<sec_host_vlan>\d+)$")
        # primary promiscuous vlanid: 32767
        p2_3 = re.compile(r"^primary\s+promiscuous\s+vlanid:\s+"
               r"(?P<pri_promiscuous_vlan>\d+)$")
        # secondary prom vlans:  none
        p2_4 = re.compile(r"^secondary\s+prom\s+vlans:\s+(?P<sec_prom_vlan>\w+)$")
        # speed: auto speedauto: auto-default   duplex: auto   mode: access
        p2_5 = re.compile(r"^speed:\s+(?P<speed>\w+)\s+speedauto:\s+"
               r"(?P<speed_auto>\S+)\s+duplex:\s+(?P<duplex>\w+)\s+"
               r"mode:\s+(?P<mode>\w+)$")
        # encap: dot1q   nonegotiate: false
        p2_6 = re.compile(r"^encap:\s+(?P<encap>\S+)\s+nonegotiate:\s+"
               r"(?P<nonego>\w+)$")
        # jumbo cap: true   jumbo: false  mtu: 1500  sync-delay: 210  HOL: Enable
        p2_7 = re.compile(r"^jumbo\s+cap:\s+(?P<jumbo_cap>\w+)\s+jumbo:\s+"
               r"(?P<jumbo>\w+)\s+mtu:\s+(?P<mtu>\d+)\s+sync-delay:\s+"
               r"(?P<sync_delay>\d+)\s+HOL:\s+(?P<hol>\w+)$")
        # bcast-supp-level: 10000   mcast-supp-level: 10000   ucast-supp-level: 10000
        p2_8 = re.compile(r"^bcast-supp-level:\s+(?P<bcast_sup_level>\d+)\s+"
               r"mcast-supp-level:\s+(?P<mcast_sup_level>\d+)\s+ucast-supp-level:"
               r"\s+(?P<ucast_sup_level>\d+)$")
        # disl: off   dtp nonegotiate: FALSE   media: unknown   dualmode 0
        p2_9 = re.compile(r"^disl:\s+(?P<disl>\w+)\s+dtp\s+nonegotiate:\s+"
               r"(?P<dtp_nonego>\w+)\s+media:\s+(?P<media>\w+)\s+dualmode\s+"
               r"(?P<dualmode>\d+)$")
        # tdr_ever_run: FALSE tdr_in_progress: FALSE tdr_result_valid: FALSE
        p2_10 = re.compile(r"^tdr_ever_run:\s+(?P<tdr_ever_run>\w+)\s+"
                r"tdr_in_progress:\s+(?P<tdr_in_progress>\w+)\s+tdr_result_valid:"
                r"\s+(?P<tdr_result_valid>\w+)$")
        # tdr_err_code: 0, prbs_err_code: 0
        p2_11 = re.compile(r"^tdr_err_code:\s+(?P<tdr_error_code>\d+),\s+"
                r"prbs_err_code:\s+(?P<prbs_err_code>\d+)$")
        # PRBS: Stopped PRBS - port was admin down
        p2_12 = re.compile(r"^PRBS:\s+(?P<prbs>\S+\s+\S+\s+\S+\s+\S+\s+\S+\s+\S+\s+\S+)$")


        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # port 1/24  pd 0x7F837FEABD78 swidb 0x7F837EBFA020(switch)  sb 0x7F837EBFCA40
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                if 'pm_port_info' not in ret_dict:
                    pm_port_info = ret_dict.setdefault('pm_port_info', {})
                pm_port_info['port'] = dict_val['port']
                pm_port_info['pd'] = dict_val['pd']
                pm_port_info['sw_idb'] = dict_val['sw_idb']
                pm_port_info['sb'] = dict_val['sb']
                continue

            #  hwidb 0x7F837EBF8C38
            m = p1_1.match(line)
            if m:
                dict_val = m.groupdict()
                if 'pm_port_info' not in ret_dict:
                    pm_port_info = ret_dict.setdefault('pm_port_info', {})
                pm_port_info['hw_idb'] = dict_val['hw_idb']
                continue

            # if_number = 32 hw_if_index = 31 snmp_if_index = 32(32) ptrunkgroup = 0(port)
            m = p1_2.match(line)
            if m:
                dict_val = m.groupdict()
                if 'pm_port_info' not in ret_dict:
                    pm_port_info = ret_dict.setdefault('pm_port_info', {})
                pm_port_info['if_num'] = int(dict_val['if_num'])
                pm_port_info['hw_if_index'] = int(dict_val['hw_if_index'])
                pm_port_info['snmp_if_index'] = dict_val['snmp_if_index']
                pm_port_info['ptrunk_group'] = dict_val['ptrunk_group']
                continue

            # admin up(up)  line up(up)  operErr none
            m = p1_3.match(line)
            if m:
                dict_val = m.groupdict()
                if 'pm_port_info' not in ret_dict:
                    pm_port_info = ret_dict.setdefault('pm_port_info', {})
                pm_port_info['admin'] = dict_val['admin']
                pm_port_info['line'] = dict_val['line']
                pm_port_info['oper_err'] = dict_val['oper_err']
                continue

            # port assigned mac address 683b.78f3.3118
            m = p1_4.match(line)
            if m:
                dict_val = m.groupdict()
                if 'pm_port_info' not in ret_dict:
                    pm_port_info = ret_dict.setdefault('pm_port_info', {})
                pm_port_info['port_mac'] = dict_val['port_mac']
                continue

            # idb port vlan id 1  default vlan id 1
            m = p1_5.match(line)
            if m:
                dict_val = m.groupdict()
                if 'pm_port_info' not in ret_dict:
                    pm_port_info = ret_dict.setdefault('pm_port_info', {})
                pm_port_info['idb_port_vlan'] = int(dict_val['idb_port_vlan'])
                pm_port_info['def_vlan_id'] = int(dict_val['def_vlan_id'])
                continue

            # internalVlan 0x0  remapVlan 0x0
            m = p1_6.match(line)
            if m:
                dict_val = m.groupdict()
                if 'pm_port_info' not in ret_dict:
                    pm_port_info = ret_dict.setdefault('pm_port_info', {})
                pm_port_info['internal_vlan'] = dict_val['internal_vlan']
                continue

            # dtp special no  pagp special no
            m = p1_7.match(line)
            if m:
                dict_val = m.groupdict()
                if 'pm_port_info' not in ret_dict:
                    pm_port_info = ret_dict.setdefault('pm_port_info', {})
                pm_port_info['dtp_special'] = dict_val['dtp_special']
                pm_port_info['pagp_special'] = dict_val['pagp_special']
                continue

            # speed: 100M   duplex: full   mode: access   encap: native
            m = p1_8.match(line)
            if m:
                dict_val = m.groupdict()
                if 'pm_port_info' not in ret_dict:
                    pm_port_info = ret_dict.setdefault('pm_port_info', {})
                pm_port_info['speed'] = dict_val['speed']
                pm_port_info['duplex'] = dict_val['duplex']
                pm_port_info['mode'] = dict_val['mode']
                pm_port_info['encap'] = dict_val['encap']
                continue

            # dtp nonegotiate: FALSE
            m = p1_9.match(line)
            if m:
                dict_val = m.groupdict()
                if 'pm_port_info' not in ret_dict:
                    pm_port_info = ret_dict.setdefault('pm_port_info', {})
                pm_port_info['dtp_nonego'] = dict_val['dtp_nonego']
                continue

            # flowcontrol receive: on   flowcontrol send: off
            m = p1_10.match(line)
            if m:
                dict_val = m.groupdict()
                if 'pm_port_info' not in ret_dict:
                    pm_port_info = ret_dict.setdefault('pm_port_info', {})
                pm_port_info['flow_ctrl_receive'] = dict_val['flow_ctrl_receive']
                pm_port_info['flow_ctrl_send'] = dict_val['flow_ctrl_send']
                continue

            # linkflapcnt: 0  dtpflapcnt: 0  pagpflapcnt: 0
            m = p1_11.match(line)
            if m:
                dict_val = m.groupdict()
                if 'pm_port_info' not in ret_dict:
                    pm_port_info = ret_dict.setdefault('pm_port_info', {})
                pm_port_info['link_flap_cnt'] = int(dict_val['link_flap_cnt'])
                pm_port_info['dtp_flap_cnt'] = int(dict_val['dtp_flap_cnt'])
                pm_port_info['pagp_flap_cnt'] = int(dict_val['pagp_flap_cnt'])
                continue

            # unidirectional: off
            m = p1_12.match(line)
            if m:
                dict_val = m.groupdict()
                if 'pm_port_info' not in ret_dict:
                    pm_port_info = ret_dict.setdefault('pm_port_info', {})
                pm_port_info['unidirectional'] = dict_val['unidirectional']
                continue

            # operVlan: 0
            m = p1_13.match(line)
            if m:
                dict_val = m.groupdict()
                if 'pm_port_info' not in ret_dict:
                    pm_port_info = ret_dict.setdefault('pm_port_info', {})
                pm_port_info['oper_vlan'] = int(dict_val['oper_vlan'])
                continue

            # flag:     0
            m = p1_14.match(line)
            if m:
                dict_val = m.groupdict()
                if 'pm_port_info' not in ret_dict:
                    pm_port_info = ret_dict.setdefault('pm_port_info', {})
                pm_port_info['flag'] = int(dict_val['flag'])
                continue

            # sm(pm_port 1/24), running yes, state access_multi
            m = p1_15.match(line)
            if m:
                dict_val = m.groupdict()
                if 'pm_port_info' not in ret_dict:
                    pm_port_info = ret_dict.setdefault('pm_port_info', {})
                pm_port_info['sm'] = dict_val['sm']
                pm_port_info['running'] = dict_val['running']
                pm_port_info['state'] = dict_val['state']
                continue

            # Last transition recorded: (cfg_access_vvlanid)-> pagp_port_cleanup (cfg_access_vvlanid)-> pagp (cfg_access_vvlanid)-> pre_pagp_may_suspend (cfg_access_vvlanid)-> pagp_may_suspend (pagp_continue)-> start_pagp (pagp_continue)-> pagp (dont_bundle)-> pre_post_pagp (dont_bundle)-> post_pagp (dtp_access_multi)-> access_multi (bulk_sync)-> access_multi
            m = p1_16.match(line)
            if m:
                dict_val = m.groupdict()
                if 'pm_port_info' not in ret_dict:
                    pm_port_info = ret_dict.setdefault('pm_port_info', {})
                pm_port_info['last_transition'] = dict_val['last_transition']
                continue

            # vp:  1 100
            m = p1_17.match(line)
            if m:
                dict_val = m.groupdict()
                if 'pm_port_info' not in ret_dict:
                    pm_port_info = ret_dict.setdefault('pm_port_info', {})
                pm_port_info['vp'] = dict_val['vp']
                continue

            # vlans:  1 100
            m = p1_18.match(line)
            if m:
                dict_val = m.groupdict()
                if 'pm_port_info' not in ret_dict:
                    pm_port_info = ret_dict.setdefault('pm_port_info', {})
                pm_port_info['vlans'] = dict_val['vlans']
                continue

            # trunkVlans:  1 100
            m = p1_19.match(line)
            if m:
                dict_val = m.groupdict()
                if 'pm_port_info' not in ret_dict:
                    pm_port_info = ret_dict.setdefault('pm_port_info', {})
                pm_port_info['trunk_vlans'] = dict_val['trunk_vlans']
                continue

            # fwdVlans:  100
            m = p1_20.match(line)
            if m:
                dict_val = m.groupdict()
                if 'pm_port_info' not in ret_dict:
                    pm_port_info = ret_dict.setdefault('pm_port_info', {})
                pm_port_info['fwd_vlans'] = int(dict_val['fwd_vlans'])
                continue

            # currentlyPrunedVlans:  none
            m = p1_21.match(line)
            if m:
                dict_val = m.groupdict()
                if 'pm_port_info' not in ret_dict:
                    pm_port_info = ret_dict.setdefault('pm_port_info', {})
                pm_port_info['current_pruned_vlans'] = dict_val['current_pruned_vlans']
                continue

            # previouslyPrunedVlans:  none
            m = p1_22.match(line)
            if m:
                dict_val = m.groupdict()
                if 'pm_port_info' not in ret_dict:
                    pm_port_info = ret_dict.setdefault('pm_port_info', {})
                pm_port_info['previous_pruned_vlans'] = dict_val['previous_pruned_vlans']
                continue

            # protocols: ip=on ipx=on misc=on other=on
            m = p1_23.match(line)
            if m:
                dict_val = m.groupdict()
                if 'pm_port_info' not in ret_dict:
                    pm_port_info = ret_dict.setdefault('pm_port_info', {})
                pm_port_info['protocols'] = dict_val['protocols']
                continue

            # access mode: unknown   access vlanid: 1   native vlanid: 1
            m = p2.match(line)
            if m:
                dict_val = m.groupdict()
                if 'config_values' not in ret_dict:
                    config_values = ret_dict.setdefault('config_values', {})
                config_values['access_mode'] = dict_val['access_mode']
                config_values['access_vlan_id'] = int(dict_val['access_vlan_id'])
                config_values['native_vlan_id'] = int(dict_val['native_vlan_id'])
                continue

            # trunkVlans:  1-4094
            m = p2_1.match(line)
            if m:
                dict_val = m.groupdict()
                if 'config_values' not in ret_dict:
                    config_values = ret_dict.setdefault('config_values', {})
                config_values['trunk_vlans'] = dict_val['trunk_vlans']
                continue

            # pruneVlans:  2-1001primary host vlanid: 32767    secondary host vlanid: 32767
            m = p2_2.match(line)
            if m:
                dict_val = m.groupdict()
                if 'config_values' not in ret_dict:
                    config_values = ret_dict.setdefault('config_values', {})
                config_values['prune_vlans'] = dict_val['prune_vlans']
                config_values['primary_host_vlan'] = int(dict_val['primary_host_vlan'])
                config_values['sec_host_vlan'] = int(dict_val['sec_host_vlan'])
                continue

            # primary promiscuous vlanid: 32767
            m = p2_3.match(line)
            if m:
                dict_val = m.groupdict()
                if 'config_values' not in ret_dict:
                    config_values = ret_dict.setdefault('config_values', {})
                config_values['pri_promiscuous_vlan'] = int(dict_val['pri_promiscuous_vlan'])
                continue

            # secondary prom vlans:  none
            m = p2_4.match(line)
            if m:
                dict_val = m.groupdict()
                if 'config_values' not in ret_dict:
                    config_values = ret_dict.setdefault('config_values', {})
                config_values['sec_prom_vlan'] = dict_val['sec_prom_vlan']
                continue

            # speed: auto speedauto: auto-default   duplex: auto   mode: access
            m = p2_5.match(line)
            if m:
                dict_val = m.groupdict()
                if 'config_values' not in ret_dict:
                    config_values = ret_dict.setdefault('config_values', {})
                config_values['speed'] = dict_val['speed']
                config_values['speed_auto'] = dict_val['speed_auto']
                config_values['duplex'] = dict_val['duplex']
                config_values['mode'] = dict_val['mode']
                continue

            # encap: dot1q   nonegotiate: false
            m = p2_6.match(line)
            if m:
                dict_val = m.groupdict()
                if 'config_values' not in ret_dict:
                    config_values = ret_dict.setdefault('config_values', {})
                config_values['encap'] = dict_val['encap']
                config_values['nonego'] = dict_val['nonego']
                continue


            # jumbo cap: true   jumbo: false  mtu: 1500  sync-delay: 210  HOL: Enable
            m = p2_7.match(line)
            if m:
                dict_val = m.groupdict()
                if 'config_values' not in ret_dict:
                    config_values = ret_dict.setdefault('config_values', {})
                config_values['jumbo_cap'] = dict_val['jumbo_cap']
                config_values['jumbo'] = dict_val['jumbo']
                config_values['mtu'] = int(dict_val['mtu'])
                config_values['sync_delay'] = int(dict_val['sync_delay'])
                config_values['hol'] = dict_val['hol']
                continue

            # bcast-supp-level: 10000   mcast-supp-level: 10000   ucast-supp-level: 10000
            m = p2_8.match(line)
            if m:
                dict_val = m.groupdict()
                if 'config_values' not in ret_dict:
                    config_values = ret_dict.setdefault('config_values', {})
                config_values['bcast_sup_level'] = int(dict_val['bcast_sup_level'])
                config_values['mcast_sup_level'] = int(dict_val['mcast_sup_level'])
                config_values['ucast_sup_level'] = int(dict_val['ucast_sup_level'])
                continue

            # disl: off   dtp nonegotiate: FALSE   media: unknown   dualmode 0
            m = p2_9.match(line)
            if m:
                dict_val = m.groupdict()
                if 'config_values' not in ret_dict:
                    config_values = ret_dict.setdefault('config_values', {})
                config_values['disl'] = dict_val['disl']
                config_values['dtp_nonego'] = dict_val['dtp_nonego']
                config_values['media'] = dict_val['media']
                config_values['dualmode'] = int(dict_val['dualmode'])
                continue

            # tdr_ever_run: FALSE tdr_in_progress: FALSE tdr_result_valid: FALSE
            m = p2_10.match(line)
            if m:
                dict_val = m.groupdict()
                if 'config_values' not in ret_dict:
                    config_values = ret_dict.setdefault('config_values', {})
                config_values['tdr_ever_run'] = dict_val['tdr_ever_run']
                config_values['tdr_in_progress'] = dict_val['tdr_in_progress']
                config_values['tdr_result_valid'] = dict_val['tdr_result_valid']
                continue

            # tdr_err_code: 0, prbs_err_code: 0
            m = p2_11.match(line)
            if m:
                dict_val = m.groupdict()
                if 'config_values' not in ret_dict:
                    config_values = ret_dict.setdefault('config_values', {})
                config_values['tdr_error_code'] = int(dict_val['tdr_error_code'])
                config_values['prbs_err_code'] = int(dict_val['prbs_err_code'])
                continue

            # PRBS: Stopped PRBS - port was admin down
            m = p2_12.match(line)
            if m:
                dict_val = m.groupdict()
                if 'config_values' not in ret_dict:
                    config_values = ret_dict.setdefault('config_values', {})
                config_values['prbs'] = dict_val['prbs']
                continue

        return ret_dict

# ======================================================
# Parser for 'show interfaces private-vlan mapping'
# ======================================================
class ShowInterfacesPrivateVlanMappingSchema(MetaParser):
    """Schema for show interfaces private-vlan mapping"""

    schema = {
        'secondary_vlan': {
            Any(): {
                'type': str,
                'interface': str
            }
        }
    }

class ShowInterfacesPrivateVlanMapping(ShowInterfacesPrivateVlanMappingSchema):
    """Parser for show interfaces private-vlan mapping"""

    cli_command = 'show interfaces private-vlan mapping'

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # vlan70    71             community
        p1 = re.compile(r'^(?P<interface>\w+)\s+(?P<secondary_vlan>\d+)\s+(?P<type>\w+)$')

        result_dict = {}
        for line in output.splitlines():
            line = line.strip()
            # vlan70    71             community
            m = p1.match(line)
            if m:
                group = m.groupdict()
                intf_dict = result_dict.setdefault('secondary_vlan', {}).setdefault(int(group['secondary_vlan']), {})

                intf_dict.update({k:v for k, v in group.items() if v and k != 'secondary_vlan'})
                intf_dict['interface'] = Common.convert_intf_name(intf_dict['interface'])
                intf_dict['type'] = intf_dict['type']
                continue

        return result_dict

# ======================================================
# Schema for 'show interface {interface_id} etherchannel'
# ======================================================

class ShowInterfaceEtherchannelSchema(MetaParser):
    """Schema for show interface {interface_id} etherchannel"""

    schema = {
        'port_state': str,
        'channel_group': int,
        'mode': str,
        'gcchange': str,
        'port_channel': str,
        'gc': str,
        'pseudo_port_channel': str,
        'port_index': int,
        'load': str,
        'protocol': str,
        Optional('flags'): {
            str: str
        },
        Optional('local_information'): {
            'port': str,
            'flags': str,
            'state': str,
            'priority': str,
            'admin_key': str,
            'oper_key': str,
            'port_number': str,
            'port_state': str,
        },
        'port_age': str
    }

# ======================================================
# Parser for 'show interface {interface_id} etherchannel'
# ======================================================
class ShowInterfaceEtherchannel(ShowInterfaceEtherchannelSchema):
    """Parser for show interface {interface_id} etherchannel"""

    cli_command = 'show interface {interface_id} etherchannel'

    def cli(self, interface_id, output=None):

        if output is None:
            cmd = self.cli_command.format(interface_id=interface_id)
            output = self.device.execute(cmd)

        #Port state    = Up Mstr In-Bndl
        p1 = re.compile(r'^Port state\s+=\s+(?P<port_state>[\w -]+)$')
        #Channel group = 2           Mode = On              Gcchange = -
        p2 = re.compile(r'^Channel group\s+=\s+(?P<channel_group>\d+)\s+Mode\s+=\s+(?P<mode>\w+)\s+Gcchange\s+=\s+(?P<gcchange>\S+)$')
        #Port-channel  = Po2         GC   =   -             Pseudo port-channel = Po2
        p3 = re.compile(r'^Port-channel\s+=\s+(?P<port_channel>\w+)\s+GC\s+=\s+(?P<gc>\S+)\s+Pseudo port-channel\s+=\s+(?P<pseudo_port_channel>\S+)$')
        #Port index    = 0           Load = 0x00            Protocol =    -
        p4 = re.compile(r'^Port index\s+=\s+(?P<port_index>\d+)\s+Load\s+=\s+(?P<load>\S+)\s+Protocol\s+=\s+(?P<protocol>\S+)$')
        #Flags:  S - Device is sending Slow LACPDUs   F - Device is sending fast LACPDUs.
        p5 = re.compile(r'^Flags:\s+(?P<flag>\S+)\s-\s(?P<flag_value>[\S\s]+)\s+(?P<flag2>\w+)\s-\s(?P<flag_value2>[\S\s]+)\.$')
        #A - Device is in active mode.        P - Device is in passive mode.
        p5_1 = re.compile(r'^(?P<flag>\S+)\s-\s(?P<flag_value>[\S\s]+)\.\s+(?P<flag2>\S+)\s-\s(?P<flag_value2>[\S\s]+)\.$')
        #Local information:
        #                                 LACP port    Admin     Oper    Port        Port
        # Port          Flags   State     Priority     Key       Key     Number      State
        # Gi2/0/13      SA      down      32768        0xA       0x0     0x20E       0x4D
        p6 = re.compile(r'^(?P<port>Gi[\w\/\d]+)\s+(?P<flags>\w+)\s+(?P<state>\w+)\s+(?P<priority>\d+)'
                        r'\s+(?P<admin_key>\w+)\s+(?P<oper_key>\w+)\s+(?P<port_number>\w+)\s+(?P<port_state>\w+)$')
        #Age of the port in the current state: 0d:00h:00m:29s
        p7 = re.compile(r'^Age of the port in the current state:\s+(?P<age_of_port>\S+)$')

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            #Port state    = Up Mstr In-Bndl
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['port_state'] = group['port_state']
                continue

            #Channel group = 2           Mode = On              Gcchange = -
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict['channel_group'] = int(group['channel_group'])
                ret_dict['mode'] = group['mode']
                ret_dict['gcchange'] = group['gcchange']
                continue

            #Port-channel  = Po2         GC   =   -             Pseudo port-channel = Po2
            m = p3.match(line)
            if m:
                group = m.groupdict()
                ret_dict['port_channel'] = group['port_channel']
                ret_dict['gc'] = group['gc']
                ret_dict['pseudo_port_channel'] = group['pseudo_port_channel']
                continue

            #Port index    = 0           Load = 0x00            Protocol =    -
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ret_dict['port_index'] = int(group['port_index'])
                ret_dict['load'] = group['load']
                ret_dict['protocol'] = group['protocol']
                continue

            #Flags:  S - Device is sending Slow LACPDUs   F - Device is sending fast LACPDUs.
            m = p5.match(line)
            if m:
                group = m.groupdict()
                flag_dict = ret_dict.setdefault('flags',{})
                flag_dict[group['flag']] = group['flag_value'].strip()
                flag_dict[group['flag2']] = group['flag_value2']
                continue

            #A - Device is in active mode.        P - Device is in passive mode.
            m = p5_1.match(line)
            if m:
                group = m.groupdict()
                flag_dict = ret_dict.setdefault('flags',{})
                flag_dict[group['flag']] = group['flag_value']
                flag_dict[group['flag2']] = group['flag_value2']
                continue

            #Local information:
            #                                 LACP port    Admin     Oper    Port        Port
            # Port          Flags   State     Priority     Key       Key     Number      State
            # Gi2/0/13      SA      down      32768        0xA       0x0     0x20E       0x4D
            m = p6.match(line)
            if m:
                group = m.groupdict()
                info_dict = ret_dict.setdefault('local_information',{})
                info_dict['port'] = group['port']
                info_dict['flags'] = group['flags']
                info_dict['state'] = group['state']
                info_dict['priority'] = group['priority']
                info_dict['admin_key'] = group['admin_key']
                info_dict['oper_key'] = group['oper_key']
                info_dict['port_number'] = group['port_number']
                info_dict['port_state'] = group['port_state']
                continue

            #Age of the port in the current state: 0d:00h:00m:29s
            m = p7.match(line)
            if m:
                group = m.groupdict()
                ret_dict['port_age'] = group['age_of_port']
                continue

        return ret_dict


class ShowInterfacesCapabilitiesSchema(MetaParser):
    """
        Schema for show interfaces capabilities
    """

    schema = {
        'interface': {
            Any() : {
                Any() : str,
            }
        }
    }


class ShowInterfacesCapabilities(ShowInterfacesCapabilitiesSchema):
    """
        parser for show interfaces capabilities
    """

    cli_command = ['show interfaces capabilities', 'show interfaces {interface} capabilities']

    def cli(self, interface=None, output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[1].format(interface=interface)
            else:
                cmd = self.cli_command[0]

            output = self.device.execute(cmd)

        # TenGigabitEthernet3/1/3
        p1 = re.compile(r'^(?P<interface>[\w\/\d\.]+)$')

        # Model:                 WS-C3650-48PD
        # Type:                  SFP-10G-ACTIVE-CABLE
        # Speed:                 10000
        # Duplex:                full
        p2 = re.compile(r'^(?P<key_name>[\w\s\.]+):\s+(?P<value>.+)$')

        # tx-(2p6q3t)
        p3 = re.compile(r'^(?P<qos_tx>tx-.+)$')

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # TenGigabitEthernet3/1/3
            m = p1.match(line)
            if m:
                int_dict = ret_dict.setdefault('interface', {}).setdefault(Common.convert_intf_name(m.groupdict()['interface']), {})
                continue

            # Model:                 WS-C3650-48PD
            # Type:                  SFP-10G-ACTIVE-CABLE
            # Speed:                 10000
            # Duplex:                full
            m = p2.match(line)
            if m:
                key = m.groupdict()['key_name'].strip().lower().replace(' ', '_').replace('.', '')
                int_dict[key] = m.groupdict()['value']
                continue

            # tx-(2p6q3t)
            m = p3.match(line)
            if m:
                int_dict[key] = f"{int_dict[key]} {m.groupdict()['qos_tx']}"

        return ret_dict

class ShowInterfaceFlowControlSchema(MetaParser):
    """Schema for show interfaces {interface_id} flowcontrol"""

    schema = {
        'interface': {
            'port': str,
            'send_fc_admin': str,
            'send_fc_oper': str,
            'receive_fc_admin': str,
            'receive_fc_oper': str,
            'rx_pause': int,
            'tx_pause': int,
        }
    }

# ======================================================
# Parser for 'show interface {interface_id} flowcontrol'
# ======================================================
class ShowInterfaceFlowControl(ShowInterfaceFlowControlSchema):
    """Parser for show interfaces {interface_id} flowcontrol"""

    cli_command = 'show interfaces {interface_id} flowcontrol'

    def cli(self, interface_id, output=None):

        if output is None:
            cmd = self.cli_command.format(interface_id=interface_id)
            output = self.device.execute(cmd)

        # Port            Send FlowControl  Receive FlowControl  RxPause TxPause
        #                 admin    oper     admin    oper
        # ------------    -------- -------- -------- --------    ------- -------
        # Fo2/1/0/10      Unsupp.  Unsupp.  on       on          0       0
        p1 = re.compile(r'^(?P<port>[\w\/\d]+)\s+(?P<send_fc_admin>[\.\w]+)\s+(?P<send_fc_oper>[\.\w]+)\s+(?P<receive_fc_admin>\w+)\s+(?P<receive_fc_oper>\w+)\s+(?P<rx_pause>\d+)\s+(?P<tx_pause>\d+)$')

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Port            Send FlowControl  Receive FlowControl  RxPause TxPause
            #                 admin    oper     admin    oper
            # ------------    -------- -------- -------- --------    ------- -------
            # Fo2/1/0/10      Unsupp.  Unsupp.  on       on          0       0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                info_dict = ret_dict.setdefault('interface',{})
                info_dict['port'] = Common.convert_intf_name(group['port'])
                info_dict['send_fc_admin'] = group['send_fc_admin']
                info_dict['send_fc_oper'] = group['send_fc_oper']
                info_dict['receive_fc_admin'] = group['receive_fc_admin']
                info_dict['receive_fc_oper'] = group['receive_fc_oper']
                info_dict['rx_pause'] = int(group['rx_pause'])
                info_dict['tx_pause'] = int(group['tx_pause'])
                continue

        return ret_dict


class ShowInterfacesVlanMappingSchema(MetaParser):
    """Schema for show interfaces {interface} vlan mapping"""

    schema = {
        'vlan_on_wire': {
            Any(): {
                'trans_vlan': int,
                'operation': str,
            }
        }
    }


class ShowInterfacesVlanMapping(ShowInterfacesVlanMappingSchema):
    """Parser for show interfaces {interface} vlan mapping"""

    cli_command = 'show interface {interface} vlan mapping'

    def cli(self, interface, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        # 20                                    30             1-to-1
        p1 = re.compile(r"^(?P<vlan_on_wire>\d+)\s+(?P<trans_vlan>\d+)\s+(?P<operation>\S+)$")

        ret_dict = {}

        for line in output.splitlines():

            # 20                                    30             1-to-1
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                vlan_dict = ret_dict.setdefault('vlan_on_wire', {}).setdefault(dict_val['vlan_on_wire'], {})
                vlan_dict['trans_vlan'] = int(dict_val['trans_vlan'])
                vlan_dict['operation'] = dict_val['operation']
                continue

        return ret_dict

# ======================================================
# Parser for 'show interface <interface> human-readable | i drops'
# ======================================================
class ShowInterfaceHumanReadableIncludeDropsSchema(MetaParser):
    """Schema for show interface human-readable include drops"""

    schema = {
        'unknown_protocol_drops': int,
        'size': int,
        'max': int,
        'drops': int,
        'flushes': int,
        'total_output_drops': int
    }

class ShowInterfaceHumanReadableIncludeDrops(ShowInterfaceHumanReadableIncludeDropsSchema):
    """Parser for show interface human-readable include drops"""

    cli_command = 'show interface {interface} human-readable | i drops'

    def cli(self, interface, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(interface=interface))

        #   Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0

        p1 = re.compile(r"^Input queue: (?P<size>\d+)/(?P<max>\d+)/(?P<drops>\d+)/(?P<flushes>\d+)\s+\(size/max/drops/flushes\); Total output drops:\s+(?P<total_output_drops>\d+)$")

        # 0 unknown protocol drops
        p2 = re.compile(r"^(?P<unknown_protocol_drops>\d+)\s+unknown protocol drops$")

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            #   Input queue: 0/2000/0/0 (size/max/drops/flushes); Total output drops: 0
            m = p1.match(line)
            if m:
                dict_val = m.groupdict()
                ret_dict['size'] = int(dict_val['size'])
                ret_dict['max'] = int(dict_val['max'])
                ret_dict['drops'] = int(dict_val['drops'])
                ret_dict['flushes'] = int(dict_val['flushes'])
                ret_dict['total_output_drops'] = int(dict_val['total_output_drops'])
                continue

            # 0 unknown protocol drops
            m = p2.match(line)
            if m:
                dict_val = m.groupdict()
                ret_dict['unknown_protocol_drops'] = int(dict_val['unknown_protocol_drops'])

        return ret_dict

# ========================================================================
# Schema for 'show interface <interface> human-readable'
# ========================================================================
class ShowInterfaceHumanReadableSchema(MetaParser):
    """Schema for show interface human-readable"""

    schema = {
        Any(): str
    }

# ========================================================================
# Parser for 'show interface <interface> human-readable'
# ========================================================================
class ShowInterfaceHumanReadable(ShowInterfaceHumanReadableSchema):
    """Parser for show interface human-readable"""

    cli_command = 'show interface {interface} human-readable'

    def cli(self, interface, output=None):
        if output is None:
            output = self.device.execute(self.cli_command.format(interface=interface))

        # 5 minute input rate 0 bits/sec, 0 packets/sec
        # 5 minute output rate 0 bits/sec, 0 packets/sec
        p1 = re.compile(r'^\d+\s+(minute|seconds)\s+(?P<dir>(input|output))\s+rate\s+(?P<rate>[\S\s]+)\s*,[\S\s\d]+$')

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # 5 minute input rate 0 bits/sec, 0 packets/sec
            # 5 minute output rate 0 bits/sec, 0 packets/sec
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({
                    group['dir']: group['rate']
                })
                continue

        return ret_dict



# ======================================================
# Schema for 'show interfaces transceiver module {mod}'
# ======================================================

class ShowInterfacesTransceiverModuleSchema(MetaParser):
    """Schema for show interfaces transceiver module {mod}"""

    schema = {
        'interface': {
            Any() : {
            Optional('temperature'): str,
            Optional('voltage'): str,
            Optional('current'): str,
            Optional('tx_power'): str,
            Optional('rx_power'): str,
            }
        }
    }

# ======================================================
# Parser for 'show interfaces transceiver module {mod}'
# ======================================================

class ShowInterfacesTransceiverModule(ShowInterfacesTransceiverModuleSchema):
    """Parser for show interfaces transceiver module {mod}"""

    cli_command = 'show interfaces transceiver module {mod}'

    def cli(self, mod, output=None):

        if output is None:
            output = self.device.execute(self.cli_command.format(mod=mod))
        
        #                                             Optical   Optical
        #             Temperature  Voltage  Current   Tx Power  Rx Power
        # Port         (Celsius)    (Volts)  (mA)      (dBm)     (dBm)
        # ---------    -----------  -------  --------  --------  --------
        # Te1/2        50.3       3.25       9.9      -5.7      -4.4

        p1 = re.compile(
            r'^(?P<interface>\S+)\s+'
            r'(?P<temperature>[-+]?\d+(\.\d+)?)\s+'
            r'(?P<voltage>[-+]?\d+(\.\d+)?)\s+'
            r'(?P<current>[-+]?\d+(\.\d+)?)\s+'
            r'(?P<tx_power>[-+]?\d+(\.\d+)?)\s+'
            r'(?P<rx_power>[-+]?\d+(\.\d+)?)$'
        )

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Skip headers or empty lines
            if not line or line.startswith(("Port", "Temperature", "-", "Optical")):
                continue

            #                                             Optical   Optical
            #             Temperature  Voltage  Current   Tx Power  Rx Power
            # Port         (Celsius)    (Volts)  (mA)      (dBm)     (dBm)
            # ---------    -----------  -------  --------  --------  --------
            # Te1/2        50.3       3.25       9.9      -5.7      -4.4
            m = p1.match(line)
            if m:
                group = m.groupdict()
                intf_dict = ret_dict.setdefault('interface', {}).setdefault(group['interface'], {})
                intf_dict['temperature'] = f"{group['temperature']}"
                intf_dict['voltage'] = f"{group['voltage']}"
                intf_dict['current'] = f"{group['current']}"
                intf_dict['tx_power'] = f"{group['tx_power']}"
                intf_dict['rx_power'] = f"{group['rx_power']}"
                continue

        return ret_dict
