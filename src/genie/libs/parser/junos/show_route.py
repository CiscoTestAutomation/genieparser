''' show_route.py

JUNOS parsers for the following commands:

    * show route table {table}
    * show route table {table} {prefix}

'''

import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, Use, Schema
from genie.metaparser.util.exceptions import SchemaTypeError
'''
Schema for:
    * show route table {table}
    * show route table {table} {prefix}
    * show route protocol {protocol} {ip_address}
    * show route protocol {protocol} {ip_address} | no-more
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

class ShowRouteProtocolSchema(MetaParser):
    """ Schema for:
            * show route protocol {protocol} {ip_address}
    """
    """
        schema = {
            "route-information": {
                "route-table": [
                    {
                        "active-route-count": str,
                        "destination-count": str,
                        "hidden-route-count": str,
                        "holddown-route-count": str,
                        "rt": {
                            "rt-destination": str,
                            "rt-entry": {
                                "active-tag": str,
                                "age": str,
                                "nh": {
                                    "to": str,
                                    "via": str
                                },
                                "preference": str,
                                "protocol-name": str
                            }
                        },
                        "table-name": str,
                        "total-route-count": str
                    }
                ]
            }
        }
    """
    def validate_route_table_list(value):
        # Pass route-table list of dict in value
        if not isinstance(value, list):
            raise SchemaTypeError('route-table is not a list')
        # Create RouteEntry Schema
        route_entry_schema = Schema({
                "active-route-count": str,
                "destination-count": str,
                "hidden-route-count": str,
                "holddown-route-count": str,
                Optional("rt"): {
                    "rt-destination": str,
                    "rt-entry": {
                        "active-tag": str,
                        "age": str,
                        "nh": {
                            "to": str,
                            "via": str
                        },
                        "preference": str,
                        "protocol-name": str
                    }
                },
                "table-name": str,
                "total-route-count": str
            })
        # Validate each dictionary in list
        for item in value:
            route_entry_schema.validate(item)
        return value

    # Main Schema
    schema = {
        'route-information': {
            'route-table': Use(validate_route_table_list)
        }
    }

class ShowRouteProtocol(ShowRouteProtocolSchema):
    """ Parser for:
            * show route protocol {protocol} {ip_address}
    """
    cli_command = 'show route protocol {protocol} {ip_address}'
    def cli(self, protocol, ip_address, output=None):
        if not output:
            cmd = self.cli_command.format(
                protocol=protocol,
                ip_address=ip_address)
            out = self.device.execute(cmd)
        else:
            out = output

        ret_dict = {}

        # inet.0: 932 destinations, 1618 routes (932 active, 0 holddown, 0 hidden)
        p1 = re.compile(r'^(?P<table_name>\S+): +(?P<destination_count>\d+) +'
                r'destinations, +(?P<total_route_count>\d+) +routes +'
                r'\((?P<active_route_count>\d+) +active, +(?P<holddown>\d+) +'
                r'holddown, +(?P<hidden>\d+) +hidden\)$')
        
        # 10.169.14.240/32  *[Static/5] 5w2d 15:42:25
        p2 = re.compile(r'^((?P<rt_destination>\S+) +)?(?P<active_tag>[\*\+\-])'
                r'\[(?P<protocol>Static)\/(?P<preference>\d+)\] +'
                r'(?P<text>[\S ]+)$')
        
        # >  to 10.169.14.121 via ge-0/0/1.0
        p3 = re.compile(r'^\> +to +(?P<to>\S+) +via +(?P<via>\S+)$')

        # 2001:db8:eb18:ca45::1/128
        p4 = re.compile(r'^(?P<rt_destination>[\w:\/]+)$')

        for line in out.splitlines():
            line = line.strip()

            # 10.169.14.240/32  *[Static/5] 5w2d 15:42:25
            m = p1.match(line)
            if m:
                group = m.groupdict()
                table_name = group['table_name']
                destination_count = group['destination_count']
                total_route_count = group['total_route_count']
                active_route_count = group['active_route_count']
                holddown = group['holddown']
                hidden = group['hidden']
                route_information_dict = ret_dict.setdefault('route-information', {})
                route_table_list = route_information_dict.setdefault('route-table', [])
                route_table_dict = {}
                route_table_dict.update({'active-route-count': active_route_count})
                route_table_dict.update({'destination-count': destination_count})
                route_table_dict.update({'hidden-route-count': hidden})
                route_table_dict.update({'holddown-route-count': holddown})
                route_table_dict.update({'table-name': table_name})
                route_table_dict.update({'total-route-count': total_route_count})
                route_table_list.append(route_table_dict)
                continue
            
            # 10.169.14.240/32  *[Static/5] 5w2d 15:42:25
            m = p2.match(line) 
            if m:
                group = m.groupdict()
                rt_destination = group['rt_destination']
                active_tag = group['active_tag']
                protocol = group['protocol']
                preference = group['preference']
                text = group['text']
                rt_dict = route_table_dict.setdefault('rt', {})
                if rt_destination:
                    rt_dict.update({'rt-destination': rt_destination})
                rt_entry_dict = {}
                rt_entry_dict.update({'active-tag': active_tag})
                rt_entry_dict.update({'protocol-name': protocol})
                rt_entry_dict.update({'preference': preference})
                age_dict = rt_entry_dict.setdefault('age', text)
                rt_dict.update({'rt-entry': rt_entry_dict})
                continue

            # >  to 10.169.14.121 via ge-0/0/1.0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                _to = group['to']
                via = group['via']
                nh_dict = rt_entry_dict.setdefault('nh', {})
                nh_dict.update({'to': _to})
                nh_dict.update({'via': via})
                continue
            
            # 2001:db8:eb18:ca45::1/128
            m = p4.match(line)
            if m:
                group = m.groupdict()
                rt_destination = group['rt_destination']
                rt_dict = route_table_dict.setdefault('rt', {})
                rt_dict.update({'rt-destination': rt_destination})
                continue
            
        return ret_dict

class ShowRouteProtocolNoMore(ShowRouteProtocol):
    """ Parser for:
            * show route protocol static {ip_address} | no-more
    """
    cli_command = 'show route protocol {protocol} {ip_address} | no-more'
    def cli(self, protocol, ip_address, output=None):
        if not output:
            cmd = self.cli_command.format(
                    protocol=protocol,
                    ip_address=ip_address)
            out = self.device.execute(cmd)
        else:
            out = output
        
        return super().cli(protocol=protocol,
            ip_address=ip_address, output=out)