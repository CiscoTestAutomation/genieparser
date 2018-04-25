"""
show_static_route.py

"""
import re
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                         Any, \
                                         Optional

# ====================================================
#  schema for show static ipv4 topology detail
# ====================================================
class ShowStaticTopologyDetailSchema(MetaParser):
    """Schema for:
        show static topology detail
        show static vrf all topology detail
        show static vrf <vrf> topology detail
        show static vrf <vrf> ipv4 topology detail
        show static vrf <vrf> ipv6 topology detail
        show static ipv4 topology detail
        show static ipv6 topology detail"""
    schema = {
        'vrf': {
            Any(): {
                Optional('address_family'): {
                   Any(): {
                       Optional('table_id'): str,
                       Optional('safi'): str,
                       Optional('routes'): {
                           Any(): {
                               Optional('route'): str,
                               Optional('next_hop'): {
                                   Optional('outgoing_interface'): {
                                       Any(): {    # interface  if there is no next_hop
                                           Optional('outgoing_interface'): str,
                                           Optional('active'): bool,
                                           Optional('install_date'): str,
                                           Optional('configure_date'): str,
                                           Optional('tag'): int,
                                           Optional('path_version'): int,
                                           Optional('path_status'): str,
                                           Optional('metrics'): int,
                                           Optional('track'): int,
                                           Optional('explicit_path'): str,
                                           Optional('preference'): int,
                                       },
                                   },
                                   Optional('next_hop_list'): {
                                       Any(): {     # index
                                           Optional('index'): int,
                                           Optional('active'): bool,
                                           Optional('next_hop'): str,
                                           Optional('outgoing_interface'): str,
                                           Optional('install_date'): str,
                                           Optional('configure_date'): str,
                                           Optional('tag'): int,
                                           Optional('path_version'): int,
                                           Optional('path_status'): str,
                                           Optional('metrics'): int,
                                           Optional('track'): int,
                                           Optional('explicit_path'): str,
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
#  parser for show static topology detail
# ====================================================
class ShowStaticTopologyDetail(ShowStaticTopologyDetailSchema):
    """Parser for:
       show static topology detail
       show static vrf all topology detail
       show static vrf <vrf> topology detail
       show static vrf <vrf> ipv4 topology detail
       show static ipv4 topology detail
       show static ipv6 topology detail
    """
    def cli(self, vrf="", af=""):
        if vrf:
            if af:
                cmd = 'show static vrf {} {} topology detail'.format(vrf, af)
            else:
                cmd = 'show static vrf {} topology detail'.format(vrf)
        else:
            if af:
                cmd = 'show static {} topology detail'.format(af)
            else:
                cmd = 'show static topology detail'
            vrf = 'default'

        out = self.device.execute(cmd)

        route = interface = next_hop = ""

        result_dict = {}
        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            # No routes in this topology
            p = re.compile(r'^\s*No routes in this topology$')
            m = p.match(line)
            if m:
                continue

            # VRF: default Table Id: 0xe0000000 AFI: IPv4 SAFI: Unicast
            p1 = re.compile(r'^\s*VRF: +(?P<vrf>[\w]+) +Table +Id: +(?P<table_id>[\w]+) +AFI: +(?P<af>[\w]+)'
                            ' +SAFI: +(?P<safi>[\w]+)$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                af = m.groupdict()['af'].lower()
                table_id = m.groupdict()['table_id']
                safi = m.groupdict()['safi'].lower()

                if 'vrf' not in result_dict:
                    result_dict['vrf'] = {}

                if vrf not in result_dict['vrf']:
                    result_dict['vrf'][vrf] = {}

                if 'address_family' not in result_dict['vrf'][vrf]:
                    result_dict['vrf'][vrf]['address_family'] = {}

                if af and af not in result_dict['vrf'][vrf]['address_family']:
                    result_dict['vrf'][vrf]['address_family'][af] = {}

                result_dict['vrf'][vrf]['address_family'][af]['safi'] = safi.lower()
                result_dict['vrf'][vrf]['address_family'][af]['table_id'] = table_id
                continue

            # Prefix/Len          Interface                Nexthop             Object              Explicit-path       Metrics
            # 2001:1:1:1::1/128   GigabitEthernet0_0_0_3   2001:10:1:2::1      None                None                [0/0/1/0/1]
            #             GigabitEthernet0_0_0_0   None                None                None                [0/4096/1/0/1]
            p2 = re.compile(r'^\s*(?P<route>[\d\s\/\.\:]+)?'
                             '(?P<interface>[a-zA-Z][\w\/\.]+)'
                             ' +(?P<nexthop>[\w\/\.\:]+)'
                             ' +(?P<object>[\w]+)'
                             ' +(?P<explicit_path>[\w]+)'
                             ' +(?P<metrics>[\w\/\[\]]+)$')
            m = p2.match(line)
            if m:
                next_hop = ""

                if m.groupdict()['route']:
                    route = m.groupdict()['route'].strip()
                    index = 1
                else:
                    index += 1

                if m.groupdict()['interface'] and 'none' not in m.groupdict()['interface'].lower() :
                    interface = m.groupdict()['interface'].replace('_','/')
                if m.groupdict()['nexthop'] and 'none' not in m.groupdict()['nexthop'].lower():
                    next_hop = m.groupdict()['nexthop']

                if m.groupdict()['metrics']:
                    metrics_value = m.groupdict()['metrics'].strip('[').strip(']').split('/')
                    metrics = int(metrics_value[4])
                    prefernce = int(metrics_value[2])

                if m.groupdict()['object'] and 'none' not in m.groupdict()['object'].lower() :
                    object = m.groupdict()['object']

                if m.groupdict()['explicit_path'] and 'none' not in m.groupdict()['explicit_path'].lower() :
                    explicit_path = m.groupdict()['explicit_path']

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

                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['outgoing_interface'][interface]['metrics'] = metrics
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['outgoing_interface'][interface]['preference'] = prefernce

                    if m.groupdict()['explicit_path']and 'none' not in m.groupdict()['explicit_path'].lower():
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['next_hop']['outgoing_interface'][interface]['explicit_path'] = explicit_path
                    if m.groupdict()['object'] and 'none' not in m.groupdict()['object'].lower():
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                            ['next_hop']['outgoing_interface'][interface]['track'] = int(object)


                else:
                    if 'next_hop_list' not in result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop']:
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop']['next_hop_list'] = {}

                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                        ['next_hop_list'][index] = {}

                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                        ['next_hop_list'][index]['index'] = index

                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                        ['next_hop_list'][index]['next_hop'] = next_hop.strip()

                    if m.groupdict()['interface'] and 'none' not in m.groupdict()['interface'].lower():
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index]['outgoing_interface'] = interface

                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                        ['next_hop_list'][index]['metrics'] = metrics
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                        ['next_hop_list'][index]['preference'] = prefernce

                    if m.groupdict()['explicit_path'] and 'none' not in m.groupdict()['explicit_path'].lower():
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index]['explicit_path'] = explicit_path
                    if m.groupdict()['object'] and 'none' not in m.groupdict()['object'].lower():
                        result_dict['vrf'][vrf]['address_family'][af]['routes'][route]['next_hop'] \
                            ['next_hop_list'][index]['track'] = int(object)
                continue

            # Path is installed into RIB at Dec  7 21:52:00.853
            p3 = re.compile(r'^\s*Path +is +installed +into +RIB +at +(?P<install_date>[\w\s\:\.]+)$')
            m = p3.match(line)
            if m:
                active = True
                install_date = m.groupdict()['install_date']
                if not next_hop:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['outgoing_interface'][interface]['active'] = active
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['outgoing_interface'][interface]['install_date'] = install_date
                else:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['next_hop_list'][index]['active'] = active
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['next_hop_list'][index]['install_date'] = install_date
                continue

            # Path is configured at Dec  7 21:47:43.624
            p3_1 = re.compile(r'^\s*Path +is +configured +at +(?P<configure_date>[\w\s\:\.]+)$')
            m = p3_1.match(line)
            if m:
                active = False
                configure_date = m.groupdict()['configure_date']
                if not next_hop:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['outgoing_interface'][interface]['active'] = active
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['outgoing_interface'][interface]['configure_date'] = configure_date
                else:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['next_hop_list'][index]['active'] = active
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['next_hop_list'][index]['configure_date'] = configure_date
                continue

            # Path version: 1, Path status: 0x21
            p4 = re.compile(r'^\s*Path +version: +(?P<path_version>[\d]+), +Path +status: +(?P<path_status>[\w]+)$')
            m = p4.match(line)
            if m:
                path_version = int(m.groupdict()['path_version'])
                path_status = m.groupdict()['path_status']
                if not next_hop:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['outgoing_interface'][interface]['path_version'] = path_version
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['outgoing_interface'][interface]['path_status'] = path_status
                else:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['next_hop_list'][index]['path_version'] = path_version
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['next_hop_list'][index]['path_status'] = path_status
                continue

            # Path has best tag: 0
            p5 = re.compile(r'^\s*Path +has +best +tag: +(?P<tag>[\d]+)$')
            m = p5.match(line)
            if m:
                tag = m.groupdict()['tag']
                if not next_hop:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['outgoing_interface'][interface]['tag'] = int(tag)
                else:
                    result_dict['vrf'][vrf]['address_family'][af]['routes'][route] \
                        ['next_hop']['next_hop_list'][index]['tag'] = int(tag)
                continue

        return result_dict
