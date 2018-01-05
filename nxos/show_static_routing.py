'''
show_static_route.py

'''
import re
from metaparser import MetaParser
from metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional

# ====================================================
#  schema for show ip static-route
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
                                           Optional('rnh_active'): bool,
                                       },
                                   },
                                   Optional('next_hop_list'): {
                                       Any(): {     # index
                                           Optional('index'): int,
                                           Optional('active'): bool,
                                           Optional('next_hop'): str,
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
    '''
       show ip static-route
       show ip static-route vrf <vrf>
       show ip static-route vrf all
    '''
    def cli(self, vrf=""):
        if vrf:
            cmd = 'show ip static-route vrf {}'.format(vrf)
        else:
            cmd = 'show ip static-route'
            vrf = 'default'
        out = self.device.execute(cmd)

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
                if 'vrfs' not in result_dict:
                    result_dict['vrfs'] = {}

                if vrf not in result_dict['vrfs']:
                    result_dict['vrfs'][vrf] = {}

                if 'address_family' not in result_dict['vrfs'][vrf]:
                    result_dict['vrfs'][vrf]['address_family'] = {}

                if af and af not in result_dict['vrfs'][vrf]['address_family']:
                    result_dict['vrfs'][vrf]['address_family'][af] = {}
                continue

            #  2.2.2.2/32, configured nh: 10.2.3.2/32 Ethernet1/4
            #  2.2.2.2/32, configured nh: 20.2.3.2/32
            p2 = re.compile(r'^\s*(?P<route>[\d\/\.]+),'
                             ' +configured +nh: +(?P<nexthop>[\d\/\.]+)?( +(?P<interface>[a-zA-Z][\w\/\.]+))?$')
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
                    next_hop = m.groupdict()['nexthop']

                if 'routes' not in result_dict['vrfs'][vrf]['address_family'][af]:
                    result_dict['vrfs'][vrf]['address_family'][af]['routes'] = {}
                if route not in result_dict['vrfs'][vrf]['address_family'][af]['routes']:
                    result_dict['vrfs'][vrf]['address_family'][af]['routes'][route] = {}
                result_dict['vrfs'][vrf]['address_family'][af]['routes'][route]['route'] = route

                if 'next_hop' not in result_dict['vrfs'][vrf]['address_family'][af]['routes'][route]:
                    result_dict['vrfs'][vrf]['address_family'][af]['routes'][route]['next_hop'] = {}

                if not next_hop:
                    if 'outgoing_interface' not in result_dict['vrfs'][vrf]['address_family'][af] \
                            ['routes'][route]['next_hop']:
                        result_dict['vrfs'][vrf]['address_family'][af]['routes'][route] \
                            ['next_hop']['outgoing_interface'] = {}

                    if m.groupdict()['interface'] and interface not in \
                            result_dict['vrfs'][vrf]['address_family'][af]['routes'][route] \
                            ['next_hop']['outgoing_interface']:
                        result_dict['vrfs'][vrf]['address_family'][af]['routes'][route] \
                            ['next_hop']['outgoing_interface'][interface] = {}
                    result_dict['vrfs'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['outgoing_interface'][interface]['outgoing_interface'] = interface

                else:
                    if 'next_hop_list' not in result_dict['vrfs'][vrf]['address_family'][af]['routes'][route]['next_hop']:
                        result_dict['vrfs'][vrf]['address_family'][af]['routes'][route]['next_hop']['next_hop_list'] = {}

                    result_dict['vrfs'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                        ['next_hop_list'][index] = {}

                    result_dict['vrfs'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                        ['next_hop_list'][index]['index'] = index

                    result_dict['vrfs'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                        ['next_hop_list'][index]['next_hop'] = next_hop.strip()

                    if m.groupdict()['interface']:
                        result_dict['vrfs'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index]['outgoing_interface'] = interface

                continue

            # (not installed in urib)
            p3 = re.compile(r'^\s*\(not +installed +in +(?P<urib>[\w]+)\)$')
            m = p3.match(line)
            if m:
                active = False
                if not next_hop:
                    result_dict['vrfs'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['outgoing_interface'][interface]['active'] = active
                else:
                    result_dict['vrfs'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['next_hop_list'][index]['active'] = active
                continue

            # (installed in urib)
            p4 = re.compile(r'^\s*\(installed +in +(?P<urib>[\w]+)\)$')
            m = p4.match(line)
            if m:
                active = True
                if not next_hop:
                    result_dict['vrfs'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['outgoing_interface'][interface]['active'] = active
                else:
                    result_dict['vrfs'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['next_hop_list'][index]['active'] = active
                continue

            #rnh(installed in urib)
            p5 = re.compile(r'^\s*rnh\(installed +in +(?P<urib>[\w]+)\)$')
            m = p5.match(line)
            if m:
                active = True
                if not next_hop:
                    result_dict['vrfs'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['outgoing_interface'][interface]['rnh_active'] = active
                else:
                    result_dict['vrfs'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['next_hop_list'][index]['rnh_active'] = active
                continue

        return result_dict


# ====================================================
#  schema for show ipv6 static detail
# ====================================================
class ShowIpv6StaticDetailSchema(MetaParser):
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
                                           Optional('preference'): int,
                                           Optional('tag'): int,
                                       },
                                   },
                                   Optional('next_hop_list'): {
                                       Any(): {     # index
                                           Optional('index'): int,
                                           Optional('next_hop'): str,
                                           Optional('outgoing_interface'): str,
                                           Optional('resolved_outgoing_interface'): str,
                                           Optional('resolved_paths_number'): int,
                                           Optional('rejected_by'): str,
                                           Optional('max_depth'): int,
                                           Optional('preference'): int,
                                           Optional('tag'): int,
                                           Optional('track'): int,
                                           Optional('track_shutdown'): bool,
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
#  parser for show ipv6 static detail
# ====================================================
class ShowIpv6StaticDetail(ShowIpv6StaticDetailSchema):
    '''
       show ipv6 static detail
       show ipv6 static vrf <vrf> detail
    '''
    def cli(self, vrf=""):
        if vrf:
            cmd = 'show ipv6 static vrf {} detail'.format(vrf)
        else:
            cmd = 'show ipv6 static detail'
        out = self.device.execute(cmd)

        af = 'ipv6'
        resolved_interface = False
        vrf = route = interface = next_hop = ""

        result_dict = {}
        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            # IPv6 Static routes Table - default
            p1 = re.compile(r'^\s*IPv6 +Static +routes +Table -+ (?P<vrf>[\w]+)$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                if vrf:
                    if 'vrfs' not in result_dict:
                        result_dict['vrfs'] = {}

                    if vrf not in result_dict['vrfs']:
                        result_dict['vrfs'][vrf] = {}

                    if 'address_family' not in result_dict['vrfs'][vrf]:
                        result_dict['vrfs'][vrf]['address_family'] = {}

                    if af and af not in result_dict['vrfs'][vrf]['address_family']:
                        result_dict['vrfs'][vrf]['address_family'][af] = {}
                continue

            # 2001:2:2:2::2/128 via 2001:10:1:2::2, distance 3
            # *   2001:2:2:2::2/128 via 2001:20:1:2::2, GigabitEthernet0/1, distance 1
            # 2001:2:2:2::2/128 via 2001:10:1:2::2, GigabitEthernet0/0, distance 11, tag 100
            # *   2001:3:3:3::3/128 via GigabitEthernet0/3, distance 1
            p2 = re.compile(r'^\s*([*]  +)?(?P<route>[\w\/\:]+)?'
                            ' +via +((?P<nexthop>[\d\:]+), )?'
                            '((?P<interface>[a-zA-Z][\w\.\/]+), )?'
                            '(distance (?P<distance>[\d]+))?'
                            '(, +tag +(?P<tag>[\d]+))?$')
            m = p2.match(line)
            if m:
                next_hop = ""
                if m.groupdict()['route']:
                    if route == m.groupdict()['route']:
                        index += 1
                    else:
                        route = m.groupdict()['route']
                        index = 1

                if_preference = m.groupdict()['distance']
                if m.groupdict()['nexthop']:
                    next_hop = m.groupdict()['nexthop']
                if m.groupdict()['interface']:
                    interface = m.groupdict()['interface']
                if m.groupdict()['distance']:
                    if_preference = m.groupdict()['distance']
                if m.groupdict()['tag']:
                    tag = m.groupdict()['tag']

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

                    if m.groupdict()['interface'] and interface not in result_dict['vrfs']\
                            [vrf]['address_family'][af]['routes'][route]\
                            ['next_hop']['outgoing_interface']:
                        result_dict['vrfs'][vrf]['address_family'][af]['routes'][route]\
                            ['next_hop']['outgoing_interface'][interface] = {}
                    result_dict['vrfs'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['outgoing_interface'][interface]['outgoing_interface'] = interface

                    result_dict['vrfs'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['outgoing_interface'][interface]['preference'] = int(if_preference)

                    if m.groupdict()['tag']:
                        result_dict['vrfs'][vrf]['address_family'][af]['routes'][route] \
                            ['next_hop']['outgoing_interface'][interface]['tag'] = int(tag)

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
                        ['next_hop_list'][index]['next_hop'] = next_hop.strip()

                    if interface:
                        result_dict['vrfs'][vrf]['address_family'][af]['routes'][route]['next_hop']\
                            ['next_hop_list'][index]['outgoing_interface'] = interface
                    result_dict['vrfs'][vrf]['address_family'][af]['routes'][route]['next_hop']\
                        ['next_hop_list'][index]['preference'] = if_preference_int
                    if m.groupdict()['tag']:
                        result_dict['vrfs'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index]['tag'] = int(tag)

                continue

            # Resolves to 1 paths (max depth 1)
            p3 = re.compile(r'^\s*Resolves +to +(?P<no_paths>[\d]+)? +paths'
                            ' +\(max +depth +(?P<max_depth>[\d]+)\)$')
            m = p3.match(line)
            if m:
                resolved_interface = True
                max_depth = m.groupdict()['max_depth']
                number_of_paths = m.groupdict()['no_paths']
                result_dict['vrfs'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                    ['next_hop_list'][index]['resolved_paths_number'] = int(number_of_paths)

                result_dict['vrfs'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                    ['next_hop_list'][index]['max_depth'] = int(max_depth)
                continue

            # via GigabitEthernet0/0
            p4 = re.compile(r'^\s*via +(?P<resolved_interface>[\w\/\.]+)$')
            m = p4.match(line)
            if m:
                if resolved_interface:
                    resolved_outgoing_interface = m.groupdict()['resolved_interface']
                    result_dict['vrfs'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                        ['next_hop_list'][index]['resolved_outgoing_interface'] = resolved_outgoing_interface
                    resolved_interface = False
                continue

            # Rejected by routing table
            p6 = re.compile(r'^\s*Rejected +by +(?P<rejected_by>[\w\s]+)$')
            m = p6.match(line)
            if m:
                rejected_by = m.groupdict()['rejected_by']
                result_dict['vrfs'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                    ['next_hop_list'][index]['rejected_by'] = rejected_by
                continue

            # Tracked object 1 is Up
            p7 = re.compile(r'^\s*Tracked +object +(?P<tracked_no>\d+) +is +(?P<interface_status>[\w]+)$')
            m = p7.match(line)
            if m:
                track = m.groupdict()['tracked_no']
                track_shutdown = False if m.groupdict()['interface_status'].lower() == 'up' else True
                result_dict['vrfs'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                    ['next_hop_list'][index]['track'] = int(track)
                result_dict['vrfs'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                    ['next_hop_list'][index]['track_shutdown'] = track_shutdown
                continue

        return result_dict