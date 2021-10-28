"""
show_static_route.py

"""
import re
from genie.metaparser import MetaParser
from genie.libs.parser.utils.common import Common
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
                                           Optional('path_event'): str,
                                           Optional('tag'): int,
                                           Optional('path_version'): int,
                                           Optional('path_status'): str,
                                           Optional('metrics'): int,
                                           Optional('track'): int,
                                           Optional('explicit_path'): str,
                                           Optional('preference'): int,
                                           Optional('local_label'): str,
                                       },
                                   },
                                   Optional('next_hop_list'): {
                                       Any(): {     # index
                                           Optional('index'): int,
                                           Optional('active'): bool,
                                           Optional('next_hop'): str,
                                           Optional('outgoing_interface'): str,
                                           Optional('path_event'): str,
                                           Optional('tag'): int,
                                           Optional('path_version'): int,
                                           Optional('path_status'): str,
                                           Optional('metrics'): int,
                                           Optional('track'): int,
                                           Optional('explicit_path'): str,
                                           Optional('preference'): int,
                                           Optional('local_label'): str,
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
    cli_command = ['show static vrf {vrf} {af} topology detail','show static vrf {vrf} topology detail',
                   'show static {af} topology detail','show static topology detail']
    exclude = ['install_date', 'configure_date', 'path_version']

    def cli(self, vrf="", af="", output=None):
        if output is None:
            if vrf:
                if af:
                    cmd = self.cli_command[0].format(vrf=vrf, af=af)
                else:
                    cmd = self.cli_command[1].format(vrf=vrf)
            else:
                if af:
                    cmd = self.cli_command[2].format(af=af)
                else:
                    cmd = self.cli_command[3]

            out = self.device.execute(cmd)
        else:
            out = output

        if not vrf:
            vrf = 'default'

        route = interface = next_hop = ""

        result_dict = {}

        # regex

        # No routes in this topology
        p = re.compile(r'^\s*No routes in this topology$')

        # VRF: default Table Id: 0xe0000000 AFI: IPv4 SAFI: Unicast
        p1 = re.compile(r'^\s*VRF: +(?P<vrf>[\w]+) +Table +Id: +(?P<table_id>[\w]+) +AFI: +(?P<af>[\w]+)'
                        ' +SAFI: +(?P<safi>[\w]+)$')

        # Prefix/Len          Interface                Nexthop             Object              Explicit-path       Metrics
        # 2001:1:1:1::1/128   GigabitEthernet0_0_0_3   2001:10:1:2::1      None                None                [0/0/1/0/1]
        # 2001:1:1:a::1/128   GigabitEthernet0_0_0_3   2001:10:1:2::1      None                None                [0/0/1/0/1]
        #             GigabitEthernet0_0_0_0   None                None                None                [0/4096/1/0/1]
        # Prefix/Len          Interface                Nexthop             Object         Explicit-path       Metrics          Local-Label
        # 172.16.0.89/32      TenGigE0_0_1_2           None                None          None                [0/4096/1/0/1]    No label    Path is configured at Sep 11 08:29:25.605
        # 10.00.00.0/00       Bundle-Ether2.25         10.01.02.03         None                None                [0/0/1/0/1]
        p2 = re.compile(r'^(?P<route>[a-fA-F\d\/\.\:]+)? '
                        r'*(?P<interface>[a-zA-Z][\w\/\.-]+) '
                        r'+(?P<nexthop>[\w\/\.\:]+) +(?P<object>[\w]+) '
                        r'+(?P<explicit_path>[\w]+) +(?P<metrics>[\w\/\[\]]+)'
                        r'(\s+(?P<local_label>[\w\s]+?))?'
                        r'(\s+(?P<path_event>(Path|Last).*))?$')

        # Path is installed into RIB at Dec  7 21:52:00.853
        p3 = re.compile(r'^\s*(?P<path_event>Path +is +installed +into +RIB +at +(?P<date>[\S\s]+))$')

        # Path is configured at Dec  7 21:47:43.624
        p3_1 = re.compile(r'^\s*(?P<path_event>Path +is +configured +at +(?P<date>[\S\s]+))$')

        # Path is removed from RIB at Dec  7 21:47:43.624
        p3_2 = re.compile(r'^\s*(?P<path_event>Path +is +removed +from +RIB +at +(?P<date>[\S\s]+))$')

        # Last RIB event is at Dec  7 21:47:43.624
        p3_3 = re.compile(r'^\s*(?P<path_event>Last +RIB +event +is +at +(?P<date>[\S\s]+))$')

        # Path version: 1, Path status: 0x21
        p4 = re.compile(r'^\s*Path +version: +(?P<path_version>[\d]+), +Path +status: +(?P<path_status>[\w]+)$')

        # Path has best tag: 0
        p5 = re.compile(r'^\s*Path +has +best +tag: +(?P<tag>[\d]+)$')

        for line in out.splitlines():
            if line:
                line = line.strip()
            else:
                continue

            m = p.match(line)
            if m:
                continue

            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                af = m.groupdict()['af'].lower()
                table_id = m.groupdict()['table_id']
                safi = m.groupdict()['safi'].lower()

                af_dict = result_dict.setdefault('vrf', {}).setdefault(vrf, {}).\
                            setdefault('address_family', {}).setdefault(af, {})

                af_dict['safi'] = safi.lower()
                af_dict['table_id'] = table_id
                continue

            m = p2.match(line)

            if m:
                next_hop = ""

                if m.groupdict()['route']:
                    route = m.groupdict()['route'].strip()
                    index = 1
                else:
                    index += 1

                if m.groupdict()['interface'] and 'none' not in m.groupdict()['interface'].lower():
                    interface = Common.convert_intf_name(m.groupdict()['interface'].replace('_','/'))
                if m.groupdict()['nexthop'] and 'none' not in m.groupdict()['nexthop'].lower():
                    next_hop = m.groupdict()['nexthop']

                if m.groupdict()['metrics']:
                    metrics_value = m.groupdict()['metrics'].strip('[').strip(']').split('/')
                    metrics = int(metrics_value[4])
                    preference = int(metrics_value[2])

                if m.groupdict()['object'] and 'none' not in m.groupdict()['object'].lower() :
                    object = m.groupdict()['object']

                if m.groupdict()['explicit_path'] and 'none' not in m.groupdict()['explicit_path'].lower():
                    explicit_path = m.groupdict()['explicit_path']
                
                local_label = m.groupdict()['local_label']
                path_event = m.groupdict()['path_event']

                route_dict = af_dict.setdefault('routes', {}).setdefault(route, {})
                route_dict['route'] = route
                hop_dict = route_dict.setdefault('next_hop', {})

                if not next_hop:

                    intf_dict = hop_dict.setdefault('outgoing_interface', {}).\
                                         setdefault(interface, {})
                    intf_dict['outgoing_interface'] = interface

                    intf_dict['metrics'] = metrics
                    intf_dict['preference'] = preference

                    if m.groupdict()['explicit_path']and 'none' not in m.groupdict()['explicit_path'].lower():
                        intf_dict['explicit_path'] = explicit_path
                    if m.groupdict()['object'] and 'none' not in m.groupdict()['object'].lower():
                        intf_dict['track'] = int(object)
                    if local_label:
                        intf_dict['local_label'] = local_label
                    if path_event:
                        intf_dict['path_event'] = path_event

                else:
                    idx_dict = hop_dict.setdefault('next_hop_list', {}).setdefault(index, {})

                    idx_dict['index'] = index
                    idx_dict['next_hop'] = next_hop.strip()

                    if m.groupdict()['interface'] and 'none' not in m.groupdict()['interface'].lower():
                        idx_dict['outgoing_interface'] = interface

                    idx_dict['metrics'] = metrics
                    idx_dict['preference'] = preference

                    if m.groupdict()['explicit_path'] and 'none' not in m.groupdict()['explicit_path'].lower():
                        idx_dict['explicit_path'] = explicit_path
                    if m.groupdict()['object'] and 'none' not in m.groupdict()['object'].lower():
                        idx_dict['track'] = int(object)
                    if local_label:
                        idx_dict['local_label'] = local_label
                    if path_event:
                        idx_dict['path_event'] = path_event
                continue

            m = p3.match(line)
            if m:
                active = True
                path_event = m.groupdict()['path_event']
                if not next_hop:
                    intf_dict['active'] = active
                    intf_dict['path_event'] = path_event
                else:
                    idx_dict['active'] = active
                    idx_dict['path_event'] = path_event
                continue

            m = p3_1.match(line)
            if m:
                active = False
                path_event = m.groupdict()['path_event']
                if not next_hop:
                    intf_dict['active'] = active
                    intf_dict['path_event'] = path_event
                else:
                    idx_dict['active'] = active
                    idx_dict['path_event'] = path_event
                continue

            m = p3_2.match(line)
            if m:
                active = False
                path_event = m.groupdict()['path_event']
                if not next_hop:
                    intf_dict['active'] = active
                    intf_dict['path_event'] = path_event
                else:
                    idx_dict['active'] = active
                    idx_dict['path_event'] = path_event
                continue

            m = p3_3.match(line)
            if m:
                path_event = m.groupdict()['path_event']
                if not next_hop:
                    intf_dict['path_event'] = path_event
                else:
                    idx_dict['path_event'] = path_event
                continue

            m = p4.match(line)
            if m:
                path_version = int(m.groupdict()['path_version'])
                path_status = m.groupdict()['path_status']
                if not next_hop:
                    intf_dict['path_version'] = path_version
                    intf_dict['path_status'] = path_status
                else:
                    idx_dict['path_version'] = path_version
                    idx_dict['path_status'] = path_status
                continue

            m = p5.match(line)
            if m:
                tag = m.groupdict()['tag']
                if not next_hop:
                    intf_dict['tag'] = int(tag)
                else:
                    idx_dict['tag'] = int(tag)
                continue

        return result_dict
