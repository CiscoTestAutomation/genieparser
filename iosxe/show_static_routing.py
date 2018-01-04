'''
show_static_route.py

'''
import re
from metaparser import MetaParser
# parser utils
from parser.utils.common import Common
from metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional

# ====================================================
#  schema for show ip static route
# ====================================================
class ShowIpStaticRouteSchema(MetaParser):
    schema = {
        'vrfs': {
            Any(): {
                Optional('address_family'): {
                   Any(): {
                       Optional('routes'): {
                           Any(): {
                               Optional('route'): str,
                               Optional('next_hop'): {
                                   Optional('outgoing_interface'): {
                                       Any(): {    # interface  if there is no next_hop
                                           Optional('outgoing_interface'): str,
                                           Optional('active'): bool,
                                           Optional('preference'): int,
                                       },
                                   },
                                   Optional('next_hop_list'): {
                                       Any(): {     # index
                                           Optional('index'): int,
                                           Optional('active'): bool,
                                           Optional('next_hop'): str,
                                           Optional('outgoing_interface'): str,
                                           Optional('preference'): int,
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
#  parser for show ip static route
# ====================================================
class ShowIpStaticRoute(ShowIpStaticRouteSchema):
    '''
       show ip static route
       show ip static route vrf <vrf>
    '''
    def cli(self, vrf=""):
        if vrf:
            cmd = 'show ip static route vrf {}'.format(vrf)
        else:
            cmd = 'show ip static route'
        out = self.device.execute(cmd)

        af = 'ipv4'
        vrf = route = next_hop = ""

        result_dict = {}
        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue
            # Static local RIB for default
            p1 = re.compile(r'^\s*Static +local +RIB +for +(?P<vrf>[\w]+)$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']

                continue

            # M  2.2.2.2/32 [1/0] via GigabitEthernet0/0 10.1.2.2 [A]
            # M             [2/0] via GigabitEthernet0/1 20.1.2.2 [N]
            # M             [3/0] via 20.1.2.2 [N]
            # M  3.3.3.3/32 [1/0] via GigabitEthernet0/2 [A]
            # M             [1/0] via GigabitEthernet0/3 [A]
            p2 = re.compile(r'^\s*(?P<code>[A-Z]+) +(?P<route>[\w\/\.]+)?'
                             ' +\[(?P<if_preference>[\d]+)\/(?P<if_preference2>[\d]+)\]'
                             ' +via +(?P<interface>[a-zA-Z][\w\/\.]+)?(?P<nexthop>[\d\s\.]+)?'
                             ' +\[(?P<code_in_bracket>[\w])]$')
            m = p2.match(line)
            if m:
                code = m.groupdict()['code']
                next_hop = ""
                if m.groupdict()['route']:
                    route1 = m.groupdict()['route']
                    network, netmask = Common.cidr_to_netmask(route1)
                    route = "{0}/{1}".format(network, netmask)
                    index = 1
                else:
                    index += 1
                if_preference = m.groupdict()['if_preference']
                interface = m.groupdict()['interface']
                if m.groupdict()['nexthop']:
                    next_hop = m.groupdict()['nexthop']

                code_in_bracket = m.groupdict()['code_in_bracket']

                if vrf:
                    if 'vrfs' not in result_dict:
                        result_dict['vrfs'] = {}

                    if vrf not in result_dict['vrfs']:
                        result_dict['vrfs'][vrf] = {}

                    if 'address_family' not in result_dict['vrfs'][vrf]:
                        result_dict['vrfs'][vrf]['address_family'] = {}

                    if af and af not in result_dict['vrfs'][vrf]['address_family']:
                        result_dict['vrfs'][vrf]['address_family'][af] = {}

                    if 'routes' not in result_dict['vrfs'][vrf]['address_family'][af]:
                        result_dict['vrfs'][vrf]['address_family'][af]['routes'] = {}
                    if route not in result_dict['vrfs'][vrf]['address_family'][af]['routes']:
                        result_dict['vrfs'][vrf]['address_family'][af]['routes'][route] = {}
                    result_dict['vrfs'][vrf]['address_family'][af]['routes'][route]['route'] = route

                    if 'next_hop' not in result_dict['vrfs'][vrf]['address_family'][af]['routes'][route]:
                        result_dict['vrfs'][vrf]['address_family'][af]['routes'][route]['next_hop'] = {}

                    if not next_hop:
                        if 'outgoing_interface' not in result_dict['vrfs'][vrf]['address_family'][af]\
                                ['routes'][route]['next_hop']:
                            result_dict['vrfs'][vrf]['address_family'][af]['routes'][route]\
                                ['next_hop']['outgoing_interface'] = {}

                        if interface not in result_dict['vrfs'][vrf]['address_family'][af]['routes'][route]\
                                ['next_hop']['outgoing_interface']:
                            result_dict['vrfs'][vrf]['address_family'][af]['routes'][route]\
                                ['next_hop']['outgoing_interface'][interface] = {}
                        result_dict['vrfs'][vrf]['address_family'][af]['routes'][route] \
                            ['next_hop']['outgoing_interface'][interface]['outgoing_interface'] = interface

                        result_dict['vrfs'][vrf]['address_family'][af]['routes'][route] \
                            ['next_hop']['outgoing_interface'][interface]['active'] = True if code_in_bracket == 'A' else False

                        result_dict['vrfs'][vrf]['address_family'][af]['routes'][route] \
                            ['next_hop']['outgoing_interface'][interface]['preference'] = int(if_preference)

                    else:
                        if 'next_hop_list' not in result_dict['vrfs'][vrf]['address_family'][af]['routes'][route]['next_hop']:
                            result_dict['vrfs'][vrf]['address_family'][af]['routes'][route]['next_hop']['next_hop_list'] = {}

                        if int(if_preference):
                            if_preference_int = int(if_preference)
                            result_dict['vrfs'][vrf]['address_family'][af]['routes'][route]['next_hop']\
                                ['next_hop_list'][index] = {}

                        result_dict['vrfs'][vrf]['address_family'][af]['routes'][route]['next_hop']\
                            ['next_hop_list'][index]['index'] = index

                        result_dict['vrfs'][vrf]['address_family'][af]['routes'][route]['next_hop']\
                            ['next_hop_list'][index]['active'] = True if code_in_bracket == 'A' else False

                        result_dict['vrfs'][vrf]['address_family'][af]['routes'][route]['next_hop']\
                            ['next_hop_list'][index]['next_hop'] = next_hop.strip()

                        if interface:
                            result_dict['vrfs'][vrf]['address_family'][af]['routes'][route]['next_hop']\
                                ['next_hop_list'][index]['outgoing_interface'] = interface
                        result_dict['vrfs'][vrf]['address_family'][af]['routes'][route]['next_hop']\
                            ['next_hop_list'][index]['preference'] = if_preference_int
                continue

        return result_dict

