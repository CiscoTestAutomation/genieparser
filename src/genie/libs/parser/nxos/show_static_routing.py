"""show_static_route.py

"""
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional

# ====================================================
#  schema for show ip static-route
# ====================================================
class ShowIpStaticRouteSchema(MetaParser):
    """Schema for show ip static-route"""
    schema = {
        'vrf': {
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
                                           Optional('rnh_active'): bool,
                                       },
                                   },
                                   Optional('next_hop_list'): {
                                       Any(): {     # index
                                           Optional('index'): int,
                                           Optional('active'): bool,
                                           Optional('next_hop'): str,
                                           Optional('next_hop_netmask'): str,
                                           Optional('outgoing_interface'): str,
                                           Optional('rnh_active'): bool,
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
#  parser for show ip static-route
# ====================================================
class ShowIpStaticRoute(ShowIpStaticRouteSchema):
    """Parser for:
       show ip static-route
       show ip static-route vrf <vrf>
       show ip static-route vrf all
    """
    cli_command = ['show ip static-route vrf {vrf}','show ip static-route']

    def cli(self, vrf='', output=None):
        if vrf and vrf != 'default':
            cmd = self.cli_command[0].format(vrf=vrf)
        else:
            vrf = 'default'
            cmd = self.cli_command[1]

        # excute command to get output
        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output

        af = 'ipv4'
        vrf = route = next_hop = ""

        result_dict = {}
        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            # Static-route for VRF "default"(1)
            p1 = re.compile(r'^\s*Static-route +for +VRF +\"(?P<vrf>[\w]+)\"\((?P<number>[\d])\)$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                if 'vrf' not in result_dict:
                    result_dict['vrf'] = {}

                if vrf not in result_dict['vrf']:
                    result_dict['vrf'][vrf] = {}

                if 'address_family' not in result_dict['vrf'][vrf]:
                    result_dict['vrf'][vrf]['address_family'] = {}

                if af and af not in result_dict['vrf'][vrf]['address_family']:
                    result_dict['vrf'][vrf]['address_family'][af] = {}
                continue

            #  2.2.2.2/32, configured nh: 10.2.3.2/32 Ethernet1/4
            #  2.2.2.2/32, configured nh: 20.2.3.2/32
            # 200.0.5.1/32, configured nh: 0.0.0.0/32 tunnel-te12
            p2 = re.compile(r'^\s*(?P<route>[\d\/\.]+),'
                             ' +configured +nh: +(?P<nexthop>[\d\/\.]+)?( +(?P<interface>[a-zA-Z][\w\-\/\.]+))?$')
            m = p2.match(line)
            if m:
                next_hop = ""
                if m.groupdict()['route']:
                    if route == m.groupdict()['route']:
                        index += 1
                    else:
                        route = m.groupdict()['route']
                        index = 1
                if m.groupdict()['interface']:
                    interface = m.groupdict()['interface']
                if m.groupdict()['nexthop']:
                    next_hop_origin = m.groupdict()['nexthop']
                    if '/' in next_hop_origin:
                        next_hop_split = next_hop_origin.split('/')

                        next_hop = next_hop_split[0]
                        next_hop_netmask = next_hop_split[1]


                if 'routes' not in result_dict['vrf'][vrf]['address_family'][af]:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'] = {}
                if route not in result_dict['vrf'][vrf]['address_family'][af]['routes']:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] = {}
                result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['route'] = route

                if 'next_hop' not in result_dict['vrf'][vrf]['address_family'][af]['routes'][route]:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] = {}

                if not next_hop:
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

                else:
                    if 'next_hop_list' not in result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop']:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop']['next_hop_list'] = {}

                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                        ['next_hop_list'][index] = {}

                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                        ['next_hop_list'][index]['index'] = index

                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                        ['next_hop_list'][index]['next_hop'] = next_hop.strip()
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                        ['next_hop_list'][index]['next_hop_netmask'] = next_hop_netmask

                    if m.groupdict()['interface']:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index]['outgoing_interface'] = interface

                continue

            # (not installed in urib)
            p3 = re.compile(r'^\s*\(not +installed +in +(?P<urib>[\w]+)\)$')
            m = p3.match(line)
            if m:
                active = False
                if not next_hop:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['outgoing_interface'][interface]['active'] = active
                else:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['next_hop_list'][index]['active'] = active
                continue

            # (installed in urib)
            p4 = re.compile(r'^\s*\(installed +in +(?P<urib>[\w]+)\)$')
            m = p4.match(line)
            if m:
                active = True
                if not next_hop:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['outgoing_interface'][interface]['active'] = active
                else:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['next_hop_list'][index]['active'] = active
                continue

            #rnh(installed in urib)
            p5 = re.compile(r'^\s*rnh\(installed +in +(?P<urib>[\w]+)\)$')
            m = p5.match(line)
            if m:
                active = True
                if not next_hop:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['outgoing_interface'][interface]['rnh_active'] = active
                else:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['next_hop_list'][index]['rnh_active'] = active
                continue

        return result_dict


# ====================================================
#  schema for show ipv6 static-static
# ====================================================
class ShowIpv6StaticRouteSchema(MetaParser):
    """chema for show ipv6 static-static"""
    schema = {
        'vrf': {
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
                                           Optional('preference'): int,
                                           Optional('resolved_tid'): int,
                                           Optional('bfd_enabled'): bool,
                                           Optional('rnh_active'): bool,
                                           Optional('next_hop_vrf'): str,
                                       },
                                   },
                                   Optional('next_hop_list'): {
                                       Any(): {     # index
                                           Optional('index'): int,
                                           Optional('next_hop'): str,
                                           Optional('next_hop_netmask'): str,
                                           Optional('outgoing_interface'): str,
                                           Optional('resolved_tid'): int,
                                           Optional('preference'): int,
                                           Optional('bfd_enabled'): bool,
                                           Optional('next_hop_vrf'): str,
                                           Optional('rnh_active'): bool,
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
#  parser for show ipv6 static-route
# ====================================================
class ShowIpv6StaticRoute(ShowIpv6StaticRouteSchema):
    """Parser for:
        show ipv6 static-route
        show ipv6 static-route vrf <vrf>
        show ipv6 static-route vrf all"""

    cli_command = ['show ipv6 static-route vrf {vrf}', 'show ipv6 static-route']

    def cli(self, vrf='', output=None):
        if vrf:
            cmd = self.cli_command[0].format(vrf=vrf)
        else:
            cmd = self.cli_command[1]

        # excute command to get output
        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output

        af = 'ipv6'
        vrf = route = interface = next_hop = ""

        result_dict = {}
        for line in out.splitlines():
            if line:
                line = line.strip()
            else:
                continue

            # IPv6 Configured Static Routes for VRF "default"(1)
            p1 = re.compile(r'^\s*IPv6 +Configured +Static +Routes +for +VRF +\"(?P<vrf>[\w]+)\"\((?P<index>\d)\)$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                if vrf:
                    if 'vrf' not in result_dict:
                        result_dict['vrf'] = {}

                    if vrf not in result_dict['vrf']:
                        result_dict['vrf'][vrf] = {}

                    if 'address_family' not in result_dict['vrf'][vrf]:
                        result_dict['vrf'][vrf]['address_family'] = {}

                    if af and af not in result_dict['vrf'][vrf]['address_family']:
                        result_dict['vrf'][vrf]['address_family'][af] = {}
                continue

            # 2001:1:1:1::1/128 -> 2001:10:1:3::1/128, preference: 1
            # 2001:1:1:1::1/128 -> Null0, preference: 1
            p2 = re.compile(r'^\s*(?P<route>[\d\/\:]+)( +\-\> +(?P<nexthop>[\d\:\/]+), )?'
                            '( \-\> +(?P<interface>[\w\.\/]+), )?'
                            '(preference: +(?P<preference>[\d]+))?$')
            m = p2.match(line)
            if m:
                next_hop = ""
                if m.groupdict()['route']:
                    if route == m.groupdict()['route']:
                        index += 1
                    else:
                        route = m.groupdict()['route']
                        index = 1

                if m.groupdict()['preference']:
                    if_preference = m.groupdict()['preference']
                if m.groupdict()['nexthop']:
                    next_hop_origin = m.groupdict()['nexthop']
                    if '/' in next_hop_origin:
                        next_hop_split = next_hop_origin.split('/')

                        next_hop = next_hop_split[0]
                        next_hop_netmask = next_hop_split[1]

                if m.groupdict()['interface']:
                    interface = m.groupdict()['interface']

                if 'routes' not in result_dict['vrf'][vrf]['address_family'][af]:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'] = {}
                if route not in result_dict['vrf'][vrf]['address_family'][af]['routes']:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] = {}
                result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['route'] = route

                if 'next_hop' not in result_dict['vrf'][vrf]['address_family'][af]['routes'][route]:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] = {}

                if not next_hop:
                    if 'outgoing_interface' not in result_dict['vrf'][vrf]['address_family'][af]\
                            ['routes'][route]['next_hop']:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]\
                            ['next_hop']['outgoing_interface'] = {}

                    if m.groupdict()['interface'] and interface not in result_dict['vrf']\
                            [vrf]['address_family'][af]['routes'][route]\
                            ['next_hop']['outgoing_interface']:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]\
                            ['next_hop']['outgoing_interface'][interface] = {}

                    if m.groupdict()['interface']:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['next_hop']['outgoing_interface'][interface]['outgoing_interface'] = interface

                    if m.groupdict()['interface']:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['next_hop']['outgoing_interface'][interface]['preference'] = int(if_preference)


                else:
                    if 'next_hop_list' not in result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop']:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop']['next_hop_list'] = {}

                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop']['next_hop_list'][index] = {}

                    if m.groupdict('preference'):
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index]['preference'] = int(if_preference)

                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop']\
                        ['next_hop_list'][index]['index'] = index

                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop']\
                        ['next_hop_list'][index]['next_hop'] = next_hop.strip()
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                        ['next_hop_list'][index]['next_hop_netmask'] = next_hop_netmask

                    if m.groupdict()['interface']:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop']\
                            ['next_hop_list'][index]['outgoing_interface'] = interface



                continue

            #  nh_vrf(default) reslv_tid 0
            p3 = re.compile(r'^\s*nh_vrf\((?P<next_vrf>[\w]+)\) +reslv_tid +(?P<resolved_tid>[\d]+)$')
            m = p3.match(line)
            if m:
                next_vrf = m.groupdict()['next_vrf']
                resolved_tid = m.groupdict()['resolved_tid']
                if next_hop:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                        ['next_hop_list'][index]['next_hop_vrf'] = next_vrf

                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                        ['next_hop_list'][index]['resolved_tid'] = int(resolved_tid)
                else:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                        ['outgoing_interface'][interface]['next_hop_vrf'] = next_vrf
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                        ['outgoing_interface'][interface]['resolved_tid'] = int(resolved_tid)

                continue

            # real-next-hop: 2001:10:2:3::2, interface: Ethernet1/4
            p4 = re.compile(r'^\s*real-next-hop: +(?P<real_next_hop>[\d\:]+)'
                            '(, +interface: +(?P<interface2>[\w\/\.]+))?$')
            m = p4.match(line)
            if m:
                if m.groupdict()['interface2']:
                    interface2 = m.groupdict()['interface2']
                if m.groupdict()['real_next_hop'] and '0' not in m.groupdict()['real_next_hop']:
                    real_next_hop = m.groupdict()['real_next_hop']

                if not interface and m.groupdict()['interface2']:
                    if not next_hop:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['next_hop']['outgoing_interface'][interface2]['outgoing_interface'] = interface2
                    else:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop']\
                            ['next_hop_list'][index]['outgoing_interface'] = interface2
                continue

            # rnh(installed in u6rib)
            # rnh(not installed in u6rib)
            p5 = re.compile(r'^\s*rnh\((?P<not>[not]+)? ?installed +in +(?P<urib>[\w]+)\)$')
            m = p5.match(line)
            if m:
                if m.groupdict()['not']:
                    rnh_active = False
                else:
                    rnh_active = True
                if not next_hop:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['outgoing_interface'][interface]['rnh_active'] = rnh_active
                else:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['next_hop_list'][index]['rnh_active'] = rnh_active
                continue

            #  bfd_enabled no
            p6 = re.compile(r'^\s*bfd_enabled +(?P<bfd>[\w]+)$')
            m = p6.match(line)
            if m:
                bfd_enabled = False if m.groupdict()['bfd'].lower() == 'no' else True
                if not next_hop:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['outgoing_interface'][interface]['bfd_enabled'] = bfd_enabled
                else:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['next_hop_list'][index]['bfd_enabled'] = bfd_enabled
                continue


        if result_dict:
            for i in list(result_dict['vrf']):
                if not len(result_dict['vrf'][i]['address_family'][af]):
                    del result_dict['vrf'][i]


        return result_dict