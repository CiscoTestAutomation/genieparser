"""show_rip.py

NXOS parser class for below command(s):
    show ip rip vrf all
    show ip rip route vrf all
    show ip rip interface vrf all
    show ipv6 rip vrf all
    show ipv6 rip route vrf all
    show ipv6 interface vrf all
"""
import xmltodict
import re

try:
    from ats import tcl
except Exception:
    pass

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, And, Default, Use

def regexp(expression):
    def match(value):
        if re.match(expression,value):
            return value
        else:
            raise TypeError("Value '%s' doesnt match regex '%s'"
                              %(value,expression))
    return match

class ShowIpRipSchema(MetaParser):
    """Schema for show ip rip vrf all"""
    schema = {'process':
                {regexp('rip-(.*)'):
                    {'vrf':
                        {Any():
                            {Optional('ripPort'): str,
                             'multicastGroup': str,
                             'adminDistance': str,
                             'updateTime': str,
                             'expiryTime': str,
                             'garbageCollectorTime': str,
                             'defaultMetric': str,
                             'maxPaths': str,
                             Optional('ripInterfaceList'): str,
                             'state': str,
                             'status': str,}
                        }
                    }
                }
            }


class ShowIpRipVrfAll(ShowIpRipSchema, MetaParser):
    """Parser for:
        show ip rip vrf all
        parser class implements detail parsing mechanisms for cli and xml output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).


    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        result = tcl.q.caas.abstract(device=self.device.handle,
                                     exec='show ip rip vrf all')

        #        # To leverage router_show parsers:
        #        result = tcl.q.router_show(device=device, cmd='show version')

        return tcl.cast_any(result[1])

    def xml(self):
        ''' parsing mechanism: xml

        Function xml() defines the xml type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        output =  tcl.q.caas.abstract(device=self.device.handle,
                                      exec='show ip rip vrf all | xml')
        result = tcl.cast_any(output[1])

        return result

class ShowIpv6RipVrfAll(MetaParser):
    """Parser for:
        show ipv6 rip vrf all
        parser class implements detail parsing mechanisms for cli and xml output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).


    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        result = tcl.q.caas.abstract(device=self.device.handle,
                                     exec='show ipv6 rip vrf all')

        #        # To leverage router_show parsers:
        #        result = tcl.q.router_show(device=device, cmd='show version')

        return tcl.cast_any(result[1])

    def xml(self):
        ''' parsing mechanism: xml

        Function xml() defines the xml type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        output =  tcl.q.caas.abstract(device=self.device.handle,
                                      exec='show ipv6 rip vrf all | xml')
        result = tcl.cast_any(output[1])

        return result

class ShowRunRip(MetaParser):
    """Parser for:
        show running-config rip
        parser class implements detail parsing mechanisms for cli and xml output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).


    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        result = tcl.q.caas.abstract(device=self.device.handle,
                                     exec='show running-config rip')

        #        # To leverage router_show parsers:
        #        result = tcl.q.router_show(device=device, cmd='show version')

        return tcl.cast_any(result[1])

    def xml(self):
        ''' parsing mechanism: xml

        Function xml() defines the xml type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        output =  tcl.q.caas.abstract(device=self.device.handle,
                                      exec='show running-config rip | xml')
        result = tcl.cast_any(output[1])

        return result

class ShowIpRipNeighborSchema(MetaParser):
    """Schema for show ip rip neighbor vrf all"""
    schema = {'interfaces': str,
              'process_id':
                  {regexp('rip-(.*)'):
                       {'vrf':
                            {Any():
                                 {'neighbors':
                                      {Any():
                                           {'bad_pkts_received': str,
                                            'bad_routes_received': str,
                                            'last_request_received': str,
                                            'last_request_sent': str,
                                            'last_response_received': str,
                                            'last_response_sent': str,
                                            'neighbor': str
                                           }
                                      },
                                  Optional('number_of_neighbors'): str
                                 }
                            }
                       }
                  }
             }

class ShowIpRipNeighborVrfAll(ShowIpRipNeighborSchema, MetaParser):
    """Parser for:
        show ip rip neighbor vrf all
        parser class implements detail parsing mechanisms for cli and xml output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).


    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        result = tcl.q.caas.abstract(device=self.device.handle,
                                     exec='show ip rip neighbor vrf all')

        #        # To leverage router_show parsers:
        #        result = tcl.q.router_show(device=device, cmd='show version')

        return tcl.cast_any(result[1])

    def xml(self):
        ''' parsing mechanism: xml

        Function xml() defines the xml type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        output =  tcl.q.caas.abstract(device=self.device.handle,
                                      exec='show ip rip neighbor vrf all | xml')
        result = tcl.cast_any(output[1])

        return result

class ShowIpv6RipNeighborVrfAll(ShowIpRipNeighborSchema, MetaParser):
    """Parser for:
        show ipv6 rip neighbor vrf all
        parser class implements detail parsing mechanisms for cli and xml output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).


    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        result = tcl.q.caas.abstract(device=self.device.handle,
                                     exec='show ipv6 rip neighbor vrf all')

        #        # To leverage router_show parsers:
        #        result = tcl.q.router_show(device=device, cmd='show version')

        return tcl.cast_any(result[1])

    def xml(self):
        ''' parsing mechanism: xml

        Function xml() defines the xml type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        output =  tcl.q.caas.abstract(device=self.device.handle,
                                      exec='show ipv6 rip neighbor vrf all | xml')
        result = tcl.cast_any(output[1])

        return result

class ShowIpRipInterfaceSchema(MetaParser):
    """Schema for show ip rip interface vrf all"""
    schema = {regexp('rip-(.*)'):
                {Any():
                     {Any():
                          {'address': str,
                           'admin': str,
                           'link': str,
                           'mask': str,
                           'metric': str,
                           'protocol': str,
                           'rip_state': str,
                           'split_horizon': str}
                     }
                }
            }


class ShowIpRipInterfaceVrfAll(ShowIpRipInterfaceSchema,MetaParser):
    """Parser for:
        show ip rip interface vrf all
        parser class implements detail parsing mechanisms for cli and xml output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).


    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        result = tcl.q.caas.abstract(device=self.device.handle,
                                     exec='show ip rip interface vrf all')

        #        # To leverage router_show parsers:
        #        result = tcl.q.router_show(device=device, cmd='show version')

        return tcl.cast_any(result[1])

    def xml(self):
        ''' parsing mechanism: xml

        Function xml() defines the xml type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        output =  tcl.q.caas.abstract(device=self.device.handle,
                                      exec='show ip rip interface vrf all | xml')
        result = tcl.cast_any(output[1])

        return result

class ShowIpv6RipInterfaceVrfAll(ShowIpRipInterfaceSchema,MetaParser):
    """Parser for:
        show ipv6 rip interface vrf all
        parser class implements detail parsing mechanisms for cli and xml output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).


    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        result = tcl.q.caas.abstract(device=self.device.handle,
                                     exec='show ipv6 rip interface vrf all')

        #        # To leverage router_show parsers:
        #        result = tcl.q.router_show(device=device, cmd='show version')

        return tcl.cast_any(result[1])

    def xml(self):
        ''' parsing mechanism: xml

        Function xml() defines the xml type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        output =  tcl.q.caas.abstract(device=self.device.handle,
                                      exec='show ipv6 rip interface vrf all | xml')
        result = tcl.cast_any(output[1])

        return result

class ShowIpRipStatisticsSchema(MetaParser):
    """Schema for show ip rip statistics"""
    schema = {'process':
                  {regexp('rip-(.*)'):
                       {'multicast_update_periodic': str,
                        'multicast_update_triggered': str,
                        'recv_bad_pkts': str,
                        'recv_bad_routes': str,
                        'recv_multi_request': str,
                        'recv_multicast_updates': str,
                        'recv_uni_requests': str,
                        'recv_uni_updates': str,
                        'sent_multicast_request': str,
                        'sent_uni_updates': str
                       }
                  }
             }


class ShowIpRipStatistics(ShowIpRipStatisticsSchema, MetaParser):
    """Parser for:
        show ip rip statistics
        parser class implements detail parsing mechanisms for cli and xml output.
    """
    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).


    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        result = tcl.q.caas.abstract(device=self.device.handle,
                                     exec='show ip rip statistics')

        #        # To leverage router_show parsers:
        #        result = tcl.q.router_show(device=device, cmd='show version')

        return tcl.cast_any(result[1])

    def xml(self):
        ''' parsing mechanism: xml

        Function xml() defines the xml type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        output =  tcl.q.caas.abstract(device=self.device.handle,
                                      exec='show ip rip statistics | xml')
        result = tcl.cast_any(output[1])

        return result

class ShowIpv6RipStatistics(ShowIpRipStatisticsSchema, MetaParser):
    """Parser for:
           show ipv6 rip statistics
           parser class implements detail parsing mechanisms for cli and xml output.
    """

    #*************************
    # schema - class variable
    #
    # Purpose is to make sure the parser always return the output
    # (nested dict) that has the same data structure across all supported
    # parsing mechanisms (cli(), yang(), xml()).


    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        result = tcl.q.caas.abstract(device=self.device.handle,
                                     exec='show ipv6 rip statistics')

        #        # To leverage router_show parsers:
        #        result = tcl.q.router_show(device=device, cmd='show version')

        return tcl.cast_any(result[1])

    def xml(self):
        ''' parsing mechanism: xml

        Function xml() defines the xml type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        output =  tcl.q.caas.abstract(device=self.device.handle,
                                      exec='show ipv6 rip statistics | xml')
        result = tcl.cast_any(output[1])

        return result

# class ShowIpRipRouteVrfAll(MetaParser):
#     """ parser class - implements detail parsing mechanisms for cli, xml, and
#     yang output.
#     """
#     #*************************
#     # schema - class variable
#     #
#     # Purpose is to make sure the parser always return the output
#     # (nested dict) that has the same data structure across all supported
#     # parsing mechanisms (cli(), yang(), xml()).
#
#
#     def cli(self):
#         ''' parsing mechanism: cli
#
#         Function cli() defines the cli type output parsing mechanism which
#         typically contains 3 steps: executing, transforming, returning
#         '''
#         result = tcl.q.caas.abstract(device=self.device.handle,
#                                      exec='show ip rip route vrf all')
#
#         #        # To leverage router_show parsers:
#         #        result = tcl.q.router_show(device=device, cmd='show version')
#
#         return tcl.cast_any(result[1])
#
#     def xml(self):
#         ''' parsing mechanism: xml
#
#         Function xml() defines the xml type output parsing mechanism which
#         typically contains 3 steps: executing, transforming, returning
#         '''
#         output =  tcl.q.caas.abstract(device=self.device.handle,
#                                       exec='show ip rip route vrf all | xml')
#         result = tcl.cast_any(output[1])
#
#         return result
#
# class ShowIpv6RipRouteVrfAll(MetaParser):
#     """ parser class - implements detail parsing mechanisms for cli, xml, and
#     yang output.
#     """
#     #*************************
#     # schema - class variable
#     #
#     # Purpose is to make sure the parser always return the output
#     # (nested dict) that has the same data structure across all supported
#     # parsing mechanisms (cli(), yang(), xml()).
#
#
#     def cli(self):
#         ''' parsing mechanism: cli
#
#         Function cli() defines the cli type output parsing mechanism which
#         typically contains 3 steps: executing, transforming, returning
#         '''
#         result = tcl.q.caas.abstract(device=self.device.handle,
#                                      exec='show ipv6 rip route vrf all')
#
#         #        # To leverage router_show parsers:
#         #        result = tcl.q.router_show(device=device, cmd='show version')
#
#         return tcl.cast_any(result[1])
#
#     def xml(self):
#         ''' parsing mechanism: xml
#
#         Function xml() defines the xml type output parsing mechanism which
#         typically contains 3 steps: executing, transforming, returning
#         '''
#         output =  tcl.q.caas.abstract(device=self.device.handle,
#                                       exec='show ipv6 rip route vrf all | xml')
#         result = tcl.cast_any(output[1])
#
#         return result


class ShowIpRipVrfAllSchema(MetaParser):
    """Schema for:
        * show ip rip vrf all
        * show ipv6 rip vrf all"""

    schema = {
        'vrf': {
            'isolate_mode': bool,
            'mmode': str,
            Any(): {
                'address_family': {
                    Any(): {
                        'instance': {
                            Any(): {
                                'port': int,
                                'multicast_group': str,
                                'distance': int,
                                Optional('timers'): {
                                    Optional('update_interval'): int,
                                    Optional('expire_time'): int,
                                    Optional('flush_time'): int,
                                },
                                'default_metric': int,
                                'max_path': int,
                                'state': str,
                                Optional('interfaces'): {
                                    Any(): {
                                    },
                                },
                                Optional('redistribute'): {
                                    Any(): {
                                        Optional('route_policy'): str,
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }


class ShowIpRipVrfAll(ShowIpRipVrfAllSchema):
    """Parser for show ip rip vrf all"""

    cli_command = "show ip rip vrf all"
    address_family = "ipv4"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        address_family = self.address_family

        # RIP Isolate Mode: No
        p1 = re.compile(r'^RIP +Isolate +Mode: +(?P<isolate_mode>(Yes|No))$')

        # MMODE: Initialized
        p2 = re.compile(r'^MMODE\: +(?P<mmode>[a-zA-Z]+)$')

        # Process Name "rip-1" VRF "default"
        p3 = re.compile(r'^Process +Name +\"(?P<instance>.+)\" +'
                        r'VRF +\"(?P<vrf>.+)\"$')

        # RIP port 520, multicast-group 224.0.0.9
        p4 = re.compile(r'^RIP +port +(?P<port>\d+), +'
                        r'multicast\-group +'
                        r'(?P<multicast_group>[\w\:\/\.]+)$')

        # Admin-distance: 120
        p5 = re.compile(r'^Admin\-distance\: +(?P<distance>\d+)$')

        # Updates every 10 sec, expire in 21 sec
        p6 = re.compile(r'^Updates +every +(?P<update_interval>\d+) +sec,'
                        r' +expire +in +(?P<expire_time>\d+) +sec$')

        # Collect garbage in 23 sec
        p7 = re.compile(r'^Collect +garbage +in +(?P<flush_time>\d+) +sec$')

        # Default-metric: 3
        p8 = re.compile(r'^Default\-metric\: +(?P<default_metric>\d+)$')

        # Max-paths: 16
        p9 = re.compile(r'^Max\-paths\: +(?P<max_path>\d+)$')

        # Process is up and running
        p10 = re.compile(r'^Process +is +(?P<state>.+)$')

        #   Interfaces supported by ipv4 RIP :
        #     Ethernet1/1.100
        #     Ethernet1/2.100
        p11 = re.compile(r'^(?P<interface>^(?!None)[\w\/\.]+)$')

        #   Redistributing :
        #     direct          policy ALL
        #     static          policy ALL
        p12 = re.compile(r'^(?P<redistribute>\w+)\s+policy +'
                         r'(?P<route_policy>[\w\-]+)$')

        ret_dict = {}
        for line in out.splitlines():
            if line:
                line = line.strip()
            else:
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                vrf_dict = ret_dict.setdefault('vrf', {})
                vrf_dict['isolate_mode'] = \
                    True if group['isolate_mode'] == 'Yes' else False
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                vrf_dict['mmode'] = str(group['mmode'])
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                instance_dict = vrf_dict \
                    .setdefault(str(group['vrf']), {}) \
                    .setdefault('address_family', {}) \
                    .setdefault(address_family, {}) \
                    .setdefault('instance', {}) \
                    .setdefault(str(group['instance']), {})
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                instance_dict['port'] = int(group['port'])
                instance_dict['multicast_group'] = \
                    str(group['multicast_group'])
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                instance_dict['distance'] = int(group['distance'])
                continue

            m = p6.match(line)
            if m:
                group = m.groupdict()
                timers_dict = instance_dict.setdefault('timers', {})
                timers_dict['update_interval'] = int(group['update_interval'])
                timers_dict['expire_time'] = int(group['expire_time'])
                continue

            m = p7.match(line)
            if m:
                group = m.groupdict()
                timers_dict = instance_dict.setdefault('timers', {})
                timers_dict['flush_time'] = int(group['flush_time'])
                continue

            m = p8.match(line)
            if m:
                group = m.groupdict()
                instance_dict['default_metric'] = \
                    int(group['default_metric'])
                continue

            m = p9.match(line)
            if m:
                group = m.groupdict()
                instance_dict['max_path'] = int(group['max_path'])
                continue

            m = p10.match(line)
            if m:
                group = m.groupdict()
                instance_dict['state'] = str(group['state'])
                continue

            m = p11.match(line)
            if m:
                group = m.groupdict()
                interface_dict = instance_dict \
                    .setdefault('interfaces', {})
                interface_dict.setdefault(str(group['interface']), {})
                continue

            m = p12.match(line)
            if m:
                group = m.groupdict()
                redistribute_str = str(group['redistribute'])
                redistribute_dict = instance_dict \
                    .setdefault('redistribute', {}) \
                    .setdefault(redistribute_str, {})
                redistribute_dict['route_policy'] = str(group['route_policy'])
                continue

        return ret_dict


class ShowIpRipRouteVrfAllSchema(MetaParser):
    """Schema for:
        * show ip rip vrf all
        * show ipv6 rip vrf all"""
    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        'instance': {
                            Any(): {
                                'routes': {
                                    Any(): {
                                        'index': {
                                            Any(): {
                                                Optional('next_hop'): str,
                                                Optional('interface'): str,
                                                Optional('metric'): int,
                                                Optional('tag'): int,
                                                Optional('redistributed'): bool,
                                                Optional('route_type'): str,
                                                Optional('expire_time'): str,
                                            },
                                        },
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }


class ShowIpRipRouteVrfAll(ShowIpRipRouteVrfAllSchema):
    """Parser for : show ip rip route vrf all"""

    cli_command = "show ip rip route vrf all"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Process Name "rip-1" VRF "default"
        p1 = re.compile(r'^Process +Name +\"(?P<instance>.+)\" +'
                        r'VRF +\"(?P<vrf>.+)\"$')

        # RIP routing table
        # > - indicates best RIP route

        # >10.1.2.0/24 next-hops 0
        # >2001:db8:1:2::/64 next-hops 0
        p2 = re.compile(r'^\> *(?P<route>[a-zA-Z0-9\.\/\:]+) +'
                        r'next\-hops +\d+$')

        # via 10.1.2.1 Ethernet1/1.100, metric 1, tag 0, direct route
        p3 = re.compile(
            r'^via +(?P<next_hop>[a-zA-Z0-9\.\/\:]+)( +(?P<interface>\S+))?, +'
            r'metric +(?P<metric>\d+), +tag +(?P<tag>\d+), +')
        p3_1 = re.compile(r'.*(?P<route_type>((direct '
                          r'+route)|external|external\-backup|rip))$')

        # via 10.1.2.2 Ethernet1/1.100, metric 3, tag 0, timeout 00:00:05
        p3_2 = re.compile(r'.*timeout +(?P<expire_time>[\d\:]+)$')

        # via 0.0.0.0, metric 15, tag 0, redistributed route
        p3_3 = re.compile(r'.*redistributed +route$')

        ret_dict = {}
        address_family = "ipv4"
        index = 1
        route_type_list = ['connected', 'external', 'external-backup', 'rip']
        route_dict = {}

        for line in out.splitlines():
            if line:
                line = line.strip()
            else:
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                routes_dict = ret_dict.setdefault('vrf', {}) \
                    .setdefault(str(group['vrf']), {}) \
                    .setdefault('address_family', {}) \
                    .setdefault(address_family, {}) \
                    .setdefault('instance', {}) \
                    .setdefault(str(group['instance']), {}) \
                    .setdefault('routes', {})
                continue

            # >10.1.2.0/24 next-hops 0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                route = str(group['route'])
                if route not in routes_dict.keys():
                    index = 1
                route_dict = routes_dict.setdefault(route, {})
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                index_dict = route_dict.setdefault('index', {}) \
                    .setdefault(index, {})
                index_dict.update({'next_hop': str(group['next_hop'])})
                if 'interface' in group.keys():
                    index_dict.update({'interface': str(group['interface'])})
                index_dict.update({'metric': int(group['metric'])})
                index_dict.update({'tag': int(group['tag'])})
                index += 1

                m1 = p3_1.match(line)
                if m1:
                    group = m1.groupdict()
                    route_type = str(group['route_type'])
                    if route_type.replace(" ", "") == 'directroute':
                        route_type = "connected"
                    if route_type in route_type_list:
                        index_dict.update({'route_type': route_type})

                m2 = p3_2.match(line)
                if m2:
                    group = m2.groupdict()
                    index_dict.update(
                        {'expire_time': str(group['expire_time'])})

                m3 = p3_3.match(line)
                if m3:
                    index_dict.update({'redistributed': True})

                continue

        return ret_dict


class ShowIpRipInterfaceVrfAllSchema(MetaParser):
    """Schema for show ip rip interface vrf all"""
    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        'instance': {
                            Any(): {
                                'interfaces': {
                                    Any(): {
                                        Optional('states'): {
                                            Optional('protocol_state'): str,
                                            Optional('link_state'): str,
                                            Optional('admin_state'): str,
                                        },
                                        'oper_status': str,
                                        Optional('authentication'): {
                                            'auth_key_chain': {
                                                'key_chain': str,
                                            },
                                            'auth_key': {
                                                'crypto_algorithm': str,
                                            },
                                        },
                                        'summary_address': {
                                            Any(): {
                                                'metric': int,
                                            },
                                        },
                                        Optional('split_horizon'): bool,
                                        Optional('passive'): bool,
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }


class ShowIpRipInterfaceVrfAll(ShowIpRipInterfaceVrfAllSchema):
    """Parser for : show ip rip interface vrf all"""

    cli_command = "show ip rip interface vrf all"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Process Name "rip-1" VRF "default"
        p1 = re.compile(r'^Process +Name +\"(?P<instance>.+)\" +'
                        r'VRF +\"(?P<vrf>.+)\"$')

        # RIP-configured interface information

        # Ethernet1/1.100, protocol-up/link-up/admin-up, RIP state : up
        p2 = re.compile(r'^(?P<interface>\S+), +'
                        r'protocol\-(?P<protocol_state>(up|down))\/'
                        r'link\-(?P<link_state>(up|down))\/'
                        r'admin\-(?P<admin_state>(up|down)), +'
                        r'RIP +state *\: +(?P<oper_status>(up|down))$')

        #   address/mask 10.1.2.1/24, metric 1, split-horizon, passive (
        # no outbound updates)
        #   address/mask 10.1.3.1/24, metric 1, split-horizon
        p3 = re.compile(r'^address\/mask +(?P<summary_address>[\d\.\/]+),'
                        r' +metric +(?P<metric>\d+)'
                        r'(, +(?P<split_horizon>split\-horizon))?'
                        r'(, +(?P<passive>passive)[a-zA-Z\(\) ]+)?$')

        # Authentication Mode: md5  Keychain: none
        p4 = re.compile(r'Authentication +Mode\: +'
                        r'(?P<crypto_algorithm>\w+) +'
                        r'Keychain\: +(?P<key_chain>\w+)')

        address_family = 'ipv4'
        state_list = ['protocol_state', 'link_state', 'admin_state']
        ret_dict = {}
        for line in out.splitlines():
            if line:
                line = line.strip()
            else:
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                intfs_dict = ret_dict.setdefault('vrf', {}) \
                    .setdefault(str(group['vrf']), {}) \
                    .setdefault('address_family', {}) \
                    .setdefault(address_family, {}) \
                    .setdefault('instance', {}) \
                    .setdefault(str(group['instance']), {}) \
                    .setdefault('interfaces', {})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                intf_dict = intfs_dict.setdefault(str(group['interface']), {})
                for key in state_list:
                    if key in group.keys():
                        intf_dict.setdefault('states', {}) \
                            .setdefault(key, str(group[key]))
                intf_dict.update({'oper_status': group['oper_status']})
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                intf_dict.setdefault('summary_address', {}) \
                    .setdefault(str(group['summary_address']), {}) \
                    .setdefault('metric', int(group['metric']))
                for key in ['split_horizon', 'passive']:
                    intf_dict[key] = True if key in group.keys() else False
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                auth_dict = intf_dict.setdefault('authentication', {})
                auth_dict.setdefault('auth_key_chain', {}) \
                    .setdefault('key_chain', str(group['key_chain']))
                auth_dict.setdefault('auth_key', {}) \
                    .setdefault('crypto_algorithm', str(group['crypto_algorithm']))

        return ret_dict


class ShowIpv6RipVrfAll(ShowIpRipVrfAll, ShowIpRipVrfAllSchema):
    """Parser for show ipv6 rip vrf all"""

    cli_command = "show ipv6 rip vrf all"
    address_family = "ipv6"

    def cli(self, output=None):
        return super().cli(output)


class ShowIpv6RipRouteVrfAll(ShowIpRipRouteVrfAll, ShowIpRipRouteVrfAllSchema):
    """Parser for show ipv6 rip route vrf all"""

    cli_command = "show ipv6 rip route vrf all"
    address_family = "ipv6"

    def cli(self, output=None):
        return super().cli(output)


class ShowIpv6InterfaceVrfAllSchema(MetaParser):
    """Schema for show ip rip interface vrf all"""
    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        'instance': {
                            Any(): {
                                Optional('interfaces'): {
                                    Any(): {
                                        'states': {
                                            Optional('protocol_state'): str,
                                            Optional('link_state'): str,
                                            Optional('admin_state'): str,
                                        },
                                        'iod': int,
                                        'address': {
                                            Any(): {
                                                'valid': bool
                                            }
                                        },
                                        'subnet': str,
                                        'link_local_address': {
                                            Any(): {
                                                'default': bool,
                                                'valid': bool,
                                            },
                                        },
                                        Optional(
                                            'virtual_addresses_configured'): str,
                                        'multicast_routing': str,
                                        'report_link_local': str,
                                        'forwarding_feature': str,
                                        Optional(
                                            'multicast_groups_locally_joined'):list,
                                        Optional(
                                            'multicast_SG_entries_joined'): str,
                                        Optional('mtu'): int,
                                        Optional(
                                            'unicast_reverse_path_forwarding'): str,
                                        Optional('load_sharing'): str,
                                        Optional(
                                            'interface_statistics_last_reset'): str,
                                        'RP_traffic_statistics': {
                                            Optional('unicast_packets'): str,
                                            Optional('unicast_bytes'): str,
                                            Optional('multicast_packets'): str,
                                            Optional('multicast_bytes'): str,
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }


class ShowIpv6InterfaceVrfAll(ShowIpv6InterfaceVrfAllSchema):
    """Parser for : show ipv6 interface vrf all"""

    cli_command = "show ipv6 interface vrf all"

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # IPv6 Interface Status for VRF "default"
        p1 = re.compile(r'^(?P<address_family>(IP|ip)v\d) +Interface +Status +'
                        r'for +VRF +\"(?P<vrf>.+)\"$')

        # Ethernet1/1.100, Interface status: protocol-up/link-up/admin-up, iod: 136
        p2 = re.compile(r'^(?P<interface>\S+), +Interface +status\: +'
                        r'protocol\-(?P<protocol_state>(up|down))\/'
                        r'link\-(?P<link_state>(up|down))\/'
                        r'admin\-(?P<admin_state>(up|down)), +'
                        r'iod: +(?P<iod>\d+)$')

        # IPv6 address: 
        #   2001:db8:1:2::1/64 [VALID]
        p3 = re.compile(r'^IPv6 +address\:$')
        p4 = re.compile(r'^(?P<address>[0-9a-zA-Z\:\/]+)( +\[(?P<valid>VALID)\])?$')

        # IPv6 subnet:  2001:db8:1:2::/64
        p5 = re.compile(r'IPv6 +subnet\: +(?P<subnet>[0-9a-zA-Z\:\/]+)$')

        # IPv6 link-local address: fe80::5c00:ff:fe00:7 (default) [VALID]
        p6 = re.compile(r'IPv6 +link\-local +address\: +'
            r'(?P<address>[0-9a-zA-Z\:\/]+)'
            r'( +\((?P<default>default)\))?'
            r'( +\[(?P<valid>VALID)\])?$')

        # IPv6 virtual addresses configured: none
        p7 = re.compile(r'IPv6 +virtual +addresses +configured\: +'
            r'(?P<virtual_addresses_configured>[\s\S]+)$')

        # IPv6 multicast routing: disabled
        p8 = re.compile(r'IPv6 +multicast +routing\: +'
            r'(?P<multicast_routing>\w+)$')

        # IPv6 report link local: disabled
        p9 = re.compile(r'IPv6 +report +link +local\: +'
            r'(?P<report_link_local>\w+)$')

        # IPv6 Forwarding feature: disabled
        p10 = re.compile(r'IPv6 +Forwarding +feature\: +'
            r'(?P<forwarding_feature>\w+)$')

        # IPv6 multicast groups locally joined:
        p11 = re.compile(r'^IPv6 +multicast +groups +locally +joined:$')
        p11_1 = re.compile(r'^(?P<address>[0-9a-zA-Z\:\s]+)+$')

        # IPv6 multicast (S,G) entries joined: none
        p12 = re.compile(r'^IPv6 +multicast +\(S\,G\) +entries +joined\:'
            r'(?P<multicast_SG_entries_joined>[\s\S]+)$')

        # IPv6 MTU: 1500 (using link MTU)
        p13 = re.compile(r'IPv6 +MTU\: +(?P<mtu>\d+)(\s\S)+$')

        # IPv6 unicast reverse path forwarding: none
        p14 = re.compile(r'IPv6 +unicast +reverse +path +forwarding\:'
            r' +(?P<unicast_reverse_path_forwarding>[\s\S]+)$')

        # IPv6 load sharing: none
        p15 = re.compile(r'IPv6 +load +sharing\: +'
            r'(?P<load_sharing>[\s\S]+)$')

        # IPv6 interface statistics last reset: never
        p16 = re.compile(r'^IPv6 +interface +statistics +last +reset\: +'
            r'(?P<interface_statistics_last_reset>[\s\S]+)$')

        # IPv6 interface RP-traffic statistics: (forwarded/originated/consumed)
        p17 = re.compile(r'IPv6 +interface +RP-traffic +statistics\: +'
            r'\(forwarded\/originated\/consumed\)$')

        #     Unicast packets:      0/11/11
        p17_1 = re.compile(r'Unicast +packets\:\s'
            r'+ (?P<unicast_packets>[0-9\/]+)$')
        #     Unicast bytes:        0/990/792
        p17_2 = re.compile(r'Unicast +bytes\:\s'
            r'+ (?P<unicast_bytes>[0-9\/]+)$')
        #     Multicast packets:    0/162/157
        p17_3 = re.compile(r'Multicast +packets\:\s'
            r'+ (?P<multicast_packets>[0-9\/]+)$')
        #     Multicast bytes:      0/19712/14568
        p17_4 = re.compile(r'Multicast +bytes\:\s'
            r'+ (?P<multicast_bytes>[0-9\/]+)$')

        instance = 'rip'
        state_list = ['protocol_state', 'link_state', 'admin_state']
        ret_dict = {}
        bool_ipv6_address = False
        
        for line in out.splitlines():
            if line:
                line = line.strip()
            else:
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                inst_dict = ret_dict.setdefault('vrf', {}) \
                    .setdefault(str(group['vrf']), {}) \
                    .setdefault('address_family', {}) \
                    .setdefault(str(group['address_family']).lower(), {}) \
                    .setdefault('instance', {}) \
                    .setdefault(instance, {})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                intf_dict = inst_dict.setdefault('interfaces', {}) \
                    .setdefault(str(group['interface']),{})
                for key in state_list:
                    if key in group.keys():
                        intf_dict.setdefault('states', {}) \
                            .update({key: str(group[key])})
                intf_dict.update({'iod': int(group['iod'])})
                continue

            m = p3.match(line)
            if m:
                bool_ipv6_address = True
                continue

            m = p4.match(line)
            if bool_ipv6_address and m:
                group = m.groupdict()
                address_dict = intf_dict.setdefault('address', {}) \
                    .setdefault(str(group['address']), {})
                if 'valid' in group.keys():
                    address_dict.setdefault('valid', True)
                bool_ipv6_address = False
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'subnet': group['subnet']})
                continue

            m = p6.match(line)
            if m:
                group = m.groupdict()
                link_dict = intf_dict.setdefault('link_local_address', {}) \
                    .setdefault(str(group['address']), {})
                for key in ['valid', 'default']:
                    if key in group.keys():
                        link_dict.setdefault(key, True)
                continue

            m = p7.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'virtual_addresses_configured': \
                    group['virtual_addresses_configured']})
                continue

            m = p8.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'multicast_routing': \
                    group['multicast_routing']})
                continue

            m = p9.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'report_link_local': \
                    group['report_link_local']})
                continue

            m = p10.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'forwarding_feature': \
                    group['forwarding_feature']})
                continue

            m = p12.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'multicast_SG_entries_joined': \
                    group['multicast_SG_entries_joined']})
                continue

            m = p13.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'mtu': group['mtu']})
                continue
            
            m = p14.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'unicast_reverse_path_forwarding': \
                    group['unicast_reverse_path_forwarding']})
                continue

            m = p15.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'load_sharing': group['load_sharing']})
                continue

            m = p16.match(line)
            if m:
                group = m.groupdict()
                intf_dict.update({'interface_statistics_last_reset': \
                    group['interface_statistics_last_reset']})
                continue

            m = p17.match(line)
            if m:
                RP_dict = intf_dict.setdefault('RP_traffic_statistics', {})
                continue

            m = p17_1.match(line)
            if m:
                group = m.groupdict()
                RP_dict.update({'unicast_packets': \
                    group['unicast_packets']})
                continue

            m = p17_2.match(line)
            if m:
                group = m.groupdict()
                RP_dict.update({'unicast_bytes': \
                    group['unicast_bytes']})
                continue

            m = p17_3.match(line)
            if m:
                group = m.groupdict()
                RP_dict.update({'multicast_packets': \
                    group['multicast_packets']})
                continue

            m = p17_4.match(line)
            if m:
                group = m.groupdict()
                RP_dict.update({'multicast_bytes': \
                    group['multicast_bytes']})
                continue

            m = p11.match(line)
            if m:
                continue

            m = p11_1.match(line)
            if m:
                group = m.groupdict()
                intf_dict.setdefault('multicast_groups_locally_joined', [])
                multicast_groups = str(group['address']).split()
                intf_dict.get('multicast_groups_locally_joined').extend(multicast_groups)
                continue

        return ret_dict
