''' show_l2fib.py

IOSXE parsers for the following show commands:

    * show l2fib path-list {id}
    * show l2fib path-list detail
    * show l2fib bridge-domain {bd_id} port

Copyright (c) 2021 by Cisco Systems, Inc.
All rights reserved.
'''

import re


# genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, ListOf, Optional


# ====================================================
# Schema for 'show l2fib path-list <id>'
# ====================================================
class ShowL2fibPathListIdSchema(MetaParser):
    """ Schema for show l2fib path-list {id}
                   show l2fib path-list detail
    """

    schema = {
        'path_ids': {
            Any(): {
               'type': str,
               'eth_seg': str,
               'path_cnt': int,
               'path_list': ListOf(
                    {
                      'path': str
                    }
                )
            }
        }
    }


# =============================================
# Parser for 'show l2fib path-list <id>'
# =============================================
class ShowL2fibPathListId(ShowL2fibPathListIdSchema):
    """ Parser for show l2fib path-list {id}
                   show l2fib path-list detail
    """

    cli_command = [
            'show l2fib path-list {id}',
            'show l2fib path-list detail'
    ]

    def cli(self, id=None, output=None):

        if output is None:
            if id:
                cli_cmd = self.device.execute(self.cli_command[0].format(id=id))
            else:
                cli_cmd = self.device.execute(self.cli_command[1])

            cli_output = self.device.execute(cli_cmd)
        else:
            cli_output = output

        # PathList ID                   : 28
        p1 = re.compile(r'^PathList ID\s+:\s+(?P<path_list_id>\d+)$')

        # PathList Type                 : MPLS_UC
        p2 = re.compile(r'^PathList Type\s+:\s+(?P<type>\w+)$')

        # Ethernet Segment              : 0000.0000.0000.0000.0000
        p3 = re.compile(r'^Ethernet Segment\s+:\s+'
                        r'(?P<eth_seg>[0-9a-fA-F\.]+)$')

        # Path Count                    : 1
        p4 = re.compile(r'^Path Count\s+:\s+(?P<path_cnt>\d+)$')

        # Paths                         : [MAC]16@2.2.2.1
        p5 = re.compile(r'^[Paths]*\s*:\s+(?P<path>\[\w+\]\d+'
                        r'[0-9a-fA-F\.:@ ]+)$')

        parser_dict = {}

        for line in cli_output.splitlines():
            line = line.strip()
            if not line:
                continue

            # PathList ID                   : 28
            m = p1.match(line)
            if m:
                group = m.groupdict()
                path_ids = parser_dict.setdefault('path_ids', {})
                path_list = path_ids.setdefault(int(group['path_list_id']), {})
                paths = path_list.setdefault('path_list', [])
                continue

            # PathList Type                 : MPLS_UC
            m = p2.match(line)
            if m:
                group = m.groupdict()
                path_list.update({'type': group['type']})
                continue

            # Ethernet Segment              : 0000.0000.0000.0000.0000
            m = p3.match(line)
            if m:
                group = m.groupdict()
                path_list.update({'eth_seg': group['eth_seg']})
                continue

            # Path Count                    : 1
            m = p4.match(line)
            if m:
                group = m.groupdict()
                path_list.update({'path_cnt': int(group['path_cnt'])})
                continue

            # Paths                         : [MAC]16@2.2.2.1
            m = p5.match(line)
            if m:
                group = m.groupdict()
                path = group['path']
                paths_dict = {}
                paths_dict.update({'path': path})
                paths.append(paths_dict)
                continue

        return parser_dict

# ====================================================
# Schema for 'show l2fib bridge-domain {bd_id} port'
# ====================================================
class ShowL2fibBdPortSchema(MetaParser):
    """ Schema for show l2fib bridge-domain {bd-id} port """

    schema = {
        Any(): {
            'type': str,
            'is_path_list': bool,
            Optional('port'): str,
            Optional('path_list'): {
                'id': int,
                'path_count': int,
                'type': str,
                'description': str
            }
        }
    }

# ==================================================
# Parser for 'show l2fib bridge-domain <bd_id> port'
# ==================================================
class ShowL2fibBdPort(ShowL2fibBdPortSchema):
    """ Parser for show l2fib bridge-domain {bd_id} port """

    cli_command = [ 'show l2fib bridge-domain {bd_id} port']

    def cli(self, output=None, bd_id=None):
        if output is None:
            cli_output = self.device.execute(self.cli_command[0].format(bd_id=bd_id))
        else:
            cli_output = output

        #BD_PORT   Et0/2:12
        p1 = re.compile(r'^(?P<port_type>BD_PORT)\s+(?P<interface>[\w:\/]+)$')

        #VXLAN_REP PL:1191(1) T:VXLAN_REP [IR]20012:2.2.2.2
        p2 = re.compile(r'^(?P<type>\w+)\s+PL:(?P<path_list_id>\d+)\((?P<path_list_count>\d+)\)'
                        r'\s+T:(?P<path_list_type>\w+)\s+(?P<path_list_desc>\[\w+\][0-9a-fA-F:@\.]+)$')

        parser_dict = {}

        for line in cli_output.splitlines():
            line = line.strip()
            if not line:
                continue

            #BD_PORT   Et0/2:12
            m = p1.match(line)
            if m:
                group = m.groupdict()
                port_type = group['port_type']
                interface_id = group['interface']
                parser_dict.update({
                    interface_id: {
                        'type': port_type,
                        'is_path_list': False,
                        'port': interface_id
                    }
                })
                continue

            #VXLAN_REP PL:1191(1) T:VXLAN_REP [IR]20012:2.2.2.2
            m = p2.match(line)
            if m:
                group = m.groupdict()
                parser_dict.update({
                    group['path_list_desc']: {
                        'type': group['type'],
                        'is_path_list': True,
                        'path_list': {
                            'id': int(group['path_list_id']),
                            'path_count': int(group['path_list_count']),
                            'type': group['path_list_type'],
                            'description': group['path_list_desc']
                        }
                    }
                })
                continue
        return parser_dict