''' show_route.py

JUNOS parsers for the following commands:

    * show route table {table}
    * show route table {table} {prefix}

'''

import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

# Libs 
from genie.libs.parser.utils.common import Common


'''
Schema for:
    * show route table {table}
    * show route table {table} {prefix}
'''
class ShowRouteTableSchema(MetaParser):

    schema = {
        'route_information': {
            'route_table': {
                'table_name': {
                    Any(): {
                        'destination_count': int,
                        'total_route_count': int,
                        'active_route_count': int,
                        'holddown_route_count': int,
                        'hidden_route_count': int,
                        'rt': {
                            'rt_destination': {
                                Any(): {
                                    'active_tag': str,
                                    'protocol_name': str,
                                    'preference': str,
                                    'age': str,
                                    'metric': str,
                                    'nh': {
                                        'to': str,
                                        'via': str,
                                        Optional('mpls_label'): str,
                                    }
                                }   
                            }
                        }
                    }
                }
            }
        }
    }

'''
Parser for:
    * show route table {table}
    * show route table {table} {prefix}
'''
class ShowRouteTable(ShowRouteTableSchema):

    cli_commands = [
        'show route table {table}',
        'show route table {table} {prefix}',
    ]

    def cli(self, table, prefix=None, output=None):

        if output is None:
            if table and prefix:
                command = self.cli_commands[1].format(table=table, prefix=prefix)
            else:
                command = self.cli_commands[0].format(table=table)
            out = self.device.execute(command)
        else:
            out = output


        # inet.3: 3 destinations, 3 routes (3 active, 0 holddown, 0 hidden)
        r1 = re.compile(r'(?P<table_name>\S+)\s+(?P<destination_count>\d+)\s+'
                         'destinations\,\s+(?P<total_route_count>\d+)\s+routes\s+'
                         '\((?P<active_route_count>\d+)\s+active\,\s+(?P<holddown_route_count>\d+)'
                         '\s+holddown\,\s+(?P<hidden_route_count>\d+)\s+hidden\)')

        # 4.4.4.4/32         *[LDP/9] 03:40:50, metric 110
        r2 = re.compile(r'(?P<rt_destination>\S+)\s+(?P<active_tag>\*|\-\*)'
                         '\[(?P<protocol_name>\S+)\/(?P<preference>\d+)\]\s+'
                         '(?P<age>\S+)\,\s+metric\s+(?P<metric>\d+)')

        # > to 200.0.0.6 via ge-0/0/1.0
        # > to 200.0.0.6 via ge-0/0/1.0, Push 305550
        r3 = re.compile(r'\>\s+to\s+(?P<to>\S+)\s+via\s+(?P<via>[\w\d\/\-\.]+)'
                         '\,*\s*(?:(?P<mpls_label>\S+\s+\d+))?')

        parsed_output = {}

        for line in out.splitlines():
            line = line.strip()

            # inet.3: 3 destinations, 3 routes (3 active, 0 holddown, 0 hidden)
            result = r1.match(line)
            if result:
                group = result.groupdict()
                
                table_name = group['table_name']
                table_dict = parsed_output.setdefault('route_information', {})\
                .setdefault('route_table', {}).setdefault('table_name', {})\
                .setdefault(table_name, {})

                table_dict['destination_count'] = int(group['destination_count'])
                table_dict['total_route_count'] = int(group['total_route_count'])
                table_dict['active_route_count'] = int(group['active_route_count'])
                table_dict['holddown_route_count'] = int(group['holddown_route_count'])
                table_dict['hidden_route_count'] = int(group['hidden_route_count'])

                continue

            # 4.4.4.4/32         *[LDP/9] 03:40:50, metric 110
            result = r2.match(line)
            if result:
                group = result.groupdict()

                rt_destination = group['rt_destination']

                route_dict = table_dict.setdefault('rt', {})\
                .setdefault('rt_destination', {})\
                .setdefault(rt_destination, {})
                
                route_dict['active_tag'] = group['active_tag']
                route_dict['protocol_name'] = group['protocol_name']
                route_dict['preference'] = group['preference']
                route_dict['age'] = group['age']
                route_dict['metric'] = group['metric']

                continue

            # > to 200.0.0.6 via ge-0/0/1.0
            # > to 200.0.0.6 via ge-0/0/1.0, Push 305550
            result = r3.match(line)
            if result:
                group = result.groupdict()
                nh_dict = route_dict.setdefault('nh', {})
                nh_dict['to'] = group['to']

                interface = group['via'].strip()
                interface = Common.convert_intf_name(intf=interface)
                nh_dict['via'] = interface

                mpls_label = group['mpls_label']
                if mpls_label:
                    nh_dict['mpls_label'] = mpls_label

                continue

        return parsed_output
