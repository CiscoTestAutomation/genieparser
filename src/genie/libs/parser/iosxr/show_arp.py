''' show_arp.py

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
        'interfaces': {
            Any(): {
                'ipv4': {
                    'neighbors': {     
                        Any(): {
                            'ip': str,
                            'link_layer_address': str,
                            'origin': str,
                            'age': str,
                            'type': str,
                        },
                    }
                }
            },
        }
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
    cli_command = ['show arp vrf {vrf} detail','show arp detail']
    def cli(self, vrf=None,output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[0].format(vrf=vrf)
            else:
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)
        else:
            out = output

        # 10.1.2.1        02:55:43   fa16.3eff.06af  Dynamic    Dynamic ARPA GigabitEthernet0/0/0/0
        # 10.1.2.2        -          fa16.3eff.f847  Interface  Unknown ARPA GigabitEthernet0/0/0/0
        # 10.1.2.3        01:42:59   0896.adff.66f2  Dynamic    Dynamic ARPA Bundle-Ether1
        p1 = re.compile(r'^(?P<ip_address>[\w\.]+) +(?P<age>[\w\:\-]+)'
            ' +(?P<mac_address>[\w\.]+) +(?P<state>\w+) +(?P<flag>\w+)'
            ' +(?P<type>[\w\.]+) +(?P<interface>[\w\.\/\-]+)$')

        # initial variables
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()
            if not line: 
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                address = group['ip_address']
                interface = group['interface']
                final_dict = ret_dict.setdefault('interfaces', {}).setdefault(
                    interface, {}).setdefault('ipv4', {}).setdefault(
                    'neighbors', {}).setdefault(address, {})
                
                final_dict['ip'] = address
                final_dict['link_layer_address'] = group['mac_address']
                final_dict['age'] = group['age']
                if group['age'] == '-':
                    final_dict['origin'] = 'static'
                else:
                    final_dict['origin'] = 'dynamic'

                final_dict['type'] = group['type']
                continue

        return ret_dict

# =======================================
# Schema for 'show arp traffic detail'
# =======================================
class ShowArpTrafficDetailSchema(MetaParser):
    """ Schema for show arp traffic detail """

    schema = {
        Any():
            {'statistics':
                {'in_requests_pkts': int,
                 'in_replies_pkts': int,
                 'out_requests_pkts': int,
                 'out_replies_pkts': int,
                 'out_gratuitous_pkts': int,
                 'out_proxy': int,
                 'out_local_proxy': int,
                 'subscriber_intf_requests': int,
                 'subscriber_intf_replies': int,
                 'subscriber_intf_gratuitous': int,
                 'resolve_rcvd_requests': int,
                 'resolve_dropped_requests': int,
                 'out_of_memory_errors': int,
                 'no_buffers_errors': int,
                 'out_of_subnet_errors': int,
                 Optional('unsolicited'): int,
                },
            'cache':
                {'total_arp_entries': int,
                 'dynamic': int,
                 'interface': int,
                 'standby': int,
                 'alias': int,
                 'static': int,
                 'dhcp': int,
                 Optional('drop_adj'): int,
                 'ip_packet_drop_count': int,
                 'total_arp_idb': int,
                }
            }
        }


# =======================================
# Parser for 'show arp traffic detail'
# =======================================
class ShowArpTrafficDetail(ShowArpTrafficDetailSchema):
    """ Parser for show arp traffic detail """

    cli_command = 'show arp traffic detail'
    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # 0/0/CPU0
        p1 = re.compile(r'^(?P<rack_slot_module>[\w\/]+)$')

        # ARP statistics:
        p2 = re.compile(r'^ARP +statistics:$')

        # Recv: 108 requests, 8 replies
        p3 = re.compile(r'^Recv: +(?P<in_requests_pkts>\w+) +requests, '
            '+(?P<in_replies_pkts>[\w]+) +replies( '
            '+\((?P<unsolicited>\w+) +unsolicited\))*')

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

        # Errors: 0 out of memory, 0 no buffers, 0 out of subnet
        p8 = re.compile(r'^Errors:'
            ' +(?P<out_of_memory_errors>\w+) +out +of +memory,'
            ' +(?P<no_buffers_errors>\w+) +no +buffers,'
            ' +(?P<out_of_subnet_errors>\w+) +out +of +(subnet|sunbet)$')

        # ARP cache:
        p9 = re.compile(r'^ARP +cache:$')

        # Total ARP entries in cache: 4
        p10 = re.compile(r'^Total +ARP +entries +in +cache:'
            ' +(?P<total_arp_entries>\w+)$')

        # Dynamic: 2, Interface: 2, Standby: 0
        p11 = re.compile(r'^Dynamic: +(?P<dynamic>\w+),'
            ' +Interface: +(?P<interface>\w+),'
            ' +Standby: +(?P<standby>\w+)$')

        # Alias: 0,   Static: 0,    DHCP: 0
        # Alias: 0,   Static: 0,    DHCP: 0,    DropAdj: 0
        p12 = re.compile(r'^Alias: +(?P<alias>\w+),'
            ' +Static: +(?P<static>\w+),'
            ' +DHCP: +(?P<dhcp>\w+)'
            '(, +DropAdj: +(?P<drop_adj>\d+))?$')

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
                final_dict = ret_dict.setdefault(
                    rack_slot_module, {}).setdefault('statistics', {})
                continue

            m = p3.match(line)
            if m:
                groups = m.groupdict()
                final_dict.update({k: \
                    int(v) for k, v in groups.items() if isinstance(groups[k], str)})
                continue

            m = p4.match(line)
            if m:
                groups = m.groupdict()
                final_dict.update({k: \
                    int(v) for k, v in groups.items()})
                continue

            m = p5.match(line)
            if m:
                groups = m.groupdict()
                final_dict.update({k: \
                    int(v) for k, v in groups.items()})
                continue

            m = p6.match(line)
            if m:
                groups = m.groupdict()
                final_dict.update({k: \
                    int(v) for k, v in groups.items()})
                continue

            m = p7.match(line)
            if m:
                groups = m.groupdict()
                final_dict.update({k: \
                    int(v) for k, v in groups.items()})
                continue

            m = p8.match(line)
            if m:
                groups = m.groupdict()
                final_dict.update({k: \
                    int(v) for k, v in groups.items()})
                continue

            m = p9.match(line)
            if m:
                final_dict = ret_dict[rack_slot_module].setdefault('cache', {})
                continue

            m = p10.match(line)
            if m:
                groups = m.groupdict()
                final_dict.update({k: \
                    int(v) for k, v in groups.items()})
                continue

            m = p11.match(line)
            if m:
                groups = m.groupdict()
                final_dict.update({k: \
                    int(v) for k, v in groups.items()})
                continue

            m = p12.match(line)
            if m:
                groups = m.groupdict()
                final_dict.update({k: \
                    int(v) for k, v in groups.items() if v is not None})
                continue

            m = p13.match(line)
            if m:
                groups = m.groupdict()
                final_dict['ip_packet_drop_count'] = \
                    int(groups['ip_packet_drop_count'])
                continue

            m = p14.match(line)
            if m:
                groups = m.groupdict()
                final_dict.update({k: \
                    int(v) for k, v in groups.items()})
                continue

        return ret_dict