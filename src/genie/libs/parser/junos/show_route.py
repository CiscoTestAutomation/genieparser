''' show_route.py

JUNOS parsers for the following commands:

    * show route table {table}
    * show route table {table} {prefix}
    * show route protocol {protocol} extensive
    * show route protocol {protocol} table {table} extensive
    * show route protocol {protocol} table {table}
    * show route protocol {protocol}
    * show route protocol {protocol} {ip_address}
    * 'show route protocol {protocol} table {table} extensive {destination}'
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
            * show route protocol {protocol} table {table}
    """
    cli_command = ['show route protocol {protocol}',
                    'show route protocol {protocol} {ip_address}',
                    'show route protocol {protocol} table {table}']

    def cli(self, protocol, ip_address=None, table=None, output=None):
        if not output:
            if ip_address:
                cmd = self.cli_command[1].format(
                    protocol=protocol,
                    ip_address=ip_address)
            elif table:
                cmd = self.cli_command[2].format(
                    protocol=protocol,
                    table=table)
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

class ShowRouteProtocolExtensiveSchema(MetaParser):
    """ Schema for:
            * show route protocol {protocol} extensive
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
                                "rt-announced-count": str,
                                "rt-destination": str,
                                "rt-entry": {
                                    "active-tag": str,
                                    "age": {
                                        "#text": str,
                                        Optional("@junos:seconds"): str
                                    },
                                    "announce-bits": str,
                                    "announce-tasks": str,
                                    "as-path": str,
                                    "bgp-path-attributes": {
                                        "attr-as-path-effective": {
                                            "aspath-effective-string": str,
                                            "attr-value": str
                                        }
                                    },
                                    "current-active": str,
                                    "inactive-reason": str,
                                    "last-active": str,
                                    "local-as": str,
                                    "metric": str,
                                    "nh": {
                                        Optional("@junos:indent"): str,
                                        "label-element": str,
                                        "label-element-childcount": str,
                                        "label-element-lspid": str,
                                        "label-element-parent": str,
                                        "label-element-refcount": str,
                                        "label-ttl-action": str,
                                        "load-balance-label": str,
                                        "mpls-label": str,
                                        "nh-string": str,
                                        "selected-next-hop": str,
                                        "session": str,
                                        "to": str,
                                        "via": str,
                                        "weight": str
                                    },
                                    "nh-address": str,
                                    "nh-index": str,
                                    "nh-kernel-id": str,
                                    "nh-reference-count": str,
                                    "nh-type": str,
                                    "preference": str,
                                    "preference2": str,
                                    "protocol-name": str,
                                    "rt-entry-state": str,
                                    "rt-ospf-area": str,
                                    "rt-tag": str,
                                    "task-name": str,
                                    "validation-state": str
                                },
                                "rt-entry-count": {
                                    "#text": str,
                                    Optional("@junos:format"): str
                                },
                                "rt-prefix-length": str,
                                "rt-state": str,
                                "tsi": {
                                    "#text": str,
                                    Optional("@junos:indent"): str
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
                raise SchemaTypeError('rt is not a list')
            def validate_nh_list(value):
                # Pass nh list of dict in value
                if not isinstance(value, list):
                    raise SchemaTypeError('nh is not a list')
                nh_schema = Schema({
                    Optional("@junos:indent"): str,
                    Optional("label-element"): str,
                    Optional("label-element-childcount"): str,
                    Optional("label-element-lspid"): str,
                    Optional("label-element-parent"): str,
                    Optional("label-element-refcount"): str,
                    Optional("label-ttl-action"): str,
                    Optional("load-balance-label"): str,
                    Optional("mpls-label"): str,
                    "nh-string": str,
                    Optional("selected-next-hop"): str,
                    Optional("session"): str,
                    "to": str,
                    "via": str,
                    Optional("weight"): str
                })
                # Validate each dictionary in list
                for item in value:
                    nh_schema.validate(item)
                return value

            # Create rt Schema
            rt_schema = Schema({
                Optional("@junos:style"): str,
                "rt-announced-count": str,
                "rt-destination": str,
                Optional("rt-entry"): {
                    Optional("active-tag"): str,
                    Optional("age"): {
                        "#text": str,
                        Optional("@junos:seconds"): str
                    },
                    Optional("announce-bits"): str,
                    Optional("announce-tasks"): str,
                    "as-path": str,
                    "bgp-path-attributes": {
                        "attr-as-path-effective": {
                            "aspath-effective-string": str,
                            "attr-value": str
                        }
                    },
                    Optional("current-active"): str,
                    Optional("inactive-reason"): str,
                    Optional("last-active"): str,
                    "local-as": str,
                    Optional("metric"): str,
                    Optional("nh"): Use(validate_nh_list),
                    "nh-address": str,
                    "nh-index": str,
                    Optional("nh-kernel-id"): str,
                    "nh-reference-count": str,
                    "nh-type": str,
                    "preference": str,
                    Optional("preference2"): str,
                    "protocol-name": str,
                    "rt-entry-state": str,
                    Optional("rt-ospf-area"): str,
                    Optional("rt-tag"): str,
                    "task-name": str,
                    "validation-state": str
                },
                "rt-entry-count": {
                    "#text": str,
                    Optional("@junos:format"): str
                },
                Optional("rt-prefix-length"): str,
                Optional("rt-state"): str,
                Optional("tsi"): {
                    "#text": str,
                    Optional("@junos:indent"): str
                }
            })
            # Validate each dictionary in list
            for item in value:
                rt_schema.validate(item)
            return value

        # Create Route Table Schema
        route_table_schema = Schema({
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
            route_table_schema.validate(item)
        return value

    # Main Schema
    schema = {
        Optional("@xmlns:junos"): str,
        "route-information": {
            Optional("@xmlns"): str,
            "route-table": Use(validate_route_table_list)
        }
    }

class ShowRouteProtocolExtensive(ShowRouteProtocolExtensiveSchema):
    """ Parser for:
            * show route protocol {protocol} extensive
            * show route protocol {protocol} table {table} extensive
            * show route protocol {protocol} table {table} extensive {destination}
    """

    cli_command = ['show route protocol {protocol} extensive',
                    'show route protocol {protocol} table {table} extensive',
                    'show route protocol {protocol} table {table} extensive {destination}',]
    def cli(self, protocol, table=None, destination=None, output=None):
        if not output:
            if table and destination:
                cmd = self.cli_command[1].format(
                    protocol=protocol,
                    table=table,
                    destination=destination)
            elif table:
                cmd = self.cli_command[1].format(
                    protocol=protocol,
                    table=table)
            else:
                cmd = self.cli_command[0].format(
                    protocol=protocol)
            out = self.device.execute(cmd)
        else:
            out = output

        ret_dict = {}
        state_type = None

        # inet.0: 929 destinations, 1615 routes (929 active, 0 holddown, 0 hidden)
        p1 = re.compile(r'^(?P<table_name>\S+): +(?P<destination_count>\d+) +'
                r'destinations, +(?P<total_route_count>\d+) +routes +'
                r'\((?P<active_route_count>\d+) +active, +(?P<holddown_route_count>\d+) +'
                r'holddown, +(?P<hidden_route_count>\d+) +hidden\)$')

        # 0.0.0.0/0 (1 entry, 1 announced)
        # 10.1.0.0/24 (2 entries, 1 announced)
        p2 = re.compile(r'^(?P<rt_destination>\S+)(\/(?P<rt_prefix_length>\d+))? +\((?P<format>(?P<text>\d+) +(entry|entries)), +(?P<announced>\d+) +announced\)$')

        # State: <FlashAll>
        # State: <Active Int Ext>
        p3 = re.compile(r'State: +\<(?P<rt_state>[\S\s]+)\>$')

        # *OSPF   Preference: 150/10
        p4 = re.compile(r'^(?P<active_tag>\*)?(?P<protocol>\S+)\s+Preference:\s+(?P<preference>\d+)(\/(?P<preference2>\d+))?$')

        # Next hop type: Router, Next hop index: 613
        p5 = re.compile(r'^Next +hop type: +(?P<nh_type>\S+), +Next +hop +index: +(?P<nh_index>\d+)$')

        # Address: 0xdfa7934
        p6 = re.compile(r'^Address: +(?P<nh_address>\S+)$')

        # Next-hop reference count: 458
        p7 = re.compile(r'^Next-hop +reference +count: +(?P<nh_reference_count>\d+)$')

        # Next hop: 10.169.14.121 via ge-0/0/1.0 weight 0x1, selected
        p8 = re.compile(r'^(?P<nh_string>Next +hop): +(?P<to>\S+) +via +(?P<via>\S+)( +weight +(?P<weight>\w+))?(, +(?P<selected_next_hop>\w+))?$')

        # Session Id: 0x141
        p9 = re.compile(r'^Session +Id: +\d+[a-z]+(?P<session_id>\w+)$')

        # Local AS: 65171 
        p10 = re.compile(r'^Local +AS: (?P<local_as>\d+)$')

        # Age: 3w2d 4:43:35   Metric: 101 
        # Age: 3:07:25    Metric: 200
        p11 = re.compile(r'^Age:\s+(?P<age>\w+(\s+\S+)?)\s+Metric:\s+(?P<metric>\d+)$')

        # Validation State: unverified 
        p12 = re.compile(r'^Validation +State: +(?P<validation_state>\S+)$')

        # Tag: 0 
        p13 = re.compile(r'^Tag: +(?P<rt_tag>\d+)$')
        
        # Task: OSPF
        p14 = re.compile(r'^Task: +(?P<task>\S+)$')

        # Announcement bits (3): 0-KRT 5-LDP 7-Resolve tree 3 
        p15 = re.compile(r'^Announcement +bits +\((?P<announce_bits>\d+)\): +(?P<announce_tasks>[\S\s]+)$')

        # AS path: I 
        p16 = re.compile(r'^(?P<aspath_effective_string>AS +path:) +(?P<attr_value>\S+)$')

        # KRT in-kernel 0.0.0.0/0 -> {10.169.14.121}
        p17 = re.compile(r'^(?P<text>KRT +in-kernel+[\S\s]+)$')

        # Inactive reason: Route Preference
        p18 = re.compile(r'^Inactive\s+reason: +(?P<inactive_reason>[\S\s]+)$')

        # Area: 0.0.0.8
        p19 = re.compile(r'^Area: +(?P<rt_ospf_area>\S+)$')

        # Label operation: Push 17000
        # Label operation: Push 17000, Push 1650, Push 1913(top)
        p20 = re.compile(r'^Label +operation: +(?P<mpls_label>[\S\s]+)$')

        # Label TTL action: no-prop-ttl
        # Label TTL action: no-prop-ttl, no-prop-ttl, no-prop-ttl(top)
        p21 = re.compile(r'^Label +TTL +action: +(?P<label_ttl_action>[\S\s]+)$')

        # Load balance label: Label 17000: None; Label 1650: None; Label 1913: None;
        p22 = re.compile(r'^Load +balance +label: +(?P<load_balance_label>[\S\s]+)$')

        # Label element ptr: 0xc5f6ec0
        p23 = re.compile(r'^Label +element +ptr: +(?P<label_element>\S+)$')

        # Label parent element ptr: 0x0
        p24 = re.compile(r'^Label +parent +element +ptr: +(?P<label_element_parent>\S+)$')
        
        # Label element references: 2
        p25 = re.compile(r'^Label +element +references: +(?P<label_element_refcount>\d+)$')

        # Label element child references: 1
        p26 = re.compile(r'^Label +element +child +references: +(?P<label_element_childcount>\d+)$')

        # Label element lsp id: 0
        p27 = re.compile(r'^Label +element +lsp +id: +(?P<label_element_lspid>\d+)$')

        # Task: OSPF3 I/O./var/run/ppmd_control
        p28 = re.compile(r'^Task: +(?P<task_name>[\S\s]+)$')

        # OSPF3 realm ipv6-unicast area : 0.0.0.0, LSA ID : 0.0.0.1, LSA type : Extern
        p29 = re.compile(r'^OSPF3\s+realm\s+ipv6-unicast\s+area\s:[\S\s]+$')

        for line in out.splitlines():
            line = line.strip()
            # inet.0: 929 destinations, 1615 routes (929 active, 0 holddown, 0 hidden)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                route_table = ret_dict.setdefault('route-information', {}). \
                    setdefault('route-table', [])
                route_table_dict = {k.replace('_', '-'):v for k, v in group.items() if v is not None}
                route_table.append(route_table_dict)
                continue

            # 0.0.0.0/0 (1 entry, 1 announced)
            # 10.1.0.0/24 (2 entries, 1 announced)
            m = p2.match(line)
            if m:
                group = m.groupdict()
                state_type = 'route_table'
                rt_destination = group['rt_destination']
                rt_format = group['format']
                text = group['text']
                announced = group['announced']
                rt_prefix_length = group['rt_prefix_length']
                rt_list = route_table_dict.setdefault('rt', [])
                rt_dict = {}
                rt_dict.update({'rt-announced-count' : announced})
                rt_dict.update({'rt-destination' : rt_destination})
                if rt_prefix_length:
                    rt_dict.update({'rt-prefix-length' : rt_prefix_length})
                rt_entry_count_dict = rt_dict.setdefault('rt-entry-count', {})
                rt_entry_count_dict.update({'#text': text})
                rt_entry_count_dict.update({'@junos:format': rt_format})
                rt_list.append(rt_dict)
                continue

            # State: <FlashAll>
            # State: <Active Int Ext>
            m = p3.match(line)
            if m:
                group = m.groupdict()
                if state_type == 'route_table':
                    rt_dict.update({'rt-state': group['rt_state']})
                elif state_type == 'protocol':
                    rt_entry_dict.update({'rt-entry-state': group['rt_state']})
                continue

            # *OSPF   Preference: 150/10
            m = p4.match(line)
            if m:
                group = m.groupdict()
                state_type = 'protocol'
                active_tag = group['active_tag']
                protocol_name = group['protocol']
                preference = group['preference']
                preference2 = group['preference2']
                rt_entry_dict = rt_dict.setdefault('rt-entry', {})
                if active_tag:
                    rt_entry_dict.update({'active-tag': active_tag})
                rt_entry_dict.update({'protocol-name': protocol_name})
                rt_entry_dict.update({'preference': preference})
                if preference2:
                    rt_entry_dict.update({'preference2': preference2})
                continue

            # Next hop type: Router, Next hop index: 613
            m = p5.match(line)
            if m:
                group = m.groupdict()
                nh_type = group['nh_type']
                nh_index = group['nh_index']
                rt_entry_dict.update({'nh-type': nh_type})
                rt_entry_dict.update({'nh-index': nh_index})
                continue

            # Address: 0xdfa7934
            m = p6.match(line)
            if m:
                group = m.groupdict()
                rt_entry_dict.update({'nh-address': group['nh_address']})
                continue

            # Next-hop reference count: 458
            m = p7.match(line)
            if m:
                group = m.groupdict()
                rt_entry_dict.update({'nh-reference-count': group['nh_reference_count']})
                continue

            # Next hop: 10.169.14.121 via ge-0/0/1.0 weight 0x1, selected
            m = p8.match(line)
            if m:
                group = m.groupdict()
                selected_next_hop = group['selected_next_hop']
                nh_list = rt_entry_dict.setdefault('nh', [])
                nh_dict = {}
                nh_list.append(nh_dict)
                keys = ['to', 'via', 'weight', 'nh_string']
                for key in keys:
                    v = group[key]
                    if v:
                        nh_dict.update({key.replace('_', '-'): v})
                continue

            # Session Id: 0x141
            m = p9.match(line)
            if m:
                group = m.groupdict()
                nh_dict.update({'session': group['session_id']})
                continue

            # Local AS: 65171 
            m = p10.match(line)
            if m:
                group = m.groupdict()
                rt_entry_dict.update({'local-as': group['local_as']})
                continue

            # Age: 3w2d 4:43:35   Metric: 101 
            m = p11.match(line)
            if m:
                group = m.groupdict()
                age_dict = rt_entry_dict.setdefault('age', {})
                age_dict.update({'#text': group['age']})
                rt_entry_dict.update({'metric': group['metric']})
                continue

            # Validation State: unverified 
            m = p12.match(line)
            if m:
                group = m.groupdict()
                rt_entry_dict.update({'validation-state': group['validation_state']})
                continue

            # Tag: 0 
            m = p13.match(line)
            if m:
                group = m.groupdict()
                rt_entry_dict.update({'rt-tag': group['rt_tag']})
                continue
            
            # Task: OSPF
            m = p14.match(line)
            if m:
                group = m.groupdict()
                rt_entry_dict.update({'task-name': group['task']})
                continue

            # Announcement bits (3): 0-KRT 5-LDP 7-Resolve tree 3 
            m = p15.match(line)
            if m:
                group = m.groupdict()
                rt_entry_dict.update({'announce-bits': group['announce_bits']})
                rt_entry_dict.update({'announce-tasks': group['announce_tasks']})
                continue

            # AS path: I 
            m = p16.match(line)
            if m:
                group = m.groupdict()
                attr_as_path_dict = rt_entry_dict.setdefault('bgp-path-attributes', {}). \
                    setdefault('attr-as-path-effective', {})
                rt_entry_dict.update({'as-path': line})
                attr_as_path_dict.update({'aspath-effective-string': group['aspath_effective_string']})
                attr_as_path_dict.update({'attr-value': group['attr_value']})
                continue

            # KRT in-kernel 0.0.0.0/0 -> {10.169.14.121}
            m = p17.match(line)
            if m:
                group = m.groupdict()
                tsi_dict = rt_dict.setdefault('tsi', {})
                tsi_dict.update({'#text': group['text']})
                continue
            
            # Inactive reason: Route Preference
            m = p18.match(line)
            if m:
                group = m.groupdict()
                rt_entry_dict.update({'inactive-reason': group['inactive_reason']})
                continue
            
            # Area: 0.0.0.8
            m = p19.match(line)
            if m:
                group = m.groupdict()
                rt_entry_dict.update({'rt-ospf-area': group['rt_ospf_area']})
                continue

            # Label operation: Push 17000
            # Label operation: Push 17000, Push 1650, Push 1913(top)
            m = p20.match(line)
            if m:
                group = m.groupdict()
                nh_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # Label TTL action: no-prop-ttl
            # Label TTL action: no-prop-ttl, no-prop-ttl, no-prop-ttl(top)
            m = p21.match(line)
            if m:
                group = m.groupdict()
                nh_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # Load balance label: Label 17000: None; Label 1650: None; Label 1913: None;
            m = p22.match(line)
            if m:
                group = m.groupdict()
                nh_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # Label element ptr: 0xc5f6ec0
            m = p23.match(line)
            if m:
                group = m.groupdict()
                nh_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # Label parent element ptr: 0x0
            m = p24.match(line)
            if m:
                group = m.groupdict()
                nh_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue
            
            # Label element references: 2
            m = p25.match(line)
            if m:
                group = m.groupdict()
                nh_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # Label element child references: 1
            m = p26.match(line)
            if m:
                group = m.groupdict()
                nh_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # Label element lsp id: 0
            m = p27.match(line)
            if m:
                group = m.groupdict()
                nh_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # Task: OSPF3 I/O./var/run/ppmd_control
            m = p28.match(line)
            if m:
                group = m.groupdict()
                rt_entry_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue
            
            # OSPF3 realm ipv6-unicast area : 0.0.0.0, LSA ID : 0.0.0.1, LSA type : Extern
            m = p29.match(line)
            if m:
                group = m.groupdict()
                text = tsi_dict.get('#text', '')
                tsi_dict.update({'#text': '{}\n{}'.format(text, line)})
                continue

        return ret_dict