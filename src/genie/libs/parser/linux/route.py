"""route.py

Linux parsers for the following commands:
    * route
"""

# python
import re

# metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

from netaddr import IPAddress, IPNetwork

# =======================================================
# Schema for 'route'
# =======================================================
class RouteSchema(MetaParser):
    """Schema for route"""

    # Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
    # 0.0.0.0         192.168.1.1     0.0.0.0         UG        0 0          0 wlo1


    schema = {
        'routes': {
            Any(): { # 'destination'
                'mask': {
                    Any(): {
                        'nexthop': {
                            Any(): { # index: 1, 2, 3, etc
                                'interface': str,
                                Optional('flags'): str,
                                Optional('gateway'): str,
                                Optional('metric'): int,
                                Optional('ref'): int,
                                Optional('use'): int,
                                Optional('scope'): str,
                                Optional('proto'): str,
                                Optional('src'): str,
                                Optional('broadcast'): bool,
                                Optional('table'): str,
                                Optional('local'): bool
                            }
                        }
                    }
                }
            }
        }
    }

# =======================================================
# Parser for 'route'
# =======================================================
class Route(RouteSchema):
    """Parser for 
        * route
        * route -4 -n 
        * route -4n
        * route -n4
        * route -n -4
        """

    cli_command = ['route', 'route {flag}']

    def cli(self, flag=None, output=None):
        if output is None:    
            cmd = self.cli_command[0]
            if flag in ['-4 -n', '-4n', '-n4']:
                command = self.cli_command[1].replace('{flag}', flag)
            out = self.device.execute(cmd)
        else:
            out = output

        # Destination     Gateway         Genmask         Flags Metric Ref    Use Iface
        # 192.168.1.0     0.0.0.0         255.255.255.0   U     600    0        0 wlo1

        p1 = re.compile(r'(?P<destination>[a-z0-9\.\:]+)'
                        ' +(?P<gateway>[a-z0-9\.\:_]+)'
                        ' +(?P<mask>[a-z0-9\.\:]+)'
                        ' +(?P<flags>[a-zA-Z]+)'
                        ' +(?P<metric>(\d+))'
                        ' +(?P<ref>(\d+))'
                        ' +(?P<use>(\d+))'
                        ' +(?P<interface>\S+)'
                        )
        
        # Initializes the Python dictionary variable
        parsed_dict = {}


        # Defines the "for" loop, to pattern match each line of output

        for line in out.splitlines():
            line = line.strip()


            # 192.168.1.0     0.0.0.0         255.255.255.0   U     600    0        0 wlo1
            m = p1.match(line)
            if m:
                if 'routes' not in parsed_dict:
                    parsed_dict.setdefault('routes', {})
       
                group = m.groupdict()
                destination = group['destination']
                mask = group['mask']

                index_dict = {}
                for str_k in ['interface', 'flags', 'gateway']:
                    index_dict[str_k] = group[str_k]
                
                for int_k in ['metric', 'ref', 'use']:
                    index_dict[int_k] = int(group[int_k])

                if destination in parsed_dict['routes']:
                    if mask in parsed_dict['routes'][destination]['mask']:
                        parsed_dict['routes'][destination]['mask'][mask].\
                                setdefault('nexthop', {index+1: index_dict})
                    else:
                        index = 1
                        parsed_dict['routes'][destination]['mask'].\
                            setdefault(mask, {}).\
                                setdefault('nexthop', {index: index_dict})
                else:
                    index = 1
                    parsed_dict['routes'].setdefault(destination, {}).\
                        setdefault('mask', {}).\
                            setdefault(mask, {}).\
                                setdefault('nexthop', {index: index_dict})

                continue

        return parsed_dict


# =======================================================
# Parser for 'netstat -rn'
# =======================================================
class ShowNetworkStatusRoute(Route, RouteSchema):
    """Parser for 
        * netstat -rn 
        """

    cli_command = ['netstat -rn']

    def cli(self, output=None):
        if output is None:    
            cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        return super().cli(output=out)

# =====================================================
# Parser for ip route show table all
# =====================================================
class IpRouteShowTableAll(RouteSchema):
    """
    Parser for
        * ip route show table all
    """

    cli_command = ['ip route show table all']

    def cli(self, output=None):
        if output is None:    
            cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        # default via 192.168.1.1 dev enp7s0 proto dhcp metric 100 

        p1 = re.compile(r'default via (?P<gateway>[a-z0-9\.\:]+)'
                         ' dev (?P<device>[a-z0-9\.\-]+)'
                         ' proto (?P<proto>[a-z]+)'
                         ' metric (?P<metric>[\d]+)'
                         )

        # 169.254.0.0/16 dev enp7s0 scope link metric 1000 

        p2 = re.compile(r'(?P<destination>[a-z0-9\.\:\/]+)'
                         ' dev (?P<device>[a-z0-9\.\-]+)'
                         ' scope (?P<scope>\w+)'
                         ' metric (?P<metric>[\d]+)'
                         )

        # 172.17.0.0/16 dev docker0 proto kernel scope link src 172.17.0.1

        p3 = re.compile(r'(?P<destination>[a-z0-9\.\:\/]+)'
                         ' dev (?P<device>[a-z0-9\.\-]+)'
                         ' proto (?P<proto>\w+)'
                         ' scope (?P<scope>\w+)'
                         ' src (?P<src>[a-z0-9\.\:\/]+)'
                         )

        # 172.18.0.0/16 dev br-d19b23fac393 proto kernel scope link src 172.18.0.1 linkdown 

        p4 = re.compile(r'(?P<destination>[a-z0-9\.\:\/]+)'
                         ' dev (?P<device>[a-z0-9\.\-]+)'
                         ' proto (?P<proto>\w+)'
                         ' scope (?P<scope>\w+)'
                         ' src (?P<src>[a-z0-9\.\:\/]+)'
                         ' linkdown '
                         )       

        # 192.168.1.0/24 dev enp7s0 proto kernel scope link src 192.168.1.212 metric 100

        p5 = re.compile(r'(?P<destination>[a-z0-9\.\:\/]+)'
                         ' dev (?P<device>[a-z0-9\.\-]+)'
                         ' proto (?P<proto>\w+)'
                         ' scope (?P<scope>\w+)'
                         ' src (?P<src>[a-z0-9\.\:\/]+)'
                         ' metric (?P<metric>[\d]+)'
                         )

        # broadcast 127.0.0.0 dev lo table local proto kernel scope link src 127.0.0.1 

        p6 = re.compile(r'broadcast (?P<destination>[a-z0-9\.\:\/]+)'
                         ' dev (?P<device>[a-z0-9\.\-]+)'
                         ' table (?P<table>\w+)'
                         ' proto (?P<proto>\w+)'
                         ' scope (?P<scope>\w+)'
                         ' src (?P<src>[a-z0-9\.\:\/]+)'
                         )
                         
        
        # local 10.233.44.70 dev kube-ipvs0 table local proto kernel scope host src 10.233.44.70

        p7 = re.compile(r'local (?P<destination>[a-z0-9\.\:\/]+)'
                         ' dev (?P<device>[a-z0-9\.\-]+)'
                         ' table (?P<table>\w+)'
                         ' proto (?P<proto>\w+)'
                         ' scope (?P<scope>\w+)'
                         ' src (?P<src>[a-z0-9\.\:\/]+)'
                         )



        # Initializes the Python dictionary variable
        parsed_dict = {}


        # Defines the "for" loop, to pattern match each line of output

        for line in out.splitlines():
            line = line.strip()

            # default via 192.168.1.1 dev enp7s0 proto dhcp metric 100
            m = p1.match(line)
            if m:
                if 'routes' not in parsed_dict:
                    parsed_dict.setdefault('routes', {})

                group = m.groupdict()
                gateway = group['gateway']
                interface = group['device']
                metric = int(group['metric'])

                
                if gateway:
                    parsed_dict['routes'] = { '0.0.0.0': {
                                                'mask': {
                                                   '0.0.0.0': {
                                                       'nexthop': {
                                                           1:{
                                                               'gateway': gateway,
                                                               'interface': interface, 
                                                               'metric': metric
                                                              
                                                                }
                                                               
                                                               }
                                                           }
                                                       }
                                                   }
                                                } 

            # 169.254.0.0/16 dev enp7s0 scope link metric 1000 
            m = p2.match(line)
            if m:

                group = m.groupdict()
                destination = IPNetwork(group['destination'])
                
                mask = str(destination.netmask)
                destination_addr = str(destination.ip)
                interface = group['device']
                metric = int(group['metric'])
                scope = group['scope']
                index_dict = {'interface' : interface,
                              'scope' : scope,
                              'metric': metric
                              }
                
                index = 1
                parsed_dict['routes'].setdefault(destination_addr, {}).\
                        setdefault('mask', {}).\
                            setdefault(mask, {}).\
                                setdefault('nexthop', {index: index_dict})
            
            # 172.17.0.0/16 dev docker0 proto kernel scope link src 172.17.0.1
            m = p3.match(line)
            if m:

                group = m.groupdict()
                destination = IPNetwork(group['destination'])
                
                mask = str(destination.netmask)
                destination_addr = str(destination.ip)
                interface = group['device']
                scope = group['scope']
                proto = group['proto']
                src = group['src']
                index_dict = {'interface' : interface,
                              'scope' : scope,
                              'proto' : proto ,
                              'src' : src
                              }
                
                index = 1
                parsed_dict['routes'].setdefault(destination_addr, {}).\
                        setdefault('mask', {}).\
                            setdefault(mask, {}).\
                                setdefault('nexthop', {index: index_dict})

            # 172.18.0.0/16 dev br-d19b23fac393 proto kernel scope link src 172.18.0.1 linkdown 

            m = p4.match(line)
            if m:

                group = m.groupdict()
                destination = IPNetwork(group['destination'])
                
                mask = str(destination.netmask)
                destination_addr = str(destination.ip)
                interface = group['device']
                scope = group['scope']
                proto = group['proto']
                src = group['src']
                index_dict = {'interface' : interface,
                              'scope' : scope,
                              'proto' : proto ,
                              'src' : src
                              }
                
                index = 1
                parsed_dict['routes'].setdefault(destination_addr, {}).\
                        setdefault('mask', {}).\
                            setdefault(mask, {}).\
                                setdefault('nexthop', {index: index_dict})
            
            # 192.168.1.0/24 dev enp7s0 proto kernel scope link src 192.168.1.212 metric 100 
            m = p5.match(line)
            if m:

                group = m.groupdict()
                destination = IPNetwork(group['destination'])
                
                mask = str(destination.netmask)
                destination_addr = str(destination.ip)
                interface = group['device']
                scope = group['scope']
                proto = group['proto']
                metric = group['metric']
                src = group['src']
                index_dict = {'interface' : interface,
                              'scope' : scope,
                              'proto' : proto ,
                              'src' : src,
                              'metric': metric
                              }
                
                index = 1
                parsed_dict['routes'].setdefault(destination_addr, {}).\
                        setdefault('mask', {}).\
                            setdefault(mask, {}).\
                                setdefault('nexthop', {index: index_dict})
            
            # broadcast 127.0.0.0 dev lo table local proto kernel scope link src 127.0.0.1 
            m = p6.match(line)
            if m:

                group = m.groupdict()
                destination = IPNetwork(group['destination'])
                
                mask = str(destination.netmask)
                destination_addr = str(destination.ip)
                interface = group['device']
                scope = group['scope']
                proto = group['proto']
                src = group['src']
                table = group['table']
                
                index_dict = {'interface' : interface,
                              'scope' : scope,
                              'proto' : proto ,
                              'src' : src,
                              'broadcast': True,
                              'table': table
                              }
                
                index = 1
                parsed_dict['routes'].setdefault(destination_addr, {}).\
                        setdefault('mask', {}).\
                            setdefault(mask, {}).\
                                setdefault('nexthop', {index: index_dict})

            # local 10.233.44.70 dev kube-ipvs0 table local proto kernel scope host src 10.233.44.70
            m = p7.match(line)
            if m:

                group = m.groupdict()
                destination = IPNetwork(group['destination'])
                
                mask = str(destination.netmask)
                destination_addr = str(destination.ip)
                interface = group['device']
                scope = group['scope']
                proto = group['proto']
                src = group['src']
                table = group['table']
                
                index_dict = {'interface' : interface,
                              'scope' : scope,
                              'proto' : proto ,
                              'src' : src,
                              'local': True,
                              'table': table
                              }
                
                index = 1
                parsed_dict['routes'].setdefault(destination_addr, {}).\
                        setdefault('mask', {}).\
                            setdefault(mask, {}).\
                                setdefault('nexthop', {index: index_dict})

        return parsed_dict
