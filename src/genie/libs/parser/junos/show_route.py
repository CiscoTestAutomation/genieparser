''' show_route.py

JUNOS parsers for the following commands:
    * show route table {table}
    * show route table {table} {prefix}
    * show route table {table} label-switched-path {name}
    * show route
    * show route protocol {protocol} extensive
    * show route protocol {protocol} table {table} extensive
    * show route protocol {protocol} table {table}
    * show route protocol {protocol}
    * show route protocol {protocol} {ip_address}
    * show route instance detail
    * show route protocol {protocol} table {table} extensive {destination}
    * show route advertising-protocol {protocol} {ip_address}
    * show route advertising-protocol {protocol} {ip_address} {route}
    * show route advertising-protocol {protocol} {ip_address} {route} detail
    * show route forwarding-table summary
    * show route forwarding-table label {label}
    * show route summary
    * show route {route} extensive
    * show route extensive
    * show route extensive {destination}
'''

import re

# Metaparser
from genie.metaparser import MetaParser
from pyats.utils.exceptions import SchemaError
from genie.metaparser.util.schemaengine import Any, Optional, Use, Schema, ListOf, Or
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
                            Optional('active_tag'): str,
                            Optional('protocol_name'): str,
                            Optional('preference'): str,
                            Optional('preference2'): str,
                            Optional('age'): str,
                            Optional('metric'): str,
                            Optional('rt-tag'): str,
                            Optional('learned_from'): str,
                            Optional('local_preference'): str,
                            Optional('nh_type'): str,
                            Optional('next_hop'): {
                                'next_hop_list': {
                                    Any(): {
                                        Optional('to'): str,
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
    * show route table {table} {prefix} {destination}
'''
class ShowRouteTable(ShowRouteTableSchema):

    cli_command = [
        'show route table {table}',
        'show route table {table} {prefix}',
        'show route table {table} {prefix} {destination}',
    ]

    def cli(self, table, prefix=None, destination=None, output=None):

        if output is None:
            if table and prefix and destination:
                command = self.cli_command[2].format(
                    table=table, 
                    prefix=prefix,
                    destination=destination)
            elif table and prefix:
                command = self.cli_command[1].format(table=table, prefix=prefix)
            else:
                command = self.cli_command[0].format(table=table)
            out = self.device.execute(command)
        else:
            out = output


        # inet.3: 3 destinations, 3 routes (3 active, 0 holddown, 0 hidden)
        r1 = re.compile(r'(?P<table_name>\S+):\s+(?P<destination_count>\d+)\s+'
                        r'destinations\,\s+(?P<total_route_count>\d+)\s+routes\s+'
                        r'\((?P<active_route_count>\d+)\s+active\,\s+(?P<holddown_route_count>\d+)'
                        r'\s+holddown\,\s+(?P<hidden_route_count>\d+)\s+hidden\)')

        # 192.168.51.1/32    *[Local/0] 00:02:35
        # 10.64.4.4/32         *[LDP/9] 03:40:50, metric 110
        # 10.64.4.4/32   *[L-OSPF/9/5] 1d 02:16:51, metric 110
        # 118420             *[VPN/170] 31w3d 20:13:54
        # ff02::2/128 *[INET6/0] 00:05:35
        r2 = re.compile(r'^ *(?P<rt_destination>\S+) +(?P<active_tag>\*)?\[(?P<protocol_name>[\w\-]+)\/(?P<preference>\d+)\/?(?P<preference2>\d+)?\] +(?P<age>[\d\:wd ]+)(, +metric +(?P<metric>\d+))?(, +tag +(?P<rt_tag>\d+))?(, +localpref +(?P<local_preference>\d+))?(, +from +(?P<learned_from>\S+))?$')

        # > to 192.168.220.6 via ge-0/0/1.0
        # > to 192.168.220.6 via ge-0/0/1.0, Push 305550
        # > to 192.168.220.6 via ge-0/0/1.0, Pop
        # Local via ge-0/0/4.11
        # >  via ge-0/0/2.1
        r3 = re.compile(r'^(?P<best_route>>)?(Local)? *(to +(?P<to>\S+))? *via +(?P<via>[^,\s]+)(, +(?P<mpls_label>[\S ]+))?')

        # fe80::250:5600:b8d:fea3/128
        # this regex widely match other pattern. intendedly exclude below `Reject`
        # 192.168.51.1/32    *[Local/0] 00:02:35
        #                Reject # <-----
        r4 = re.compile(r'^(?!.*Reject)(?P<rt_destination>[\w\:\/]+)$')

        # *[Local/0] 00:26:06
        r5 = re.compile(r'^(?P<active_tag>\*)?\[(?P<protocol_name>[\w\-]+)\/'
            r'(?P<preference>\d+)\/?(?P<preference2>\d+)?\] +(?P<age>[\d\:wd ]+)'
            r'(, +metric +(?P<metric>\d+))?(, +tag +(?P<rt_tag>\d+))?$')

        # Reject
        r6 = re.compile(r'^(?P<nh_type>Reject)$')

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
                rt_tag = group.pop('rt_tag', None)
                rt_destination = group.pop('rt_destination', None)

                route_dict = table_dict.setdefault('routes', {})\
                                       .setdefault(rt_destination, {})

                route_dict.update({k: v for k, v in group.items() if v})
                if rt_tag:
                    route_dict.update({'rt-tag': rt_tag})
                continue

            # > to 192.168.220.6 via ge-0/0/1.0
            # > to 192.168.220.6 via ge-0/0/1.0, Push 305550
            # to 10.2.94.2 via lt-1/2/0.49
            # 
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

                if group['to']:
                    nh_dict['to'] = group['to']

                nh_dict['via'] = group['via']

                mpls_label = group['mpls_label']
                if mpls_label:
                    nh_dict['mpls_label'] = mpls_label

                best_route = group['best_route']
                if best_route:
                    nh_dict['best_route'] = best_route

                continue
        
            # fe80::250:5600:b8d:fea3/128
            result = r4.match(line)
            if result:
                group = result.groupdict()
                rt_destination = group.pop('rt_destination', None)

                route_dict = table_dict.setdefault('routes', {})\
                                       .setdefault(rt_destination, {})
                continue

            result = r5.match(line)
            if result:
                group = result.groupdict()
                rt_tag = group.pop('rt_tag', None)

                route_dict = table_dict.setdefault('routes', {})\
                                       .setdefault(rt_destination, {})

                route_dict.update({k: v for k, v in group.items() if v})
                if rt_tag:
                    route_dict.update({'rt-tag': rt_tag})
                continue

            result = r6.match(line)
            if result:
                group = result.groupdict()
                route_dict.update({k: v for k, v in group.items() if v})
                continue

        return parsed_output

class ShowRouteSchema(MetaParser):
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

    # Main Schema
    schema = {
        Optional("@xmlns:junos"): str,
        'route-information': {
            Optional("@xmlns"): str,
            'route-table': ListOf({
                "active-route-count": str,
                "destination-count": str,
                "hidden-route-count": str,
                "holddown-route-count": str,
                Optional("rt"): ListOf({
                    Optional("@junos:style"): str,
                    Optional("rt-destination"): str,
                    "rt-entry": {
                        Optional("active-tag"): str,
                        "age": {
                            "#text": str,
                            Optional("@junos:seconds"): str
                        },
                        Optional('as-path'): str,
                        Optional("current-active"): str,
                        Optional("last-active"): str,
                        Optional("learned-from"): str,
                        Optional("local-preference"): str,
                        Optional("peer-id"): str,
                        Optional("med"): str,
                        Optional("metric"): str,
                        Optional("metric2"): str,
                        Optional("nh"): ListOf({
                            Optional("mpls-label"): str,
                            Optional("selected-next-hop"): str,
                            Optional("nh-local-interface"): str,
                            Optional("nh-table"): str,
                            Optional("to"): str,
                            Optional("via"): str
                        }),
                        Optional('nh-type'): str,
                        "preference": str,
                        Optional("preference2"): str,
                        "protocol-name": str,
                        Optional('rt-tag'): str,
                        Optional("validation-state"): str
                    }
                }),
                "table-name": str,
                "total-route-count": str
            })
        }
    }

class ShowRoute(ShowRouteSchema):
    """ Parser for:
            * show route
            * show route {ip_address}
            * show route protocol {protocol} {ip_address}
            * show route protocol {protocol}
            * show route protocol {protocol} table {table}
    """
    cli_command = [
                    'show route',
                    'show route {ip_address}',
                    'show route protocol {protocol}',
                    'show route protocol {protocol} {ip_address}',
                    'show route protocol {protocol} table {table}']

    def cli(self, protocol=None, ip_address=None, table=None, output=None):
        if not output:
            if protocol and table:
                cmd = self.cli_command[4].format(
                    protocol=protocol,
                    table=table
                )
            elif ip_address and not protocol:
                cmd = self.cli_command[1].format(
                    ip_address=ip_address
                )
            elif protocol and not ip_address:
                cmd = self.cli_command[2].format(
                    protocol=protocol
                )
            elif ip_address and protocol:
                cmd = self.cli_command[3].format(
                    ip_address=ip_address,
                    protocol=protocol
                )
            else:
                cmd = self.cli_command[0]

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
        
        # 10.220.0.0/16      *[BGP/170] 3w3d 03:12:24, MED 12003, localpref 120, from 10.169.14.240
        # 10.169.14.240/32  *[Static/5] 5w2d 15:42:25
        # *[OSPF3/10] 3w1d 17:03:23, metric 5
        # 0.0.0.0/0          *[OSPF/150/10] 3w3d 03:24:58, metric 101, tag 0
        # 167963             *[LDP/9] 1w6d 20:41:01, metric 1, metric2 100, tag 65000500
        # 10.16.2.2/32         *[Static/5] 00:00:02
        p2 = re.compile(r'^((?P<rt_destination>\S+) +)?(?P<active_tag>[\*\+\-])?\[(?P<protocol>[\w\-]+)\/(?P<preference>\d+)(\/(?P<preference2>\d+))?\] +(?P<text>\S+( +\S+)?)(, +metric +(?P<metric>\d+))?(, +metric2 +(?P<metric2>\d+))?(, +tag +(?P<rt_tag>\d+))?(, +MED +(?P<med>\w+))?(, +localpref +(?P<local_preference>\d+))?(, +from +(?P<learned_from>\S+))?$')

        # MultiRecv
        p2_1 = re.compile(r'^(?P<nh_type>MultiRecv)$')
        
        # >  to 10.169.14.121 via ge-0/0/1.0
        p3 = re.compile(r'^(\> +)?(to +(?P<to>\S+) +)?via +(?P<via>\S+)'
                        r'(, +(?P<mpls_label>[\S\s]+))?$')
        
        # Local via fxp0.0
        p3_1 = re.compile(r'^Local +via +(?P<nh_local_interface>\S+)$')

        # AS path: (65151 65000) I, validation-state: unverified
        # AS path: I
        # AS path: 3 4 I, validation-state: unverified
        p4 = re.compile(r'AS +path:(?P<as_path>([()\d\s]+ )?\w)'
                        r'(, validation-state: +(?P<validation_state>\S+))?$')
        
        # to table inet.0
        p5 = re.compile(r'^to +table +(?P<nh_table>\S+)$')

        # 2001:db8:eb18:ca45::1/128
        pIP = re.compile(r'^(?P<rt_destination>[\w:\/]+)$')

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
                metric2 = group['metric2']
                rt_tag = group['rt_tag']
                learned_from = group['learned_from']
                local_preference = group['local_preference']
                med = group['med']
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
                if metric2:
                    rt_entry_dict.update({'metric2': metric2})
                if rt_tag:
                    rt_entry_dict.update({'rt-tag': rt_tag})
                if learned_from:
                    rt_entry_dict.update({'learned-from': learned_from})
                if local_preference:
                    rt_entry_dict.update({'local-preference': local_preference})
                if med:
                    rt_entry_dict.update({'med': med})
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

            # Local via fxp0.0
            m = p3_1.match(line)
            if m:
                group = m.groupdict()
                nh_list = rt_entry_dict.setdefault('nh', [])
                nh_dict = {}
                nh_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                nh_list.append(nh_dict)
                continue
            
            # AS path: (65151 65000) I, validation-state: unverified
            # AS path: I
            m = p4.match(line)
            if m:
                group = m.groupdict()
                rt_entry_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue
            
            # to table inet.0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                nh_list = rt_entry_dict.setdefault('nh', [])
                nh_dict = {}
                nh_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                nh_list.append(nh_dict)
                continue

            # 2001:db8:eb18:ca45::1/128
            m = pIP.match(line)
            if m:
                group = m.groupdict()
                rt_destination = group['rt_destination']
                continue
        return ret_dict

class ShowRouteLogicalSystem(ShowRoute):
    """ Parser for:
            * show route logical-system {logical_name}
    """
    cli_command = 'show route logical-system {logical_name}'
    def cli(self, logical_name, output=None):
        if not output:
            cmd = self.cli_command.format(
                    logical_name=logical_name)
            out = self.device.execute(cmd)
        else:
            out = output
        
        return super().cli(output=out) 

class ShowRouteProtocolNoMore(ShowRoute):
    """ Parser for:
            * show route protocol {protocol} {ip_address} | no-more
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
                                    "accepted": str,
                                    "active-tag": str,
                                    "age": {
                                        "#text": str,
                                        Optional("@junos:seconds"): str
                                    },
                                    "announce-bits": str,
                                    "announce-tasks": str,
                                    "as-path": str,
                                    "cluster-list": str,
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
                                    "peer-as": str,
                                    "metric": str,
                                    "metric2": str,
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
                                    "gateway": str,
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

    rt_entry_schema = {
        Optional("accepted"): str,
        Optional("active-tag"): str,
        Optional("age"): {
            "#text": str,
            Optional("@junos:seconds"): str
        },
        Optional("announce-bits"): str,
        Optional("announce-tasks"): str,
        Optional("as-path"): str,
        Optional("cluster-list"): str,
        Optional("bgp-rt-flag"): str,
        Optional("bgp-path-attributes"): {
            "attr-as-path-effective": {
                "aspath-effective-string": str,
                "attr-value": str
            }
        },
        Optional("current-active"): str,
        Optional("inactive-reason"): str,
        Optional("last-active"): str,
        Optional("local-as"): str,
        Optional("local-preference"): str,
        Optional("peer-as"): str,
        Optional("metric"): str,
        Optional("metric2"): str,
        Optional("nh"): ListOf({
            Optional("@junos:indent"): str,
            Optional("label-element"): str,
            Optional("label-element-childcount"): str,
            Optional("label-element-lspid"): str,
            Optional("label-element-parent"): str,
            Optional("label-element-refcount"): str,
            Optional("label-ttl-action"): str,
            Optional("load-balance-label"): str,
            Optional("mpls-label"): str,
            Optional("nh-string"): str,
            Optional("selected-next-hop"): str,
            Optional("session"): str,
            Optional("to"): str,
            Optional("via"): str,
            Optional("weight"): str
        }),
        Optional("nh-address"): str,
        Optional("nh-index"): str,
        Optional("nh-kernel-id"): str,
        Optional("nh-reference-count"): str,
        Optional("gateway"): str,
        Optional("nh-type"): str,
        Optional("preference"): str,
        Optional("preference2"): str,
        Optional("protocol-name"): str,
        Optional("protocol-nh"): ListOf({
            Optional("@junos:indent"): str,
            Optional("forwarding-nh-count"): str,
            "indirect-nh": str,
            Optional("label-ttl-action"): str,
            Optional("load-balance-label"): str,
            Optional("metric"): str,
            Optional("mpls-label"): str,
            Optional("nh"): ListOf({
                Optional("@junos:indent"): str,
                Optional("label-element"): str,
                Optional("label-element-childcount"): str,
                Optional("label-element-lspid"): str,
                Optional("label-element-parent"): str,
                Optional("label-element-refcount"): str,
                Optional("label-ttl-action"): str,
                Optional("load-balance-label"): str,
                Optional("mpls-label"): str,
                Optional("nh-string"): str,
                Optional("selected-next-hop"): str,
                Optional("session"): str,
                Optional("to"): str,
                Optional("via"): str,
                Optional("weight"): str
            }),
            Optional("nh-index"): str,
            Optional("nh-type"): str,
            Optional("output"): str,
            "to": str
        }),
        Optional("rt-entry-state"): str,
        Optional("rt-ospf-area"): str,
        Optional("rt-tag"): str,
        Optional("peer-id"): str,
        Optional("task-name"): str,
        Optional("validation-state"): str
    }

    # Main Schema
    schema = {
        Optional("@xmlns:junos"): str,
        "route-information": {
            Optional("@xmlns"): str,
            "route-table": ListOf({
                "active-route-count": str,
                "destination-count": str,
                "hidden-route-count": str,
                "holddown-route-count": str,
                Optional("rt"): ListOf({
                    Optional("@junos:style"): str,
                    "rt-announced-count": str,
                    "rt-destination": str,
                    Optional("rt-entry"): Or(rt_entry_schema, ListOf(rt_entry_schema)),
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
                }),
                "table-name": str,
                "total-route-count": str
            })
        }
    }


class ShowRouteProtocolExtensive(ShowRouteProtocolExtensiveSchema):
    """ Parser for:
            * show route protocol {protocol} extensive
            * show route protocol {protocol} table {table} extensive
            * show route protocol {protocol} table {table} extensive {destination}
            * show route {route} extensive
            * show route extensive
            * show route extensive {destination}
    """

    cli_command = ['show route protocol {protocol} extensive',
                    'show route protocol {protocol} table {table} extensive',
                    'show route protocol {protocol} table {table} extensive {destination}',
                    'show route {route} extensive',
                    'show route extensive',
                    'show route extensive {destination}',
                    'show route protocol {protocol} {destination} extensive']
    def cli(self, protocol=None, table=None, 
            destination=None, route=None, 
            output=None):
        if not output:
            if protocol and table and destination:
                cmd = self.cli_command[2].format(
                    protocol=protocol,
                    table=table,
                    destination=destination)
            elif protocol and destination:
                cmd = self.cli_command[6].format(
                    protocol=protocol,
                    destination=destination)
            elif table and protocol:
                cmd = self.cli_command[1].format(
                    protocol=protocol,
                    table=table)
            elif protocol:
                cmd = self.cli_command[0].format(
                    protocol=protocol)
            elif route:
                cmd = self.cli_command[3].format(
                    route=route)
            elif destination:
                cmd = self.cli_command[5].format(
                    destination=destination)
            else:
                cmd = self.cli_command[4]
            out = self.device.execute(cmd)
        else:
            out = output

        ret_dict = {}
        state_type = None
        forwarding_nh_count = None
        protocol_nh_found = None
        originating_rib_found = None

        # inet.0: 929 destinations, 1615 routes (929 active, 0 holddown, 0 hidden)
        p1 = re.compile(r'^(?P<table_name>\S+): +(?P<destination_count>\d+) +'
                        r'destinations, +(?P<total_route_count>\d+) +routes +'
                        r'\((?P<active_route_count>\d+) +active, +(?P<holddown_route_count>\d+) +'
                        r'holddown, +(?P<hidden_route_count>\d+) +hidden\)$')

        # 0.0.0.0/0 (1 entry, 1 announced)
        # 10.1.0.0/24 (2 entries, 1 announced)
        # 0.0.0.0 (1 entry, 1 announced)
        p2 = re.compile(r'^(?P<rt_destination>\S+)(\/(?P<rt_prefix_length>\d+))? +'
                        r'\((?P<format>(?P<text>\d+) +(entry|entries)), +(?P<announced>\d+) +announced\)$')

        # State: <FlashAll>
        # State: <Active Int Ext>
        p3 = re.compile(r'State: +\<(?P<rt_state>[\S\s]+)\>$')

        # *OSPF   Preference: 150/10
        # *BGP    Preference: 170/-121
        p4 = re.compile(r'^(?P<active_tag>\*)?(?P<protocol>\S+)\s+'
                        r'Preference:\s+(?P<preference>\d+)(\/(\-)?(?P<preference2>\d+))?$')

        # Next hop type: Router, Next hop index: 613
        p5 = re.compile(r'^Next +hop type: +(?P<nh_type>\S+), +Next +hop +'
                        r'index: +(?P<nh_index>\d+)$')

        # Address: 0xdfa7934
        p6 = re.compile(r'^Address: +(?P<nh_address>\S+)$')

        # Next-hop reference count: 458
        p7 = re.compile(r'^Next-hop +reference +count: +(?P<nh_reference_count>\d+)$')

        # Source: 10.16.2.2
        p7_1 = re.compile(r'^Source: +(?P<gateway>\S+)$')

        # Next hop: 10.169.14.121 via ge-0/0/1.0 weight 0x1, selected
        # Nexthop: 10.169.14.121 via ge-0/0/1.0
        p8 = re.compile(r'^(?P<nh_string>Next *hop):( +(?P<to>\S+))? +via +(?P<via>\S+)'
                        r'( +weight +(?P<weight>\w+))?(, +(?P<selected_next_hop>\w+))?$')

        # Protocol next hop: 10.169.14.240
        p8_1 = re.compile(r'^Protocol +next +hop: +(?P<to>\S+)( +Metric: +(?P<metric>\d+))?$')

        # Session Id: 0x141
        p9 = re.compile(r'^Session +Id: +\d+[a-z]+(?P<session_id>\w+)$')

        # Local AS: 65171 
        # Local AS: 65171 Peer AS: 65171
        # Local AS:     1 Peer AS:     3
        p10 = re.compile(r'^Local +AS: +(?P<local_as>\d+)( +Peer +AS: +(?P<peer_as>\d+))?$')

        # Age: 3w2d 4:43:35   Metric: 101 
        # Age: 3:07:25    Metric: 200
        # Age: 29w6d 21:42:46
        p11 = re.compile(r'^Age:\s+(?P<age>(\w+(\s+\S+)?)|[\d:]+)(\s+Metric:\s+(?P<metric>\d+))?$')

        # Age: 12 Metric2: 50
        p11_2 = re.compile(r'^Age:\s+(?P<age>(\w+(\s+\S+)?)|[\d:]+)(\s+Metric2:\s+(?P<metric2>\d+))?$')

        # Validation State: unverified 
        p12 = re.compile(r'^Validation +State: +(?P<validation_state>\S+)$')

        # Tag: 0 
        p13 = re.compile(r'^Tag: +(?P<rt_tag>\d+)$')
        
        # Task: OSPF
        p14 = re.compile(r'^Task: +(?P<task>\S+)$')

        # Announcement bits (3): 0-KRT 5-LDP 7-Resolve tree 3 
        p15 = re.compile(r'^Announcement +bits +\((?P<announce_bits>\d+)\): +'
                         r'(?P<announce_tasks>[\S\s]+)$')

        # AS path: I 
        # AS path: 30000 4 103 104 105 106 107 108 109 I
        # AS path: I (Originator) Cluster list:  0.0.0.1 0.0.0.2 0.0.0.4
        p16 = re.compile(r'^(?P<aspath_effective_string>AS +path:) '
                         r'+((?P<attr_value>[\S\s]+) +Cluster +list: '
                         r'(?P<cluster_list>[\d\.\s]+)|(?P<attr_value2>[\S\s]+))$')

        # Accepted Multipath
        p16_1 = re.compile(r'^Accepted +(?P<accepted>\S+)$')

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

        # Page 0 idx 1, (group hktGCS002 type Internal) Type 1 val 0x10c0b9b0 (adv_entry)
        p30 = re.compile(r'^Page +\d+ +idx +\d+[\S\s]+$')
        
        # Advertised metrics:
        #     Flags: Nexthop Change
        #     Nexthop: Self
        #     MED: 12003
        #     Localpref: 120
        #     AS path: [65171] (65151 65000) I
        #     Communities: 65001:10 65151:244
        # Path 10.220.0.0
        # from 10.169.14.240
        # Vector len 4.  Val: 1
        p31 = re.compile(r'^(Advertised +metrics:)|'
                         r'(Flags: +)|(Nexthop: +)|(MED: +)|'
                         r'(Localpref: +)|(AS +path:)|(Communities:)|'
                         r'(Path +\S+)|(from +\S+)|(Vector +len)')
        
        # Indirect next hop: 0xc285884 1048574 INH Session ID: 0x1ac
        p32 = re.compile(r'^Indirect +next +hop: +(?P<indirect_nh>[\S\s]+)$')

        # Indirect next hops: 1
        p33 = re.compile(r'^Indirect +next +hops: +(?P<forwarding_nh_count>\d+)$')

        # 10.169.14.240/32 Originating RIB: inet.0
        p34 = re.compile(r'^\S+ +Originating +RIB: +[\S\s]+$')

        # Node path count: 1
        # Forwarding nexthops: 1
        p35 = re.compile(r'^(Node +path +count: +)|(Forwarding +nexthops: +)[\S\s]+$')

        # Cluster list:  10.16.2.2 10.64.4.4
        p36 = re.compile(r'^Cluster +list: +(?P<cluster_list>[\S\s]+)$')

        # Router ID: 10.16.2.2
        p37 = re.compile(r'^Router +ID: +(?P<peer_id>\S+)$')

        for line in out.splitlines():
            line = line.strip()
            # inet.0: 929 destinations, 1615 routes (929 active, 0 holddown, 0 hidden)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                route_table = ret_dict.setdefault('route-information', {}). \
                    setdefault('route-table', [])
                route_table_dict = {k.replace('_', '-'):
                    v for k, v in group.items() if v is not None}
                route_table.append(route_table_dict)
                continue

            # 0.0.0.0/0 (1 entry, 1 announced)
            # 10.1.0.0/24 (2 entries, 1 announced)
            m = p2.match(line)
            if m:
                group = m.groupdict()
                state_type = 'route_table'
                rt_prefix_length = group['rt_prefix_length']

                rt_destination = group['rt_destination']

                rt_format = group['format']
                text = group['text']
                announced = group['announced']
                
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
                protocol_nh_found = None
                originating_rib_found = None
                active_tag = group['active_tag']
                protocol_name = group['protocol']
                preference = group['preference']
                preference2 = group['preference2']
                rt_entry_exist = rt_dict.get('rt-entry', None)
                if not rt_entry_exist:
                    rt_entry_dict = rt_dict.setdefault('rt-entry', {})
                else:
                    if isinstance(rt_entry_exist, list):
                        rt_entry_dict = {}
                        rt_entry_exist.append(rt_entry_dict)
                    else:
                        old_rt_entry_dict = rt_entry_exist
                        rt_entry_dict = {}
                        rt_dict['rt-entry'] = []
                        rt_dict_list = rt_dict['rt-entry']
                        rt_dict_list.append(old_rt_entry_dict)
                        rt_dict_list.append(rt_entry_dict)
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

            # Source: 10.16.2.2
            m = p7_1.match(line)
            if m:
                group = m.groupdict()
                rt_entry_dict.update({'gateway': group['gateway']})
                continue
                
            # Next hop: 10.169.14.121 via ge-0/0/1.0 weight 0x1, selected
            m = p8.match(line)
            if m:
                group = m.groupdict()
                if originating_rib_found:
                    proto_output = protocol_nh_dict.get('output', '')
                    proto_output = '{}{}\n'.format(proto_output, line)
                    protocol_nh_dict.update({'output': proto_output})
                    continue
                selected_next_hop = group['selected_next_hop']
                if protocol_nh_found:
                    nh_list = protocol_nh_dict.setdefault('nh', [])
                    proto_nh_dict = {}
                    nh_list.append(proto_nh_dict)
                else:
                    nh_list = rt_entry_dict.setdefault('nh', [])
                    nh_dict = {}
                    nh_list.append(nh_dict)
                keys = ['to', 'via', 'weight', 'nh_string']
                for key in keys:
                    v = group[key]
                    if v:
                        if protocol_nh_found:
                            proto_nh_dict.update({key.replace('_', '-'): v})
                        else:
                            nh_dict.update({key.replace('_', '-'): v})
                continue
            
            # Protocol Next hop: 10.169.14.121 via ge-0/0/1.0 weight 0x1, selected
            m = p8_1.match(line)
            if m:
                group = m.groupdict()
                protocol_nh_found = True
                protocol_nh_list = rt_entry_dict.setdefault('protocol-nh', [])
                protocol_nh_dict = {k.replace('_', '-'):
                    v for k, v in group.items() if v is not None}
                if forwarding_nh_count:
                    protocol_nh_dict.update({'forwarding-nh-count' : forwarding_nh_count})
                protocol_nh_list.append(protocol_nh_dict)
                forwarding_nh_count = None
                continue

            # Session Id: 0x141
            m = p9.match(line)
            if m:
                group = m.groupdict()
                if originating_rib_found:
                    proto_output = protocol_nh_dict.get('output', '')
                    proto_output = '{}{}\n'.format(proto_output, line)
                    protocol_nh_dict.update({'output': proto_output})
                elif protocol_nh_found:
                    proto_nh_dict.update({'session': group['session_id']})
                else:
                    nh_dict.update({'session': group['session_id']})
                continue

            # Local AS: 65171 
            # Local AS: 65171 Peer AS: 65171
            # Local AS:     1 Peer AS:     3
            m = p10.match(line)
            if m:
                group = m.groupdict()
                rt_entry_dict.update({'local-as': group['local_as']})
                if group.get('peer_as'):
                    rt_entry_dict.update({'peer-as': group['peer_as']})
                continue

            # Age: 3w2d 4:43:35   Metric: 101 
            m = p11.match(line)
            if m:
                group = m.groupdict()
                age_dict = rt_entry_dict.setdefault('age', {})
                age_dict.update({'#text': group['age']})
                metric = group['metric']
                if metric:
                    rt_entry_dict.update({'metric': metric})
                continue

            # Age: 12 Metric2: 50
            m = p11_2.match(line)
            if m:
                group = m.groupdict()
                age_dict = rt_entry_dict.setdefault('age', {})
                age_dict.update({'#text': group['age']})
                metric2 = group['metric2']
                if metric2:
                    rt_entry_dict.update({'metric2': metric2})
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
            # AS path: I (Originator) Cluster list:  0.0.0.1 0.0.0.2 0.0.0.4
            m = p16.match(line)
            if m:
                rt_entry_exist = rt_dict.get('rt-entry', None)
                if rt_entry_exist:
                    group = m.groupdict()
                    if rt_dict.get('rt-entry', None) and group['cluster_list']:
                        rt_entry_dict.update({'cluster-list': group['cluster_list']})
                    group['attr_value'] = group['attr_value2'] if group['attr_value2'] else group['attr_value']
                    attr_as_path_dict = rt_entry_dict.setdefault('bgp-path-attributes', {}). \
                        setdefault('attr-as-path-effective', {})
                    rt_entry_dict.update({'as-path': line})
                    attr_as_path_dict.update({'aspath-effective-string': 
                        group['aspath_effective_string']})
                    attr_as_path_dict.update({'attr-value': group['attr_value']})
                    continue

            # Accepted Multipath
            m = p16_1.match(line)
            if m:
                group = m.groupdict()
                rt_entry_dict.update({'accepted': group['accepted']})
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
                if protocol_nh_found:
                    protocol_nh_dict.update({k.replace('_', '-'):
                        v for k, v in group.items() if v is not None})
                else:
                    nh_dict.update({k.replace('_', '-'):
                        v for k, v in group.items() if v is not None})
                continue

            # Label TTL action: no-prop-ttl
            # Label TTL action: no-prop-ttl, no-prop-ttl, no-prop-ttl(top)
            m = p21.match(line)
            if m:
                group = m.groupdict()
                if protocol_nh_found:
                    protocol_nh_dict.update({k.replace('_', '-'):
                        v for k, v in group.items() if v is not None})
                else:
                    nh_dict.update({k.replace('_', '-'):
                        v for k, v in group.items() if v is not None})
                continue

            # Load balance label: Label 17000: None; Label 1650: None; Label 1913: None;
            m = p22.match(line)
            if m:
                group = m.groupdict()
                if protocol_nh_found:
                    protocol_nh_dict.update({k.replace('_', '-'):
                        v for k, v in group.items() if v is not None})
                else:
                    nh_dict.update({k.replace('_', '-'):
                        v for k, v in group.items() if v is not None})
                continue

            # Label element ptr: 0xc5f6ec0
            m = p23.match(line)
            if m:
                group = m.groupdict()
                if protocol_nh_found:
                    protocol_nh_dict.update({k.replace('_', '-'):
                        v for k, v in group.items() if v is not None})
                else:
                    nh_dict.update({k.replace('_', '-'):
                        v for k, v in group.items() if v is not None})
                continue

            # Label parent element ptr: 0x0
            m = p24.match(line)
            if m:
                group = m.groupdict()
                nh_dict.update({k.replace('_', '-'):
                    v for k, v in group.items() if v is not None})
                continue
            
            # Label element references: 2
            m = p25.match(line)
            if m:
                group = m.groupdict()
                nh_dict.update({k.replace('_', '-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Label element child references: 1
            m = p26.match(line)
            if m:
                group = m.groupdict()
                nh_dict.update({k.replace('_', '-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Label element lsp id: 0
            m = p27.match(line)
            if m:
                group = m.groupdict()
                nh_dict.update({k.replace('_', '-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Task: OSPF3 I/O./var/run/ppmd_control
            m = p28.match(line)
            if m:
                group = m.groupdict()
                rt_entry_dict.update({k.replace('_', '-'):
                    v for k, v in group.items() if v is not None})
                continue
            
            # OSPF3 realm ipv6-unicast area : 0.0.0.0, LSA ID : 0.0.0.1, LSA type : Extern
            m = p29.match(line)
            if m:
                group = m.groupdict()
                tsi_dict = rt_dict.setdefault('tsi', {})
                text = tsi_dict.get('#text', '')
                tsi_dict.update({'#text': '{}\n{}'.format(text, line)})
                continue
            
            # Page 0 idx 1, (group hktGCS002 type Internal) Type 1 val 0x10c0b9b0 (adv_entry)
            m = p30.match(line)
            if m:
                tsi_dict = rt_dict.setdefault('tsi', {})
                group = m.groupdict()
                text = tsi_dict.get('#text', '')
                tsi_dict.update({'#text': '{}\n{}'.format(text, line)})
                continue

            # Advertised metrics:
            #     Flags: Nexthop Change
            #     Nexthop: Self
            #     MED: 12003
            #     Localpref: 120
            #     AS path: [65171] (65151 65000) I
            #     Communities: 65001:10 65151:244
            # Path 10.220.0.0
            # from 10.169.14.240
            # Vector len 4.  Val: 1
            m = p31.match(line)
            if m:
                group = m.groupdict()
                tsi_dict = rt_dict.setdefault('tsi', {})
                text = tsi_dict.get('#text', '')
                tsi_dict.update({'#text': '{}\n{}'.format(text, line)})
                continue

            # Indirect next hop: 0xc285884 1048574 INH Session ID: 0x1ac
            m = p32.match(line)
            if m:
                group = m.groupdict()
                protocol_nh_dict.update({k.replace('_', '-'):
                    v for k, v in group.items() if v is not None})
                continue

            # Indirect next hops: 1
            m = p33.match(line)
            if m:
                group = m.groupdict()
                protocol_nh_found = True
                forwarding_nh_count = group['forwarding_nh_count']
                continue

            # 10.169.14.240/32 Originating RIB: inet.0
            m = p34.match(line)
            if m:
                originating_rib_found = True
                proto_output = protocol_nh_dict.get('output', '')
                proto_output = '{}{}\n'.format(proto_output, line)
                protocol_nh_dict.update({'output': proto_output})
                continue

            # Node path count: 1
            # Forwarding nexthops: 1
            m = p35.match(line)
            if m:
                proto_output = protocol_nh_dict.get('output', '')
                proto_output = '{}{}\n'.format(proto_output, line)
                protocol_nh_dict.update({'output': proto_output})
                continue

            # Cluster list:  10.16.2.2 10.64.4.4
            m = p36.match(line)
            if m:
                group = m.groupdict()
                if rt_dict.get('rt-entry', None):
                    rt_entry_dict.update({'cluster-list': group['cluster_list']})
                continue
            
            # Router ID: 10.16.2.2 
            m = p37.match(line)
            if m:
                group = m.groupdict()
                rt_entry_dict.update({'peer-id': group['peer_id']})
                continue

        return ret_dict
    
class ShowRouteForwardingTableSummarySchema(MetaParser):
    """ Schema for:
            * show route forwarding-table summary
    """
    # schema = {
    #     Optional("@xmlns:junos"): str,
    #     "forwarding-table-information": {
    #         Optional("@xmlns"): str,
    #         "route-table": [
    #             {
    #                 "address-family": str,
    #                 "enabled-protocols": str,
    #                 "route-table-summary": [
    #                     {
    #                         "route-count": str,
    #                         "route-table-type": str
    #                     }
    #                 ],
    #                 "table-name": str
    #             }
    #         ]
    #     }
    # }

    schema = {
        Optional("@xmlns:junos"): str,
        "forwarding-table-information": {
            Optional("@xmlns"): str,
            "route-table": ListOf({
                "address-family": str,
                Optional("enabled-protocols"): str,
                "route-table-summary": ListOf({
                    "route-count": str,
                    "route-table-type": str
                }),
                "table-name": str
            })
        }
    }

class ShowRouteForwardingTableSummary(ShowRouteForwardingTableSummarySchema):
    """ Parser for:
            * show route forwarding-table summary
    """
    cli_command = 'show route forwarding-table summary'
    
    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        ret_dict = {}

        # Routing table: default.inet
        p1 = re.compile(r'^Routing +table: +(?P<table_name>\S+)$')

        # Internet:
        # DHCP Snooping:
        p2 = re.compile(r'^(?P<address_family>\S+( +\S+)?):$')

        # Enabled protocols: Bridging, 
        p3 = re.compile(r'^Enabled +protocols: +(?P<enabled_protocols>[\S\s]+)$')

        # perm:          1 routes
        p4 = re.compile(r'^(?P<route_table_type>\S+): +(?P<route_count>\d+) +routes$')

        for line in out.splitlines():
            line = line.strip()

            # Routing table: default.inet
            m = p1.match(line)
            if m:
                group = m.groupdict()
                forwarding_table_information_dict = ret_dict.setdefault('forwarding-table-information', {})
                route_table_list = forwarding_table_information_dict.setdefault('route-table', [])
                route_table_dict = {k.replace('_', '-'):v for k, v in group.items() if v is not None}
                route_table_list.append(route_table_dict)
                continue

            # Internet:
            # DHCP Snooping:
            m = p2.match(line)
            if m:
                group = m.groupdict()
                route_table_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # Enabled protocols: Bridging, 
            m = p3.match(line)
            if m:
                group = m.groupdict()
                route_table_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # perm:          1 routes
            m = p4.match(line)
            if m:
                group = m.groupdict()
                route_table_summary_list = route_table_dict.setdefault('route-table-summary', [])
                route_table_summary_list.append({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

        return ret_dict

class ShowRouteReceiveProtocolSchema(MetaParser):
    """ Schema for:
            * show route receive-protocol {protocol} {peer}
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
                                    "as-path": str,
                                    "local-preference": str,
                                    "med": str,
                                    "nh": {
                                        "to": str
                                    },
                                    "protocol-name": str
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

    # Main Schema
    schema = {
        Optional("@xmlns:junos"): str,
        "route-information": {
            Optional("@xmlns"): str,
            "route-table": ListOf({
                "active-route-count": str,
                "destination-count": str,
                "hidden-route-count": str,
                "holddown-route-count": str,
                Optional("rt"): ListOf({
                    Optional("@junos:style"): str,
                    "rt-destination": str,
                    "rt-entry": {
                        Optional("active-tag"): str,
                        "as-path": str,
                        Optional("local-preference"): str,
                        Optional("med"): str,
                        "nh": {
                            "to": str
                        },
                        "protocol-name": str
                    }
                }),
                "table-name": str,
                "total-route-count": str
            })
        }
    }

class ShowRouteReceiveProtocol(ShowRouteReceiveProtocolSchema):
    """ Parser for:
            * show route receive-protocol {protocol} {peer}
            * show route receive-protocol {protocol} {peer} {target}
    """

    cli_command = ['show route receive-protocol {protocol} {peer}',
                   'show route receive-protocol {protocol} {peer} {target}']
    def cli(self, protocol, peer, target=None, output=None):
        if not output:
            if target:
                cmd = self.cli_command[1].format(
                            protocol=protocol,
                            peer=peer,
                            target=target)
            else:
                cmd = self.cli_command[0].format(protocol=protocol,
                        peer=peer)
            out = self.device.execute(cmd)
        else:
            out = output
        
        ret_dict = {}
        
        # inet.0: 929 destinations, 1615 routes (929 active, 0 holddown, 0 hidden)
        p1 = re.compile(r'^(?P<table_name>\S+): +(?P<destination_count>\d+) +'
                        r'destinations, +(?P<total_route_count>\d+) +routes +'
                        r'\((?P<active_route_count>\d+) +active, +(?P<holddown_route_count>\d+) +'
                        r'holddown, +(?P<hidden_route_count>\d+) +hidden\)$')

        # * 10.220.0.0/16           Self                 12003   120        (65151 65000) I
        # 10.220.0.0/16           10.189.5.253         12003   120        (65151 65000) I
        # * 10.4.1.1/32              Self                                    I
        # * 10.36.3.3/32              Self                                    2 I     
        # * 192.168.225.0/24           10.64.4.4                      100        200000 4 5 6 I   
        p2 = re.compile(r'^((?P<active_tag>\*) +)?(?P<rt_destination>[\d\.\:\/]+) '
                        r'+(?P<to>\S+)( +(?P<med>\d+)? +(?P<local_preference>\d+))? '
                        r'+(?P<as_path>(\(([\S\s]+\)) +\w+)|([\d\s]+?\S))$')

        # * 2001:db8:3000::/48      2001:db8:7fc5:ca45::2 1000               65509 I
        # * 2001:db8:3000::/48      2001:db8:7fc5:ca45::2 1000     100       65509 I
        # * 2001:db8:3000::/48      2001:db8:7fc5:ca45::2          100       65509 I
        p2_1 = re.compile(r'^((?P<active_tag>\*) +)?(?P<rt_destination>[\d\w\:]+\/[\d]+) '
                          r'+(?P<to>\S+) (((?P<med>\d+)? +)(?P<local_preference>\d+)?)? '
                          r'+(?P<as_path>(\(([\S\s]+\)) +\w+)|([\d\s]+?\S))$')

        # 2001:db8:7fc5:ca45::1
        p3 = re.compile(r'^(?P<rt_destination>[\d\:\w\/]+)$')

        # *                         2001:db8:7fc5:ca45::4             100        I
        # *                         Self                 2       100        I
        p4 = re.compile(r'^((?P<active_tag>\*) +)?(?P<to>[\d\:\w]+)( +(?P<med>\d+)? +(?P<local_preference>\d+))? +(?P<as_path>(\(([\S\s]+\)) +\w+)|((\d\s)?\w))$')
                        

        for line in out.splitlines():
            line = line.strip()

            # inet.0: 929 destinations, 1615 routes (929 active, 0 holddown, 0 hidden)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                route_table_list = ret_dict.setdefault('route-information', {}). \
                    setdefault('route-table', [])
                route_table_dict = {k.replace('_', '-'):v for k, v in group.items() if v is not None}
                route_table_list.append(route_table_dict)
                continue
            
            # * 10.220.0.0/16           Self                 12003   120        (65151 65000) I
            # 10.220.0.0/16           10.189.5.253         12003   120        (65151 65000) I
            m = p2.match(line)
            if m:
                group = m.groupdict()
                rt_list = route_table_dict.setdefault('rt', [])
                rt_dict = {'rt-destination': group['rt_destination']}
                rt_entry_dict = rt_dict.setdefault('rt-entry', {})
                keys = ['active_tag', 'as_path', 'local_preference', 'med']
                for key in keys:
                    v = group[key]
                    if v:
                        rt_entry_dict.update({key.replace('_', '-'): v})
                nh_dict = rt_entry_dict.setdefault('nh', {})
                nh_dict.update({'to': group['to']})
                rt_entry_dict.update({'protocol-name': protocol.upper()})
                rt_list.append(rt_dict)
                continue

            m = p2_1.match(line)
            if m:
                group = m.groupdict()
                rt_list = route_table_dict.setdefault('rt', [])
                rt_dict = {'rt-destination': group['rt_destination']}
                rt_entry_dict = rt_dict.setdefault('rt-entry', {})
                keys = ['active_tag', 'as_path', 'local_preference', 'med']
                for key in keys:
                    v = group[key]
                    if v:
                        rt_entry_dict.update({key.replace('_', '-'): v})
                nh_dict = rt_entry_dict.setdefault('nh', {})
                nh_dict.update({'to': group['to']})
                rt_entry_dict.update({'protocol-name': protocol.upper()})
                rt_list.append(rt_dict)
                continue


            # 2001:db8:7fc5:ca45::1
            m = p3.match(line)
            if m:
                
                group = m.groupdict()

                rt_list = route_table_dict.setdefault('rt', [])
                rt_dict = {'rt-destination': group['rt_destination']}

            #  *                         Self                 2       100        I
            m = p4.match(line)
            if m:
                group = m.groupdict()
                rt_entry_dict = rt_dict.setdefault('rt-entry', {})
                keys = ['active_tag', 'as_path', 'local_preference', 'med']

                for key in keys:
                    if group[key]:
                        rt_entry_dict.update({key.replace('_', '-'): group[key]})

                nh_dict = rt_entry_dict.setdefault('nh', {})
                nh_dict.update({'to': group['to']})

                rt_entry_dict.update({'protocol-name': protocol.upper()})

                rt_list.append(rt_dict)

        return ret_dict

class ShowRouteAdvertisingProtocolSchema(MetaParser):
    """ Schema for:
            * show route advertising-protocol {protocol} {ip_address}
            * show route advertising-protocol {protocol} {neighbor} {route}
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
                                "as-path": str,
                                "bgp-metric-flags": str,
                                "local-preference": str,
                                "med": str,
                                "nh": {
                                    "to": str
                                },
                                "protocol-name": str
                            }
                        }
                    ],
                    "table-name": str,
                    "total-route-count": str
                }
            }
        }
    """

    # Main schema
    schema = {
        Optional("@xmlns:junos"): str,
        "route-information": {
            Optional("@xmlns"): str,
            "route-table": {
                "active-route-count": str,
                "destination-count": str,
                "hidden-route-count": str,
                "holddown-route-count": str,
                Optional('rt'): ListOf({
                    Optional("@junos:style"): str,
                    "rt-destination": str,
                    "rt-entry": {
                        Optional("active-tag"): str,
                        "as-path": str,
                        "bgp-metric-flags": str,
                        Optional("local-preference"): str,
                        Optional("med"): str,
                        "nh": {
                            "to": str
                        },
                        "protocol-name": str
                    }
                }),
                "table-name": str,
                "total-route-count": str
            }
        }
    }


class ShowRouteAdvertisingProtocol(ShowRouteAdvertisingProtocolSchema):
    """ Parser for:
            * show route advertising-protocol {protocol} {neighbor}
            * show route advertising-protocol {protocol} {neighbor} {route}
    """

    cli_command = [
        'show route advertising-protocol {protocol} {neighbor}',
        'show route advertising-protocol {protocol} {neighbor} {route}'
        ]
    def cli(self, protocol, neighbor, route=None, output=None):
        if not output:
            if route:
                cmd = self.cli_command[1].format(
                    protocol=protocol,
                    neighbor=neighbor,
                    route=route)
            else:
                cmd = self.cli_command[0].format(
                    protocol=protocol,
                    neighbor=neighbor)
            out = self.device.execute(cmd)
        else:
            out = output
        
        ret_dict = {}
        
        # inet.0: 929 destinations, 1615 routes (929 active, 0 holddown, 0 hidden)
        p1 = re.compile(r'^(?P<table_name>\S+): +(?P<destination_count>\d+) +'
                        r'destinations, +(?P<total_route_count>\d+) +routes +'
                        r'\((?P<active_route_count>\d+) +active, +(?P<holddown_route_count>\d+) +'
                        r'holddown, +(?P<hidden_route_count>\d+) +hidden\)$')

        # * 10.220.0.0/16           Self                 12003   120        (65151 65000) I
        # * 10.4.1.1/32              Self                                    I
        # * 10.36.3.3/32              Self                                    2 I
        # * 10.81.123.0/32        Self                                    67890 [1] I
        p2 = re.compile(r'((?P<active_tag>\*) +)?(?P<rt_destination>[\d\.\:\/]+)'
                        r' +(?P<to>\S+)( +(?P<med>\d+) +(?P<local_preference>\d+))? '
                        r'+(?P<as_path>[\s\S]+)')
        
        # 2001:db8:7fc5:ca45::1
        p3 = re.compile(r'^(?P<rt_destination>[\d\:\w\/]+)$')

        # *                         Self                 2       100        I
        p4 = re.compile(r'^((?P<active_tag>\*) +)?(?P<to>\S+)( +(?P<med>\d+)? +(?P<local_preference>\d+))? +(?P<as_path>(\(([\S\s]+\)) +\w+)|((\d\s)?\w))$')
        
        for line in out.splitlines():
            line = line.strip()

            # inet.0: 929 destinations, 1615 routes (929 active, 0 holddown, 0 hidden)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                route_table_dict = ret_dict.setdefault('route-information', {}). \
                    setdefault('route-table', {})
                route_table_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue
            
            # * 10.220.0.0/16           Self                 12003   120        (65151 65000) I
            m = p2.match(line)
            if m:
                group = m.groupdict()

                rt_list = route_table_dict.setdefault('rt', [])
                rt_dict = {'rt-destination': group['rt_destination']}
                rt_entry_dict = rt_dict.setdefault('rt-entry', {})
                keys = ['active_tag', 'as_path', 'local_preference', 'med']
                
                for key in keys:
                    if group[key]:
                        rt_entry_dict.update({key.replace('_', '-'): group[key]})

                nh_dict = rt_entry_dict.setdefault('nh', {})
                nh_dict.update({'to': group['to']})

                rt_entry_dict.update({'bgp-metric-flags': 'Nexthop Change'})
                rt_entry_dict.update({'protocol-name': protocol.upper()})

                rt_list.append(rt_dict)

            # 2001:db8:7fc5:ca45::1
            m = p3.match(line)
            if m:
                
                group = m.groupdict()

                rt_list = route_table_dict.setdefault('rt', [])
                rt_dict = {'rt-destination': group['rt_destination']}

            #  *                         Self                 2       100        I
            m = p4.match(line)
            if m:
                group = m.groupdict()
                rt_entry_dict = rt_dict.setdefault('rt-entry', {})
                keys = ['active_tag', 'as_path', 'local_preference', 'med']

                for key in keys:
                    if group[key]:
                        rt_entry_dict.update({key.replace('_', '-'): group[key]})

                nh_dict = rt_entry_dict.setdefault('nh', {})
                nh_dict.update({'to': group['to']})

                rt_entry_dict.update({'bgp-metric-flags': 'Nexthop Change'})
                rt_entry_dict.update({'protocol-name': protocol.upper()})

                rt_list.append(rt_dict)
        
        
        return ret_dict

class ShowRouteSummarySchema(MetaParser):
    """ Schema for:
            * show route summary
    """
    # schema = {
    #     Optional("@xmlns:junos"): str,
    #     "route-summary-information": {
    #         Optional("@xmlns"): str,
    #         "as-number": str,
    #         "route-table": [
    #             {
    #                 "active-route-count": str,
    #                 "destination-count": str,
    #                 "hidden-route-count": str,
    #                 "holddown-route-count": str,
    #                 "protocols": [
    #                     {
    #                         "active-route-count": str,
    #                         "protocol-name": str,
    #                         "protocol-route-count": str
    #                     }
    #                 ],
    #                 "table-name": str,
    #                 "total-route-count": str
    #             }
    #         ],
    #         "router-id": str
    #     }
    # }

    # Main Schema
    schema = {
        Optional("@xmlns:junos"): str,
        "route-summary-information": {
            Optional("@xmlns"): str,
            Optional("as-number"): str,
            "route-table": ListOf({
                "active-route-count": str,
                "destination-count": str,
                "hidden-route-count": str,
                "holddown-route-count": str,
                "protocols": ListOf({
                    "active-route-count": str,
                    "protocol-name": str,
                    "protocol-route-count": str
                }),
                "table-name": str,
                "total-route-count": str
            }),
            "router-id": str
        }
    }

class ShowRouteSummary(ShowRouteSummarySchema):
    """ Parser for:
            * show route summary
    """
    cli_command = 'show route summary'
    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        ret_dict = {}

        # Autonomous system number: 65171
        p1 = re.compile(r'^Autonomous +system +number: +(?P<as_number>\d+)$')

        # Router ID: 10.189.5.252
        p2 = re.compile(r'^Router +ID: +(?P<router_id>\S+)$')

        # inet.0: 929 destinations, 1615 routes (929 active, 0 holddown, 0 hidden)
        p3 = re.compile(r'^(?P<table_name>\S+): +(?P<destination_count>\d+) +'
                        r'destinations, +(?P<total_route_count>\d+) +routes +'
                        r'\((?P<active_route_count>\d+) +active, +(?P<holddown_route_count>\d+) +'
                        r'holddown, +(?P<hidden_route_count>\d+) +hidden\)$')
        
        #  Direct:      6 routes,      6 active
        p4 = re.compile(r'^(?P<protocol_name>\S+): +(?P<protocol_route_count>\d+) +'
                        r'routes, +(?P<active_route_count>\d+) +\w+$')

        for line in out.splitlines():
            line = line.strip()

            # Autonomous system number: 65171
            m = p1.match(line)
            if m:
                group = m.groupdict()
                route_summary_information_dict = ret_dict.setdefault('route-summary-information', {})
                route_summary_information_dict.update({
                    k.replace('_', '-'):v for k, v in group.items() 
                    if v is not None})
                continue

            # Router ID: 10.189.5.252
            m = p2.match(line)
            if m:
                group = m.groupdict()
                route_summary_information_dict = ret_dict.setdefault('route-summary-information', {})
                route_summary_information_dict.update({k.replace('_', '-'):
                    v for k, v in group.items() if v is not None})
                continue

            # inet.0: 929 destinations, 1615 routes (929 active, 0 holddown, 0 hidden)
            m = p3.match(line)
            if m:
                group = m.groupdict()
                route_table = route_summary_information_dict. \
                    setdefault('route-table', [])
                route_table_dict = {k.replace('_', '-'):
                    v for k, v in group.items() if v is not None}
                route_table.append(route_table_dict)
                continue
            
            #  Direct:      6 routes,      6 active
            m = p4.match(line)
            if m:
                group = m.groupdict()
                protocols_list = route_table_dict.setdefault('protocols', [])
                protocols_list.append({k.replace('_', '-'):
                    v for k, v in group.items() if v is not None})
                continue

        return ret_dict

class ShowRouteInstanceDetailSchema(MetaParser):
    """ Schema for:
            * show route instance detail
    """
    # schema = {
    #     Optional("@xmlns:junos"): str,
    #     "instance-information": {
    #         Optional("@junos:style"): str,
    #         Optional("@xmlns"): str,
    #         "instance-core": [
    #             {
    #                 "instance-interface": [
    #                     {
    #                         "interface-name": str
    #                     }
    #                 ],
    #                 "instance-name": str,
    #                 "instance-rib": [
    #                     {
    #                         "irib-active-count": str,
    #                         "irib-hidden-count": str,
    #                         "irib-holddown-count": str,
    #                         "irib-name": str,
    #                         "irib-route-count": str
    #                     }
    #                 ],
    #                 "instance-state": str,
    #                 "instance-type": str,
    #                 "router-id": str
    #             }
    #         ]
    #     }
    # }


    schema = {
        Optional("@xmlns:junos"): str,
        "instance-information": {
            Optional("@junos:style"): str,
            Optional("@xmlns"): str,
            "instance-core": ListOf({
                Optional("instance-interface"): ListOf({
                    "interface-name": str
                }),
                "instance-name": str,
                Optional("instance-rib"): ListOf({
                    "irib-active-count": str,
                    "irib-hidden-count": str,
                    "irib-holddown-count": str,
                    "irib-name": str,
                    "irib-route-count": str
                }),
                Optional("instance-state"): str,
                Optional("instance-type"): str,
                Optional("router-id"): str
            })
        }
    }

class ShowRouteInstanceDetail(ShowRouteInstanceDetailSchema):
    """ Parser for:
            * show route instance detail
    """
    cli_command = 'show route instance detail'
    
    def cli(self, output=None):
        if not output:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}
        # Router ID: 0.0.0.0
        p1 = re.compile(r'^Router +ID: +(?P<router_id>\S+)$')

        # Type: forwarding        State: Active        
        p2 = re.compile(r'^Type: +(?P<instance_type>\S+) +State: +(?P<instance_state>\S+)$')

        # Tables:
        p3 = re.compile(r'^Tables:$')

        # Interfaces:
        p4 = re.compile(r'^Interfaces:$')

        # inet.0                 : 1615 routes (929 active, 0 holddown, 0 hidden)
        # __juniper_private1__.inet.0: 6 routes (5 active, 0 holddown, 0 hidden)
        p5 = re.compile(r'^(?P<irib_name>\S+) *: +(?P<irib_route_count>\d+) +'
                r'routes +\((?P<irib_active_count>\d+) +active, +'
                r'(?P<irib_holddown_count>\d+) +holddown, +'
                r'(?P<irib_hidden_count>\d+) +hidden\)$')

        # master:
        p6 = re.compile(r'^(?P<instance_name>\S+):$')

        # pfh-0/0/0.16383
        p7 = re.compile(r'^(?P<interface_name>\S+)$')


        for line in out.splitlines():
            line = line.strip()

            # Router ID: 0.0.0.0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                instance_core_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # Type: forwarding        State: Active        
            m = p2.match(line)
            if m:
                group = m.groupdict()
                instance_core_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # Tables:
            m = p3.match(line)
            if m:
                continue

            # Interfaces:
            m = p4.match(line)
            if m:
                instance_interface_list = instance_core_dict.setdefault('instance-interface', [])
                continue

            # inet.0                 : 1615 routes (929 active, 0 holddown, 0 hidden)
            # __juniper_private1__.inet.0: 6 routes (5 active, 0 holddown, 0 hidden)
            m = p5.match(line)
            if m:
                group = m.groupdict()
                instance_rib_list = instance_core_dict.setdefault('instance-rib', [])
                instance_rib_list.append({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # master:
            m = p6.match(line)
            if m:
                group = m.groupdict()
                instance_core_list = ret_dict.setdefault('instance-information', {}). \
                    setdefault('instance-core', [])
                instance_core_dict = {k.replace('_', '-'):v for k, v in group.items() if v is not None}
                instance_core_list.append(instance_core_dict)
                continue

            # pfh-0/0/0.16383
            m = p7.match(line)
            if m:
                group = m.groupdict()
                instance_interface_list.append({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue
        return ret_dict

class ShowRouteAdvertisingProtocolDetailSchema(MetaParser):
    """ Schema for:
        * show route advertising-protocol {protocol} {ip_address} {route} detail
    """

    # schema = {
    #     Optional("@xmlns:junos"): str,
    #     "route-information":{
    #         Optional("@xmlns"): str,
    #         "route-table": [{
    #             Optional("@junos:style"): str,
    #             "table-name": str,
    #             "destination-count": str,
    #             "total-route-count": str,
    #             "active-route-count": str,
    #             "holddown-route-count": str,
    #             "hidden-route-count": str,
    #             "rt-entry": {
    #                 Optional('active-tag'): str,
    #                 "rt-destination": str,
    #                 "rt-prefix-length": str,
    #                 "rt-entry-count": str,
    #                 "rt-announced-count": str,
    #                 Optional('route-label'): str,
    #                 Optional("bgp-group"): {
    #                     "bgp-group-name": str,
    #                     "bgp-group-type": str,
    #                 },
    #                 "nh": {
    #                     "to": str,
    #                 },
    #                 "med": str,
    #                 "local-preference": str,
    #                 "as-path": str,
    #                 "communities": str,
    #                 "flags": str,
    #             }
    #         }],
    #     },
    # }

    # Main schema
    schema = {
        Optional("@xmlns:junos"): str,
        "route-information":{
            Optional("@xmlns"): str,
            "route-table": ListOf({
                Optional("@junos:style"): str,
                "table-name": str,
                "destination-count": str,
                "total-route-count": str,
                "active-route-count": str,
                "holddown-route-count": str,
                "hidden-route-count": str,
                "rt-entry": {
                    Optional('active-tag'): str,
                    "rt-destination": str,
                    "rt-prefix-length": str,
                    "rt-entry-count": str,
                    "rt-announced-count": str,
                    Optional('route-label'): str,
                    Optional("bgp-group"): {
                        "bgp-group-name": str,
                        "bgp-group-type": str,
                    },
                    "nh": {
                        "to": str,
                    },
                    Optional("med"): str,
                    Optional("local-preference"): str,
                    'as-path': str,
                    Optional("communities"): str,
                    Optional("flags"): str,
                }
            }),
        },
    }

class ShowRouteAdvertisingProtocolDetail(ShowRouteAdvertisingProtocolDetailSchema):
    """ Schema for:
        * show route advertising-protocol {protocol} {ip_address} {route} detail
    """

    cli_command = 'show route advertising-protocol {protocol} {ip_address} {route} detail'
    def cli(self, protocol, ip_address, route, output=None):
        if not output:
            cmd = self.cli_command.format(protocol=protocol,
                    ip_address=ip_address, route=route)
            out = self.device.execute(cmd)
        else:
            out = output

        ret_dict = {}

        # inet.0: 60 destinations, 66 routes (60 active, 1 holddown, 0 hidden)
        p1 = re.compile(r'^(?P<table_name>[^:]+): +(?P<destination_count>\d+) +'
                        r'destinations, +(?P<total_route_count>\d+) +'
                        r'routes +\((?P<active_route_count>\d+) +'
                        r'active, +(?P<holddown_route_count>\d+) +'
                        r'holddown, +(?P<hidden_route_count>\d+) +hidden\)$')

        # * 10.36.255.252/32 (1 entry, 1 announced)
        # * 2001:3/128 (2 entries, 2 announced)
        p2 = re.compile(r'^(?P<active_tag>\*)? *(?P<rt_destination>[\s\S]+)'
                        r'/(?P<rt_prefix_length>\d+)'
                        r' +\((?P<rt_entry_count>\d+) +\S+, +'
                        r'(?P<rt_announced_count>\d+) +announced\)$')

        # BGP group lacGCS001 type External
        p3 = re.compile(r'^BGP group +(?P<bgp_group_name>\S+)'
                        r' +type +(?P<bgp_group_type>Internal|External)$')

        # Route Label: 118071
        p4 = re.compile(r'^Route Label: +(?P<route_label>\S+)$')

        # Nexthop: 10.189.5.252
        p5 = re.compile(r'^Nexthop: +(?P<to>\S+)$')

        # MED: 29012
        p6 = re.compile(r'^MED: +(?P<med>\S+)$')

        # Localpref: 4294967285
        p7 = re.compile(r'^Localpref: +(?P<local_preference>\S+)$')

        # AS path: [65151] (65171) I
        p8 = re.compile(r'^AS +path: +(?P<as_path>.*)$')


        # Communities: 65151:65109
        # Communities: 2:2 4:4 no-export
        p9 = re.compile(r'^Communities: +(?P<communities>[\s\S]+)$')

        # Flags: Nexthop Change
        p10 = re.compile(r'^Flags: +(?P<flags>.*)$')


        for line in out.splitlines():
            line = line.strip()

            # inet.0: 60 destinations, 66 routes (60 active, 1 holddown, 0 hidden)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                route_list = ret_dict.setdefault('route-information', {}). \
                    setdefault('route-table', [])
                protocol_dict = {}
                route_list.append(protocol_dict)
                protocol_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # * 10.36.255.252/32 (1 entry, 1 announced)
            m = p2.match(line)
            if m:
                group = m.groupdict()
                rt_entry_dict = protocol_dict.setdefault('rt-entry', {})
                rt_entry_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # BGP group lacGCS001 type External
            m = p3.match(line)
            if m:
                group = m.groupdict()
                bgp_dict = rt_entry_dict.setdefault('bgp-group', {})
                bgp_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            # Route Label: 118071
            m = p4.match(line)
            if m:
                group = m.groupdict()
                rt_entry_dict.update({'route-label': group['route_label']})
                continue

            # Nexthop: 10.189.5.252
            m = p5.match(line)
            if m:
                group = m.groupdict()
                nh_dict = rt_entry_dict.setdefault('nh', {})
                nh_dict.update({'to': group['to']})
                continue

            # MED: 29012
            m = p6.match(line)
            if m:
                group = m.groupdict()
                rt_entry_dict.update({'med': group['med']})
                continue

            # Localpref: 4294967285
            m = p7.match(line)
            if m:
                group = m.groupdict()
                rt_entry_dict.update({'local-preference': group['local_preference']})
                continue

            # AS path: [65151] (65171) I
            m = p8.match(line)
            if m:
                group = m.groupdict()
                rt_entry_dict.update({'as-path': group['as_path']})
                continue

            # Communities: 65151:65109
            m = p9.match(line)
            if m:
                group = m.groupdict()
                rt_entry_dict.update({'communities': group['communities']})
                continue

            # Flags: Nexthop Change
            m = p10.match(line)
            if m:
                group = m.groupdict()
                rt_entry_dict.update({'flags': group['flags']})
                continue

        return ret_dict

class ShowRouteForwardingTableLabelSchema(MetaParser):
    """ Schema for:
        * show route forwarding-table label {label}
    """

    # Main schema
    schema = {
            "forwarding-table-information":{
                "route-table": ListOf({
                    "table-name": str,
                    "address-family": str,
                    Optional("enabled-protocols"): str,
                    "rt-entry": ListOf({
                        "rt-destination": str,
                        "destination-type": str,
                        "route-reference-count": str,
                        "nh":{
                            Optional("to"): str,
                            "nh-type": str,
                            "nh-index": str,
                            "nh-reference-count": str,
                            Optional("nh-lb-label"): str,
                            Optional("via"): str,
                        }
                    })
                })
            }
        }

class ShowRouteForwardingTableLabel(ShowRouteForwardingTableLabelSchema):
    """ Schema for:
        * show route forwarding-table label {label}
    """

    cli_command = 'show route forwarding-table label {label}'
    def cli(self, label, output=None):
        if not output:
            out = self.device.execute(
                self.cli_command.format(label=label))
        else:
            out = output

        ret_dict = {}

        # Routing table: default.mpls
        # Routing table: __mpls-oam__.mpls
        p1 = re.compile(r'^Routing +table: +(?P<table_name>\S+)$')

        # MPLS:
        p2 = re.compile(r'^(?P<address_family>[^\s:]+):$')

        # Enabled protocols: Bridging, Single VLAN, Dual VLAN,
        p3 = re.compile(r'^Enabled +protocols: +(?P<enabled_protocols>.*)$')

        # Destination        Type RtRef Next hop           Type Index    NhRef Netif
        p4 = re.compile(r'^Destination +Type +RtRef +Next hop +Type Index  +NhRef +Netif$')

        # 16                 user     0 10.169.14.158    Pop        578     2 ge-0/0/0.0
        # 16(S=0)            user     0 10.169.14.158    Pop        579     2 ge-0/0/0.0
        # 16(S=0) user 0 2001:AE Pop 579 2 ge-0/0/0.0
        # default            perm     0                    dscd      535     1
        # 575                user     0 192.168.145.218   Swap 526      590     2 ge-0/0/1.0
        p5 = re.compile(r'^(?P<rt_destination>\S+) +(?P<destination_type>\S+) +'
                        r'(?P<route_reference_count>\d+) +(?P<to>[\d\.|\d\:a-fA-F]+)? +'
                        r'(?P<nh_type>\S+( \S+)?) +(?P<nh_index>\d+) +'
                        r'(?P<nh_reference_count>\d+)( +)?(?P<via>\S+)?$')


        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                route_table_list = ret_dict.setdefault(
                    'forwarding-table-information', {}).setdefault('route-table', [])
                route_table_dict = {}
                route_table_list.append(route_table_dict)
                route_table_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                route_table_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                route_table_dict.update({k.replace('_', '-'):v for k, v in group.items() if v is not None})
                continue

            m = p4.match(line)
            if m:
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                route_entry_list = route_table_dict.setdefault('rt-entry', [])
                route_entry_dict = {}

                route_entry_dict['rt-destination'] = group.pop('rt_destination')
                route_entry_dict['destination-type'] = group.pop('destination_type')
                route_entry_dict['route-reference-count'] = group.pop('route_reference_count')

                route_entry_dict['nh'] = {k.replace('_', '-'):v for k, v in group.items() if v is not None}

                route_entry_list.append(route_entry_dict)

        return ret_dict


class ShowRouteTableLabelSwitchedNameSchema(MetaParser):
    """ Schema for:
        * show route table {table} label-switched-path {name}
    """

    schema = {
            "route-information": {
                "route-table": {
                    "table-name": str,
                    "destination-count": str,
                    "total-route-count": str,
                    "active-route-count": str,
                    "holddown-route-count": str,
                    "hidden-route-count": str,
                    "rt": ListOf({
                        "rt-destination": str,
                        "rt-entry": ListOf({
                            Optional("active-tag"): str,
                            Optional("current-active"): str,
                            Optional("last-active"): str,
                            "protocol-name": str,
                            "preference": str,
                            "preference2": str,
                            "age": {
                                '#text': str,
                                Optional('@junos:seconds'): str,
                            },
                            "metric": str,
                            "nh": ListOf({
                                Optional("selected-next-hop"): bool,
                                "to": str,
                                "via": str,
                                "lsp-name": str,
                            })
                        })
                    })
                }
            }
        }

class ShowRouteTableLabelSwitchedName(ShowRouteTableLabelSwitchedNameSchema):
    """ Parser for:
        * show route table {table} label-switched-path {name}
    """

    cli_command = ['show route table {table} label-switched-path {name}']

    def cli(self, table, name, output=None):

        if not output:
            out = self.device.execute(self.cli_command[0].format(
                table=table,
                name=name
            ))
        else:
            out = output
        
        ret_dict = {}

        # mpls.0: 36 destinations, 36 routes (36 active, 0 holddown, 0 hidden)
        p1 = re.compile(r'^(?P<table_name>[^\s:]+): +(?P<destination_count>\d+) +'
                        r'destinations, +(?P<total_route_count>\d+) +routes +'
                        r'\((?P<active_route_count>\d+) +active, +'
                        r'(?P<holddown_route_count>\d+) +holddown, +'
                        r'(?P<hidden_route_count>\d+) +hidden\)$')

        # 46                 *[RSVP/7/1] 00:10:22, metric 1
        p2 = re.compile(r'^(?P<rt_destination>\S+) +(?P<active_tag>\*)?'
                        r'\[(?P<protocol_name>[^\s/]+)/(?P<preference>\d+)/(?P<preference2>\d+)\] +'
                        r'(?P<age>[\d:]+), +metric +(?P<metric>\d+)$')

        # >  to 192.168.145.218 via ge-0/0/1.1, label-switched-path test_lsp_01
        p3 = re.compile(r'^(?P<selected_next_hop>\> +)?to +(?P<to>\S+) +via +'
                        r'(?P<via>[^\s,]+), +label-switched-path +(?P<lsp_name>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            # mpls.0: 36 destinations, 36 routes (36 active, 0 holddown, 0 hidden)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                route_table_dict = ret_dict.setdefault('route-information', {}).setdefault('route-table', {})
                route_table_dict.update(
                    {k.replace('_', '-'):v for k, v in group.items() if v is not None}
                )

            # 46                 *[RSVP/7/1] 00:10:22, metric 1
            m = p2.match(line)
            if m:
                group = m.groupdict()
                rt_list = route_table_dict.setdefault('rt', [])
                rt_dict = {
                    'rt-destination': group.pop('rt_destination')
                }
                rt_entry_list = rt_dict.setdefault('rt-entry', [])
                rt_entry_dict = {
                    'age': {'#text': group.pop('age')}
                }
                rt_entry_dict.update(
                    {k.replace('_', '-'):v for k, v in group.items() if v is not None}
                )
                rt_entry_list.append(rt_entry_dict)
                rt_list.append(rt_dict)


            # >  to 192.168.145.218 via ge-0/0/1.1, label-switched-path test_lsp_01
            m = p3.match(line)
            if m:
                group = m.groupdict()
                nh_list = rt_entry_dict.setdefault('nh', [])
                nh_dict = {
                    'selected-next-hop': True if group.pop('selected_next_hop', None) else False
                }
                nh_dict.update(
                    {k.replace('_', '-'):v for k, v in group.items() if v is not None}
                )
                nh_list.append(nh_dict)


        return ret_dict


class ShowRouteProtocolProtocolExtensiveIpaddressSchema(MetaParser):

    """ Schema for:
            * show route protocol {protocol} extensive {ipaddress}
    """
    schema = {
        "route-information": {
            "route-table": {
                "active-route-count": str,
                "destination-count": str,
                "hidden-route-count": str,
                "holddown-route-count": str,
                "rt": {
                    "rt-announced-count": str,
                    "rt-destination": str,
                    "rt-entry": {
                        "active-tag": str,
                        "age": {
                            "#text": str
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
                        "bgp-rt-flag": str,
                        "gateway": str,
                        "local-as": str,
                        "local-preference": str,
                        "nh": {
                            "nh-string": str,
                            "session": str,
                            "to": str,
                            "via": str
                        },
                        "nh-address": str,
                        "nh-index": str,
                        Optional("nh-kernel-id"): str,
                        "nh-reference-count": str,
                        "nh-type": str,
                        "peer-as": str,
                        "peer-id": str,
                        "preference": str,
                        "preference2": str,
                        "protocol-name": str,
                        "rt-entry-state": str,
                        "task-name": str,
                        "validation-state": str
                    },
                    "rt-entry-count": {
                        "#text": str
                    },
                    "rt-prefix-length": str,
                    "tsi": {
                        "#text": str
                    }
                },
                "table-name": str,
                "total-route-count": str
            }
        }
    }


class ShowRouteProtocolProtocolExtensiveIpaddress(ShowRouteProtocolProtocolExtensiveIpaddressSchema):
    """ Parser for:
        * show route protocol {protocol} extensive {ipaddress}
    """

    cli_command = 'show route protocol {protocol} extensive {ipaddress}'

    def cli(self, protocol, ipaddress, output=None):

        if not output:
            out = self.device.execute(self.cli_command.format(
                protocol=protocol,
                ipaddress=ipaddress
            ))
        else:
            out = output
        
        ret_dict = {}

        # inet.0: 8 destinations, 8 routes (8 active, 0 holddown, 0 hidden)
        p1 = re.compile(r'^(?P<table_name>\S+): +(?P<destination_count>\d+) +'
                        r'destinations, +(?P<total_route_count>\d+) +routes +'
                        r'\((?P<active_route_count>\d+) +active, +(?P<holddown_route_count>\d+) +'
                        r'holddown, +(?P<hidden_route_count>\d+) +hidden\)$')

        
        # 10.16.2.2/32 (1 entry, 1 announced)
        # 2001:db8:4885:2101::1/128 (1 entry, 1 announced)
        p2 = re.compile(r'^(?P<rt_destination>[\d\:\.]+)+\/+(?P<rt_prefix_length>\d+) +\((?P<text>\d+) +entry, +(?P<rt_announced_count>\d+) +announced\)$')

        # KRT in-kernel 10.16.2.2/32 -> {10.145.0.3}
        p3 = re.compile(r'^(?P<text>KRT +in-kernel+[\S\s]+)$')

        # *BGP Preference: 170/-101
        p4 = re.compile(r'^(?P<active_tag>\*)?(?P<protocol_name>\S+)\s+'
                        r'Preference:\s+(?P<preference>\d+)(\/(\-)?(?P<preference2>\d+))?$')

        # Next hop type: Router, Next hop index: 604
        p5 = re.compile(r'^Next +hop type: +(?P<nh_type>\S+), +Next +hop +'
                        r'index: +(?P<nh_index>\d+)$')

        # Address: 0xf991014
        p6 = re.compile(r'^Address: +(?P<nh_address>\S+)$')

        # Next-hop reference count: 2
        p7 = re.compile(r'^Next-hop +reference +count: +(?P<nh_reference_count>\d+)$')

        # Source: 10.145.0.3
        p8 = re.compile(r'^Source: +(?P<gateway>\S+)$')

        # Next hop: 10.145.0.3 via ge-0/0/0.0, selected
        p9 = re.compile(r'^(?P<nh_string>Next hop):( +(?P<to>\S+))? '
                        r'+via +(?P<via>\S+), +selected$')

        # Session Id: 0xe78
        p10 = re.compile(r'^Session +Id: +(?P<session>\S+)$')

        # State: <Active Ext>
        p11 = re.compile(r'State: +\<(?P<rt_entry_state>[\S\s]+)\>$')

        # Local AS:     1 Peer AS: 30000
        p12 = re.compile(r'^Local +AS: +(?P<local_as>\d+) +Peer +AS: +(?P<peer_as>\d+)$')

        # Age: 7:14:16
        p13 = re.compile(r'^Age: +(?P<text>[\d\:]+)$')

        # Validation State: unverified 
        p14 = re.compile(r'^Validation +State: +(?P<validation_state>\S+)$')

        # Task: BGP_30000.10.145.0.3
        p15 = re.compile(r'^Task: +(?P<task_name>\S+)$')

        # Announcement bits (1): 0-KRT
        p16 = re.compile(r'^Announcement +bits +\((?P<announce_bits>\d+)\): '
                         r'+(?P<announce_tasks>[\S\s]+)$')

        # AS path: I 
        p17 = re.compile(r'^(?P<aspath_effective_string>AS +path:) +(?P<attr_value>[\d\w\s]+)$')

        # Accepted 
        p18 = re.compile(r'^(?P<bgp_rt_flag>\w+)$')

        # Localpref: 100 
        p19 = re.compile(r'^Localpref: +(?P<local_preference>\d+)$')

        # Router ID: 10.16.2.2
        p20 = re.compile(r'^Router +ID: +(?P<peer_id>[\d\.]+)$')

        for line in out.splitlines():
            line = line.strip()

            # inet.0: 8 destinations, 8 routes (8 active, 0 holddown, 0 hidden)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                route_table_dict = ret_dict.setdefault('route-information', {}).setdefault('route-table', {})
                route_table_dict.update(
                    {k.replace('_', '-'):v for k, v in group.items() if v is not None}
                )
                rt_entry_dict = None
                continue

            # 10.16.2.2/32 (1 entry, 1 announced)
            m = p2.match(line)
            if m:
                group = m.groupdict()
                rt_dict = {}
                rt_entry_count_dict = {}
                
                for group_key, group_value in m.groupdict().items():
                    if(group_key != 'text'):
                        entry_key = group_key.replace('_', '-')
                        rt_dict[entry_key] = group_value
                    else:
                        rt_entry_count_dict['#text'] = group_value
                        rt_dict['rt-entry-count'] = rt_entry_count_dict
                
                continue

            # KRT in-kernel 10.16.2.2/32 -> {10.145.0.3}
            m = p3.match(line)
            if m:
                group = m.groupdict()
                tsi_dict = {}
                tsi_dict['#text'] = group['text']
                rt_dict['tsi'] = tsi_dict

                continue

            # *BGP Preference: 170/-101
            m = p4.match(line)
            if m:
                group = m.groupdict()
                if rt_entry_dict == None:
                    rt_entry_dict = {}
                rt_entry_dict['active-tag'] = group['active_tag']
                rt_entry_dict['preference'] = group['preference']
                rt_entry_dict['preference2'] = group['preference2']
                rt_entry_dict['protocol-name'] = group['protocol_name']

                continue

            # Next hop type: Router, Next hop index: 604
            m = p5.match(line)
            if m:
                group = m.groupdict()
                for group_key, group_value in m.groupdict().items():
                    entry_key = group_key.replace('_', '-')
                    rt_entry_dict[entry_key] = group_value

                continue

            # Address: 0xf991014
            m = p6.match(line)
            if m:
                group = m.groupdict()
                for group_key, group_value in m.groupdict().items():
                    entry_key = group_key.replace('_', '-')
                    rt_entry_dict[entry_key] = group_value
                
                continue

            # Next-hop reference count: 2
            m = p7.match(line)
            if m:
                group = m.groupdict()
                for group_key, group_value in m.groupdict().items():
                    entry_key = group_key.replace('_', '-')
                    rt_entry_dict[entry_key] = group_value

                continue

            # Source: 10.145.0.3
            m = p8.match(line)
            if m:
                group = m.groupdict()
                for group_key, group_value in m.groupdict().items():
                    entry_key = group_key.replace('_', '-')
                    rt_entry_dict[entry_key] = group_value

                continue

            # Next hop: 10.145.0.3 via ge-0/0/0.0, selected
            m = p9.match(line)
            if m:
                group = m.groupdict()
                nh_dict = {}
                for group_key, group_value in m.groupdict().items():
                    entry_key = group_key.replace('_', '-')
                    nh_dict[entry_key] = group_value

                continue

            # Session Id: 0xe78
            m = p10.match(line)
            if m:
                group = m.groupdict()
                for group_key, group_value in m.groupdict().items():
                    entry_key = group_key.replace('_', '-')
                    nh_dict[entry_key] = group_value
                
                rt_entry_dict['nh'] = nh_dict
                
                continue

            # State: <Active Ext>
            m = p11.match(line)
            if m:
                if rt_entry_dict == None:
                    rt_entry_dict = {}
                group = m.groupdict()
                for group_key, group_value in m.groupdict().items():
                    entry_key = group_key.replace('_', '-')
                    rt_entry_dict[entry_key] = group_value
                
                continue

            # Local AS:     1 Peer AS: 30000
            m = p12.match(line)
            if m:
                group = m.groupdict()
                for group_key, group_value in m.groupdict().items():
                    entry_key = group_key.replace('_', '-')
                    rt_entry_dict[entry_key] = group_value

                continue

            # Age: 7:14:16
            m = p13.match(line)
            if m:
                group = m.groupdict()
                age = {}
                age['#text'] = group['text']
                rt_entry_dict['age'] = age

                continue

            # Validation State: unverified
            m = p14.match(line)
            if m:
                group = m.groupdict()
                for group_key, group_value in m.groupdict().items():
                    entry_key = group_key.replace('_', '-')
                    rt_entry_dict[entry_key] = group_value

                continue

            # Task: BGP_30000.10.145.0.3
            m = p15.match(line)
            if m:
                group = m.groupdict()
                for group_key, group_value in m.groupdict().items():
                    entry_key = group_key.replace('_', '-')
                    rt_entry_dict[entry_key] = group_value

                continue

            # Announcement bits (1): 0-KRT
            m = p16.match(line)
            if m:
                group = m.groupdict()
                for group_key, group_value in m.groupdict().items():
                    entry_key = group_key.replace('_', '-')
                    rt_entry_dict[entry_key] = group_value

                continue

            # AS path: I 
            m = p17.match(line)
            if m:
                group = m.groupdict()
                attr_as_path_effective_dict = {}
                for group_key, group_value in m.groupdict().items():
                    entry_key = group_key.replace('_', '-')
                    attr_as_path_effective_dict[entry_key] = group_value
                attr_dict = {}
                attr_dict['attr-as-path-effective'] = attr_as_path_effective_dict
                rt_entry_dict['bgp-path-attributes'] = attr_dict

                rt_entry_dict['as-path'] = group['aspath_effective_string'] + group['attr_value']

                continue

            # Accepted 
            m = p18.match(line)
            if m:
                group = m.groupdict()
                for group_key, group_value in m.groupdict().items():
                    if group_key == 'bgp_rt_flag':
                        entry_key = group_key.replace('_', '-')
                        rt_entry_dict[entry_key] = group_value

                continue

            # Localpref: 100 
            m = p19.match(line)
            if m:
                group = m.groupdict()
                for group_key, group_value in m.groupdict().items():
                    entry_key = group_key.replace('_', '-')
                    rt_entry_dict[entry_key] = group_value

                continue

            # Router ID: 10.16.2.2 
            m = p20.match(line)
            if m:
                group = m.groupdict()
                for group_key, group_value in m.groupdict().items():
                    entry_key = group_key.replace('_', '-')
                    rt_entry_dict[entry_key] = group_value

                rt_dict['rt-entry'] = rt_entry_dict
                route_table_dict['rt'] = rt_dict

                continue

        return ret_dict

# Schema for 
#   *'show route receive-protocol bgp {peer_address} {target_address} extensive'
class ShowRouteReceiveProtocolExtensiveSchema(MetaParser):
    """ Schema for:
            * 'show route receive-protocol bgp {peer_address} {target_address} extensive'
    """

    # Main Schema
    schema = {
        "route-information": {
            Optional("@xmlns"): str,
            "route-table": ListOf({
                "active-route-count": str,
                "destination-count": str,
                "hidden-route-count": str,
                "holddown-route-count": str,
                Optional("rt"): {
                        Optional("@junos:style"): str,
                        "rt-announced-count": str,
                        "rt-destination": str,
                        Optional("active-tag"): str,
                        Optional("rt-entry"): {
                            Optional("as-path"): str,
                            Optional("bgp-rt-flag"): str,
                            Optional("bgp-path-attributes"): {
                                "attr-as-path-effective": {
                                    "aspath-effective-string": str,
                                    "attr-value": str
                                }
                            },
                            Optional("local-preference"): str,
                            Optional("nh"): {
                                'to': str,
                            }
                        },
                        "rt-entry-count": {
                            "#text": str,
                        },
                        Optional("rt-prefix-length"): str,
                        Optional("rt-state"): str,
                    },
                "table-name": str,
                "total-route-count": str
            })
        }
    }

# Parser for 'show route receive-protocol bgp {peer_address} {target_address} extensive'
class ShowRouteReceiveProtocolExtensive(ShowRouteReceiveProtocolExtensiveSchema):
    cli_command = ['show route receive-protocol {protocol} {peer_address} {target_address} extensive']

    def cli(self, peer_address, target_address, protocol='bgp', output=None):

        if not output:
            out = self.device.execute(self.cli_command[0].format(
                peer_address=peer_address,
                target_address=target_address,
                protocol=protocol
            ))
        else:
            out = output

        ret_dict = {}

        # inet.0: 929 destinations, 1615 routes (929 active, 0 holddown, 0 hidden)
        p1 = re.compile(r'^(?P<table_name>\S+): +(?P<destination_count>\d+) +'
                        r'destinations, +(?P<total_route_count>\d+) +routes +'
                        r'\((?P<active_route_count>\d+) +active, +(?P<holddown_route_count>\d+) +'
                        r'holddown, +(?P<hidden_route_count>\d+) +hidden\)$')

        # 0.0.0.0/0 (1 entry, 1 announced)
        # * 10.60.1.0/24 (1 entry, 1 announced)
        # * 2001:db8:4401:19::/64 (1 entry, 1 announced)
        p2 = re.compile(r'^(?P<active_tag>\*)? *(?P<rt_destination>[\w.:]+)(\/(?P<rt_prefix_length>\d+))? +'
                        r'\((?P<format>(?P<text>\d+) +(entry|entries)), +(?P<rt_announced_count>\d+) +announced\)$')        

        # Accepted
        p3 = re.compile(r'^(?P<bgp_rt_flag>Accepted)$')

        # Nexthop: 10.64.4.4
        p4 = re.compile(r'^Nexthop: +(?P<to>[0-9a-f.:]+)$')

        # Localpref: 100
        p5 = re.compile(r'^Localpref: +(?P<local_preference>\d+)$')

        # AS path: I 
        # AS path: 30000 4 103 104 105 106 107 108 109 I
        p6 = re.compile(r'^(?P<aspath_effective_string>AS +path:) +(?P<attr_value>([\S]+( +)?)+)$')        

        for line in out.splitlines():
            line = line.strip()     

            # inet.0: 929 destinations, 1615 routes (929 active, 0 holddown, 0 hidden)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                route_table = ret_dict.setdefault('route-information', {}). \
                    setdefault('route-table', [])
                route_table_dict = {k.replace('_', '-'):
                    v for k, v in group.items() if v is not None}
                route_table.append(route_table_dict)
                continue

            # 0.0.0.0/0 (1 entry, 1 announced)
            # * 10.60.1.0/24 (1 entry, 1 announced)
            m = p2.match(line)
            if m:
                group = m.groupdict()                
                rt_dict = route_table_dict.setdefault('rt', {})

                for k in ['active_tag', 'rt_destination', 'rt_prefix_length', 'rt_announced_count']:
                    if group[k]:
                        rt_dict[k.replace('_', '-')] = group[k]

                rt_entry_count_dict = rt_dict.setdefault('rt-entry-count', {})
                rt_entry_count_dict['#text'] = group['text']
                
                continue               

            # Accepted
            m = p3.match(line)
            if m:
                rt_entry_exist = rt_dict.get('rt-entry', None)

                if not rt_entry_exist:
                    rt_entry_dict = rt_dict.setdefault('rt-entry', {})
                
                rt_entry_dict['bgp-rt-flag'] = m.groupdict()['bgp_rt_flag']
                continue
            
            # Nexthop: 10.64.4.4
            m = p4.match(line) 
            if m:
                group = m.groupdict()
                
                nh_dict = rt_entry_dict.setdefault('nh', {})
                nh_dict['to'] = group['to']
                continue
            
            # Localpref: 100
            m = p5.match(line)
            if m:
                rt_entry_dict['local-preference'] = m.groupdict()['local_preference']
                continue      

            # AS path: I 
            m = p6.match(line)
            if m:
                rt_entry_exist = rt_dict.get('rt-entry', None)
                if rt_entry_exist:
                    group = m.groupdict()
                    attr_as_path_dict = rt_entry_dict.setdefault('bgp-path-attributes', {}). \
                                        setdefault('attr-as-path-effective', {})

                    rt_entry_dict['as-path'] = line

                    attr_as_path_dict.update({
                        'aspath-effective-string': group['aspath_effective_string'],
                        'attr-value': group['attr_value']})

                    continue 

        return ret_dict                 


# Schema for 
#   *'show route receive-protocol bgp {peer_address} extensive'
class ShowRouteReceiveProtocolPeerAddressExtensiveSchema(MetaParser):
    """ Schema for:
            * 'show route receive-protocol bgp {peer_address} extensive'
    """

    # Main Schema
    schema = {
        "route-information": {
            Optional("@xmlns"): str,
            "route-table": ListOf({
                "active-route-count": str,
                "destination-count": str,
                "hidden-route-count": str,
                "holddown-route-count": str,
                Optional("rt"): ListOf({
                    Optional("@junos:style"): str,
                    Optional("active-tag"): str,
                    "rt-announced-count": str,
                    "rt-destination": str,
                    Optional("rt-entry"): {
                        Optional("as-path"): str,
                        Optional("bgp-rt-flag"): str,
                        Optional("bgp-path-attributes"): {
                            "attr-as-path-effective": {
                                "aspath-effective-string": str,
                                "attr-value": str
                            }
                        },
                        Optional("local-preference"): str,
                        Optional("nh"): {
                            'to': str,
                        }
                    },
                    "rt-entry-count": {
                        "#text": str,
                    },
                    Optional("rt-prefix-length"): str,
                    Optional("rt-state"): str,
                }),
                "table-name": str,
                "total-route-count": str
            })
        }
    }

# Parser for 'show route receive-protocol bgp {peer_address} extensive'
class ShowRouteReceiveProtocolPeerAddressExtensive(ShowRouteReceiveProtocolPeerAddressExtensiveSchema):
    cli_command = 'show route receive-protocol {protocol} {peer_address} extensive'

    def cli(self, peer_address, protocol='bgp', output=None):

        if not output:
            out = self.device.execute(self.cli_command.format(
                peer_address=peer_address,
                protocol=protocol
            ))
        else:
            out = output

        ret_dict = {}

        # inet.0: 929 destinations, 1615 routes (929 active, 0 holddown, 0 hidden)
        p1 = re.compile(r'^(?P<table_name>\S+): +(?P<destination_count>\d+) +'
                        r'destinations, +(?P<total_route_count>\d+) +routes +'
                        r'\((?P<active_route_count>\d+) +active, +(?P<holddown_route_count>\d+) +'
                        r'holddown, +(?P<hidden_route_count>\d+) +hidden\)$')

        # 0.0.0.0/0 (1 entry, 1 announced)
        # * 192.168.115.0/24 (1 entry, 1 announced)
        p2 = re.compile(r'^(?P<active_tag>\* )?(?P<rt_destination>[0-9a-f.:]+)(\/(?P<rt_prefix_length>\d+))? +'
                        r'\((?P<format>(?P<text>\d+) +(entry|entries)), +(?P<rt_announced_count>\d+) +announced\)$')        

        # Accepted
        p3 = re.compile(r'^(?P<bgp_rt_flag>Accepted)$')

        # Nexthop: 10.64.4.4
        p4 = re.compile(r'^Nexthop: +(?P<to>[0-9a-f.:]+)$')

        # Localpref: 100
        p5 = re.compile(r'^Localpref: +(?P<local_preference>\d+)$')

        # AS path: I 
        # AS path: 30000 4 103 104 105 106 107 108 109 I
        p6 = re.compile(r'^(?P<aspath_effective_string>AS +path:) +(?P<attr_value>([\S]+( +)?)+)$')        

        for line in out.splitlines():
            line = line.strip()     

            # inet.0: 929 destinations, 1615 routes (929 active, 0 holddown, 0 hidden)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                route_table = ret_dict.setdefault('route-information', {}). \
                    setdefault('route-table', [])
                route_table_dict = {k.replace('_', '-'):
                    v for k, v in group.items() if v is not None}
                route_table.append(route_table_dict)
                continue

            # 0.0.0.0/0 (1 entry, 1 announced)
            m = p2.match(line)
            if m:
                group = m.groupdict()                
                rt_dict_list = route_table_dict.setdefault('rt', [])

                rt_dict = {}

                if group['active_tag']:
                    rt_dict['active-tag'] = group['active_tag']

                rt_dict['rt-announced-count'] = group['rt_announced_count']
                rt_dict['rt-destination'] = group['rt_destination']
                rt_dict['rt-prefix-length'] = group['rt_prefix_length']

                rt_entry_count_dict = rt_dict.setdefault('rt-entry-count', {})
                rt_entry_count_dict['#text'] = group['text']

                rt_dict_list.append(rt_dict)
                
                continue               

            # Accepted
            m = p3.match(line)
            if m:
                rt_entry_exist = rt_dict.get('rt-entry', None)

                if not rt_entry_exist:
                    rt_entry_dict = rt_dict.setdefault('rt-entry', {})
                
                rt_entry_dict['bgp-rt-flag'] = m.groupdict()['bgp_rt_flag']
                continue
            
            # Nexthop: 10.64.4.4
            m = p4.match(line) 
            if m:
                group = m.groupdict()
                
                nh_dict = rt_entry_dict.setdefault('nh', {})
                nh_dict['to'] = group['to']
                continue
            
            # Localpref: 100
            m = p5.match(line)
            if m:
                rt_entry_dict['local-preference'] = m.groupdict()['local_preference']
                continue      

            # AS path: I 
            m = p6.match(line)
            if m:
                rt_entry_exist = rt_dict.get('rt-entry', None)
                if rt_entry_exist:
                    group = m.groupdict()
                    attr_as_path_dict = rt_entry_dict.setdefault('bgp-path-attributes', {}). \
                                        setdefault('attr-as-path-effective', {})

                    rt_entry_dict['as-path'] = line

                    attr_as_path_dict.update({
                        'aspath-effective-string': group['aspath_effective_string'],
                        'attr-value': group['attr_value']})

                    continue 

        return ret_dict       


class ShowRouteInstanceNameSchema(MetaParser):
    """ Schema for:
            * show route instance {name}
    """

    # Main Schema
    schema = {
        "instance-information": {
            "instance-core": {
                "instance-name": str,
                "instance-type": str,
                Optional("instance-ribs"): ListOf({
                    "irib-name": str,
                    "irib-active-count": str,
                    "irib-holddown-count": str,
                    "irib-hidden-count": str,
                })
            }
        }
    }

class ShowRouteInstanceName(ShowRouteInstanceNameSchema):
    """Parser for
        * show route instance {name}
    """
    cli_command = 'show route instance {name}'

    def cli(self, name, output=None):

        if not output:
            out = self.device.execute(self.cli_command.format(
                name=name
            ))
        else:
            out = output

        ret_dict = {}

        # NF-TEST              non-forwarding 
        # VR-TEST001           virtual-router
        # VRF-TEST001          vrf
        p1 = re.compile(r'^(?P<instance_name>\S+) +(?P<instance_type>(non-forwarding|virtual-router|vrf))$')  

        # NF-TEST.inet.0                                  106/0/0
        p2 = re.compile(r'^(?P<irib_name>\S+) +(?P<irib_active_count>\d+)/'
                        r'(?P<irib_holddown_count>\d+)/(?P<irib_hidden_count>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # NF-TEST              non-forwarding 
            # VR-TEST001           virtual-router
            # VRF-TEST001          vrf
            m = p1.match(line)
            if m:
                group = m.groupdict()
                instance_core = ret_dict.setdefault('instance-information', {}).setdefault('instance-core', {})
                instance_core.update({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue

            # NF-TEST.inet.0                                  106/0/0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                instance_rib_list = instance_core.setdefault('instance-ribs', [])
                instance_rib_list.append({k.replace('_','-'):
                    v for k, v in group.items() if v is not None})
                continue


        return ret_dict       
