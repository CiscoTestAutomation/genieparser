''' show_route.py

JUNOS parsers for the following commands:

    * show route table {table}
    * show route table {table} {prefix}

'''

import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional

'''
Schema for:
    * show route table {table}
    * show route table {table} {prefix}
'''
class ShowRouteTableSchema(MetaParser):

    schema = {        
        'table_name': {
            Any(): {
                'destination_count': int,
                'total_route_count': int,
                'active_route_count': int,
                'holddown_route_count': int,
                'hidden_route_count': int,
                'routes': {                            
                        Any(): {
                            'active_tag': str,
                            'protocol_name': str,
                            'preference': str,
                            Optional('preference2'): str,
                            'age': str,
                            'metric': str,
                            'next_hop': {
                                'next_hop_list': {
                                    Any(): {
                                        'to': str,
                                        'via': str,
                                        Optional('mpls_label'): str,
                                        Optional('best_route'): str
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

    cli_command = [
        'show route table {table}',
        'show route table {table} {prefix}',
    ]

    def cli(self, table, prefix=None, output=None):

        if output is None:
            if table and prefix:
                command = self.cli_command[1].format(table=table, prefix=prefix)
            else:
                command = self.cli_command[0].format(table=table)
            out = self.device.execute(command)
        else:
            out = output


        # inet.3: 3 destinations, 3 routes (3 active, 0 holddown, 0 hidden)
        r1 = re.compile(r'(?P<table_name>\S+):\s+(?P<destination_count>\d+)\s+'
                         'destinations\,\s+(?P<total_route_count>\d+)\s+routes\s+'
                         '\((?P<active_route_count>\d+)\s+active\,\s+(?P<holddown_route_count>\d+)'
                         '\s+holddown\,\s+(?P<hidden_route_count>\d+)\s+hidden\)')

        # 10.64.4.4/32         *[LDP/9] 03:40:50, metric 110
        # 10.64.4.4/32   *[L-OSPF/9/5] 1d 02:16:51, metric 110
        r2 = re.compile(r'(?P<rt_destination>\S+)\s+(?P<active_tag>\*|\-\*)'
                         '\[(?P<protocol_name>[\w\-]+)\/(?P<preference>\d+)(?:\/'
                         '(?P<preference2>\d+))?\]\s+(?P<age>[\S ]+)\,\s+'
                         'metric\s+(?P<metric>\d+)$')

        # > to 192.168.220.6 via ge-0/0/1.0
        # > to 192.168.220.6 via ge-0/0/1.0, Push 305550
        r3 = re.compile(r'(?:(?P<best_route>\>*))?\s*to\s+(?P<to>\S+)\s+via\s+'
                         '(?P<via>[\w\d\/\-\.]+)\,*\s*(?:(?P<mpls_label>\S+\s+\d+))?')

        parsed_output = {}

        for line in out.splitlines():
            line = line.strip()

            # inet.3: 3 destinations, 3 routes (3 active, 0 holddown, 0 hidden)
            result = r1.match(line)
            if result:
                group = result.groupdict()
                
                table_name = group['table_name']
                table_dict = parsed_output.setdefault('table_name', {})\
                .setdefault(table_name, {})

                table_dict['destination_count'] = int(group['destination_count'])
                table_dict['total_route_count'] = int(group['total_route_count'])
                table_dict['active_route_count'] = int(group['active_route_count'])
                table_dict['holddown_route_count'] = int(group['holddown_route_count'])
                table_dict['hidden_route_count'] = int(group['hidden_route_count'])

                continue

            # 10.64.4.4/32         *[LDP/9] 03:40:50, metric 110
            result = r2.match(line)
            if result:
                group = result.groupdict()

                rt_destination = group.pop('rt_destination', None)

                route_dict = table_dict.setdefault('routes', {})\
                                       .setdefault(rt_destination, {})

                route_dict.update({k: v for k, v in group.items() if v})
                continue

            # > to 192.168.220.6 via ge-0/0/1.0
            # > to 192.168.220.6 via ge-0/0/1.0, Push 305550
            # to 10.2.94.2 via lt-1/2/0.49
            result = r3.match(line)
            if result:

                max_index = table_dict.get('routes', {}).get(rt_destination, {})\
                                      .get('next_hop', {})\
                                      .get('next_hop_list', {}).keys()

                if not max_index:
                    max_index = 1
                else:
                    max_index = max(max_index) + 1

                group = result.groupdict()

                nh_dict = route_dict.setdefault('next_hop', {})\
                                    .setdefault('next_hop_list', {})\
                                    .setdefault(max_index, {})

                nh_dict['to'] = group['to']
                nh_dict['via'] = group['via']

                mpls_label = group['mpls_label']
                if mpls_label:
                    nh_dict['mpls_label'] = mpls_label

                best_route = group['best_route']
                if best_route:
                    nh_dict['best_route'] = best_route

                continue
        
        return parsed_output
