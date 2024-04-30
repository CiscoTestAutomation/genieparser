"""
    show_ip.py
    IOSXR parsers for the following show commands:

    * show ipv4 virtual address status

"""
import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, ListOf
from genie.libs.parser.utils.common import Common


class ShowIpv4VirtualAddressStatusSchema(MetaParser):

    schema = {
        'virtual_address': {
            'vrf_name': str,
            'virtual_ip': str,
            'active_interface_name': str,
            'active_interface_mac_address': str,
            'vrf_node_create_timestamp': str,
            'arp_add_timestamp': str,
            'rib_add_timestamp': str,
            'snmac_add_timestamp': str
        }
    }


class ShowIpv4VirtualAddressStatus(ShowIpv4VirtualAddressStatusSchema):

    cli_command = "show ipv4 virtual address status"

    def cli(self, output=None):

        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # VRF Name: default
        p0 = re.compile(r'VRF Name:\s+(?P<vrf_name>\w+)$')

        # Virtual IP: 5.2.21.22/16
        p1 = re.compile(r'Virtual IP:\s+(?P<virtual_ip>.+)$')

        # Active Interface Name: MgmtEth0/RP0/CPU0/0
        p2 = re.compile(r'Active Interface Name:\s+(?P<active_interface_name>.+)$')

        # Active Interface MAC Address: 88fc.5dc4.9d90
        p3 = re.compile(r'Active Interface MAC Address:\s+(?P<active_interface_mac>.+)$')

        # VRF Node Create Timestamp   : .7337
        p4 = re.compile(r'VRF Node Create Timestamp\s+:\s+(?P<vrf_node>.+)$')

        # ARP Add Timestamp           : Sat Jul 01 2002241054 16:32:19.1471
        p5 = re.compile(r'ARP Add Timestamp\s+:\s+(?P<arp_add_timestamp>.+)$')

        # RIB Add Timestamp           : .7337
        p6 = re.compile(r'RIB Add Timestamp\s+:\s+(?P<rib_add_timestamp>.+)$')

        # SNMAC Add Timestamp         : N/A
        p7 = re.compile(r'SNMAC Add Timestamp\s+:\s+(?P<snmac_add_timestamp>.+)$')

        for line in output.splitlines():
            line = line.strip()

            # VRF Name: default
            m = p0.match(line)
            if m:
                match_dict = m.groupdict()
                virt_dict = ret_dict.setdefault('virtual_address', {})
                virt_dict['vrf_name'] = match_dict['vrf_name']
                continue

            # Virtual IP: 5.2.21.22/16
            m = p1.match(line)
            if m:
                match_dict = m.groupdict()
                virt_dict['virtual_ip'] = match_dict['virtual_ip']
                continue

            # Active Interface Name: MgmtEth0/RP0/CPU0/0
            m = p2.match(line)
            if m:
                match_dict = m.groupdict()
                virt_dict['active_interface_name'] = match_dict['active_interface_name']
                continue

            # Active Interface MAC Address: 88fc.5dc4.9d90
            m = p3.match(line)
            if m:
                match_dict = m.groupdict()
                virt_dict['active_interface_mac_address'] = match_dict['active_interface_mac']
                continue

            # VRF Node Create Timestamp   : .7337
            m = p4.match(line)
            if m:
                match_dict = m.groupdict()
                virt_dict['vrf_node_create_timestamp'] = match_dict['vrf_node']
                continue

            # ARP Add Timestamp           : Sat Jul 01 2002241054 16:32:19.1471
            m = p5.match(line)
            if m:
                match_dict = m.groupdict()
                virt_dict['arp_add_timestamp'] = match_dict['arp_add_timestamp']
                continue

            # RIB Add Timestamp           : .7337
            m = p6.match(line)
            if m:
                match_dict = m.groupdict()
                virt_dict['rib_add_timestamp'] = match_dict['rib_add_timestamp']
                continue

            # SNMAC Add Timestamp         : N/A
            m = p7.match(line)
            if m:
                match_dict = m.groupdict()
                virt_dict['snmac_add_timestamp'] = match_dict['snmac_add_timestamp']
                continue

        return ret_dict
