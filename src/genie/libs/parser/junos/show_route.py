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
            Optional("@xmlns:junos"): str,
            "route-information": {
                Optional("@xmlns"): str,
                "route-table": [
                    {
                        "active-route-count": str,
                        "destination-count": str,
                        "hidden-route-count": str,
                        "holddown-route-count": str,
                        "rt": [
                            {
                                Optional("@junos:style"): str,
                                "rt-destination": str,
                                "rt-entry": {
                                    "active-tag": str,
                                    "age": {
                                        "#text": str,
                                        Optional("@junos:seconds"): str
                                    },
                                    "current-active": str,
                                    "last-active": str,
                                    "metric": str,
                                    "nh": {
                                        "mpls-label": str,
                                        "selected-next-hop": str,
                                        "to": str,
                                        "via": str
                                    },
                                    "nh-type": str,
                                    "preference": str,
                                    "preference2": str,
                                    "protocol-name": str,
                                    "rt-tag": str
                                }
                            }
                        ],
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
        
        def validate_rt_list(value):
            # Pass rt list of dict in value
            if not isinstance(value, list):
                raise SchemaTypeError('rt list is not a list')
            
            def validate_nh_list(value):
                # Pass nh list of dict in value
                if not isinstance(value, list):
                    raise SchemaTypeError('nh list is not a list')
                # Create nh-list Entry Schema
                nh_schema = Schema({
                            Optional("mpls-label"): str,
                            Optional("selected-next-hop"): str,
                            "to": str,
                            "via": str
                        })
                # Validate each dictionary in list
                for item in value:
                    nh_schema.validate(item)
                return value

            # Create rt-list Entry Schema
            rt_schema = Schema({
                    Optional("@junos:style"): str,
                    "rt-destination": str,
                    "rt-entry": {
                        Optional("active-tag"): str,
                        "age": {
                            "#text": str,
                            Optional("@junos:seconds"): str
                        },
                        Optional("nh"): Use(validate_nh_list),
                        "preference": str,
                        "protocol-name": str,
                        Optional("metric"): str,
                        Optional('nh-type'): str,
                        Optional('rt-tag'): str,
                        Optional("current-active"): str,
                        Optional("last-active"): str,
                        Optional("preference2"): str,
                    }
                })
            # Validate each dictionary in list
            for item in value:
                rt_schema.validate(item)
            return value

        # Create RouteEntry Schema
        route_entry_schema = Schema({
                "active-route-count": str,
                "destination-count": str,
                "hidden-route-count": str,
                "holddown-route-count": str,
                Optional("rt"): Use(validate_rt_list),
                "table-name": str,
                "total-route-count": str
            })
        # Validate each dictionary in list
        for item in value:
            route_entry_schema.validate(item)
        return value

    # Main Schema
    schema = {
        Optional("@xmlns:junos"): str,
        'route-information': {
            Optional("@xmlns"): str,
            'route-table': Use(validate_route_table_list)
        }
    }

class ShowRouteProtocol(ShowRouteProtocolSchema):
    """ Parser for:
            * show route protocol {protocol} {ip_address}
            * show route protocol {protocol}
    """
    cli_command = ['show route protocol {protocol}',
                    'show route protocol {protocol} {ip_address}']
    def cli(self, protocol, ip_address=None, output=None):
        if not output:
            if ip_address:
                cmd = self.cli_command[1].format(
                    protocol=protocol,
                    ip_address=ip_address)
            else:
                cmd = self.cli_command[0].format(
                    protocol=protocol)
            out = self.device.execute(cmd)
        else:
            out = output

        ret_dict = {}
        rt_destination = None

        # inet.0: 932 destinations, 1618 routes (932 active, 0 holddown, 0 hidden)
        p1 = re.compile(r'^(?P<table_name>\S+): +(?P<destination_count>\d+) +'
                r'destinations, +(?P<total_route_count>\d+) +routes +'
                r'\((?P<active_route_count>\d+) +active, +(?P<holddown>\d+) +'
                r'holddown, +(?P<hidden>\d+) +hidden\)$')
        
        # 10.169.14.240/32  *[Static/5] 5w2d 15:42:25
        # *[OSPF3/10] 3w1d 17:03:23, metric 5
        # 0.0.0.0/0          *[OSPF/150/10] 3w3d 03:24:58, metric 101, tag 0
        p2 = re.compile(r'^((?P<rt_destination>\S+) +)?(?P<active_tag>[\*\+\-])?'
                r'\[(?P<protocol>[\w\-]+)\/(?P<preference>\d+)'
                r'(\/(?P<preference2>\d+))?\] +(?P<text>\S+ +\S+)'
                r'(, +metric +(?P<metric>\d+))?(, +tag +(?P<rt_tag>\d+))?$')

        # MultiRecv
        p2_1 = re.compile(r'^(?P<nh_type>MultiRecv)$')
        
        # >  to 10.169.14.121 via ge-0/0/1.0
        p3 = re.compile(r'^(\> +)?to +(?P<to>\S+) +via +(?P<via>\S+)(, +(?P<mpls_label>[\S\s]+))?$')

        # 2001:db8:eb18:ca45::1/128
        p4 = re.compile(r'^(?P<rt_destination>[\w:\/]+)$')

        for line in out.splitlines():
            line = line.strip()

            # inet.0: 932 destinations, 1618 routes (932 active, 0 holddown, 0 hidden)
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
            # *[OSPF3/10] 3w1d 17:03:23, metric 5
            m = p2.match(line) 
            if m:
                group = m.groupdict()
                if not rt_destination:
                    rt_destination = group['rt_destination']
                active_tag = group['active_tag']
                protocol = group['protocol']
                preference = group['preference']
                preference2 = group['preference2']
                text = group['text']
                metric = group['metric']
                rt_tag = group['rt_tag']
                rt_list = route_table_dict.setdefault('rt', [])
                rt_dict = {}
                rt_list.append(rt_dict)
                rt_entry_dict = {}
                if active_tag:
                    rt_entry_dict.update({'active-tag': active_tag})
                rt_entry_dict.update({'protocol-name': protocol})
                rt_entry_dict.update({'preference': preference})
                if preference2:
                    rt_entry_dict.update({'preference2': preference2})
                if metric:
                    rt_entry_dict.update({'metric': metric})
                if rt_tag:
                    rt_entry_dict.update({'rt-tag': rt_tag})
                age_dict = rt_entry_dict.setdefault('age', {})
                age_dict.update({'#text': text})
                rt_dict.update({'rt-entry': rt_entry_dict})
                if rt_destination:
                    rt_dict.update({'rt-destination': rt_destination})
                rt_destination = None
                continue
            
            m = p2_1.match(line)
            if m:
                group = m.groupdict()
                rt_entry_dict.update({'nh-type': group['nh_type']})
                continue

            # >  to 10.169.14.121 via ge-0/0/1.0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                # nh_dict = rt_entry_dict.setdefault('nh', {})
                nh_list = rt_entry_dict.setdefault('nh', [])
                nh_dict = {}
                nh_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                nh_list.append(nh_dict)
                continue
            
            # 2001:db8:eb18:ca45::1/128
            m = p4.match(line)
            if m:
                group = m.groupdict()
                rt_destination = group['rt_destination']
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

class ShowRouteProtocolTable(ShowRouteProtocol):
    """ Parser for:
            * show route protocol {protocol} table {table}
    """
    """
        schema = {
            Optional("@xmlns:junos"): str,
            "route-information": {
                Optional("@xmlns"): str,
                "route-table": {
                    "active-route-count": str,
                    "destination-count": str,
                    "hidden-route-count": str,
                    "holddown-route-count": str,
                    "rt": [
                        {
                            Optional("@junos:style"): str,
                            "rt-destination": str,
                            "rt-entry": {
                                "active-tag": str,
                                "age": {
                                    "#text": str,
                                    Optional("@junos:seconds"): str
                                },
                                "current-active": str,
                                "last-active": str,
                                "metric": str,
                                "nh": {
                                    "selected-next-hop": str,
                                    "to": str,
                                    "via": str
                                },
                                "nh-type": str,
                                "preference": str,
                                "preference2": str,
                                "protocol-name": str,
                                "rt-tag": str
                            }
                        }
                    ],
                    "table-name": str,
                    "total-route-count": str
                }
            }
        }
    """
    cli_command = 'show route protocol {protocol} table {table}'
    def cli(self, protocol, table, output=None):
        if not output:
            cmd = self.cli_command.format(
                    protocol=protocol,
                    table=table)
            out = self.device.execute(cmd)
        else:
            out = output
        
        return super().cli(protocol=protocol, output=out)
