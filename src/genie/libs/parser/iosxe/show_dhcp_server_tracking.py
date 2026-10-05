'''show_dhcp_server_tracking.py

IOSXE parsers for the following show commands:

    * 'show dhcp-server-tracking database'
    * 'show dhcp-server-tracking database vlan {vlan_id}'
    * 'show dhcp-server-tracking database detail'
    * 'show dhcp-server-tracking database vlan {vlan_id} detail'
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional


# ====================================
# Schema for:
#  * 'show dhcp-server-tracking database'
# ====================================
class ShowDhcpServerTrackingDatabaseSchema(MetaParser):
    """Schema for show dhcp-server-tracking database"""

    schema = {
        "dhcp_server_database_count": int,
        Optional('entries'): {
            int: {
                "link_layer_address": str,
                "vlan_id": int,
                "network_layer_address": str,
            }
        }
    }


# ====================================
# Parser for:
#  * 'show dhcp-server-tracking database'
# ====================================
class ShowDhcpServerTrackingDatabase(ShowDhcpServerTrackingDatabaseSchema):
    """Parser for show dhcp-server-tracking database"""

    cli_command = ['show dhcp-server-tracking database',
                   'show dhcp-server-tracking database vlan {vlan_id}']

    def cli(self, vlan_id=None, output=None):
        if output is None:
            if vlan_id:
                out = self.device.execute(self.cli_command[1].format(vlan_id=vlan_id))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # DHCP Server Tracking Database contains 1 entries
        #
        # MAC Address          VLAN  IP Address
        # dead.beef.0008       20    3002::3002

        dhcp_server_tracking_database_dict = {}

        # DHCP Server Tracking Database contains 1 entries
        table_info_capture = re.compile(r'^\s*DHCP +Server +Tracking +Database +contains +(?P<entries>\d+) +entries$')

        # dead.beef.0008       20    3002::3002
        entry_capture = re.compile(
            r"^(?P<link_layer_address>\S+)"
            r"\s+(?P<vlan_id>\d+)"
            r"\s+(?P<network_layer_address>\S+)$"
        )

        entry_num = 0
        for line in out.splitlines():
            line = line.strip()

            # DHCP Server Tracking Database contains 1 entries
            match = table_info_capture.match(line)
            if match:
                groups = match.groupdict()
                entries = int(groups['entries'])
                dhcp_server_tracking_database_dict['dhcp_server_database_count'] = entries
                continue

            # dead.beef.0008       20    3002::3002
            match = entry_capture.match(line)
            if match:
                entry_num += 1
                groups = match.groupdict()

                lla = groups['link_layer_address']
                vlan = int(groups['vlan_id'])
                ip = groups['network_layer_address']

                index_dict = dhcp_server_tracking_database_dict.setdefault('entries', {}).setdefault(entry_num, {})
                index_dict['link_layer_address'] = lla
                index_dict['vlan_id'] = vlan
                index_dict['network_layer_address'] = ip
                continue

        return dhcp_server_tracking_database_dict


# ====================================
# Schema for:
#  * 'show dhcp-server-tracking database detail'
# ====================================
class ShowDhcpServerTrackingDatabaseDetailSchema(MetaParser):
    '''Schema for:
        * 'show dhcp-server-tracking database detail'
    '''

    schema = {
        "dhcp_server_database_count": int,
        Optional('entries'): {
            int: {
                "link_layer_address": str,
                "vlan_id": int,
                "network_layer_address": str,
                "duid_length": int,
                "duid": str,
                "interface": str,
                "last_pkt_recv": str,
                "reply_count": int,
                "last_reply_recv": str,
                "last_addr_allocated": str,
                "preferred_lifetime": str,
                "valid_lifetime": str,
            }
        }
    }


# ====================================
# Parser for:
#  * 'show dhcp-server-tracking database detail'
# ====================================
class ShowDhcpServerTrackingDatabaseDetail(ShowDhcpServerTrackingDatabaseDetailSchema):
    """Parser for show dhcp-server-tracking database detail"""

    cli_command = ['show dhcp-server-tracking database detail',
                   'show dhcp-server-tracking database vlan {vlan_id} detail']

    def cli(self, vlan_id=None, output=None):
        if output is None:
            if vlan_id:
                out = self.device.execute(self.cli_command[1].format(vlan_id=vlan_id))
            else:
                out = self.device.execute(self.cli_command[0])
        else:
            out = output

        # DHCP Server Tracking Database contains 1 entries
        #
        # DHCP Server MAC: dead.beef.0008, VLAN 20
        #   Address: 3002::30
        #   DUID length: 1
        #   DUID: 10
        #   Interface: Twe1/0/1
        #   Last packet received: 6s ago
        #   Received 1 replies, last reply: 6s ago
        #   Last address assigned: 2001:DB8::105
        #   Last address preferred lifetime: 60s, valid lifetime: 60s

        dhcp_server_tracking_database_detail_dict = {}

        # DHCP Server Tracking Database contains 1 entries
        table_info_capture = re.compile(r'^\s*DHCP +Server +Tracking +Database +contains +(?P<entries>\d+) +entries$')

        # DHCP Server MAC: dead.beef.0008, VLAN 20
        p1 = re.compile(r"^DHCP +Server +MAC: +(?P<link_layer_address>\S+), +VLAN +(?P<vlan_id>\d+)$")

        # Address: 3002::30
        p2 = re.compile(r"^Address: +(?P<network_layer_address>\S+)$")

        # DUID length: 1
        p3 = re.compile(r"^DUID +length: +(?P<duid_length>\d+)$")

        # DUID: 10
        p4 = re.compile(r"^DUID: +(?P<duid>\S+)$")

        # Interface: Twe1/0/1
        p5 = re.compile(r"^Interface: +(?P<interface>\S+)$")

        # Last packet received: 6s ago
        p6 = re.compile(r"^Last +packet +received: +(?P<last_pkt_recv>[\d\w\s]+) +ago$")

        # Received 1 replies, last reply: 6s ago
        # Received 0 replies, last reply: n/a
        # Received 1 replies, last reply: 1m 1s ago
        p7 = re.compile(r"^Received +(?P<reply_count>\d+) +replies, +last +reply: +(?P<last_reply_recv>.+?)(?: +ago)?$")

        # Last address assigned: 2001:DB8::105
        p8 = re.compile(r"^Last +address +assigned: +(?P<last_addr_allocated>\S+)$")

        # Last address preferred lifetime: 60s, valid lifetime: 60s
        p9 = re.compile(r"^Last +address +preferred +lifetime: +(?P<preferred_lifetime>\S+), +valid +lifetime: +(?P<valid_lifetime>\S+)$")

        entry_num = 0
        for line in out.splitlines():
            line = line.strip()

            # DHCP Server Tracking Database contains 1 entries
            match = table_info_capture.match(line)
            if match:
                groups = match.groupdict()
                entries = int(groups['entries'])
                dhcp_server_tracking_database_detail_dict['dhcp_server_database_count'] = entries
                continue

            # DHCP Server MAC: dead.beef.0008, VLAN 20
            match = p1.match(line)
            if match:
                entry_num += 1
                groups = match.groupdict()
                index_dict = dhcp_server_tracking_database_detail_dict.setdefault('entries', {}).setdefault(entry_num, {})
                index_dict['link_layer_address'] = groups['link_layer_address']
                index_dict['vlan_id'] = int(groups['vlan_id'])
                continue

            # Address: 3002::30
            match = p2.match(line)
            if match:
                index_dict['network_layer_address'] = match.group('network_layer_address')
                continue

            # DUID length: 1
            match = p3.match(line)
            if match:
                index_dict['duid_length'] = int(match.group('duid_length'))
                continue

            # DUID: 10
            match = p4.match(line)
            if match:
                index_dict['duid'] = match.group('duid')
                continue

            # Interface: Twe1/0/1
            match = p5.match(line)
            if match:
                index_dict['interface'] = match.group('interface')
                continue

            # Last packet received: 6s ago
            match = p6.match(line)
            if match:
                index_dict['last_pkt_recv'] = match.group('last_pkt_recv')
                continue

            # Received 1 replies, last reply: 6s ago
            match = p7.match(line)
            if match:
                groups = match.groupdict()
                index_dict['reply_count'] = int(groups['reply_count'])
                index_dict['last_reply_recv'] = groups['last_reply_recv']
                continue

            # Last address assigned: 2001:DB8::105
            match = p8.match(line)
            if match:
                index_dict['last_addr_allocated'] = match.group('last_addr_allocated')
                continue

            # Last address preferred lifetime: 60s, valid lifetime: 60s
            match = p9.match(line)
            if match:
                groups = match.groupdict()
                index_dict['preferred_lifetime'] = groups['preferred_lifetime']
                index_dict['valid_lifetime'] = groups['valid_lifetime']
                continue

        return dhcp_server_tracking_database_detail_dict
