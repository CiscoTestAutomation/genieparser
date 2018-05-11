"""show_rip.py

NXOS parser class for below command(s):
    show ip rip vrf all
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
                            {'adminDistance': str,
                             'defaultMetric': str,
                             'expiryTime': str,
                             'garbageCollectorTime': str,
                             'maxPaths': str,
                             'multicastGroup': str,
                             Optional('ripInterfaceList'): str,
                             Optional('ripPort'): str,
                             'state': str,
                             'status': str,
                             'updateTime': str,}
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