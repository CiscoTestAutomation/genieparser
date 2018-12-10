''' show_archive.py

IOSXR parsers for the following show commands:
    * show arp detail
    * show arp vrf <WORD> detail
    * show arp traffic detail
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# parser utils
from genie.libs.parser.utils.common import Common

# =======================================
# Schema for 'show arp detail'
#            'show arp vrf <WORD> detail'
# =======================================
class ShowArpDetailSchema(MetaParser):
    """Schema for
            show arp detail
            show arp vrf <WORD> detail
    """

    schema = {
        'global_static_table':
            {Any():
                {'ip_address': str,
                 'mac_address': str,
                 'interface': str,
                 'encap_type': str,
                 'age': str,
                 'state': str,
                 'flag': str}
            },
        }


# =======================================
# Parser for 'show arp detail'
#            'show arp vrf <WORD> detail'
# =======================================
class ShowArpDetail(ShowArpDetailSchema):
    """Parser for:
        show arp detail
        show arp vrf <WORD> detail
        parser class - implements detail parsing mechanisms for cli,xml and yang output.
    """

    def cli(self, vrf=None):
        if vrf:
            cmd  = 'show arp vrf {vrf} detail'.format(vrf=vrf)
        else:
            cmd = 'show arp detail'

        out = self.device.execute(cmd)

        # 10.1.2.1        02:55:43   fa16.3e4c.b963  Dynamic    Dynamic ARPA GigabitEthernet0/0/0/0
        # 10.1.2.2        -          fa16.3ee4.1462  Interface  Unknown ARPA GigabitEthernet0/0/0/0
        p1 = re.compile(r'^(?P<ip_address>[\w\.]+) +(?P<age>[\w\:\-]+)'
            ' +(?P<mac_address>[\w\.]+) +(?P<state>\w+) +(?P<flag>\w+)'
            ' +(?P<encap_type>[\w\.]+) +(?P<interface>[\w\.\/]+)$')

        # initial variables
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()
            if not line: 
                continue

            m = p1.match(line)
            if m:
                groups = m.groupdict()
                address = groups['ip_address']
                final_dict = ret_dict.setdefault('global_static_table', {}).\
                  setdefault(address, {})

                final_dict.update({k: \
                    str(v) for k, v in groups.items()})

                continue

        return ret_dict

# =======================================
# Schema for 'show arp traffic detail'
# =======================================
class ShowArpTrafficDetailSchema(MetaParser):
    """ Schema for show arp traffic detail """

    schema = {
        'statistics':
            {Any():
                {'in_requests_pkts': str,
                 'in_replies_pkts': str,
                 'out_requests_pkts': str,
                 'out_replies_pkts': str,
                 'out_gratuitous_pkts': str,
                 'out_proxy': str,
                 'out_local_proxy': str,
                 'subscriber_intf_requests': str,
                 'subscriber_intf_replies': str,
                 'subscriber_intf_gratuitous': str,
                 'resolve_rcvd_requests': str,
                 'resolve_dropped_requests': str,
                 'out_of_memory_errors': str,
                 'no_buffers_errors': str,
                 'out_of_sunbet_errors': str,
            }
        },
        'cache':
            {Any():
                {'total_arp_entries': str,
                 'arp_cache_dynamic': str,
                 'arp_cache_interface': str,
                 'arp_cache_standby': str,
                 'arp_cache_alias': str,
                 'arp_cache_static': str,
                 'arp_cache_dhcp': str,
                 'arp_cache_dhcp': str,
                 'ip_packet_drop_count': str,
                 'total_arp_idb': str,
            }
        }
    }


# =======================================
# Parser for 'show arp traffic detail'
# =======================================
class ShowArpTrafficDetail(ShowArpTrafficDetailSchema):
    """ Parser for show arp traffic detail """

    def cli(self):

        out = self.device.execute('show arp traffic detail')

        # 0/0/CPU0
        p1 = re.compile(r'^(?P<rack_slot_module>[\w\/]+)$')

        # ARP statistics:
        p2 = re.compile(r'^ARP +statistics:$')

        # Recv: 108 requests, 8 replies
        p3 = re.compile(r'^Recv: +(?P<in_requests_pkts>\w+) +requests,'
            ' +(?P<in_replies_pkts>[\w]+) +replies$')

        # Sent: 8 requests, 108 replies (0 proxy, 0 local proxy, 2 gratuitous)
        p4 = re.compile(r'^Sent: +(?P<out_requests_pkts>\w+) +requests,'
            ' +(?P<out_replies_pkts>\w+) +replies +\((?P<out_proxy>\w+)'
            ' +proxy, +(?P<out_local_proxy>\w+) +local +proxy,'
            ' +(?P<out_gratuitous_pkts>\w+) +gratuitous\)$')

        # 0 requests recv, 0 replies sent, 0 gratuitous replies sent
        p5 = re.compile(r'^(?P<subscriber_intf_requests>\w+) +requests +recv,'
            ' +(?P<subscriber_intf_replies>\w+) +replies +sent,'
            ' +(?P<subscriber_intf_gratuitous>\w+) +gratuitous +replies +sent$')

        # Resolve requests rcvd: 0
        p6 = re.compile(r'^Resolve +requests +rcvd:'
            ' +(?P<resolve_rcvd_requests>\w+)$')

        # Resolve requests dropped: 0
        p7 = re.compile(r'^Resolve +requests +dropped:'
            ' +(?P<resolve_dropped_requests>\w+)$')

        # Errors: 0 out of memory, 0 no buffers, 0 out of sunbet
        p8 = re.compile(r'^Errors:'
            ' +(?P<out_of_memory_errors>\w+) +out +of +memory,'
            ' +(?P<no_buffers_errors>\w+) +no +buffers,'
            ' +(?P<out_of_sunbet_errors>\w+) +out +of +sunbet$')

        # ARP cache:
        p9 = re.compile(r'^ARP +cache:$')

        # Total ARP entries in cache: 4
        p10 = re.compile(r'^Total +ARP +entries +in +cache:'
            ' +(?P<total_arp_entries>\w+)$')

        # Dynamic: 2, Interface: 2, Standby: 0
        p11 = re.compile(r'^Dynamic: +(?P<arp_cache_dynamic>\w+),'
            ' +Interface: +(?P<arp_cache_interface>\w+),'
            ' +Standby: +(?P<arp_cache_standby>\w+)$')

        # Alias: 0,   Static: 0,    DHCP: 0
        p12 = re.compile(r'^Alias: +(?P<arp_cache_alias>\w+),'
            ' +Static: +(?P<arp_cache_static>\w+),'
            ' +DHCP: +(?P<arp_cache_dhcp>\w+)$')

        # IP Packet drop count for node 0/0/CPU0: 0
        p13 = re.compile(r'^IP +Packet +drop +count +for +node'
            ' +(?P<ip_packet_rack_slot_module>[\w\/]+):'
            ' +(?P<ip_packet_drop_count>\w+)$')

        # Total ARP-IDB:2
        p14 = re.compile(r'^Total +ARP-IDB:(?P<total_arp_idb>\w+)$')

        # initial variables
        ret_dict = {}
        rack_slot_module = ''

        for line in out.splitlines():
            line = line.strip()
            if not line: 
                continue

            m = p1.match(line)
            if m:
                groups = m.groupdict()
                rack_slot_module = groups['rack_slot_module']
                continue

            m = p2.match(line)
            if m:
                final_dict = ret_dict.setdefault('statistics', {}).setdefault(
                    rack_slot_module, {})
                continue

            m = p3.match(line)
            if m:
                groups = m.groupdict()
                final_dict.update({k: \
                    str(v) for k, v in groups.items()})
                continue

            m = p4.match(line)
            if m:
                groups = m.groupdict()
                final_dict.update({k: \
                    str(v) for k, v in groups.items()})
                continue

            m = p5.match(line)
            if m:
                groups = m.groupdict()
                final_dict.update({k: \
                    str(v) for k, v in groups.items()})
                continue

            m = p6.match(line)
            if m:
                groups = m.groupdict()
                final_dict.update({k: \
                    str(v) for k, v in groups.items()})
                continue

            m = p7.match(line)
            if m:
                groups = m.groupdict()
                final_dict.update({k: \
                    str(v) for k, v in groups.items()})
                continue

            m = p8.match(line)
            if m:
                groups = m.groupdict()
                final_dict.update({k: \
                    str(v) for k, v in groups.items()})
                continue

            m = p9.match(line)
            if m:
                final_dict = ret_dict.setdefault('cache', {}).setdefault(
                    rack_slot_module, {})
                continue

            m = p10.match(line)
            if m:
                groups = m.groupdict()
                final_dict.update({k: \
                    str(v) for k, v in groups.items()})
                continue

            m = p11.match(line)
            if m:
                groups = m.groupdict()
                final_dict.update({k: \
                    str(v) for k, v in groups.items()})
                continue

            m = p12.match(line)
            if m:
                groups = m.groupdict()
                final_dict.update({k: \
                    str(v) for k, v in groups.items()})
                continue

            m = p13.match(line)
            if m:
                groups = m.groupdict()
                final_dict['ip_packet_drop_count'] = \
                    groups['ip_packet_drop_count']
                continue

            m = p14.match(line)
            if m:
                groups = m.groupdict()
                final_dict.update({k: \
                    str(v) for k, v in groups.items()})
                continue

        return ret_dict