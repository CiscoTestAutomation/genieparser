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
# Parser for 'show arp traffic detail'
# =======================================
class ShowArpTrafficDetail(ShowArpTrafficDetailSchema):
    """ Parser for show arp traffic detail """

    def cli(self):

        out = self.device.execute('show arp traffic detail')

        # -------------------------------------------------------------------------------
        # 0/0/CPU0
        # -------------------------------------------------------------------------------

        # ARP statistics:
        #   Recv: 108 requests, 8 replies
        #   Sent: 8 requests, 108 replies (0 proxy, 0 local proxy, 2 gratuitous)
        #   Subscriber Interface: 
        #          0 requests recv, 0 replies sent, 0 gratuitous replies sent
        #   Resolve requests rcvd: 0
        #   Resolve requests dropped: 0
        #   Errors: 0 out of memory, 0 no buffers, 0 out of sunbet

        # ARP cache:
        #   Total ARP entries in cache: 4
        #   Dynamic: 2, Interface: 2, Standby: 0
        #   Alias: 0,   Static: 0,    DHCP: 0

        #   IP Packet drop count for node 0/0/CPU0: 0

        #   Total ARP-IDB:2

        # 0/0/CPU0
        p1 = re.compile(r'^(?P<rack>[\w\.]+)\/(?P<slot>[\w\:\-]+)\/'
            '(?P<module>\w+)$')

        # ARP statistics:
        p2 = re.compile(r'^ARP +statistics:$')

        # ARP cache:
        p3 = re.compile(r'^ARP +cache:$')

        # Recv: 108 requests, 8 replies
        p4 = re.compile(r'^Recv: +(?P<rcvd_requests>[\w]+) +requests,'
            ' +(?P<rcvd_replies>[\w]+) +replies$')

        # Sent: 8 requests, 108 replies (0 proxy, 0 local proxy, 2 gratuitous)
        p5 = re.compile(r'^Sent: +(?P<sent_requests>[\w]+) +requests,'
            ' +(?P<sent_replies>[\w]+) +replies +\((?P<sent_proxy>[\w]+)'
            ' +proxy, +(?P<sent_local_proxy>[\w]+) +local +proxy,'
            ' +(?P<sent_gratuitous>[\w]+) +gratuitous\)$')

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