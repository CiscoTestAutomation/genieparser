''' showversion.py

Example parser class

'''
import xmltodict
import re
from ats import tcl
from metaparser import MetaParser
from metaparser.util.schemaengine import Schema, Any, Optional, Or, And, Default, Use

def regexp(expression):
    def match(value):
        if re.match(expression,value):
            return value
        else:
            raise TypeError("Value '%s' doesnt match regex '%s'"
                              %(value,expression))
    return match

class ShowIpOspfSchema(MetaParser):

    schema = {'process_id':
                {Any():
                    {'vrf':
                        {Any():
                            {'id': str,
                             'instance_number': str,
                             'graceful_restart': str,
                             'grace_period': str,
                             'administrative_distance': str,
                             'number_of_areas': str,
                             Optional('area'):
                                 {regexp('(.*)'):
                                     {'interfaces_in_this_area': str,
                                      'active_interfaces': str,
                                      'passive_interfaces': str,
                                      'loopback_interfaces': str},
                                 },
                             }
                         },
                     }
                 },
            }


class ShowIpOspfVrfAll(ShowIpOspfSchema, MetaParser):
    """ parser class - implements detail parsing mechanisms for cli, xml, and
    yang output.
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
                                     exec='show ip ospf vrf all')

        #        # To leverage router_show parsers:
        #        result = tcl.q.router_show(device=device, cmd='show version')

        return tcl.cast_any(result[1])

    def xml(self):
        ''' parsing mechanism: xml

        Function xml() defines the xml type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        output =  tcl.q.caas.abstract(device=self.device.handle,
                                      exec='show ip ospf vrf all | xml')
        result = tcl.cast_any(output[1])

        return result

class ShowIpOspfNeighborDetailSchema(MetaParser):
    schema = {Optional('intf_list'): str,
              'intf':
                {Any():
                     {'neighbor': str,
                      'interface_address': str,
                      'process_id': str,
                      'vrf': str,
                      'area': str,
                      'state': str,
                      'state_changes': str,
                      'last_change': str,
                      'dr': str,
                      'bdr':str}
                },
            }

class ShowIpOspfNeighborsDetailVrfAll(ShowIpOspfNeighborDetailSchema, MetaParser):
    """ parser class - implements detail parsing mechanisms for cli, xml, and
    yang output.
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
                                     exec='show ip ospf neighbors detail vrf all')

        #        # To leverage router_show parsers:
        #        result = tcl.q.router_show(device=device, cmd='show version')

        return tcl.cast_any(result[1])

    def xml(self):
        ''' parsing mechanism: xml

        Function xml() defines the xml type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        output =  tcl.q.caas.abstract(device=self.device.handle,
                                      exec='show ip ospf neighbors detail vrf all | xml')
        result = tcl.cast_any(output[1])

        return result

class ShowIpOspfInterfaceSchema(MetaParser):
    schema = {Optional('intf_list'): str,
              'intf':
                {Any():
                     {'ip_address': str,
                      'process_id': str,
                      'vrf': str,
                      'area': str,
                      'state': str,
                      'network_type': str,
                      'cost': str,
                      Optional('designated_router_id'): str,
                      Optional('designated_router_address'): str,
                      Optional('backup_designated_router_id'): str,
                      Optional('backup_designated_router_address'): str,
                      Optional('neighbors'): str,
                      Optional('flooding_to'): str,
                      Optional('adjacency_with'): str,
                      Optional('hello_timer'): str,
                      Optional('dead_timer'): str,
                      Optional('wait_timer'): str,
                      Optional('retransmit_timer'): str}
                },
            }




class ShowIpOspfInterfaceVrfAll(ShowIpOspfInterfaceSchema,MetaParser):
    """ parser class - implements detail parsing mechanisms for cli, xml, and
    yang output.
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
                                     exec='show ip ospf interface vrf all')

        #        # To leverage router_show parsers:
        #        result = tcl.q.router_show(device=device, cmd='show version')

        return tcl.cast_any(result[1])

    def xml(self):
        ''' parsing mechanism: xml

        Function xml() defines the xml type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        output =  tcl.q.caas.abstract(device=self.device.handle,
                                      exec='show ip ospf interface vrf all | xml')
        result = tcl.cast_any(output[1])

        return result

class ShowIpOspfDatabaseSchema(MetaParser):

    schema = {'process_id':
                  {Any():
                       {'router_id': str,
                        Optional('vrf'):
                            {Any():
                                {'area':
                                    {regexp('.*'):
                                        {Any():
                                            {'ls_id':
                                                {Any():
                                                    {'advrouter':
                                                        {Any():
                                                            {'age': str,
                                                             'seq': str,
                                                             'cksum': str,
                                                             Optional('lnkcnt'): str},
                                                        }
                                                    },
                                                },
                                            },
                                        },
                                    },
                                },
                            },
                        }
                   }
              }

class ShowIpOspfDatabase(ShowIpOspfDatabaseSchema, MetaParser):
    """ parser class - implements detail parsing mechanisms for cli, xml, and
    yang output.
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
                                     exec='show ip ospf database')

        #        # To leverage router_show parsers:
        #        result = tcl.q.router_show(device=device, cmd='show version')

        return tcl.cast_any(result[1])

    def xml(self):
        ''' parsing mechanism: xml

        Function xml() defines the xml type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        output =  tcl.q.caas.abstract(device=self.device.handle,
                                      exec='show ip ospf database | xml')
        result = tcl.cast_any(output[1])

        return result
