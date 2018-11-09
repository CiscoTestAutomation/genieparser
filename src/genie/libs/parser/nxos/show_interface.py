"""show_interface.py

NXOS parsers for the following show commands:
    * show interface
    * show vrf all interface
    * show ip interface vrf all
    * show ipv6 interface detail vrf all
    * show interface switchport
    * show running-config interface <word>
"""

# python
import re

# metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional
                                         
# import parser utils
from genie.libs.parser.utils.common import Common


# ===========================
# Schema for 'show interface'
# ===========================
class ShowInterfaceSchema(MetaParser):
    """Schema for show interface"""

    schema = {
        Any(): 
            {Optional('description'): str,
            Optional('types'): str,
            Optional('parent_interface'): str,
            'oper_status': str,
            Optional('admin_state'): str,
            Optional('dedicated_intface'): bool,
            Optional('line_protocol'): str,
            Optional('autostate'): bool,
            Optional('link_state'): str,
            Optional('phys_address'): str,
            Optional('port_speed'): str,
            Optional('mtu'): int,
            'enabled': bool,
            Optional('mac_address'): str,
            Optional('auto_negotiate'): bool,
            Optional('duplex_mode'): str,
            Optional('port_mode'): str,
            Optional('auto_mdix'): str,
            Optional('switchport_monitor'): str,
            Optional('efficient_ethernet'): str,
            Optional('last_link_flapped'): str,
            Optional('interface_reset'): int,
            Optional('ethertype'): str,
            Optional('beacon'): str,
            Optional('medium'): str,
            Optional('reliability'): str,
            Optional('txload'): str,
            Optional('rxload'): str,
            Optional('delay'): int,
            Optional('flow_control'):
                {Optional('receive'): bool,
                Optional('send'): bool,
            },
            Optional('port_channel'):
                {Optional('port_channel_member'): bool,
                Optional('port_channel_int'): str,
                Optional('port_channel_member_intfs'): list
            },
            Optional('bandwidth'): int,
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
                Optional('in_oversize_frame'): int,
                Optional('in_overrun'): int,
                Optional('in_underrun'): int,
                Optional('in_ignored'): int,
                Optional('in_watchdog'): int,
                Optional('in_bad_etype_drop'): int,
                Optional('in_unknown_protos'): int,
                Optional('in_if_down_drop'): int,
                Optional('in_with_dribble'): int,
                Optional('in_discard'): int,
                Optional('in_octets'): int,
                Optional('in_errors'): int,
                Optional('in_short_frame'): int,
                Optional('in_no_buffer'): int,
                Optional('out_pkts'): int,
                Optional('out_unicast_pkts'): int,
                Optional('out_multicast_pkts'): int,
                Optional('out_broadcast_pkts'): int,
                Optional('out_discard'): int,
                Optional('out_octets'): int,
                Optional('out_jumbo_packets'): int,
                Optional('out_errors'): int,
                Optional('out_collision'): int,
                Optional('out_deferred'): int,
                Optional('out_late_collision'): int,
                Optional('out_lost_carrier'): int,
                Optional('out_no_carrier'): int,
                Optional('out_babble'): int,
                Optional('last_clear'): str,
                Optional('tx'): bool,
                Optional('rx'): bool,
                Optional('out_mac_pause_frames'): int,
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
                     Optional('secondary'): bool,
                     Optional('route_tag'): str
                    },
                },
            },
        }

# ===========================
# Parser for 'show interface'
# ===========================
class ShowInterface(ShowInterfaceSchema):
    """Parser for show interface"""

    def cli(self):
        out = self.device.execute('show interface')

        interface_dict = {}

        rx = False
        tx = False
        for line in out.splitlines():
            line = line.replace('\t', '    ')
            line = line.rstrip()


            # Ethernet2/1.10 is down (Administratively down)
            p1 =  re.compile(r'^\s*(?P<interface>[a-zA-Z0-9\/\.\-]+) *is'
                              ' *(?P<enabled>(down))'
                              '( *\((?P<link_state>[a-zA-Z0-9\-\s]+)\))?$')
            m = p1.match(line)
            if m:
                interface = m.groupdict()['interface']
                enabled = m.groupdict()['enabled']
                link_state = m.groupdict()['link_state']

                if interface not in interface_dict:
                    interface_dict[interface] = {}
                    interface_dict[interface]['port_channel'] = {}
                    interface_dict[interface]['port_channel']\
                        ['port_channel_member'] = False
                if link_state:
                    interface_dict[interface]\
                                ['link_state'] = link_state

                interface_dict[interface]['enabled'] = False
                interface_dict[interface]['oper_status'] = 'down'
                continue

            # Vlan1 is down (Administratively down), line protocol is down, autostate enabled
            # Vlan23 is administratively down (Administratively down), line protocol is down, autostate enabled
            p1_1 =  re.compile(r'^\s*(?P<interface>[a-zA-Z0-9\/\.\-]+) *is'
                              ' *(?P<enabled>[\w\s]+)'
                              '( *\((?P<link_state>[\w\-\/\s]+)\))?, +'
                              'line +protocol +is +(?P<line_protocol>\w+),? *'
                              '(autostate +(?P<autostate>\w+))?$')
            m = p1_1.match(line)
            if m:
                interface = m.groupdict()['interface']
                enabled = m.groupdict()['enabled']
                link_state = m.groupdict()['link_state']
                line_protocol = m.groupdict()['line_protocol']
                autostate = m.groupdict()['autostate']

                if interface not in interface_dict:
                    interface_dict[interface] = {}
                    interface_dict[interface]['port_channel'] = {}
                    interface_dict[interface]['port_channel']\
                        ['port_channel_member'] = False
                if link_state:
                    interface_dict[interface]\
                                ['link_state'] = link_state

                if enabled:
                    enabled = enabled.lower()
                    interface_dict[interface]['enabled'] = False if 'down' in enabled else True
                    interface_dict[interface]['oper_status'] = enabled.strip()
                if line_protocol:
                    interface_dict[interface]['line_protocol'] = line_protocol.lower()
                if autostate:
                    interface_dict[interface]['autostate'] = True if \
                        autostate.lower() == 'enabled' else False

                continue

            # Ethernet2/2 is up
            p1_2 =  re.compile(r'^\s*(?P<interface>[a-zA-Z0-9\/\.\-]+) *is'
                              ' *(?P<enabled>(up))'
                              '( *\((?P<link_state>[a-zA-Z\s]+)\))?$')
            m = p1_2.match(line)
            if m:
                interface = m.groupdict()['interface']
                enabled = m.groupdict()['enabled']
                link_state = m.groupdict()['link_state']

                if interface not in interface_dict:
                    interface_dict[interface] = {}
                    interface_dict[interface]['port_channel'] = {}
                    interface_dict[interface]['port_channel']\
                        ['port_channel_member'] = False
                if link_state:
                    interface_dict[interface]\
                                ['link_state'] = link_state

                interface_dict[interface]['enabled'] = True
                interface_dict[interface]['oper_status'] = 'up'
                continue

            # admin state is up
            # admin state is up,
            # admin state is up, Dedicated Interface
            # admin state is up, Dedicated Interface, [parent interface is Ethernet2/1]
            p2 = re.compile(r'^\s*admin +state +is'
                             ' +(?P<admin_state>([a-zA-Z0-9\/\.]+))(?:,)?'
                             '(?: +(?P<dedicated_intf>(Dedicated Interface)))?'
                             '(?:, +\[parent +interface +is'
                             ' +(?P<parent_intf>(\S+))\])?$')
            m = p2.match(line)
            if m:
                # admin_state
                interface_dict[interface]['admin_state'] = \
                    m.groupdict()['admin_state']
                # dedicated_interface
                if m.groupdict()['dedicated_intf']:
                    interface_dict[interface]['dedicated_intface'] = True
                # parent_interface
                if m.groupdict()['parent_intf']:
                    interface_dict[interface]['parent_interface'] = \
                        m.groupdict()['parent_intf']
                continue

            # Dedicated Interface
            p2_1 = re.compile(r'^\s*Dedicated Interface$')
            m = p2_1.match(line)
            if m:
                interface_dict[interface]['dedicated_intface'] = True
                continue

            # Belongs to Po1
            p2_2 = re.compile(r'^\s*Belongs *to *(?P<port_channel_int>[a-zA-Z0-9]+)$')
            m = p2_2.match(line)
            if m:
                port_channel_int = str(m.groupdict()['port_channel_int'])
                if 'port_channel' not in interface_dict[interface]:
                    interface_dict[interface]['port_channel'] = {}
                interface_dict[interface]['port_channel']\
                    ['port_channel_member'] = True
                interface_dict[interface]['port_channel']\
                    ['port_channel_int'] = Common.convert_intf_name(port_channel_int)
                continue

            # Hardware: Ethernet, address: 5254.00c9.d26e (bia 5254.00c9.d26e)
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
            p4 = re.compile(r'^\s*Description: *(?P<description>.*)$')
            m = p4.match(line)
            if m:
                description = m.groupdict()['description']

                interface_dict[interface]['description'] = description
                continue

            #Internet Address is 10.4.4.4/24 secondary tag 10
            p5 = re.compile(r'^\s*Internet *Address *is *(?P<ip>[0-9\.]+)'
                             '\/(?P<prefix_length>[0-9]+)'
                             '(?: *(?P<secondary>(secondary)))?(?: *tag'
                             ' *(?P<route_tag>[0-9]+))?$')
            m = p5.match(line)
            if m:
                ip = m.groupdict()['ip']
                prefix_length = str(m.groupdict()['prefix_length'])
                secondary = m.groupdict()['secondary']
                route_tag = m.groupdict()['route_tag']
                #address = ipv4+prefix_length
                address = ip + '/' + prefix_length
                if 'ipv4' not in interface_dict[interface]:
                    interface_dict[interface]['ipv4'] = {}
                if address not in interface_dict[interface]['ipv4']:
                    interface_dict[interface]['ipv4'][address] = {}

                interface_dict[interface]['ipv4'][address]\
                ['ip'] = ip
                interface_dict[interface]['ipv4'][address]\
                ['prefix_length'] = prefix_length

                if secondary:
                    interface_dict[interface]['ipv4'][address]\
                    ['secondary'] = True
                if route_tag:
                    interface_dict[interface]['ipv4'][address]\
                    ['route_tag'] = route_tag
                continue
            
            # MTU 1600 bytes, BW 768 Kbit, DLY 3330 usec
            # MTU 1500 bytes, BW 1000000 Kbit, DLY 10 usec,
            # MTU 1500 bytes, BW 1000000 Kbit
            p6 = re.compile(r'^\s*MTU *(?P<mtu>[0-9]+) *bytes, *BW'
                             ' *(?P<bandwidth>[0-9]+) *Kbit(, *DLY'
                             ' *(?P<delay>[0-9]+) *usec)?,?$')
            m = p6.match(line)
            if m:
                mtu = int(m.groupdict()['mtu'])
                bandwidth = int(m.groupdict()['bandwidth'])
                if m.groupdict()['delay']:
                    interface_dict[interface]['delay'] = int(m.groupdict()['delay'])
                
                interface_dict[interface]['mtu'] = mtu
                interface_dict[interface]['bandwidth'] = bandwidth
                continue
            
            # MTU 1500 bytes,  BW 40000000 Kbit,, BW 40000000 Kbit, DLY 10 usec
            p6_1 = re.compile(r'^\s*MTU *(?P<mtu>[0-9]+) *bytes, *BW'
                             ' *(?P<bandwidth>[0-9]+) *Kbit, *,? *BW'
                             ' *([0-9]+) *Kbit, *DLY'
                             ' *(?P<delay>[0-9]+) *usec$')
            m = p6_1.match(line)
            if m:
                mtu = int(m.groupdict()['mtu'])
                bandwidth = int(m.groupdict()['bandwidth'])
                
                interface_dict[interface]['mtu'] = mtu
                interface_dict[interface]['bandwidth'] = bandwidth
                interface_dict[interface]['delay'] = int(m.groupdict()['delay'])
                continue

            # reliability 255/255, txload 1/255, rxload 1/255
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
                encapsulation = m.groupdict()['encapsulation'].lower()
                encapsulation = encapsulation.replace("802.1q virtual lan","dot1q")
                medium = m.groupdict()['medium']

                if 'encapsulations' not in interface_dict[interface]:
                    interface_dict[interface]['encapsulations'] = {}

                interface_dict[interface]['encapsulations']\
                ['encapsulation'] = encapsulation
                interface_dict[interface]['medium'] = medium
                continue

            p8_1 = re.compile(r'^\s*Encapsulation *(?P<encapsulation>[a-zA-Z0-9\.\s]+),'
                               ' *Vlan *ID *(?P<first_dot1q>[0-9]+),'
                               ' *medium *is *(?P<medium>[a-z0-9]+)$')
            m = p8_1.match(line)
            if m:
                encapsulation = m.groupdict()['encapsulation'].lower()
                encapsulation = encapsulation.replace("802.1q virtual lan","dot1q")
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

            # Encapsulation ARPA, loopback not set
            p8_2 = re.compile(r'^\s*Encapsulation *(?P<encapsulation>[a-zA-Z0-9\.\s]+),'
                             ' *([\w\s]+)$')
            m = p8_2.match(line)
            if m:
                encapsulation = m.groupdict()['encapsulation'].lower()

                if 'encapsulations' not in interface_dict[interface]:
                    interface_dict[interface]['encapsulations'] = {}

                interface_dict[interface]['encapsulations']\
                ['encapsulation'] = encapsulation
                continue

            #Port mode is routed
            p9 = re.compile(r'^\s*Port *mode *is *(?P<port_mode>[a-z]+)$')
            m = p9.match(line)
            if m:
                port_mode = m.groupdict()['port_mode']
                interface_dict[interface]['port_mode'] = port_mode
                continue

            # auto-duplex, auto-speed
            p10_1 = re.compile(r'^\s*auto-duplex, +auto-speed$')
            m = p10_1.match(line)
            if m:
                # not caring for this line
                continue

            #full-duplex, 1000 Mb/s
            # auto-duplex, auto-speed
            p10 = re.compile(r'^\s*(?P<duplex_mode>[a-z]+)-duplex,'
                              ' *(?P<port_speed>[a-z0-9\-]+)(?: *Mb/s)?$')
            m = p10.match(line)
            if m:
                duplex_mode = m.groupdict()['duplex_mode'].lower()
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

            #Auto-Negotiation is turned on
            p12_1 = re.compile(r'^\s*Auto-Negotiation *is *turned'
                              ' *(?P<auto_negotiate>(on))$')
            m = p12_1.match(line)
            if m:
                auto_negotiation = m.groupdict()['auto_negotiate']
                interface_dict[interface]['auto_negotiate'] = True
                continue

            #Input flow-control is off, output flow-control is off
            p13 = re.compile(r'^\s*Input *flow-control *is *(?P<receive>(off)+),'
                              ' *output *flow-control *is *(?P<send>(off)+)$')
            m = p13.match(line)
            if m:
                receive = m.groupdict()['receive']
                send = m.groupdict()['send']

                if 'flow_control' not in interface_dict[interface]:
                    interface_dict[interface]['flow_control'] = {}

                interface_dict[interface]['flow_control']['receive'] = False
                interface_dict[interface]['flow_control']['send'] = False
                continue
            #Input flow-control is off, output flow-control is on
            p13_1 = re.compile(r'^\s*Input *flow-control *is *(?P<receive>(on)+),'
                                ' *output *flow-control *is *(?P<send>(on)+)$')
            m = p13_1.match(line)
            if m:
                receive = m.groupdict()['receive']
                send = m.groupdict()['send']

                if 'flow_control' not in interface_dict[interface]:
                    interface_dict[interface]['flow_control'] = {}

                interface_dict[interface]['flow_control']['receive'] = True
                interface_dict[interface]['flow_control']['send'] = True
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
            p16 = re.compile(r'^\s*EtherType *is *(?P<ethertype>[a-z0-9]+)$')
            m = p16.match(line)
            if m:
                ethertype = m.groupdict()['ethertype']
                interface_dict[interface]['ethertype'] = ethertype
                continue

            # Members in this channel: Eth1/15, Eth1/16
            # Members in this channel: Eth1/28
            p38 = re.compile(r'^\s*Members +in +this +channel *: *'
                              '(?P<port_channel_member_intfs>[\w\/\.\-\,\s]+)$')
            m = p38.match(line)
            if m:
                port_channel_member_intfs = m.groupdict()['port_channel_member_intfs']
                if port_channel_member_intfs:
                    if 'port_channel' not in interface_dict[interface]:
                        interface_dict[interface]['port_channel'] = {}
                    interface_dict[interface]['port_channel']\
                        ['port_channel_member'] = True
                    interface_dict[interface]['port_channel']\
                        ['port_channel_member_intfs'] = [Common.convert_intf_name(item) \
                                for item in port_channel_member_intfs.split(',')]
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
                              ' *(?P<last_link_flapped>[a-z0-9\:]+)$')
            m = p18.match(line)
            if m:
                last_link_flapped = m.groupdict()['last_link_flapped']
                interface_dict[interface]['last_link_flapped']\
                 = last_link_flapped
                continue

            # Last clearing of "show interface" counters never
            p19 = re.compile(r'^\s*Last *clearing *of *\"show *interface\"'
                              ' *counters *(?P<last_clear>[a-z0-9\:]+)$')
            m = p19.match(line)
            if m:
                last_clear = m.groupdict()['last_clear']
                continue

            # Last clearing of "" counters 00:15:42
            p19_1 = re.compile(r'^\s*Last *clearing *of *\" *\"'
                              ' *counters *(?P<last_clear>[a-z0-9\:]+)$')
            m = p19_1.match(line)
            if m:
                last_clear = m.groupdict()['last_clear']
                continue

            #1 interface resets
            p20 = re.compile(r'^\s*(?P<interface_reset>[0-9]+) *interface'
                              ' *resets$')
            m = p20.match(line)
            if m:
                interface_reset = int(m.groupdict()['interface_reset'])
                interface_dict[interface]['interface_reset'] = interface_reset
                continue

            # 1 minute input rate 0 bits/sec, 0 packets/sec  
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
            
            p23_1 = re.compile(r'^\s*(?P<rx>(RX))$')
            m = p23_1.match(line)
            if m:
                rx = m.groupdict()['rx']
                if 'counters' not in interface_dict[interface]:
                    interface_dict[interface]['counters'] = {}

                interface_dict[interface]['counters']['rx'] = True
                continue

            if rx:
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
                    try:
                        interface_dict[interface]['counters']['last_clear'] = last_clear
                    except Exception:
                        pass
                    continue
                    

            #0 input packets  0 bytes
            p25 = re.compile(r'^\s*(?P<in_pkts>[0-9]+) +input +packets'
                              ' +(?P<in_octets>[0-9]+) +bytes$')
            m = p25.match(line)
            if m:
                in_pkts = int(m.groupdict()['in_pkts'])
                in_octets = int(m.groupdict()['in_octets'])
                if 'counters' not in interface_dict[interface]:
                    interface_dict[interface]['counters'] = {}

                interface_dict[interface]['counters']['in_pkts'] = in_pkts
                interface_dict[interface]['counters']['in_octets'] = in_octets
                continue

            #0 jumbo packets  0 storm suppression packets
            p26 = re.compile(r'^\s*(?P<in_jumbo_packets>[0-9]+) +jumbo +packets'
                              ' *(?P<in_storm_suppression_packets>[0-9]+)'
                              ' *storm *suppression *packets$')
            m = p26.match(line)
            if m:
                in_jumbo_packets = int(m.groupdict()['in_jumbo_packets'])
                in_storm_suppression_packets = int(m.groupdict()['in_storm_suppression_packets'])

                interface_dict[interface]['counters']['in_jumbo_packets']= in_jumbo_packets
                interface_dict[interface]['counters']\
                ['in_storm_suppression_packets'] = in_storm_suppression_packets
                continue

            #0 runts  0 giants  0 CRC/FCS  0 no buffer
            #0 runts  0 giants  0 CRC  0 no buffer
            p27 = re.compile(r'^\s*(?P<in_runts>[0-9]+) *runts'
                              ' *(?P<in_oversize_frame>[0-9]+) *giants'
                              ' *(?P<in_crc_errors>[0-9]+) *CRC(/FCS)?'
                              ' *(?P<in_no_buffer>[0-9]+) *no *buffer$')
            m = p27.match(line)
            if m:

                interface_dict[interface]['counters']['in_runts'] = int(m.groupdict()['in_runts'])
                interface_dict[interface]['counters']['in_oversize_frame'] = int(m.groupdict()['in_oversize_frame'])
                interface_dict[interface]['counters']['in_crc_errors'] = int(m.groupdict()['in_crc_errors'])
                interface_dict[interface]['counters']['in_no_buffer'] = int(m.groupdict()['in_no_buffer'])
                continue

            #0 input error  0 short frame  0 overrun   0 underrun  0 ignored
            p28 = re.compile(r'^\s*(?P<in_errors>[0-9]+) *input *error'
                              ' *(?P<in_short_frame>[0-9]+) *short *frame'
                              ' *(?P<in_overrun>[0-9]+) *overrun *(?P<in_underrun>[0-9]+)'
                              ' *underrun *(?P<in_ignored>[0-9]+) *ignored$')
            m = p28.match(line)
            if m:

                interface_dict[interface]['counters']['in_errors'] = int(m.groupdict()['in_errors'])
                interface_dict[interface]['counters']['in_short_frame'] = int(m.groupdict()['in_short_frame'])
                interface_dict[interface]['counters']['in_overrun'] = int(m.groupdict()['in_overrun'])
                interface_dict[interface]['counters']['in_underrun'] = int(m.groupdict()['in_underrun'])
                interface_dict[interface]['counters']['in_ignored'] = int(m.groupdict()['in_ignored'])
                continue

            #0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
            p29 = re.compile(r'^\s*(?P<in_watchdog>[0-9]+) *watchdog'
                              ' *(?P<in_bad_etype_drop>[0-9]+)'
                              ' *bad *etype *drop *(?P<in_unknown_protos>[0-9]+)'
                              ' *bad *proto'
                              ' *drop *(?P<in_if_down_drop>[0-9]+) *if *down *drop$')
            m = p29.match(line)
            if m:

                interface_dict[interface]['counters']['in_watchdog'] = int(m.groupdict()['in_watchdog'])
                interface_dict[interface]['counters']['in_bad_etype_drop'] = int(m.groupdict()['in_bad_etype_drop'])
                interface_dict[interface]['counters']['in_unknown_protos'] = int(m.groupdict()['in_unknown_protos'])
                interface_dict[interface]['counters']['in_if_down_drop'] = int(m.groupdict()['in_if_down_drop'])
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
                
            p31_1 = re.compile(r'^\s*(?P<tx>(TX))$')
            m = p31_1.match(line)
            if m:
                rx = False
                tx = m.groupdict()['tx']
                if 'counters' not in interface_dict[interface]:
                    interface_dict[interface]['counters'] = {}
                interface_dict[interface]['counters']['tx'] = True
                continue
                
            if tx:
                #0 unicast packets  0 multicast packets  0 broadcast packets
                p32 = re.compile(r'^\s*(?P<out_unicast_pkts>[0-9]+) *unicast *packets'
                                  ' *(?P<out_multicast_pkts>[0-9]+) *multicast *packets'
                                  ' *(?P<out_broadcast_pkts>[0-9]+) *broadcast *packets$')
                m = p32.match(line)
                if m:
                    interface_dict[interface]['counters']['out_unicast_pkts'] = int(m.groupdict()['out_unicast_pkts'])
                    interface_dict[interface]['counters']['out_multicast_pkts'] = int(m.groupdict()['out_multicast_pkts'])
                    interface_dict[interface]['counters']['out_broadcast_pkts'] = int(m.groupdict()['out_broadcast_pkts'])
                    continue

            #0 output packets  0 bytes
            p33 = re.compile(r'^\s*(?P<out_pkts>[0-9]+) *output *packets'
                              ' *(?P<out_octets>[0-9]+) *bytes$')
            m = p33.match(line)
            if m:
                out_pkts = int(m.groupdict()['out_pkts'])
                out_octets = int(m.groupdict()['out_octets'])

                interface_dict[interface]['counters']['out_pkts'] = out_pkts
                interface_dict[interface]['counters']['out_octets'] = out_octets
                continue

            #0 jumbo packets
            p34 = re.compile(r'^\s*(?P<out_jumbo_packets>[0-9]+) *jumbo *packets$')
            m = p34.match(line)
            if m:
                out_jumbo_packets = int(m.groupdict()['out_jumbo_packets'])

                interface_dict[interface]['counters']['out_jumbo_packets'] = out_jumbo_packets
                continue

            #0 output error  0 collision  0 deferred  0 late collision
            p35 = re.compile(r'^\s*(?P<out_errors>[0-9]+) *output *error'
                              ' *(?P<out_collision>[0-9]+) *collision'
                              ' *(?P<out_deferred>[0-9]+) *deferred'
                              ' *(?P<out_late_collision>[0-9]+)'
                              ' *late *collision$')
            m = p35.match(line)
            if m:
                interface_dict[interface]['counters']['out_errors'] = int(m.groupdict()['out_errors'])
                interface_dict[interface]['counters']['out_collision'] = int(m.groupdict()['out_collision'])
                interface_dict[interface]['counters']['out_deferred'] = int(m.groupdict()['out_deferred'])
                interface_dict[interface]['counters']['out_late_collision'] = int(m.groupdict()['out_late_collision'])
                continue

            #0 lost carrier  0 no carrier  0 babble  0 output discard
            p36 = re.compile(r'^\s*(?P<out_lost_carrier>[0-9]+) *lost *carrier'
                              ' *(?P<out_no_carrier>[0-9]+) *no *carrier'
                              ' *(?P<out_babble>[0-9]+) *babble'
                              ' *(?P<out_discard>[0-9]+) *output *discard$')
            m = p36.match(line)
            if m:

                interface_dict[interface]['counters']['out_lost_carrier'] = int(m.groupdict()['out_lost_carrier'])
                interface_dict[interface]['counters']['out_no_carrier'] = int(m.groupdict()['out_no_carrier'])
                interface_dict[interface]['counters']['out_babble'] = int(m.groupdict()['out_babble'])
                interface_dict[interface]['counters']['out_discard'] = int(m.groupdict()['out_discard'])
                continue

            #0 Tx pause
            p37 = re.compile(r'^\s*(?P<out_mac_pause_frames>[0-9]+) *Tx *pause$')
            m = p37.match(line)
            if m:
                out_mac_pause_frames = int(m.groupdict()['out_mac_pause_frames'])

                interface_dict[interface]['counters']['out_mac_pause_frames'] = out_mac_pause_frames
                continue

        return interface_dict


# ===================================
# Schema for 'show interface vrf all'
# ===================================
class ShowIpInterfaceVrfAllSchema(MetaParser):
    """Schema for show ip interface vrf all"""

    schema = {
    Any():
        {'vrf': str,
         'interface_status': str,
         'iod': int,
         Optional('ipv4'):
            {Any():
                {Optional('ip'): str,
                 Optional('prefix_length'): str,
                 Optional('secondary'): bool,
                 Optional('route_tag'): str,
                 Optional('ip_subnet'): str,
                 Optional('broadcast_address'): str,
                 Optional('route_preference'): str,
                },            
            Optional('unnumbered'):
                {'interface_ref': str,
            },       
            'counters':
                {'unicast_packets_sent': int,
                 'unicast_packets_received': int,
                 'unicast_packets_forwarded': int,
                 'unicast_packets_originated': int,
                 'unicast_packets_consumed': int,
                 'unicast_bytes_sent': int,
                 'unicast_bytes_received': int,
                 'unicast_bytes_forwarded': int,
                 'unicast_bytes_originated': int,
                 'unicast_bytes_consumed': int,
                 'multicast_packets_sent': int,
                 'multicast_packets_received': int,
                 'multicast_packets_forwarded': int,
                 'multicast_packets_originated': int,
                 'multicast_packets_consumed': int,
                 'multicast_bytes_sent': int,
                 'multicast_bytes_received': int,
                 'multicast_bytes_forwarded': int,
                 'multicast_bytes_originated': int,
                 'multicast_bytes_consumed': int,
                 'broadcast_packets_sent': int,
                 'broadcast_packets_received': int,
                 'broadcast_packets_forwarded': int,
                 'broadcast_packets_originated': int,
                 'broadcast_packets_consumed': int,
                 'broadcast_bytes_sent': int,
                 'broadcast_bytes_received': int,
                 'broadcast_bytes_forwarded': int,
                 'broadcast_bytes_originated': int,
                 'broadcast_bytes_consumed': int,
                 'labeled_packets_sent': int,
                 'labeled_packets_received': int,
                 'labeled_packets_forwarded': int,
                 'labeled_packets_originated': int,
                 'labeled_packets_consumed': int,
                 'labeled_bytes_sent': int,
                 'labeled_bytes_received': int,
                 'labeled_bytes_forwarded': int,
                 'labeled_bytes_originated': int,
                 'labeled_bytes_consumed': int,
                },
            },     
         Optional('multicast_groups'): list,
         Optional('multicast_groups_address'): str,
         'ip_mtu': int,
         'proxy_arp': str,
         'local_proxy_arp': str,
         'multicast_routing': str,
         'icmp_redirects': str,
         'directed_broadcast': str,
         Optional('ip_forwarding'): str,
         'icmp_unreachable': str,
         'icmp_port_unreachable': str,
         'unicast_reverse_path': str,
         'load_sharing': str,
         'int_stat_last_reset': str,
         'wccp_redirect_outbound': str,
         'wccp_redirect_inbound': str,
         'wccp_redirect_exclude': str
        },
    }   

# ===================================
# Parser for 'show interface vrf all'
# ===================================
class ShowIpInterfaceVrfAll(ShowIpInterfaceVrfAllSchema):
    """Parser for show ip interface vrf all"""

    def cli(self):
        out = self.device.execute('show ip interface vrf all')

        ip_interface_vrf_all_dict = {}
        temp_intf = []

        for line in out.splitlines():
            line = line.rstrip()

            # IP Interface Status for VRF "VRF1"
            p1 = re.compile(r'^\s*IP *Interface *Status *for *VRF'
                             ' *(?P<vrf>\S+)$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                vrf = vrf.replace('"',"")
                continue

            #Ethernet2/1, Interface status: protocol-up/link-up/admin-up, iod: 36,
            p2 = re.compile(r'^\s*(?P<interface>[a-zA-Z0-9\/\-\.]+), *Interface'
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

                #init multicast groups list to empty for this interface
                multicast_groups = []
                unnumbered_intf = None
                # unnumbered interface didn't share the same information
                temp_intf = None

                # check if the ipv4 and address already assgined during the unnumbered block
                if 'ipv4' in ip_interface_vrf_all_dict[interface]:
                    for key in ip_interface_vrf_all_dict[interface]['ipv4'].keys():
                        if re.match('^\d+.\d+.\d+.\d+\/\d+', key):
                            address = key
                continue
                

            # Unnumbered interfaces of loopback0: first iod 46
            p2_1 = re.compile(r'^\s*Unnumbered +interfaces +of +(?P<unnumbered_intf>[\w\.\/]+): *'
                               'first +iod +(?P<first_iod>\d+)$')
            m = p2_1.match(line)
            if m:
                unnumbered_intf = m.groupdict()['unnumbered_intf']
                continue

            # Ethernet2/11:
            # mti18: tunnel-te11: tunnel-te12:
            p2_2 = re.compile(r'(([E|e]thernet|[L|l]oopback|[T|t]unnel|[V|v]lan|mti|[t|T]unnel-te|[p|P]ort-channel)[\d\/\.]+):')
            m = p2_2.findall(line)
            if m and unnumbered_intf:
                temp_intf = []
                temp_intf = [i[0] for i in m]
                for intf in temp_intf:
                    if intf not in ip_interface_vrf_all_dict:
                        ip_interface_vrf_all_dict[intf] = {}
                continue

            # IP address: 10.4.4.4, IP subnet: 10.4.4.0/24 secondary
            # IP address: 4.4.4.4, IP subnet: 4.4.4.0/24
            p3 = re.compile(r'^\s*IP *address: *(?P<ip>[0-9\.]+), *IP'
                             ' *subnet: *(?P<ip_subnet>[a-z0-9\.]+)\/'
                             '(?P<prefix_length>[0-9]+)'
                             ' *(?P<secondary>(secondary))?$')
            m = p3.match(line)
            if m:
                ip = m.groupdict()['ip']
                ip_subnet = m.groupdict()['ip_subnet']
                prefix_length = m.groupdict()['prefix_length']
                secondary = m.groupdict()['secondary']

                address = ip + '/' + prefix_length

                if temp_intf:
                    temp_intf.append(interface)
                    intf_lst = temp_intf
                else:
                    intf_lst = [interface]

                for intf in intf_lst:
                    if 'ipv4' not in ip_interface_vrf_all_dict[intf]:
                        ip_interface_vrf_all_dict[intf]['ipv4'] = {}

                    if address not in ip_interface_vrf_all_dict[intf]['ipv4']:
                        ip_interface_vrf_all_dict[intf]['ipv4'][address] = {}

                    ip_interface_vrf_all_dict[intf]['ipv4'][address]\
                        ['ip'] = ip
                    ip_interface_vrf_all_dict[intf]['ipv4'][address]\
                        ['ip_subnet'] = ip_subnet
                    ip_interface_vrf_all_dict[intf]['ipv4'][address]\
                        ['prefix_length'] = prefix_length
                    if secondary:
                        ip_interface_vrf_all_dict[intf]['ipv4'][address]\
                            ['secondary'] = True
                    else:
                        ip_interface_vrf_all_dict[intf]['ipv4'][address]\
                            ['secondary'] = False

                continue

            # IP address: 201.1.34.1, IP subnet: 201.1.34.0/24 route-preference: 0, tag: 0
            p3_1 = re.compile(r'^\s*IP *address: *(?P<ip>[0-9\.]+), *IP'
                               ' *subnet: *(?P<ip_subnet>[a-z0-9\.]+)\/'
                               '(?P<prefix_length>[0-9\,]+)(?: *route-preference:'
                               ' *(?P<route_preference>[0-9]+),)?(?: *tag:'
                               ' *(?P<route_tag>[0-9]+))?$')
            m = p3_1.match(line)
            if m:
                ip = m.groupdict()['ip']
                ip_subnet = m.groupdict()['ip_subnet']
                prefix_length = m.groupdict()['prefix_length']
                route_tag = m.groupdict()['route_tag']
                route_preference = m.groupdict()['route_preference']

                address = ip + '/' + prefix_length

                if temp_intf:
                    temp_intf.append(interface)
                    intf_lst = temp_intf
                    # unnumbered interface didn't share the same information
                    temp_intf = None
                else:
                    intf_lst = [interface]

                for intf in intf_lst:
                    if 'ipv4' not in ip_interface_vrf_all_dict[intf]:
                        ip_interface_vrf_all_dict[intf]['ipv4'] = {}

                    if address not in ip_interface_vrf_all_dict[intf]['ipv4']:
                        ip_interface_vrf_all_dict[intf]['ipv4'][address] = {}

                    ip_interface_vrf_all_dict[intf]['ipv4'][address]\
                        ['ip'] = ip
                    ip_interface_vrf_all_dict[intf]['ipv4'][address]\
                        ['ip_subnet'] = ip_subnet
                    ip_interface_vrf_all_dict[intf]['ipv4'][address]\
                        ['prefix_length'] = prefix_length
                    if route_tag:
                        ip_interface_vrf_all_dict[intf]['ipv4'][address]\
                        ['route_tag'] = route_tag
                    if route_preference:
                        ip_interface_vrf_all_dict[intf]['ipv4'][address]\
                        ['route_preference'] = route_preference
                continue

            #IP broadcast address: 255.255.255.255
            p4 = re.compile(r'^\s*IP *broadcast *address:'
                             ' *(?P<broadcast_address>[0-9\.]+)$')
            m = p4.match(line)
            if m:
                broadcast_address = str(m.groupdict()['broadcast_address'])
                if 'ipv4' in ip_interface_vrf_all_dict[interface]:
                    ip_interface_vrf_all_dict[interface]['ipv4'][address]['broadcast_address'] = broadcast_address
                continue
            
            #IP multicast groups locally joined: none
            #224.0.0.6  224.0.0.5  224.0.0.2 
            p5 = re.compile(r'^\s*IP *multicast *groups *locally *joined:'
                             ' *(?P<multicast_groups_address>[a-z]+)$')
            m = p5.match(line)
            if m:
                multicast_groups_address = m.groupdict()['multicast_groups_address']

                ip_interface_vrf_all_dict[interface]['multicast_groups_address']\
                = multicast_groups_address
                continue

            #224.0.0.6  224.0.0.5  224.0.0.2 
            p5_1 = re.compile(r'^\s*(?P<multicast_groups_address>[a-z0-9\.\s]+)$')
            m = p5_1.match(line)
            if m:
                multicast_groups_address = str(m.groupdict()['multicast_groups_address'])

                #Split string of addressed into a list
                multicast_groups_address = [str(i) for i in multicast_groups_address.split()]
                
                #Add to previous created list
                for mgroup in multicast_groups_address:
                    multicast_groups.append(mgroup)

                ip_interface_vrf_all_dict[interface]['multicast_groups']\
                 = sorted(multicast_groups)
                continue

            #IP MTU: 1600 bytes (using link MTU)
            p6 = re.compile(r'^\s*IP *MTU: *(?P<ip_mtu>[0-9]+)'
                             ' *bytes *\(using *link *MTU\)$')
            m = p6.match(line)
            if m:
                ip_mtu = int(m.groupdict()['ip_mtu'])

                ip_interface_vrf_all_dict[interface]['ip_mtu'] = ip_mtu
                continue

            #IP primary address route-preference: 0, tag: 0
            p7 = re.compile(r'^\s*IP *primary *address *route-preference:'
                             ' *(?P<route_preference>[0-9]+), *tag:'
                             ' *(?P<route_tag>[0-9]+)$')
            m = p7.match(line)
            if m:
                route_preference = m.groupdict()['route_preference']
                route_tag = m.groupdict()['route_tag']

                if route_preference:
                    ip_interface_vrf_all_dict[interface]['ipv4'][address]['route_preference']\
                     = route_preference

                if route_tag:
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
                              ' *(?P<int_stat_last_reset>[a-zA-Z0-9\:]+)')
            m = p18.match(line)
            if m:
                int_stat_last_reset = m.groupdict()['int_stat_last_reset']

                ip_interface_vrf_all_dict[interface]['int_stat_last_reset']\
                 = int_stat_last_reset
                continue

            # IP interface software stats: (sent/received/forwarded/originated/consumed)
            # Unicast packets    : 0/0/0/0/0
            # Unicast bytes      : 0/0/0/0/0
            # Multicast packets  : 0/0/0/0/0
            # Multicast bytes    : 0/0/0/0/0
            # Broadcast packets  : 0/0/0/0/0
            # Broadcast bytes    : 0/0/0/0/0
            # Labeled packets    : 0/0/0/0/0
            # Labeled bytes      : 0/0/0/0/0
            try:
                interface
            except Exception:
                continue

            if 'ipv4' in ip_interface_vrf_all_dict[interface]:
                #Unicast packets    : 0/0/0/0/0
                p20 = re.compile(r'^\s*Unicast *packets *:'
                                  ' *(?P<unicast_packets_sent>[0-9]+)\/'
                                  '(?P<unicast_packets_received>[0-9]+)\/'
                                  '(?P<unicast_packets_forwarded>[0-9]+)\/'
                                  '(?P<unicast_packets_originated>[0-9]+)\/'
                                  '(?P<unicast_packets_consumed>[0-9]+)$')
                m = p20.match(line)
                if m:
                    if 'counters' not in ip_interface_vrf_all_dict[interface]['ipv4'][address]:
                        ip_interface_vrf_all_dict[interface]['ipv4']['counters'] = {}

                    ip_interface_vrf_all_dict[interface]['ipv4']['counters']\
                    ['unicast_packets_sent']= int(m.groupdict()['unicast_packets_sent'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters']\
                    ['unicast_packets_received']= int(m.groupdict()['unicast_packets_received'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters']\
                    ['unicast_packets_forwarded']= int(m.groupdict()['unicast_packets_forwarded'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters']\
                    ['unicast_packets_originated']= int(m.groupdict()['unicast_packets_originated'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters']\
                    ['unicast_packets_consumed']= int(m.groupdict()['unicast_packets_consumed'])
                    continue

                #Unicast bytes      : 0/0/0/0/0
                p21 = re.compile(r'^\s*Unicast *bytes *:'
                                  ' *(?P<unicast_bytes_sent>[0-9]+)\/'
                                  '(?P<unicast_bytes_received>[0-9]+)\/'
                                  '(?P<unicast_bytes_forwarded>[0-9]+)\/'
                                  '(?P<unicast_bytes_originated>[0-9]+)\/'
                                  '(?P<unicast_bytes_consumed>[0-9]+)$')
                m = p21.match(line)
                if m:
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters']\
                    ['unicast_bytes_sent']= int(m.groupdict()['unicast_bytes_sent'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters']\
                    ['unicast_bytes_received']= int(m.groupdict()['unicast_bytes_received'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters']\
                    ['unicast_bytes_forwarded']= int(m.groupdict()['unicast_bytes_forwarded'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters']\
                    ['unicast_bytes_originated']= int(m.groupdict()['unicast_bytes_originated'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters']\
                    ['unicast_bytes_consumed']= int(m.groupdict()['unicast_bytes_consumed'])
                    continue

                #Multicast packets  : 0/0/0/0/0
                p22 = re.compile(r'^\s*Multicast *packets *:'
                                  ' *(?P<multicast_packets_sent>[0-9]+)\/'
                                  '(?P<multicast_packets_received>[0-9]+)\/'
                                  '(?P<multicast_packets_forwarded>[0-9]+)\/'
                                  '(?P<multicast_packets_originated>[0-9]+)\/'
                                  '(?P<multicast_packets_consumed>[0-9]+)$')
                m = p22.match(line)
                if m:
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters']\
                    ['multicast_packets_sent']= int(m.groupdict()['multicast_packets_sent'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters']\
                    ['multicast_packets_received']= int(m.groupdict()['multicast_packets_received'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters']\
                    ['multicast_packets_forwarded']= int(m.groupdict()['multicast_packets_forwarded'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters']\
                    ['multicast_packets_originated']= int(m.groupdict()['multicast_packets_originated'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters']\
                    ['multicast_packets_consumed']= int(m.groupdict()['multicast_packets_consumed'])
                    continue

                #Multicast bytes    : 0/0/0/0/0
                p23 = re.compile(r'^\s*Multicast *bytes *:'
                                  ' *(?P<multicast_bytes_sent>[0-9]+)\/'
                                  '(?P<multicast_bytes_received>[0-9]+)\/'
                                  '(?P<multicast_bytes_forwarded>[0-9]+)\/'
                                  '(?P<multicast_bytes_originated>[0-9]+)\/'
                                  '(?P<multicast_bytes_consumed>[0-9]+)$')
                m = p23.match(line)
                if m:
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters']\
                    ['multicast_bytes_sent']= int(m.groupdict()['multicast_bytes_sent'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters']\
                    ['multicast_bytes_received']= int(m.groupdict()['multicast_bytes_received'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters']\
                    ['multicast_bytes_forwarded']= int(m.groupdict()['multicast_bytes_forwarded'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters']\
                    ['multicast_bytes_originated']= int(m.groupdict()['multicast_bytes_originated'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters']\
                    ['multicast_bytes_consumed']= int(m.groupdict()['multicast_bytes_consumed'])
                    continue

                #Broadcast packets  : 0/0/0/0/0
                p24 = re.compile(r'^\s*Broadcast *packets *:'
                                  ' *(?P<broadcast_packets_sent>[0-9]+)\/'
                                  '(?P<broadcast_packets_received>[0-9]+)\/'
                                  '(?P<broadcast_packets_forwarded>[0-9]+)\/'
                                  '(?P<broadcast_packets_originated>[0-9]+)\/'
                                  '(?P<broadcast_packets_consumed>[0-9]+)$')
                m = p24.match(line)
                if m:
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters']\
                    ['broadcast_packets_sent']= int(m.groupdict()['broadcast_packets_sent'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters']\
                    ['broadcast_packets_received']= int(m.groupdict()['broadcast_packets_received'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters']\
                    ['broadcast_packets_forwarded']= int(m.groupdict()['broadcast_packets_forwarded'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters']\
                    ['broadcast_packets_originated']= int(m.groupdict()['broadcast_packets_originated'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters']\
                    ['broadcast_packets_consumed']= int(m.groupdict()['broadcast_packets_consumed'])
                    continue

                #Broadcast bytes    : 0/0/0/0/0
                p25 = re.compile(r'^\s*Broadcast *bytes *:'
                                  ' *(?P<broadcast_bytes_sent>[0-9]+)\/'
                                  '(?P<broadcast_bytes_received>[0-9]+)\/'
                                  '(?P<broadcast_bytes_forwarded>[0-9]+)\/'
                                  '(?P<broadcast_bytes_originated>[0-9]+)\/'
                                  '(?P<broadcast_bytes_consumed>[0-9]+)$')
                m = p25.match(line)
                if m:
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters']\
                    ['broadcast_bytes_sent']= int(m.groupdict()['broadcast_bytes_sent'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters']\
                    ['broadcast_bytes_received']= int(m.groupdict()['broadcast_bytes_received'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters']\
                    ['broadcast_bytes_forwarded']= int(m.groupdict()['broadcast_bytes_forwarded'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters']\
                    ['broadcast_bytes_originated']= int(m.groupdict()['broadcast_bytes_originated'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters']\
                    ['broadcast_bytes_consumed']= int(m.groupdict()['broadcast_bytes_consumed'])
                    continue

                #Labeled packets    : 0/0/0/0/0
                p26 = re.compile(r'^\s*Labeled *packets *:'
                                  ' *(?P<labeled_packets_sent>[0-9]+)\/'
                                  '(?P<labeled_packets_received>[0-9]+)\/'
                                  '(?P<labeled_packets_forwarded>[0-9]+)\/'
                                  '(?P<labeled_packets_originated>[0-9]+)\/'
                                  '(?P<labeled_packets_consumed>[0-9]+)$')
                m = p26.match(line)
                if m:
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters']\
                    ['labeled_packets_sent']= int(m.groupdict()['labeled_packets_sent'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters']\
                    ['labeled_packets_received']= int(m.groupdict()['labeled_packets_received'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters']\
                    ['labeled_packets_forwarded']= int(m.groupdict()['labeled_packets_forwarded'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters']\
                    ['labeled_packets_originated']= int(m.groupdict()['labeled_packets_originated'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters']\
                    ['labeled_packets_consumed']= int(m.groupdict()['labeled_packets_consumed'])
                    continue

                #Labeled bytes      : 0/0/0/0/0
                p27 = re.compile(r'^\s*Labeled *bytes *:'
                                  ' *(?P<labeled_bytes_sent>[0-9]+)\/'
                                  '(?P<labeled_bytes_received>[0-9]+)\/'
                                  '(?P<labeled_bytes_forwarded>[0-9]+)\/'
                                  '(?P<labeled_bytes_originated>[0-9]+)\/'
                                  '(?P<labeled_bytes_consumed>[0-9]+)$')
                m = p27.match(line)
                if m:
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters']\
                    ['labeled_bytes_sent']= int(m.groupdict()['labeled_bytes_sent'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters']\
                    ['labeled_bytes_received']= int(m.groupdict()['labeled_bytes_received'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters']\
                    ['labeled_bytes_forwarded']= int(m.groupdict()['labeled_bytes_forwarded'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters']\
                    ['labeled_bytes_originated']= int(m.groupdict()['labeled_bytes_originated'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters']\
                    ['labeled_bytes_consumed']= int(m.groupdict()['labeled_bytes_consumed'])
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

            # IP unnumbered interface (loopback0)
            p31 = re.compile(r'^\s*IP +unnumbered +interface +\((?P<unnum_intf>[\w\/\.]+)\)$')
            m = p31.match(line)
            if m:
                unnum_intf = m.groupdict()['unnum_intf']
                if 'ipv4' in ip_interface_vrf_all_dict[interface]:
                    ip_interface_vrf_all_dict[interface]['ipv4']['unnumbered'] = {}
                    ip_interface_vrf_all_dict[interface]['ipv4']['unnumbered']['interface_ref']\
                         = unnum_intf
                continue

        return ip_interface_vrf_all_dict


# ===================================
# Schema for 'show vrf all interface'
# ===================================
class ShowVrfAllInterfaceSchema(MetaParser):
    """Schema for show vrf all interface"""
    schema = { 
                Any():
                    {'vrf': str,
                     'vrf_id': int,
                     'site_of_origin': str
                    },
                }

# ===================================
# Parser for 'show vrf all interface'
# ===================================
class ShowVrfAllInterface(ShowVrfAllInterfaceSchema):
    """Parser for show vrf all interface"""

    def cli(self):
        out = self.device.execute('show vrf all interface')

        vrf_all_interface_dict = {}

        for line in out.splitlines():
            line = line.rstrip()

            # Interface                 VRF-Name                        VRF-ID  Site-of-Origin
            # Ethernet2/1               VRF1                                 3  --
            # Null0                     default                              1  --
            # Ethernet2/1.10            default                              1  --
            # Ethernet2/1.20            default                              1  --
            # Ethernet2/4               default                              1  --
            # Ethernet2/5               default                              1  --
            # Ethernet2/6               default                              1  --
            
            p1 = re.compile(r'^\s*(?P<interface>[a-zA-Z0-9\.\/]+)'
                             ' *(?P<vrf>[a-zA-Z0-9]+)'
                             ' *(?P<vrf_id>[0-9]+)'
                             ' *(?P<site_of_origin>[a-zA-Z\-]+)$')

            m = p1.match(line)
            if m:

                interface = m.groupdict()['interface']
                vrf = m.groupdict()['vrf']
                vrf_id = int(m.groupdict()['vrf_id'])
                site_of_origin = m.groupdict()['site_of_origin']

                if interface not in vrf_all_interface_dict:
                    vrf_all_interface_dict[interface] = {}
                vrf_all_interface_dict[interface]['vrf'] = vrf
                vrf_all_interface_dict[interface]['vrf_id'] = vrf_id
                vrf_all_interface_dict[interface]\
                ['site_of_origin'] = site_of_origin

        return vrf_all_interface_dict


# ======================================
# Schema for 'show interface switchport'
# ======================================
class ShowInterfaceSwitchportSchema(MetaParser):
    """Schema for show interface switchport"""

    schema = {
        Any():
            {'switchport_status': str,
             'switchport_monitor': str,
             'switchport_mode': str,
             'access_vlan': int,
             'switchport_enable': bool,
             Optional('access_vlan_mode'): str,
             'native_vlan': int,
             Optional('native_vlan_mode'): str,
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
                    
# ======================================
# Parser for 'show interface switchport'
# ======================================
class ShowInterfaceSwitchport(ShowInterfaceSwitchportSchema):
    """Parser for show interface switchport"""

    def cli(self):
        out = self.device.execute('show interface switchport')

        interface_switchport_dict = {}

        for line in out.splitlines():
            line = line.rstrip()

            #Name: Ethernet2/2
            p1 = re.compile(r'^\s*Name: *(?P<interface>[a-zA-Z0-9\/\-\.]+)$')
            m = p1.match(line)
            if m:
                interface = m.groupdict()['interface']

                if interface not in interface_switchport_dict:
                    interface_switchport_dict[interface] = {}
                    continue

            #Switchport: Enabled
            p2 = re.compile(r'^\s*Switchport: *(?P<switchport_status>[a-zA-Z\s]+)$')
            m = p2.match(line)
            if m:    
                switchport_status = m.groupdict()['switchport_status'].lower()
                interface_switchport_dict[interface]['switchport_status'] = switchport_status

                interface_switchport_dict[interface]['switchport_enable'] = True \
                    if 'enable' in switchport_status else False

                continue

            #Switchport Monitor: Not enabled
            p3 = re.compile(r'^\s*Switchport *Monitor: *(?P<switchport_monitor>[a-zA-Z\s]+)$')
            m = p3.match(line)
            if m:
                switchport_monitor = m.groupdict()['switchport_monitor']

                interface_switchport_dict[interface]['switchport_monitor'] = switchport_monitor
                continue

            # Operational Mode: trunk
            p4 = re.compile(r'^\s*Operational *Mode: *(?P<switchport_mode>\S+)$')
            m = p4.match(line)
            if m:
                interface_switchport_dict[interface]['switchport_mode'] = m.groupdict()['switchport_mode'] 
                continue

            # Access Mode VLAN: 1 (default)
            # Access Mode VLAN: 7 (server-vlan7)
            p5 = re.compile(r'^\s*Access *Mode *VLAN: *(?P<access_vlan>[0-9]+)'
                             '(?: *\((?P<access_vlan_mode>[\w\-\s]+)\))?$')
            m = p5.match(line)
            if m:
                access_vlan = int(m.groupdict()['access_vlan'])
                access_vlan_mode = m.groupdict()['access_vlan_mode']

                interface_switchport_dict[interface]\
                ['access_vlan'] = access_vlan
                interface_switchport_dict[interface]\
                ['access_vlan_mode'] = access_vlan_mode
                continue

            #Trunking Native Mode VLAN: 1 (default)
            # Trunking Native Mode VLAN: 200 (VLAN0200)
            p6 = re.compile(r'^\s*Trunking *Native *Mode *VLAN:'
                             ' *(?P<native_vlan>[0-9]+)'
                             ' *\((?P<native_vlan_mode>[a-zA-Z0-9\-\_]+)\)$')
            m = p6.match(line)
            if m:
                native_vlan = int(m.groupdict()['native_vlan'])
                native_vlan_mode = m.groupdict()['native_vlan_mode']

                interface_switchport_dict[interface]\
                ['native_vlan'] = native_vlan
                interface_switchport_dict[interface]\
                ['native_vlan_mode'] = native_vlan_mode
                continue

            #Trunking VLANs Allowed: 100,300
            p7 = re.compile(r'^\s*Trunking *VLANs *Allowed: *(?P<trunk_vlans>[0-9\,\-]+)$')
            m = p7.match(line)
            if m:
                trunk_vlans = m.groupdict()['trunk_vlans']

                interface_switchport_dict[interface]['trunk_vlans'] = trunk_vlans
                continue

            #Administrative private-vlan primary host-association: none
            p8 = re.compile(r'^\s*Administrative *private-vlan *primary'
                             ' *host-association:'
                             ' *(?P<admin_priv_vlan_primary_host_assoc>[a-z]+)$')
            m = p8.match(line)
            if m:
                admin_priv_vlan_primary_host_assoc = m.groupdict()['admin_priv_vlan_primary_host_assoc']

                interface_switchport_dict[interface]['admin_priv_vlan_primary_host_assoc'] = admin_priv_vlan_primary_host_assoc
                continue

            #Administrative private-vlan secondary host-association: none
            p9 = re.compile(r'^\s*Administrative *private-vlan *secondary'
                             ' *host-association:'
                             ' *(?P<admin_priv_vlan_secondary_host_assoc>[a-z]+)$')
            m = p9.match(line)
            if m:
                admin_priv_vlan_secondary_host_assoc\
                 = m.groupdict()['admin_priv_vlan_secondary_host_assoc']

                interface_switchport_dict[interface]\
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

                interface_switchport_dict[interface]\
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

                interface_switchport_dict[interface]\
                ['admin_priv_vlan_secondary_mapping'] = admin_priv_vlan_secondary_mapping
                continue

            #Administrative private-vlan trunk native VLAN: none
            p12 = re.compile(r'^\s*Administrative *private-vlan *trunk *native'
                             ' *VLAN:'
                             ' *(?P<admin_priv_vlan_trunk_native_vlan>[a-z]+)$')
            m = p12.match(line)
            if m:
                admin_priv_vlan_trunk_native_vlan = m.groupdict()['admin_priv_vlan_trunk_native_vlan']

                interface_switchport_dict[interface]\
                ['admin_priv_vlan_trunk_native_vlan'] = admin_priv_vlan_trunk_native_vlan
                continue

            #Administrative private-vlan trunk encapsulation: dot1q
            p13 = re.compile(r'^\s*Administrative *private-vlan *trunk'
                             ' *encapsulation:'
                             ' *(?P<admin_priv_vlan_trunk_encapsulation>[a-z0-9]+)$')
            m = p13.match(line)
            if m:
                admin_priv_vlan_trunk_encapsulation = m.groupdict()['admin_priv_vlan_trunk_encapsulation']

                interface_switchport_dict[interface]\
                ['admin_priv_vlan_trunk_encapsulation'] = admin_priv_vlan_trunk_encapsulation
                continue

            #Administrative private-vlan trunk normal VLANs: none
            p14 = re.compile(r'^\s*Administrative *private-vlan *trunk'
                             ' *normal VLANs:'
                             ' *(?P<admin_priv_vlan_trunk_normal_vlans>[a-z]+)$')
            m = p14.match(line)
            if m:
                admin_priv_vlan_trunk_normal_vlans = m.groupdict()['admin_priv_vlan_trunk_normal_vlans']

                interface_switchport_dict[interface]\
                ['admin_priv_vlan_trunk_normal_vlans'] = admin_priv_vlan_trunk_normal_vlans
                continue

            # Administrative private-vlan trunk private VLANs: none
            # Administrative private-vlan trunk private VLANs: none(0 none)
            p15 = re.compile(r'^\s*Administrative *private-vlan *trunk'
                             ' *private VLANs:'
                             ' *(?P<admin_priv_vlan_trunk_private_vlans>[a-z]+)(?P<dummy>.*)?$')
            m = p15.match(line)
            if m:
                admin_priv_vlan_trunk_private_vlans = m.groupdict()['admin_priv_vlan_trunk_private_vlans']

                interface_switchport_dict[interface]\
                ['admin_priv_vlan_trunk_private_vlans'] = admin_priv_vlan_trunk_private_vlans
                continue

            #Operational private-vlan: none
            p16 = re.compile(r'^\s*Operational *private-vlan:'
                             ' *(?P<operational_private_vlan>[a-z]+)$')
            m = p16.match(line)
            if m:
                operational_private_vlan = m.groupdict()['operational_private_vlan']

                interface_switchport_dict[interface]\
                ['operational_private_vlan'] = operational_private_vlan
                continue

        return interface_switchport_dict


# ========================================
# Schema for 'show ipv6 interface vrf all'
# ========================================
class ShowIpv6InterfaceVrfAllSchema(MetaParser):
    """Schema for show ipv6 interface vrf all"""

    schema = {
        Any():
            {'vrf': str,
             'interface_status': str,
             'iod': int,
             'enabled': bool,
             Optional('ipv6'):
                {Any():
                    {Optional('ip'): str,
                     Optional('prefix_length'): str,
                     Optional('anycast'): bool,
                     Optional('status'): str,
                     },                
                'counters':
                    {'unicast_packets_forwarded': int,
                     'unicast_packets_originated': int,
                     'unicast_packets_consumed': int,
                     'unicast_bytes_forwarded': int,
                     'unicast_bytes_originated': int,
                     'unicast_bytes_consumed': int,
                     'multicast_packets_forwarded': int,
                     'multicast_packets_originated': int,
                     'multicast_packets_consumed': int,
                     'multicast_bytes_forwarded': int,
                     'multicast_bytes_originated': int,
                     'multicast_bytes_consumed': int,
                    },
                Optional('ipv6_subnet'): str,
                'ipv6_link_local': str,
                'ipv6_link_local_state': str,
                'ipv6_ll_state': str,
                Optional('ipv6_virtual_add'): str,
                Optional('ipv6_virtual_groups'): list,
                Optional('virtual_add'): bool,
                Optional('multicast_groups'): bool,
                'ipv6_multicast_routing': str,
                'ipv6_report_link_local': str,
                'ipv6_forwarding_feature': str,
                Optional('ipv6_multicast_groups'): list,
                Optional('ipv6_multicast_entries'): str,
                'ipv6_mtu': int,
                'ipv6_unicast_rev_path_forwarding': str,
                'ipv6_load_sharing': str,
                'ipv6_last_reset': str
                },
            },
        }

# ========================================
# Parser for 'show ipv6 interface vrf all'
# ========================================
class ShowIpv6InterfaceVrfAll(ShowIpv6InterfaceVrfAllSchema):
    """Parser for ipv6 interface vrf all"""

    def cli(self):
        out = self.device.execute('show ipv6 interface vrf all')

        # Init variables
        ipv6_interface_dict = {}
        ipv6_addresses = None
        anycast_addresses = None
        virtual_add = False
        multicast_groups = False

        for line in out.splitlines():
            line = line.rstrip()

            #IPv6 Interface Status for VRF "VRF1"
            p1 = re.compile(r'^\s*IPv6 *Interface *Status *for *VRF'
                             ' *(?P<vrf>\S+)$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                vrf = vrf.replace('"',"")
                continue

            #Ethernet2/1, Interface status: protocol-up/link-up/admin-up, iod: 36
            #port-channel2.101, Interface status: protocol-down/link-down/admin-up, iod: 71
            p2 = re.compile(r'^\s*(?:(?P<interface>[a-zA-Z0-9\/\-\.]+)), Interface'
                             ' *status: *(?P<interface_status>[a-z\-\/]+),'
                             ' *iod: *(?P<iod>[0-9]+)$')
            m = p2.match(line)
            if m:

                interface = str(m.groupdict()['interface'])
                interface_status = m.groupdict()['interface_status']
                iod = int(m.groupdict()['iod'])

                if interface not in ipv6_interface_dict:
                    ipv6_interface_dict[interface] = {}
                ipv6_interface_dict[interface]['iod'] = iod
                ipv6_interface_dict[interface]['interface_status'] = interface_status  
                ipv6_interface_dict[interface]['vrf'] = vrf
                ipv6_interface_dict[interface]['enabled'] = True

                # init multicast groups list to empty for this interface
                ipv6_multicast_groups = []
                ipv6_virtual_groups = []
                ipv6_multicast_entries = multicast_groups = False
                continue

            # IPv6 address:
            p3_1 = re.compile(r'^\s*IPv6 address:$')
            m = p3_1.match(line)
            if m:
                ipv6_addresses = True
                anycast_addresses = False
                continue

            # Anycast configured addresses:
            p3_2 = re.compile(r'^\s*Anycast configured addresses:$')
            m = p3_2.match(line)
            if m:
                anycast_addresses = True
                ipv6_addresses = False
                continue

            # 2001:db8:1:1::1/64 [VALID]
            p3_3 = re.compile(r'^\s*(?P<ip>[a-z0-9\:]+)'
                             '\/(?P<prefix_length>[0-9]+)'
                             ' *\[(?P<status>[a-zA-Z]+)\]$')
            m = p3_3.match(line)
            if m:
                ip  = m.groupdict()['ip']
                prefix_length = m.groupdict()['prefix_length']
                status = m.groupdict()['status'].lower()

                address = ip + '/' + prefix_length

                if 'ipv6' not in ipv6_interface_dict[interface]:
                    ipv6_interface_dict[interface]['ipv6'] = {}
                if address not in ipv6_interface_dict[interface]['ipv6']:
                    ipv6_interface_dict[interface]['ipv6'][address] = {}
                
                ipv6_interface_dict[interface]['ipv6'][address]\
                    ['ip'] = ip
                ipv6_interface_dict[interface]['ipv6'][address]\
                    ['prefix_length'] = prefix_length

                if ipv6_addresses:
                    ipv6_interface_dict[interface]['ipv6'][address]\
                        ['status'] = status
                elif anycast_addresses:
                    ipv6_interface_dict[interface]['ipv6'][address]\
                        ['anycast'] = True
                continue

            #IPv6 subnet:  2001:db8:1:1::/64
            p4 = re.compile(r'^\s*IPv6 *subnet:'
                             ' *(?P<ipv6_subnet>[a-z0-9\:\/]+)$')
            m = p4.match(line)
            if m:
                ipv6_subnet = m.groupdict()['ipv6_subnet']

                ipv6_interface_dict[interface]['ipv6']['ipv6_subnet'] = ipv6_subnet
                continue

            #IPv6 link-local address: fe80::a8aa:bbff:febb:cccc (default) [VALID]
            p5 = re.compile(r'^\s*IPv6 *link-local *address:'
                             ' *(?P<ipv6_link_local>[a-z0-9\:\s]+)'
                             ' *\((?P<ipv6_link_local_state>[a-z]+)\)'
                             ' *\[(?P<ipv6_ll_state>[A-Z]+)\]$')
            m = p5.match(line)
            if m:
                ipv6_link_local = m.groupdict()['ipv6_link_local']
                ipv6_link_local_state = m.groupdict()['ipv6_link_local_state']
                ipv6_ll_state = m.groupdict()['ipv6_ll_state'].lower()

                if 'ipv6' not in ipv6_interface_dict[interface]:
                    ipv6_interface_dict[interface]['ipv6'] = {}

                ipv6_interface_dict[interface]['ipv6']['ipv6_link_local'] = ipv6_link_local
                ipv6_interface_dict[interface]['ipv6']['ipv6_link_local_state'] = ipv6_link_local_state
                ipv6_interface_dict[interface]['ipv6']['ipv6_ll_state'] = ipv6_ll_state
                continue

            #IPv6 virtual addresses configured: none
            p6 = re.compile(r'^\s*IPv6 *virtual *addresses *configured:'
                             ' *(?P<ipv6_virtual_add>[a-z]+)$')
            m = p6.match(line)
            if m:
                ipv6_virtual_add = m.groupdict()['ipv6_virtual_add']

                ipv6_interface_dict[interface]['ipv6']['ipv6_virtual_add'] = ipv6_virtual_add
                continue

            #IPv6 virtual addresses configured:
            #        fe80::5:73ff:fea0:2  192:168::1
            p6_1 = re.compile(r'^\s*(IPv6 virtual *(?P<virtual_add>(addresses|address) configured:))$')
            m = p6_1.match(line)
            if m:
                virtual_add = m.groupdict()['virtual_add']

                ipv6_interface_dict[interface]['ipv6']['virtual_add'] = True
                continue

            if virtual_add:
                p6_2 = re.compile(r'^\s*(?P<ipv6_virtual_addresses>[a-z0-9\:\s]+)$')
                m = p6_2.match(line)
                if m:
                    ipv6_virtual_addresses = str(m.groupdict()['ipv6_virtual_addresses'])

                    #split string of addresses to list
                    ipv6_virtual_addresses = [str(j) for j in ipv6_virtual_addresses.split()]

                    #Add to previous created list
                    for add in ipv6_virtual_addresses:
                        ipv6_virtual_groups.append(add)

                    ipv6_interface_dict[interface]['ipv6']['ipv6_virtual_groups']\
                    = sorted(ipv6_virtual_groups)
                    continue

            #IPv6 multicast routing: disabled
            p7 = re.compile(r'^\s*IPv6 *multicast *routing:'
                             ' *(?P<ipv6_multicast_routing>[a-z]+)$')
            m = p7.match(line)
            if m:
                ipv6_multicast_routing = m.groupdict()['ipv6_multicast_routing']

                ipv6_interface_dict[interface]['ipv6']['ipv6_multicast_routing'] = ipv6_multicast_routing
                continue

            #IPv6 report link local: disabled
            p8 = re.compile(r'^\s*IPv6 *report *link *local:'
                              ' *(?P<ipv6_report_link_local>[a-z]+)$')
            m = p8.match(line)
            if m:
                ipv6_report_link_local = m.groupdict()['ipv6_report_link_local']

                ipv6_interface_dict[interface]['ipv6']['ipv6_report_link_local']\
                 = ipv6_report_link_local
                continue

            #IPv6 Forwarding feature: disabled
            p9 = re.compile(r'^\s*IPv6 *Forwarding *feature:'
                              ' *(?P<ipv6_forwarding_feature>[a-z]+)$')
            m = p9.match(line)
            if m:
                ipv6_forwarding_feature = m.groupdict()['ipv6_forwarding_feature']

                ipv6_interface_dict[interface]['ipv6']['ipv6_forwarding_feature']\
                 = ipv6_forwarding_feature
                continue

            #IPv6 multicast groups locally joined:
            p10 = re.compile(r'^\s*(?P<multicast_groups>(IPv6 *multicast *(groups|group) *locally *joined:))$')
            m = p10.match(line)
            if m:
                virtual_add = False
                multicast_groups = m.groupdict()['multicast_groups']
                ipv6_interface_dict[interface]['ipv6']['multicast_groups'] = True
                continue

            if multicast_groups:
                # ff02::1:ffbb:cccc  ff02::1:ff00:3  ff02::1:ff00:2  ff02::2   
                # ff02::1  ff02::1:ff00:1  ff02::1:ffbb:cccc  ff02::1:ff00:0
                # ff02::1:ffad:beef  ff02::1:ff00:1(2)  ff02::2(2)  ff02::1(2)
                p11 = re.compile(r'^\s*(?P<ipv6_multicast_group_addresses>[a-z0-9\(\)\:\s]+)$')
                m = p11.match(line)
                if m:
                    ipv6_multicast_group_addresses = str(m.groupdict()['ipv6_multicast_group_addresses'])

                    # Split string of addressed into a list
                    ipv6_multicast_group_addresses = [str(i) for i in ipv6_multicast_group_addresses.split()]
                    
                    # Add to previous created list
                    for address in ipv6_multicast_group_addresses:
                        ipv6_multicast_groups.append(address)

                    ipv6_interface_dict[interface]['ipv6']['ipv6_multicast_groups']\
                     = sorted(ipv6_multicast_groups)
                    continue

            # IPv6 multicast (S,G) entries joined: none
            # IPv6 multicast (S,G) entries joined: 
            #  (2001:20:1:1::254, ff38::1)
            p12 = re.compile(r'^\s*IPv6 *multicast *\(S\,G\) *entries *joined:$')
            m = p12.match(line)
            if m:
                ipv6_multicast_entries = True
                continue

            #  (2001:20:1:1::254, ff38::1)
            p12_1 = re.compile(r'^\s*\((?P<ip_list>.*)\)')
            m = p12_1.match(line)
            if m and ipv6_multicast_entries:
                ipv6_multicast_entries = m.groupdict()['ip_list']
                ipv6_interface_dict[interface]['ipv6']['ipv6_multicast_entries']\
                 = ipv6_multicast_entries
                continue

            #IPv6 MTU: 1600 (using link MTU)
            p13 = re.compile(r'^\s*IPv6 *MTU: *(?P<ipv6_mtu>[0-9]+)'
                              ' *\(using *link *MTU\)$')
            m = p13.match(line)
            if m:
                ipv6_mtu = int(m.groupdict()['ipv6_mtu'])

                ipv6_interface_dict[interface]['ipv6']['ipv6_mtu'] = ipv6_mtu
                continue

            #IPv6 unicast reverse path forwarding: none
            p14 = re.compile(r'^\s*IPv6 *unicast *reverse *path *forwarding:'
                              ' *(?P<ipv6_unicast_rev_path_forwarding>[a-z]+)$')
            m = p14.match(line)
            if m:
                ipv6_unicast_rev_path_forwarding = m.groupdict()\
                ['ipv6_unicast_rev_path_forwarding']

                ipv6_interface_dict[interface]['ipv6']\
                ['ipv6_unicast_rev_path_forwarding']\
                 = ipv6_unicast_rev_path_forwarding
                continue

            #IPv6 load sharing: none
            p15 = re.compile(r'^\s*IPv6 *load *sharing:'
                             ' *(?P<ipv6_load_sharing>[a-z]+)$')
            m = p15.match(line)
            if m:
                ipv6_load_sharing = m.groupdict()['ipv6_load_sharing']

                ipv6_interface_dict[interface]['ipv6']['ipv6_load_sharing']\
                 = ipv6_load_sharing
                continue

            #IPv6 interface statistics last reset: never
            p16 = re.compile(r'^\s*IPv6 *interface *statistics *last *reset:'
                              ' *(?P<ipv6_last_reset>[a-z]+)$')
            m = p16.match(line)
            if m:
                ipv6_last_reset = m.groupdict()['ipv6_last_reset']

                ipv6_interface_dict[interface]['ipv6']['ipv6_last_reset']\
                 = ipv6_last_reset
                continue

            #Unicast packets:      0/0/0
            p18 = re.compile(r'^\s*Unicast *packets:'
                             ' *(?P<unicast_packets_forwarded>[0-9]+)\/'
                             '(?P<unicast_packets_originated>[0-9]+)\/'
                             '(?P<unicast_packets_consumed>[0-9]+)$')
            m = p18.match(line)
            if m:
                if 'counters' not in ipv6_interface_dict[interface]['ipv6']:
                    ipv6_interface_dict[interface]['ipv6']['counters'] = {}


                ipv6_interface_dict[interface]['ipv6']['counters']\
                ['unicast_packets_forwarded'] = int(m.groupdict()['unicast_packets_forwarded'])
                ipv6_interface_dict[interface]['ipv6']['counters']\
                ['unicast_packets_originated'] = int(m.groupdict()['unicast_packets_originated'])
                ipv6_interface_dict[interface]['ipv6']['counters']\
                ['unicast_packets_consumed'] = int(m.groupdict()['unicast_packets_consumed'])
                continue

            #Unicast bytes:        0/0/0
            p19 = re.compile(r'^\s*Unicast *bytes: *(?P<unicast_bytes_forwarded>[0-9]+)'
                              '\/(?P<unicast_bytes_originated>[0-9]+)\/'
                              '(?P<unicast_bytes_consumed>[0-9]+)$')
            m = p19.match(line)
            if m:
                ipv6_interface_dict[interface]['ipv6']['counters']\
                ['unicast_bytes_forwarded'] = int(m.groupdict()['unicast_bytes_forwarded'])
                ipv6_interface_dict[interface]['ipv6']['counters']\
                ['unicast_bytes_originated'] = int(m.groupdict()['unicast_bytes_originated'])
                ipv6_interface_dict[interface]['ipv6']['counters']\
                ['unicast_bytes_consumed'] = int(m.groupdict()['unicast_bytes_consumed'])
                continue

            #Multicast packets:    0/12/9
            p20 = re.compile(r'^\s*Multicast *packets: *(?P<multicast_packets_forwarded>[0-9]+)'
                              '\/(?P<multicast_packets_originated>[0-9]+)\/'
                              '(?P<multicast_packets_consumed>[0-9]+)$')
            m = p20.match(line)
            if m:
                ipv6_interface_dict[interface]['ipv6']['counters']\
                ['multicast_packets_forwarded'] = int(m.groupdict()['multicast_packets_forwarded'])
                ipv6_interface_dict[interface]['ipv6']['counters']\
                ['multicast_packets_originated'] = int(m.groupdict()['multicast_packets_originated'])
                ipv6_interface_dict[interface]['ipv6']['counters']\
                ['multicast_packets_consumed'] = int(m.groupdict()['multicast_packets_consumed'])
                continue

            #Multicast bytes:      0/1144/640
            p21 = re.compile(r'^\s*Multicast *bytes: *(?P<multicast_bytes_forwarded>[0-9]+)\/'
                              '(?P<multicast_bytes_originated>[0-9]+)\/'
                              '(?P<multicast_bytes_consumed>[0-9]+)$')
            m = p21.match(line)
            if m:
                ipv6_interface_dict[interface]['ipv6']['counters']\
                ['multicast_bytes_forwarded'] = int(m.groupdict()['multicast_bytes_forwarded'])
                ipv6_interface_dict[interface]['ipv6']['counters']\
                ['multicast_bytes_originated'] = int(m.groupdict()['multicast_bytes_originated'])
                ipv6_interface_dict[interface]['ipv6']['counters']\
                ['multicast_bytes_consumed'] = int(m.groupdict()['multicast_bytes_consumed'])
                continue

        return ipv6_interface_dict


# ====================================
# Schema for 'show ip interface brief'
# ====================================
class ShowIpInterfaceBriefSchema(MetaParser):
    """Schema for show ip interface brief"""
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

# ====================================
# Parser for 'show ip interface brief'
# ====================================
class ShowIpInterfaceBrief(ShowIpInterfaceBriefSchema):
    """Parser for show ip interface brief"""

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

# ===========================================
# Parser for 'show ip interface brief | vlan'
# ===========================================
class ShowIpInterfaceBriefPipeVlan(ShowIpInterfaceBrief):
    """Parser for show ip interface brief | include Vlan"""

    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cmd = 'show ip interface brief | include Vlan'.format()


# =================================
# Schema for 'show interface brief'
# =================================
class ShowInterfaceBriefSchema(MetaParser):
    """Schema for show interface brief"""

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

# =================================
# Parser for 'show interface brief'
# =================================
class ShowInterfaceBrief(ShowInterfaceBriefSchema):
    """Parser for show interface brief"""
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
                    m.groupdict()['reason'].strip()
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
                    m.groupdict()['reason'].strip()
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

# =================================================
# Schema for 'show running-config interface <WORD>'
# =================================================
class ShowRunningConfigInterfaceSchema(MetaParser):
    """Schema for show running-config interface <WORD>"""

    schema = {'interface':
                {Any():
                    {Optional('shutdown'): bool,
                     Optional('host_reachability_protocol'): str,
                     Optional('source_interface'): str,
                     Optional('member_vni'):
                        {Any():
                            {Optional('associate_vrf'): bool,
                             Optional('mcast_group'): str,
                             Optional('suppress_arp'): bool,
                            }
                        },
                    }
                },
            }

# =================================================
# Parser for 'show running-config interface <WORD>'
# =================================================
class ShowRunningConfigInterface(ShowRunningConfigInterfaceSchema):
    """Parser for show running-config interface <WORD>"""

    def cli(self, intf):
        cmd = 'show running-config interface {}'.format(intf)
        out = self.device.execute(cmd)

        # Init vars
        interface_dict = {}

        for line in out.splitlines():
            line = line.rstrip()

            # interface nve1
            p1 = re.compile(r'^\s*interface +(?P<intf_name>[a-zA-Z0-9\-]+)$')
            m = p1.match(line)
            if m:

                interface = str(m.groupdict()['intf_name'])

                if 'interface' not in interface_dict:
                    interface_dict['interface'] = {}

                interface_dict['interface'][interface] = {}

                continue

            # no shutdown
            p2 = re.compile(r'^\s*no shutdown$')
            m = p2.match(line)
            if m:

                interface_dict['interface'][interface]['shutdown'] = False

                continue

            # host-reachability protocol bgp
            p3 = re.compile(r'^\s*host-reachability protocol +(?P<protocol>[a-zA-Z]+)$')
            m = p3.match(line)
            if m:

                interface_dict['interface'][interface]['host_reachability_protocol'] = \
                    str(m.groupdict()['protocol'])

                continue

            # source-interface loopback1
            p4 = re.compile(r'^\s*source-interface +(?P<src_intf>[a-zA-Z0-9\-]+)$')
            m = p4.match(line)
            if m:

                interface_dict['interface'][interface]['source_interface'] = \
                    str(m.groupdict()['src_intf'])

                continue

            # member vni 8100
            # member vni 9100 associate-vrf
            # member vni 2001201-2001300
            p5 = re.compile(r'^\s*member vni +(?P<vni>[0-9\-]+)( +(?P<associate_vrf>[a-zA-Z\-]+))?$')
            m = p5.match(line)
            if m:

                if 'member_vni' not in interface_dict['interface'][interface]:
                    interface_dict['interface'][interface]['member_vni'] = {}

                vni = str(m.groupdict()['vni'])

                if '-' in vni:
                    vni_range = re.findall(r'(?P<first_vni>[0-9]+)\-(?P<last_vni>[0-9]+)?$', vni)
                    members = range(int(vni_range[0][0]), int(vni_range[0][1])+1)
                else:
                    members = [vni]

                for memb in members:
                    interface_dict['interface'][interface]['member_vni'][str(memb)] = {}

                    if m.groupdict()['associate_vrf']:
                        interface_dict['interface'][interface]['member_vni'][str(memb)]['associate_vrf'] = \
                            True

                continue

            # mcast-group 225.0.1.25
            p6 = re.compile(r'^\s*mcast-group +(?P<ip>[0-9\.]+)$')
            m = p6.match(line)
            if m:

                for memb in members:
                    interface_dict['interface'][interface]['member_vni'][str(memb)]['mcast_group'] = \
                        str(m.groupdict()['ip'])

                continue

            # suppress-arp
            p7 = re.compile(r'^\s*suppress-arp$')
            m = p7.match(line)
            if m:

                for memb in members:
                    interface_dict['interface'][interface]['member_vni'][str(memb)]['suppress_arp'] = \
                        True

                continue

        return interface_dict

# ===============================
# Schema for 'show nve interface'
# ===============================
class ShowNveInterfaceSchema(MetaParser):
    """Schema for show nve interface"""

    schema = {'interface':
                {Any():
                    {'state': str,
                    Optional('encapsulation'): str,
                    Optional('source_interface'):
                        {Any():
                            {Optional('primary'): str,
                             Optional('secondary'): str,
                            }
                        },
                    Optional('vpc_capability'):
                        {Any():
                            {Optional('notified'): bool,
                            }
                        },
                    }
                },
            }

# ===============================
# Parser for 'show nve interface'
# ===============================
class ShowNveInterface(ShowNveInterfaceSchema):
    """Parser for show nve interface"""

    def cli(self, intf):
        cmd = 'sh nve interface {} detail'.format(intf)
        out = self.device.execute(cmd)

        # Init vars
        interface_dict = {}

        # Interface: nve1, State: Up, encapsulation: VXLAN
        p1 = re.compile(r'^\s*Interface: +(?P<intf>[\w]+)\,'
            ' +State: +(?P<state>[\w]+)\, +encapsulation:'
            ' +(?P<encapsulation>[\w]+)$')

        # Source-Interface: loopback0 (primary: 2.0.0.1, secondary: 0.0.0.0)
        p2 = re.compile(r'^\s*Source-Interface: +(?P<src_intf>[a-zA-Z0-9\-]+)'
            ' +\(primary: +(?P<primary>[a-zA-Z0-9\.]+)\, +secondary:'
            ' +(?P<secondary>[a-zA-Z0-9\.]+)\)$')

        # VPC Capability: VPC-VIP-Only [not-notified]
        p3 = re.compile(r'^\s*VPC Capability: +(?P<vpc>[a-zA-Z0-9\-]+)'
            ' +\[(?P<notified>[a-zA-Z\-]+)\]$')

        for line in out.splitlines():
            line = line.rstrip()

            m = p1.match(line)
            if m:

                intf = str(m.groupdict()['intf'])

                if 'interface' not in interface_dict:
                    interface_dict['interface'] = {}
                if intf not in interface_dict['interface']:
                    interface_dict['interface'][intf] = {}

                interface_dict['interface'][intf]['state'] = \
                    str(m.groupdict()['state'])
                interface_dict['interface'][intf]['encapsulation'] = \
                    str(m.groupdict()['encapsulation'])

                continue

            m = p2.match(line)
            if m:

                src_intf = str(m.groupdict()['src_intf'])

                if 'source_interface' not in interface_dict['interface'][intf]:
                    interface_dict['interface'][intf]['source_interface'] = {}
                if src_intf not in interface_dict['interface'][intf]['source_interface']:
                    interface_dict['interface'][intf]['source_interface'][src_intf] = {}

                interface_dict['interface'][intf]['source_interface'][src_intf]['primary'] = \
                    str(m.groupdict()['primary'])
                interface_dict['interface'][intf]['source_interface'][src_intf]['secondary'] = \
                    str(m.groupdict()['secondary'])

                continue

            m = p3.match(line)
            if m:

                vpc = str(m.groupdict()['vpc'])
                notified = str(m.groupdict()['notified'])

                if 'vpc_capability' not in interface_dict['interface'][intf]:
                    interface_dict['interface'][intf]['vpc_capability'] = {}
                if vpc not in interface_dict['interface'][intf]['vpc_capability']:
                    interface_dict['interface'][intf]['vpc_capability'][vpc] = {}

                if notified == 'notified':
                    interface_dict['interface'][intf]['vpc_capability'][vpc]['notified'] = \
                        True
                else:
                    interface_dict['interface'][intf]['vpc_capability'][vpc]['notified'] = \
                        False

                continue

        return interface_dict

# ============================================
# Schema for 'show ip interface brief vrf all'
# ============================================
class ShowIpInterfaceBriefVrfAllSchema(MetaParser):
    """Schema for show ip interface brief vrf all"""
    schema = {'interface':
                {Any():
                    {Optional('ip_address'): str,
                     Optional('interface_status'): str}
                },
            }

# ============================================
# Schema for 'show ip interface brief vrf all'
# ============================================
class ShowIpInterfaceBriefVrfAll(ShowIpInterfaceBriefVrfAllSchema):
    """Parser for show ip interface brief vrf all"""

    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    def cli(self, ip=''):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        '''

        cmd = 'show ip interface brief vrf all' if not ip else \
              'show ip interface brief vrf all | include {}'.format(ip)

        out = self.device.execute(cmd)
        interface_dict = {}

        # mgmt0                10.255.5.169    protocol-up/link-up/admin-up
        p = re.compile(r'^\s*(?P<interface>[a-zA-Z0-9\/\.\-]+) '
            '+(?P<ip_address>[a-z0-9\.]+) +(?P<interface_status>[a-z\-\/]+)$')

        for line in out.splitlines():
            line = line.rstrip()

            m = p.match(line)
            if m:
                interface = m.groupdict()['interface']

                if 'interface' not in interface_dict:
                    interface_dict['interface'] = {}
                if interface not in interface_dict['interface']:
                    interface_dict['interface'][interface] = {}

                interface_dict['interface'][interface]['ip_address'] = \
                    str(m.groupdict()['ip_address'])
                interface_dict['interface'][interface]['interface_status'] = \
                    str(m.groupdict()['interface_status'])

                continue

        return interface_dict