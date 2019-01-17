'''
show_static_route.py

'''
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional


# ====================================================
#  schema for show ip static route
# ====================================================
class ShowIpStaticRouteSchema(MetaParser):
    """Schema for show ip static route"""
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
                                        Any(): {  # interface  if there is no next_hop
                                            Optional('outgoing_interface'): str,
                                            Optional('active'): bool,
                                            Optional('preference'): int,
                                        },
                                    },
                                    Optional('next_hop_list'): {
                                        Any(): {  # index
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
    """Parser for :
       show ip static route
       show ip static route vrf <vrf>
    """
    cli_command = ['show ip static route vrf {vrf}','show ip static route']

    def cli(self, vrf="",output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[0].format(vrf=vrf)
            else:
                cmd = self.cli_command[1]
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
                    route = m.groupdict()['route']
                    index = 1
                else:
                    index += 1
                if_preference = m.groupdict()['if_preference']
                interface = m.groupdict()['interface']
                if m.groupdict()['nexthop']:
                    next_hop = m.groupdict()['nexthop']

                code_in_bracket = m.groupdict()['code_in_bracket']

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

                    if 'next_hop' not in result_dict['vrf'][vrf]['address_family'][af]['routes'][route]:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] = {}

                    if not next_hop:
                        if 'outgoing_interface' not in result_dict['vrf'][vrf]['address_family'][af] \
                                ['routes'][route]['next_hop']:
                            result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                                ['next_hop']['outgoing_interface'] = {}

                        if interface not in result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                                ['next_hop']['outgoing_interface']:
                            result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                                ['next_hop']['outgoing_interface'][interface] = {}
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['next_hop']['outgoing_interface'][interface]['outgoing_interface'] = interface

                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['next_hop']['outgoing_interface'][interface][
                            'active'] = True if code_in_bracket == 'A' else False

                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['next_hop']['outgoing_interface'][interface]['preference'] = int(if_preference)

                    else:
                        if 'next_hop_list' not in result_dict['vrf'][vrf]['address_family'][af]['routes'][route][
                            'next_hop']:
                            result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'][
                                'next_hop_list'] = {}

                        if int(if_preference):
                            if_preference_int = int(if_preference)
                            result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                                ['next_hop_list'][index] = {}

                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index]['index'] = index

                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index]['active'] = True if code_in_bracket == 'A' else False

                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index]['next_hop'] = next_hop.strip()

                        if interface:
                            result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                                ['next_hop_list'][index]['outgoing_interface'] = interface
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index]['preference'] = if_preference_int
                continue

        return result_dict


# ====================================================
#  schema for show ipv6 static detail
# ====================================================
class ShowIpv6StaticDetailSchema(MetaParser):
    """Schema for show ipv6 static detail"""
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
                                        Any(): {  # interface  if there is no next_hop
                                            Optional('outgoing_interface'): str,
                                            Optional('active'): bool,
                                            Optional('preference'): int,
                                            Optional('tag'): int,
                                        },
                                    },
                                    Optional('next_hop_list'): {
                                        Any(): {  # index
                                            Optional('index'): int,
                                            Optional('next_hop'): str,
                                            Optional('active'): bool,
                                            Optional('outgoing_interface'): str,
                                            Optional('resolved_outgoing_interface'): str,
                                            Optional('resolved_paths_number'): int,
                                            Optional('rejected_by'): str,
                                            Optional('max_depth'): int,
                                            Optional('preference'): int,
                                            Optional('tag'): int,
                                            Optional('track'): int,
                                            Optional('track_state'): str,
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
    """Parser for:
       show ipv6 static detail
       show ipv6 static vrf <vrf> detail
    """

    cli_command = ['show ipv6 static vrf {vrf} detail', 'show ipv6 static detail']

    def cli(self, vrf="", output=None):
        if output is None:
            if vrf:
                cmd = self.cli_command[0].format(vrf=vrf)
            else:
                cmd = self.cli_command[1]
            out = self.device.execute(cmd)
        else:
            out = output

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
                    if 'vrf' not in result_dict:
                        result_dict['vrf'] = {}

                    if vrf not in result_dict['vrf']:
                        result_dict['vrf'][vrf] = {}

                    if 'address_family' not in result_dict['vrf'][vrf]:
                        result_dict['vrf'][vrf]['address_family'] = {}

                    if af and af not in result_dict['vrf'][vrf]['address_family']:
                        result_dict['vrf'][vrf]['address_family'][af] = {}
                continue

            # 2001:2:2:2::2/128 via 2001:10:1:2::2, distance 3
            # *   2001:2:2:2::2/128 via 2001:20:1:2::2, GigabitEthernet0/1, distance 1
            # 2001:2:2:2::2/128 via 2001:10:1:2::2, GigabitEthernet0/0, distance 11, tag 100
            # *   2001:3:3:3::3/128 via GigabitEthernet0/3, distance 1
            p2 = re.compile(r'^\s*((?P<star>[*]+)  +)?(?P<route>[\w\/\:]+)?'
                            ' +via +((?P<nexthop>[0-9a-fA-F\:]+), )?'
                            '((?P<interface>[a-zA-Z][\w\.\/]+), )?'
                            '(distance (?P<distance>[\d]+))?'
                            '(, +tag +(?P<tag>[\d]+))?$')
            m = p2.match(line)
            if m:
                next_hop = ""
                if m.groupdict()['star']:
                    active = True
                else:
                    active = False
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

                    if m.groupdict()['interface'] and interface not in result_dict['vrf'] \
                            [vrf]['address_family'][af]['routes'][route] \
                            ['next_hop']['outgoing_interface']:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['next_hop']['outgoing_interface'][interface] = {}
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['outgoing_interface'][interface]['outgoing_interface'] = interface

                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['outgoing_interface'][interface]['preference'] = int(if_preference)

                    if m.groupdict()['tag']:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['next_hop']['outgoing_interface'][interface]['tag'] = int(tag)

                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['outgoing_interface'][interface]['active'] = active

                else:
                    if 'next_hop_list' not in result_dict['vrf'][vrf]['address_family'][af]['routes'][route][
                        'next_hop']:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'][
                            'next_hop_list'] = {}

                    if int(if_preference):
                        if_preference_int = int(if_preference)
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index] = {}

                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                        ['next_hop_list'][index]['index'] = index

                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                        ['next_hop_list'][index]['next_hop'] = next_hop.strip()

                    if interface:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index]['outgoing_interface'] = interface
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                        ['next_hop_list'][index]['preference'] = if_preference_int
                    if m.groupdict()['tag']:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index]['tag'] = int(tag)

                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['next_hop_list'][index]['active'] = active

                continue

            # Resolves to 1 paths (max depth 1)
            p3 = re.compile(r'^\s*Resolves +to +(?P<no_paths>[\d]+)? +paths'
                            ' +\(max +depth +(?P<max_depth>[\d]+)\)$')
            m = p3.match(line)
            if m:
                resolved_interface = True
                max_depth = m.groupdict()['max_depth']
                number_of_paths = m.groupdict()['no_paths']
                result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                    ['next_hop_list'][index]['resolved_paths_number'] = int(number_of_paths)

                result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                    ['next_hop_list'][index]['max_depth'] = int(max_depth)
                continue

            # via GigabitEthernet0/0
            p4 = re.compile(r'^\s*via +(?P<resolved_interface>[\w\/\.]+)$')
            m = p4.match(line)
            if m:
                if resolved_interface:
                    resolved_outgoing_interface = m.groupdict()['resolved_interface']
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                        ['next_hop_list'][index]['resolved_outgoing_interface'] = resolved_outgoing_interface
                    resolved_interface = False
                continue

            # Rejected by routing table
            p6 = re.compile(r'^\s*Rejected +by +(?P<rejected_by>[\w\s]+)$')
            m = p6.match(line)
            if m:
                rejected_by = m.groupdict()['rejected_by']
                result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                    ['next_hop_list'][index]['rejected_by'] = rejected_by
                continue

            # Tracked object 1 is Up
            p7 = re.compile(r'^\s*Tracked +object +(?P<tracked_no>\d+) +is +(?P<interface_status>[\w]+)$')
            m = p7.match(line)
            if m:
                track = m.groupdict()['tracked_no']
                track_state = m.groupdict()['interface_status'].lower()
                result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                    ['next_hop_list'][index]['track'] = int(track)
                result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                    ['next_hop_list'][index]['track_state'] = track_state
                continue

        return result_dict
