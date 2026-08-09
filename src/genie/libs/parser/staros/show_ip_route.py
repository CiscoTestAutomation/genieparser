"""starOS implementation of show_ip_route.py

"""
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Or, Schema

class ShowIpRouteSchema(MetaParser):
    """Schema ip route"""

    schema = {
        'ip_route': {
            Any():{
                'DESTINATION': str,
                'NEXTHOP': str,
                'PROTOCOL': str,
                'PREC': str,
                'COST': str,
                'INTERFACE': str,
            },
            'Summary':{
                'TOTAL': str,
                'UNIQUE': str,
                'CONNECTED': str,
                'STATIC': str,
            },
        },
    }


class ShowIpRoute(ShowIpRouteSchema):
    """Parser for show ip route"""

    cli_command = 'show ip route'

    """
[local]ASU-ASR5K5-1# show ip route
Friday December 22 20:56:24 ART 2023
"*" indicates the Best or Used route.  S indicates Stale.

 Destination         Nexthop          Protocol   Prec Cost Interface
*0.0.0.0/0           192.168.45.137   static     1    0    LOCAL1              
*192.168.45.136/29   0.0.0.0          connected  0    0    LOCAL1              
*192.168.45.140/32   0.0.0.0          connected  0    0    LOCAL1              

Total route count : 3
Unique route count: 3
Connected: 2 (Framed Route: 0) Static: 1
    """

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        ip_route_dict = {}
        
        result_dict = {}

        # initial regexp pattern
        #p0 = re.compile(r'((?P<destination>.\d+\.\d+\.\d+\.\d+\/\d+)\s+(?P<nexthop>\d+\.\d+\.\d+\.\d+)\s+(?P<protocol>\S+)\s+(?P<prec>\d+)\s+(?P<cost>\d+)\s+(?P<interface>\S+)|(?P<totalroute>Total route count\s*:\s*(\d+))|(?P<uniqueroute>Unique route count\s*:\s*(\d+))|(?P<connected>Connected:\s*(\d+))|(?P<static>Static:\s*(\d+)))')
        p0 = re.compile(r'((?P<destination>.\d+\.\d+\.\d+\.\d+\/\d+)\s+(?P<nexthop>\d+\.\d+\.\d+\.\d+)\s+(?P<protocol>\S+)\s+(?P<prec>\d+)\s+(?P<cost>\d+)\s+(?P<interface>\S+))')
        p1 = re.compile(r'(Total\sroute\scount\s:\s+(?P<total_route>\d+))')
        p2 = re.compile(r'(Unique\sroute\scount:\s+(?P<unique_route>\d+))')
        p3 = re.compile(r'(Connected:\s+(?P<connected>\d+)\s+\S+\s\S+\s+\S+\sStatic:\s+(?P<static>\S))')

        contador = 1

        for line in out.splitlines():
            #Quita espacios al inicio y al final
            line = line.strip()

            m = p0.match(line)
            if m:
                if 'ip_route' not in ip_route_dict:
                    result_dict = ip_route_dict.setdefault('ip_route',{})
                destination = m.groupdict()['destination']
                result_dict[contador] = {}
                result_dict[contador]['DESTINATION'] = destination
                nexthop = m.groupdict()['nexthop']
                result_dict[contador]['NEXTHOP'] = nexthop
                protocol = m.groupdict()['protocol']
                result_dict[contador]['PROTOCOL'] = protocol
                prec = m.groupdict()['prec']
                result_dict[contador]['PREC'] = prec
                cost = m.groupdict()['cost']
                result_dict[contador]['COST'] = cost
                interface = m.groupdict()['interface']
                result_dict[contador]['INTERFACE'] = interface
                contador += 1

            m = p1.match(line)
            if m:
                if 'ip_route' not in ip_route_dict:
                    result_dict = ip_route_dict.setdefault('ip_route',{})
                if 'Summary' not in ip_route_dict['ip_route']:
                    result_dict.setdefault('Summary',{})    
                totalroute = m.groupdict()['total_route']
                result_dict['Summary']['TOTAL'] = totalroute
            
            m = p2.match(line)
            if m:
                if 'ip_route' not in ip_route_dict:
                    result_dict = ip_route_dict.setdefault('ip_route',{})
                if 'Summary' not in ip_route_dict['ip_route']:
                    result_dict.setdefault('Summary',{}) 
                uniqueroute = m.groupdict()['unique_route']
                result_dict['Summary']['UNIQUE'] = uniqueroute
                
            
            m = p3.match(line)
            if m:
                if 'ip_route' not in ip_route_dict:
                    result_dict = ip_route_dict.setdefault('ip_route',{})
                if 'Summary' not in ip_route_dict['ip_route']:
                    result_dict.setdefault('Summary',{})     
                connected = m.groupdict()['connected']
                result_dict['Summary']['CONNECTED'] = connected    
                static = m.groupdict()['static']
                result_dict['Summary']['STATIC'] = static

        return ip_route_dict
