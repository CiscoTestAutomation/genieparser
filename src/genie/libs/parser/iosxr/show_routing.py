'''
show_route.py

'''
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional


# ====================================================
#  schema for show route ipv4
# ====================================================
class ShowRouteIpv4Schema(MetaParser):
    """Schema for show route ipv4"""
    schema = {
        'vrf': {
            Any(): {
                Optional('address_family'): {
                    Any(): {
                        Optional('routes'): {
                            Any(): {
                                Optional('route'): str,
                                Optional('active'): bool,
                                Optional('route_preference'): int,
                                Optional('metric'): int,
                                Optional('source_protocol'): str,
                                Optional('source_protocol_codes'): str,
                                Optional('next_hop'): {
                                    Optional('outgoing_interface'): {
                                        Any(): {  # interface  if there is no next_hop
                                            Optional('outgoing_interface'): str,
                                            Optional('updated'): str,
                                        },
                                    },
                                    Optional('next_hop_list'): {
                                        Any(): {  # index
                                            Optional('index'): int,
                                            Optional('next_hop'): str,
                                            Optional('outgoing_interface'): str,
                                            Optional('updated'): str,
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


# ====================================================
#  parser for show ip route
# ====================================================
class ShowRouteIpv4(ShowRouteIpv4Schema):
    """Parser for :
       show route ipv4
       show route vrf <vrf> ipv4"""
    cli_command = ['show route vrf {vrf} ipv4','show route ipv4']

    def cli(self, vrf="",output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[0].format(vrf=vrf)
            else:
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)
        else:
            out = output

        if not vrf:
            vrf = 'default'

        af = 'ipv4'
        route = ""
        source_protocol_dict = {}
        source_protocol_dict['ospf'] = ['O','IA','N1','N2','E1','E2']
        source_protocol_dict['odr'] = ['o']
        source_protocol_dict['isis'] = ['i','su','L1','L2','ia']
        source_protocol_dict['eigrp'] = ['D','EX']
        source_protocol_dict['static'] = ['S']
        source_protocol_dict['egp'] = ['E']
        source_protocol_dict['dagr'] = ['G']
        source_protocol_dict['rpl'] = ['r']
        source_protocol_dict['mobile router'] = ['M']
        source_protocol_dict['lisp'] = ['I']
        source_protocol_dict['nhrp'] = ['H']
        source_protocol_dict['local'] = ['L']
        source_protocol_dict['connected'] = ['C']
        source_protocol_dict['bgp'] = ['B']

        result_dict = {}
        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue
            next_hop = interface = updated = metrics = route_preference = ""

            # VRF: VRF501
            p1 = re.compile(r'^\s*VRF: +(?P<vrf>[\w]+)$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                continue

            # S    10.4.1.1/32 is directly connected, 01:51:13, GigabitEthernet0/0/0/0
            # S    10.36.3.3/32 [1/0] via 10.2.3.3, 01:51:13, GigabitEthernet0/0/0/1
            # B    10.19.31.31/32 [200/0] via 10.229.11.11, 00:55:14
            # i L1 10.76.23.23/32 [115/11] via 10.2.3.3, 00:52:41, GigabitEthernet0/0/0/1
            p3 = re.compile(r'^\s*(?P<code1>[\w]+) +(?P<code2>[\w]+)? +(?P<network>[\d\/\.]+)'
                            '( +is +directly +connected,)?( +\[(?P<route_preference>[\d\/]+)\]?'
                            '( +via )?(?P<next_hop>[\d\.]+)?,)?( +(?P<date>[0-9][\w\:]+))?,?( +(?P<interface>[\S]+))?$')
            m = p3.match(line)
            if m:
                active = True
                updated = ""
                if m.groupdict()['code1']:
                    source_protocol_codes = m.groupdict()['code1'].strip()
                    for key,val in source_protocol_dict.items():
                        if source_protocol_codes in val:
                            source_protocol = key

                if m.groupdict()['code2']:
                    source_protocol_codes = '{} {}'.format(source_protocol_codes, m.groupdict()['code2'])

                if m.groupdict()['network']:
                    route = m.groupdict()['network']

                if m.groupdict()['route_preference']:
                    routepreference = m.groupdict()['route_preference']
                    if '/' in routepreference:
                        route_preference = int(routepreference.split('/')[0])
                        metrics = routepreference.split('/')[1]

                index = 1
                if m.groupdict()['next_hop']:
                    next_hop = m.groupdict()['next_hop']
                if m.groupdict()['interface']:
                    interface = m.groupdict()['interface']

                if m.groupdict()['date']:
                    updated = m.groupdict()['date']

                if vrf:
                    if 'vrf' not in result_dict:
                        result_dict['vrf'] = {}

                    if vrf not in result_dict['vrf']:
                        result_dict['vrf'][vrf] = {}

                    if 'address_family' not in result_dict['vrf'][vrf]:
                        result_dict['vrf'][vrf]['address_family'] = {}

                    if af and af not in result_dict['vrf'][vrf]['address_family']:
                        result_dict['vrf'][vrf]['address_family'][af] = {}

                    if 'routes' not in result_dict['vrf'][vrf]['address_family'][af]:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'] = {}
                    if route not in result_dict['vrf'][vrf]['address_family'][af]['routes']:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] = {}

                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['route'] = route

                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['active'] = active

                    if metrics:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['metric'] = int(metrics)
                    if route_preference:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['route_preference'] = route_preference
                    if source_protocol_codes:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['source_protocol_codes'] = source_protocol_codes
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['source_protocol'] = source_protocol

                    if 'next_hop' not in result_dict['vrf'][vrf]['address_family'][af]['routes'][route]:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] = {}

                    if not next_hop:

                        if 'outgoing_interface' not in result_dict['vrf'][vrf]['address_family'][af] \
                                ['routes'][route]['next_hop']:
                            result_dict['vrf'][vrf]['address_family'][af]['routes'][route]\
                                ['next_hop']['outgoing_interface'] = {}

                        if m.groupdict()['interface'] and interface not in \
                                result_dict['vrf'][vrf]['address_family'][af]['routes'][route]\
                                ['next_hop']['outgoing_interface']:
                            result_dict['vrf'][vrf]['address_family'][af]['routes'][route]\
                                ['next_hop']['outgoing_interface'][interface] = {}

                        if interface:
                            result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                                ['next_hop']['outgoing_interface'][interface]['outgoing_interface'] = interface
                        if updated:
                            result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                                ['next_hop']['outgoing_interface'][interface]['updated'] = updated

                    else:
                        if 'next_hop_list' not in result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop']:
                            result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'][
                                'next_hop_list'] = {}


                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index] = {}

                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index]['index'] = index

                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index]['next_hop'] = next_hop

                        if updated:
                            result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                                ['next_hop_list'][index]['updated'] = updated

                        if interface:
                            result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                                ['next_hop_list'][index]['outgoing_interface'] = interface

                continue

            #    [110/2] via 10.1.2.1, 01:50:49, GigabitEthernet0/0/0/3
            p4 = re.compile(r'^\s*\[(?P<route_preference>[\d\/]+)\]'
                            ' +via +(?P<next_hop>[\d\.]+)?,?( +(?P<date>[0-9][\w\:]+),)?( +(?P<interface>[\S]+))?$')
            m = p4.match(line)
            if m:
                updated = ""
                routepreference = m.groupdict()['route_preference']
                if '/' in routepreference:
                    route_preference = int(routepreference.split('/')[0])
                    metrics = routepreference.split('/')[1]

                next_hop = m.groupdict()['next_hop']
                index += 1
                if m.groupdict()['interface']:
                    interface = m.groupdict()['interface']

                if m.groupdict()['date']:
                    updated = m.groupdict()['date']

                if 'routes' not in result_dict['vrf'][vrf]['address_family'][af]:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'] = {}
                if route not in result_dict['vrf'][vrf]['address_family'][af]['routes']:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] = {}

                result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['route'] = route

                result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                    ['active'] = active

                if metrics:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['metric'] = int(metrics)
                if route_preference:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['route_preference'] = route_preference
                if source_protocol_codes:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['source_protocol_codes'] = source_protocol_codes
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['source_protocol'] = source_protocol

                if 'next_hop' not in result_dict['vrf'][vrf]['address_family'][af]['routes'][route]:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] = {}

                if not next_hop:
                    if 'outgoing_interface' not in result_dict['vrf'][vrf]['address_family'][af] \
                            ['routes'][route]['next_hop']:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['next_hop']['outgoing_interface'] = {}

                    if m.groupdict()['interface'] and interface not in result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['next_hop']['outgoing_interface']:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['next_hop']['outgoing_interface'][interface] = {}

                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['outgoing_interface'][interface]['outgoing_interface'] = interface
                    if updated:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['next_hop']['outgoing_interface'][interface]['updated'] = updated

                else:
                    if 'next_hop_list' not in result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop']:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'][
                            'next_hop_list'] = {}

                    if index not in result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list']:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index] = {}

                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                        ['next_hop_list'][index]['index'] = index

                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                        ['next_hop_list'][index]['next_hop'] = next_hop

                    if updated:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index]['updated'] = updated

                    if interface:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index]['outgoing_interface'] = interface

                continue

            #       is directly connected, 01:51:13, GigabitEthernet0/0/0/3
            p4 = re.compile(r'^\s*is +directly +connected,'
                            '( +(?P<date>[0-9][\w\:]+),)?( +(?P<interface>[\S]+))?$')
            m = p4.match(line)
            if m:
                updated = ""
                if m.groupdict()['interface']:
                    interface = m.groupdict()['interface']

                if m.groupdict()['date']:
                    updated = m.groupdict()['date']


                if 'outgoing_interface' not in result_dict['vrf'][vrf]['address_family'][af] \
                        ['routes'][route]['next_hop']:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['outgoing_interface'] = {}

                if m.groupdict()['interface'] and interface not in \
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                                ['next_hop']['outgoing_interface']:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['outgoing_interface'][interface] = {}

                result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                    ['next_hop']['outgoing_interface'][interface]['outgoing_interface'] = interface
                if updated:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['outgoing_interface'][interface]['updated'] = updated

                continue

        return result_dict


# ====================================================
#  parser for show route ipv6
# ====================================================

class ShowRouteIpv6(ShowRouteIpv4Schema):
    """Parser for :
       show route ipv6
       show route vrf <vrf> ipv6"""
    cli_command = ['show route vrf {vrf} ipv6', 'show route ipv6']

    def cli(self, vrf="", output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[0].format(vrf=vrf)
            else:
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)
        else:
            out = output

        if not vrf:
            vrf = 'default'

        af = 'ipv6'
        route = ""
        next_hop = interface = metrics = route_preference = ""
        source_protocol_dict = {}
        source_protocol_dict['ospf'] = ['O', 'IA', 'N1', 'N2', 'E1', 'E2']
        source_protocol_dict['odr'] = ['o']
        source_protocol_dict['isis'] = ['i', 'su', 'L1', 'L2', 'ia']
        source_protocol_dict['eigrp'] = ['D', 'EX']
        source_protocol_dict['static'] = ['S']
        source_protocol_dict['egp'] = ['E']
        source_protocol_dict['dagr'] = ['G']
        source_protocol_dict['rpl'] = ['r']
        source_protocol_dict['mobile router'] = ['M']
        source_protocol_dict['lisp'] = ['I']
        source_protocol_dict['nhrp'] = ['H']
        source_protocol_dict['local'] = ['L']
        source_protocol_dict['connected'] = ['C']
        source_protocol_dict['bgp'] = ['B']

        result_dict = {}
        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            # VRF: VRF501
            p1 = re.compile(r'^\s*VRF: +(?P<vrf>[\w]+)$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                continue

            # S    2001:1:1:1::1/128
            # L    2001:2:2:2::2/128 is directly connected,
            #i L1 2001:23:23:23::23/128
            p2 = re.compile(r'^\s*(?P<code1>[\w]+)( +(?P<code2>[\w]+))? +(?P<route>[\w\/\:]+)'
                            '( +is +directly +connected,)?$')
            m = p2.match(line)
            if m:
                active = True
                if m.groupdict()['code1']:
                    source_protocol_codes = m.groupdict()['code1'].strip()
                    for key, val in source_protocol_dict.items():
                        if source_protocol_codes in val:
                            source_protocol = key

                if m.groupdict()['code2']:
                    source_protocol_codes = '{} {}'.format(source_protocol_codes, m.groupdict()['code2'])


                if m.groupdict()['route']:
                    route = m.groupdict()['route']

                index = 1

                if vrf:
                    if 'vrf' not in result_dict:
                        result_dict['vrf'] = {}

                    if vrf not in result_dict['vrf']:
                        result_dict['vrf'][vrf] = {}

                    if 'address_family' not in result_dict['vrf'][vrf]:
                        result_dict['vrf'][vrf]['address_family'] = {}

                    if af and af not in result_dict['vrf'][vrf]['address_family']:
                        result_dict['vrf'][vrf]['address_family'][af] = {}

                    if 'routes' not in result_dict['vrf'][vrf]['address_family'][af]:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'] = {}
                    if route not in result_dict['vrf'][vrf]['address_family'][af]['routes']:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] = {}

                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['route'] = route

                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['active'] = active

                    if source_protocol_codes:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['source_protocol_codes'] = source_protocol_codes
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['source_protocol'] = source_protocol
                continue

            #   [1/0] via 2001:20:1:2::1, 01:52:23, GigabitEthernet0/0/0/0
            #   [200/0] via ::ffff:10.229.11.11 (nexthop in vrf default), 00:55:12
            p3 = re.compile(r'^\s*\[(?P<route_preference>[\d\/]+)\]'
                            ' +via +(?P<next_hop>[\w\:\.)]+)?( \(nexthop in vrf default\))?,? +(?P<date>[0-9][\w\:]+)?,?( +(?P<interface>[\S]+))?$')
            m = p3.match(line)
            if m:
                updated = interface = ""
                routepreference = m.groupdict()['route_preference']
                if '/' in routepreference:
                    route_preference = int(routepreference.split('/')[0])
                    metrics = routepreference.split('/')[1]

                if m.groupdict()['next_hop']:
                    next_hop = m.groupdict()['next_hop']

                if m.groupdict()['interface']:
                    interface = m.groupdict()['interface']

                if m.groupdict()['date']:
                    updated = m.groupdict()['date']

                if 'vrf' not in result_dict:
                    result_dict['vrf'] = {}

                if vrf not in result_dict['vrf']:
                    result_dict['vrf'][vrf] = {}

                if 'address_family' not in result_dict['vrf'][vrf]:
                    result_dict['vrf'][vrf]['address_family'] = {}

                if af and af not in result_dict['vrf'][vrf]['address_family']:
                    result_dict['vrf'][vrf]['address_family'][af] = {}
                if 'routes' not in result_dict['vrf'][vrf]['address_family'][af]:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'] = {}
                if route not in result_dict['vrf'][vrf]['address_family'][af]['routes']:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] = {}

                result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['route'] = route
                if metrics:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['metric'] = int(metrics)
                if route_preference:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['route_preference'] = route_preference


                if 'next_hop' not in result_dict['vrf'][vrf]['address_family'][af]['routes'][route]:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] = {}

                if not next_hop:
                    if 'outgoing_interface' not in result_dict['vrf'][vrf]['address_family'][af] \
                            ['routes'][route]['next_hop']:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['next_hop']['outgoing_interface'] = {}

                    if m.groupdict()['interface'] and interface not in result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['next_hop']['outgoing_interface']:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['next_hop']['outgoing_interface'][interface] = {}

                    if interface:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['next_hop']['outgoing_interface'][interface]['outgoing_interface'] = interface
                    if updated:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['next_hop']['outgoing_interface'][interface]['updated'] = updated

                else:
                    if 'next_hop_list' not in result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop']:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'][
                            'next_hop_list'] = {}

                    if index not in result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list']:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index] = {}

                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                        ['next_hop_list'][index]['index'] = index

                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                        ['next_hop_list'][index]['next_hop'] = next_hop

                    if interface:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index]['outgoing_interface'] = interface

                    if updated:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index]['updated'] = updated
                index += 1
                continue

            #   01:52:24, Loopback0
            p4 = re.compile(r'^\s*(?P<date>[\w\:]+),'
                            ' +(?P<interface>[\S]+)$')
            m = p4.match(line)
            if m:
                interface = updated = ""
                if m.groupdict()['interface']:
                    interface = m.groupdict()['interface']

                if m.groupdict()['date']:
                    updated = m.groupdict()['date']


                if 'vrf' not in result_dict:
                    result_dict['vrf'] = {}

                if vrf not in result_dict['vrf']:
                    result_dict['vrf'][vrf] = {}

                if 'address_family' not in result_dict['vrf'][vrf]:
                    result_dict['vrf'][vrf]['address_family'] = {}

                if af and af not in result_dict['vrf'][vrf]['address_family']:
                    result_dict['vrf'][vrf]['address_family'][af] = {}
                if 'routes' not in result_dict['vrf'][vrf]['address_family'][af]:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'] = {}
                if route not in result_dict['vrf'][vrf]['address_family'][af]['routes']:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] = {}

                result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['route'] = route

                if 'next_hop' not in result_dict['vrf'][vrf]['address_family'][af]['routes'][route]:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] = {}

                if 'outgoing_interface' not in result_dict['vrf'][vrf]['address_family'][af] \
                        ['routes'][route]['next_hop']:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['outgoing_interface'] = {}

                if m.groupdict()['interface'] and interface not in \
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                                ['next_hop']['outgoing_interface']:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['outgoing_interface'][interface] = {}

                if interface:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['outgoing_interface'][interface]['outgoing_interface'] = interface
                if updated:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['outgoing_interface'][interface]['updated'] = updated


                continue

        return result_dict