'''show_interface.py

NXOS parsers for the following show commands:
    * show interface
    * show interface {interface}
    * show ip interface {interface} vrf {vrf}
    * show ip interface {interface} vrf all
    * show ip interface vrf {vrf}
    * show ip interface vrf all
    * show vrf {vrf} interface {interface}
    * show vrf all interface {interface}
    * show vrf {vrf} interface
    * show vrf all interface
    * show interface switchport
    * show interface {interface} switchport
    * show ipv6 interface {interface} vrf {vrf}
    * show ipv6 interface {interface} vrf all
    * show ipv6 interface vrf {vrf}
    * show ipv6 interface vrf all
    * show ip interface brief
    * show ip interface brief | include Vlan
    * show interface brief
    * show interface {interface} brief
    * show running-config interface {interface}
    * show running-config | section ^interface
    * show nve interface {interface} detail
    * show ip interface brief vrf all | include {ip}
    * show ip interface brief vrf all
    * show interface description
    * show interface {interface} description
    * show interface status
    * show interface {interface} status
    * show interface capabilities
    * show interface {interface} capabilities
    * show interface transceiver
    * show interface {interface} transceiver
    * show interface transceiver details
    * show interface {interface} transceiver details
    * show interface fec
    * show interface hardware-mappings
'''

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
        Any(): {
            Optional("description"): str,
            Optional("types"): str,
            Optional("parent_interface"): str,
            "oper_status": str,
            Optional("admin_state"): str,
            Optional("dedicated_interface"): bool,
            Optional("line_protocol"): str,
            Optional("autostate"): bool,
            Optional("link_state"): str,
            Optional("phys_address"): str,
            Optional("port_speed"): str,
            Optional("mtu"): int,
            "enabled": bool,
            Optional("mac_address"): str,
            Optional("auto_negotiate"): bool,
            Optional("duplex_mode"): str,
            Optional("port_mode"): str,
            Optional("auto_mdix"): str,
            Optional("switchport_monitor"): str,
            Optional("efficient_ethernet"): str,
            Optional("last_link_flapped"): str,
            Optional("interface_reset"): int,
            Optional("ethertype"): str,
            Optional("beacon"): str,
            Optional("medium"): str,
            Optional("reliability"): str,
            Optional("txload"): str,
            Optional("rxload"): str,
            Optional("delay"): int,
            Optional("media_type"): str,
            Optional("flow_control"): {
                Optional("receive"): bool,
                Optional("send"): bool,
            },
            Optional("port_channel"): {
                Optional("port_channel_member"): bool,
                Optional("port_channel_int"): str,
                Optional("port_channel_member_intfs"): list,
            },
            Optional("bandwidth"): int,
            Optional("counters"): {
                Optional("rate"): {
                    Optional("load_interval"): int,
                    Optional("in_rate"): int,
                    Optional("in_rate_pkts"): int,
                    Optional("out_rate"): int,
                    Optional("out_rate_pkts"): int,
                    Optional("in_rate_bps"): int,
                    Optional("in_rate_pps"): int,
                    Optional("out_rate_bps"): int,
                    Optional("out_rate_pps"): int,
                },
                Optional("in_unicast_pkts"): int,
                Optional("in_multicast_pkts"): int,
                Optional("in_broadcast_pkts"): int,
                Optional("in_discards"): int,
                Optional("in_crc_errors"): int,
                Optional("in_oversize_frames"): int,
                Optional("in_pkts"): int,
                Optional("in_mac_pause_frames"): int,
                Optional("in_jumbo_packets"): int,
                Optional("in_storm_suppression_packets"): int,
                Optional("in_storm_suppression_bytes"): int,
                Optional("in_runts"): int,
                Optional("in_oversize_frame"): int,
                Optional("in_overrun"): int,
                Optional("in_underrun"): int,
                Optional("in_ignored"): int,
                Optional("in_watchdog"): int,
                Optional("in_bad_etype_drop"): int,
                Optional("in_unknown_protos"): int,
                Optional("in_if_down_drop"): int,
                Optional("in_with_dribble"): int,
                Optional("in_discard"): int,
                Optional("in_octets"): int,
                Optional("in_errors"): int,
                Optional("in_short_frame"): int,
                Optional("in_no_buffer"): int,
                Optional("out_pkts"): int,
                Optional("out_unicast_pkts"): int,
                Optional("out_multicast_pkts"): int,
                Optional("out_broadcast_pkts"): int,
                Optional("out_discard"): int,
                Optional("out_octets"): int,
                Optional("out_jumbo_packets"): int,
                Optional("out_errors"): int,
                Optional("out_collision"): int,
                Optional("out_deferred"): int,
                Optional("out_late_collision"): int,
                Optional("out_lost_carrier"): int,
                Optional("out_no_carrier"): int,
                Optional("out_babble"): int,
                Optional("last_clear"): str,
                Optional("tx"): bool,
                Optional("rx"): bool,
                Optional("out_mac_pause_frames"): int,
            },
            Optional("encapsulations"): {
                Optional("encapsulation"): str,
                Optional("first_dot1q"): str,
                Optional("native_vlan"): int,
            },
            Optional("ipv4"): {
                Any(): {
                    Optional("ip"): str,
                    Optional("prefix_length"): str,
                    Optional("secondary"): bool,
                    Optional("route_tag"): str,
                },
            },
        },
    }



# ===========================
# Parser for 'show interface'
# ===========================


class ShowInterface(ShowInterfaceSchema):
    """Parser for show interface, show interface <interface>"""

    cli_command = ['show interface', 'show interface {interface}']
    exclude = [
        'in_unicast_pkts',
        'out_unicast_pkts',
        'in_octets',
        'out_octets',
        'in_pkts',
        'out_pkts',
        'in_multicast_pkts',
        'out_multicast_pkts',
        'in_rate',
        'out_rate',
        'in_broadcast_pkts',
        'out_broadcast_pkts',
        'last_link_flapped',
        'in_rate_pkts',
        'out_rate_pkts',
        'out_rate_bps',
        'in_rate_bps',
        'interface_reset',
        'in_rate_pps',
        'out_rate_pps',
        'last_clear',
        'out_jumbo_packets',
        'in_jumbo_packets',
        'rxload',
        'txload',
        'in_errors',
        'mac_address',
        'phys_address',
        'in_crc_errors',
        'reliability']

    def cli(self, interface="", output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[1].format(interface=interface)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        # Ethernet2/1.10 is down (Administratively down)
        # Vlan1 is down (Administratively down), line protocol is down, autostate enabled
        # Vlan200 is down (VLAN/BD is down), line protocol is down, autostate enabled
        # Vlan23 is administratively down (Administratively down), line protocol is down, autostate enabled
        # Vlan3378 is down (VLAN/BD does not exist), line protocol is down, autostate enabled
        # Ethernet2/2 is up
        # Ethernet1/10 is down (Link not connected)
        # Ethernet1/1 is down (DCX-No ACK in 100 PDUs)
        # Ethernet1/3 is down (XCVR not inserted)
        # Ethernet1/2 is down (SFP validation failed)
        # Ethernet1/4 is down (SFP not inserted)
        # Ethernet1/11 is down (inactive)
        # Ethernet1/12 is down (Transceiver validation failed)
        # Ethernet1/13 is down (SFP validation failed)
        # Ethernet1/13 is down (Channel admin down)
        p1 = re.compile(r'^(?P<interface>\S+)\s*is\s*'
                        r'(?P<link_state>(down|up|'
                        r'inactive|Transceiver +validation +failed|'
                        r'SFP +validation +failed|Channel +admin +down))?'
                        r'(administratively\s+(?P<admin_1>(down)))?\s*'
                        r'(\(Administratively\s*(?P<admin_2>(down))\))?'
                        r'(\(VLAN\/BD\s+((is\s+(down|up))|does\s+not\s+exist)\))?'
                        r'(,\s*line\s+protocol\s+is\s+(?P<line_protocol>\w+))?'
                        r'(,\s+autostate\s+(?P<autostate>\S+))?'
                        r'(\(No\s+operational\s+members\))?'
                        r'(\(Transceiver\s+validation\s+failed\))?'
                        r'(\(Channel\s+admin\s+down\))?'
                        r'(\(Link\s+not\s+connected\))?'
                        r'(\(SFP\s+validation\s+failed\))?'
                        r'(\(SFP\s+not\s+inserted\))?'
                        r'(\(SFP\s+checksum\s+error\))?'
                        r'(\(suspended\(.*\)\))?'
                        r'(\(\S+ErrDisabled\))?'
                        r'(\(XCVR\s+not\s+inserted\))?'
                        r'(\(No\s+operational\s+members\))?'
                        r'(\(.*ACK.*\))?'
                        r'(\(inactive\))?'
                        r'(\(Hardware\s+failure\))?$')

        # admin state is up
        # admin state is up,
        # admin state is up, Dedicated Interface
        # admin state is up, Dedicated Interface, [parent interface is Ethernet2/1]
        p2 = re.compile(r'^admin +state +is'
                        r' +(?P<admin_state>([a-zA-Z0-9\/\.]+))(?:,)?'
                        r'(?: +(?P<dedicated_intf>(Dedicated Interface)))?'
                        r'(?:, +\[parent +interface +is'
                        r' +(?P<parent_intf>(\S+))\])?$')

        # Dedicated Interface
        p2_1 = re.compile(r'^Dedicated Interface$')

        # Belongs to Po1
        p2_2 = re.compile(r'^Belongs *to *(?P<port_channel_int>[a-zA-Z0-9]+)$')

        # Hardware: Ethernet, address: 5254.00ff.9c38 (bia 5254.00ff.9c38)
        p3 = re.compile(r'^Hardware: *(?P<types>[a-zA-Z0-9\/\s]+),'
                        r' *address: *(?P<mac_address>[a-z0-9\.]+)'
                        r' *\(bia *(?P<phys_address>[a-z0-9\.]+)\)$')


        # Hardware is EtherSVI, address is  547f.ee6d.7d7c
        p3_1 = re.compile(r'^Hardware is  *(?P<types>[a-zA-Z0-9\/\s]+), '
                          r'address is *(?P<mac_address>[a-z0-9\.]+)$')

        # Description: desc
        p4 = re.compile(r'^Description:\s*(?P<description>.*)$')

        # Description: VLAN information Internet Address is 10.10.10.1/24
        p4_1 = re.compile(r'^Description:\s*(?P<description>.*)'
                          r'\s+Internet\s+Address\s+is\s+(?P<ip>[0-9\.]+)'
                          r'\/(?P<prefix_length>[0-9]+)$')

        # Internet Address is 10.4.4.4/24 secondary tag 10
        p5 = re.compile(r'^Internet *Address *is *(?P<ip>[0-9\.]+)'
                        r'\/(?P<prefix_length>[0-9]+)'
                        r'(?: *(?P<secondary>(secondary)))?(?: *tag'
                        r' *(?P<route_tag>[0-9]+))?$')

        # MTU 1600 bytes, BW 768 Kbit, DLY 3330 usec
        # MTU 1500 bytes, BW 1000000 Kbit, DLY 10 usec,
        # MTU 1500 bytes, BW 1000000 Kbit
        # MTU 600 bytes, BW 10000000 Kbit , DLY 10 usec
        p6 = re.compile(r'^MTU *(?P<mtu>[0-9]+) *bytes, *BW'
                        r' *(?P<bandwidth>[0-9]+) *Kbit( *, *DLY'
                        r' *(?P<delay>[0-9]+) *usec)?,?$')

        # MTU 1500 bytes,  BW 40000000 Kbit,, BW 40000000 Kbit, DLY 10 usec
        p6_1 = re.compile(r'^MTU *(?P<mtu>[0-9]+) *bytes, *BW'
                          r' *(?P<bandwidth>[0-9]+) *Kbit, *,? *BW'
                          r' *([0-9]+) *Kbit, *DLY'
                          r' *(?P<delay>[0-9]+) *usec$')

        # reliability 255/255, txload 1/255, rxload 1/255
        p7 = re.compile(r'^reliability *(?P<reliability>[0-9\/]+),'
                        r' *txload *(?P<txload>[0-9\/]+),'
                        r' *rxload *(?P<rxload>[0-9\/]+)$')

        # Encapsulation 802.1Q Virtual LAN, Vlan ID 10, medium is broadcast
        # Encapsulation 802.1Q Virtual LAN, Vlan ID 20, medium is p2p
        # Encapsulation ARPA, medium is broadcast
        p8 = re.compile(r'^Encapsulation *(?P<encapsulation>[a-zA-Z0-9\.\s]+),'
                        r' *medium *is *(?P<medium>[a-zA-Z]+)$')

        p8_1 = re.compile(r'^Encapsulation *(?P<encapsulation>[a-zA-Z0-9\.\s]+),'
                          r' *Vlan *ID *(?P<first_dot1q>[0-9]+),'
                          r' *medium *is *(?P<medium>[a-z0-9]+)$')

        # Encapsulation ARPA, loopback not set
        p8_2 = re.compile(r'^Encapsulation *(?P<encapsulation>[a-zA-Z0-9\.\s]+),'
                          r' *([\w\s]+)$')

        # Port mode is routed
        p9 = re.compile(r'^Port *mode *is *(?P<port_mode>[a-z]+)$')

        # auto-duplex, auto-speed
        p10_1 = re.compile(r'^auto-duplex, +auto-speed$')

        # full-duplex, 1000 Mb/s
        # auto-duplex, auto-speed
        # full-duplex, 1000 Mb/s, media type is 1G
        # auto-duplex, auto-speed, media type is 10G
        p10 = re.compile(r'^(?P<duplex_mode>[a-z]+)-duplex, *(?P<port_speed>[a-z0-9\-]+)(?: '
                         r'*[G|M]b/s)?(?:, +media +type +is (?P<media_type>\w+))?$')

        # Beacon is turned off
        p11 = re.compile(r'^Beacon *is *turned *(?P<beacon>[a-z]+)$')

        # Auto-Negotiation is turned off
        p12 = re.compile(r'^Auto-Negotiation *is *turned'
                         r' *(?P<auto_negotiate>(off))$')

        # Auto-Negotiation is turned on
        p12_1 = re.compile(r'^Auto-Negotiation *is *turned'
                           r' *(?P<auto_negotiate>(on))$')

        # Input flow-control is off, output flow-control is off
        p13 = re.compile(r'^Input *flow-control *is *(?P<receive>(off)+),'
                         r' *output *flow-control *is *(?P<send>(off)+)$')

        # Input flow-control is off, output flow-control is on
        p13_1 = re.compile(r'^Input *flow-control *is *(?P<receive>(on)+),'
                           r' *output *flow-control *is *(?P<send>(on)+)$')

        # Auto-mdix is turned off
        p14 = re.compile(r'^Auto-mdix *is *turned *(?P<auto_mdix>[a-z]+)$')

        # Switchport monitor is off
        p15 = re.compile(r'^Switchport *monitor *is *(?P<switchport_monitor>[a-z]+)$')

        # EtherType is 0x8100
        p16 = re.compile(r'^EtherType *is *(?P<ethertype>[a-z0-9]+)$')

        # Members in this channel: Eth1/15, Eth1/16
        # Members in this channel: Eth1/28
        p38 = re.compile(r'^Members +in +this +channel *: *'
                         r'(?P<port_channel_member_intfs>[\w\/\.\-\,\s]+)$')

        # EEE (efficient-ethernet) : n/a
        p17 = re.compile(r'^EEE *\(efficient-ethernet\) *:'
                         r' *(?P<efficient_ethernet>[A-Za-z\/]+)$')

        # Last link flapped 00:07:28
        # Last link flapped 15week(s) 5day(s)
        p18 = re.compile(r'^Last *link *flapped'
                         r' *(?P<last_link_flapped>[\S ]+)$')

        # Last clearing of "show interface" counters never
        p19 = re.compile(r'^Last *clearing *of *\"show *interface\"'
                         r' *counters *(?P<last_clear>[a-z0-9\:]+)$')

        # Last clearing of "" counters 00:15:42
        p19_1 = re.compile(r'^Last *clearing *of *\" *\"'
                           r' *counters *(?P<last_clear>[a-z0-9\:]+)$')

        # 1 interface resets
        p20 = re.compile(r'^(?P<interface_reset>[0-9]+) *interface'
                         r' *resets$')

        # 1 minute input rate 0 bits/sec, 0 packets/sec
        p21 = re.compile(r'^(?P<load_interval>[0-9\#]+)'
                         r' *(minute|second|minutes|seconds) *input *rate'
                         r' *(?P<in_rate>[0-9]+) *bits/sec,'
                         r' *(?P<in_rate_pkts>[0-9]+) *packets/sec$')

        # 1 minute output rate 24 bits/sec, 0 packets/sec
        p22 = re.compile(r'^(?P<load_interval>[0-9\#]+)'
                         r' *(minute|second|minutes|seconds) *output'
                         r' *rate *(?P<out_rate>[0-9]+)'
                         r' *bits/sec, *(?P<out_rate_pkts>[0-9]+)'
                         r' *packets/sec$')

        # input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
        p23 = re.compile(r'^input *rate *(?P<in_rate_bps>[0-9]+) *bps,'
                         r' *(?P<in_rate_pps>[0-9]+) *pps; *output *rate'
                         r' *(?P<out_rate_bps>[0-9]+) *bps,'
                         r' *(?P<out_rate_pps>[0-9]+) *pps$')

        # RX
        # Rx
        p23_1 = re.compile(r'^(?P<rx>(RX|Rx))$')

        # 0 unicast packets  0 multicast packets  0 broadcast packets
        p24 = re.compile(r'^(?P<in_unicast_pkts>[0-9]+) +unicast +packets'
                         r' +(?P<in_multicast_pkts>[0-9]+) +multicast +packets'
                         r' +(?P<in_broadcast_pkts>[0-9]+) +broadcast +packets$')

        # 0 input packets  0 bytes
        # 607382344 input packets 445986207 unicast packets 132485585 multicast packets
        p25 = re.compile(r'^(?P<in_pkts>[0-9]+) +input +packets(?: '
                         r'+(?P<in_octets>[0-9]+) +bytes)?(?: +(?P<in_unicast_pkts>[0-9]+) '
                         r'+unicast +packets +(?P<in_multicast_pkts>[0-9]+) +multicast +packets)?$')

        # 0 jumbo packets  0 storm suppression packets
        # 1 jumbo packets  0 storm suppression bytes
        p26 = re.compile(r'^(?P<in_jumbo_packets>[0-9]+) +jumbo +packets '
                         r'+(?P<in_storm_suppression>[0-9]+) +storm +suppression +(?P<type>(packets|bytes))$')

        # 0 runts  0 giants  0 CRC/FCS  0 no buffer
        # 0 runts  0 giants  0 CRC  0 no buffer
        p27 = re.compile(r'^(?P<in_runts>[0-9]+) *runts'
                         r' *(?P<in_oversize_frame>[0-9]+) *giants'
                         r' *(?P<in_crc_errors>[0-9]+) *CRC(/FCS)?'
                         r' *(?P<in_no_buffer>[0-9]+) *no *buffer$')

        # 0 input error  0 short frame  0 overrun   0 underrun  0 ignored
        p28 = re.compile(r'^(?P<in_errors>[0-9]+) *input *error'
                         r' *(?P<in_short_frame>[0-9]+) *short *frame'
                         r' *(?P<in_overrun>[0-9]+) *overrun *(?P<in_underrun>[0-9]+)'
                         r' *underrun *(?P<in_ignored>[0-9]+) *ignored$')

        # 0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
        p29 = re.compile(r'^(?P<in_watchdog>[0-9]+) *watchdog'
                         r' *(?P<in_bad_etype_drop>[0-9]+)'
                         r' *bad *etype *drop *(?P<in_unknown_protos>[0-9]+)'
                         r' *bad *proto'
                         r' *drop *(?P<in_if_down_drop>[0-9]+) *if *down *drop$')

        # 0 input with dribble  0 input discard
        p30 = re.compile(r'^(?P<in_with_dribble>[0-9]+) *input *with'
                         r' *dribble *(?P<in_discard>[0-9]+) *input *discard$')

        # 0 Rx pause
        p31 = re.compile(r'^(?P<in_mac_pause_frames>[0-9]+) *Rx *pause$')

        # TX
        p31_1 = re.compile(r'^(?P<tx>(TX|Tx))$')

        # 0 unicast packets  0 multicast packets  0 broadcast packets
        p32 = re.compile(r'^(?P<out_unicast_pkts>[0-9]+) *unicast *packets'
                         r' *(?P<out_multicast_pkts>[0-9]+) *multicast *packets'
                         r' *(?P<out_broadcast_pkts>[0-9]+) *broadcast *packets$')

        # 0 output packets  0 bytes
        p33 = re.compile(r'^(?P<out_pkts>[0-9]+) *output *packets'
                         r' *(?P<out_octets>[0-9]+) *bytes$')

        # 0 jumbo packets
        p34 = re.compile(r'^(?P<out_jumbo_packets>[0-9]+) *jumbo *packets$')

        # 0 output error  0 collision  0 deferred  0 late collision
        p35 = re.compile(r'^(?P<out_errors>[0-9]+) *output *error'
                         r' *(?P<out_collision>[0-9]+) *collision'
                         r' *(?P<out_deferred>[0-9]+) *deferred'
                         r' *(?P<out_late_collision>[0-9]+)'
                         r' *late *collision$')

        # 0 lost carrier  0 no carrier  0 babble  0 output discard
        p36 = re.compile(r'^(?P<out_lost_carrier>[0-9]+) *lost *carrier'
                         r' *(?P<out_no_carrier>[0-9]+) *no *carrier'
                         r' *(?P<out_babble>[0-9]+) *babble'
                         r' *(?P<out_discard>[0-9]+) *output *discard$')

        # 0 Tx pause
        p37 = re.compile(r'^(?P<out_mac_pause_frames>[0-9]+) *Tx *pause$')

        # Members in this channel: Eth1/15, Eth1/16
        # Members in this channel: Eth1/28
        p38 = re.compile(r'^Members +in +this +channel *: *'
                         r'(?P<port_channel_member_intfs>[\w\/\.\-\,\s]+)$')

        # 28910552 broadcast packets 63295517997 bytes
        p39 = re.compile(r'^(?P<in_broadcast_pkts>[0-9]+) +broadcast +packets +(?P<in_octets>[0-9]+) +bytes$')

        interface_dict = {}

        rx = False
        tx = False
        for line in out.splitlines():
            line = line.replace('\t', '    ')
            line = line.strip()

            # Ethernet2/1.10 is down (Administratively down)
            # Vlan1 is down (Administratively down), line protocol is down, autostate enabled
            # Vlan200 is down (VLAN/BD is down), line protocol is down, autostate enabled
            # Vlan23 is administratively down (Administratively down), line protocol is down, autostate enabled
            # Ethernet2/2 is up
            # Ethernet1/10 is down (Link not connected)
            # Ethernet1/3 is down (XCVR not inserted)
            # Ethernet1/1 is down (DCX-No ACK in 100 PDUs)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                interface = group['interface']

                if interface not in interface_dict:
                    interface_dict[interface] = {}
                    interface_dict[interface]['port_channel'] = {}
                    interface_dict[interface]['port_channel']['port_channel_member'] = False

                if group['link_state']:
                    interface_dict[interface]['link_state'] = group['link_state']

                    if 'oper_status' not in interface_dict[interface]:
                        interface_dict[interface]['oper_status'] = group['link_state']

                if group['admin_1']:
                    interface_dict[interface]['enabled'] = False
                elif group['admin_2']:
                    interface_dict[interface]['enabled'] = False
                else:
                    interface_dict[interface]['enabled'] = True

                if group['line_protocol']:
                    interface_dict[interface]['line_protocol'] = group['line_protocol']
                    if 'oper_status' not in interface_dict[interface]:
                        interface_dict[interface]['oper_status'] = group['line_protocol']

                if group['autostate']:
                    interface_dict[interface]['autostate'] = True if group['autostate'] == 'enabled' else False
                continue

            # admin state is up
            # admin state is up,
            # admin state is up, Dedicated Interface
            # admin state is up, Dedicated Interface, [parent interface is Ethernet2/1]
            m = p2.match(line)
            if m:
                # admin_state
                admin_state = m.groupdict()['admin_state']
                interface_dict[interface]['admin_state'] = admin_state
                if admin_state == 'up':
                    interface_dict[interface]['enabled'] = True
                # dedicated_interface
                if m.groupdict()['dedicated_intf']:
                    interface_dict[interface]['dedicated_interface'] = True
                # parent_interface
                if m.groupdict()['parent_intf']:
                    interface_dict[interface]['parent_interface'] = \
                        m.groupdict()['parent_intf']
                continue

            # Dedicated Interface
            m = p2_1.match(line)
            if m:
                interface_dict[interface]['dedicated_interface'] = True
                continue

            # Belongs to Po1
            m = p2_2.match(line)
            if m:
                port_channel_int = str(m.groupdict()['port_channel_int'])
                if 'port_channel' not in interface_dict[interface]:
                    interface_dict[interface]['port_channel'] = {}
                interface_dict[interface]['port_channel'] \
                    ['port_channel_member'] = True
                interface_dict[interface]['port_channel'] \
                    ['port_channel_int'] = Common.convert_intf_name(port_channel_int)
                continue


            # Hardware: Ethernet, address: 5254.00ff.9c38 (bia 5254.00ff.9c38)
            m = p3.match(line)
            if m:
                types = m.groupdict()['types']
                mac_address = m.groupdict()['mac_address']
                phys_address = m.groupdict()['phys_address']

                interface_dict[interface]['types'] = types
                interface_dict[interface] \
                    ['mac_address'] = mac_address
                interface_dict[interface] \
                    ['phys_address'] = phys_address
                continue

            # Hardware is EtherSVI, address is  547f.ee6d.7d7c
            m = p3_1.match(line)
            if m:
                types = m.groupdict()['types']
                interface_dict[interface]['types'] = types
                mac_address = m.groupdict()['mac_address']
                interface_dict[interface] \
                    ['mac_address'] = mac_address
                continue

            # Description: VLAN information Internet Address is 10.10.10.1/24
            m = p4_1.match(line)
            if m:
                group = m.groupdict()
                description = group['description']
                interface_dict[interface]['description'] = description

                ip = group['ip']
                prefix_length = str(m.groupdict()['prefix_length'])

                address = ip + '/' + prefix_length

                interface_dict[interface].setdefault('ipv4', {})
                add_dict = interface_dict[interface]['ipv4']. \
                    setdefault(address, {})

                add_dict['ip'] = ip
                add_dict['prefix_length'] = prefix_length
                continue

            # Description: desc
            m = p4.match(line)
            if m:
                description = m.groupdict()['description']

                interface_dict[interface]['description'] = description
                continue

            # Internet Address is 10.4.4.4/24 secondary tag 10
            m = p5.match(line)
            if m:
                ip = m.groupdict()['ip']
                prefix_length = str(m.groupdict()['prefix_length'])
                secondary = m.groupdict()['secondary']
                route_tag = m.groupdict()['route_tag']
                # address = ipv4+prefix_length
                address = ip + '/' + prefix_length
                if 'ipv4' not in interface_dict[interface]:
                    interface_dict[interface]['ipv4'] = {}
                if address not in interface_dict[interface]['ipv4']:
                    interface_dict[interface]['ipv4'][address] = {}

                interface_dict[interface]['ipv4'][address] \
                    ['ip'] = ip
                interface_dict[interface]['ipv4'][address] \
                    ['prefix_length'] = prefix_length

                if secondary:
                    interface_dict[interface]['ipv4'][address] \
                        ['secondary'] = True
                if route_tag:
                    interface_dict[interface]['ipv4'][address] \
                        ['route_tag'] = route_tag
                continue

            # MTU 1600 bytes, BW 768 Kbit, DLY 3330 usec
            # MTU 1500 bytes, BW 1000000 Kbit, DLY 10 usec,
            # MTU 1500 bytes, BW 1000000 Kbit
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
            m = p6_1.match(line)
            if m:
                mtu = int(m.groupdict()['mtu'])
                bandwidth = int(m.groupdict()['bandwidth'])

                interface_dict[interface]['mtu'] = mtu
                interface_dict[interface]['bandwidth'] = bandwidth
                interface_dict[interface]['delay'] = int(m.groupdict()['delay'])
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

            # Encapsulation 802.1Q Virtual LAN, Vlan ID 10, medium is broadcast
            # Encapsulation 802.1Q Virtual LAN, Vlan ID 20, medium is p2p
            # Encapsulation ARPA, medium is broadcast
            m = p8.match(line)
            if m:
                encapsulation = m.groupdict()['encapsulation'].lower()
                encapsulation = encapsulation.replace("802.1q virtual lan", "dot1q")
                medium = m.groupdict()['medium']

                if 'encapsulations' not in interface_dict[interface]:
                    interface_dict[interface]['encapsulations'] = {}

                interface_dict[interface]['encapsulations'] \
                    ['encapsulation'] = encapsulation
                interface_dict[interface]['medium'] = medium
                continue

            m = p8_1.match(line)
            if m:
                encapsulation = m.groupdict()['encapsulation'].lower()
                encapsulation = encapsulation.replace("802.1q virtual lan", "dot1q")
                first_dot1q = str(m.groupdict()['first_dot1q'])
                medium = m.groupdict()['medium']

                if 'encapsulations' not in interface_dict[interface]:
                    interface_dict[interface]['encapsulations'] = {}

                interface_dict[interface]['encapsulations'] \
                    ['encapsulation'] = encapsulation
                interface_dict[interface]['encapsulations'] \
                    ['first_dot1q'] = first_dot1q
                interface_dict[interface]['medium'] = medium
                continue

            # Encapsulation ARPA, loopback not set
            m = p8_2.match(line)
            if m:
                encapsulation = m.groupdict()['encapsulation'].lower()

                if 'encapsulations' not in interface_dict[interface]:
                    interface_dict[interface]['encapsulations'] = {}

                interface_dict[interface]['encapsulations'] \
                    ['encapsulation'] = encapsulation
                continue

            # Port mode is routed
            m = p9.match(line)
            if m:
                port_mode = m.groupdict()['port_mode']
                interface_dict[interface]['port_mode'] = port_mode
                continue

            # auto-duplex, auto-speed
            m = p10_1.match(line)
            if m:
                # not caring for this line
                continue

            # full-duplex, 1000 Mb/s
            # auto-duplex, auto-speed
            # full-duplex, 1000 Mb/s, media type is 1G
            # auto-duplex, auto-speed, media type is 10G
            m = p10.match(line)
            if m:
                duplex_mode = m.groupdict()['duplex_mode'].lower()
                port_speed = m.groupdict()['port_speed']
                if m.groupdict()['media_type']:
                    interface_dict[interface]['media_type'] = m.groupdict()['media_type']
                else:
                    media_type = None

                interface_dict[interface]['duplex_mode'] = duplex_mode
                interface_dict[interface]['port_speed'] = port_speed
                continue

            # Beacon is turned off
            m = p11.match(line)
            if m:
                beacon = m.groupdict()['beacon']
                interface_dict[interface]['beacon'] = beacon
                continue

            # Auto-Negotiation is turned off
            m = p12.match(line)
            if m:
                auto_negotiation = m.groupdict()['auto_negotiate']
                interface_dict[interface]['auto_negotiate'] = False
                continue

            # Auto-Negotiation is turned on
            m = p12_1.match(line)
            if m:
                auto_negotiation = m.groupdict()['auto_negotiate']
                interface_dict[interface]['auto_negotiate'] = True
                continue

            # Input flow-control is off, output flow-control is off
            m = p13.match(line)
            if m:
                receive = m.groupdict()['receive']
                send = m.groupdict()['send']

                if 'flow_control' not in interface_dict[interface]:
                    interface_dict[interface]['flow_control'] = {}

                interface_dict[interface]['flow_control']['receive'] = False
                interface_dict[interface]['flow_control']['send'] = False
                continue
            # Input flow-control is off, output flow-control is on
            m = p13_1.match(line)
            if m:
                receive = m.groupdict()['receive']
                send = m.groupdict()['send']

                if 'flow_control' not in interface_dict[interface]:
                    interface_dict[interface]['flow_control'] = {}

                interface_dict[interface]['flow_control']['receive'] = True
                interface_dict[interface]['flow_control']['send'] = True
                continue

            # Auto-mdix is turned off
            m = p14.match(line)
            if m:
                auto_mdix = m.groupdict()['auto_mdix']
                interface_dict[interface]['auto_mdix'] = auto_mdix
                continue

            # Switchport monitor is off
            m = p15.match(line)
            if m:
                switchport_monitor = m.groupdict()['switchport_monitor']
                interface_dict[interface]['switchport_monitor'] = switchport_monitor
                continue

            # EtherType is 0x8100
            m = p16.match(line)
            if m:
                ethertype = m.groupdict()['ethertype']
                interface_dict[interface]['ethertype'] = ethertype
                continue

            # Members in this channel: Eth1/15, Eth1/16
            # Members in this channel: Eth1/28
            m = p38.match(line)
            if m:
                port_channel_member_intfs = m.groupdict()['port_channel_member_intfs']
                if port_channel_member_intfs:
                    if 'port_channel' not in interface_dict[interface]:
                        interface_dict[interface]['port_channel'] = {}

                    interface_dict[interface]['port_channel']['port_channel_member'] = True

                    interface_dict[interface]['port_channel']['port_channel_member_intfs'] =\
                        [Common.convert_intf_name(item) for item in port_channel_member_intfs.split(',')]

                continue

            # EEE (efficient-ethernet) : n/a
            m = p17.match(line)
            if m:
                efficient_ethernet = m.groupdict()['efficient_ethernet']
                interface_dict[interface]['efficient_ethernet'] = efficient_ethernet
                continue

            # Last link flapped 00:07:28
            m = p18.match(line)
            if m:
                last_link_flapped = m.groupdict()['last_link_flapped']
                interface_dict[interface]['last_link_flapped'] \
                    = last_link_flapped
                continue

            # Last clearing of "show interface" counters never
            m = p19.match(line)
            if m:
                last_clear = m.groupdict()['last_clear']
                continue

            # Last clearing of "" counters 00:15:42
            m = p19_1.match(line)
            if m:
                last_clear = m.groupdict()['last_clear']
                continue

            # 1 interface resets
            m = p20.match(line)
            if m:
                interface_reset = int(m.groupdict()['interface_reset'])
                interface_dict[interface]['interface_reset'] = interface_reset
                continue

            # 1 minute input rate 0 bits/sec, 0 packets/sec
            m = p21.match(line)
            if m:

                load_interval = int(m.groupdict()['load_interval'])
                in_rate = int(m.groupdict()['in_rate'])
                in_rate_pkts = int(m.groupdict()['in_rate_pkts'])

                if 'counters' not in interface_dict[interface]:
                    interface_dict[interface]['counters'] = {}
                if 'rate' not in interface_dict[interface]['counters']:
                    interface_dict[interface]['counters']['rate'] = {}

                interface_dict[interface]['counters']['rate'] \
                    ['load_interval'] = load_interval
                interface_dict[interface]['counters']['rate'] \
                    ['in_rate'] = in_rate
                interface_dict[interface]['counters']['rate'] \
                    ['in_rate_pkts'] = in_rate_pkts
                continue

            # 1 minute output rate 24 bits/sec, 0 packets/sec
            m = p22.match(line)
            if m:
                load_interval = int(m.groupdict()['load_interval'])
                out_rate = int(m.groupdict()['out_rate'])
                out_rate_pkts = int(m.groupdict()['out_rate_pkts'])

                interface_dict[interface]['counters']['rate'] \
                    ['load_interval'] = load_interval
                interface_dict[interface]['counters']['rate'] \
                    ['out_rate'] = out_rate
                interface_dict[interface]['counters']['rate'] \
                    ['out_rate_pkts'] = out_rate_pkts
                continue

            # input rate 0 bps, 0 pps; output rate 0 bps, 0 pps
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

                interface_dict[interface]['counters']['rate'] \
                    ['in_rate_bps'] = in_rate_bps
                interface_dict[interface]['counters']['rate'] \
                    ['in_rate_pps'] = in_rate_pps
                interface_dict[interface]['counters']['rate'] \
                    ['out_rate_bps'] = out_rate_bps
                interface_dict[interface]['counters']['rate'] \
                    ['out_rate_pps'] = out_rate_pps
                continue
            # RX
            # Rx
            m = p23_1.match(line)
            if m:
                rx = m.groupdict()['rx']
                if 'counters' not in interface_dict[interface]:
                    interface_dict[interface]['counters'] = {}

                interface_dict[interface]['counters']['rx'] = True
                continue

            if rx:
                # 0 unicast packets  0 multicast packets  0 broadcast packets
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

            # 0 input packets  0 bytes
            # 607382344 input packets 445986207 unicast packets 132485585 multicast packets
            m = p25.match(line)
            if m:
                group = m.groupdict()
                if 'counters' not in interface_dict[interface]:
                    interface_dict[interface]['counters'] = {}
                interface_dict[interface]['counters']['in_pkts'] = int(group['in_pkts'])
                if group['in_octets']:
                    interface_dict[interface]['counters']['in_octets'] = int(group['in_octets'])
                if group['in_unicast_pkts']:
                    interface_dict[interface]['counters']['in_unicast_pkts'] = int(group['in_unicast_pkts'])
                if group['in_multicast_pkts']:
                    interface_dict[interface]['counters']['in_multicast_pkts'] = int(group['in_multicast_pkts'])
                continue

            # 28910552 broadcast packets 63295517997 bytes
            m = p39.match(line)
            if m:
                in_octets = int(m.groupdict()['in_octets'])
                interface_dict[interface]['counters']['in_octets'] = in_octets

                in_broadcast_pkts = int(m.groupdict()['in_broadcast_pkts'])
                interface_dict[interface]['counters']['in_broadcast_pkts'] = in_broadcast_pkts

            # 0 jumbo packets  0 storm suppression packets
            m = p26.match(line)
            if m:
                in_storm_suppression = int(m.groupdict()['in_storm_suppression'])
                if m.groupdict()['type'] == 'packets':
                    interface_dict[interface]['counters']['in_storm_suppression_packets'] = in_storm_suppression
                elif m.groupdict()['type'] == 'bytes':
                    interface_dict[interface]['counters']['in_storm_suppression_bytes'] = in_storm_suppression

                interface_dict[interface]['counters']['in_jumbo_packets'] = int(m.groupdict()['in_jumbo_packets'])
                continue

            # 0 runts  0 giants  0 CRC/FCS  0 no buffer
            # 0 runts  0 giants  0 CRC  0 no buffer
            m = p27.match(line)
            if m:
                interface_dict[interface]['counters']['in_runts'] = int(m.groupdict()['in_runts'])
                interface_dict[interface]['counters']['in_oversize_frame'] = int(m.groupdict()['in_oversize_frame'])
                interface_dict[interface]['counters']['in_crc_errors'] = int(m.groupdict()['in_crc_errors'])
                interface_dict[interface]['counters']['in_no_buffer'] = int(m.groupdict()['in_no_buffer'])
                continue

            # 0 input error  0 short frame  0 overrun   0 underrun  0 ignored
            m = p28.match(line)
            if m:
                interface_dict[interface]['counters']['in_errors'] = int(m.groupdict()['in_errors'])
                interface_dict[interface]['counters']['in_short_frame'] = int(m.groupdict()['in_short_frame'])
                interface_dict[interface]['counters']['in_overrun'] = int(m.groupdict()['in_overrun'])
                interface_dict[interface]['counters']['in_underrun'] = int(m.groupdict()['in_underrun'])
                interface_dict[interface]['counters']['in_ignored'] = int(m.groupdict()['in_ignored'])
                continue

            # 0 watchdog  0 bad etype drop  0 bad proto drop  0 if down drop
            m = p29.match(line)
            if m:
                interface_dict[interface]['counters']['in_watchdog'] = int(m.groupdict()['in_watchdog'])
                interface_dict[interface]['counters']['in_bad_etype_drop'] = int(m.groupdict()['in_bad_etype_drop'])
                interface_dict[interface]['counters']['in_unknown_protos'] = int(m.groupdict()['in_unknown_protos'])
                interface_dict[interface]['counters']['in_if_down_drop'] = int(m.groupdict()['in_if_down_drop'])
                continue

            # 0 input with dribble  0 input discard
            m = p30.match(line)
            if m:
                in_with_dribble = int(m.groupdict()['in_with_dribble'])
                in_discard = int(m.groupdict()['in_discard'])

                interface_dict[interface]['counters']['in_with_dribble'] = in_with_dribble
                interface_dict[interface]['counters']['in_discard'] = in_discard
                continue

            # 0 Rx pause
            m = p31.match(line)
            if m:
                in_mac_pause_frames = int(m.groupdict()['in_mac_pause_frames'])

                interface_dict[interface]['counters']['in_mac_pause_frames'] = in_mac_pause_frames
                continue
            # TX
            # Tx
            m = p31_1.match(line)
            if m:
                rx = False
                tx = m.groupdict()['tx']
                if 'counters' not in interface_dict[interface]:
                    interface_dict[interface]['counters'] = {}
                interface_dict[interface]['counters']['tx'] = True
                continue

            if tx:
                # 0 unicast packets  0 multicast packets  0 broadcast packets
                m = p32.match(line)
                if m:
                    interface_dict[interface]['counters']['out_unicast_pkts'] = int(m.groupdict()['out_unicast_pkts'])
                    interface_dict[interface]['counters']['out_multicast_pkts'] = int(
                        m.groupdict()['out_multicast_pkts'])
                    interface_dict[interface]['counters']['out_broadcast_pkts'] = int(
                        m.groupdict()['out_broadcast_pkts'])
                    continue

            # 0 output packets  0 bytes
            m = p33.match(line)
            if m:
                out_pkts = int(m.groupdict()['out_pkts'])
                out_octets = int(m.groupdict()['out_octets'])

                interface_dict[interface]['counters']['out_pkts'] = out_pkts
                interface_dict[interface]['counters']['out_octets'] = out_octets
                continue

            # 0 jumbo packets
            m = p34.match(line)
            if m:
                out_jumbo_packets = int(m.groupdict()['out_jumbo_packets'])

                interface_dict[interface]['counters']['out_jumbo_packets'] = out_jumbo_packets
                continue

            # 0 output error  0 collision  0 deferred  0 late collision
            m = p35.match(line)
            if m:
                interface_dict[interface]['counters']['out_errors'] = int(m.groupdict()['out_errors'])
                interface_dict[interface]['counters']['out_collision'] = int(m.groupdict()['out_collision'])
                interface_dict[interface]['counters']['out_deferred'] = int(m.groupdict()['out_deferred'])
                interface_dict[interface]['counters']['out_late_collision'] = int(m.groupdict()['out_late_collision'])
                continue

            # 0 lost carrier  0 no carrier  0 babble  0 output discard
            m = p36.match(line)
            if m:
                interface_dict[interface]['counters']['out_lost_carrier'] = int(m.groupdict()['out_lost_carrier'])
                interface_dict[interface]['counters']['out_no_carrier'] = int(m.groupdict()['out_no_carrier'])
                interface_dict[interface]['counters']['out_babble'] = int(m.groupdict()['out_babble'])
                interface_dict[interface]['counters']['out_discard'] = int(m.groupdict()['out_discard'])
                continue

            # 0 Tx pause
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
             Optional('wccp_redirect_outbound'): str,
             Optional('wccp_redirect_inbound'): str,
             Optional('wccp_redirect_exclude'): str
             },
    }


# ===================================
# Parser for 'show interface vrf all'
# ===================================
class ShowIpInterfaceVrfAll(ShowIpInterfaceVrfAllSchema):
    """Parser for show ip interface vrf all
        show ip interface vrf <vrf>
        show ip interface <interface> vrf all
        show ip interface <interface> vrf <vrf>"""

    cli_command = ['show ip interface {interface} vrf {vrf}', 'show ip interface {interface} vrf all',
                   'show ip interface vrf {vrf}', 'show ip interface vrf all']
    exclude = [
        'multicast_bytes_consumed',
        'multicast_bytes_received',
        'unicast_bytes_consumed',
        'unicast_packets_consumed',
        'unicast_bytes_originated',
        'unicast_packets_originated',
        'unicast_bytes_received',
        'unicast_bytes_sent',
        'unicast_packets_received',
        'unicast_packets_sent',
        'multicast_packets_consumed',
        'multicast_packets_received',
        'multicast_bytes_originated',
        'multicast_bytes_sent',
        'multicast_packets_originated',
        'multicast_packets_sent',
        'broadcast_bytes_consumed',
        'broadcast_bytes_received',
        'broadcast_packets_consumed',
        'broadcast_packets_received',
        'multicast_groups',
        'int_stat_last_reset',
        'unicast_bytes_forwarded',
        'unicast_packets_forwarded',
        'oil_uptime',
        'iod',
        '(tunnel.*)',
        'wccp_redirect_outbound',
        'wccp_redirect_inbound',
        'wccp_redirect_exclude'
        'multicast_groups_address']

    def cli(self, interface='', vrf='', output=None):
        if interface and vrf:
            cmd = self.cli_command[0].format(interface=interface, vrf=vrf)
        elif interface:
            cmd = self.cli_command[1].format(interface=interface)
        elif vrf:
            cmd = self.cli_command[2].format(vrf=vrf)
        else:
            cmd = self.cli_command[3]
        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output
        del interface  # delete this to prevent use from below due to scope
        ip_interface_vrf_all_dict = {}
        temp_intf = []
        save_addr_for_route_tag_next_line = None

        for line in out.splitlines():
            line = line.rstrip()
            # IP Interface Status for VRF "VRF1"
            p1 = re.compile(r'^\s*IP *Interface *Status *for *VRF'
                            ' *(?P<vrf>\S+)$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                vrf = vrf.replace('"', "")
                continue

            # Ethernet2/1, Interface status: protocol-up/link-up/admin-up, iod: 36,
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

                ip_interface_vrf_all_dict[interface]['interface_status'] \
                    = interface_status
                ip_interface_vrf_all_dict[interface]['iod'] = iod
                ip_interface_vrf_all_dict[interface]['vrf'] = vrf

                # init multicast groups list to empty for this interface
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
            p2_2 = re.compile(r'(([E|e]thernet|[L|l]oopback|[T|t]unnel|'
                              r'[V|v]lan|mti|[t|T]unnel-te|[p|P]ort-channel)[\d\/\.]+):')
            m = p2_2.findall(line)
            if m and unnumbered_intf:
                temp_intf = []
                temp_intf = [i[0] for i in m]
                for intf in temp_intf:
                    if intf not in ip_interface_vrf_all_dict:
                        ip_interface_vrf_all_dict[intf] = {}
                continue
            # IP address: 10.4.4.4, IP subnet: 10.4.4.0/24 secondary
            # IP address: 10.64.4.4, IP subnet: 10.64.4.0/24
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

                    ip_interface_vrf_all_dict[intf]['ipv4'][address] \
                        ['ip'] = ip
                    ip_interface_vrf_all_dict[intf]['ipv4'][address] \
                        ['ip_subnet'] = ip_subnet
                    ip_interface_vrf_all_dict[intf]['ipv4'][address] \
                        ['prefix_length'] = prefix_length
                    if secondary:
                        ip_interface_vrf_all_dict[intf]['ipv4'][address] \
                            ['secondary'] = True
                    else:
                        ip_interface_vrf_all_dict[intf]['ipv4'][address] \
                            ['secondary'] = False

                continue

            # IP address: 192.168.106.1, IP subnet: 192.168.106.0/24 route-preference: 0, tag: 0
            # IP address: 10.115.69.2, IP subnet: 10.115.69.0/24 secondary route-preference: 0, tag: 0
            p3_1 = re.compile(r'^\s*IP *address: *(?P<ip>[0-9\.]+), *IP *subnet: '
                              r'*(?P<ip_subnet>[a-z0-9\.]+)\/(?P<prefix_length>[0-9\,]+)'
                              r'(\s*(?P<secondary>secondary)\s*)?(?: *route-preference: *'
                              r'(?P<route_preference>[0-9]+),)?'
                              r'(?: *tag: *(?P<route_tag>[0-9]+)?)?$')
            m = p3_1.match(line)

            if m:
                group = m.groupdict()
                ip = group['ip']
                ip_subnet = group['ip_subnet']
                prefix_length = group['prefix_length']
                route_tag = group['route_tag']
                route_preference = group['route_preference']

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

                    ip_interface_vrf_all_dict[intf]['ipv4'][address] \
                        ['ip'] = ip
                    ip_interface_vrf_all_dict[intf]['ipv4'][address] \
                        ['ip_subnet'] = ip_subnet
                    ip_interface_vrf_all_dict[intf]['ipv4'][address] \
                        ['prefix_length'] = prefix_length
                    if route_tag:
                        ip_interface_vrf_all_dict[intf]['ipv4'][address] \
                            ['route_tag'] = route_tag
                    else:
                        save_addr_for_route_tag_next_line = address
                    if route_preference:
                        ip_interface_vrf_all_dict[intf]['ipv4'][address] \
                            ['route_preference'] = route_preference

                    if group['secondary']:
                        ip_interface_vrf_all_dict[intf]['ipv4'][address]['secondary'] = True
                continue

            # IP address: none
            p3_2 = re.compile('^\s*IP +address: +(?P<ip>\S+)$')
            m = p3_2.match(line)
            if m:
                group = m.groupdict()
                address = group.get('ip')
                if 'ipv4' not in ip_interface_vrf_all_dict:
                    ip_interface_vrf_all_dict[interface]['ipv4'] = {}
                if address not in ip_interface_vrf_all_dict[interface]['ipv4']:
                    ip_interface_vrf_all_dict[interface]['ipv4'][address] = {}
                ip_interface_vrf_all_dict[interface]['ipv4'][address] \
                    ['ip'] = address
                continue

            #   0
            p3_3 = re.compile(r'^\s*(?P<route_tag>\d+)$')
            m = p3_3.match(line)
            if m:
                group = m.groupdict()
                route_tag = group['route_tag']
                if temp_intf:
                    temp_intf.append(interface)
                    intf_lst = temp_intf
                else:
                    intf_lst = [interface]

                if save_addr_for_route_tag_next_line:
                    for intf in intf_lst:
                        address = save_addr_for_route_tag_next_line
                        ip_interface_vrf_all_dict[intf]['ipv4'][address] \
                            ['route_tag'] = route_tag
                        save_addr_for_route_tag_next_line = None
                continue

            # IP broadcast address: 255.255.255.255
            p4 = re.compile(r'^\s*IP *broadcast *address:'
                            ' *(?P<broadcast_address>[0-9\.]+)$')
            m = p4.match(line)
            if m:
                broadcast_address = str(m.groupdict()['broadcast_address'])
                if 'ipv4' in ip_interface_vrf_all_dict[interface]:
                    ip_interface_vrf_all_dict[interface]['ipv4'][address]['broadcast_address'] = broadcast_address
                continue

            # IP multicast groups locally joined: none
            # 224.0.0.6  224.0.0.5  224.0.0.2
            p5 = re.compile(r'^\s*IP *multicast *groups *locally *joined:'
                            ' *(?P<multicast_groups_address>[a-z]+)$')
            m = p5.match(line)
            if m:
                multicast_groups_address = m.groupdict()['multicast_groups_address']

                ip_interface_vrf_all_dict[interface]['multicast_groups_address'] \
                    = multicast_groups_address
                continue

            #     show ip interface vrf all
            p5_0 = re.compile(r'^\s*show')
            m = p5_0.match(line)
            if m:
                continue

            # 224.0.0.6  224.0.0.5  224.0.0.2
            p5_1 = re.compile(r'^\s*(?P<multicast_groups_address>[a-fA-F0-9\.\s]+)$')
            m = p5_1.match(line)
            if m:
                multicast_groups_address = str(m.groupdict()['multicast_groups_address'])

                # Split string of addressed into a list
                multicast_groups_address = [str(i) for i in multicast_groups_address.split()]

                # Add to previous created list
                for mgroup in multicast_groups_address:
                    multicast_groups.append(mgroup)

                ip_interface_vrf_all_dict[interface]['multicast_groups'] \
                    = sorted(multicast_groups)
                continue

            # IP MTU: 1600 bytes (using link MTU)
            p6 = re.compile(r'^\s*IP *MTU: *(?P<ip_mtu>[0-9]+)'
                            ' *bytes *\(using *link *MTU\)$')
            m = p6.match(line)
            if m:
                ip_mtu = int(m.groupdict()['ip_mtu'])

                ip_interface_vrf_all_dict[interface]['ip_mtu'] = ip_mtu
                continue

            # IP primary address route-preference: 0, tag: 0
            p7 = re.compile(r'^\s*IP *primary *address *route-preference:'
                            ' *(?P<route_preference>[0-9]+), *tag:'
                            ' *(?P<route_tag>[0-9]+)$')
            m = p7.match(line)
            if m:
                route_preference = m.groupdict()['route_preference']
                route_tag = m.groupdict()['route_tag']

                if route_preference:
                    ip_interface_vrf_all_dict[interface]['ipv4'][address]['route_preference'] \
                        = route_preference

                if route_tag:
                    ip_interface_vrf_all_dict[interface]['ipv4'][address] \
                        ['route_tag'] = route_tag
                continue

            # IP proxy ARP : disabled
            p8 = re.compile(r'^\s*IP *proxy *ARP *: *(?P<proxy_arp>[a-z]+)$')
            m = p8.match(line)
            if m:
                proxy_arp = m.groupdict()['proxy_arp']

                ip_interface_vrf_all_dict[interface]['proxy_arp'] = proxy_arp
                continue

            # IP Local Proxy ARP : disabled
            p9 = re.compile(r'^\s*IP *Local *Proxy *ARP *:'
                            ' *(?P<local_proxy_arp>[a-z]+)$')
            m = p9.match(line)
            if m:
                local_proxy_arp = m.groupdict()['local_proxy_arp']

                ip_interface_vrf_all_dict[interface]['local_proxy_arp'] \
                    = local_proxy_arp
                continue

            # IP multicast routing: disabled
            p10 = re.compile(r'^\s*IP *multicast *routing:'
                             ' *(?P<multicast_routing>[a-z]+)$')
            m = p10.match(line)
            if m:
                multicast_routing = m.groupdict()['multicast_routing']

                ip_interface_vrf_all_dict[interface]['multicast_routing'] \
                    = multicast_routing
                continue

            # IP icmp redirects: disabled
            p11 = re.compile(r'^\s*IP *icmp *redirects:'
                             ' *(?P<icmp_redirects>[a-z]+)$')
            m = p11.match(line)
            if m:
                icmp_redirects = m.groupdict()['icmp_redirects']

                ip_interface_vrf_all_dict[interface]['icmp_redirects'] \
                    = icmp_redirects
                continue

            # IP directed-broadcast: disabled
            p12 = re.compile(r'^\s*IP directed-broadcast:'
                             ' *(?P<directed_broadcast>[a-z]+)$')
            m = p12.match(line)
            if m:
                directed_broadcast = m.groupdict()['directed_broadcast']

                ip_interface_vrf_all_dict[interface]['directed_broadcast'] \
                    = directed_broadcast
                continue

            # IP Forwarding: disabled
            p13 = re.compile(r'^\s*IP *Forwarding: *(?P<ip_forwarding>[a-z]+)$')
            m = p13.match(line)
            if m:
                ip_forwarding = m.groupdict()['ip_forwarding']

                ip_interface_vrf_all_dict[interface]['ip_forwarding'] \
                    = ip_forwarding
                continue

            # IP icmp unreachables (except port): disabled
            p14 = re.compile(r'^\s*IP *icmp *unreachables *\(except *port\):'
                             ' *(?P<icmp_unreachable>[a-z]+)$')
            m = p14.match(line)
            if m:
                icmp_unreachable = m.groupdict()['icmp_unreachable']

                ip_interface_vrf_all_dict[interface]['icmp_unreachable'] \
                    = icmp_unreachable
                continue

            # IP icmp port-unreachable: enabled
            p15 = re.compile(r'^\s*IP *icmp *port-unreachable:'
                             ' *(?P<icmp_port_unreachable>[a-z]+)$')
            m = p15.match(line)
            if m:
                icmp_port_unreachable = m.groupdict()['icmp_port_unreachable']

                ip_interface_vrf_all_dict[interface]['icmp_port_unreachable'] \
                    = icmp_port_unreachable
                continue

            # IP unicast reverse path forwarding: loose allow default
            p16 = re.compile(r'^\s*IP\s+unicast\s+reverse\s+path\s+forwarding:\s+'
                             '(?P<unicast_reverse_path>([\w\s]+)\s*)$')
            m = p16.match(line)
            if m:
                unicast_reverse_path = m.groupdict()['unicast_reverse_path']

                ip_interface_vrf_all_dict[interface]['unicast_reverse_path'] \
                    = unicast_reverse_path
                continue

            # IP load sharing: none
            p17 = re.compile(r'^\s*IP *load *sharing: *(?P<load_sharing>\w+)$')
            m = p17.match(line)
            if m:
                load_sharing = m.groupdict()['load_sharing']

                ip_interface_vrf_all_dict[interface]['load_sharing'] \
                    = load_sharing
                continue

            # IP interface statistics last reset: never
            # ip interface statistics last reset: never
            p18 = re.compile(r'^\s*(IP|ip) *interface *statistics *last *reset:'
                             r' *(?P<int_stat_last_reset>[a-zA-Z0-9\:]+)')
            m = p18.match(line)
            if m:
                int_stat_last_reset = m.groupdict()['int_stat_last_reset']

                ip_interface_vrf_all_dict[interface]['int_stat_last_reset'] \
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
                # Unicast packets    : 0/0/0/0/0
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

                    ip_interface_vrf_all_dict[interface]['ipv4']['counters'] \
                        ['unicast_packets_sent'] = int(m.groupdict()['unicast_packets_sent'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters'] \
                        ['unicast_packets_received'] = int(m.groupdict()['unicast_packets_received'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters'] \
                        ['unicast_packets_forwarded'] = int(m.groupdict()['unicast_packets_forwarded'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters'] \
                        ['unicast_packets_originated'] = int(m.groupdict()['unicast_packets_originated'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters'] \
                        ['unicast_packets_consumed'] = int(m.groupdict()['unicast_packets_consumed'])
                    continue

                # Unicast bytes      : 0/0/0/0/0
                p21 = re.compile(r'^\s*Unicast *bytes *:'
                                 ' *(?P<unicast_bytes_sent>[0-9]+)\/'
                                 '(?P<unicast_bytes_received>[0-9]+)\/'
                                 '(?P<unicast_bytes_forwarded>[0-9]+)\/'
                                 '(?P<unicast_bytes_originated>[0-9]+)\/'
                                 '(?P<unicast_bytes_consumed>[0-9]+)$')
                m = p21.match(line)
                if m:
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters'] \
                        ['unicast_bytes_sent'] = int(m.groupdict()['unicast_bytes_sent'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters'] \
                        ['unicast_bytes_received'] = int(m.groupdict()['unicast_bytes_received'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters'] \
                        ['unicast_bytes_forwarded'] = int(m.groupdict()['unicast_bytes_forwarded'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters'] \
                        ['unicast_bytes_originated'] = int(m.groupdict()['unicast_bytes_originated'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters'] \
                        ['unicast_bytes_consumed'] = int(m.groupdict()['unicast_bytes_consumed'])
                    continue

                # Multicast packets  : 0/0/0/0/0
                p22 = re.compile(r'^\s*Multicast *packets *:'
                                 ' *(?P<multicast_packets_sent>[0-9]+)\/'
                                 '(?P<multicast_packets_received>[0-9]+)\/'
                                 '(?P<multicast_packets_forwarded>[0-9]+)\/'
                                 '(?P<multicast_packets_originated>[0-9]+)\/'
                                 '(?P<multicast_packets_consumed>[0-9]+)$')
                m = p22.match(line)
                if m:
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters'] \
                        ['multicast_packets_sent'] = int(m.groupdict()['multicast_packets_sent'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters'] \
                        ['multicast_packets_received'] = int(m.groupdict()['multicast_packets_received'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters'] \
                        ['multicast_packets_forwarded'] = int(m.groupdict()['multicast_packets_forwarded'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters'] \
                        ['multicast_packets_originated'] = int(m.groupdict()['multicast_packets_originated'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters'] \
                        ['multicast_packets_consumed'] = int(m.groupdict()['multicast_packets_consumed'])
                    continue

                # Multicast bytes    : 0/0/0/0/0
                p23 = re.compile(r'^\s*Multicast *bytes *:'
                                 ' *(?P<multicast_bytes_sent>[0-9]+)\/'
                                 '(?P<multicast_bytes_received>[0-9]+)\/'
                                 '(?P<multicast_bytes_forwarded>[0-9]+)\/'
                                 '(?P<multicast_bytes_originated>[0-9]+)\/'
                                 '(?P<multicast_bytes_consumed>[0-9]+)$')
                m = p23.match(line)
                if m:
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters'] \
                        ['multicast_bytes_sent'] = int(m.groupdict()['multicast_bytes_sent'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters'] \
                        ['multicast_bytes_received'] = int(m.groupdict()['multicast_bytes_received'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters'] \
                        ['multicast_bytes_forwarded'] = int(m.groupdict()['multicast_bytes_forwarded'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters'] \
                        ['multicast_bytes_originated'] = int(m.groupdict()['multicast_bytes_originated'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters'] \
                        ['multicast_bytes_consumed'] = int(m.groupdict()['multicast_bytes_consumed'])
                    continue

                # Broadcast packets  : 0/0/0/0/0
                p24 = re.compile(r'^\s*Broadcast *packets *:'
                                 ' *(?P<broadcast_packets_sent>[0-9]+)\/'
                                 '(?P<broadcast_packets_received>[0-9]+)\/'
                                 '(?P<broadcast_packets_forwarded>[0-9]+)\/'
                                 '(?P<broadcast_packets_originated>[0-9]+)\/'
                                 '(?P<broadcast_packets_consumed>[0-9]+)$')
                m = p24.match(line)
                if m:
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters'] \
                        ['broadcast_packets_sent'] = int(m.groupdict()['broadcast_packets_sent'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters'] \
                        ['broadcast_packets_received'] = int(m.groupdict()['broadcast_packets_received'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters'] \
                        ['broadcast_packets_forwarded'] = int(m.groupdict()['broadcast_packets_forwarded'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters'] \
                        ['broadcast_packets_originated'] = int(m.groupdict()['broadcast_packets_originated'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters'] \
                        ['broadcast_packets_consumed'] = int(m.groupdict()['broadcast_packets_consumed'])
                    continue

                # Broadcast bytes    : 0/0/0/0/0
                p25 = re.compile(r'^\s*Broadcast *bytes *:'
                                 ' *(?P<broadcast_bytes_sent>[0-9]+)\/'
                                 '(?P<broadcast_bytes_received>[0-9]+)\/'
                                 '(?P<broadcast_bytes_forwarded>[0-9]+)\/'
                                 '(?P<broadcast_bytes_originated>[0-9]+)\/'
                                 '(?P<broadcast_bytes_consumed>[0-9]+)$')
                m = p25.match(line)
                if m:
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters'] \
                        ['broadcast_bytes_sent'] = int(m.groupdict()['broadcast_bytes_sent'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters'] \
                        ['broadcast_bytes_received'] = int(m.groupdict()['broadcast_bytes_received'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters'] \
                        ['broadcast_bytes_forwarded'] = int(m.groupdict()['broadcast_bytes_forwarded'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters'] \
                        ['broadcast_bytes_originated'] = int(m.groupdict()['broadcast_bytes_originated'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters'] \
                        ['broadcast_bytes_consumed'] = int(m.groupdict()['broadcast_bytes_consumed'])
                    continue

                # Labeled packets    : 0/0/0/0/0
                p26 = re.compile(r'^\s*Labeled *packets *:'
                                 ' *(?P<labeled_packets_sent>[0-9]+)\/'
                                 '(?P<labeled_packets_received>[0-9]+)\/'
                                 '(?P<labeled_packets_forwarded>[0-9]+)\/'
                                 '(?P<labeled_packets_originated>[0-9]+)\/'
                                 '(?P<labeled_packets_consumed>[0-9]+)$')
                m = p26.match(line)
                if m:
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters'] \
                        ['labeled_packets_sent'] = int(m.groupdict()['labeled_packets_sent'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters'] \
                        ['labeled_packets_received'] = int(m.groupdict()['labeled_packets_received'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters'] \
                        ['labeled_packets_forwarded'] = int(m.groupdict()['labeled_packets_forwarded'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters'] \
                        ['labeled_packets_originated'] = int(m.groupdict()['labeled_packets_originated'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters'] \
                        ['labeled_packets_consumed'] = int(m.groupdict()['labeled_packets_consumed'])
                    continue

                # Labeled bytes      : 0/0/0/0/0
                p27 = re.compile(r'^\s*Labeled *bytes *:'
                                 ' *(?P<labeled_bytes_sent>[0-9]+)\/'
                                 '(?P<labeled_bytes_received>[0-9]+)\/'
                                 '(?P<labeled_bytes_forwarded>[0-9]+)\/'
                                 '(?P<labeled_bytes_originated>[0-9]+)\/'
                                 '(?P<labeled_bytes_consumed>[0-9]+)$')
                m = p27.match(line)
                if m:
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters'] \
                        ['labeled_bytes_sent'] = int(m.groupdict()['labeled_bytes_sent'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters'] \
                        ['labeled_bytes_received'] = int(m.groupdict()['labeled_bytes_received'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters'] \
                        ['labeled_bytes_forwarded'] = int(m.groupdict()['labeled_bytes_forwarded'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters'] \
                        ['labeled_bytes_originated'] = int(m.groupdict()['labeled_bytes_originated'])
                    ip_interface_vrf_all_dict[interface]['ipv4']['counters'] \
                        ['labeled_bytes_consumed'] = int(m.groupdict()['labeled_bytes_consumed'])
                    continue

            # WCCP Redirect outbound: disabled
            p28 = re.compile(r'^\s*WCCP *Redirect *outbound:'
                             ' *(?P<wccp_redirect_outbound>[a-z]+)$')
            m = p28.match(line)
            if m:
                wccp_redirect_outbound = m.groupdict()['wccp_redirect_outbound']

                ip_interface_vrf_all_dict[interface]['wccp_redirect_outbound'] \
                    = wccp_redirect_outbound
                continue

            # WCCP Redirect inbound: disabled
            p29 = re.compile(r'^\s*WCCP *Redirect *inbound:'
                             ' *(?P<wccp_redirect_inbound>[a-z]+)$')
            m = p29.match(line)
            if m:
                wccp_redirect_inbound = m.groupdict()['wccp_redirect_inbound']

                ip_interface_vrf_all_dict[interface]['wccp_redirect_inbound'] \
                    = wccp_redirect_inbound
                continue

            # WCCP Redirect exclude: disabled
            p30 = re.compile(r'^\s*WCCP *Redirect *exclude:'
                             ' *(?P<wccp_redirect_exclude>[a-z]+)$')
            m = p30.match(line)
            if m:
                wccp_redirect_exclude = m.groupdict()['wccp_redirect_exclude']

                ip_interface_vrf_all_dict[interface]['wccp_redirect_exclude'] \
                    = wccp_redirect_exclude
                continue

            # IP unnumbered interface (loopback0)
            p31 = re.compile(r'^\s*IP +unnumbered +interface +\((?P<unnum_intf>[\w\/\.]+)\)$')
            m = p31.match(line)
            if m:
                unnum_intf = m.groupdict()['unnum_intf']
                if 'ipv4' in ip_interface_vrf_all_dict[interface]:
                    ip_interface_vrf_all_dict[interface]['ipv4']['unnumbered'] = {}
                    ip_interface_vrf_all_dict[interface]['ipv4']['unnumbered']['interface_ref'] \
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
    """Parser for show vrf all interface
                show vrf <vrf> interface <interface>
                show vrf <vrf> interface
                show vrf all interface <interface>"""

    cli_command = ['show vrf {vrf} interface {interface}',
                   'show vrf all interface {interface}',
                   'show vrf {vrf} interface', 'show vrf all interface']
    exclude = [
        '(Null.*)']

    def cli(self, interface='', vrf='', output=None):
        if interface and vrf:
            cmd = self.cli_command[0].format(interface=interface, vrf=vrf)
        elif interface:
            cmd = self.cli_command[1].format(interface=interface)
        elif vrf:
            cmd = self.cli_command[2].format(vrf=vrf)
        else:
            cmd = self.cli_command[3]
        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output

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
            # port-channel1101          default                              1  --

            p1 = re.compile(r'^\s*(?P<interface>[a-zA-Z0-9\.\/\-]+)'
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
                vrf_all_interface_dict[interface] \
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
             Optional('switchport_monitor'): str,
             Optional('switchport_mode'): str,
             Optional('access_vlan'): int,
             'switchport_enable': bool,
             Optional('access_vlan_mode'): str,
             Optional('native_vlan'): int,
             Optional('native_vlan_mode'): str,
             Optional('trunk_vlans'): str,
             Optional('admin_priv_vlan_primary_host_assoc'): str,
             Optional('admin_priv_vlan_secondary_host_assoc'): str,
             Optional('admin_priv_vlan_primary_mapping'): str,
             Optional('admin_priv_vlan_secondary_mapping'): str,
             Optional('admin_priv_vlan_trunk_native_vlan'): str,
             Optional('admin_priv_vlan_trunk_encapsulation'): str,
             Optional('admin_priv_vlan_trunk_normal_vlans'): str,
             Optional('admin_priv_vlan_trunk_private_vlans'): str,
             Optional('operational_private_vlan'): str
             },
    }


# ======================================
# Parser for 'show interface switchport'
# ======================================
class ShowInterfaceSwitchport(ShowInterfaceSwitchportSchema):
    """Parser for show interface switchport
                show interface <interface> switchport"""

    cli_command = ['show interface switchport', 'show interface {interface} switchport']

    def cli(self, interface="", output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[1].format(interface=interface)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        interface_switchport_dict = {}

        for line in out.splitlines():
            line = line.rstrip()

            # Name: Ethernet2/2
            p1 = re.compile(r'^\s*Name: *(?P<interface>[a-zA-Z0-9\/\-\.]+)$')
            m = p1.match(line)
            if m:
                interface = m.groupdict()['interface']

                if interface not in interface_switchport_dict:
                    interface_switchport_dict[interface] = {}
                    continue

            # Switchport: Enabled
            p2 = re.compile(r'^\s*Switchport: *(?P<switchport_status>[a-zA-Z\s]+)$')
            m = p2.match(line)
            if m:
                switchport_status = m.groupdict()['switchport_status'].lower()
                interface_switchport_dict[interface]['switchport_status'] = switchport_status

                interface_switchport_dict[interface]['switchport_enable'] = True \
                    if 'enable' in switchport_status else False

                continue

            # Switchport Monitor: Not enabled
            p3 = re.compile(r'^\s*Switchport *Monitor: *(?P<switchport_monitor>[a-zA-Z\s]+)$')
            m = p3.match(line)
            if m:
                switchport_monitor = m.groupdict()['switchport_monitor']

                interface_switchport_dict[interface]['switchport_monitor'] = switchport_monitor
                continue

            # Operational Mode: Private-vlan host
            p4 = re.compile(r'^\s*Operational *Mode: *(?P<switchport_mode>[\w\s-]+)$')
            m = p4.match(line)
            if m:
                interface_switchport_dict[interface]['switchport_mode'] = m.groupdict()['switchport_mode']
                continue

            # Access Mode VLAN: 1 (default)
            # Access Mode VLAN: 7 (server-vlan7)
            # Access Mode VLAN: 551 (Test_VM_192.168.1.0/24)
            p5 = re.compile(r'^\s*Access *Mode *VLAN: *(?P<access_vlan>[0-9]+)'
                            '(?: *\((?P<access_vlan_mode>[\S\s]+)\))?$')
            m = p5.match(line)
            if m:
                access_vlan = int(m.groupdict()['access_vlan'])
                access_vlan_mode = m.groupdict()['access_vlan_mode']

                interface_switchport_dict[interface] \
                    ['access_vlan'] = access_vlan
                interface_switchport_dict[interface] \
                    ['access_vlan_mode'] = access_vlan_mode
                continue

            # Trunking Native Mode VLAN: 1 (default)
            # Trunking Native Mode VLAN: 200 (VLAN0200)
            # Trunking Native Mode VLAN: 3967 (Vlan not created)
            # Trunking Native Mode VLAN: 451 (VM_Machines_192.168.1.0/24)
            p6 = re.compile(r'^\s*Trunking *Native *Mode *VLAN:'
                            ' *(?P<native_vlan>[0-9]+)'
                            ' *\((?P<native_vlan_mode>[\S\s]+)\)$')
            m = p6.match(line)
            if m:
                native_vlan = int(m.groupdict()['native_vlan'])
                native_vlan_mode = m.groupdict()['native_vlan_mode']

                interface_switchport_dict[interface] \
                    ['native_vlan'] = native_vlan
                interface_switchport_dict[interface] \
                    ['native_vlan_mode'] = native_vlan_mode
                continue

            # Trunking VLANs Allowed: 100,300
            p7 = re.compile(r'^\s*Trunking *VLANs *Allowed: *(?P<trunk_vlans>[0-9\,\-]+)$')
            m = p7.match(line)
            if m:
                trunk_vlans = m.groupdict()['trunk_vlans']

                interface_switchport_dict[interface]['trunk_vlans'] = trunk_vlans
                continue

            # Administrative private-vlan primary host-association: 2000
            p8 = re.compile(r'^\s*Administrative *private-vlan *primary'
                            ' *host-association:'
                            ' *(?P<admin_priv_vlan_primary_host_assoc>\w+)$')
            m = p8.match(line)
            if m:
                admin_priv_vlan_primary_host_assoc = m.groupdict()['admin_priv_vlan_primary_host_assoc']

                interface_switchport_dict[interface][
                    'admin_priv_vlan_primary_host_assoc'] = admin_priv_vlan_primary_host_assoc
                continue

            # Administrative private-vlan secondary host-association: 110
            p9 = re.compile(r'^\s*Administrative *private-vlan *secondary'
                            ' *host-association:'
                            ' *(?P<admin_priv_vlan_secondary_host_assoc>\w+)$')
            m = p9.match(line)
            if m:
                admin_priv_vlan_secondary_host_assoc \
                    = m.groupdict()['admin_priv_vlan_secondary_host_assoc']

                interface_switchport_dict[interface] \
                    ['admin_priv_vlan_secondary_host_assoc'] = admin_priv_vlan_secondary_host_assoc
                continue

            # Administrative private-vlan primary mapping: none
            p10 = re.compile(r'^\s*Administrative *private-vlan *primary'
                             ' *mapping:'
                             ' *(?P<admin_priv_vlan_primary_mapping>\w+)$')
            m = p10.match(line)
            if m:
                admin_priv_vlan_primary_mapping \
                    = m.groupdict()['admin_priv_vlan_primary_mapping']

                interface_switchport_dict[interface] \
                    ['admin_priv_vlan_primary_mapping'] \
                    = admin_priv_vlan_primary_mapping
                continue

            # Administrative private-vlan secondary mapping: none
            p11 = re.compile(r'^\s*Administrative *private-vlan *secondary'
                             ' *mapping:'
                             ' *(?P<admin_priv_vlan_secondary_mapping>\w+)$')
            m = p11.match(line)
            if m:
                admin_priv_vlan_secondary_mapping = m.groupdict()['admin_priv_vlan_secondary_mapping']

                interface_switchport_dict[interface] \
                    ['admin_priv_vlan_secondary_mapping'] = admin_priv_vlan_secondary_mapping
                continue

            # Administrative private-vlan trunk native VLAN: 1
            p12 = re.compile(r'^\s*Administrative *private-vlan *trunk *native'
                             ' *VLAN:'
                             ' *(?P<admin_priv_vlan_trunk_native_vlan>\w+)$')
            m = p12.match(line)
            if m:
                admin_priv_vlan_trunk_native_vlan = m.groupdict()['admin_priv_vlan_trunk_native_vlan']

                interface_switchport_dict[interface] \
                    ['admin_priv_vlan_trunk_native_vlan'] = admin_priv_vlan_trunk_native_vlan
                continue

            # Administrative private-vlan trunk encapsulation: dot1q
            p13 = re.compile(r'^\s*Administrative *private-vlan *trunk'
                             ' *encapsulation:'
                             ' *(?P<admin_priv_vlan_trunk_encapsulation>[a-z0-9]+)$')
            m = p13.match(line)
            if m:
                admin_priv_vlan_trunk_encapsulation = m.groupdict()['admin_priv_vlan_trunk_encapsulation']

                interface_switchport_dict[interface] \
                    ['admin_priv_vlan_trunk_encapsulation'] = admin_priv_vlan_trunk_encapsulation
                continue

            # Administrative private-vlan trunk normal VLANs: none
            p14 = re.compile(r'^\s*Administrative *private-vlan *trunk'
                             ' *normal VLANs:'
                             ' *(?P<admin_priv_vlan_trunk_normal_vlans>\w+)$')
            m = p14.match(line)
            if m:
                admin_priv_vlan_trunk_normal_vlans = m.groupdict()['admin_priv_vlan_trunk_normal_vlans']

                interface_switchport_dict[interface] \
                    ['admin_priv_vlan_trunk_normal_vlans'] = admin_priv_vlan_trunk_normal_vlans
                continue

            # Administrative private-vlan trunk private VLANs: none
            # Administrative private-vlan trunk private VLANs: none(0 none)
            p15 = re.compile(r'^\s*Administrative *private-vlan *trunk'
                             ' *private VLANs:'
                             ' *(?P<admin_priv_vlan_trunk_private_vlans>\w+)(?P<dummy>.*)?$')
            m = p15.match(line)
            if m:
                admin_priv_vlan_trunk_private_vlans = m.groupdict()['admin_priv_vlan_trunk_private_vlans']

                interface_switchport_dict[interface] \
                    ['admin_priv_vlan_trunk_private_vlans'] = admin_priv_vlan_trunk_private_vlans
                continue

            # Operational private-vlan: (2500,101)
            p16 = re.compile(r'^\s*Operational *private-vlan:'
                             ' *(?P<operational_private_vlan>\S+)$')
            m = p16.match(line)
            if m:
                operational_private_vlan = m.groupdict()['operational_private_vlan']

                interface_switchport_dict[interface] \
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
    """Parser for show ipv6 interface vrf all
        show ipv6 interface vrf <vrf>
        show ipv6 interface <interface> vrf all
        show ipv6 interface <interface> vrf <vrf>"""

    cli_command = ['show ipv6 interface {interface} vrf {vrf}', 'show ipv6 interface {interface} vrf all',
                   'show ipv6 interface vrf {vrf}', 'show ipv6 interface vrf all']
    exclude = [
        'multicast_bytes_consumed',
        'multicast_packets_consumed',
        'multicast_bytes_originated',
        'multicast_packets_originated',
        'unicast_bytes_consumed',
        'unicast_packets_consumed',
        'unicast_bytes_originated',
        'unicast_packets_originated',
        'ipv6_multicast_groups',
        'iod',
        'multicast_groups',
        'unicast_bytes_forwarded',
        'unicast_packets_forwarded',
        'ipv6_link_local']

    def cli(self, interface='', vrf='', output=None):
        if interface and vrf:
            cmd = self.cli_command[0].format(interface=interface, vrf=vrf)
        elif interface:
            cmd = self.cli_command[1].format(interface=interface)
        elif vrf:
            cmd = self.cli_command[2].format(vrf=vrf)
        else:
            cmd = self.cli_command[3]
        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output
        del interface
        # Init variables
        ipv6_interface_dict = {}
        ipv6_addresses = None
        anycast_addresses = None
        virtual_add = False
        multicast_groups = False

        for line in out.splitlines():
            line = line.rstrip()

            # IPv6 Interface Status for VRF "VRF1"
            p1 = re.compile(r'^\s*IPv6 *Interface *Status *for *VRF'
                            ' *(?P<vrf>\S+)$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                vrf = vrf.replace('"', "")
                continue

            # Ethernet2/1, Interface status: protocol-up/link-up/admin-up, iod: 36
            # port-channel2.101, Interface status: protocol-down/link-down/admin-up, iod: 71
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
                ip = m.groupdict()['ip']
                prefix_length = m.groupdict()['prefix_length']
                status = m.groupdict()['status'].lower()

                address = ip + '/' + prefix_length

                if 'ipv6' not in ipv6_interface_dict[interface]:
                    ipv6_interface_dict[interface]['ipv6'] = {}
                if address not in ipv6_interface_dict[interface]['ipv6']:
                    ipv6_interface_dict[interface]['ipv6'][address] = {}

                ipv6_interface_dict[interface]['ipv6'][address] \
                    ['ip'] = ip
                ipv6_interface_dict[interface]['ipv6'][address] \
                    ['prefix_length'] = prefix_length

                if ipv6_addresses:
                    ipv6_interface_dict[interface]['ipv6'][address] \
                        ['status'] = status
                elif anycast_addresses:
                    ipv6_interface_dict[interface]['ipv6'][address] \
                        ['anycast'] = True
                continue

            # IPv6 subnet:  2001:db8:1:1::/64
            p4 = re.compile(r'^\s*IPv6 *subnet:'
                            ' *(?P<ipv6_subnet>[a-z0-9\:\/]+)$')
            m = p4.match(line)
            if m:
                ipv6_subnet = m.groupdict()['ipv6_subnet']

                ipv6_interface_dict[interface]['ipv6']['ipv6_subnet'] = ipv6_subnet
                continue

            # IPv6 link-local address: fe80::a8aa:bbff:febb:cccc (default) [VALID]
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

            # IPv6 virtual addresses configured: none
            p6 = re.compile(r'^\s*IPv6 *virtual *addresses *configured:'
                            ' *(?P<ipv6_virtual_add>\w+)$')
            m = p6.match(line)
            if m:
                ipv6_virtual_add = m.groupdict()['ipv6_virtual_add']

                ipv6_interface_dict[interface]['ipv6']['ipv6_virtual_add'] = ipv6_virtual_add
                continue

            # IPv6 virtual addresses configured:
            #        fe80::5:73ff:fea0:2  2001:db8:7746:fa41::1
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

                    # split string of addresses to list
                    ipv6_virtual_addresses = [str(j) for j in ipv6_virtual_addresses.split()]

                    # Add to previous created list
                    for add in ipv6_virtual_addresses:
                        ipv6_virtual_groups.append(add)

                    ipv6_interface_dict[interface]['ipv6']['ipv6_virtual_groups'] \
                        = sorted(ipv6_virtual_groups)
                    continue

            # IPv6 multicast routing: disabled
            p7 = re.compile(r'^\s*IPv6 *multicast *routing:'
                            ' *(?P<ipv6_multicast_routing>[a-z]+)$')
            m = p7.match(line)
            if m:
                ipv6_multicast_routing = m.groupdict()['ipv6_multicast_routing']

                ipv6_interface_dict[interface]['ipv6']['ipv6_multicast_routing'] = ipv6_multicast_routing
                continue

            # IPv6 report link local: disabled
            p8 = re.compile(r'^\s*IPv6 *report *link *local:'
                            ' *(?P<ipv6_report_link_local>[a-z]+)$')
            m = p8.match(line)
            if m:
                ipv6_report_link_local = m.groupdict()['ipv6_report_link_local']

                ipv6_interface_dict[interface]['ipv6']['ipv6_report_link_local'] \
                    = ipv6_report_link_local
                continue

            # IPv6 Forwarding feature: disabled
            p9 = re.compile(r'^\s*IPv6 *Forwarding *feature:'
                            ' *(?P<ipv6_forwarding_feature>[a-z]+)$')
            m = p9.match(line)
            if m:
                ipv6_forwarding_feature = m.groupdict()['ipv6_forwarding_feature']

                ipv6_interface_dict[interface]['ipv6']['ipv6_forwarding_feature'] \
                    = ipv6_forwarding_feature
                continue

            # IPv6 multicast groups locally joined:
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

                    ipv6_interface_dict[interface]['ipv6']['ipv6_multicast_groups'] \
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
                ipv6_interface_dict[interface]['ipv6']['ipv6_multicast_entries'] \
                    = ipv6_multicast_entries
                continue

            # IPv6 MTU: 1600 (using link MTU)
            p13 = re.compile(r'^\s*IPv6 *MTU: *(?P<ipv6_mtu>[0-9]+)'
                             ' *\(using *link *MTU\)$')
            m = p13.match(line)
            if m:
                ipv6_mtu = int(m.groupdict()['ipv6_mtu'])

                ipv6_interface_dict[interface]['ipv6']['ipv6_mtu'] = ipv6_mtu
                continue

            # IPv6 unicast reverse path forwarding: loose allow default
            p14 = re.compile(r'^\s*IPv6\s+unicast\s+reverse\s+path\s+forwarding:\s+'
                             '(?P<ipv6_unicast_rev_path_forwarding>([\w\s]+)\s*)$')
            m = p14.match(line)
            if m:
                ipv6_unicast_rev_path_forwarding = m.groupdict() \
                    ['ipv6_unicast_rev_path_forwarding']

                ipv6_interface_dict[interface]['ipv6'] \
                    ['ipv6_unicast_rev_path_forwarding'] \
                    = ipv6_unicast_rev_path_forwarding
                continue

            # IPv6 load sharing: none
            p15 = re.compile(r'^\s*IPv6 *load *sharing:'
                             ' *(?P<ipv6_load_sharing>\w+)$')
            m = p15.match(line)
            if m:
                ipv6_load_sharing = m.groupdict()['ipv6_load_sharing']

                ipv6_interface_dict[interface]['ipv6']['ipv6_load_sharing'] \
                    = ipv6_load_sharing
                continue

            # IPv6 interface statistics last reset: never
            p16 = re.compile(r'^\s*IPv6 *interface *statistics *last *reset:'
                             ' *(?P<ipv6_last_reset>[a-z]+)$')
            m = p16.match(line)
            if m:
                ipv6_last_reset = m.groupdict()['ipv6_last_reset']

                ipv6_interface_dict[interface]['ipv6']['ipv6_last_reset'] \
                    = ipv6_last_reset
                continue

            # Unicast packets:      0/0/0
            p18 = re.compile(r'^\s*Unicast *packets:'
                             ' *(?P<unicast_packets_forwarded>[0-9]+)\/'
                             '(?P<unicast_packets_originated>[0-9]+)\/'
                             '(?P<unicast_packets_consumed>[0-9]+)$')
            m = p18.match(line)
            if m:
                if 'counters' not in ipv6_interface_dict[interface]['ipv6']:
                    ipv6_interface_dict[interface]['ipv6']['counters'] = {}

                ipv6_interface_dict[interface]['ipv6']['counters'] \
                    ['unicast_packets_forwarded'] = int(m.groupdict()['unicast_packets_forwarded'])
                ipv6_interface_dict[interface]['ipv6']['counters'] \
                    ['unicast_packets_originated'] = int(m.groupdict()['unicast_packets_originated'])
                ipv6_interface_dict[interface]['ipv6']['counters'] \
                    ['unicast_packets_consumed'] = int(m.groupdict()['unicast_packets_consumed'])
                continue

            # Unicast bytes:        0/0/0
            p19 = re.compile(r'^\s*Unicast *bytes: *(?P<unicast_bytes_forwarded>[0-9]+)'
                             '\/(?P<unicast_bytes_originated>[0-9]+)\/'
                             '(?P<unicast_bytes_consumed>[0-9]+)$')
            m = p19.match(line)
            if m:
                ipv6_interface_dict[interface]['ipv6']['counters'] \
                    ['unicast_bytes_forwarded'] = int(m.groupdict()['unicast_bytes_forwarded'])
                ipv6_interface_dict[interface]['ipv6']['counters'] \
                    ['unicast_bytes_originated'] = int(m.groupdict()['unicast_bytes_originated'])
                ipv6_interface_dict[interface]['ipv6']['counters'] \
                    ['unicast_bytes_consumed'] = int(m.groupdict()['unicast_bytes_consumed'])
                continue

            # Multicast packets:    0/12/9
            p20 = re.compile(r'^\s*Multicast *packets: *(?P<multicast_packets_forwarded>[0-9]+)'
                             '\/(?P<multicast_packets_originated>[0-9]+)\/'
                             '(?P<multicast_packets_consumed>[0-9]+)$')
            m = p20.match(line)
            if m:
                ipv6_interface_dict[interface]['ipv6']['counters'] \
                    ['multicast_packets_forwarded'] = int(m.groupdict()['multicast_packets_forwarded'])
                ipv6_interface_dict[interface]['ipv6']['counters'] \
                    ['multicast_packets_originated'] = int(m.groupdict()['multicast_packets_originated'])
                ipv6_interface_dict[interface]['ipv6']['counters'] \
                    ['multicast_packets_consumed'] = int(m.groupdict()['multicast_packets_consumed'])
                continue

            # Multicast bytes:      0/1144/640
            p21 = re.compile(r'^\s*Multicast *bytes: *(?P<multicast_bytes_forwarded>[0-9]+)\/'
                             '(?P<multicast_bytes_originated>[0-9]+)\/'
                             '(?P<multicast_bytes_consumed>[0-9]+)$')
            m = p21.match(line)
            if m:
                ipv6_interface_dict[interface]['ipv6']['counters'] \
                    ['multicast_bytes_forwarded'] = int(m.groupdict()['multicast_bytes_forwarded'])
                ipv6_interface_dict[interface]['ipv6']['counters'] \
                    ['multicast_bytes_originated'] = int(m.groupdict()['multicast_bytes_originated'])
                ipv6_interface_dict[interface]['ipv6']['counters'] \
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

    # *************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).
    cli_command = 'show ip interface brief'
    exclude = [
        '(tunnel.*)']

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cmd = self.cli_command

    def cli(self, output=None):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: exe
        cuting, transforming, returning
        '''
        if output is None:
            out = self.device.execute(self.cmd)
        else:
            out = output

        interface_dict = {}
        for line in out.splitlines():
            line = line.rstrip()
            p1 = re.compile(r'^\s*Interface +IP Address +Interface Status$')
            m = p1.match(line)
            if m:
                continue

            p2 = re.compile(
                r'^\s*(?P<interface>[a-zA-Z0-9\/\.\-]+) +(?P<ip_address>[a-z0-9\.]+) +(?P<interface_status>[a-z\-\/]+)$')
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
                    new_ip_address = interface_dict['interface'] \
                                         [interface]['vlan_id'][vlan_id]['ip_address'] + ipaddress_extension
                    interface_dict['interface'][interface]['vlan_id'][vlan_id]['ip_address'] = \
                        new_ip_address
                else:
                    new_ip_address = interface_dict['interface'] \
                                         [interface]['ip_address'] + ipaddress_extension
                    interface_dict['interface'][interface]['ip_address'] = new_ip_address
                continue

        return interface_dict


# ===========================================
# Parser for 'show ip interface brief | vlan'
# ===========================================
class ShowIpInterfaceBriefPipeVlan(ShowIpInterfaceBrief):
    """Parser for show ip interface brief | include Vlan"""

    # *************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).
    cli_command = 'show ip interface brief | include Vlan'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.cmd = self.cli_command


# =================================
# Schema for 'show interface brief'
# =================================
class ShowInterfaceBriefSchema(MetaParser):
    """Schema for show interface brief"""

    schema = {
        'interface': {
            Optional('ethernet'): {
                Any(): {
                    'vlan': str,
                    'type': str,
                    'mode': str,
                    'status': str,
                    'speed': str,
                    'reason': str,
                    'port_ch': str,
                },
            },
            Optional('port'): {
                Any(): {
                    Optional('vrf'): str,
                    Optional('status'): str,
                    Optional('ip_address'): str,
                    Optional('speed'): str,
                    Optional('mtu'): int,
                },
            },
            Optional('port_channel'): {
                Any(): {
                    Optional('vlan'): str,
                    Optional('type'): str,
                    Optional('mode'): str,
                    Optional('status'): str,
                    Optional('speed'): str,
                    Optional('reason'): str,
                    Optional('protocol'): str,
                },
            },
            Optional('loopback'): {
                Any(): {
                    Optional('status'): str,
                    Optional('description'): str,
                },
            },
            Optional('vlan'): {
                Any(): {
                    Optional('type'): str,
                    Optional('status'): str,
                    Optional('reason'): str,
                },
            },
            Optional('nve'): {
                Any(): {
                    Optional('mtu'): str,
                    Optional('status'): str,
                    Optional('reason'): str,
                },
            },
        }
    }


# =================================
# Parser for 'show interface brief'
# =================================
class ShowInterfaceBrief(ShowInterfaceBriefSchema):
    '''Parser for:
        * show interface brief
        * show interface {interface} brief
    '''

    cli_command = ['show interface brief',
                   'show interface {interface} brief']

    exclude = ['reason']

    def cli(self, interface=None, output=None):

        if output is None:
            # Determine command
            if interface:
                cmd = self.cli_command[1].format(interface=interface)
            else:
                cmd = self.cli_command[0]
            # Execute command
            output = self.device.execute(cmd)

        # Init
        parsed_dict = {}
        vlan_flag = False
        # Port   VRF          Status IP Address                              Speed    MTU
        p1 = re.compile(r'^Port +VRF +Status +IP Address +Speed +MTU$')

        # mgmt0  --           up     172.25.143.76                           1000     1500
        # mgmt0  --           up     172.25.143.76                           --     1500
        p2 = re.compile(r'^(?P<port>[a-zA-Z0-9]+) +(?P<vrf>[a-zA-Z0-9\-]+)'
                        r' +(?P<status>[a-zA-Z]+) +(?P<ip_address>(\S+))'
                        r' +(?P<speed>\S+) +(?P<mtu>[0-9]+)$')

        # Ethernet      VLAN    Type Mode   Status  Reason                   Speed     Port
        p3 = re.compile(r'^Ethernet +VLAN +Type +Mode +Status +Reason +Speed'
                        r' +Port$')

        # Eth1/6        1       eth  access down    Link not connected         auto(D) --
        # Eth1/4.2      112     eth  routed down    Administratively down    auto(D) --
        p4 = re.compile(r'^(?P<interface>[^pP][\S]+) +(?P<vlan>[a-zA-Z0-9\-]+) +'
                        r'(?P<type>[a-zA-Z]+) +(?P<mode>[a-z]+) +'
                        r'(?P<status>[a-z]+) +(?P<reason>[a-zA-Z\s]+) +'
                        r'(?P<speed>[0-9a-zA-Z\(\)]+) +(?P<port>[0-9\-]+)$')

        # Port-channel VLAN    Type Mode   Status  Reason                    Speed   Protocol
        p5 = re.compile(r'^Port-channel +VLAN +Type +Mode +Status +Reason'
                        r' +Speed +Protocol$')

        # Po8          1       eth  access down    No operational members      auto(I)  none
        # Po10         --      eth  routed up      none                                 a-40G(D)  lacp
        # Po10.1       2       eth  routed up      none                                 a-40G(D)    --
        p6 = re.compile(r'^(?P<interface>(P|p)\S+) +(?P<vlan>\S+) '
                        r'+(?P<type>[a-zA-Z]+) +(?P<mode>[a-z]+) '
                        r'+(?P<status>[a-z]+) +(?P<reason>[\w\s]+) '
                        r'+(?P<speed>\S+) +(?P<protocol>[\w\-]+)$')

        # Interface     Status     Description
        p7 = re.compile(r'^Interface +Status +Description$')

        # Lo0           up         --
        p8 = re.compile(r'^(?P<interface>[a-zA-Z0-9\/]+) +(?P<status>[a-z]+)'
                        r' +(?P<description>[a-zA-Z\s\-]+)$')

        # Interface Secondary VLAN(Type)                    Status Reason
        p9 = re.compile(r'^Interface +Secondary +VLAN\(Type\) +Status +Reason$')

        # Vlan1     --                                      down   Administratively down
        # Vlan2     --                                      down   VLAN/BD is down
        p10 = re.compile(r'^(?P<interface>[\S]+) +(?P<type>[\w\-]+) +(?P<status>[\w]+)'
                         r' +(?P<reason>[\w\s\-\/]+)$')

        # Port           Status Reason          MTU
        p11 = re.compile(r'^Port +Status +Reason + MTU$')
        # nve1           up     none            9216
        p12 = re.compile(r'^(?P<interface>[a-zA-Z0-9]+) +(?P<status>[a-z]+)'
                         r' +(?P<reason>[a-zA-Z\s\-]+) +(?P<mtu>[0-9]+)$')
        for line in output.splitlines():
            line = line.strip()

            # Port   VRF          Status IP Address                              Speed    MTU
            m = p1.match(line)
            if m:
                port_dict = parsed_dict.setdefault('interface', {}). \
                    setdefault('port', {})
                continue

            # mgmt0  --           up     172.25.143.76                           1000     1500
            m = p2.match(line)
            if m:
                group = m.groupdict()
                intf_dict = port_dict. \
                    setdefault(Common.convert_intf_name(group['port']), {})
                intf_dict['vrf'] = group['vrf']
                intf_dict['status'] = group['status']
                intf_dict['ip_address'] = group['ip_address']
                intf_dict['speed'] = group['speed']
                intf_dict['mtu'] = int(group['mtu'])
                continue

            # Ethernet      VLAN    Type Mode   Status  Reason                   Speed     Port
            m = p3.match(line)
            if m:
                eth_dict = parsed_dict.setdefault('interface', {}). \
                    setdefault('ethernet', {})
                continue

            # Eth1/6        1       eth  access down    Link not connected         auto(D) --
            m = p4.match(line)
            if m:
                group = m.groupdict()
                intf_dict = eth_dict. \
                    setdefault(Common.convert_intf_name(group['interface']), {})
                intf_dict['vlan'] = group['vlan']
                intf_dict['type'] = group['type']
                intf_dict['mode'] = group['mode']
                intf_dict['status'] = group['status']
                intf_dict['reason'] = group['reason'].strip()
                intf_dict['speed'] = group['speed']
                intf_dict['port_ch'] = group['port']
                continue

            # Port-channel VLAN    Type Mode   Status  Reason                    Speed   Protocol
            m = p5.match(line)
            if m:
                pch_dict = parsed_dict.setdefault('interface', {}). \
                    setdefault('port_channel', {})
                continue

            # Po8          1       eth  access down    No operational members      auto(I)  none
            m = p6.match(line)
            if m:
                group = m.groupdict()
                intf_dict = pch_dict. \
                    setdefault(Common.convert_intf_name(group['interface']), {})
                intf_dict['vlan'] = group['vlan']
                intf_dict['type'] = group['type']
                intf_dict['mode'] = group['mode']
                intf_dict['status'] = group['status']
                intf_dict['reason'] = group['reason'].strip()
                intf_dict['speed'] = group['speed']
                intf_dict['protocol'] = group['protocol']
                continue

            # Interface     Status     Description
            m = p7.match(line)
            if m:
                loopback_dict = parsed_dict.setdefault('interface', {}). \
                    setdefault('loopback', {})
                continue

            # Lo0           up         --
            m = p8.match(line)
            if m:
                group = m.groupdict()
                intf_dict = loopback_dict. \
                    setdefault(Common.convert_intf_name(group['interface']), {})
                intf_dict['status'] = group['status']
                intf_dict['description'] = group['description']
                continue

            # Interface Secondary VLAN(Type)                    Status Reason
            m = p9.match(line)
            if m:
                vlan_flag = True
                vlan_dict = parsed_dict.setdefault('interface', {}). \
                    setdefault('vlan', {})
                continue

            # Vlan1     --                                      down   Administratively down
            m = p10.match(line)
            if m and vlan_flag:
                group = m.groupdict()
                intf_dict = vlan_dict. \
                    setdefault(Common.convert_intf_name(group['interface']), {})
                intf_dict['type'] = group['type']
                intf_dict['status'] = group['status']
                intf_dict['reason'] = group['reason']
                continue
            # Port           Status Reason          MTU
            m = p11.match(line)
            if m:
                nve_dict = parsed_dict.setdefault('interface', {}). \
                    setdefault('nve', {})
                continue

            # nve1           up     none            9216
            m = p12.match(line)
            if m:
                group = m.groupdict()
                intf_dict = nve_dict. \
                    setdefault(group['interface'], {})
                intf_dict['status'] = group['status']
                intf_dict['reason'] = group['reason'].strip()
                intf_dict['mtu'] = group['mtu']
                continue

        return parsed_dict


# ==============================================================================
# Schema for 'show running-config interface {interface} or | section ^interface
# ==============================================================================
class ShowRunningConfigInterfaceSchema(MetaParser):
    """Schema for
        show running-config interface
        show running-config | section ^interface
        show running-config interface

    The 2nd and 3rd cmd returns the same result. The reason to have them both is so that users can use either
    """

    schema = {'interface':
                  {Any():
                       {Optional('shutdown'): bool,
                        Optional('switchport'): bool,
                        Optional('switchport_mode'): str,
                        Optional('trunk_vlans'): str,
                        Optional('trunk_native_vlan'): str,
                        Optional('description'): str,
                        Optional('access_vlan'): str,
                        Optional('speed'): int,
                        Optional('duplex'): str,
                        Optional('vpc'): str,
                        Optional('port_channel'): {
                            Optional('port_channel_mode'): str,
                            Optional('port_channel_int'): str,
                        },
                        Optional('host_reachability_protocol'): str,
                        Optional('source_interface'): str,
                        Optional('member_vni'):
                            {Any():
                                 {Optional('associate_vrf'): bool,
                                  Optional('mcast_group'): str,
                                  Optional('suppress_arp'): bool,
                                  }
                             },
                        Optional('mtu'): int,
                        Optional('ip_address'): str,
                        Optional('vrf_member'): str,
                        }
                   },
              }


# ======================================================
# Parser for 'show running-config interface {interface}'
# ======================================================
class ShowRunningConfigInterface(ShowRunningConfigInterfaceSchema):
    """Parser for
        show running-config interface {interface},
        show running-config | section ^interface,
        show running-config interface

        The 2nd and 3rd cmd returns the same result. The reason to have them both is so that users can use either

    """

    cli_command = ['show running-config interface {interface}',
                   'show running-config | section ^interface',
                   'show running-config interface']

    def cli(self, interface=None, output=None):
        # Determine command
        if output is None:
            if interface:
                cmd = self.cli_command[0].format(interface=interface)
            else:
                if 'section ^interface' in self.cli_command:
                    cmd = self.cli_command[1]
                else:
                    cmd = self.cli_command[2]
            # Execute command
            out = self.device.execute(cmd)
        else:
            out = output
        # Init vars
        ret_dict = {}
        interface_dict = {}

        # interface nve1
        # interface Ethernet1/1
        p1 = re.compile(r'^interface +(?P<intf_name>\S+)$')

        # no shutdown
        p2 = re.compile(r'^\s*no shutdown$')

        # host-reachability protocol bgp
        p3 = re.compile(r'^\s*host-reachability protocol +(?P<protocol>[a-zA-Z]+)$')

        # source-interface loopback1
        p4 = re.compile(r'^\s*source-interface +(?P<src_intf>[a-zA-Z0-9\-]+)$')

        # member vni 8100
        # member vni 9100 associate-vrf
        # member vni 2001201-2001300
        p5 = re.compile(r'^\s*member vni +(?P<vni>[0-9\-]+)( +(?P<associate_vrf>[a-zA-Z\-]+))?$')

        # mcast-group 225.0.1.25
        p6 = re.compile(r'^\s*mcast-group +(?P<ip>[0-9\.]+)$')

        # suppress-arp
        p7 = re.compile(r'^\s*suppress-arp$')

        # switchport
        p8 = re.compile(r'^switchport$')

        # switchport mode trunk
        p9 = re.compile(r'^switchport +mode +(?P<mode>\S+)$')

        # switchport trunk allowed vlan 1-99,101-199,201-1399,1401-4094
        p10 = re.compile(r'^switchport +trunk +allowed +vlan +(?P<trunk_vlans>\S+)$')

        # switchport trunk native vlan x
        p10_1 = re.compile(r'^switchport +trunk +native +vlan +(?P<trunk_native_vlan>\S+)$')

        # switchport access vlan x
        p10_2 = re.compile(r'^switchport +access +vlan +(?P<access_vlan>\S+)$')

        # channel-group 1 mode active
        p11 = re.compile(r'^channel-group +(?P<port_channel_int>\d+) +mode +(?P<mode>\S+)$')

        # speed 1000
        p12 = re.compile(r'^speed +(?P<speed>\d+)$')

        # duplex full
        p13 = re.compile(r'^duplex +(?P<duplex>\S+)$')

        # description DeviceA-description
        p14 = re.compile(r'^description +(?P<description>.+)$')

        # vpc ID, for port-channels only
        p15 = re.compile(r'^vpc +(?P<vpc>\S+)$')

        # mtu 1500
        p16 = re.compile(r'^mtu +(?P<mtu>\S+)$')

        # ip address 10.10.6.73/30
        p17 = re.compile(r'^ip address +(?P<ip_address>[a-z0-9\.]+.*)$')

        # vrf member TEST
        p18 = re.compile(r'^vrf member +(?P<vrf_member>\S+)$')

        # no switchport
        p19 = re.compile(r'^no switchport$')

        for line in out.splitlines():
            line = line.strip()

            # interface nve1
            # interface Ethernet1/1
            m = p1.match(line)
            if m:
                interface = str(m.groupdict()['intf_name'])
                interface_dict = ret_dict.setdefault('interface', {}). \
                    setdefault(interface, {})
                continue

            m = p2.match(line)
            if m:
                interface_dict['shutdown'] = False
                continue

            m = p3.match(line)
            if m:
                interface_dict['host_reachability_protocol'] = \
                    str(m.groupdict()['protocol'])
                continue

            m = p4.match(line)
            if m:
                interface_dict['source_interface'] = \
                    str(m.groupdict()['src_intf'])
                continue

            m = p5.match(line)
            if m:
                if 'member_vni' not in interface_dict:
                    interface_dict['member_vni'] = {}
                vni = str(m.groupdict()['vni'])

                if '-' in vni:
                    vni_range = re.findall(r'(?P<first_vni>[0-9]+)\-(?P<last_vni>[0-9]+)?$', vni)
                    members = range(int(vni_range[0][0]), int(vni_range[0][1]) + 1)
                else:
                    members = [vni]

                for memb in members:
                    interface_dict['member_vni'][str(memb)] = {}

                    if m.groupdict()['associate_vrf']:
                        interface_dict['member_vni'][str(memb)]['associate_vrf'] = \
                            True
                continue

            m = p6.match(line)
            if m:
                for memb in members:
                    interface_dict['member_vni'][str(memb)]['mcast_group'] = \
                        str(m.groupdict()['ip'])
                continue

            m = p7.match(line)
            if m:
                for memb in members:
                    interface_dict['member_vni'][str(memb)]['suppress_arp'] = \
                        True
                continue

            m = p8.match(line)
            if m:
                interface_dict.update({'switchport': True})
                continue

            m = p9.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({'switchport_mode': group['mode']})
                continue

            m = p10.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({'trunk_vlans': group['trunk_vlans']})
                continue

            m = p10_1.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({'trunk_native_vlan': group['trunk_native_vlan']})
                continue

            m = p10_2.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({'switchport_mode': 'access'})
                interface_dict.update({'access_vlan': group['access_vlan']})
                continue

            m = p11.match(line)
            if m:
                group = m.groupdict()
                port_channel_dict = interface_dict.setdefault('port_channel', {})
                port_channel_dict.update({'port_channel_int': group['port_channel_int']})
                port_channel_dict.update({'port_channel_mode': group['mode']})
                continue

            m = p12.match(line)
            if m:
                interface_dict.update({'speed': int(m.groupdict()['speed'])})
                continue

            m = p13.match(line)
            if m:
                interface_dict.update({'duplex': m.groupdict()['duplex']})
                continue

            m = p14.match(line)
            if m:
                interface_dict.update({'description': m.groupdict()['description']})
                continue

            m = p15.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({'vpc': group['vpc']})
                continue

            m = p16.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({'mtu': int(group['mtu'])})
                continue

            m = p17.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({'ip_address': group['ip_address']})
                continue

            m = p18.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({'vrf_member': group['vrf_member']})
                continue

            m = p19.match(line)
            if m:
                interface_dict.update({'switchport': False})
                continue

        return ret_dict


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

    cli_command = 'show nve interface {interface}'

    def cli(self, interface, output=None):
        cmd = ""
        if output is None:
            if interface:
                cmd = self.cli_command.format(interface=interface)
                out = self.device.execute(cmd)
        else:
            out = output

        # Init vars
        interface_dict = {}

        # Interface: nve1, State: Up, encapsulation: VXLAN
        p1 = re.compile(r'^\s*Interface: +(?P<intf>[\w]+)\,'
                        ' +State: +(?P<state>[\w]+)\, +encapsulation:'
                        ' +(?P<encapsulation>[\w]+)$')

        # Source-Interface: loopback0 (primary: 10.4.0.1, secondary: 0.0.0.0)
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
    schema = {
        'interface': {
            Any(): {
                Optional('vrf'): str,
                Optional('ip_address'): str,
                Optional('interface_status'): str
            }
        }
    }



# ============================================
# Parser for 'show ip interface brief vrf all'
# ============================================
class ShowIpInterfaceBriefVrfAll(ShowIpInterfaceBriefVrfAllSchema):
    """Parser for show ip interface brief vrf all"""

    # *************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).

    cli_command = ['show ip interface brief vrf all | include {ip}', 'show ip interface brief vrf all']

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

        # IP Interface Status for VRF "default"(1)
        p1 = re.compile(r'^IP Interface Status for VRF "(?P<vrf>(\S+))"')

        # mgmt0                10.255.5.169    protocol-up/link-up/admin-up
        p2 = re.compile(r'^\s*(?P<interface>[a-zA-Z0-9\/\.\-]+) '
                        r'+(?P<ip_address>[a-z0-9\.]+) +(?P<interface_status>[a-z\-\/]+)$')

        ret_dict = {}
        # sets empty variable so it always exists. Useful for cases such as:
        # CH-P2-TOR-1# show ip interface brief vrf all | include 172.27.230.58
        # mgmt0                172.27.230.58   protocol-up/link-up/admin-up
        vrf = None
        for line in out.splitlines():
            line = line.rstrip()

            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                continue

            m = p2.match(line)
            if m:
                interface_dict = ret_dict.setdefault('interface', {}).setdefault(m.groupdict()['interface'], {})

                if vrf:
                    interface_dict.update({'vrf': vrf})

                interface_dict.update({'ip_address': m.groupdict()['ip_address']})
                interface_dict.update({'interface_status': m.groupdict()['interface_status']})
                continue

        return ret_dict


#############################################################################
# Schema For show interface Description
#############################################################################

class ShowInterfaceDescriptionSchema(MetaParser):
    """schema for show interface description
    """

    schema = {
        'interfaces': {
            Any(): {
                Optional('type'): str,
                Optional('speed'): str,
                'description': str
            }
        }
    }


class ShowInterfaceDescription(ShowInterfaceDescriptionSchema):
    """parser for show interface description
    """

    cli_command = ['show interface description', 'show interface {interface} description']

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

        # -------------------------------------------------------------------------------
        # Port          Type   Speed   Description
        # -------------------------------------------------------------------------------
        # Eth1/1        eth    10G     --

        p1 = re.compile(r'(?P<interface>(\S+)) +(?P<type>(\S+))? +(?P<speed>(\S+))? +(?P<description>(.*))$')

        for line in out.splitlines():
            line = line.strip()
            line = line.replace('\t', '')
            # -------------------------------------------------------------------------------
            # Port          Type   Speed   Description
            # -------------------------------------------------------------------------------
            # Eth1/1        eth    10G     --
            m = p1.match(line)
            if m and m.groupdict()['description'] != 'Description':
                group = m.groupdict()
                interface = Common.convert_intf_name(group['interface'])
                intf_dict = result_dict.setdefault('interfaces', {}).setdefault(interface, {})
                if group['type'] is not None:
                    intf_dict['type'] = str(group['type'])
                if group['speed'] is not None:
                    intf_dict['speed'] = str(group['speed'])
                intf_dict['description'] = str(group['description'])
                index += 1
                continue

        return result_dict


#############################################################################
# Parser For show interface status
#############################################################################

class ShowInterfaceStatusSchema(MetaParser):
    """schema for show interface status
    """

    schema = {
        'interfaces': {
            Any(): {
                Optional('name'): str,
                'status': str,
                Optional('vlan'): str,
                Optional('duplex_code'): str,
                Optional('port_speed'): str,
                Optional('type'): str,
                Optional('reason'): str,
            }
        }
    }


class ShowInterfaceStatus(ShowInterfaceStatusSchema):
    """parser for
        * show interface status
        * show interfaces {interfaces} status

    """

    cli_command = ['show interface status', 'show interface {interface} status']

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
        flag = False

        # Interface     Name                Status    Reason
        p0 = re.compile(r'Interface\s+Name\s+Status\s+Reason')

        # Port          Name               Status    Vlan      Duplex  Speed   Type
        # --------------------------------------------------------------------------------
        # Eth1/1        KeepAlive          connected routed    full    10G     10g
        # Eth1/2        AOTLXPRISS10004    connected trunk     full    10G     10g
        # mgmt0         --                 connected routed    full    1000    --
        # Po1           VPC_PeerLink       connected trunk     full    40G     --
        # Vlan366       BigData            connected routed    auto    auto    --
        # Eth101/1/10   DO-HYPER-03        connected 101       full    a-1000
        # Lo0            --                  connected  routed     auto     --       --
        # Eth1/19       --                 connected 105       full    10G     SFP-H10GB-C
        # Eth102/1/1    xxx (Gb1) [test_s] connected 110       full    a-1000
        # Eth102/1/2    yyy (Gb1) [test_s] connected trunk     full    a-1000
        # Eth102/1/3    zzz (Eth1, test_st connected 205       full    a-1000
        p1 = re.compile(r'(?P<interface>(\S+))\s+(?P<name>(\S+))?\s'
                        r'+(?P<status>(\S+))?\s+(?P<vlan>(\S+))'
                        r' +(?P<duplex_code>(\S+))\s'
                        r'+(?P<port_speed>(\S+))(\s*(?P<type>(\S*)))?$')

        # Eth1/5 *** L2 L3-CIS-N connected trunk full a-1000 1000base-T
        # Eth1/4 *** FEX 2248TP  connected 1     full a-10G  Fabric Exte
        p1_1 = re.compile(r'(?P<interface>(\S+))\s+'
                          r'(?P<name>([\S\s]+))(?<! )\s+'
                          r'(?P<status>(\S+))\s+'
                          r'(?P<vlan>(\S+))\s+'
                          r'(?P<duplex_code>([a-z]+))\s+'
                          r'(?P<port_speed>(\S+))\s*'
                          r'(?P<type>([\S\s]*))$')

        # Tunnel7       --                  up        no-reason 
        p2 = re.compile(r'(?P<interface>(\S+))\s+(?P<name>([\S\s]+))(?<! )\s+(?P<status>(\S+))\s+(?P<reason>(\S+))')

        for line in out.splitlines():
            line = line.strip()

            m = p0.match(line)
            if m:
                flag = True
                continue

            m = p1.match(line) or p1_1.match(line)
            if m and m.groupdict()['name'] != 'Name' and not flag:
                group = m.groupdict()
                interface = Common.convert_intf_name(group['interface'])
                intf_dict = result_dict.setdefault('interfaces', {}).setdefault(interface, {})

                keys = ['name', 'status', 'vlan', 'duplex_code', 'port_speed', 'type']

                for k in keys:
                    if group[k] and group[k] != '--':
                        intf_dict[k] = group[k]
                continue

            m = p2.match(line)
            if m and flag:
                group = m.groupdict()
                interface = Common.convert_intf_name(group['interface'])
                intf_dict = result_dict.setdefault('interfaces', {}).setdefault(interface, {})

                keys = ['name', 'status', 'reason']

                for k in keys:
                    if group[k] and group[k] != '--':
                        intf_dict[k] = group[k]
                continue

        return result_dict


# ========================================
# Schema for 'show interface capabilities'
# ========================================
class ShowInterfaceCapabilitiesSchema(MetaParser):
    """Schema for show interface capabilities"""

    schema = {
        Any(): {
            Optional('model'): str,
            Optional('sfp'): bool,
            Optional('type'): str,
            Optional('speed'): list,
            Optional('duplex'): str,
            Optional('trunk_encap_type'): str,
            Optional('channel'): str,
            Optional('broadcast_suppression'): {
                Optional('type'): str,
                Optional('value'): str
            },
            Optional('flowcontrol'): {
                Optional('rx'): str,
                Optional('tx'): str
            },
            Optional('rate_mode'): str,
            Optional('port_mode'): str,
            Optional('qos_scheduling'): {
                Optional('rx'): str,
                Optional('tx'): str
            },
            Optional('cos_rewrite'): str,
            Optional('tos_rewrite'): str,
            Optional('span'): str,
            Optional('udld'): str,
            Optional('mdix'): str,
            Optional('tdr_capable'): str,
            Optional('link_debounce'): str,
            Optional('link_debounce_time'): str,
            Optional('fex_fabric'): str,
            Optional('dot1q_tunnel_mode'): str,
            Optional('pvlan_trunk_capable'): str,
            Optional('port_group_members'): int,
            Optional('eee_efficient_eth'): str,
            Optional('pfc_capable'): str,
            Optional('buffer_boost_capable'): str,
            Optional('breakout_capable'): str,
            Optional('macsec_capable'): str
        }
    }


# ========================================
# Parser for 'show interface capabilities'
# ========================================

class ShowInterfaceCapabilities(ShowInterfaceCapabilitiesSchema):
    """Parser for show interface capabilities, show interface <interface> capabilities"""

    cli_command = ['show interface capabilities', 'show interface {interface} capabilities']
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

        # Match interface
        p1 = re.compile(r'^([A-Za-z0-9/]+)$')

        ## Model:     N9K-X9736C-FX
        p2 = re.compile(r'^\s*Model *: +([a-zA-Z0-9-]+)')

        # Type (SFP capable):    QSFP-H40G-AOC1M
        # Type (Non SFP):        10g
        p3 = re.compile(r'^\s*Type\s*\([Non|SFP|sfp|Sfp]+ +[SFP|sfp|Sfp|Capable|capable]*\s*\): +([a-zA-Z0-9-]+)')

        # Speed:                 100,1000,10000
        p4 = re.compile(r'^\s*Speed *: +([\d+,]+)\s*')

        # Duplex:                full
        p5 = re.compile(r'^\s*Duplex *: +(half|full)\s*')

        # Trunk encap. type:     802.1Q
        p6 = re.compile(r'^\s*Trunk +encap\. +type *: +([A-Za-z0-9.]+)\s*')

        # Channel:               yes
        p7 = re.compile(r'^\s*Channel *: +(\w+)\s*')

        # Broadcast suppression: percentage(0-100)
        p8 = re.compile(r'^\s*Broadcast +suppression *: +(?P<type>\w+)(\((?P<value>[0-9\-]+)\))?\s*')

        # Flowcontrol:           rx-(off/on),tx-(off/on)
        p9 = re.compile(r'^\s*Flowcontrol *: +(rx?-?\(?(?P<rx>[a-z/]*)\)?)?,?((tx?-?\(?(?P<tx>[a-z/]+)\)?)?)?\s*')

        # Rate mode:             dedicated
        p10 = re.compile(r'^\s*Rate mode\s*: +((?P<rate_mode>[a-zA-Z,\-]+))?')

        # Port mode:             Routed,Switched
        p11 = re.compile(r'^\s*Port mode\s*: +((?P<port_mode>[a-zA-Z,\-]+))?')

        # QOS scheduling:        rx-(8q2t),tx-(7q)
        p12 = re.compile(
            r'^\s*QOS scheduling\s*: +(rx?-?\(?(?P<rx>[a-z0-9/\-]*)\)?)?,?((tx?-?\(?(?P<tx>[a-z0-9/\-]+)\)?)?)?\s*')

        # CoS rewrite:           yes
        p13 = re.compile(r'^\s*CoS rewrite\s*: +(\w+)\s*')

        # ToS rewrite:           yes
        p14 = re.compile(r'^\s*ToS rewrite\s*: +(\w+)\s*')

        # SPAN:                  yes
        p15 = re.compile(r'^\s*SPAN\s*: +(\w+)\s*')

        # UDLD:                  yes
        p16 = re.compile(r'^\s*UDLD\s*: +(\w+)\s*')

        # MDIX:                  yes
        p17 = re.compile(r'^\s*MDIX\s*: +(\w+)\s*')

        # TDR capable:           no
        p18 = re.compile(r'^\s*TDR capable\s*: +(\w+)\s*')

        # Link Debounce:         yes
        p19 = re.compile(r'^\s*Link Debounce\s*: +(\w+)\s*')

        # Link Debounce Time:    yes
        p20 = re.compile(r'^\s*Link Debounce Time\s*: +(\w+)\s*')

        # FEX Fabric:            yes
        p21 = re.compile(r'^\s*FEX Fabric\s*: +(\w+)\s*')

        # dot1Q-tunnel mode:     yes
        p22 = re.compile(r'^\s*dot1Q-tunnel mode\s*: +(\w+)\s*')

        # Pvlan Trunk capable:   no
        p23 = re.compile(r'^\s*Pvlan Trunk capable\s*: +(\w+)\s*')

        # Port Group Members:    4
        p24 = re.compile(r'^\s*Port Group Members\s*: +(\d+)\s*')

        # EEE (efficient-eth):   no
        p25 = re.compile(r'^\s*EEE \(efficient-eth\)\s*: +(\w+)\s*')

        # PFC capable:           yes
        p26 = re.compile(r'^\s*PFC capable\s*: +(\w+)\s*')

        # Buffer Boost capable:  no
        p27 = re.compile(r'^\s*Buffer Boost capable\s*: +(\w+)\s*')

        # Breakout capable:      no
        p28 = re.compile(r'^\s*Breakout capable\s*: +(\w+)\s*')

        # MACSEC capable:        no
        p29 = re.compile(r'^\s*MACSEC capable\s*: +(\w+)\s*')

        parsed_cap_dict = {}

        rx = False
        tx = False
        for line in out.splitlines():
            line = line.replace('\t', '    ')
            line = line.strip()

            # Match Ethernet interfaces
            # Ethernet1/1 or Eth1/1 or Eth1/1/1 or Ethernet1/1/1
            m = p1.match(line)
            if m:
                interface = m.group()
                parsed_cap_dict[interface] = {}
                continue

            # Model:     N9K-X9736C-FX
            m = p2.match(line)
            if m:
                parsed_cap_dict[interface]['model'] = m.group(1)

            # Type (SFP capable):    QSFP-H40G-AOC1M
            # Type (Non SFP):        10g
            m = p3.match(line)
            if m:
                parsed_cap_dict[interface]['sfp'] = False if 'Non' in m.group() else True
                parsed_cap_dict[interface]['type'] = m.group(1)
                continue

            # Speed:                 100,1000,10000
            m = p4.match(line)
            if m:
                parsed_cap_dict[interface]['speed'] = [int(val) for val in m.group(1).split(',')]
                continue

            # Duplex:                full
            m = p5.match(line)
            if m:
                parsed_cap_dict[interface]['duplex'] = m.group(1)
                continue

            # Trunk encap. type:     802.1Q
            m = p6.match(line)
            if m:
                parsed_cap_dict[interface]['trunk_encap_type'] = m.group(1)
                continue

            # Channel:               yes
            m = p7.match(line)
            if m:
                parsed_cap_dict[interface]['channel'] = m.group(1)
                continue

            # Broadcast suppression: percentage(0-100)
            m = p8.match(line)
            if m:
                parsed_cap_dict[interface]['broadcast_suppression'] = {}
                parsed_cap_dict[interface]['broadcast_suppression']['type'] = m.group('type')
                parsed_cap_dict[interface]['broadcast_suppression']['value'] = m.group('value')
                continue

            # Flowcontrol:           rx-(off/on),tx-(off/on)
            m = p9.match(line)
            if m:
                parsed_cap_dict[interface]['flowcontrol'] = {}
                parsed_cap_dict[interface]['flowcontrol']['rx'] = m.group('rx')
                parsed_cap_dict[interface]['flowcontrol']['tx'] = m.group('tx')
                continue

            # Rate mode:             dedicated
            m = p10.match(line)
            if m:
                parsed_cap_dict[interface]['rate_mode'] = m.group('rate_mode')
                continue

            # Port mode:             Routed,Switched
            m = p11.match(line)
            if m:
                parsed_cap_dict[interface]['port_mode'] = m.group('port_mode')
                continue

            # QOS scheduling:        rx-(8q2t),tx-(7q)
            m = p12.match(line)
            if m:
                parsed_cap_dict[interface]['qos_scheduling'] = {}
                parsed_cap_dict[interface]['qos_scheduling']['rx'] = m.group('rx')
                parsed_cap_dict[interface]['qos_scheduling']['tx'] = m.group('tx')
                continue

            # CoS rewrite:           yes
            m = p13.match(line)
            if m:
                parsed_cap_dict[interface]['cos_rewrite'] = m.group(1)
                continue

            # ToS rewrite:           yes
            m = p14.match(line)
            if m:
                parsed_cap_dict[interface]['tos_rewrite'] = m.group(1)
                continue

            # SPAN:                  yes
            m = p15.match(line)
            if m:
                parsed_cap_dict[interface]['span'] = m.group(1)
                continue

            # UDLD:                  yes
            m = p16.match(line)
            if m:
                parsed_cap_dict[interface]['udld'] = m.group(1)
                continue

            # MDIX:                  yes
            m = p17.match(line)
            if m:
                parsed_cap_dict[interface]['mdix'] = m.group(1)
                continue

            # TDR capable:           no
            m = p18.match(line)
            if m:
                parsed_cap_dict[interface]['tdr_capable'] = m.group(1)
                continue

            # Link Debounce:         yes
            m = p19.match(line)
            if m:
                parsed_cap_dict[interface]['link_debounce'] = m.group(1)
                continue

            # Link Debounce Time:    yes
            m = p20.match(line)
            if m:
                parsed_cap_dict[interface]['link_debounce_time'] = m.group(1)
                continue

            # FEX Fabric:            yes
            m = p21.match(line)
            if m:
                parsed_cap_dict[interface]['fex_fabric'] = m.group(1)
                continue

            # dot1Q-tunnel mode:     yes
            m = p22.match(line)
            if m:
                parsed_cap_dict[interface]['dot1q_tunnel_mode'] = m.group(1)
                continue

            # Pvlan Trunk capable:   no
            m = p23.match(line)
            if m:
                parsed_cap_dict[interface]['pvlan_trunk_capable'] = m.group(1)
                continue

            # Port Group Members:    4
            m = p24.match(line)
            if m:
                parsed_cap_dict[interface]['port_group_members'] = int(m.group(1))
                continue

            # EEE (efficient-eth):   no
            m = p25.match(line)
            if m:
                parsed_cap_dict[interface]['eee_efficient_eth'] = m.group(1)
                continue

            # PFC capable:           yes
            m = p26.match(line)
            if m:
                parsed_cap_dict[interface]['pfc_capable'] = m.group(1)
                continue

            # Buffer Boost capable:  no
            m = p27.match(line)
            if m:
                parsed_cap_dict[interface]['buffer_boost_capable'] = m.group(1)
                continue

            # Breakout capable:      no
            m = p28.match(line)
            if m:
                parsed_cap_dict[interface]['breakout_capable'] = m.group(1)
                continue

            # MACSEC capable:        no
            m = p29.match(line)
            if m:
                parsed_cap_dict[interface]['macsec_capable'] = m.group(1)
                continue

        return parsed_cap_dict


# ========================================
# Schema for 'show interface transceiver'
# ========================================
class ShowInterfaceTransceiverSchema(MetaParser):
    """Schema for show interface transceiver"""

    schema = {
        Any(): {
            Optional('transceiver_present'): bool,
            Optional('transceiver_type'): str,
            Optional('name'): str,
            Optional('part_number'): str,
            Optional('revision'): str,
            Optional('serial_number'): str,
            Optional('nominal_bitrate'): int,
            Optional('cisco_id'): str,
            Optional('cis_part_number'): str,
            Optional('cis_product_id'): str,
            Optional('cis_version_id'): str,
            Optional('firmware_ver'): str,
            Optional('link_length'): str,
            Optional('nominal_trans_wavelength'): str,
            Optional('wavelength_tolerance'): str,
            Optional('host_lane_count'): int,
            Optional('media_lane_count'): int,
            Optional('max_mod_temp'): int,
            Optional('min_mod_temp'): int,
            Optional('min_oper_volt'): str,
            Optional('vendor_oui'): str,
            Optional('date_code'): str,
            Optional('clei'): str,
            Optional('power_class'): str,
            Optional('max_power'): float,
            Optional('near_end_lanes'): str,
            Optional('far_end_lanes'): str,
            Optional('media_interface'): str,
            Optional('advertising_code'): str,
            Optional('host_electrical_intf'): str,
            Optional('media_interface_advert_code'): str,
            Optional('cable_length'): float,
            Optional('cmis_ver'): int,
            Optional('cable_attenuation'): str
        }
    }


# ========================================
# Parser for 'show interface transceiver'
# ========================================

class ShowInterfaceTransceiver(ShowInterfaceTransceiverSchema):
    """Parser for show interface transceiver, show interface <interface> transceiver"""

    cli_command = ['show interface transceiver', 'show interface {interface} transceiver']
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

        # match interface name
        p1 = re.compile(r'^\s*(?P<intf>(Ethernet|Eth)[0-9/]+)')

        p2 = re.compile(r'^\s*transceiver\s+is\s*(not)?\s+present')

        p3 = re.compile(r'^\s*type is\s+(?P<type>[A-Za-z0-9-]+)\s*')

        p4 = re.compile(r'^\s*name is\s+(?P<name>[A-Za-z0-9-]+)\s*')

        p5 = re.compile(r'^\s*part number is\s+(?P<part_number>[A-Za-z0-9-]+)\s*')

        p6 = re.compile(r'^\s*revision is\s+(?P<rev>[A-Z0-9]+)\s*')

        p7 = re.compile(r'^\s*serial\s+number\s+is\s+(?P<sn>[A-Z0-9-]+)\s*')

        p8 = re.compile(r'^\s*nominal\s+bitrate\s+is\s+(?P<bit_rate>\d+) MBit/sec')

        p9 = re.compile(r'^\s*cisco\s+id\s+is\s+(?P<cis_id>[0-9x]+)')

        p10 = re.compile(r'^\s*cisco\s+part\s+number\s+is\s+(?P<cis_part_num>[0-9-]+)\s*')

        p11 = re.compile(r'^\s*cisco\s+product\s+id\s+is\s+(?P<prod_id>[A-Z0-9-]+)\s*')

        p12 = re.compile(r'^\s*cisco\s+version\s+id\s+is\s+(?P<ver_id>[A-Z0-9]+)\s*')

        p13 = re.compile(r'^\s*firmware\s+version\s+is\s+(?P<fw_ver>[0-9.]+)\s*')

        p14 = re.compile(r'^\s*Link\s+length\s+\w+\s+is\s+(?P<link_length>[0-9.]+\s*\w+)\s*')

        p15 = re.compile(r'^\s*Nominal\s+transmitter\s+wavelength\s+is\s+(?P<nom_tran_wl>[0-9.]+\s*\w+)\s*')

        p16 = re.compile(r'^\s*Wavelength\s+tolerance\s+is\s+(?P<wl_tol>[0-9.]+\s*\w+)\s*')

        p17 = re.compile(r'^\s*host\s+lane\s+count\s+is\s+(?P<host_lane_count>\d+)')

        p18 = re.compile(r'^\s*media\s+lane\s+count\s+is\s+(?P<media_lane_count>\d+)')

        p19 = re.compile(r'^\s*max\s+module\s+temperature\s+is\s+(?P<max_mod_temp>\d+)')

        p20 = re.compile(r'^\s*min\s+module\s+temperature\s+is\s+(?P<min_mod_temp>\d+)')

        p21 = re.compile(r'^\s*min\s+operational\s+voltage\s+is\s+(?P<min_oper_volt>[0-9.]+\s+\w+)')

        p22 = re.compile(r'^\s*vendor\s+OUI\s+is\s+(?P<oui>[a-zA-Z0-9]+)')

        p23 = re.compile(r'^\s*date\s+code\s+is\s+(?P<date_code>\d+)')

        p24 = re.compile(r'^\s*clei\s+code\s+is\s+(?P<clei>[A-Za-z0-9]+)')

        p25 = re.compile(r'^\s*power\s+class\s+is\s+(?P<power_class>[0-9a-zA-Z\(\) .]+)')

        p26 = re.compile(r'^\s*max\s+power\s+is\s+(?P<max_power>[0-9.]+)\s+W\s*')

        p27 = re.compile(r'^\s*near-end\s+lanes\s+used\s+(?P<near_end_lanes>\w+)')

        p28 = re.compile(r'^\s*far-end\s+lane\s+code\s+for\s+(?P<far_end_lanes>.*)\s*')

        p29 = re.compile(r'^\s*media\s+interface\s+is\s+(?P<media_intf>.*)\s*')

        p30 = re.compile(r'^\s*Advertising\s+code\s+is\s+(?P<adv_code>.*)\s*')

        p31 = re.compile(r'^\s*Host\s+electrical\s+interface\s+code\s+is\s+(?P<host_elec_intf>.*)\s*')

        p32 = re.compile(r'^\s*media\s+interface\s+advertising\s+code\s+is\s+(?P<media_intf_adv_code>.*)\s*')

        p33 = re.compile(r'^\s*Cable\s+Length\s+is\s+(?P<cable_len>[0-9.]+)')

        p34 = re.compile(r'^\s*CMIS\s+version\s+is\s+(?P<cmis_ver>\d+)')

        p35 = re.compile(r'^\s*cable\s+attenuation\s+is\s+(?P<cable_attenuation>.*)\s*')

        parsed_xcvr_dict = {}
        for line in out.splitlines():
            line = line.replace('\t', '    ')
            line = line.strip()

            # Match Ethernet interfaces
            # Ethernet1/1 or Eth1/1 or Eth1/1/1 or Ethernet1/1/1
            m = p1.match(line)
            if m:
                interface = m.group()
                parsed_xcvr_dict[interface] = {}
                continue

            m = p2.match(line)
            if m:
                parsed_xcvr_dict[interface]['transceiver_present'] = False if 'not' in m.group(0) else True
                continue

            m = p3.match(line)
            if m:
                parsed_xcvr_dict[interface]['transceiver_type'] = m.group('type')
                continue

            m = p4.match(line)
            if m:
                parsed_xcvr_dict[interface]['name'] = m.group('name')
                continue

            m = p5.match(line)
            if m:
                parsed_xcvr_dict[interface]['part_number'] = m.group('part_number')
                continue

            m = p6.match(line)
            if m:
                parsed_xcvr_dict[interface]['revision'] = m.group('rev')
                continue

            m = p7.match(line)
            if m:
                parsed_xcvr_dict[interface]['serial_number'] = m.group('sn')
                continue

            m = p8.match(line)
            if m:
                parsed_xcvr_dict[interface]['nominal_bitrate'] = int(m.group('bit_rate'))
                continue

            m = p9.match(line)
            if m:
                parsed_xcvr_dict[interface]['cisco_id'] = m.group('cis_id')
                continue

            m = p10.match(line)
            if m:
                parsed_xcvr_dict[interface]['cis_part_number'] = m.group('cis_part_num')
                continue

            m = p11.match(line)
            if m:
                parsed_xcvr_dict[interface]['cis_product_id'] = m.group('prod_id')
                continue

            m = p12.match(line)
            if m:
                parsed_xcvr_dict[interface]['cis_version_id'] = m.group('ver_id')
                continue

            m = p13.match(line)
            if m:
                parsed_xcvr_dict[interface]['firmware_ver'] = m.group('fw_ver')
                continue

            m = p14.match(line)
            if m:
                parsed_xcvr_dict[interface]['link_length'] = m.group('link_length')
                continue

            m = p15.match(line)
            if m:
                parsed_xcvr_dict[interface]['nominal_trans_wavelength'] = m.group('nom_tran_wl')
                continue

            m = p16.match(line)
            if m:
                parsed_xcvr_dict[interface]['wavelength_tolerance'] = m.group('wl_tol')
                continue

            m = p17.match(line)
            if m:
                parsed_xcvr_dict[interface]['host_lane_count'] = int(m.group('host_lane_count'))
                continue

            m = p18.match(line)
            if m:
                parsed_xcvr_dict[interface]['media_lane_count'] = int(m.group('media_lane_count'))
                continue

            m = p19.match(line)
            if m:
                parsed_xcvr_dict[interface]['max_mod_temp'] = int(m.group('max_mod_temp'))
                continue

            m = p20.match(line)
            if m:
                parsed_xcvr_dict[interface]['min_mod_temp'] = int(m.group('min_mod_temp'))
                continue

            m = p21.match(line)
            if m:
                parsed_xcvr_dict[interface]['min_oper_volt'] = m.group('min_oper_volt')
                continue

            m = p22.match(line)
            if m:
                parsed_xcvr_dict[interface]['vendor_oui'] = m.group('oui')
                continue

            m = p23.match(line)
            if m:
                parsed_xcvr_dict[interface]['date_code'] = m.group('date_code')
                continue

            m = p24.match(line)
            if m:
                parsed_xcvr_dict[interface]['clei'] = m.group('clei')
                continue

            m = p25.match(line)
            if m:
                parsed_xcvr_dict[interface]['power_class'] = m.group('power_class')
                continue

            m = p26.match(line)
            if m:
                parsed_xcvr_dict[interface]['max_power'] = float(m.group('max_power'))
                continue

            m = p27.match(line)
            if m:
                parsed_xcvr_dict[interface]['near_end_lanes'] = m.group('near_end_lanes')
                continue

            m = p28.match(line)
            if m:
                parsed_xcvr_dict[interface]['far_end_lanes'] = m.group('far_end_lanes')
                continue

            m = p29.match(line)
            if m:
                parsed_xcvr_dict[interface]['media_interface'] = m.group('media_intf')
                continue

            m = p30.match(line)
            if m:
                parsed_xcvr_dict[interface]['advertising_code'] = m.group('adv_code')
                continue

            m = p31.match(line)
            if m:
                parsed_xcvr_dict[interface]['host_electrical_intf'] = m.group('host_elec_intf')
                continue

            m = p32.match(line)
            if m:
                parsed_xcvr_dict[interface]['media_interface_advert_code'] = m.group('media_intf_adv_code')
                continue

            m = p33.match(line)
            if m:
                parsed_xcvr_dict[interface]['cable_length'] = float(m.group('cable_len'))
                continue

            m = p34.match(line)
            if m:
                parsed_xcvr_dict[interface]['cmis_ver'] = int(m.group('cmis_ver'))
                continue

            m = p35.match(line)
            if m:
                parsed_xcvr_dict[interface]['cable_attenuation'] = m.group('cable_attenuation')
                continue

        return parsed_xcvr_dict


# ================================================
# Schema for 'show interface transceiver details'
# ================================================
class ShowInterfaceTransceiverDetailsSchema(MetaParser):
    """Schema for show interface transceiver details"""

    schema = {
        Any(): {
            Optional('transceiver_present'): bool,
            Optional('transceiver_type'): str,
            Optional('name'): str,
            Optional('part_number'): str,
            Optional('revision'): str,
            Optional('serial_number'): str,
            Optional('nominal_bitrate'): int,
            Optional('cisco_id'): str,
            Optional('cis_part_number'): str,
            Optional('cis_product_id'): str,
            Optional('cis_version_id'): str,
            Optional('firmware_ver'): str,
            Optional('link_length'): str,
            Optional('nominal_trans_wavelength'): str,
            Optional('wavelength_tolerance'): str,
            Optional('host_lane_count'): int,
            Optional('media_lane_count'): int,
            Optional('max_mod_temp'): int,
            Optional('min_mod_temp'): int,
            Optional('min_oper_volt'): str,
            Optional('vendor_oui'): str,
            Optional('date_code'): str,
            Optional('clei'): str,
            Optional('power_class'): str,
            Optional('max_power'): float,
            Optional('near_end_lanes'): str,
            Optional('far_end_lanes'): str,
            Optional('media_interface'): str,
            Optional('advertising_code'): str,
            Optional('host_electrical_intf'): str,
            Optional('media_interface_advert_code'): str,
            Optional('cable_length'): float,
            Optional('cmis_ver'): int,
            Optional('cable_attenuation'): str,
            Optional('dom_supported'): bool,
            Optional('lane_number'): {
                Any(): {
                    Any(): {
                        Optional('current'): str,
                        Optional('high_alarm'): str,
                        Optional('high_warning'): str,
                        Optional('low_alarm'): str,
                        Optional('low_warning'): str,
                        Optional('alarm'): str
                    },
                    Optional('tx_fault_count'): int
                }
            }
        }
    }


# ================================================
# Parser for 'show interface transceiver details'
# ================================================

class ShowInterfaceTransceiverDetails(ShowInterfaceTransceiverDetailsSchema):
    """Parser for show interface transceiver details, show interface <interface> transceiver details"""

    cli_command = ['show interface transceiver details', 'show interface {interface} transceiver details']
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

        # match interface name
        p1 = re.compile(r'^\s*(?P<intf>(Ethernet|Eth)[0-9/]+)')

        p2 = re.compile(r'^\s*transceiver\s+is\s*(not)?\s+present')

        p3 = re.compile(r'^\s*type is\s+(?P<type>[A-Za-z0-9-]+)\s*')

        p4 = re.compile(r'^\s*name is\s+(?P<name>[A-Za-z0-9-]+)\s*')

        p5 = re.compile(r'^\s*part number is\s+(?P<part_number>[A-Za-z0-9-]+)\s*')

        p6 = re.compile(r'^\s*revision is\s+(?P<rev>[A-Z0-9]+)\s*')

        p7 = re.compile(r'^\s*serial\s+number\s+is\s+(?P<sn>[A-Z0-9-]+)\s*')

        p8 = re.compile(r'^\s*nominal\s+bitrate\s+is\s+(?P<bit_rate>\d+) MBit/sec')

        p9 = re.compile(r'^\s*cisco\s+id\s+is\s+(?P<cis_id>[0-9x]+)')

        p10 = re.compile(r'^\s*cisco\s+part\s+number\s+is\s+(?P<cis_part_num>[0-9-]+)\s*')

        p11 = re.compile(r'^\s*cisco\s+product\s+id\s+is\s+(?P<prod_id>[A-Z0-9-]+)\s*')

        p12 = re.compile(r'^\s*cisco\s+version\s+id\s+is\s+(?P<ver_id>[A-Z0-9]+)\s*')

        p13 = re.compile(r'^\s*firmware\s+version\s+is\s+(?P<fw_ver>[0-9.]+)\s*')

        p14 = re.compile(r'^\s*Link\s+length\s+\w+\s+is\s+(?P<link_length>[0-9.]+\s*\w+)\s*')

        p15 = re.compile(r'^\s*Nominal\s+transmitter\s+wavelength\s+is\s+(?P<nom_tran_wl>[0-9.]+\s*\w+)\s*')

        p16 = re.compile(r'^\s*Wavelength\s+tolerance\s+is\s+(?P<wl_tol>[0-9.]+\s*\w+)\s*')

        p17 = re.compile(r'^\s*host\s+lane\s+count\s+is\s+(?P<host_lane_count>\d+)')

        p18 = re.compile(r'^\s*media\s+lane\s+count\s+is\s+(?P<media_lane_count>\d+)')

        p19 = re.compile(r'^\s*max\s+module\s+temperature\s+is\s+(?P<max_mod_temp>\d+)')

        p20 = re.compile(r'^\s*min\s+module\s+temperature\s+is\s+(?P<min_mod_temp>\d+)')

        p21 = re.compile(r'^\s*min\s+operational\s+voltage\s+is\s+(?P<min_oper_volt>[0-9.]+\s+\w+)')

        p22 = re.compile(r'^\s*vendor\s+OUI\s+is\s+(?P<oui>[a-zA-Z0-9]+)')

        p23 = re.compile(r'^\s*date\s+code\s+is\s+(?P<date_code>\d+)')

        p24 = re.compile(r'^\s*clei\s+code\s+is\s+(?P<clei>[A-Za-z0-9]+)')

        p25 = re.compile(r'^\s*power\s+class\s+is\s+(?P<power_class>[0-9a-zA-Z\(\) .]+)')

        p26 = re.compile(r'^\s*max\s+power\s+is\s+(?P<max_power>[0-9.]+)\s+W\s*')

        p27 = re.compile(r'^\s*near-end\s+lanes\s+used\s+(?P<near_end_lanes>\w+)')

        p28 = re.compile(r'^\s*far-end\s+lane\s+code\s+for\s+(?P<far_end_lanes>.*)\s*')

        p29 = re.compile(r'^\s*media\s+interface\s+is\s+(?P<media_intf>.*)\s*')

        p30 = re.compile(r'^\s*Advertising\s+code\s+is\s+(?P<adv_code>.*)\s*')

        p31 = re.compile(r'^\s*Host\s+electrical\s+interface\s+code\s+is\s+(?P<host_elec_intf>.*)\s*')

        p32 = re.compile(r'^\s*media\s+interface\s+advertising\s+code\s+is\s+(?P<media_intf_adv_code>.*)\s*')

        p33 = re.compile(r'^\s*Cable\s+Length\s+is\s+(?P<cable_len>[0-9.]+)')

        p34 = re.compile(r'^\s*CMIS\s+version\s+is\s+(?P<cmis_ver>\d+)')

        p35 = re.compile(r'^\s*cable\s+attenuation\s+is\s+(?P<cable_attenuation>.*)\s*')

        p36 = re.compile(r'^\s*DOM\s+is\s+not\s+supported')

        p37 = re.compile(r'^\s*(?P<lane>Lane)\s+Number:(?P<lane_num>\d+\s+Network\s+Lane)')

        # SFP Detail Diagnostics Information
        # SFP Detail Diagnostics Information (internal calibration)
        p37_1 = re.compile(r'^SFP\s+Detail\s+Diagnostics\s+Information(\s+\(internal\s+calibration\))?$')

        p38 = re.compile(r'^\s*(?P<temp>Temperature)\s+'
                         r'(?P<curr>[0-9.NAna/-]+)\s?C?(\s+)?'
                         r'(?P<alarm>[+-]+)?\s+'
                         r'(?P<high_alarm>[0-9.NAna/-]+)\s?C?\s+'
                         r'(?P<low_alarm>[0-9.NAna/-]+)\s?C?\s+'
                         r'(?P<high_warn>[0-9.NAna/-]+)\s?C?\s+'
                         r'(?P<low_warn>[0-9.NAna/-]+)\s?C?')

        p39 = re.compile(r'^\s*(?P<voltage>Voltage)\s+'
                         r'(?P<curr>[0-9.NAna/-]+)\s?V?(\s+)?'
                         r'(?P<alarm>[+-]+)?\s+'
                         r'(?P<high_alarm>[0-9.NAna/-]+)\s?V?\s+'
                         r'(?P<low_alarm>[0-9.NAna/-]+)\s?V?\s+'
                         r'(?P<high_warn>[0-9.NAna/-]+)\s?V?\s+'
                         r'(?P<low_warn>[0-9.NAna/-]+)\s?V?')

        p40 = re.compile(r'^\s*(?P<current>Current)\s+'
                         r'(?P<curr>[0-9.NAna/-]+)\s?(mA)?(\s+)?'
                         r'(?P<alarm>[+-]+)?\s+'
                         r'(?P<high_alarm>[0-9.NAna/-]+)\s?(mA)?\s+'
                         r'(?P<low_alarm>[0-9.NAna/-]+)\s?(mA)?\s+'
                         r'(?P<high_warn>[0-9.NAna/-]+)\s?(mA)?\s+'
                         r'(?P<low_warn>[0-9.NAna/-]+)\s?(mA)?')

        p41 = re.compile(r'^\s*(?P<tx_power>Tx Power)\s+'
                         r'(?P<curr>[0-9.NAna/-]+)\s?(dBm)?(\s+)?'
                         r'(?P<alarm>[+-]+)?\s+'
                         r'(?P<high_alarm>[0-9.NAna/-]+)\s?(dBm)?\s+'
                         r'(?P<low_alarm>[0-9.NAna/-]+)\s?(dBm)?\s+'
                         r'(?P<high_warn>[0-9.NAna/-]+)\s?(dBm)?\s+'
                         r'(?P<low_warn>[0-9.NAna/-]+)\s?(dBm)?')

        p42 = re.compile(r'^\s*(?P<rx_power>Rx Power)\s+'
                         r'(?P<curr>[0-9.NAna/-]+)\s?(dBm)?(\s+)?'
                         r'(?P<alarm>[+-]+)?\s+'
                         r'(?P<high_alarm>[0-9.NAna/-]+)\s?(dBm)?\s+'
                         r'(?P<low_alarm>[0-9.NAna/-]+)\s?(dBm)?\s+'
                         r'(?P<high_warn>[0-9.NAna/-]+)\s?(dBm)?\s+'
                         r'(?P<low_warn>[0-9.NAna/-]+)\s?(dBm)?')

        p43 = re.compile(r'^\s*Transmit\s+Fault\s+Count\s+=\s+(?P<fault_count>\d+)')

        parsed_xcvr_dict = {}
        xcvr_lane = ''

        for line in out.splitlines():
            line = line.replace('\t', '    ')
            line = line.strip()

            # Match Ethernet interfaces
            # Ethernet1/1 or Eth1/1 or Eth1/1/1 or Ethernet1/1/1
            m = p1.match(line)
            if m:
                interface = m.group()
                parsed_xcvr_dict[interface] = {}
                continue

            m = p2.match(line)
            if m:
                parsed_xcvr_dict[interface]['transceiver_present'] = False if 'not' in m.group(0) else True
                continue

            m = p3.match(line)
            if m:
                parsed_xcvr_dict[interface]['transceiver_type'] = m.group('type')
                continue

            m = p4.match(line)
            if m:
                parsed_xcvr_dict[interface]['name'] = m.group('name')
                continue

            m = p5.match(line)
            if m:
                parsed_xcvr_dict[interface]['part_number'] = m.group('part_number')
                continue

            m = p6.match(line)
            if m:
                parsed_xcvr_dict[interface]['revision'] = m.group('rev')
                continue

            m = p7.match(line)
            if m:
                parsed_xcvr_dict[interface]['serial_number'] = m.group('sn')
                continue

            m = p8.match(line)
            if m:
                parsed_xcvr_dict[interface]['nominal_bitrate'] = int(m.group('bit_rate'))
                continue

            m = p9.match(line)
            if m:
                parsed_xcvr_dict[interface]['cisco_id'] = m.group('cis_id')
                continue

            m = p10.match(line)
            if m:
                parsed_xcvr_dict[interface]['cis_part_number'] = m.group('cis_part_num')
                continue

            m = p11.match(line)
            if m:
                parsed_xcvr_dict[interface]['cis_product_id'] = m.group('prod_id')
                continue

            m = p12.match(line)
            if m:
                parsed_xcvr_dict[interface]['cis_version_id'] = m.group('ver_id')
                continue

            m = p13.match(line)
            if m:
                parsed_xcvr_dict[interface]['firmware_ver'] = m.group('fw_ver')
                continue

            m = p14.match(line)
            if m:
                parsed_xcvr_dict[interface]['link_length'] = m.group('link_length')
                continue

            m = p15.match(line)
            if m:
                parsed_xcvr_dict[interface]['nominal_trans_wavelength'] = m.group('nom_tran_wl')
                continue

            m = p16.match(line)
            if m:
                parsed_xcvr_dict[interface]['wavelength_tolerance'] = m.group('wl_tol')
                continue

            m = p17.match(line)
            if m:
                parsed_xcvr_dict[interface]['host_lane_count'] = int(m.group('host_lane_count'))
                continue

            m = p18.match(line)
            if m:
                parsed_xcvr_dict[interface]['media_lane_count'] = int(m.group('media_lane_count'))
                continue

            m = p19.match(line)
            if m:
                parsed_xcvr_dict[interface]['max_mod_temp'] = int(m.group('max_mod_temp'))
                continue

            m = p20.match(line)
            if m:
                parsed_xcvr_dict[interface]['min_mod_temp'] = int(m.group('min_mod_temp'))
                continue

            m = p21.match(line)
            if m:
                parsed_xcvr_dict[interface]['min_oper_volt'] = m.group('min_oper_volt')
                continue

            m = p22.match(line)
            if m:
                parsed_xcvr_dict[interface]['vendor_oui'] = m.group('oui')
                continue

            m = p23.match(line)
            if m:
                parsed_xcvr_dict[interface]['date_code'] = m.group('date_code')
                continue

            m = p24.match(line)
            if m:
                parsed_xcvr_dict[interface]['clei'] = m.group('clei')
                continue

            m = p25.match(line)
            if m:
                parsed_xcvr_dict[interface]['power_class'] = m.group('power_class')
                continue

            m = p26.match(line)
            if m:
                parsed_xcvr_dict[interface]['max_power'] = float(m.group('max_power'))
                continue

            m = p27.match(line)
            if m:
                parsed_xcvr_dict[interface]['near_end_lanes'] = m.group('near_end_lanes')
                continue

            m = p28.match(line)
            if m:
                parsed_xcvr_dict[interface]['far_end_lanes'] = m.group('far_end_lanes')
                continue

            m = p29.match(line)
            if m:
                parsed_xcvr_dict[interface]['media_interface'] = m.group('media_intf')
                continue

            m = p30.match(line)
            if m:
                parsed_xcvr_dict[interface]['advertising_code'] = m.group('adv_code')
                continue

            m = p31.match(line)
            if m:
                parsed_xcvr_dict[interface]['host_electrical_intf'] = m.group('host_elec_intf')
                continue

            m = p32.match(line)
            if m:
                parsed_xcvr_dict[interface]['media_interface_advert_code'] = m.group('media_intf_adv_code')
                continue

            m = p33.match(line)
            if m:
                parsed_xcvr_dict[interface]['cable_length'] = float(m.group('cable_len'))
                continue

            m = p34.match(line)
            if m:
                parsed_xcvr_dict[interface]['cmis_ver'] = int(m.group('cmis_ver'))
                continue

            m = p35.match(line)
            if m:
                parsed_xcvr_dict[interface]['cable_attenuation'] = m.group('cable_attenuation')
                continue

            m = p36.match(line)
            if m:
                parsed_xcvr_dict[interface]['dom_supported'] = False
                continue

            # Lane Number:1 Network Lane
            m = p37.match(line)
            if m:
                values = m.groupdict()
                parsed_xcvr_dict[interface]['dom_supported'] = True
                xcvr_lane = values['lane_num']
                parsed_xcvr_dict[interface].setdefault('lane_number', {})
                parsed_xcvr_dict[interface]['lane_number'].setdefault(xcvr_lane, {})
                continue

            # SFP Detail Diagnostics Information
            # SFP Detail Diagnostics Information (internal calibration)
            m = p37_1.match(line)
            if m:
                if not 'lane_number' in parsed_xcvr_dict[interface]:
                    parsed_xcvr_dict[interface]['dom_supported'] = True
                    xcvr_lane = '0 SFP Detail Diagnostics Information'
                    parsed_xcvr_dict[interface].setdefault('lane_number', {})
                    parsed_xcvr_dict[interface]['lane_number'].setdefault(xcvr_lane, {})
                continue

            # Temperature   24.18 C        80.00 C     -5.00 C     75.00 C        0.00 C
            m = p38.match(line)
            if m:
                values = m.groupdict()
                parsed_xcvr_dict[interface]['lane_number'][xcvr_lane][values['temp']] = {
                    'current': values['curr'],
                    'high_alarm': values['high_alarm'],
                    'low_alarm': values['low_alarm'],
                    'high_warning': values['high_warn'],
                    'low_warning': values['low_warn'],
                    'alarm': str(values['alarm'])}

            # Voltage        3.33 V         3.63 V      2.97 V      3.46 V        3.13 V
            m = p39.match(line)
            if m:
                values = m.groupdict()
                parsed_xcvr_dict[interface]['lane_number'][xcvr_lane][values['voltage']] = {
                    'current': values['curr'],
                    'high_alarm': values['high_alarm'],
                    'low_alarm': values['low_alarm'],
                    'high_warning': values['high_warn'],
                    'low_warning': values['low_warn'],
                    'alarm': str(values['alarm'])}

            # Current           N/A       120.00 mA    20.00 mA   110.00 mA      30.00 mA
            m = p40.match(line)
            if m:
                values = m.groupdict()
                parsed_xcvr_dict[interface]['lane_number'][xcvr_lane][values['current']] = {
                    'current': values['curr'],
                    'high_alarm': values['high_alarm'],
                    'low_alarm': values['low_alarm'],
                    'high_warning': values['high_warn'],
                    'low_warning': values['low_warn'],
                    'alarm': str(values['alarm'])}

            # Tx Power          N/A         6.99 dBm   -6.90 dBm    3.99 dBm     -2.90 dBm
            m = p41.match(line)
            if m:
                values = m.groupdict()
                parsed_xcvr_dict[interface]['lane_number'][xcvr_lane][values['tx_power']] = {
                    'current': values['curr'],
                    'high_alarm': values['high_alarm'],
                    'low_alarm': values['low_alarm'],
                    'high_warning': values['high_warn'],
                    'low_warning': values['low_warn'],
                    'alarm': str(values['alarm'])}

            # Rx Power          N/A         6.99 dBm   -9.91 dBm    3.99 dBm     -5.90 dBm
            m = p42.match(line)
            if m:
                values = m.groupdict()
                parsed_xcvr_dict[interface]['lane_number'][xcvr_lane][values['rx_power']] = {
                    'current': values['curr'],
                    'high_alarm': values['high_alarm'],
                    'low_alarm': values['low_alarm'],
                    'high_warning': values['high_warn'],
                    'low_warning': values['low_warn'],
                    'alarm': str(values['alarm'])}

            # Transmit Fault Count = 0
            m = p43.match(line)
            if m:
                parsed_xcvr_dict[interface]['lane_number'][xcvr_lane]['tx_fault_count'] = int(
                    m.groupdict()['fault_count'])

        return parsed_xcvr_dict


# ========================================
# Schema for 'show interface fec'
# ========================================
class ShowInterfaceFecSchema(MetaParser):
    """Schema for show interface fec"""

    schema = {
        Any(): {
            'ifindex': str,
            'admin-fec': str,
            'oper-fec': str,
            'status': str,
            'speed': str,
            'type': str
        }
    }


# ========================================
# Parser for 'show interface fec'
# ========================================

class ShowInterfaceFec(ShowInterfaceFecSchema):
    """Parser for show interface fec """

    cli_command = 'show interface fec'

    exclude = []

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        p = re.compile(r'^\s*(?P<name>[Ethernet/0-9]+)\s+'
                       r'(?P<ifIdx>[xa-f0-9]+)\s+(?P<admin_fec>\w+)\s+'
                       r'(?P<oper_fec>\S+)\s+(?P<status>\w+)\s+'
                       r'(?P<speed>\w+|\d+)\s+(?P<type>\S+)')

        parsed_fec_dict = {}
        for line in out.splitlines():
            line = line.replace('\t', '    ')
            line = line.strip()

            m = p.match(line)
            if m:
                vdict = m.groupdict()
                parsed_fec_dict[vdict['name']] = {'ifindex': vdict['ifIdx'], 'admin-fec': vdict['admin_fec'],
                                                  'oper-fec': vdict['oper_fec'],
                                                  'status': vdict['status'], 'speed': vdict['speed'],
                                                  'type': vdict['type']}

        return parsed_fec_dict


# ========================================
# Schema for 'show interface hardware-mappings'
# ========================================
class ShowInterfaceHardwareMapSchema(MetaParser):
    """Schema for show interface hardware-mappings"""

    schema = {
        Any(): {
            'ifindex': str,
            'smod': int,
            'unit': int,
            'hport': int,
            'fport': int,
            'nport': int,
            'vport': int,
            'slice': int,
            'sport': int,
            'srcid': int,
            'macid': int,
            'macsp': int,
            'vif': int,
            'block': int,
            'blksrcid': int
        }
    }


# ========================================
# Parser for 'show interface hardware-mappings'
# ========================================

class ShowInterfaceHardwareMap(ShowInterfaceHardwareMapSchema):
    """Parser for show interface hardware-mappings """

    cli_command = 'show interface hardware-mappings'

    exclude = []

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        p = re.compile(r'^\s*(?P<name>[PoEthernet/0-9]+)\s+'
                       r'(?P<ifIdx>[xa-f0-9]+)\s+(?P<smod>\S+)\s+'
                       r'(?P<unit>\S+)\s+(?P<hport>\S+)\s+'
                       r'(?P<fport>\S+)\s+(?P<nport>\S+)\s+'
                       r'(?P<vport>\S+)\s+(?P<slice>\S+)\s+'
                       r'(?P<sport>\S+)\s+(?P<srcid>\S+)\s+'
                       r'(?P<macid>\S+)?\s+(?P<macsp>\S+)?\s+'
                       r'(?P<vif>\S+)\s+(?P<block>\S+)\s+(?P<blksrcid>\S+)\s*')
        parsed_hw_map_dict = {}

        for line in out.splitlines():
            line = line.replace('\t', '    ')
            line = line.strip()

            m = p.match(line)
            if m:
                vdict = m.groupdict()
                intf_name = interface = Common.convert_intf_name(vdict['name'])
                parsed_hw_map_dict[intf_name] = {
                    'ifindex': vdict['ifIdx'],
                    'smod': int(vdict['smod']),
                    'unit': int(vdict['unit']),
                    'hport': int(vdict['hport']),
                    'fport': int(vdict['fport']),
                    'nport': int(vdict['nport']),
                    'vport': int(vdict['vport']),
                    'slice': int(vdict['slice']),
                    'sport': int(vdict['sport']),
                    'srcid': int(vdict['srcid']),
                    'macid': int(vdict['macid']),
                    'macsp': int(vdict['macsp']),
                    'vif': int(vdict['vif']),
                    'block': int(vdict['block']),
                    'blksrcid': int(vdict['blksrcid'])}

        return parsed_hw_map_dict


#############################################################################
# Schema For show interface counters
#############################################################################
class ShowInterfaceCountersSchema(MetaParser):
    """schema for show interface counters
    """

    schema = {
        'interfaces': {
            Any(): {
                'in_octets': int,
                'in_ucast_pkts': int,
                'in_mcast_pkts': int,
                'in_bcast_pkts': int,
                'out_octets': int,
                'out_ucast_pkts': int,
                'out_mcast_pkts': int,
                'out_bcast_pkts': int,
            }
        }
    }


#############################################################################
# Parser For show interface counters
#############################################################################
class ShowInterfaceCounters(ShowInterfaceCountersSchema):
    """parser for
        * show interface counters
        * show interfaces {interfaces} counters

    """

    cli_command = ['show interface counters',
                   'show interface {interface} counters']

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

        #Port                                     InOctets                      InUcastPkts
        #Port                                  InMcastPkts                      InBcastPkts
        #Port                                    OutOctets                     OutUcastPkts
        #Port                                 OutMcastPkts                     OutBcastPkts
        p0 = re.compile(r'Port\s+(?:(?P<in_octets>InOctets)|(?P<out_octets>OutOctets)|'
                        r'(?P<in_mcast_pkts>InMcastPkts)|(?P<out_mcast_pkts>OutMcastPkts))\s+'
                        r'(?:(?P<in_ucast_pkts>InUcastPkts)|(?P<in_bcast_pkts>InBcastPkts)|'
                        r'(?P<out_ucast_pkts>OutUcastPkts)|(?P<out_bcast_pkts>OutBcastPkts))')

        #Eth1/46                                  21454282                           199828
        p1 = re.compile(r'(?P<interface>\S+)\s+(?P<val1>\d+)\s+(?P<val2>\d+)')

        for line in out.splitlines():
            line = line.rstrip()

            m = p0.match(line)
            if m:
                key1, key2 = [key for key in m.groupdict().keys() if m.groupdict()[
                    key] is not None]
                continue

            m = p1.match(line)
            if m:
                interface = Common.convert_intf_name(
                    m.groupdict()['interface'])

                intfs_dict = result_dict.setdefault('interfaces', {})
                if interface not in intfs_dict.keys():
                    intfs_dict.setdefault(interface, {})

                intfs_dict[interface][key1] = int(m.groupdict()['val1'])
                intfs_dict[interface][key2] = int(m.groupdict()['val2'])
                continue

        return result_dict
