"""show_rip.py

NXOS parser class for below commands:
    * show ip rip
    * show ip rip vrf <vrf>
    * show ip rip vrf all

    * show ipv6 rip
    * show ipv6 rip vrf <vrf>
    * show ipv6 rip vrf all

    * show ip rip route
    * show ip rip route vrf <vrf>
    * show ip rip route vrf all

    * show ipv6 rip route
    * show ipv6 rip route vrf {vrf}
    * show ipv6 rip route vrf all

    * show ip rip interface
    * show ip rip interface vrf {vrf}
    * show ip rip interface vrf all
"""
import xmltodict
import re

try:
    from pyats import tcl
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


# class ShowIpRipVrfAll(ShowIpRipSchema, MetaParser):
#     """Parser for:
#         show ip rip vrf all
#         parser class implements detail parsing mechanisms for cli and xml output.
#     """
#     #*************************
#     # schema - class variable
#     #
#     # Purpose is to make sure the parser always return the output
#     # (nested dict) that has the same data structure across all supported
#     # parsing mechanisms (cli(), yang(), xml()).


#     def cli(self):
#         ''' parsing mechanism: cli

#         Function cli() defines the cli type output parsing mechanism which
#         typically contains 3 steps: executing, transforming, returning
#         '''
#         result = tcl.q.caas.abstract(device=self.device.handle,
#                                      exec='show ip rip vrf all')

#         #        # To leverage router_show parsers:
#         #        result = tcl.q.router_show(device=device, cmd='show version')

#         return tcl.cast_any(result[1])

#     def xml(self):
#         ''' parsing mechanism: xml

#         Function xml() defines the xml type output parsing mechanism which
#         typically contains 3 steps: executing, transforming, returning
#         '''
#         output =  tcl.q.caas.abstract(device=self.device.handle,
#                                       exec='show ip rip vrf all | xml')
#         result = tcl.cast_any(output[1])

#         return result

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
        * show ip rip
        * show ip rip vrf <vrf>
        * show ip rip vrf all
        * show ipv6 rip
        * show ipv6 rip vrf <vrf>
        * show ipv6 rip vrf all"""

    schema = {
        'isolate_mode': bool,
        'mmode': str,
        'vrf': {
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
                                    Optional('expire_in'): int,
                                    Optional('collect_garbage'): int,
                                },
                                'default_metric': int,
                                'maximum_paths': int,
                                Optional('default_originate'): str,
                                'process': str,
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
    """Parser for:
        * show ip rip
        * show ip rip vrf <vrf>
        * show ip rip vrf all"""

    cli_command = ["show ip rip",
                   "show ip rip vrf {vrf}"]

    address_family = "ipv4"

    def cli(self, vrf='', output=None):
        cmd = ""
        if output is None:
            if vrf:
                cmd = self.cli_command[1].format(vrf=vrf)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
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
                        r' +expire +in +(?P<expire_in>\d+) +sec$')

        # Collect garbage in 23 sec
        p7 = re.compile(r'^Collect +garbage +in +(?P<collect_garbage>\d+) '
                        r'+sec$')

        # Default-metric: 3
        p8 = re.compile(r'^Default\-metric\: +(?P<default_metric>\d+)$')

        # Max-paths: 16
        p9 = re.compile(r'^Max\-paths\: +(?P<maximum_paths>\d+)$')

        # Default-originate:
        p10 = re.compile(r'^Default\-originate\: *'
                         r'(?P<default_originate>[\s\S]+)?$')

        # Process is up and running
        p11 = re.compile(r'^Process +is +(?P<process>.+)$')

        #   Interfaces supported by ipv4 RIP :
        #     Ethernet1/1.100
        #     Ethernet1/2.100
        p12 = re.compile(r'^(?P<interface>^(?!None)[\w\/\.]+)$')

        #   Redistributing :
        #     direct          policy ALL
        #     static          policy ALL
        p13 = re.compile(r'^(?P<redistribute>\w+)\s+policy +'
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

                ret_dict['isolate_mode'] = \
                    True if group['isolate_mode'] == 'Yes' else False
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict['mmode'] = str(group['mmode'])
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                instance_dict = ret_dict.setdefault('vrf', {}) \
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
                timers_dict['expire_in'] = int(group['expire_in'])
                continue

            m = p7.match(line)
            if m:
                group = m.groupdict()
                timers_dict = instance_dict.setdefault('timers', {})
                timers_dict['collect_garbage'] = \
                    int(group['collect_garbage'])
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
                instance_dict['maximum_paths'] = int(group['maximum_paths'])
                continue

            m = p10.match(line)
            if m:
                group = m.groupdict()
                if group['default_originate']:
                    instance_dict['default_originate'] \
                        = str(group['default_originate']).strip()
                continue

            m = p11.match(line)
            if m:
                group = m.groupdict()
                instance_dict['process'] = str(group['process'])
                continue

            m = p12.match(line)
            if m:
                group = m.groupdict()
                interface_dict = instance_dict \
                    .setdefault('interfaces', {})
                interface_dict.setdefault(str(group['interface']), {})
                continue

            m = p13.match(line)
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
        * show ip rip route
        * show ip rip route vrf <vrf>
        * show ip rip route vrf all
        * show ipv6 rip route
        * show ipv6 rip route vrf {vrf}
        * show ipv6 rip route vrf all"""

    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        'instance': {
                            Any(): {
                                'routes': {
                                    Any(): {
                                        'best_route': bool,
                                        'next_hops': int,
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
    """Parser for:
        * show ip rip route
        * show ip rip route vrf <vrf>
        * show ip rip route vrf all"""

    cli_command = ["show ip rip route",
                   "show ip rip route vrf {vrf}"]
    exclude = ['expire_time']

    def cli(self, vrf='', output=None):
        cmd = ""
        if output is None:
            if vrf:
                cmd = self.cli_command[1].format(vrf=vrf)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        # Process Name "rip-1" VRF "default"
        p1 = re.compile(r'^Process +Name +\"(?P<instance>.+)\" +'
                        r'VRF +\"(?P<vrf>.+)\"$')

        # RIP routing table
        # > - indicates best RIP route

        # >10.1.2.0/24 next-hops 0
        # >2001:db8:1:2::/64 next-hops 0
        p2 = re.compile(r'^(?P<best>\>)? *(?P<route>[a-zA-Z0-9\.\/\:]+) +'
                        r'next\-hops +(?P<next_hops>\d+)$')

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
        best = False

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
                route_dict.update({'best_route':
                                  True if group['best'] else False})
                route_dict.update({'next_hops': int(group['next_hops'])})
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                index_dict = route_dict.setdefault('index', {}) \
                    .setdefault(index, {})
                index_dict.update({'next_hop': str(group['next_hop'])})
                if group['interface']:
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
    """Schema for:
        * show ip rip interface
        * show ip rip interface vrf {vrf}
        * show ip rip interface vrf all"""

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
                                        'ipv4': {
                                            Any(): {
                                                'ip': str,
                                                'prefix_length': int,
                                            },
                                        },
                                        'metric': int,
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
    """Parser for:
        * show ip rip interface
        * show ip rip interface vrf {vrf}
        * show ip rip interface vrf all"""

    cli_command = ["show ip rip interface",
                   "show ip rip interface vrf {vrf}"]

    def cli(self, vrf='', output=None):
        cmd = ""
        if output is None:
            if vrf:
                cmd = self.cli_command[1].format(vrf=vrf)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
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
        p3 = re.compile(r'^address\/mask +(?P<ipv4>[\d\.\/]+),'
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
                            .update({key: str(group[key])})
                intf_dict.update({'oper_status': group['oper_status']})
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                temp_address = str(group['ipv4'])
                temp_address_dict = intf_dict.setdefault('ipv4', {}) \
                    .setdefault(temp_address, {})
                temp_ip, temp_prefixlen = temp_address.split('/')
                temp_address_dict.update({'ip': temp_ip})
                temp_address_dict.update({'prefix_length': int(temp_prefixlen)})
                intf_dict.update({'metric': int(group['metric'])})
                for key in ['split_horizon', 'passive']:
                    if group[key]:
                        intf_dict[key] = True
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


class ShowIpv6RipVrfAll(ShowIpRipVrfAll):
    """Parser for:
        * show ipv6 rip
        * show ipv6 rip vrf {vrf}
        * show ipv6 rip vrf all"""

    cli_command = ["show ipv6 rip",
                   "show ipv6 rip vrf {vrf}"]

    address_family = "ipv6"

    def cli(self, vrf='', output=None):
        return super().cli(vrf, output)


class ShowIpv6RipRouteVrfAll(ShowIpRipRouteVrfAll):
    """Parser for:
        * show ipv6 rip route
        * show ipv6 rip route vrf {vrf}
        * show ipv6 rip route vrf all"""

    cli_command = ["show ipv6 rip route",
                   "show ipv6 rip route vrf {vrf}"]
    exclude = ['expire_time']

    address_family = "ipv6"

    def cli(self, vrf='', output=None):
        return super().cli(vrf, output)
