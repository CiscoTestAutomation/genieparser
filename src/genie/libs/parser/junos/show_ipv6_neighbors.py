"""show_ipv6_neighbors.py

JunOS parsers for the following show commands:
    * show ipv6 neighbors
"""
# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from pyats.utils.exceptions import SchemaError
from genie.metaparser.util.schemaengine import (Any, 
        Optional, Use, Schema, ListOf)

class ShowIpv6NeighborsSchema(MetaParser):
    """ Schema for:
            * show ipv6 neighbors
    """
    """schema = {
    Optional("@xmlns:junos"): str,
    "ipv6-nd-information": {
        Optional("@junos:style"): str,
        Optional("@xmlns"): str,
        "ipv6-nd-entry": [
            {
                "ipv6-nd-expire": str,
                "ipv6-nd-interface-name": str,
                "ipv6-nd-isrouter": str,
                "ipv6-nd-issecure": str,
                "ipv6-nd-neighbor-address": str,
                "ipv6-nd-neighbor-l2-address": str,
                "ipv6-nd-state": str
            }
        ],
        "ipv6-nd-total": str
    }
}"""


    # Main Schema
    schema = {
        Optional("@xmlns:junos"): str,
        "ipv6-nd-information": {
            Optional("@junos:style"): str,
            Optional("@xmlns"): str,
            "ipv6-nd-entry": ListOf({
                "ipv6-nd-expire": str,
                "ipv6-nd-interface-name": str,
                "ipv6-nd-isrouter": str,
                "ipv6-nd-issecure": str,
                "ipv6-nd-neighbor-address": str,
                "ipv6-nd-neighbor-l2-address": str,
                "ipv6-nd-state": str
            }),
            Optional("ipv6-nd-total"): str
        }
    }

class ShowIpv6Neighbors(ShowIpv6NeighborsSchema):
    """ Parser for:
            * show ipv6 neighbors
    """
    cli_command = 'show ipv6 neighbors'
    
    def cli(self, output=None):

        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}

        #2001:db8:eb18:6337::1           00:50:56:ff:00:4b  reachable   28    yes  no      ge-0/0/1.0
        p1 = re.compile(r'^(?P<ipv6_nd_neighbor_address>[\w:]+) '
                        r'+(?P<ipv6_nd_neighbor_l2_address>[\w:]+) '
                        r'+(?P<ipv6_nd_state>\S+) +(?P<ipv6_nd_expire>\d+) '
                        r'+(?P<ipv6_nd_isrouter>\S+) +(?P<ipv6_nd_issecure>\S+) '
                        r'+(?P<ipv6_nd_interface_name>\S+)$')
        
        #Total entries: 3
        p2 = re.compile(r'^Total +entries: +(?P<ipv6_nd_total>\d+)$')

        for line in out.splitlines():
            line = line.strip()
            
            #2001:db8:eb18:6337::1           00:50:56:ff:00:4b  reachable   28    yes  no      ge-0/0/1.0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ipv6_table_entry_list = ret_dict.setdefault('ipv6-nd-information', {}). \
                    setdefault('ipv6-nd-entry', [])
                ipv6_table_entry_dict = {}
                ipv6_table_entry_dict.update({k.replace('_', '-'):
                    v for k, v in group.items() if v is not None})
                ipv6_table_entry_list.append(ipv6_table_entry_dict)
                continue

            #Total entries: 3
            m = p2.match(line)
            if m:
                group = m.groupdict()
                total_entries = group['ipv6_nd_total']
                ret_dict.setdefault('ipv6-nd-information', {}).\
                    setdefault('ipv6-nd-total', total_entries)
                continue
                
        return ret_dict

