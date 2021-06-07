"""
    show_interface.py
    IOS parsers for the following show commands:

    * show interfaces
    * show ip interface brief
    * show ip interface brief | include Vlan
    * show ip interface brief | include <WROD>
    * show ip interface
    * show ipv6 interface
    * show interfaces accounting
    * show interfaces status
    * show interfaces transciever
    * show interfaces {interface} transceiver
    * show interfaces transceiver detail
    * show interfaces {interface} transceiver detail

    # TODO: Need find replacement command for IOSXE 'show interface <intf> counters'
"""

# python
import re

# genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
    Any, Optional

# import iosxe parser
from genie.libs.parser.iosxe.show_interface import \
    ShowInterfaces as ShowInterfaces_iosxe, \
    ShowIpInterfaceBrief as ShowIpInterfaceBrief_iosxe, \
    ShowIpInterfaceBriefPipeVlan as ShowIpInterfaceBriefPipeVlan_iosxe, \
    ShowIpInterfaceBriefPipeIp as ShowIpInterfaceBriefPipeIp_iosxe, \
    ShowIpInterface as ShowIpInterface_iosxe, \
    ShowIpv6Interface as ShowIpv6Interface_iosxe, \
    ShowInterfacesAccounting as ShowInterfacesAccounting_iosxe, \
    ShowInterfacesCounters as ShowInterfacesCounters_iosxe, \
    ShowInterfacesSwitchport as ShowInterfacesSwitchport_iosxe, \
    ShowInterfacesTrunk as ShowInterfacesTrunk_iosxe, \
    ShowInterfacesStats as ShowInterfacesStats_iosxe, \
    ShowInterfacesDescription as ShowInterfacesDescription_iosxe, \
    ShowInterfacesStatus as ShowInterfacesStatus_iosxe, \
    ShowInterfacesTransceiver as ShowInterfacesTransceiver_iosxe, \
    ShowInterfacesTransceiverDetail as ShowInterfacesTransceiverDetail_iosxe

# import parser utils
from genie.libs.parser.utils.common import Common


class ShowInterfaces(ShowInterfaces_iosxe):
    """parser for show interfaces"""
    exclude = ['in_octets', 'in_pkts', 'out_octets', 'out_pkts',
               'in_rate', 'in_rate_pkts', 'out_rate', 'out_rate_pkts',
               'input_queue_size', 'in_broadcast_pkts', 'in_multicast_pkts',
               'last_output', 'out_unknown_protocl_drops', 'last_input',
               'input_queue_drops', 'out_interface_resets',
               'rxload', 'txload', 'last_clear', 'in_crc_errors',
               'in_errors', 'in_giants', 'unnumbered', 'mac_address',
               'phys_address', 'out_lost_carrier', '(Tunnel.*)',
               'input_queue_flushes', 'reliability', 'in_runts']

    pass


class ShowIpInterfaceBrief(ShowIpInterfaceBrief_iosxe):
    """Parser for: show ip interface brief"""
    exclude = ['method', '(Tunnel.*)']
    pass


class ShowIpInterfaceBriefPipeVlan(ShowIpInterfaceBriefPipeVlan_iosxe):
    """Parser for: show ip interface brief | include Vlan"""
    pass


class ShowIpInterfaceBriefPipeIp(ShowIpInterfaceBriefPipeIp_iosxe):
    """Parser for:  show ip interface brief | include <WORD>"""
    pass


class ShowIpInterface(ShowIpInterface_iosxe):
    """Parser for show ip interface"""
    exclude = ['unnumbered', 'address_determined_by',
               '(Tunnel.*)', 'joins', 'leaves']
    pass


class ShowIpv6Interface(ShowIpv6Interface_iosxe):
    """Parser for show ipv6 interface"""
    exclude = ['unnumbered', 'interface_ref',
               '(Tunnel.*)', 'joined_group_addresses', 'ipv6']
    pass


class ShowInterfacesAccounting(ShowInterfacesAccounting_iosxe):
    """Parser for:
        show interfaces accounting
        show interfaces <interface> accounting
    """
    exclude = ['pkts_in', 'pkts_out', 'chars_in', 'chars_out']
    pass


class ShowInterfacesCounters(ShowInterfacesCounters_iosxe):
    """Parser for show interfaces <interface> counters"""
    pass


class ShowInterfacesSwitchport(ShowInterfacesSwitchport_iosxe):
    """Parser for show interfaces switchport"""
    pass


class ShowInterfacesTrunk(ShowInterfacesTrunk_iosxe):
    """Parser for show interfaces trunk"""
    pass


class ShowInterfacesStats(ShowInterfacesStats_iosxe):
    """Parser for:
        show interfaces <interface> stats
        show interfaces stats"""
    pass


class ShowInterfacesDescription(ShowInterfacesDescription_iosxe):
    """Parser for:
        show interfaces <interface> description
        show interfaces description"""
    pass


class ShowInterfacesStatus(ShowInterfacesStatus_iosxe):
    """Parser for:
        show interfaces status"""
    pass


class ShowInterfacesTransceiverDetail(ShowInterfacesTransceiverDetail_iosxe):
    """
    Parser for:
        * show interfaces transceiver detail
        * show interfaces <interface> transceiver detail
    """
    pass


class ShowInterfacesTransceiver(ShowInterfacesTransceiver_iosxe):
    """
    Parser for:
        * show interfaces transciever
        * show interfaces <interface> transceiver
    """
    pass
