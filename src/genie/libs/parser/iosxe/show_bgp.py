''' show_bgp.py
    IOSXE parsers for the following show commands:

    * show bgp all detail
    * show bgp all neighbor
    * show bgp all summary
    * show bgp all cluster-ids
    * show bgp all
    * show ip bgp template peer-session <WORD>
    * show ip bgp template peer-policy <WORD>
    * show ip bgp all dampening parameters
    * show ip bgp <af_name> [ vrf <vrf_id> ] <ipv4prefix>
    * show bgp vrf [vrf_id] <af_name> <ipv6prefix>
    * show bgp <af_name> <ipv6prefix>
    * show bgp all neighbors <neighbor> policy
    * show ip route vrf <WORD> bgp
    * show vrf detail

    * show bgp all neighbor x.x.x.x advertised-routes
    * show bgp all neighbor x.x.x.x routes
    * show bgp all neighbor x.x.x.x received
    * show bgp all neighbor x.x.x.x received-routes

'''

import re   
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional


# ================================
# Parser for 'show bgp all detail'
# ================================

class ShowBgpAllDetailSchema(MetaParser):

    """Schema for show bgp all detail"""

    schema = {
    'instance':
        {'default':
            {'vrf':
                {Any():
                    {'address_family':
                        {Any():
                            {Optional('route_distinguisher'): str,
                             Optional('default_vrf'): str,
                             Optional('prefixes'):
                                {Any():
                                    {Optional('paths'): str,
                                     Optional('available_path'): str,
                                     Optional('best_path'): str,
                                     Optional('table_version'): str,
                                     Optional('index'):
                                        {Any():
                                            {Optional('next_hop'): str,
                                             Optional('next_hop_igp_metric'): str,
                                             Optional('gateway'): str,
                                             Optional('route_info'): str,
                                             Optional('next_hop_via'): str,
                                             Optional('update_group'): int,
                                             Optional('status_codes'): str,
                                             Optional('origin_codes'): str,
                                             Optional('metric'): int,
                                             Optional('inaccessible'): bool,
                                             Optional('localpref'): int,
                                             Optional('weight'): str,
                                             Optional('originator'): str,
                                             Optional('refresh_epoch'): int,
                                             Optional('recipient_pathid'): str,
                                             Optional('transfer_pathid'): str,
                                             Optional('evpn'):
                                                {Optional('ext_community'): str,
                                                 Optional('encap'): str,
                                                 Optional('evpn_esi'): str,
                                                 Optional('local_vtep'): str,
                                                 Optional('gateway_address'): str,
                                                 Optional('label'): int,
                                                 Optional('router_mac'): str,
                                                },
                                             Optional('local_vxlan_vtep'):
                                                {Optional('encap'): str,
                                                 Optional('local_router_mac'): str,
                                                 Optional('vtep_ip'): str,
                                                 Optional('vrf'): str,
                                                 Optional('vni'): str,
                                                 Optional('bdi'): str,
                                                }
                                            }
                                        },
                                    }
                                },
                            }
                        },
                    }
                },
            }
        }
    }


class ShowBgpAllDetail(ShowBgpAllDetailSchema):

    """Parser for show bgp all detail"""

    def cli(self):

        # show bgp all detail
        cmd  = 'show bgp all detail'
        out = self.device.execute(cmd)

        # Init dictionary
        bgp_dict = {}
        subdict = ''
        next_line_update_group = False
        route_distinguisher = ''
        new_address_family = ''
        refresh_epoch_flag = False
        route_info = ''

        for line in out.splitlines():
            line = line.rstrip()

            # For address family: IPv4 Unicast
            # For address family: L2VPN E-VPN
            p1 = re.compile(r'^\s*For +address +family:'
                             ' +(?P<address_family>[a-zA-Z0-9\-\s]+)$')
            m = p1.match(line)
            if m:
                index = 0
                address_family = str(m.groupdict()['address_family']).lower()
                original_address_family = address_family
                if 'instance' not in bgp_dict:
                    bgp_dict['instance'] = {}
                if 'default' not in bgp_dict['instance']:
                    bgp_dict['instance']['default'] = {}
                if 'vrf' not in bgp_dict['instance']['default']:
                    bgp_dict['instance']['default']['vrf'] = {}
                    continue

            # Paths: (1 available, best #1, table default)
            # Paths: (1 available, best #1, table VRF1)
            # Paths: (1 available, best #1, no table)
            # Paths: (1 available, best #1, table default, RIB-failure(17))
            p2 = re.compile(r'^\s*Paths: +\((?P<paths>(?P<available_path>[0-9]+) +available\, +'
                             '(no +best +path|best +\#(?P<best_path>[0-9]+))\,?'
                             '(?: +(table +(?P<vrf_id>(\S+))|no +table),?)?(?: +(.*))?)\)')
            m = p2.match(line)
            if m:
                paths = m.groupdict()['paths']
                available_path = m.groupdict()['available_path']
                if m.groupdict()['best_path']:  
                    best_path = m.groupdict()['best_path']
                else: 
                    best_path = '' 
                if m.groupdict()['vrf_id']:
                    vrf = m.groupdict()['vrf_id']
                else:
                    vrf = 'default'
                if vrf not in bgp_dict['instance']['default']['vrf']:
                    bgp_dict['instance']['default']['vrf'][vrf] = {}
                if 'address_family' not in bgp_dict['instance']\
                    ['default']['vrf'][vrf]:
                    bgp_dict['instance']['default']['vrf'][vrf]\
                        ['address_family'] = {}

                # Adding the new_address_family that contains the RD info
                if new_address_family:
                    if new_address_family not in bgp_dict['instance']\
                        ['default']['vrf'][vrf]['address_family']:
                        bgp_dict['instance']['default']['vrf'][vrf]\
                            ['address_family'][new_address_family] = {}
                    if 'prefixes' not in bgp_dict['instance']['default']['vrf']\
                        [vrf]['address_family'][new_address_family]:
                        bgp_dict['instance']['default']['vrf'][vrf]\
                            ['address_family'][new_address_family]\
                            ['prefixes'] = {}
                    if prefixes not in bgp_dict['instance']['default']['vrf']\
                        [vrf]['address_family'][new_address_family]['prefixes']:
                        bgp_dict['instance']['default']['vrf'][vrf]\
                            ['address_family'][new_address_family]\
                            ['prefixes'][prefixes] = {}

                    # Adding the keys we got from 'BGP routing table' line
                    bgp_dict['instance']['default']['vrf'][vrf]\
                        ['address_family'][new_address_family]['prefixes']\
                        [prefixes]['table_version'] = prefix_table_version

                    # Adding the keys we got from 'Route Distinguisher' line
                    if route_distinguisher:
                        bgp_dict['instance']['default']['vrf'][vrf]\
                            ['address_family'][new_address_family]\
                            ['route_distinguisher'] = route_distinguisher
                        bgp_dict['instance']['default']['vrf'][vrf]\
                            ['address_family'][new_address_family]\
                            ['default_vrf'] = default_vrf

                    bgp_dict['instance']['default']['vrf'][vrf]\
                        ['address_family'][new_address_family]['prefixes']\
                        [prefixes]['available_path'] = available_path
                    bgp_dict['instance']['default']['vrf'][vrf]\
                        ['address_family'][new_address_family]['prefixes']\
                        [prefixes]['best_path'] = best_path
                    bgp_dict['instance']['default']['vrf'][vrf]\
                        ['address_family'][new_address_family]['prefixes']\
                        [prefixes]['paths'] = paths
                else:
                    if address_family not in bgp_dict['instance']\
                        ['default']['vrf'][vrf]['address_family']:
                        bgp_dict['instance']['default']['vrf'][vrf]\
                            ['address_family'][address_family] = {}
                    if 'prefixes' not in bgp_dict['instance']['default']['vrf']\
                        [vrf]['address_family'][address_family]:
                        bgp_dict['instance']['default']['vrf'][vrf]\
                            ['address_family'][address_family]['prefixes'] = {}
                    if prefixes not in bgp_dict['instance']['default']['vrf']\
                        [vrf]['address_family'][address_family]['prefixes']:
                        bgp_dict['instance']['default']['vrf'][vrf]\
                            ['address_family'][address_family]['prefixes']\
                                [prefixes] = {}

                    # Adding the keys we got from 'BGP routing table' line
                    bgp_dict['instance']['default']['vrf'][vrf]\
                        ['address_family'][address_family]['prefixes']\
                        [prefixes]['table_version'] = prefix_table_version

                    # Adding the keys we got from 'Route Distinguisher' line
                    if route_distinguisher:
                        bgp_dict['instance']['default']['vrf'][vrf]\
                            ['address_family'][address_family]\
                            ['route_distinguisher'] = route_distinguisher
                        bgp_dict['instance']['default']['vrf'][vrf]\
                            ['address_family'][address_family]\
                            ['default_vrf'] = default_vrf

                    bgp_dict['instance']['default']['vrf'][vrf]\
                        ['address_family'][address_family]['prefixes']\
                        [prefixes]['available_path'] = available_path
                    bgp_dict['instance']['default']['vrf'][vrf]\
                        ['address_family'][address_family]['prefixes']\
                        [prefixes]['best_path'] = best_path
                    bgp_dict['instance']['default']['vrf'][vrf]\
                        ['address_family'][address_family]['prefixes']\
                        [prefixes]['paths'] = paths

            # Route Distinguisher: 100:100 (default for vrf VRF1)
            # Route Distinguisher: 65535:1 (default for vrf evpn1)
            p2_1 = re.compile(r'^\s*Route +Distinguisher:'
                             ' +(?P<route_distinguisher>[0-9\:]+)'
                             ' +\(default +for +vrf +(?P<vrf_id>[a-zA-Z0-9]+)\)$')
            m = p2_1.match(line)
            if m:
                route_distinguisher = str(m.groupdict()['route_distinguisher'])
                default_vrf = str(m.groupdict()['vrf_id'])
                if address_family == 'vpnv4 unicast' or\
                    address_family == 'vpnv6 unicast':
                    new_address_family = \
                        original_address_family + ' RD ' + route_distinguisher
                continue

            # BGP routing table entry for 1.1.1.1/32, version 4
            # BGP routing table entry for [100:100]2001:11:11::11/128, version 2
            # BGP routing table entry for 100:100:11.11.11.11/32, version 2
            # BGP routing table entry for 2001:DB8:1:1::/64, version 5
            # BGP routing table entry for 2001:2:2:2::2/128, version 2
            # BGP routing table entry for [5][65535:1][0][24][3.3.3.0]/17, version 3
            p3 = re.compile(r'^\s*BGP +routing +table +entry +for +'
                             '(\[[0-9]+\])?((?P<route_distinguisher>((\[[0-9]+'
                             '[\:][0-9]+\])|([0-9]+[\:][0-9]+[\:]))))?(\['
                             '[0-9]+\])?(\[[0-9]+\])?(?P<router_id>((\[[0-9]+'
                             '[\.][0-9]+[\.][0-9]+[\.][0-9]+\][\/][0-9]+)|'
                             '([0-9]+[\.][0-9]+[\.][0-9]+[\.][0-9]+[\/][0-9]+)'
                             '|([a-zA-Z0-9]+[\:][a-zA-Z0-9]+[\:][a-zA-Z0-9]+'
                             '[\:][\:][a-zA-Z0-9]+[\/][0-9]+)|([a-zA-Z0-9]+'
                             '[\:][a-zA-Z0-9]+[\:][a-zA-Z0-9]+[\:][a-zA-Z0-9]'
                             '+[\:][\:][\/][0-9]+)|([a-zA-Z0-9]+[\:]'
                             '[a-zA-Z0-9]+[\:][a-zA-Z0-9]+[\:][a-zA-Z0-9]+[\:]'
                             '[\:][0-9]+[\/][0-9]+)))\, +version +'
                             '(?P<prefix_table_version>[0-9]+)$')
            m = p3.match(line)
            if m:
                update_group = 0
                index = 0
                prefixes = m.groupdict()['router_id']
                prefixes = prefixes.replace('[', '')
                prefixes = prefixes.replace(']', '')
                prefix_table_version = m.groupdict()['prefix_table_version']
                continue

            # 10.1.1.2 from 10.1.1.2 (10.1.1.2)
            # 2.2.2.2 (metric 11) (via default) from 2.2.2.2 (2.2.2.2)
            # :: (via vrf VRF1) from 0.0.0.0 (10.1.1.1)
            # 192.168.0.1 (inaccessible) from 192.168.0.9 (192.168.0.9)
            p4 = re.compile(r'^\s*((?P<nexthop>[a-zA-Z0-9\.\:]+)'
                             '(( +\(metric +(?P<next_hop_igp_metric>[0-9]+)\))|'
                             '( +\((?P<inaccessible>inaccessible)\)))?'
                             '( +\(via +(?P<next_hop_via>[a-zA-Z0-9\s]+)\))? +'
                             'from +(?P<gateway>[a-zA-Z0-9\.\:]+)'
                             ' +\((?P<originator>[0-9\.]+)\))$')
            m = p4.match(line)
            if m:
                index += 1
                nexthop = m.groupdict()['nexthop']
                gateway = m.groupdict()['gateway']
                originator = m.groupdict()['originator']
                if new_address_family:
                    if 'index' not in bgp_dict['instance']['default']['vrf']\
                        [vrf]['address_family'][new_address_family]['prefixes']\
                        [prefixes]:
                        bgp_dict['instance']['default']['vrf'][vrf]\
                            ['address_family'][new_address_family]['prefixes']\
                            [prefixes]['index'] = {}
                    if index not in bgp_dict['instance']['default']['vrf'][vrf]\
                        ['address_family'][new_address_family]['prefixes']\
                        [prefixes]['index']:
                        bgp_dict['instance']['default']['vrf'][vrf]\
                        ['address_family'][new_address_family]['prefixes']\
                                [prefixes]['index'][index] = {}
                        subdict = bgp_dict['instance']['default']['vrf'][vrf]\
                            ['address_family'][new_address_family]['prefixes']\
                            [prefixes]['index'][index]

                    subdict['next_hop'] = nexthop
                    subdict['gateway'] = gateway
                    subdict['originator'] = originator
                    if m.groupdict()['next_hop_igp_metric']:
                        subdict['next_hop_igp_metric'] = \
                            m.groupdict()['next_hop_igp_metric']
                    if m.groupdict()['inaccessible']:
                        subdict['inaccessible'] = True
                    else:
                        subdict['inaccessible'] = False
                    if m.groupdict()['next_hop_via']:
                        subdict['next_hop_via'] = \
                            m.groupdict()['next_hop_via']
                    # Adding update_group to each index
                    if update_group:
                        subdict['update_group'] = update_group
                else:
                    if 'index' not in bgp_dict['instance']['default']['vrf']\
                        [vrf]['address_family'][address_family]['prefixes']\
                        [prefixes]:
                        bgp_dict['instance']['default']['vrf'][vrf]\
                            ['address_family'][address_family]['prefixes']\
                            [prefixes]['index'] = {}
                    if index not in bgp_dict['instance']['default']['vrf']\
                        [vrf]['address_family'][address_family]['prefixes']\
                        [prefixes]['index']:
                        bgp_dict['instance']['default']['vrf'][vrf]\
                        ['address_family'][address_family]['prefixes']\
                                [prefixes]['index'][index] = {}
                        subdict = bgp_dict['instance']['default']['vrf'][vrf]\
                            ['address_family'][address_family]['prefixes']\
                            [prefixes]['index'][index]

                    subdict['next_hop'] = nexthop
                    subdict['gateway'] = gateway
                    subdict['originator'] = originator
                    if m.groupdict()['next_hop_igp_metric']:
                        subdict['next_hop_igp_metric'] = \
                            m.groupdict()['next_hop_igp_metric']
                    if m.groupdict()['next_hop_via']:
                        subdict['next_hop_via'] = \
                            m.groupdict()['next_hop_via']
                    # Adding update_group to each index
                    if update_group:
                        subdict['update_group'] = update_group
                continue

            # Origin incomplete, metric 0, localpref 100, valid, internal
            # Origin incomplete, metric 0, localpref 100, valid, internal, best
            # Origin incomplete, metric 0, localpref 100, weight 32768, valid, sourced, best
            p5 = re.compile(r'^\s*Origin +(?P<origin>[a-zA-Z]+),'
                             '(?: +metric +(?P<metric>[0-9]+),?)?'
                             '(?: +localpref +(?P<locprf>[0-9]+),?)?'
                             '(?: +weight +(?P<weight>[0-9]+),?)?'
                             '(?: +(?P<valid>(valid),?))?'
                             '(?: +(?P<sourced>(sourced),?))?'
                             '(?: +(?P<state>(internal|external),?))?'
                             '(?: +(?P<best>(best)))?$')
            m = p5.match(line)
            if m:
                status_codes = ''
                if m.groupdict()['locprf']:
                     subdict['localpref'] = int(m.groupdict()['locprf'])
                if m.groupdict()['metric']:
                     subdict['metric'] = int(m.groupdict()['metric'])
                if m.groupdict()['weight']:
                    subdict['weight'] = str(m.groupdict()['weight'])
                if m.groupdict()['origin']:
                    origin = str(m.groupdict()['origin'])
                    if origin == 'incomplete':
                        subdict['origin_codes'] = '?'
                    elif origin == 'EGP':
                        subdict['origin_codes'] = 'e'
                    else:
                        subdict['origin_codes'] = 'i'
                if m.groupdict()['valid']:
                    status_codes += '* '
                if m.groupdict()['best']:
                    status_codes = status_codes.rstrip()
                    status_codes += '>'
                if m.groupdict()['state']:
                    state = str(m.groupdict()['state'])
                    if state == 'internal':
                        status_codes += 'i'
                subdict['status_codes'] = status_codes

                # Adding the keys we got from 'Refresh Epoch' line
                subdict['refresh_epoch'] = refresh_epoch

                # Adding the keys we got from 'route_info' line
                if route_info:
                    subdict['route_info'] = route_info

                continue

            # Advertised to update-groups:
            p6_1 = re.compile(r'^\s*Advertised +to +update-groups *:$')
            m = p6_1.match(line)
            if m:
                next_line_update_group = True
                continue

            # Not advertised to any peer
            p6_2 = re.compile(r'^\s*Not +advertised +to +any +peer$')
            m = p6_2.match(line)
            if m:
                next_line_update_group = False
                continue

            # 3
            p6_3 = re.compile(r'^\s*           (?P<update_group>[0-9]+)$')
            m = p6_3.match(line)
            if m:
                update_group = int(m.groupdict()['update_group'])
                continue

            # Refresh Epoch 1
            p7 = re.compile(r'^\s*Refresh +Epoch +(?P<refresh_epoch>[0-9]+)$')
            m = p7.match(line)
            if m:
                refresh_epoch_flag = True
                refresh_epoch = int(m.groupdict()['refresh_epoch'])
                continue

            # Extended Community: RT:65535:1 ENCAP:8 Router MAC:001E.7A13.E9BF
            p8 = re.compile(r'^\s*Extended +Community\: +'
                             '(?:(?P<ext_community>[A-Z0-9\:]+))?'
                             '( +ENCAP)?(?:(?P<encap>[0-9\:]+))?'
                             '( +Router)?( +)?'
                             '(?:(?P<router_mac>[a-zA-Z0-9\:\.]+))?$')
            m = p8.match(line)
            if m:
                if 'evpn' not in subdict:
                    subdict['evpn'] = {}
                ext_community = m.groupdict()['ext_community']
                subdict['evpn']['ext_community'] = ext_community
                if m.groupdict()['encap']:
                    subdict['evpn']['encap'] = m.groupdict()['encap']
                if m.groupdict()['router_mac']:
                    subdict['evpn']['router_mac'] = m.groupdict()['router_mac']
                continue

            # rx pathid: 0, tx pathid: 0
            p9 = re.compile(r'^\s*rx +pathid\: +(?P<recipient_pathid>[0-9x]+)\,'
                             ' +tx +pathid\:'
                             ' +(?P<transfer_pathid>[0-9x]+)$')
            m = p9.match(line)
            if m:
                recipient_pathid = str(m.groupdict()['recipient_pathid'])
                transfer_pathid = str(m.groupdict()['transfer_pathid'])

                subdict['recipient_pathid'] = recipient_pathid
                subdict['transfer_pathid'] = transfer_pathid
                continue

            # EVPN ESI: 00000000000000000000, Gateway Address: 0.0.0.0, local vtep: 33.33.33.33, Label 30000
            p10 = re.compile(r'^\s*EVPN +ESI\: +(?P<evpn_esi>[0-9]+)\,'
                              ' +Gateway +Address\: +'
                              '(?P<gateway_address>[a-zA-Z0-9\.\:]+)\,'
                              ' +local vtep\: +(?P<local_vtep>[a-zA-Z0-9\.\:]+)'
                              '\, +[L|l]abel +(?P<label>[0-9]+)$')
            m = p10.match(line)
            if m:
                if 'evpn' not in subdict:
                    subdict['evpn'] = {}
                subdict['evpn']['evpn_esi'] = str(m.groupdict()['evpn_esi'])
                subdict['evpn']['local_vtep'] = str(m.groupdict()['local_vtep'])
                subdict['evpn']['gateway_address'] = \
                    str(m.groupdict()['gateway_address'])
                subdict['evpn']['label'] = int(m.groupdict()['label'])
                continue

            # Local vxlan vtep:
            p11 = re.compile(r'^\s*Local +vxlan +vtep\:$')
            m = p11.match(line)
            if m:
                if 'local_vxlan_vtep' not in subdict:
                    subdict['local_vxlan_vtep'] = {}
                local_vxlan_vtep = True
                continue

            # bdi:BDI200
            p12 = re.compile(r'^\s*bdi\:(?P<bdi>[A-Z0-9]+)$')
            m = p12.match(line)
            if m and local_vxlan_vtep:
                subdict['local_vxlan_vtep']['bdi'] = str(m.groupdict()['bdi'])
                continue

            # vrf:evpn1, vni:30000
            p13 = re.compile(r'^\s*vrf\:(?P<vrf>[a-zA-Z0-9]+)\,'
                              ' +vni\:(?P<vni>[0-9]+)$')
            m = p13.match(line)
            if m and local_vxlan_vtep:
                subdict['local_vxlan_vtep']['vrf'] = str(m.groupdict()['vrf'])
                subdict['local_vxlan_vtep']['vni'] = str(m.groupdict()['vni'])
                continue

            # local router mac:001E.7A13.E9BF
            p14 = re.compile(r'^\s*local +router +mac\:'
                              '(?P<local_router_mac>[a-zA-Z0-9\.]+)$')
            m = p14.match(line)
            if m and local_vxlan_vtep:
                subdict['local_vxlan_vtep']['local_router_mac'] = \
                    str(m.groupdict()['local_router_mac'])
                continue

            # encap:8
            p15 = re.compile(r'^\s*encap\:(?P<encap>[0-9]+)$')
            m = p15.match(line)
            if m and local_vxlan_vtep:
                subdict['local_vxlan_vtep']['encap'] = \
                    str(m.groupdict()['encap'])
                continue

            # vtep-ip:33.33.33.33
            p16 = re.compile(r'^\s*vtep-ip\:(?P<vtep_ip>[0-9\.]+)$')
            m = p16.match(line)
            if m and local_vxlan_vtep:
                subdict['local_vxlan_vtep']['vtep_ip'] = \
                str(m.groupdict()['vtep_ip'])
                continue

            # Local
            # 65530
            # Local, imported path from base
            # 200 33299 51178 47751 {27016}
            # 200 33299 51178 47751 {27016}, imported path from 200:2:15.1.1.0/24 (global)
            # 400 33299 51178 47751 {27016}, imported path from [400:1]646:22:22:4::/64 (VRF2)
            p17 = re.compile(r'^\s*(?P<route_info>[a-zA-Z0-9\.\,\{\}\s\(\)\.\/\:\[\]]+)$')
            m = p17.match(line)
            if m and refresh_epoch_flag:
                route_info = str(m.groupdict()['route_info'])
                refresh_epoch_flag = False
                continue

        return bgp_dict

# =================================================
# Parser for 'show bgp all neighbors <WORD> policy'
# =================================================

class ShowBgpAllNeighborsPolicySchema(MetaParser):

    """Schema for show bgp all neighbors <WORD> policy"""

    schema = {
        'vrf':
            {Any():
                {'neighbor':
                    {Any():
                        {'address_family':
                            {Any():
                                {Optional('nbr_af_route_map_name_in'): str,
                                 Optional('nbr_af_route_map_name_out'): str,
                                }
                            },
                        }
                    },
                }
            },
        }


class ShowBgpAllNeighborsPolicy(ShowBgpAllNeighborsPolicySchema):

    """Parser for show bgp all neighbors <neighbor> policy"""

    def cli(self, neighbor):

        # show bgp all neighbors {neighbor} policy
        cmd  = 'show bgp all neighbors {neighbor} policy'.format(neighbor=neighbor)
        out = self.device.execute(cmd)

        # Init dictionary
        policy_dict = {}

        for line in out.splitlines():
            line = line.rstrip()

            # Neighbor: 10.4.6.6, Address-Family: VPNv4 Unicast (VRF1)
            p1 = re.compile(r'^\s*Neighbor: +(?P<neighbor>[a-zA-Z0-9\.\:]+),'
                             ' +Address-Family: +(?P<address_family>[a-zA-Z0-9\s\-\_]+)'
                             '( +\((?P<vrf>[a-zA-Z0-9]+)\))?$')
            m = p1.match(line)
            if m:
                neighbor_id = str(m.groupdict()['neighbor'])
                address_family = str(m.groupdict()['address_family']).lower()
                if m.groupdict()['vrf']:
                    vrf = str(m.groupdict()['vrf'])
                else:
                    vrf = 'default'
                continue

            # route-map test in
            # route-map test out
            p2 = re.compile(r'^\s*route-map +(?P<route_map_name>\S+)'
                             ' +(?P<route_map_direction>[a-zA-Z]+)$')
            m = p2.match(line)
            if m:
                route_map_name = str(m.groupdict()['route_map_name'])
                route_map_direction = str(m.groupdict()['route_map_direction'])

                # Init dict
                if 'vrf' not in policy_dict:
                    policy_dict['vrf'] = {}
                if vrf not in policy_dict['vrf']:
                    policy_dict['vrf'][vrf] = {}
                if 'neighbor' not in policy_dict['vrf'][vrf]:
                    policy_dict['vrf'][vrf]['neighbor'] = {}
                if neighbor_id not in policy_dict['vrf'][vrf]['neighbor']:
                    policy_dict['vrf'][vrf]['neighbor'][neighbor_id] = {}
                if 'address_family' not in policy_dict['vrf'][vrf]['neighbor']\
                    [neighbor_id]:
                    policy_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                        ['address_family'] = {}
                if address_family not in policy_dict['vrf'][vrf]['neighbor']\
                    [neighbor_id]['address_family']:
                    policy_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                        ['address_family'][address_family] = {}

                if route_map_direction == 'in':
                    policy_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                        ['address_family'][address_family]['nbr_af_route_map_name_in'] = route_map_name
                else:
                    policy_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                        ['address_family'][address_family]['nbr_af_route_map_name_out'] = route_map_name

                continue

        return policy_dict

# ============================================================
# Parser for 'show bgp all neighbors <WORD> advertised-routes'
# ============================================================

class ShowBgpAllNeighborsAdvertisedRoutesSchema(MetaParser):

    """Schema for show bgp all neighbors <WORD> advertised-routes"""

    schema = {
        'vrf':
            {Any():
                {'neighbor':
                    {Any():
                        {'address_family':
                            {Any():
                                {Optional('bgp_table_version'): int,
                                 Optional('local_router_id'): str,
                                 Optional('route_distinguisher'): str,
                                 Optional('default_vrf'): str,
                                 Optional('advertised'):
                                    {Optional(Any()):
                                        {Optional('index'):
                                            {Optional(Any()):
                                                {Optional('next_hop'): str,
                                                 Optional('status_codes'): str,
                                                 Optional('path_type'): str,
                                                 Optional('metric'): int,
                                                 Optional('localprf'): int,
                                                 Optional('weight'): int,
                                                 Optional('path'): str,
                                                 Optional('origin_codes'): str,
                                                },
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


class ShowBgpAllNeighborsAdvertisedRoutes(ShowBgpAllNeighborsAdvertisedRoutesSchema):

    """Parser for show bgp all neighbors <WORD> advertised-routes"""

    def cli(self, neighbor):
        # find vrf names
        # show bgp all neighbors | i BGP neighbor
        cmd_vrfs = 'show bgp all neighbors | i BGP neighbor'
        out_vrf = self.device.execute(cmd_vrfs)
        vrf = 'default'

        for line in out_vrf.splitlines():
            if not line:
                continue
            else:
                line = line.rstrip()

            # BGP neighbor is 2.2.2.2,  remote AS 100, internal link
            p = re.compile(r'^\s*BGP +neighbor +is +(?P<bgp_neighbor>[0-9A-Z\:\.]+)'
                            '(, +vrf +(?P<vrf>[0-9A-Za-z]+))?, +remote AS '
                            '+(?P<remote_as_id>[0-9]+), '
                            '+(?P<internal_external_link>[a-z\s]+)$')
            m = p.match(line)
            if m:
                # Extract the neighbor corresponding VRF name
                bgp_neighbor = str(m.groupdict()['bgp_neighbor'])
                if bgp_neighbor == neighbor:
                    if m.groupdict()['vrf']:
                        vrf = str(m.groupdict()['vrf'])
                else:
                    continue

        # show bgp all neighbors {neighbor} advertised-routes
        cmd  = 'show bgp all neighbors {neighbor} advertised-routes'.format(neighbor=neighbor)
        out = self.device.execute(cmd)

        # Init dictionary
        route_dict = {}
        af_dict = {}

        # Init vars
        data_on_nextline =  False
        index = 1
        bgp_table_version = local_router_id = ''

        for line in out.splitlines():
            line = line.rstrip()

            # For address family: IPv4 Unicast
            p1 = re.compile(r'^\s*For +address +family:'
                             ' +(?P<address_family>[a-zA-Z0-9\s\-\_]+)$')
            m = p1.match(line)
            if m:
                neighbor_id = str(neighbor)
                address_family = str(m.groupdict()['address_family']).lower()
                original_address_family = address_family
                continue

            # BGP table version is 25, Local Router ID is 21.0.101.1
            p2 = re.compile(r'^\s*BGP +table +version +is'
                             ' +(?P<bgp_table_version>[0-9]+), +[Ll]ocal +[Rr]outer'
                             ' +ID +is +(?P<local_router_id>(\S+))$')
            m = p2.match(line)
            if m:
                bgp_table_version = int(m.groupdict()['bgp_table_version'])
                local_router_id = str(m.groupdict()['local_router_id'])

                # Init dict
                if 'vrf' not in route_dict:
                    route_dict['vrf'] = {}
                if vrf not in route_dict['vrf']:
                    route_dict['vrf'][vrf] = {}
                if 'neighbor' not in route_dict['vrf'][vrf]:
                    route_dict['vrf'][vrf]['neighbor'] = {}
                if neighbor_id not in route_dict['vrf'][vrf]['neighbor']:
                    route_dict['vrf'][vrf]['neighbor'][neighbor_id] = {}
                if 'address_family' not in route_dict['vrf'][vrf]['neighbor']\
                    [neighbor_id]:
                    route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                        ['address_family'] = {}
                if address_family not in route_dict['vrf'][vrf]['neighbor']\
                    [neighbor_id]['address_family']:
                    route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                        ['address_family'][address_family] = {}

                # Set af_dict
                af_dict = route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                    ['address_family'][address_family]

                # Init advertised dict
                if 'advertised' not in af_dict:
                    af_dict['advertised'] = {}

                route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                    ['address_family'][address_family]['bgp_table_version'] = \
                        bgp_table_version
                route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                    ['address_family'][address_family]['local_router_id'] = \
                        local_router_id
                continue

            # Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
            # Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
            # Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

            # *>i[2]:[77][7,0][9.9.9.9,1,151587081][29.1.1.1,22][19.0.101.1,29.0.1.30]/616
            # *>iaaaa:1::/113       ::ffff:19.0.101.1
            # *>  646:22:22::/64   2001:DB8:20:4:6::6
            p3_1 = re.compile(r'^\s*(?P<status_codes>(s|x|S|d|h|\*|\>|\s)+)?'
                             '(?P<path_type>(i|e|c|l|a|r|I))?'
                             '(?P<prefix>[a-zA-Z0-9\.\:\/\[\]\,]+)'
                             '(?: *(?P<next_hop>[a-zA-Z0-9\.\:\/\[\]\,]+))?$')
            m = p3_1.match(line)
            if m:
                # New prefix, reset index count
                index = 1
                data_on_nextline = True

                # Get keys
                if m.groupdict()['status_codes']:
                    status_codes = str(m.groupdict()['status_codes'].rstrip())
                if m.groupdict()['path_type']:
                    path_type = str(m.groupdict()['path_type'])
                if m.groupdict()['prefix']:
                    prefix = str(m.groupdict()['prefix'])

                # Init dict
                if 'advertised' not in af_dict:
                    af_dict['advertised'] = {}
                if prefix not in af_dict['advertised']:
                    af_dict['advertised'][prefix] = {}
                if 'index' not in af_dict['advertised'][prefix]:
                    af_dict['advertised'][prefix]['index'] = {}
                if index not in af_dict['advertised'][prefix]['index']:
                    af_dict['advertised'][prefix]['index'][index] = {}

                # Set keys
                if m.groupdict()['status_codes']:
                    af_dict['advertised'][prefix]['index'][index]['status_codes'] = status_codes
                if m.groupdict()['path_type']:
                    af_dict['advertised'][prefix]['index'][index]['path_type'] = path_type
                if m.groupdict()['next_hop']:
                    af_dict['advertised'][prefix]['index'][index]['next_hop'] = str(m.groupdict()['next_hop'])
                continue

            # Network            Next Hop            Metric     LocPrf     Weight Path
            # *>i 15.1.2.0/24      1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
            # *>l1.1.1.0/24         0.0.0.0                           100      32768 i
            # *>r1.3.1.0/24         0.0.0.0               4444        100      32768 ?
            # *>r1.3.2.0/24         0.0.0.0               4444        100      32768 ?
            # *>i1.6.0.0/16         19.0.101.1                        100          0 10 20 30 40 50 60 70 80 90 i
            # *>i1.1.2.0/24         19.0.102.4                        100          0 {62112 33492 4872 41787 13166 50081 21461 58376 29755 1135} i
            # Condition placed to handle the situation of a long line that is
            # divided nto two lines while actually it is not another index.
            if not data_on_nextline:
                p3_2 = re.compile(r'^\s*(?P<status_codes>(s|x|S|d|h|\*|\>|\s)+)'
                                   '(?P<path_type>(i|e|c|l|a|r|I))?(\s)?'
                                   '(?P<prefix>(([0-9]+[\.][0-9]+[\.][0-9]+'
                                   '[\.][0-9]+[\/][0-9]+)|([a-zA-Z0-9]+[\:]'
                                   '[a-zA-Z0-9]+[\:][a-zA-Z0-9]+[\:]'
                                   '[a-zA-Z0-9]+[\:][\:][\/][0-9]+)|'
                                   '([a-zA-Z0-9]+[\:][a-zA-Z0-9]+[\:]'
                                   '[a-zA-Z0-9]+[\:][\:][\/][0-9]+)))'
                                   ' +(?P<next_hop>[a-zA-Z0-9\.\:]+)'
                                   ' +(?P<numbers>[a-zA-Z0-9\s\(\)\{\}]+)'
                                   ' +(?P<origin_codes>(i|e|\?|\&|\|))$')
                m = p3_2.match(line)
                if m:
                    # New prefix, reset index count
                    index = 1

                    # Get keys
                    if m.groupdict()['status_codes']:
                        status_codes = str(m.groupdict()['status_codes'].rstrip())
                    if m.groupdict()['path_type']:
                        path_type = str(m.groupdict()['path_type'])
                    if m.groupdict()['prefix']:
                        prefix = str(m.groupdict()['prefix'])
                    if m.groupdict()['next_hop']:
                        next_hop = str(m.groupdict()['next_hop'])
                    if m.groupdict()['origin_codes']:
                        origin_codes = str(m.groupdict()['origin_codes'])

                    # Init dict
                    if 'advertised' not in af_dict:
                        af_dict['advertised'] = {}
                    if prefix not in af_dict['advertised']:
                        af_dict['advertised'][prefix] = {}
                    if 'index' not in af_dict['advertised'][prefix]:
                        af_dict['advertised'][prefix]['index'] = {}
                    if index not in af_dict['advertised'][prefix]['index']:
                        af_dict['advertised'][prefix]['index'][index] = {}
                    if index not in af_dict['advertised'][prefix]['index']:
                        af_dict['advertised'][prefix]['index'][index] = {}

                    # Set keys
                    if m.groupdict()['status_codes']:
                        af_dict['advertised'][prefix]['index'][index]['status_codes'] = status_codes
                    if m.groupdict()['path_type']:
                        af_dict['advertised'][prefix]['index'][index]['path_type'] = path_type
                    if m.groupdict()['next_hop']:
                        af_dict['advertised'][prefix]['index'][index]['next_hop'] = next_hop
                    if m.groupdict()['origin_codes']:
                        af_dict['advertised'][prefix]['index'][index]['origin_codes'] = origin_codes

                    # Parse numbers
                    numbers = m.groupdict()['numbers']

                    # Metric     LocPrf     Weight Path
                    #    4444       100          0  10 3 10 20 30 40 50 60 70 80 90
                    m1 = re.compile(r'^(?P<metric>[0-9]+)'
                                     '(?P<space1>\s{4,10})'
                                     '(?P<localprf>[0-9]+)'
                                     '(?P<space2>\s{5,10})'
                                     '(?P<weight>[0-9]+)'
                                     '(?: *(?P<path>[0-9\{\}\s]+))?$').match(numbers)

                    #    100        ---          0 10 20 30 40 50 60 70 80 90
                    #    ---        100          0 10 20 30 40 50 60 70 80 90
                    #    100        ---      32788 ---
                    #    ---        100      32788 --- 
                    m2 = re.compile(r'^(?P<value>[0-9]+)'
                                     '(?P<space>\s{2,21})'
                                     '(?P<weight>[0-9]+)'
                                     '(?: *(?P<path>[0-9\{\}\s]+))?$').match(numbers)

                    #    ---        ---      32788 200 33299 51178 47751 {27016}
                    m3 = re.compile(r'^(?P<weight>[0-9]+)'
                                     ' +(?P<path>[0-9\{\}\s]+)$').match(numbers)

                    if m1:
                        af_dict['advertised'][prefix]['index'][index]['metric'] = int(m1.groupdict()['metric'])
                        af_dict['advertised'][prefix]['index'][index]['localprf'] = int(m1.groupdict()['localprf'])
                        af_dict['advertised'][prefix]['index'][index]['weight'] = int(m1.groupdict()['weight'])
                        # Set path
                        if m1.groupdict()['path']:
                            af_dict['advertised'][prefix]['index'][index]['path'] = m1.groupdict()['path'].strip()
                            continue
                    elif m2:
                        af_dict['advertised'][prefix]['index'][index]['weight'] = int(m2.groupdict()['weight'])
                        # Set metric or localprf
                        if len(m2.groupdict()['space']) > 10:
                            af_dict['advertised'][prefix]['index'][index]['metric'] = int(m2.groupdict()['value'])
                        else:
                            af_dict['advertised'][prefix]['index'][index]['localprf'] = int(m2.groupdict()['value'])
                        # Set path
                        if m2.groupdict()['path']:
                            af_dict['advertised'][prefix]['index'][index]['path'] = m2.groupdict()['path'].strip()
                            continue
                    elif m3:
                        af_dict['advertised'][prefix]['index'][index]['weight'] = int(m3.groupdict()['weight'])
                        af_dict['advertised'][prefix]['index'][index]['path'] = m3.groupdict()['path'].strip()
                        continue

            #                     0.0.0.0               100      32768 i
            #                     19.0.101.1            4444       100 0 3 10 20 30 40 50 60 70 80 90 i
            #*>i                  1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
            #                                           2219             0 400 33299 51178 47751 {27016} e
            p3_3 = re.compile(r'^\s*(?P<status_codes>(s|x|S|d|h|\*|\>|\s)+)?'
                               '(?P<path_type>(i|e|c|l|a|r|I))?'
                               ' +(?P<next_hop>(([0-9]+[\.][0-9]+[\.][0-9]'
                               '+[\.][0-9]+)|([a-zA-Z0-9]+[\:][a-zA-Z0-9]+'
                               '[\:][a-zA-Z0-9]+[\:][a-zA-Z0-9]+[\:]'
                               '[a-zA-Z0-9]+[\:][\:][a-zA-Z0-9])|'
                               '([a-zA-Z0-9]+[\:][a-zA-Z0-9]+[\:][a-zA-Z0-9]+'
                               '[\:][a-zA-Z0-9]+[\:][\:][a-zA-Z0-9])))?'
                               '(?: +(?P<numbers>[a-zA-Z0-9\s\(\)\{\}]+))?'
                               ' +(?P<origin_codes>(i|e|\?|\|))$')
            m = p3_3.match(line)
            if m:
                # Get keys
                if m.groupdict()['next_hop']:
                    next_hop = str(m.groupdict()['next_hop'])
                if m.groupdict()['origin_codes']:
                    origin_codes = str(m.groupdict()['origin_codes'])

                if data_on_nextline:
                    data_on_nextline =  False
                else:
                    index += 1

                # Init dict
                if 'advertised' not in af_dict:
                    af_dict['advertised'] = {}
                if prefix not in af_dict['advertised']:
                    af_dict['advertised'][prefix] = {}
                if 'index' not in af_dict['advertised'][prefix]:
                    af_dict['advertised'][prefix]['index'] = {}
                if index not in af_dict['advertised'][prefix]['index']:
                    af_dict['advertised'][prefix]['index'][index] = {}

                # Set keys
                if m.groupdict()['next_hop']:
                    af_dict['advertised'][prefix]['index'][index]['next_hop'] = next_hop
                if m.groupdict()['origin_codes']:
                    af_dict['advertised'][prefix]['index'][index]['origin_codes'] = origin_codes
                try:
                    # Set values of status_codes and path_type from prefix line
                    af_dict['advertised'][prefix]['index'][index]['status_codes'] = status_codes
                    af_dict['advertised'][prefix]['index'][index]['path_type'] = path_type
                except Exception:
                    pass

                # Parse numbers
                numbers = m.groupdict()['numbers']

                # Metric     LocPrf     Weight Path
                #    4444       100          0  10 3 10 20 30 40 50 60 70 80 90
                m1 = re.compile(r'^(?P<metric>[0-9]+)'
                                 '(?P<space1>\s{4,10})'
                                 '(?P<localprf>[0-9]+)'
                                 '(?P<space2>\s{5,10})'
                                 '(?P<weight>[0-9]+)'
                                 '(?: *(?P<path>[0-9\{\}\s]+))?$').match(numbers)

                #    100        ---          0 10 20 30 40 50 60 70 80 90
                #    ---        100          0 10 20 30 40 50 60 70 80 90
                #    100        ---      32788 ---
                #    ---        100      32788 --- 
                m2 = re.compile(r'^(?P<value>[0-9]+)'
                                 '(?P<space>\s{2,21})'
                                 '(?P<weight>[0-9]+)'
                                 '(?: *(?P<path>[0-9\{\}\s]+))?$').match(numbers)

                #    ---        ---      32788 200 33299 51178 47751 {27016}
                m3 = re.compile(r'^(?P<weight>[0-9]+)'
                                 ' +(?P<path>[0-9\{\}\s]+)$').match(numbers)

                if m1:
                    af_dict['advertised'][prefix]['index'][index]['metric'] = int(m1.groupdict()['metric'])
                    af_dict['advertised'][prefix]['index'][index]['localprf'] = int(m1.groupdict()['localprf'])
                    af_dict['advertised'][prefix]['index'][index]['weight'] = int(m1.groupdict()['weight'])
                    # Set path
                    if m1.groupdict()['path']:
                        af_dict['advertised'][prefix]['index'][index]['path'] = m1.groupdict()['path'].strip()
                        continue
                elif m2:
                    af_dict['advertised'][prefix]['index'][index]['weight'] = int(m2.groupdict()['weight'])
                    # Set metric or localprf
                    if len(m2.groupdict()['space']) > 10:
                        af_dict['advertised'][prefix]['index'][index]['metric'] = int(m2.groupdict()['value'])
                    else:
                        af_dict['advertised'][prefix]['index'][index]['localprf'] = int(m2.groupdict()['value'])
                    # Set path
                    if m2.groupdict()['path']:
                        af_dict['advertised'][prefix]['index'][index]['path'] = m2.groupdict()['path'].strip()
                        continue
                elif m3:
                    af_dict['advertised'][prefix]['index'][index]['weight'] = int(m3.groupdict()['weight'])
                    af_dict['advertised'][prefix]['index'][index]['path'] = m3.groupdict()['path'].strip()
                    continue

            # Route Distinguisher: 200:1
            # Route Distinguisher: 300:1 (default for vrf VRF1) VRF Router ID 44.44.44.44
            p4 = re.compile(r'^\s*Route +Distinguisher *: '
                             '+(?P<route_distinguisher>(\S+))'
                             '( +\(default for vrf +(?P<default_vrf>(\S+))\))?'
                             '( +VRF Router ID (?P<vrf_router_id>(\S+)))?$')
            m = p4.match(line)
            if m:
                route_distinguisher = str(m.groupdict()['route_distinguisher'])
                new_address_family = original_address_family + ' RD ' + route_distinguisher

                # Init dict
                if 'address_family' not in route_dict['vrf'][vrf]['neighbor']\
                        [neighbor_id]:
                    route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                        ['address_family'] = {}
                if new_address_family not in route_dict['vrf'][vrf]['neighbor']\
                    [neighbor_id]['address_family']:
                    route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                        ['address_family'][new_address_family] = {}

                # Set keys
                route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                    ['address_family'][new_address_family]['bgp_table_version'] = bgp_table_version
                route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                    ['address_family'][new_address_family]['local_router_id'] = local_router_id
                route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                    ['address_family'][new_address_family]['route_distinguisher'] = route_distinguisher
                if m.groupdict()['default_vrf']:
                    route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                        ['address_family'][new_address_family]['default_vrf'] = \
                            str(m.groupdict()['default_vrf'])

                # Reset address_family key and af_dict for use in other regex
                address_family = new_address_family
                af_dict = route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                    ['address_family'][address_family]

                # Init advertised dict
                if 'advertised' not in af_dict:
                    af_dict['advertised'] = {}
                    continue

        return route_dict


class ShowBgpAllSummarySchema(MetaParser):
    """Schema for show bgp all summary """
    schema = {
        'bgp_id': int,
        'vrf':
            {Any():
                 {Optional('neighbor'):
                      {Any():
                           {'address_family':
                                {Any():
                                     {'version': int,
                                      'as': int,
                                      'msg_rcvd': int,
                                      'msg_sent': int,
                                      'tbl_ver': int,
                                      'input_queue': int,
                                      'output_queue': int,
                                      'up_down': str,
                                      'state_pfxrcd': str,
                                      Optional('route_identifier'): str,
                                      Optional('local_as'): int,
                                      Optional('bgp_table_version'): int,
                                      Optional('routing_table_version'): int,
                                      Optional('prefixes'):
                                          {'total_entries': int,
                                           'memory_usage': int,
                                           },
                                      Optional('path'):
                                          {'total_entries': int,
                                           'memory_usage': int,
                                           },
                                      Optional('cache_entries'):
                                          {Any():
                                               {
                                                'total_entries': int,
                                                'memory_usage': int,
                                               },
                                          },
                                      Optional('entries'):
                                          {Any():
                                              {
                                                  'total_entries': int,
                                                  'memory_usage': int,
                                              },
                                          },
                                      Optional('community_entries'):
                                          {'total_entries': int,
                                           'memory_usage': int,
                                           },
                                      Optional('attribute_entries'): str,
                                      Optional('total_memory'): int,
                                      Optional('activity_prefixes'): str,
                                      Optional('activity_paths'): str,
                                      Optional('scan_interval'): int,
                                      },
                                 },
                            },
                       },
                  },
             },
        }


class ShowBgpAllSummary(ShowBgpAllSummarySchema):
    """
    Parser for show bgp All Summary
    """

    def cli(self):
        cmd = 'show bgp all summary'
        out = self.device.execute(cmd)

        # Init vars
        sum_dict = {}
        cache_dict = {}
        entries_dict = {}

        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            # For address family: IPv4 Unicast
            p1 = re.compile(r'^\s*For address family: +(?P<address_family>[a-zA-Z0-9\s\-\_]+)$')
            m = p1.match(line)
            if m:
                # Save variables for use later
                address_family = str(m.groupdict()['address_family']).lower()
                vrf = 'default'
                attribute_entries = ""
                num_prefix_entries = ""
                path_total_entries = ""
                total_memory = ""
                activity_paths = ""
                activity_prefixes = ""
                scan_interval = ""
                cache_dict = {}
                entries_dict = {}
                num_community_entries = ""
                continue

            # BGP router identifier 200.0.1.1, local AS number 100
            p2 = re.compile(r'^\s*BGP +router +identifier'
                            ' +(?P<route_identifier>[0-9\.\:]+), +local +AS'
                            ' +number +(?P<local_as>[0-9]+)$')
            m = p2.match(line)
            if m:
                route_identifier = str(m.groupdict()['route_identifier'])
                local_as = int(m.groupdict()['local_as'])

                if 'bgp_id' not in sum_dict:
                    sum_dict['bgp_id'] = local_as

                if 'vrf' not in sum_dict:
                    sum_dict['vrf'] = {}
                if vrf not in sum_dict['vrf']:
                    sum_dict['vrf'][vrf] = {}
                continue

            # BGP table version is 28, main routing table version 28
            p3 = re.compile(r'^\s*BGP +table +version +is'
                            ' +(?P<bgp_table_version>[0-9]+),'
                            ' +main +routing +table +version'
                            ' +(?P<routing_table_version>[0-9]+)$')
            m = p3.match(line)
            if m:
                bgp_table_version = int(m.groupdict()['bgp_table_version'])
                routing_table_version = int(m.groupdict()['routing_table_version'])
                continue

            # 27 network entries using 6696 bytes of memory
            p4 = re.compile(r'^\s*(?P<networks>[0-9]+) +network +entries +using'
                            ' +(?P<bytes>[0-9]+) +bytes +of +memory$')

            m = p4.match(line)
            if m:
                num_prefix_entries = int(m.groupdict()['networks'])
                num_memory_usage = int(m.groupdict()['bytes'])
                continue

            # 27 path entries using 3672 bytes of memory
            p5 = re.compile(r'^\s*(?P<path>[0-9]+) +path +entries +using'
                            ' +(?P<memory_usage>[0-9]+) +bytes +of +memory$')
            m = p5.match(line)
            if m:
                path_total_entries = int(m.groupdict()['path'])
                path_memory_usage = int(m.groupdict()['memory_usage'])
                continue

            # 2 BGP rrinfo entries using 48 bytes of memory
            p5_1 = re.compile(r'^\s*(?P<num_entries>([0-9]+)) +BGP +(?P<entries_type>(\S+)) +entries +using'
                              ' +(?P<entries_byte>[0-9]+) +bytes +of +memory$')
            m = p5_1.match(line)
            if m:
                num_entries = int(m.groupdict()['num_entries'])
                entries_type = str(m.groupdict()['entries_type'])
                entries_byte = int(m.groupdict()['entries_byte'])

                entries_dict[entries_type] = {}
                entries_dict[entries_type]['total_entries'] = num_entries
                entries_dict[entries_type]['memory_usage'] = entries_byte
                continue

            # 4 BGP extended community entries using 96 bytes of memory
            p5_2 = re.compile(r'^\s*(?P<num_community_entries>[0-9]+) +BGP +extended +community +entries +using'
                            ' +(?P<memory_usage>[0-9]+) +bytes +of +memory$')
            m = p5_2.match(line)
            if m:
                num_community_entries = int(m.groupdict()['num_community_entries'])
                community_memory_usage = int(m.groupdict()['memory_usage'])
                continue

            # 1/1 BGP path/bestpath attribute entries using 280 bytes of memory
            p6 = re.compile(r'^\s*(?P<attribute_entries>(\S+)) +BGP +(?P<attribute_type>(\S+))'
                            ' +attribute +entries +using +(?P<bytes>[0-9]+) +bytes +of +memory$')
            m = p6.match(line)
            if m:
                attribute_entries = str(m.groupdict()['attribute_entries'])
                attribute_type = str(m.groupdict()['attribute_type'])
                attribute_memory_usage = int(m.groupdict()['bytes'])
                continue

            # 0 BGP route-map cache entries using 0 bytes of memory
            p6_1 = re.compile(r'^\s*(?P<num_cache_entries>([0-9]+)) +BGP +(?P<cache_type>(\S+)) +cache +entries +using'
                            ' +(?P<cache_byte>[0-9]+) +bytes +of +memory$')
            m = p6_1.match(line)
            if m:
                num_cache_entries = int(m.groupdict()['num_cache_entries'])
                cache_type = str(m.groupdict()['cache_type'])
                cache_byte = int(m.groupdict()['cache_byte'])

                cache_dict[cache_type] = {}
                cache_dict[cache_type]['total_entries'] = num_cache_entries
                cache_dict[cache_type]['memory_usage'] = cache_byte
                continue

            # BGP using 10648 total bytes of memory
            p7 = re.compile(r'^\s*BGP +using'
                            ' +(?P<total_memory>[0-9]+) +total +bytes +of +memory$')
            m = p7.match(line)
            if m:
                total_memory = int(m.groupdict()['total_memory'])
                continue

            # BGP activity 47/20 prefixes, 66/39 paths, scan interval 60 secs
            p8 = re.compile(r'^\s*BGP +activity'
                            ' +(?P<activity_prefixes>(\S+)) +prefixes, +(?P<activity_paths>(\S+))'
                            ' +paths, +scan +interval +(?P<scan_interval>[0-9]+) +secs$')
            m = p8.match(line)
            if m:
                activity_prefixes = str(m.groupdict()['activity_prefixes'])
                activity_paths = str(m.groupdict()['activity_paths'])
                scan_interval = str(m.groupdict()['scan_interval'])
                continue


            # Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
            # 200.0.1.1       4          100       0       0        1    0    0 01:07:38 Idle
            # 200.0.2.1       4          100       0       0        1    0    0 never    Idle
            # 200.0.4.1       4          100       0       0        1    0    0 01:07:38 Idle

            p9 = re.compile(r'^\s*(?P<neighbor>[a-zA-Z0-9\.\:]+) +(?P<version>[0-9]+)'
                            ' +(?P<as>[0-9]+) +(?P<msg_rcvd>[0-9]+)'
                            ' +(?P<msg_sent>[0-9]+) +(?P<tbl_ver>[0-9]+)'
                            ' +(?P<inq>[0-9]+) +(?P<outq>[0-9]+)'
                            ' +(?P<up_down>[a-zA-Z0-9\:]+)'
                            ' +(?P<state>[a-zA-Z0-9\(\)\s]+)$')
            m = p9.match(line)
            if m:
                # Add neighbor to dictionary
                neighbor = str(m.groupdict()['neighbor'])
                if 'neighbor' not in sum_dict['vrf'][vrf]:
                    sum_dict['vrf'][vrf]['neighbor'] = {}
                if neighbor not in sum_dict['vrf'][vrf]['neighbor']:
                    sum_dict['vrf'][vrf]['neighbor'][neighbor] = {}
                nbr_dict = sum_dict['vrf'][vrf]['neighbor'][neighbor]

                # Add address family to this neighbor
                if 'address_family' not in nbr_dict:
                    nbr_dict['address_family'] = {}
                if address_family not in nbr_dict['address_family']:
                    nbr_dict['address_family'][address_family] = {}
                nbr_af_dict = nbr_dict['address_family'][address_family]

                # Add keys for this address_family
                nbr_af_dict['version'] = int(m.groupdict()['version'])
                nbr_af_dict['as'] = int(m.groupdict()['as'])
                nbr_af_dict['msg_rcvd'] = int(m.groupdict()['msg_rcvd'])
                nbr_af_dict['msg_sent'] = int(m.groupdict()['msg_sent'])
                nbr_af_dict['tbl_ver'] = int(m.groupdict()['tbl_ver'])
                nbr_af_dict['input_queue'] = int(m.groupdict()['inq'])
                nbr_af_dict['output_queue'] = int(m.groupdict()['outq'])
                nbr_af_dict['up_down'] = str(m.groupdict()['up_down'])
                nbr_af_dict['state_pfxrcd'] = str(m.groupdict()['state'])
                nbr_af_dict['route_identifier'] = route_identifier
                nbr_af_dict['local_as'] = local_as
                nbr_af_dict['bgp_table_version'] = bgp_table_version
                nbr_af_dict['routing_table_version'] = routing_table_version

                try:
                # Assign variables
                    if attribute_entries:
                        nbr_af_dict['attribute_entries'] = attribute_entries
                    if num_prefix_entries:
                        nbr_af_dict['prefixes'] = {}
                        nbr_af_dict['prefixes']['total_entries'] = num_prefix_entries
                        nbr_af_dict['prefixes']['memory_usage'] = num_memory_usage

                    if path_total_entries:
                        nbr_af_dict['path'] = {}
                        nbr_af_dict['path']['total_entries'] = path_total_entries
                        nbr_af_dict['path']['memory_usage'] = path_memory_usage

                    if total_memory:
                        nbr_af_dict['total_memory'] = total_memory

                    if activity_prefixes:
                        nbr_af_dict['activity_prefixes'] = activity_prefixes

                    if activity_paths:
                        nbr_af_dict['activity_paths'] = activity_paths

                    if scan_interval:
                        nbr_af_dict['scan_interval'] = int(scan_interval)

                    if len(cache_dict):
                        nbr_af_dict['cache_entries'] = cache_dict

                    if len(entries_dict):
                        nbr_af_dict['entries'] = entries_dict

                    if num_community_entries:
                        nbr_af_dict['community_entries'] = {}
                        nbr_af_dict['community_entries']['total_entries'] = num_community_entries
                        nbr_af_dict['community_entries']['memory_usage'] = community_memory_usage
                except Exception:
                    pass
            else:
                # when neighbor info break down to 2 lines.
                #  Neighbor        V           AS MsgRcvd MsgSent   TblVer  InQ OutQ Up/Down  State/PfxRcd
                #  2001:DB8:20:4:6::6
                #           4          400      67      73       66    0    0 01:03:11        5

                p10 = re.compile(r'^\s*(?P<neighbor>[a-zA-Z0-9\.\:]+)$')
                m = p10.match(line)
                if m :
                    # Add neighbor to dictionary
                    neighbor = str(m.groupdict()['neighbor'])
                    if 'neighbor' not in sum_dict['vrf'][vrf]:
                        sum_dict['vrf'][vrf]['neighbor'] = {}
                    if neighbor not in sum_dict['vrf'][vrf]['neighbor']:
                        sum_dict['vrf'][vrf]['neighbor'][neighbor] = {}
                    nbr_dict = sum_dict['vrf'][vrf]['neighbor'][neighbor]

                    # Add address family to this neighbor
                    if 'address_family' not in nbr_dict:
                        nbr_dict['address_family'] = {}
                    if address_family not in nbr_dict['address_family']:
                        nbr_dict['address_family'][address_family] = {}
                    nbr_af_dict = nbr_dict['address_family'][address_family]

                p11 = re.compile(r'^\s*(?P<version>[0-9]+)'
                                    ' +(?P<as>[0-9]+) +(?P<msg_rcvd>[0-9]+)'
                                    ' +(?P<msg_sent>[0-9]+) +(?P<tbl_ver>[0-9]+)'
                                    ' +(?P<inq>[0-9]+) +(?P<outq>[0-9]+)'
                                    ' +(?P<up_down>[a-zA-Z0-9\:]+)'
                                    ' +(?P<state>[a-zA-Z0-9\(\)\s]+)$')
                m = p11.match(line)
                if m:
                    # Add keys for this address_family
                    nbr_af_dict['version'] = int(m.groupdict()['version'])
                    nbr_af_dict['as'] = int(m.groupdict()['as'])
                    nbr_af_dict['msg_rcvd'] = int(m.groupdict()['msg_rcvd'])
                    nbr_af_dict['msg_sent'] = int(m.groupdict()['msg_sent'])
                    nbr_af_dict['tbl_ver'] = int(m.groupdict()['tbl_ver'])
                    nbr_af_dict['input_queue'] = int(m.groupdict()['inq'])
                    nbr_af_dict['output_queue'] = int(m.groupdict()['outq'])
                    nbr_af_dict['up_down'] = str(m.groupdict()['up_down'])
                    nbr_af_dict['state_pfxrcd'] = str(m.groupdict()['state'])
                    nbr_af_dict['route_identifier'] = route_identifier
                    nbr_af_dict['local_as'] = local_as
                    nbr_af_dict['bgp_table_version'] = bgp_table_version
                    nbr_af_dict['routing_table_version'] = routing_table_version

                    try:
                        # Assign variables
                        if attribute_entries:
                            nbr_af_dict['attribute_entries'] = attribute_entries
                        if num_prefix_entries:
                            nbr_af_dict['prefixes'] = {}
                            nbr_af_dict['prefixes']['total_entries'] = num_prefix_entries
                            nbr_af_dict['prefixes']['memory_usage'] = num_memory_usage

                        if path_total_entries:
                            nbr_af_dict['path'] = {}
                            nbr_af_dict['path']['total_entries'] = path_total_entries
                            nbr_af_dict['path']['memory_usage'] = path_memory_usage

                        if total_memory:
                            nbr_af_dict['total_memory'] = total_memory

                        if activity_prefixes:
                            nbr_af_dict['activity_prefixes'] = activity_prefixes

                        if activity_paths:
                            nbr_af_dict['activity_paths'] = activity_paths

                        if scan_interval:
                            nbr_af_dict['scan_interval'] = int(scan_interval)

                        if len(cache_dict):
                            nbr_af_dict['cache_entries'] = cache_dict

                        if len(entries_dict):
                            nbr_af_dict['entries'] = entries_dict

                        if num_community_entries:
                            nbr_af_dict['community_entries'] = {}
                            nbr_af_dict['community_entries']['total_entries'] = num_community_entries
                            nbr_af_dict['community_entries']['memory_usage'] = community_memory_usage
                    except Exception:
                        pass

                continue

        return sum_dict


class ShowBgpAllClusterIdsSchema(MetaParser):
    """Schema for show bgp all cluster-ids"""
    schema = {
              'vrf':
                    {Any():
                        {
                           Optional('cluster_id'): str,
                           Optional('configured_id'): str,
                           Optional('reflection_all_configured'): str,
                           Optional('reflection_intra_cluster_configured'): str,
                           Optional('reflection_intra_cluster_used'): str,
                           Optional('list_of_cluster_ids'):
                               {Any():
                                    {
                                        Optional('num_neighbors'): int,
                                        Optional('client_to_client_reflection_configured'): str,
                                        Optional('client_to_client_reflection_used'): str,

                                    }

                               }
                        }
                    },

                }

class ShowBgpAllClusterIds(ShowBgpAllClusterIdsSchema):
    """
       Parser for show bgp all cluster-ids
       Executing 'show vrf detail | inc \(VRF' to collect vrf names.
    """

    def cli(self):
        # find vrf names
        # show vrf detail | inc \(VRF
        cmd_vrfs = 'show vrf detail | inc \(VRF'
        out_vrf = self.device.execute(cmd_vrfs)
        vrf_dict = {'0':'default'}

        for line in out_vrf.splitlines():
            if not line:
                continue
            else:
                line = line.rstrip()

            # VRF VRF1 (VRF Id = 1); default RD 300:1; default VPNID <not set>
            p = re.compile(r'^\s*VRF +(?P<vrf_name>[0-9a-zA-Z]+)'
                            ' +\(+VRF +Id += +(?P<vrf_id>[0-9]+)+\)+;'
                            ' +default +(?P<other_data>.+)$')
            m = p.match(line)
            if m:
                # Save variables for use later
                vrf_name = str(m.groupdict()['vrf_name'])
                vrf_id = str(m.groupdict()['vrf_id'])
                vrf_dict[vrf_id] = vrf_name
                continue


        # show bgp all cluster-ids
        cmd = 'show bgp all cluster-ids'
        out = self.device.execute(cmd)

        # Init vars
        sum_dict = {}
        cluster_id = None
        list_of_cluster_ids = dict()
        configured_id = ""
        reflection_all_configured = ""
        reflection_intra_cluster_configured = ""
        reflection_intra_cluster_used = ""


        for line in out.splitlines():
            if line.strip():
                line = line.rstrip()
            else:
                continue

            # Global cluster-id: 4.4.4.4 (configured: 0.0.0.0)
            p1 = re.compile(r'^\s*Global +cluster-id: +(?P<cluster_id>[0-9\.]+)'
                            ' +\(+configured: +(?P<configured>[0-9\.]+)+\)$')
            m = p1.match(line)
            if m:
                # Save variables for use later
                cluster_id = str(m.groupdict()['cluster_id'])
                configured_id = str(m.groupdict()['configured'])

                if 'vrf' not in sum_dict:
                    sum_dict['vrf'] = {}

                continue

            #   all (inter-cluster and intra-cluster): ENABLED
            p3 = re.compile(r'^\s*all +\(+inter-cluster +and +intra-cluster+\):'
                            ' +(?P<all_configured>[a-zA-Z]+)$')
            m = p3.match(line)
            if m:
                reflection_all_configured = m.groupdict()['all_configured'].lower()
                continue

            # intra-cluster:                         ENABLED       ENABLED
            p4 = re.compile(r'^\s*intra-cluster:\s+(?P<intra_cluster_configured>[a-zA-Z]+)'
                            ' +(?P<intra_cluster_used>[a-zA-Z]+)$')
            m = p4.match(line)
            if m:
                reflection_intra_cluster_configured = m.groupdict()['intra_cluster_configured'].lower()
                reflection_intra_cluster_used = m.groupdict()['intra_cluster_used'].lower()
                continue

            # List of cluster-ids
            # Cluster-id  #-neighbors C2C-rfl-CFG C2C-rfl-USE
            # 192.168.1.1                2 DISABLED    DISABLED
            p5 = re.compile(r'^\s*(?P<cluster_ids>[0-9\.]+)'
                        ' +(?P<num_neighbors>[0-9]+)'
                        ' +(?P<client_to_client_ref_configured>[a-zA-Z]+)'
                        ' +(?P<client_to_client_ref_used>[a-zA-Z]+)$')
            m = p5.match(line)
            if m:
                cluster_ids = m.groupdict()['cluster_ids']
                list_of_cluster_ids[cluster_ids] = cluster_ids
                list_of_cluster_ids[cluster_ids] = {}
                list_of_cluster_ids[cluster_ids]['num_neighbors'] = int(m.groupdict()['num_neighbors'])
                list_of_cluster_ids[cluster_ids]['client_to_client_reflection_configured'] = \
                    m.groupdict()['client_to_client_ref_configured'].lower()
                list_of_cluster_ids[cluster_ids]['client_to_client_reflection_used'] = \
                    m.groupdict()['client_to_client_ref_used'].lower()

                continue

        for vrf_id, vrf_name in vrf_dict.items():
            if 'vrf' not in sum_dict:
                sum_dict['vrf'] = {}
            if vrf_name not in sum_dict['vrf']:
                sum_dict['vrf'][vrf_name] = {}
            if 'cluster_id' not in sum_dict['vrf'][vrf_name]:
                if not cluster_id:
                    del sum_dict['vrf']
                if cluster_id:
                    sum_dict['vrf'][vrf_name]['cluster_id'] = cluster_id
                if configured_id:
                    sum_dict['vrf'][vrf_name]['configured_id'] = configured_id
                if reflection_all_configured:
                    sum_dict['vrf'][vrf_name]['reflection_all_configured'] = \
                        reflection_all_configured
                if reflection_intra_cluster_configured:
                    sum_dict['vrf'][vrf_name]['reflection_intra_cluster_configured'] = \
                        reflection_intra_cluster_configured
                if reflection_intra_cluster_used:
                    sum_dict['vrf'][vrf_name]['reflection_intra_cluster_used'] = \
                        reflection_intra_cluster_used
                if list_of_cluster_ids:
                    sum_dict['vrf'][vrf_name]['list_of_cluster_ids'] = list_of_cluster_ids
        return sum_dict



class ShowBgpAllNeighborsSchema(MetaParser):
    """
    Schema for show bgp all neighbors
    """
    schema = {
        Optional('list_of_neighbors'): list,
        'vrf':
            {Any():
                 {
                 'neighbor':
                      {Any():
                          {Optional('remote_as'): int,
                          Optional('local_as'): int,
                          Optional('link'): str,
                          Optional('bgp_version'): int,
                          Optional('router_id'): str,
                          Optional('description'): str,
                          Optional('session_state'): str,
                          Optional('shutdown'): bool,

                          Optional('bgp_negotiated_keepalive_timers'):
                              {
                               Optional('keepalive_interval'): int,
                               Optional('hold_time'): int,
                               },

                          Optional('bgp_session_transport'):
                              {Optional('connection'):
                                   {
                                    Optional('last_reset'): str,
                                    Optional('reset_reason'): str,
                                    Optional('established'): int,
                                    Optional('dropped'): int,
                                    },
                              Optional('transport'):
                                   {Optional('local_port'): str,
                                    Optional('local_host'): str,
                                    Optional('foreign_port'): str,
                                    Optional('foreign_host'): str,
                                    Optional('mss'): int,
                                    },
                              Optional('min_time_between_advertisement_runs'): int,
                              Optional('address_tracking_status'): str,
                              Optional('rib_route_ip'): str,
                              Optional('tcp_path_mtu_discovery'): str,
                              Optional('graceful_restart'): str,
                              Optional('connection_state'): str,
                              Optional('io_status'): int,
                              Optional('unread_input_bytes'): int,
                              Optional('ecn_connection'): str,
                              Optional('minimum_incoming_ttl'): int,
                              Optional('outgoing_ttl'): int,
                              Optional('connection_tableid'): int,
                              Optional('maximum_output_segment_queue_size'): int,
                              Optional('enqueued_packets'):
                                  {
                                      Optional('retransmit_packet'): int,
                                      Optional('input_packet'): int,
                                      Optional('mis_ordered_packet'): int,
                                  },
                              Optional('iss'): int,
                              Optional('snduna'): int,
                              Optional('sndnxt'): int,
                              Optional('irs'): int,
                              Optional('rcvnxt'): int,
                              Optional('sndwnd'): int,
                              Optional('snd_scale'): int,
                              Optional('maxrcvwnd'): int,
                              Optional('rcvwnd'): int,
                              Optional('rcv_scale'): int,
                              Optional('delrcvwnd'): int,
                              Optional('srtt'): int,
                              Optional('rtto'): int,
                              Optional('rtv'): int,
                              Optional('krtt'): int,
                              Optional('min_rtt'): int,
                              Optional('max_rtt'): int,
                              Optional('ack_hold'): int,
                              Optional('uptime'): int,
                              Optional('sent_idletime'): int,
                              Optional('receive_idletime'): int,
                              Optional('status_flags'): str,
                              Optional('option_flags'): str,
                              Optional('ip_precedence_value'): int,
                              Optional('datagram'):
                                  {
                                      Optional('datagram_sent'):
                                          {
                                              Optional('value'): int,
                                              Optional('retransmit'): int,
                                              Optional('fastretransmit'): int,
                                              Optional('partialack'): int,
                                              Optional('second_congestion'): int,
                                              Optional('with_data'): int,
                                              Optional('total_data'): int,
                                          },
                                      Optional('datagram_received'):
                                          {
                                              Optional('value'): int,
                                              Optional('out_of_order'): int,
                                              Optional('with_data'): int,
                                              Optional('total_data'): int,
                                          },

                                      },
                                  Optional('packet_fast_path'): int,
                                  Optional('packet_fast_processed'): int,
                                  Optional('packet_slow_path'): int,
                                  Optional('fast_lock_acquisition_failures'): int,
                                  Optional('lock_slow_path'): int,
                                  Optional('tcp_semaphore'): str,
                                  Optional('tcp_semaphore_status'): str,

                              },
                          Optional('bgp_neighbor_counters'):
                              {Optional('messages'):
                                   {Optional('sent'):
                                        {
                                            Optional('opens'): int,
                                            Optional('updates'): int,
                                            Optional('notifications'): int,
                                            Optional('keepalives'): int,
                                            Optional('route_refresh'): int,
                                            Optional('total'): int,
                                         },
                                    Optional('received'):
                                        {
                                            Optional('opens'): int,
                                            Optional('updates'): int,
                                            Optional('notifications'): int,
                                            Optional('keepalives'): int,
                                            Optional('route_refresh'): int,
                                            Optional('total'): int,
                                         },
                                       Optional('in_queue_depth'): int,
                                       Optional('out_queue_depth'): int,
                                    },

                               },
                          Optional('bgp_negotiated_capabilities'):
                              {Optional('route_refresh'): str,
                               Optional('vpnv4_unicast'): str,
                               Optional('vpnv6_unicast'): str,
                               Optional('ipv4_unicast'): str,
                               Optional('ipv6_unicast'): str,
                               Optional('graceful_restart'): str,
                               Optional('graceful_restart_af_advertised_by_peer'): str,
                               Optional('graceful_remote_restart_timer'): int,
                               Optional('enhanced_refresh'): str,
                               Optional('multisession'): str,
                               Optional('four_octets_asn'): str,
                               Optional('stateful_switchover'): str,
                               },
                           Optional('bgp_event_timer'):
                               {Optional('starts'):
                                   {
                                       Optional('retrans'): int,
                                       Optional('timewait'): int,
                                       Optional('ackhold'): int,
                                       Optional('sendwnd'): int,
                                       Optional('keepalive'): int,
                                       Optional('giveup'): int,
                                       Optional('pmtuager'): int,
                                       Optional('deadwait'): int,
                                       Optional('linger'): int,
                                       Optional('processq'): int,
                                   },
                                   Optional('wakeups'):
                                       {
                                           Optional('retrans'): int,
                                           Optional('timewait'): int,
                                           Optional('ackhold'): int,
                                           Optional('sendwnd'): int,
                                           Optional('keepalive'): int,
                                           Optional('giveup'): int,
                                           Optional('pmtuager'): int,
                                           Optional('deadwait'): int,
                                           Optional('linger'): int,
                                           Optional('processq'): int,

                                       },
                                   Optional('next'):
                                       {
                                           Optional('retrans'): str,
                                           Optional('timewait'): str,
                                           Optional('ackhold'): str,
                                           Optional('sendwnd'): str,
                                           Optional('keepalive'): str,
                                           Optional('giveup'): str,
                                           Optional('pmtuager'): str,
                                           Optional('deadwait'): str,
                                           Optional('linger'): str,
                                           Optional('processq'): str,
                                       },

                               },

                          Optional('address_family'):
                              {Any():
                                   {
                                       Optional('last_read'): str,
                                       Optional('last_write'): str,
                                       Optional('up_time'): str,
                                       Optional('session_state'): str,
                                       Optional('down_time'): str,
                                       Optional('current_time'): str,
                               },
                          },
                     },
                 },
            },
        },
    }


class ShowBgpAllNeighbors(ShowBgpAllNeighborsSchema):
    """
    Parser for show bgp all neighbors
    """

    def cli(self):

        cmd = 'show bgp all neighbors'
        out = self.device.execute(cmd)

        # Init vars
        parsed_dict = {}
        af_name = ''

        for line in out.splitlines():
            if line.strip():
                line = line.rstrip()
            else:
                continue

            # For address family: IPv4 Unicast
            p1 = re.compile(r'^\s*For +address +family:'
                            ' +(?P<address_family>[a-zA-Z0-9\-\s]+)$')
            m = p1.match(line)
            if m:
                af_name = m.groupdict()['address_family'].lower()
                continue

            # BGP neighbor is 2.2.2.2,  remote AS 100, internal link
            p2 = re.compile(r'^\s*BGP +neighbor +is +(?P<neghibor>[0-9\S]+),'
                            '\s+remote +AS +(?P<remote_as>[0-9]+),'
                            ' +(?P<link>[a-zA-Z]+) +link$')
            m = p2.match(line)
            if m:
                neighbor_id = m.groupdict()['neghibor']
                vrf_name = 'default'
                remote_as = int(m.groupdict()['remote_as'])
                link = m.groupdict()['link']  # internal / external

                if 'list_of_neighbors' not in parsed_dict:
                    parsed_dict['list_of_neighbors'] = []
                parsed_dict['list_of_neighbors'].append(neighbor_id)

                if 'vrf' not in parsed_dict:
                    parsed_dict['vrf'] = {}
                if vrf_name not in parsed_dict['vrf']:
                    parsed_dict['vrf'][vrf_name] = {}

                if 'neighbor' not in parsed_dict['vrf']['default']:
                    parsed_dict['vrf']['default']['neighbor'] = {}

                if neighbor_id not in parsed_dict['vrf'][vrf_name]['neighbor']:
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] = {}
                    if remote_as is not None:
                        parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['remote_as'] = remote_as
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['link'] = link

                if 'address_family' not in  parsed_dict['vrf']\
                        [vrf_name]['neighbor'][neighbor_id]:
                    parsed_dict['vrf'][vrf_name]['neighbor']\
                        [neighbor_id]['address_family'] = {}

                if af_name:
                    parsed_dict['vrf'][vrf_name]['neighbor'] \
                        [neighbor_id]['address_family'][af_name] = {}
                continue

            # BGP neighbor is 20.4.6.6,  vrf VRF2,  remote AS 400, external link
            p2_2 = re.compile(r'^\s*BGP +neighbor +is +(?P<neghibor>[0-9\S]+),'
                              ' +vrf +(?P<vrf_name>[a-zA-Z0-9]+),'
                              '\s+remote +AS +(?P<remote_as>[0-9]+),'
                              '\s+(?P<link>[a-zA-Z]+) +link$')
            m = p2_2.match(line)
            if m:
                neighbor_id = m.groupdict()['neghibor']
                vrf_name = m.groupdict()['vrf_name']
                remote_as = int(m.groupdict()['remote_as'])
                link = m.groupdict()['link']  # internal / external

                if 'list_of_neighbors' not in parsed_dict:
                    parsed_dict['list_of_neighbors'] = []
                parsed_dict['list_of_neighbors'].append(neighbor_id)
                if 'vrf' not in parsed_dict:
                    parsed_dict['vrf'] = {}
                if vrf_name not in parsed_dict['vrf']:
                    parsed_dict['vrf'][vrf_name] = {}

                if 'neighbor' not in parsed_dict['vrf'][vrf_name]:
                    parsed_dict['vrf'][vrf_name]['neighbor'] = {}

                if neighbor_id not in parsed_dict['vrf'][vrf_name]['neighbor']:
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] = {}
                    if remote_as is not None:
                        parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['remote_as'] = remote_as
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['link'] = link

                if 'address_family' not in  parsed_dict['vrf']\
                        [vrf_name]['neighbor'][neighbor_id]:
                    parsed_dict['vrf'][vrf_name]['neighbor']\
                        [neighbor_id]['address_family'] = {}

                if af_name:
                    parsed_dict['vrf'][vrf_name]['neighbor'] \
                        [neighbor_id]['address_family'][af_name] = {}
                continue

            # IOS output
            # BGP neighbor is 50.1.1.101,  remote AS 300,  local AS 101, external link
            p2_3 = re.compile(r'^\s*BGP +neighbor +is +(?P<neghibor>[\w\.\:]+),'
                              '( +vrf +(?P<vrf_name>[a-zA-Z0-9]+),)?'
                              ' +remote +AS +(?P<remote_as>[0-9]+),'
                              ' +local +AS +(?P<local_as>[0-9]+),'
                              ' +(?P<link>[a-zA-Z]+) +link$')
            m = p2_3.match(line)
            if m:
                neighbor_id = m.groupdict()['neghibor']
                vrf_name = 'default' or m.groupdict()['vrf_name']
                remote_as = int(m.groupdict()['remote_as'])
                local_as = int(m.groupdict()['local_as'])
                link = m.groupdict()['link']  # internal / external

                if 'list_of_neighbors' not in parsed_dict:
                    parsed_dict['list_of_neighbors'] = []
                parsed_dict['list_of_neighbors'].append(neighbor_id)
                if 'vrf' not in parsed_dict:
                    parsed_dict['vrf'] = {}
                if vrf_name not in parsed_dict['vrf']:
                    parsed_dict['vrf'][vrf_name] = {}

                if 'neighbor' not in parsed_dict['vrf'][vrf_name]:
                    parsed_dict['vrf'][vrf_name]['neighbor'] = {}

                if neighbor_id not in parsed_dict['vrf'][vrf_name]['neighbor']:
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] = {}
                    if remote_as is not None:
                        parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['local_as'] = local_as
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['remote_as'] = remote_as
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['link'] = link

                if 'address_family' not in  parsed_dict['vrf']\
                        [vrf_name]['neighbor'][neighbor_id]:
                    parsed_dict['vrf'][vrf_name]['neighbor']\
                        [neighbor_id]['address_family'] = {}

                if af_name:
                    parsed_dict['vrf'][vrf_name]['neighbor'] \
                        [neighbor_id]['address_family'][af_name] = {}
                continue

            # Description: router22222222
            p2_1 = re.compile(r'^\s*Description: +(?P<description>[\w\s\S]+)$')
            m = p2_1.match(line)
            if m:
                description = m.groupdict()['description']
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['description']\
                    = description
                continue

            # Administratively shut down
            p2_3 = re.compile(r'^\s*Administratively shut down$')
            m = p2_3.match(line)
            if m:
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['shutdown'] = True
                continue

            # BGP version 4, remote router ID 2.2.2.2
            p3 = re.compile(r'^\s*BGP +version +(?P<bgp_version>[0-9]+),'
                            ' +remote +router +ID +(?P<remote_id>[0-9\.]+)$')
            m = p3.match(line)
            if m:
                bgp_version = int(m.groupdict()['bgp_version'])
                remote_router_id = m.groupdict()['remote_id']

                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['bgp_version'] = bgp_version
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['router_id'] = remote_router_id
                continue

            # BGP state = Established, up for 01:10:35
            # or
            # BGP state = Idle, down for 01:10:35
            # BGP state = Idle
            # or
            #   BGP state = Established, up for 1w2d
            p4 = re.compile(r'^\s*BGP +state += +(?P<session_state>[a-zA-Z]+)'
                            '(, +(?P<up_down>\w+) +for +(?P<time>[a-z0-9\:]+))?$')
            m = p4.match(line)
            if m:
                session_state = m.groupdict()['session_state']
                if m.groupdict()['up_down']:
                    up_down = m.groupdict()['up_down']
                if m.groupdict()['time']:
                    up_down_time = m.groupdict()['time']


                parsed_dict['vrf'][vrf_name]['neighbor']\
                [neighbor_id]['session_state'] = session_state.lower()

                if 'address_family' not in parsed_dict['vrf']\
                        [vrf_name]['neighbor'][neighbor_id]:
                    parsed_dict['vrf'][vrf_name]['neighbor']\
                        [neighbor_id]['address_family'] = {}

                if af_name:
                    if af_name not in parsed_dict['vrf'][vrf_name]['neighbor']\
                            [neighbor_id]['address_family']:
                        parsed_dict['vrf'][vrf_name]['neighbor']\
                            [neighbor_id]['address_family'][af_name] = {}

                    parsed_dict['vrf'][vrf_name]['neighbor']\
                        [neighbor_id]['address_family'][af_name]['session_state'] = session_state.lower()

                    if m.groupdict()['up_down'] and m.groupdict()['time']:
                        parsed_dict['vrf'][vrf_name]['neighbor']\
                            [neighbor_id]['address_family'][af_name][up_down+'_time'] = up_down_time

                continue

            # Last read 00:00:04, last write 00:00:09, hold time is 180, keepalive interval is 60 seconds
            p6 = re.compile(r'^\s*Last +read +(?P<last_read>[0-9\:]+),'
                            ' +last +write +(?P<last_write>[0-9\:]+),'
                            ' +hold +time +is +(?P<hold_time>[0-9]+),'
                            ' +keepalive +interval +is +(?P<keepalive_interval>[0-9]+)'
                            ' +seconds$')
            m = p6.match(line)
            if m:
                last_read = m.groupdict()['last_read']
                last_write = m.groupdict()['last_write']
                hold_time = int(m.groupdict()['hold_time'])
                keepalive_interval = int(m.groupdict()['keepalive_interval'])

                if 'bgp_negotiated_keepalive_timers' not in \
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]:
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['bgp_negotiated_keepalive_timers'] = {}

                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                    ['bgp_negotiated_keepalive_timers']['hold_time'] = hold_time

                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                    ['bgp_negotiated_keepalive_timers']['keepalive_interval'] = keepalive_interval

                if 'address_family' not in parsed_dict['vrf']\
                        [vrf_name]['neighbor'][neighbor_id]:
                    parsed_dict['vrf'][vrf_name]['neighbor']\
                        [neighbor_id]['address_family'] = {}

                if af_name:
                    if af_name not in parsed_dict['vrf'][vrf_name]['neighbor']\
                            [neighbor_id]['address_family']:
                        parsed_dict['vrf'][vrf_name]['neighbor']\
                            [neighbor_id]['address_family'][af_name] = {}

                    parsed_dict['vrf'][vrf_name]['neighbor']\
                        [neighbor_id]['address_family'][af_name]['last_read'] = last_read
                    parsed_dict['vrf'][vrf_name]['neighbor'] \
                        [neighbor_id]['address_family'][af_name]['last_write'] = last_write


                continue

            # Neighbor sessions:
            #  1 active, is not multisession capable (disabled)
            p7 = re.compile(r'^\s*(?P<num_neighbor_sessions>[0-9]+),'
                            ' +(?P<multisession_capable>[a-zA-Z\s]+) +multisession +capable'
                            ' +\(+(?P<multisession_status>[a-zA-Z])+\)$')
            m = p7.match(line)
            if m:
                num_neighbor_sessions = int(m.groupdict()['num_neighbor_sessions'])
                multisession_capable = m.groupdict()['multisession_capable']
                multisession_status = m.groupdict()['multisession_status']
                continue
            # Neighbor capabilities:
            #  Route refresh: advertised and received(new)
            p8 = re.compile(r'^\s*Route +refresh:'
                            ' +(?P<route_refresh>[\w\s\S]+)$')
            m = p8.match(line)
            if m:
                route_refresh = m.groupdict()['route_refresh']
                if 'bgp_negotiated_capabilities' not in \
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]:\
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['bgp_negotiated_capabilities'] = {}

                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                    ['bgp_negotiated_capabilities']['route_refresh'] = route_refresh
                continue

            #  Four-octets ASN Capability: advertised and received
            p9 = re.compile(r'^\s*Four-octets +ASN +Capability:'
                            ' +(?P<four_octets_asn_capability>[a-zA-Z\s]+)$')
            m = p9.match(line)
            if m:
                four_octets_asn_capability = m.groupdict()['four_octets_asn_capability']
                if 'bgp_negotiated_capabilities' not in \
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]:\
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['bgp_negotiated_capabilities'] = {}

                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                    ['bgp_negotiated_capabilities']['four_octets_asn'] = four_octets_asn_capability
                continue

            #  Address family VPNv4 Unicast: advertised and received
            p10 = re.compile(r'^\s*Address +family'
                             ' +VPNv4 +Unicast:'
                             ' +(?P<address_family_status>[a-zA-Z\s]+)$')
            m = p10.match(line)
            if m:
                address_family_status = m.groupdict()['address_family_status']
                if 'bgp_negotiated_capabilities' not in \
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]:\
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['bgp_negotiated_capabilities'] = {}
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                    ['bgp_negotiated_capabilities']['vpnv4_unicast'] = address_family_status
                continue

            #  Address family VPNv6 Unicast: advertised and received
            p10_1 = re.compile(r'^\s*Address +family'
                             ' +VPNv6 +Unicast:'
                             ' +(?P<address_family_status>[a-zA-Z\s]+)$')
            m = p10_1.match(line)
            if m:
                address_family_status = m.groupdict()['address_family_status']
                if 'bgp_negotiated_capabilities' not in \
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]:\
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['bgp_negotiated_capabilities'] = {}
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                    ['bgp_negotiated_capabilities']['vpnv6_unicast'] = address_family_status
                continue
            #  Address family IPv6 Unicast: advertised and received
            p10_2 = re.compile(r'^\s*Address +family'
                               ' +IPv6 +Unicast:'
                               ' +(?P<address_family_status>[a-zA-Z\s]+)$')
            m = p10_2.match(line)
            if m:
                address_family_status = m.groupdict()['address_family_status']
                if 'bgp_negotiated_capabilities' not in \
                        parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]: \
                        parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['bgp_negotiated_capabilities'] = {}
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                    ['bgp_negotiated_capabilities']['ipv6_unicast'] = address_family_status
                continue

            #  Address family IPv4 Unicast: advertised and received
            p10_3 = re.compile(r'^\s*Address +family'
                               ' +IPv4 +Unicast:'
                               ' +(?P<address_family_status>[a-zA-Z\s]+)$')
            m = p10_3.match(line)
            if m:
                address_family_status = m.groupdict()['address_family_status']
                if 'bgp_negotiated_capabilities' not in \
                        parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]: \
                        parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['bgp_negotiated_capabilities'] = {}
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                    ['bgp_negotiated_capabilities']['ipv4_unicast'] = address_family_status
                continue

            #  Graceful Restart Capability: received
            p11 = re.compile(r'^\s*Graceful +Restart +Capability:'
                             ' +(?P<graceful_restart_capability>[a-zA-Z\s]+)$')
            m = p11.match(line)
            if m:
                graceful_restart_capability = \
                    m.groupdict()['graceful_restart_capability']
                if 'bgp_negotiated_capabilities' not in \
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]:\
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['bgp_negotiated_capabilities'] = {}

                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                    ['bgp_negotiated_capabilities']['graceful_restart'] = graceful_restart_capability
                continue

            #   Remote Restart timer is 120 seconds
            p12 = re.compile(r'^\s*Remote +Restart +timer +is'
                             ' +(?P<remote_restart_timer>[0-9]+) +seconds$')
            m = p12.match(line)
            if m:
                remote_restart_timer = int(m.groupdict()['remote_restart_timer'])
                if 'bgp_negotiated_capabilities' not in \
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]:\
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['bgp_negotiated_capabilities'] = {}

                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                    ['bgp_negotiated_capabilities']['graceful_remote_restart_timer'] = remote_restart_timer
                continue

            #   Address families advertised by peer:
            p12_1 = re.compile(r'^\s*Address +families +advertised +by +peer:$')
            m = p12_1.match(line)
            if m:
                continue
            #    VPNv4 Unicast (was not preserved, VPNv6 Unicast (was not preserved
            p12_2 = re.compile(r'^\s*(?P<space>\s{8})+(?P<graceful_restart_af_advertised_by_peer>[0-9a-zA-Z\s\S]+)$')
            m = p12_2.match(line)
            if m:
                if len(m.groupdict()['space']) == 8 :
                    graceful_restart_af_advertised_by_peer = m.groupdict()['graceful_restart_af_advertised_by_peer']
                    if 'Sent' not in graceful_restart_af_advertised_by_peer and \
                        'Rcvd' not in graceful_restart_af_advertised_by_peer:

                        if 'bgp_negotiated_capabilities' not in \
                            parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]:\
                            parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                                ['bgp_negotiated_capabilities'] = {}

                        parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                            ['bgp_negotiated_capabilities']['graceful_restart_af_advertised_by_peer'] =\
                            graceful_restart_af_advertised_by_peer
                continue

            #  Enhanced Refresh Capability: advertised
            p13 = re.compile(r'^\s*Enhanced +Refresh +Capability:'
                             ' +(?P<enhanced_refresh_capability>[a-zA-Z\s]+)$')
            m = p13.match(line)
            if m:
                enhanced_refresh_capability = m.groupdict()['enhanced_refresh_capability']
                if 'bgp_negotiated_capabilities' not in \
                        parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]: \
                        parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['bgp_negotiated_capabilities'] = {}

                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                    ['bgp_negotiated_capabilities']['enhanced_refresh'] = enhanced_refresh_capability
                continue

            #  Multisession Capability:
            p14 = re.compile(r'^\s*Multisession +Capability:'
                             ' +(?P<multisession>[a-zA-Z\s]+)$')
            m = p14.match(line)
            if m:
                multisession_capability = m.groupdict()['multisession']
                if 'bgp_negotiated_capabilities' not in \
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]: \
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['bgp_negotiated_capabilities'] = {}

                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                ['bgp_negotiated_capabilities']['multisession'] = multisession_capability
                continue

            #  Stateful switchover support enabled: NO for session 1
            p15 = re.compile(r'^\s*Stateful +switchover +support'
                             ' +(?P<switchover>[a-zA-Z]+):'
                             ' +(?P<stateful_switchover>[0-9a-zA-Z\s\S]+)$')
            m = p15.match(line)
            if m:
                stateful_switchover = m.groupdict()['stateful_switchover']
                if 'bgp_negotiated_capabilities' not in \
                        parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]: \
                        parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['bgp_negotiated_capabilities'] = {}

                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                    ['bgp_negotiated_capabilities']['stateful_switchover'] = stateful_switchover
                continue

            # Message statistics:
            #  InQ depth is 0
            p18 = re.compile(r'^\s*InQ +depth +is'
                             ' +(?P<in_queue_depth>[0-9]+)$')
            m = p18.match(line)
            if m:
                message_input_queue = int(m.groupdict()['in_queue_depth'])
                if 'bgp_neighbor_counters' not in \
                        parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]: \
                        parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['bgp_neighbor_counters'] = {}
                if 'messages' not in parsed_dict['vrf'][vrf_name]['neighbor']\
                        [neighbor_id]['bgp_neighbor_counters']: \
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                        ['bgp_neighbor_counters']['messages'] = {}
                if 'in_queue_depth' not in parsed_dict['vrf'][vrf_name]\
                    ['neighbor'][neighbor_id]['bgp_neighbor_counters']['messages']:
                    parsed_dict['vrf'][vrf_name]\
                        ['neighbor'][neighbor_id]['bgp_neighbor_counters']['messages']\
                        ['in_queue_depth'] = message_input_queue

                continue
            #  OutQ depth is 0
            p19 = re.compile(r'^\s*OutQ +depth +is'
                             ' +(?P<out_queue_depth>[0-9]+)$')
            m = p19.match(line)
            if m:
                message_output_queue = int(m.groupdict()['out_queue_depth'])
                if 'bgp_neighbor_counters' not in \
                        parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]: \
                        parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['bgp_neighbor_counters'] = {}

                if 'messages' not in parsed_dict['vrf'][vrf_name]['neighbor']\
                        [neighbor_id]['bgp_neighbor_counters']: \
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                        ['bgp_neighbor_counters']['messages'] = {}

                if 'out_queue_depth' not in parsed_dict['vrf'][vrf_name]\
                    ['neighbor'][neighbor_id]['bgp_neighbor_counters']['messages']:
                    parsed_dict['vrf'][vrf_name]\
                        ['neighbor'][neighbor_id]['bgp_neighbor_counters']['messages']\
                        ['out_queue_depth'] = message_output_queue
                continue

            #                     Sent       Rcvd
            #  Opens:                  1          1
            #  Notifications:          0          0
            #  Updates:               11          6
            #  Keepalives:            75         74
            #  Route Refresh:          0          0
            #  Total:                 87         81
            p19_1 = re.compile(
                r'^\s*(?P<name>[a-zA-Z\s]+):\s+(?P<sent>[0-9]+) +(?P<received>[0-9]+)$')

            m = p19_1.match(line)
            if m:
                name = m.groupdict()['name'].replace(" ","_").lower()
                sent = int(m.groupdict()['sent'])
                received = int(m.groupdict()['received'])

                if 'bgp_neighbor_counters' not in \
                        parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]: \
                        parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['bgp_neighbor_counters'] = {}

                if 'messages' not in parsed_dict['vrf'][vrf_name]['neighbor']\
                        [neighbor_id]['bgp_neighbor_counters']: \
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                        ['bgp_neighbor_counters']['messages'] = {}

                if 'sent' not in parsed_dict['vrf'][vrf_name]['neighbor']\
                        [neighbor_id]['bgp_neighbor_counters']['messages']: \
                        parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                            ['bgp_neighbor_counters']['messages']['sent'] = {}
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                    ['bgp_neighbor_counters']['messages']['sent'][name] = sent


                if 'received' not in parsed_dict['vrf'][vrf_name]['neighbor']\
                        [neighbor_id]['bgp_neighbor_counters']['messages']:\
                        parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                            ['bgp_neighbor_counters']['messages']['received'] = {}
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                    ['bgp_neighbor_counters']['messages']['received'][name] = received

                continue

            # Default minimum time between advertisement runs is 0 seconds
            p26 = re.compile(r'^\s*Default +minimum +time +between +advertisement +runs +is'
                             ' +(?P<minimum_time_between_advertisement>[0-9]+)'
                             ' +seconds$')
            m = p26.match(line)
            if m:
                minimum_time_between_advertisement = int(m.groupdict()['minimum_time_between_advertisement'])
                if 'bgp_session_transport' not in \
                        parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]: \
                        parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                            ['bgp_session_transport'] = {}
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                    ['bgp_session_transport']['min_time_between_advertisement_runs']\
                    = minimum_time_between_advertisement
                continue

            # Address tracking is enabled, the RIB does have a route to 2.2.2.2
            p27 = re.compile(r'^\s*Address +tracking +is'
                             ' +(?P<address_tracking_status>[a-zA-Z]+),'
                             ' +the +RIB +does +have +a +route +to'
                             ' +(?P<rib_route_ip>[0-9\.\:\w]+)$')
            m = p27.match(line)
            if m:
                address_tracking_status = m.groupdict()['address_tracking_status']
                rib_route_ip = m.groupdict()['rib_route_ip']

                if 'bgp_session_transport' not in \
                        parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]: \
                        parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                            ['bgp_session_transport'] = {}
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                    ['bgp_session_transport']['address_tracking_status'] = address_tracking_status
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                    ['bgp_session_transport']['rib_route_ip'] = rib_route_ip

                continue

            # Connections established 1; dropped 0
            p28 = re.compile(r'^\s*Connections +established'
                             ' +(?P<num_connection_established>[0-9]+);'
                             ' +dropped +(?P<num_connection_dropped>[0-9]+)$')
            m = p28.match(line)
            if m:
                num_connection_established = int(m.groupdict()['num_connection_established'])
                num_connection_dropped = int(m.groupdict()['num_connection_dropped'])

                if 'bgp_session_transport' not in \
                        parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]: \
                        parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                            ['bgp_session_transport'] = {}

                if 'connection' not in parsed_dict['vrf'][vrf_name]\
                        ['neighbor'][neighbor_id]['bgp_session_transport']:
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                        ['bgp_session_transport']['connection'] = {}


                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                        ['bgp_session_transport']['connection']['established']\
                        = num_connection_established

                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                        ['bgp_session_transport']['connection']['dropped'] \
                        = num_connection_dropped
                continue

            # Last reset never
            p29 = re.compile(r'^\s*Last +reset'
                             ' +(?P<last_connection_reset>[a-zA-Z]+)$')
            m = p29.match(line)
            if m:
                last_connection_reset = m.groupdict()['last_connection_reset']
                if 'bgp_session_transport' not in \
                        parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]: \
                        parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                            ['bgp_session_transport'] = {}

                if 'connection' not in parsed_dict['vrf'][vrf_name] \
                        ['neighbor'][neighbor_id]['bgp_session_transport']:
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                        ['bgp_session_transport']['connection'] = {}

                if last_connection_reset:
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                        ['bgp_session_transport']['connection']['last_reset'] \
                        = last_connection_reset
                continue
            #Last reset 01:05:09, due to Active open failed
            p29_2 = re.compile(r'^\s*Last +reset'
                               ' +(?P<last_connection_reset>[0-9\:]+)\S'
                               ' +due +to (?P<reset_reason>[0-9a-zA-Z\s]+)$')
            m = p29_2.match(line)
            if m:
                last_connection_reset = m.groupdict()['last_connection_reset']
                reset_reason = m.groupdict()['reset_reason']
                if 'bgp_session_transport' not in \
                        parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]: \
                        parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                            ['bgp_session_transport'] = {}

                if 'connection' not in parsed_dict['vrf'][vrf_name] \
                        ['neighbor'][neighbor_id]['bgp_session_transport']:
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                        ['bgp_session_transport']['connection'] = {}

                if last_connection_reset:
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                        ['bgp_session_transport']['connection']['last_reset'] \
                        = last_connection_reset

                if reset_reason:
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                        ['bgp_session_transport']['connection']['reset_reason'] \
                        = reset_reason
                continue

            # Transport(tcp) path-mtu-discovery is enabled
            p30 = re.compile(r'^\s*Transport\(tcp\) +path-mtu-discovery +is'
                             ' +(?P<path_mtu_discovery_status>[a-zA-Z]+)$')
            m = p30.match(line)
            if m:
                path_mtu_discovery_status = m.groupdict()['path_mtu_discovery_status']
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                    ['bgp_session_transport']['tcp_path_mtu_discovery'] = path_mtu_discovery_status
                continue

            # Graceful-Restart is disabled
            p31 = re.compile(r'^\s*Graceful-Restart +is'
                             ' +(?P<graceful_restart>[a-zA-Z]+)$')
            m = p31.match(line)
            if m:
                graceful_restart = m.groupdict()['graceful_restart']
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                    ['bgp_session_transport']['graceful_restart'] = graceful_restart.lower()
                continue

            # Connection state is ESTAB, I/O status: 1, unread input bytes: 0
            p32 = re.compile(r'^\s*Connection +state +is'
                             ' +(?P<connection_state>[a-zA-Z]+),'
                             ' +I/O +status: (?P<num_io_status>[0-9]+),'
                             ' +unread +input +bytes:'
                             ' +(?P<num_unread_input_bytes>[0-9]+)$')
            m = p32.match(line)
            if m:
                connection_state = m.groupdict()['connection_state']
                num_io_status = int(m.groupdict()['num_io_status'])
                num_unread_input_bytes = int(m.groupdict()['num_unread_input_bytes'])

                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                    ['bgp_session_transport']['connection_state'] = connection_state.lower()

                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                    ['bgp_session_transport']['io_status'] = num_io_status
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                    ['bgp_session_transport']['unread_input_bytes'] = num_unread_input_bytes

                continue
            # Connection is ECN Disabled, Mininum incoming TTL 0, Outgoing TTL 255
            p33 = re.compile(r'^\s*Connection +is +ECN'
                             ' +(?P<connection_ecn_state>[a-zA-Z]+),'
                             ' +Mininum +incoming +TTL +(?P<minimum_incoming_ttl>[0-9]+),'
                             ' +Outgoing +TTL'
                             ' +(?P<minimum_outgoing_ttl>[0-9]+)$')
            m = p33.match(line)
            if m:
                connection_ecn_state = m.groupdict()['connection_ecn_state']
                minimum_incoming_ttl = int(m.groupdict()['minimum_incoming_ttl'])
                minimum_outgoing_ttl = int(m.groupdict()['minimum_outgoing_ttl'])

                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                    ['bgp_session_transport']['ecn_connection'] = connection_ecn_state.lower()
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                    ['bgp_session_transport']['minimum_incoming_ttl'] = minimum_incoming_ttl
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                    ['bgp_session_transport']['outgoing_ttl'] = minimum_outgoing_ttl
                continue

            # Local host: 4.4.4.4, Local port: 35281
            p34 = re.compile(r'^\s*Local +host:'
                             ' +(?P<local_host>[0-9\S]+),'
                             ' +Local +port: +(?P<local_port>[0-9]+)$')
            m = p34.match(line)
            if m:
                local_host = m.groupdict()['local_host']
                local_port = m.groupdict()['local_port']

                if 'bgp_session_transport' not in \
                        parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]: \
                        parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                            ['bgp_session_transport'] = {}

                if 'transport' not in parsed_dict['vrf'][vrf_name] \
                        ['neighbor'][neighbor_id]['bgp_session_transport']:
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                        ['bgp_session_transport']['transport'] = {}


                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                   ['bgp_session_transport']['transport']['local_host'] = local_host

                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                   ['bgp_session_transport']['transport']['local_port'] = local_port
                continue

            # Foreign host: 2.2.2.2, Foreign port: 179
            p35 = re.compile(r'^\s*Foreign +host:'
                             ' +(?P<foreign_host>[0-9\S]+),'
                             ' +Foreign +port: +(?P<foreign_port>[0-9]+)$')
            m = p35.match(line)
            if m:
                foreign_host = m.groupdict()['foreign_host']
                foreign_port = m.groupdict()['foreign_port']

                if 'bgp_session_transport' not in \
                        parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]:\
                        parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                            ['bgp_session_transport'] = {}

                if 'transport' not in parsed_dict['vrf'][vrf_name]\
                        ['neighbor'][neighbor_id]['bgp_session_transport']:
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                        ['bgp_session_transport']['transport'] = {}

                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                    ['bgp_session_transport']['transport']['foreign_host'] = foreign_host

                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                    ['bgp_session_transport']['transport']['foreign_port'] = foreign_port
                continue

            # Connection tableid (VRF): 0
            p36 = re.compile(r'^\s*Connection +tableid +\(VRF\):'
                             ' +(?P<num_connection_tableid>[0-9]+)$')
            m = p36.match(line)
            if m:
                num_connection_tableid = int(m.groupdict()['num_connection_tableid'])
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                    ['bgp_session_transport']['connection_tableid'] = num_connection_tableid
                continue

            # Maximum output segment queue size: 50
            p37 = re.compile(r'^\s*Maximum +output +segment +queue +size:'
                             ' +(?P<num_max_output_seg_queue_size>[0-9]+)$')
            m = p37.match(line)
            if m:
                num_max_output_seg_queue_size = int(m.groupdict()['num_max_output_seg_queue_size'])
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                    ['bgp_session_transport']['maximum_output_segment_queue_size'] = num_max_output_seg_queue_size

                continue

            # Enqueued packets for retransmit: 0, input: 0  mis-ordered: 0 (0 bytes)
            p38 = re.compile(r'^\s*Enqueued +packets +for +retransmit:'
                             ' +(?P<enqueued_packets_for_retransmit>[0-9]+),'
                             ' +input: +(?P<enqueued_packets_for_input>[0-9]+)'
                             '\s+mis-ordered: +(?P<enqueued_packets_for_mis_ordered>[0-9]+)'
                             ' +\((?P<num_bytes>[0-9]+) +bytes+\)$')

            m = p38.match(line)
            if m:
                enqueued_packets_for_retransmit = int(m.groupdict()['enqueued_packets_for_retransmit'])
                enqueued_packets_for_input = int(m.groupdict()['enqueued_packets_for_input'])
                enqueued_packets_for_mis_ordered = int(m.groupdict()['enqueued_packets_for_mis_ordered'])
                num_bytes = int(m.groupdict()['num_bytes'])

                if 'enqueued_packets' not in parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                    ['bgp_session_transport']:
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                        ['bgp_session_transport']['enqueued_packets'] = {}
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                    ['bgp_session_transport']['enqueued_packets']['retransmit_packet'] = enqueued_packets_for_retransmit
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                    ['bgp_session_transport']['enqueued_packets']['input_packet'] = enqueued_packets_for_input
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                    ['bgp_session_transport']['enqueued_packets']['mis_ordered_packet'] = enqueued_packets_for_mis_ordered

                continue
            # Event Timers (current time is 0x530449):
            p38_1 = re.compile(r'^\s*Event +Timers +\(+current +time +is +(?P<current_time>\S+)+\):$')
            m = p38_1.match(line)
            if m:
                current_time = m.groupdict()['current_time']

                if 'address_family' not in \
                        parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]: \
                        parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                            ['address_family'] = {}

                if af_name not in parsed_dict['vrf'][vrf_name]['neighbor']\
                        [neighbor_id]['address_family']:
                    parsed_dict['vrf'][vrf_name]['neighbor']\
                        [neighbor_id]['address_family'][af_name] = {}

                parsed_dict['vrf'][vrf_name]['neighbor']\
                    [neighbor_id]['address_family'][af_name]['current_time'] = current_time

                continue
            # Timer          Starts    Wakeups            Next
            # Retrans            86          0             0x0
            # TimeWait            0          0             0x0
            # AckHold            80         72             0x0
            # SendWnd             0          0             0x0
            # KeepAlive           0          0             0x0
            # GiveUp              0          0             0x0
            # PmtuAger            1          1             0x0
            # DeadWait            0          0             0x0
            # Linger              0          0             0x0
            # ProcessQ            0          0             0x0
            p39 = re.compile(
                r'^\s*(?P<name>\S+) +(?P<starts>[0-9]+) +(?P<wakeups>[0-9]+) +(?P<next>0x[0-9a-f]+)$')
            m = p39.match(line)
            if m:
                event_name = m.groupdict()['name'].lower()
                event_starts = int(m.groupdict()['starts'])
                event_wakeups = int(m.groupdict()['wakeups'])
                event_next = m.groupdict()['next']

                if 'bgp_event_timer' not in \
                        parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]: \
                        parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                            ['bgp_event_timer'] = {}
                if 'starts' not in parsed_dict['vrf'][vrf_name] \
                        ['neighbor'][neighbor_id]['bgp_event_timer']:
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                        ['bgp_event_timer']['starts'] = {}
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                        ['bgp_event_timer']['starts'][event_name] = event_starts

                if 'wakeups' not in parsed_dict['vrf'][vrf_name] \
                        ['neighbor'][neighbor_id]['bgp_event_timer']:
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                        ['bgp_event_timer']['wakeups'] = {}
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                        ['bgp_event_timer']['wakeups'][event_name] = event_wakeups

                if event_next:
                    if 'next' not in parsed_dict['vrf'][vrf_name]\
                            ['neighbor'][neighbor_id]['bgp_event_timer']:
                        parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                            ['bgp_event_timer']['next'] = {}
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                        ['bgp_event_timer']['next'][event_name] = event_next
                continue

            # iss:   55023811  snduna:   55027115  sndnxt:   55027115
            p40 = re.compile(r'^\s*iss:'
                             '\s+(?P<iss>[0-9]+)'
                             '\s+snduna: +(?P<snduna>[0-9]+)'
                             '\s+sndnxt: +(?P<sndnxt>[0-9]+)$')
            m = p40.match(line)
            if m:
                iss = int(m.groupdict()['iss'])
                snduna = int(m.groupdict()['snduna'])
                sndnxt = int(m.groupdict()['sndnxt'])

                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                    ['bgp_session_transport']['iss'] = iss
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                    ['bgp_session_transport']['snduna'] = snduna
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                    ['bgp_session_transport']['sndnxt'] = sndnxt
                continue

            # irs:  109992783  rcvnxt:  109995158
            p41 = re.compile(r'^\s*irs:'
                             '\s+(?P<irs>[0-9]+)'
                             '\s+rcvnxt: +(?P<rcvnxt>[0-9]+)$')
            m = p41.match(line)
            if m:
                irs = int(m.groupdict()['irs'])
                rcvnxt = int(m.groupdict()['rcvnxt'])

                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['bgp_session_transport']['irs'] = irs
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['bgp_session_transport']['rcvnxt'] = rcvnxt
                continue
            # sndwnd:  16616  scale:      0  maxrcvwnd:  16384
            p42 = re.compile(r'^\s*sndwnd:'
                             '\s+(?P<sndwnd>[0-9]+)'
                             '\s+scale: +(?P<snd_scale>[0-9]+)'
                             '\s+maxrcvwnd: +(?P<maxrcvwnd>[0-9]+)$')
            m = p42.match(line)
            if m:
                sndwnd = int(m.groupdict()['sndwnd'])
                send_scale = int(m.groupdict()['snd_scale'])
                maxrcvwnd = int(m.groupdict()['maxrcvwnd'])
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                    ['bgp_session_transport']['sndwnd'] = sndwnd
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                    ['bgp_session_transport']['snd_scale'] = send_scale
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                    ['bgp_session_transport']['maxrcvwnd'] = maxrcvwnd

                continue
            # rcvwnd:  16327  scale:      0  delrcvwnd:     57
            p43 = re.compile(r'^\s*rcvwnd:'
                             '\s+(?P<rcvwnd>[0-9]+)'
                             '\s+scale:\s+(?P<rcv_scale>[0-9]+)'
                             '\s+delrcvwnd:\s+(?P<delrcvwnd>[0-9]+)$')
            m = p43.match(line)
            if m:
                rcvwnd = int(m.groupdict()['rcvwnd'])
                rcv_scale = int(m.groupdict()['rcv_scale'])
                delrcvwnd = int(m.groupdict()['delrcvwnd'])

                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                    ['bgp_session_transport']['rcvwnd'] = rcvwnd
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                    ['bgp_session_transport']['rcv_scale'] = rcv_scale
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                    ['bgp_session_transport']['delrcvwnd'] = delrcvwnd
                continue
            # SRTT: 1000 ms, RTTO: 1003 ms, RTV: 3 ms, KRTT: 0 ms
            p44 = re.compile(r'^\s*SRTT:'
                             ' +(?P<srtt>[0-9]+) +ms,'
                             ' +RTTO: +(?P<rtto>[0-9]+) +ms,'
                             ' +RTV: +(?P<rtv>[0-9]+) +ms,'
                             ' +KRTT: +(?P<krtt>[0-9]+) +ms$')
            m = p44.match(line)
            if m:
                srtt = int(m.groupdict()['srtt'])
                rtto = int(m.groupdict()['rtto'])
                rtv = int(m.groupdict()['rtv'])
                krtt = int(m.groupdict()['krtt'])

                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['bgp_session_transport']['srtt'] = srtt
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['bgp_session_transport']['rtto'] = rtto
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['bgp_session_transport']['rtv'] = rtv
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['bgp_session_transport']['krtt'] = krtt
                continue

            # minRTT: 4 ms, maxRTT: 1000 ms, ACK hold: 200 ms
            p45 = re.compile(r'^\s*minRTT:'
                             ' +(?P<min_rtt>[0-9]+) +ms,'
                             ' +maxRTT: +(?P<max_rtt>[0-9]+) +ms,'
                             ' +ACK +hold: +(?P<ack_hold>[0-9]+) +ms$')
            m = p45.match(line)
            if m:
                min_rtt = int(m.groupdict()['min_rtt'])
                max_rtt = int(m.groupdict()['max_rtt'])
                ack_hold = int(m.groupdict()['ack_hold'])
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                    ['bgp_session_transport']['min_rtt'] = min_rtt
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                    ['bgp_session_transport']['max_rtt'] = max_rtt
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                    ['bgp_session_transport']['ack_hold'] = ack_hold
                continue
            # uptime: 4236258 ms, Sent idletime: 4349 ms, Receive idletime: 4549 ms
            p46 = re.compile(r'^\s*uptime:'
                             ' +(?P<uptime>[0-9]+) +ms,'
                             ' +Sent +idletime: +(?P<sent_idletime>[0-9]+) +ms,'
                             ' +Receive +idletime: +(?P<receive_idletime>[0-9]+) +ms$')
            m = p46.match(line)
            if m:
                uptime = int(m.groupdict()['uptime'])
                sent_idletime = int(m.groupdict()['sent_idletime'])
                receive_idletime = int(m.groupdict()['receive_idletime'])

                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                    ['bgp_session_transport']['uptime'] = uptime
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                    ['bgp_session_transport']['sent_idletime'] = sent_idletime
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                    ['bgp_session_transport']['receive_idletime'] = receive_idletime
                continue
            # Status Flags: active open
            p47 = re.compile(r'^\s*Status +Flags:'
                             ' +(?P<status_flags>[a-zA-Z\s\S]+)$')
            m = p47.match(line)
            if m:
                status_flags = m.groupdict()['status_flags']
                if 'bgp_session_transport' not in parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]:
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                        ['bgp_session_transport'] = {}

                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                    ['bgp_session_transport']['status_flags'] = status_flags
                continue

            # Option Flags: nagle, path mtu capable
            p48 = re.compile(r'^\s*Option +Flags:'
                             ' +(?P<option_flags>[a-zA-Z\s\,]+)$')
            m = p48.match(line)
            if m:
                option_flags = m.groupdict()['option_flags']
                if 'bgp_session_transport' not in parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]:
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                        ['bgp_session_transport'] = {}
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                    ['bgp_session_transport']['option_flags'] = option_flags
                continue

            # IP Precedence value : 6
            p49 = re.compile(r'^\s*IP +Precedence +value :'
                             ' +(?P<ip_precedence_value>[0-9]+)$')
            m = p49.match(line)
            if m:
                ip_precedence_value = int(m.groupdict()['ip_precedence_value'])
                if 'bgp_session_transport' not in parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]:
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                        ['bgp_session_transport'] = {}

                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                    ['bgp_session_transport']['ip_precedence_value'] = ip_precedence_value
                continue
            # Datagrams (max data segment is 536 bytes):
            p50 = re.compile(r'^\s*Datagrams +\(max +data +segment +is'
                             ' +(?P<datagram>[0-9]+) +bytes\):$')
            m = p50.match(line)
            if m:
                datagram = m.groupdict()['datagram']

                if 'bgp_session_transport' not in parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]:
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                        ['bgp_session_transport'] = {}

                if 'transport' not in parsed_dict['vrf'][vrf_name] \
                        ['neighbor'][neighbor_id]['bgp_session_transport']:
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                        ['bgp_session_transport']['transport'] = {}

                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                   ['bgp_session_transport']['transport']['mss'] = int(datagram)

                if 'datagram' not in parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                        ['bgp_session_transport']:
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                        ['bgp_session_transport']['datagram'] = {}

                continue
            # Rcvd: 164 (out of order: 0), with data: 80, total data bytes: 2374
            p51 = re.compile(r'^\s*Rcvd: (?P<received>[0-9]+)'
                             ' \(out +of +order: +(?P<out_of_order>[0-9]+)\),'
                             ' +with +data: (?P<with_data>[0-9]+),'
                             ' +total +data +bytes: (?P<total_data>[0-9]+)$')
            m = p51.match(line)
            if m:
                received = int(m.groupdict()['received'])
                out_of_order = int(m.groupdict()['out_of_order'])
                with_data = int(m.groupdict()['with_data'])
                total_data = int(m.groupdict()['total_data'])

                if 'bgp_session_transport' not in parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]:
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                        ['bgp_session_transport'] = {}


                if 'datagram' not in parsed_dict['vrf'][vrf_name]['neighbor']\
                        [neighbor_id]['bgp_session_transport']:
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                        ['bgp_session_transport']['datagram'] = {}
                if 'datagram_received' not in parsed_dict['vrf'][vrf_name]['neighbor']\
                        [neighbor_id]['bgp_session_transport']['datagram']:
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                    ['bgp_session_transport']['datagram']['datagram_received'] = {}

                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['bgp_session_transport']\
                    ['datagram']['datagram_received']['value'] = received
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['bgp_session_transport']\
                    ['datagram']['datagram_received']['out_of_order'] = out_of_order
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['bgp_session_transport']\
                    ['datagram']['datagram_received']['with_data'] = with_data
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['bgp_session_transport']\
                ['datagram']['datagram_received']['total_data'] = total_data
                continue
            # Sent: 166 (retransmit: 0, fastretransmit: 0, partialack: 0, Second Congestion: 0),
            #       with data: 87, total data bytes: 3303
            p52 = re.compile(r'^\s*Sent: (?P<sent>[0-9]+)'
                             ' \(retransmit: +(?P<retransmit>[0-9]+),'
                             ' +fastretransmit: +(?P<fastretransmit>[0-9]+),'
                             ' +partialack: +(?P<partialack>[0-9]+),'
                             ' +Second +Congestion: +(?P<second_congestion>[0-9]+)\),'
                             ' +with +data: (?P<sent_with_data>[0-9]+),'
                             ' +total +data +bytes: (?P<sent_total_data>[0-9]+)$')
            m = p52.match(line)
            if m:
                sent = int(m.groupdict()['sent'])
                retransmit = int(m.groupdict()['retransmit'])
                fastretransmit = int(m.groupdict()['fastretransmit'])
                partialack = int(m.groupdict()['partialack'])
                second_congestion = int(m.groupdict()['second_congestion'])
                sent_with_data = int(m.groupdict()['sent_with_data'])
                sent_total_data = int(m.groupdict()['sent_total_data'])

                if 'bgp_session_transport' not in parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]:
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                        ['bgp_session_transport'] = {}

                if 'datagram' not in parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                        ['bgp_session_transport']:
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]\
                        ['bgp_session_transport']['datagram'] = {}
                if 'datagram_sent' not in parsed_dict['vrf'][vrf_name]['neighbor']\
                        [neighbor_id]['bgp_session_transport']['datagram']:
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['bgp_session_transport']\
                        ['datagram']['datagram_sent'] = {}

                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['bgp_session_transport']\
                    ['datagram']['datagram_sent']['value'] = sent
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['bgp_session_transport']\
                    ['datagram']['datagram_sent']['retransmit'] = retransmit
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['bgp_session_transport']\
                    ['datagram']['datagram_sent']['fastretransmit'] = fastretransmit
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['bgp_session_transport']\
                    ['datagram']['datagram_sent']['partialack'] = partialack
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['bgp_session_transport']\
                    ['datagram']['datagram_sent']['second_congestion'] = second_congestion
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['bgp_session_transport']\
                    ['datagram']['datagram_sent']['with_data'] = sent_with_data
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]['bgp_session_transport']\
                    ['datagram']['datagram_sent']['total_data'] = sent_total_data
                continue

            # Packets received in fast path: 0, fast processed: 0, slow path: 0
            p53 = re.compile(r'^\s*Packets +received +in +fast +path:'
                             ' +(?P<packet_received_in_fast_path>[0-9]+),'
                             ' +fast +processed: +(?P<fast_processed>[0-9]+),'
                             ' +slow +path: +(?P<slow_path>[0-9]+)$')
            m = p53.match(line)
            if m:
                packet_received_in_fast_path = int(m.groupdict()['packet_received_in_fast_path'])
                fast_processed = int(m.groupdict()['fast_processed'])
                slow_path = int(m.groupdict()['slow_path'])

                if 'bgp_session_transport' not in parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]:
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                        ['bgp_session_transport'] = {}

                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                    ['bgp_session_transport']['packet_fast_path'] = packet_received_in_fast_path
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                    ['bgp_session_transport']['packet_fast_processed'] = fast_processed
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                    ['bgp_session_transport']['packet_slow_path'] = slow_path

                continue
            # fast lock acquisition failures: 0, slow path: 0
            p54 = re.compile(r'^\s*fast +lock +acquisition +failures:'
                             ' +(?P<fast_lock_acquisition_failures>[0-9]+),'
                             ' +slow +path: +(?P<slow_path>[0-9]+)$')
            m = p54.match(line)
            if m:
                fast_lock_acquisition_failures = int(m.groupdict()['fast_lock_acquisition_failures'])
                slow_path = int(m.groupdict()['slow_path'])

                if 'bgp_session_transport' not in parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]:
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                        ['bgp_session_transport'] = {}
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                    ['bgp_session_transport']['fast_lock_acquisition_failures'] = fast_lock_acquisition_failures
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                    ['bgp_session_transport']['lock_slow_path'] = slow_path
                continue

            # TCP Semaphore      0x1286E7EC  FREE 
            p55 = re.compile(r'^\s*TCP +Semaphore'
                             ' +(?P<tcp_semaphore>0x[0-9a-fA-F]+)'
                             ' +(?P<tcp_status>[a-zA-Z]+)$')
            m = p55.match(line)
            if m:
                tcp_semaphore = m.groupdict()['tcp_semaphore']
                tcp_status = m.groupdict()['tcp_status']
                if 'bgp_session_transport' not in parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id]:
                    parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                        ['bgp_session_transport'] = {}
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                    ['bgp_session_transport']['tcp_semaphore'] = tcp_semaphore
                parsed_dict['vrf'][vrf_name]['neighbor'][neighbor_id] \
                    ['bgp_session_transport']['tcp_semaphore_status'] = tcp_status
                continue

        return parsed_dict

# ==========================================================
# Parser for 'show bgp all neighbors <WORD> received-routes'
# ==========================================================

class ShowBgpAllNeighborsReceivedRoutesSchema(MetaParser):
    
    """Schema for show bgp all neighbors <WORD> received-routes"""

    schema = {
        'vrf':
            {Any():
                {'neighbor':
                    {Any():
                        {'address_family':
                            {Any():
                                {Optional('bgp_table_version'): int,
                                 Optional('local_router_id'): str,
                                 Optional('route_distinguisher'): str,
                                 Optional('default_vrf'): str,
                                 Optional('received_routes'): 
                                    {Optional(Any()):
                                        {Optional('index'):
                                            {Optional(Any()):
                                                {Optional('next_hop'): str,
                                                 Optional('status_codes'): str,
                                                 Optional('path_type'): str,
                                                 Optional('metric'): int,
                                                 Optional('localprf'): int,
                                                 Optional('weight'): int,
                                                 Optional('path'): str,
                                                 Optional('origin_codes'): str,
                                                },
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


class ShowBgpAllNeighborsReceivedRoutes(ShowBgpAllNeighborsReceivedRoutesSchema):

    """
    Parser for show bgp all neighbors <WORD> received-routes
    executing 'show bgp all neighbors | i BGP neighbor' for finging vrf names
    """

    def cli(self, neighbor):
        # find vrf names
        # show bgp all neighbors | i BGP neighbor
        cmd_vrfs = 'show bgp all neighbors | i BGP neighbor'
        out_vrf = self.device.execute(cmd_vrfs)
        vrf = 'default'

        for line in out_vrf.splitlines():
            if not line:
                continue
            else:
                line = line.rstrip()

            # BGP neighbor is 2.2.2.2,  remote AS 100, internal link
            p = re.compile(r'^\s*BGP +neighbor +is +(?P<bgp_neighbor>[0-9A-Z\:\.]+)'
                            '(, +vrf +(?P<vrf>[0-9A-Za-z]+))?, +remote AS '
                            '+(?P<remote_as_id>[0-9]+), '
                            '+(?P<internal_external_link>[a-z\s]+)$')
            m = p.match(line)
            if m:
                # Extract the neighbor corresponding VRF name
                bgp_neighbor = str(m.groupdict()['bgp_neighbor'])
                if bgp_neighbor == neighbor:
                    if m.groupdict()['vrf']:
                        vrf = str(m.groupdict()['vrf'])
                else:
                    continue

        # show bgp all neighbors {neighbor} received-routes
        cmd  = 'show bgp all neighbors {neighbor} received-routes'.format(neighbor=neighbor)
        out = self.device.execute(cmd)

        # Init dictionary
        route_dict = {}
        af_dict = {}

        # Init vars
        data_on_nextline =  False
        index = 1
        bgp_table_version = local_router_id = ''

        for line in out.splitlines():
            line = line.rstrip()

            # For address family: IPv4 Unicast
            p1 = re.compile(r'^\s*For +address +family:'
                             ' +(?P<address_family>[a-zA-Z0-9\s\-\_]+)$')
            m = p1.match(line)
            if m:
                neighbor_id = str(neighbor)
                address_family = str(m.groupdict()['address_family']).lower()
                original_address_family = address_family
                continue

            # BGP table version is 25, Local Router ID is 21.0.101.1
            p2 = re.compile(r'^\s*BGP +table +version +is'
                             ' +(?P<bgp_table_version>[0-9]+), +[Ll]ocal +[Rr]outer'
                             ' +ID +is +(?P<local_router_id>(\S+))$')
            m = p2.match(line)
            if m:
                bgp_table_version = int(m.groupdict()['bgp_table_version'])
                local_router_id = str(m.groupdict()['local_router_id'])

                # Init dict
                if 'vrf' not in route_dict:
                    route_dict['vrf'] = {}
                if vrf not in route_dict['vrf']:
                    route_dict['vrf'][vrf] = {}
                if 'neighbor' not in route_dict['vrf'][vrf]:
                    route_dict['vrf'][vrf]['neighbor'] = {}
                if neighbor_id not in route_dict['vrf'][vrf]['neighbor']:
                    route_dict['vrf'][vrf]['neighbor'][neighbor_id] = {}
                if 'address_family' not in route_dict['vrf'][vrf]['neighbor']\
                    [neighbor_id]:
                    route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                        ['address_family'] = {}
                if address_family not in route_dict['vrf'][vrf]['neighbor']\
                    [neighbor_id]['address_family']:
                    route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                        ['address_family'][address_family] = {}

                # Set af_dict
                af_dict = route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                    ['address_family'][address_family]

                # Init received_routes dict
                if 'received_routes' not in af_dict:
                    af_dict['received_routes'] = {}
                    
                route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                    ['address_family'][address_family]['bgp_table_version'] = \
                        bgp_table_version
                route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                    ['address_family'][address_family]['local_router_id'] = \
                        local_router_id
                continue

            # Status codes: s suppressed, d damped, h history, * valid, > best, i - internal, 
            #   r RIB-failure, S Stale, m multipath, b backup-path, f RT-Filter, 
            #   x best-external, a additional-path, c RIB-compressed, 
            # Origin codes: i - IGP, e - EGP, ? - incomplete
            # RPKI validation codes: V valid, I invalid, N Not found

            # *>i[2]:[77][7,0][9.9.9.9,1,151587081][29.1.1.1,22][19.0.101.1,29.0.1.30]/616
            # *>iaaaa:1::/113       ::ffff:19.0.101.1
            # *>  646:22:22::/64   2001:DB8:20:4:6::6
            p3_1 = re.compile(r'^\s*(?P<status_codes>(s|x|S|d|h|\*|\>|\s)+)?'
                             '(?P<path_type>(i|e|c|l|a|r|I))?'
                             '(?P<prefix>[a-zA-Z0-9\.\:\/\[\]\,]+)'
                             '(?: *(?P<next_hop>[a-zA-Z0-9\.\:\/\[\]\,]+))?$')
            m = p3_1.match(line)
            if m:
                # New prefix, reset index count
                index = 1
                data_on_nextline = True

                # Get keys
                if m.groupdict()['status_codes']:
                    status_codes = str(m.groupdict()['status_codes'].rstrip())
                if m.groupdict()['path_type']:
                    path_type = str(m.groupdict()['path_type'])
                if m.groupdict()['prefix']:
                    prefix = str(m.groupdict()['prefix'])

                # Init dict
                if 'received_routes' not in af_dict:
                    af_dict['received_routes'] = {}
                if prefix not in af_dict['received_routes']:
                    af_dict['received_routes'][prefix] = {}
                if 'index' not in af_dict['received_routes'][prefix]:
                    af_dict['received_routes'][prefix]['index'] = {}
                if index not in af_dict['received_routes'][prefix]['index']:
                    af_dict['received_routes'][prefix]['index'][index] = {}

                # Set keys
                if m.groupdict()['status_codes']:
                    af_dict['received_routes'][prefix]['index'][index]['status_codes'] = status_codes
                if m.groupdict()['path_type']:
                    af_dict['received_routes'][prefix]['index'][index]['path_type'] = path_type
                if m.groupdict()['next_hop']:
                    af_dict['received_routes'][prefix]['index'][index]['next_hop'] = str(m.groupdict()['next_hop'])
                continue

            # Network            Next Hop            Metric     LocPrf     Weight Path
            # *   46.1.1.0/24      10.4.6.6              2219             0 300 33299 51178 47751 {27016} e
            # *>l1.1.1.0/24         0.0.0.0                           100      32768 i
            # *>r1.3.1.0/24         0.0.0.0               4444        100      32768 ?
            # *>r1.3.2.0/24         0.0.0.0               4444        100      32768 ?
            # *>i1.6.0.0/16         19.0.101.1                        100          0 10 20 30 40 50 60 70 80 90 i
            # *>i1.1.2.0/24         19.0.102.4                        100          0 {62112 33492 4872 41787 13166 50081 21461 58376 29755 1135} i
            # Condition placed to handle the situation of a long line that is
            # divided nto two lines while actually it is not another index.
            if not data_on_nextline:
                p3_2 = re.compile(r'^\s*(?P<status_codes>(s|x|S|d|h|\*|\>|\s)+)'
                                   '(?P<path_type>(i|e|c|l|a|r|I))?(\s)?'
                                   '(?P<prefix>(([0-9]+[\.][0-9]+[\.][0-9]+'
                                   '[\.][0-9]+[\/][0-9]+)|([a-zA-Z0-9]+[\:]'
                                   '[a-zA-Z0-9]+[\:][a-zA-Z0-9]+[\:]'
                                   '[a-zA-Z0-9]+[\:][\:][\/][0-9]+)|'
                                   '([a-zA-Z0-9]+[\:][a-zA-Z0-9]+[\:]'
                                   '[a-zA-Z0-9]+[\:][\:][\/][0-9]+)))'
                                   ' +(?P<next_hop>[a-zA-Z0-9\.\:]+)'
                                   ' +(?P<numbers>[a-zA-Z0-9\s\(\)\{\}]+)'
                                   ' +(?P<origin_codes>(i|e|\?|\&|\|))$')
                m = p3_2.match(line)
                if m:
                    # New prefix, reset index count
                    index = 1

                    # Get keys
                    if m.groupdict()['status_codes']:
                        status_codes = str(m.groupdict()['status_codes'].rstrip())
                    if m.groupdict()['path_type']:
                        path_type = str(m.groupdict()['path_type'])
                    if m.groupdict()['prefix']:
                        prefix = str(m.groupdict()['prefix'])
                    if m.groupdict()['next_hop']:
                        next_hop = str(m.groupdict()['next_hop'])
                    if m.groupdict()['origin_codes']:
                        origin_codes = str(m.groupdict()['origin_codes'])

                    # Init dict
                    if 'received_routes' not in af_dict:
                        af_dict['received_routes'] = {}
                    if prefix not in af_dict['received_routes']:
                        af_dict['received_routes'][prefix] = {}
                    if 'index' not in af_dict['received_routes'][prefix]:
                        af_dict['received_routes'][prefix]['index'] = {}
                    if index not in af_dict['received_routes'][prefix]['index']:
                        af_dict['received_routes'][prefix]['index'][index] = {}
                    if index not in af_dict['received_routes'][prefix]['index']:
                        af_dict['received_routes'][prefix]['index'][index] = {}

                    # Set keys
                    if m.groupdict()['status_codes']:
                        af_dict['received_routes'][prefix]['index'][index]['status_codes'] = status_codes
                    if m.groupdict()['path_type']:
                        af_dict['received_routes'][prefix]['index'][index]['path_type'] = path_type
                    if m.groupdict()['next_hop']:
                        af_dict['received_routes'][prefix]['index'][index]['next_hop'] = next_hop
                    if m.groupdict()['origin_codes']:
                        af_dict['received_routes'][prefix]['index'][index]['origin_codes'] = origin_codes

                    # Parse numbers
                    numbers = m.groupdict()['numbers']

                    # Metric     LocPrf     Weight Path
                    #    4444       100          0  10 3 10 20 30 40 50 60 70 80 90
                    m1 = re.compile(r'^(?P<metric>[0-9]+)'
                                     '(?P<space1>\s{5,10})'
                                     '(?P<localprf>[0-9]+)'
                                     '(?P<space2>\s{5,10})'
                                     '(?P<weight>[0-9]+)'
                                     '(?: *(?P<path>[0-9\{\}\s]+))?$').match(numbers)

                    #    100        ---          0 10 20 30 40 50 60 70 80 90
                    #    ---        100          0 10 20 30 40 50 60 70 80 90
                    #    100        ---      32788 ---
                    #    ---        100      32788 --- 
                    m2 = re.compile(r'^(?P<value>[0-9]+)'
                                     '(?P<space>\s{2,21})'
                                     '(?P<weight>[0-9]+)'
                                     '(?: *(?P<path>[0-9\{\}\s]+))?$').match(numbers)

                    #    ---        ---      32788 200 33299 51178 47751 {27016}
                    m3 = re.compile(r'^(?P<weight>[0-9]+)'
                                     ' +(?P<path>[0-9\{\}\s]+)$').match(numbers)

                    if m1:
                        af_dict['received_routes'][prefix]['index'][index]['metric'] = int(m1.groupdict()['metric'])
                        af_dict['received_routes'][prefix]['index'][index]['localprf'] = int(m1.groupdict()['localprf'])
                        af_dict['received_routes'][prefix]['index'][index]['weight'] = int(m1.groupdict()['weight'])
                        # Set path
                        if m1.groupdict()['path']:
                            af_dict['received_routes'][prefix]['index'][index]['path'] = m1.groupdict()['path'].strip()
                            continue
                    elif m2:
                        af_dict['received_routes'][prefix]['index'][index]['weight'] = int(m2.groupdict()['weight'])
                        # Set metric or localprf
                        if len(m2.groupdict()['space']) > 10:
                            af_dict['received_routes'][prefix]['index'][index]['metric'] = int(m2.groupdict()['value'])
                        else:
                            af_dict['received_routes'][prefix]['index'][index]['localprf'] = int(m2.groupdict()['value'])
                        # Set path
                        if m2.groupdict()['path']:
                            af_dict['received_routes'][prefix]['index'][index]['path'] = m2.groupdict()['path'].strip()
                            continue
                    elif m3:
                        af_dict['received_routes'][prefix]['index'][index]['weight'] = int(m3.groupdict()['weight'])
                        af_dict['received_routes'][prefix]['index'][index]['path'] = m3.groupdict()['path'].strip()
                        continue

            #                     0.0.0.0               100      32768 i
            #                     19.0.101.1            4444       100 0 3 10 20 30 40 50 60 70 80 90 i
            p3_3 = re.compile(r'^\s*(?P<next_hop>[a-zA-Z0-9\.\:]+)'
                             '(?: +(?P<numbers>[a-zA-Z0-9\s\(\)\{\}]+))?'
                             ' +(?P<origin_codes>(i|e|\?|\|))$')
            m = p3_3.match(line)
            if m:
                # Get keys
                next_hop = str(m.groupdict()['next_hop'])
                origin_codes = str(m.groupdict()['origin_codes'])

                if data_on_nextline:
                    data_on_nextline =  False
                else:
                    index += 1

                # Init dict
                if 'received_routes' not in af_dict:
                    af_dict['received_routes'] = {}
                if prefix not in af_dict['received_routes']:
                    af_dict['received_routes'][prefix] = {}
                if 'index' not in af_dict['received_routes'][prefix]:
                    af_dict['received_routes'][prefix]['index'] = {}
                if index not in af_dict['received_routes'][prefix]['index']:
                    af_dict['received_routes'][prefix]['index'][index] = {}

                # Set keys
                af_dict['received_routes'][prefix]['index'][index]['next_hop'] = next_hop
                af_dict['received_routes'][prefix]['index'][index]['origin_codes'] = origin_codes
                try:
                    # Set values of status_codes and path_type from prefix line
                    af_dict['received_routes'][prefix]['index'][index]['status_codes'] = status_codes
                    af_dict['received_routes'][prefix]['index'][index]['path_type'] = path_type
                except Exception:
                    pass

                # Parse numbers
                numbers = m.groupdict()['numbers']

                # Metric     LocPrf     Weight Path
                #    4444       100          0  10 3 10 20 30 40 50 60 70 80 90
                m1 = re.compile(r'^(?P<metric>[0-9]+)'
                                 '(?P<space1>\s{5,10})'
                                 '(?P<localprf>[0-9]+)'
                                 '(?P<space2>\s{5,10})'
                                 '(?P<weight>[0-9]+)'
                                 '(?: *(?P<path>[0-9\{\}\s]+))?$').match(numbers)

                #    100        ---          0 10 20 30 40 50 60 70 80 90
                #    ---        100          0 10 20 30 40 50 60 70 80 90
                #    100        ---      32788 ---
                #    ---        100      32788 --- 
                m2 = re.compile(r'^(?P<value>[0-9]+)'
                                 '(?P<space>\s{2,21})'
                                 '(?P<weight>[0-9]+)'
                                 '(?: *(?P<path>[0-9\{\}\s]+))?$').match(numbers)

                #    ---        ---      32788 200 33299 51178 47751 {27016}
                m3 = re.compile(r'^(?P<weight>[0-9]+)'
                                 ' +(?P<path>[0-9\{\}\s]+)$').match(numbers)

                if m1:
                    af_dict['received_routes'][prefix]['index'][index]['metric'] = int(m1.groupdict()['metric'])
                    af_dict['received_routes'][prefix]['index'][index]['localprf'] = int(m1.groupdict()['localprf'])
                    af_dict['received_routes'][prefix]['index'][index]['weight'] = int(m1.groupdict()['weight'])
                    # Set path
                    if m1.groupdict()['path']:
                        af_dict['received_routes'][prefix]['index'][index]['path'] = m1.groupdict()['path'].strip()
                        continue
                elif m2:
                    af_dict['received_routes'][prefix]['index'][index]['weight'] = int(m2.groupdict()['weight'])
                    # Set metric or localprf
                    if len(m2.groupdict()['space']) > 10:
                        af_dict['received_routes'][prefix]['index'][index]['metric'] = int(m2.groupdict()['value'])
                    else:
                        af_dict['received_routes'][prefix]['index'][index]['localprf'] = int(m2.groupdict()['value'])
                    # Set path
                    if m2.groupdict()['path']:
                        af_dict['received_routes'][prefix]['index'][index]['path'] = m2.groupdict()['path'].strip()
                        continue
                elif m3:
                    af_dict['received_routes'][prefix]['index'][index]['weight'] = int(m3.groupdict()['weight'])
                    af_dict['received_routes'][prefix]['index'][index]['path'] = m3.groupdict()['path'].strip()
                    continue

            # Route Distinguisher: 200:1
            # Route Distinguisher: 300:1 (default for vrf VRF1) VRF Router ID 44.44.44.44
            p4 = re.compile(r'^\s*Route +Distinguisher *: '
                             '+(?P<route_distinguisher>(\S+))'
                             '( +\(default for vrf +(?P<default_vrf>(\S+))\))?'
                             '( +VRF Router ID (?P<vrf_router_id>(\S+)))?$')
            m = p4.match(line)
            if m:
                route_distinguisher = str(m.groupdict()['route_distinguisher'])
                new_address_family = original_address_family + ' RD ' + route_distinguisher
                
                # Init dict
                if 'address_family' not in route_dict['vrf'][vrf]['neighbor']\
                        [neighbor_id]:
                    route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                        ['address_family'] = {}
                if new_address_family not in route_dict['vrf'][vrf]['neighbor']\
                    [neighbor_id]['address_family']:
                    route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                        ['address_family'][new_address_family] = {}

                # Set keys
                route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                    ['address_family'][new_address_family]['bgp_table_version'] = bgp_table_version
                route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                    ['address_family'][new_address_family]['local_router_id'] = local_router_id
                route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                    ['address_family'][new_address_family]['route_distinguisher'] = route_distinguisher
                if m.groupdict()['default_vrf']:
                    route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                        ['address_family'][new_address_family]['default_vrf'] = \
                            str(m.groupdict()['default_vrf'])

                # Reset address_family key and af_dict for use in other regex
                address_family = new_address_family
                af_dict = route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                    ['address_family'][address_family]

                # Init received_routes dict
                if 'received_routes' not in af_dict:
                    af_dict['received_routes'] = {}
                    continue

        return route_dict




class ShowIpbgpTemplatePeerSessionSchema(MetaParser):
    """Schema show ip bgp template peer-session <WORD>"""

    schema = {
                'peer_session':
                    {Any():
                         {
                             Optional('local_policies'): str ,
                             Optional('inherited_polices'): str ,
                             Optional('fall_over_bfd'): bool ,
                             Optional('suppress_four_byte_as_capability'): bool,
                             Optional('description'): str,
                             Optional('disable_connected_check'): bool,
                             Optional('ebgp_multihop_enable'): bool,
                             Optional('ebgp_multihop_max_hop'): int,
                             Optional('local_as_as_no'): int,
                             Optional('password_text'): str,
                             Optional('remote_as'): int,
                             Optional('shutdown'): bool,
                             Optional('keepalive_interval'): int,
                             Optional('holdtime'): int,
                             Optional('transport_connection_mode'): str,
                             Optional('update_source'): str,
                             Optional('index'): int,
                             Optional('inherited_session_commands'):
                                 {
                                     Optional('fall_over_bfd'): bool,
                                     Optional('suppress_four_byte_as_capability'): bool,
                                     Optional('description'): str,
                                     Optional('disable_connected_check'): bool,
                                     Optional('ebgp_multihop_enable'): bool,
                                     Optional('ebgp_multihop_max_hop'): int,
                                     Optional('local_as_as_no'): int,
                                     Optional('password_text'): str,
                                     Optional('remote_as'): int,
                                     Optional('shutdown'): bool,
                                     Optional('keepalive_interval'): int,
                                     Optional('holdtime'): int,
                                     Optional('transport_connection_mode'): str,
                                     Optional('update_source'): str,
                                 }

                         },
                    },
                }

class ShowIpBgpTemplatePeerSession(ShowIpbgpTemplatePeerSessionSchema):
    """Parser for show ip bgp template peer-session <WORD>"""

    def cli(self, template_name=""):
        # show ip bgp template peer-session <WORD>
        cmd = 'show ip bgp template peer-session {template_name}'.format(template_name=template_name)
        out = self.device.execute(cmd)

        # Init vars
        parsed_dict = {}
        for line in out.splitlines():
            if line.strip():
                line = line.rstrip()
            else:
                continue
            # Template:PEER-SESSION, index:1
            p1 = re.compile(r'^\s*Template:+(?P<template_id>[0-9\s\S\w]+),'
                            ' +index:(?P<index>[0-9]+)$')
            m = p1.match(line)
            if m:
                template_id = m.groupdict()['template_id']
                index = int(m.groupdict()['index'])

                if 'peer_session' not in parsed_dict:
                    parsed_dict['peer_session'] = {}

                if template_id not in parsed_dict['peer_session']:
                    parsed_dict['peer_session'][template_id] = {}

                parsed_dict['peer_session'][template_id]['index'] = index
                continue

            # Local policies:0x5025FD, Inherited polices:0x0
            p2 = re.compile(r'^\s*Local +policies:+(?P<local_policies>0x[0-9A-F]+),'
                            ' +Inherited +polices:+(?P<inherited_polices>0x[0-9A-F]+)$')
            m = p2.match(line)
            if m:
                local_policy = m.groupdict()['local_policies']
                inherited_policy = m.groupdict()['inherited_polices']
                parsed_dict['peer_session'][template_id]['local_policies'] = local_policy
                parsed_dict['peer_session'][template_id]['inherited_polices'] = inherited_policy
                continue

            # Locally configured session commands:
            p3 = re.compile(r'^\s*Locally +configured +session +commands:$')
            m = p3.match(line)
            if m:
                flag = False
                continue

            # remote-as 321
            p4 = re.compile(r'^\s*remote-as +(?P<remote_as>[0-9]+)$')
            m = p4.match(line)
            if m:
                remote_as = int(m.groupdict()['remote_as'])
                if flag:
                    parsed_dict['peer_session'][template_id]['inherited_session_commands']['remote_as'] = remote_as
                else:
                    parsed_dict['peer_session'][template_id]['remote_as'] = remote_as
                continue

            # password is configured
            p5 = re.compile(r'^\s*password +(?P<password_text>[\w\s]+)$')
            m = p5.match(line)
            if m:
                password_text = m.groupdict()['password_text']
                if flag:
                    parsed_dict['peer_session'][template_id]['inherited_session_commands']\
                        ['password_text'] = password_text
                else:
                    parsed_dict['peer_session'][template_id]['password_text'] = password_text
                continue

            # shutdown
            p6 = re.compile(r'^\s*shutdown$')
            m = p6.match(line)
            if m:
                if flag:
                    parsed_dict['peer_session'][template_id]['inherited_session_commands'] \
                        ['shutdown'] = True
                else:
                    parsed_dict['peer_session'][template_id]['shutdown'] = True
                continue

            # ebgp-multihop 254
            p7 = re.compile(r'^\s*ebgp-multihop +(?P<ebgp_multihop_max_no>[0-9]+)$')
            m = p7.match(line)
            if m:
                ebgp_multihop_max_no = int(m.groupdict()['ebgp_multihop_max_no'])
                if flag:
                    parsed_dict['peer_session'][template_id]['inherited_session_commands'] \
                        ['ebgp_multihop_max_hop'] = ebgp_multihop_max_no
                    parsed_dict['peer_session'][template_id]['inherited_session_commands'] \
                            ['ebgp_multihop_enable'] = True
                else:
                    parsed_dict['peer_session'][template_id]['ebgp_multihop_max_hop'] = ebgp_multihop_max_no
                    parsed_dict['peer_session'][template_id]['ebgp_multihop_enable'] = True
                continue

            # update-source Loopback0
            p8 = re.compile(r'^\s*update-source +(?P<update_source>[\d\w]+)$')
            m = p8.match(line)
            if m:
                update_source = m.groupdict()['update_source']
                if flag:
                    parsed_dict['peer_session'][template_id]['inherited_session_commands']\
                        ['update_source'] = update_source
                else:
                    parsed_dict['peer_session'][template_id]['update_source'] = update_source
                continue
            # transport connection-mode passive
            p9 = re.compile(r'^\s*transport +connection-mode +(?P<transport_connection_mode>[\s\w]+)$')
            m = p9.match(line)
            if m:
                transport_connection_mode = m.groupdict()['transport_connection_mode']
                if flag:
                    parsed_dict['peer_session'][template_id]['inherited_session_commands'] \
                        ['transport_connection_mode'] = transport_connection_mode
                else:
                    parsed_dict['peer_session'][template_id]['transport_connection_mode'] \
                        = transport_connection_mode
                continue

            # description desc1!
            p10 = re.compile(r'^\s*description +(?P<desc>[\d\S\s\w]+)$')
            m = p10.match(line)
            if m:
                description = m.groupdict()['desc']
                if flag:
                    parsed_dict['peer_session'][template_id]['inherited_session_commands'] \
                        ['description'] = description
                else:
                    parsed_dict['peer_session'][template_id]['description'] \
                        = description
                continue

            # dont-capability-negotiate four-octets-as
            p11 = re.compile(r'^\s*dont-capability-negotiate +four-octets-as$')
            m = p11.match(line)
            if m:
                if flag:
                    parsed_dict['peer_session'][template_id]['inherited_session_commands']\
                        ['suppress_four_byte_as_capability'] = True
                else:
                    parsed_dict['peer_session'][template_id]['suppress_four_byte_as_capability'] \
                        = True
                continue
            # timers 10 30
            p12 = re.compile(r'^\s*timers +(?P<keepalive_interval>[\d]+)'
                             ' +(?P<holdtime>[\d]+)$')
            m = p12.match(line)
            if m:
                keepalive_interval = int(m.groupdict()['keepalive_interval'])
                holdtime = int(m.groupdict()['holdtime'])
                if flag:
                    parsed_dict['peer_session'][template_id]['inherited_session_commands']\
                        ['keepalive_interval'] = keepalive_interval
                    parsed_dict['peer_session'][template_id]['inherited_session_commands']['holdtime'] \
                        = holdtime
                else:
                    parsed_dict['peer_session'][template_id]['keepalive_interval'] \
                        = keepalive_interval
                    parsed_dict['peer_session'][template_id]['holdtime'] \
                        = holdtime
                continue

            # local-as 255
            p13 = re.compile(r'^\s*local-as +(?P<local_as_as_no>[\d]+)$')
            m = p13.match(line)
            if m:
                local_as_as_no = int(m.groupdict()['local_as_as_no'])
                if flag:
                    parsed_dict['peer_session'][template_id]['inherited_session_commands']\
                        ['local_as_as_no'] = local_as_as_no
                else:
                    parsed_dict['peer_session'][template_id]['local_as_as_no'] = local_as_as_no

                continue

            # disable-connected-check
            p14 = re.compile(r'^\s*disable-connected-check$')
            m = p14.match(line)
            if m:
                if flag:
                    parsed_dict['peer_session'][template_id]['inherited_session_commands']\
                        ['disable_connected_check'] = True
                else:
                    parsed_dict['peer_session'][template_id]['disable_connected_check'] = True
                continue

            # fall-over bfd
            p15 = re.compile(r'^\s*fall-over +bfd$')
            m = p15.match(line)
            if m:
                if flag:
                    parsed_dict['peer_session'][template_id]['inherited_session_commands']\
                        ['fall_over_bfd'] = True
                else:
                    parsed_dict['peer_session'][template_id]['fall_over_bfd'] = True
                continue

            # Inherited session commands:
            p16 = re.compile(r'^\s*Inherited +session +commands:$')
            m = p16.match(line)
            if m:
                if 'inherited_session_commands' not in parsed_dict['peer_session'][template_id]:
                    parsed_dict['peer_session'][template_id]['inherited_session_commands'] = {}
                    flag = True
                continue

        if parsed_dict:
            for key, value in  parsed_dict['peer_session'].items():
                if 'inherited_session_commands' in parsed_dict['peer_session'][key]:
                    if not len(parsed_dict['peer_session'][key]['inherited_session_commands']):
                        del parsed_dict['peer_session'][key]['inherited_session_commands']
        return parsed_dict

# ==========================================================
# Parser for 'show bgp all neighbors <WORD> routes'
# ==========================================================

class ShowBgpAllNeighborsRoutesSchema(MetaParser):
    """Schema for show bgp all neighbors <WORD> routes"""

    schema = {
        'vrf':
            {Any():
                {'neighbor':
                    {Any():
                        {'address_family':
                            {Any():
                                {Optional('bgp_table_version'): int,
                                 Optional('local_router_id'): str,
                                 Optional('route_distinguisher'): str,
                                 Optional('default_vrf'): str,
                                 Optional('routes'): 
                                    {Optional(Any()):
                                        {Optional('index'):
                                            {Optional(Any()):
                                                {Optional('next_hop'): str,
                                                 Optional('status_codes'): str,
                                                 Optional('path_type'): str,
                                                 Optional('metric'): int,
                                                 Optional('localprf'): int,
                                                 Optional('weight'): int,
                                                 Optional('path'): str,
                                                 Optional('origin_codes'): str,
                                                },
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


class ShowBgpAllNeighborsRoutes(ShowBgpAllNeighborsRoutesSchema):

    """
    Parser for show bgp all neighbors <WORD> routes
    executing 'show bgp all neighbors | i BGP neighbor' for finding vrf names
    """

    def cli(self, neighbor):
        # find vrf names
        # show bgp all neighbors | i BGP neighbor
        cmd_vrfs = 'show bgp all neighbors | i BGP neighbor'
        out_vrf = self.device.execute(cmd_vrfs)
        vrf = 'default'

        for line in out_vrf.splitlines():
            if not line:
                continue
            else:
                line = line.rstrip()

            # BGP neighbor is 2.2.2.2,  remote AS 100, internal link
            p = re.compile(r'^\s*BGP +neighbor +is +(?P<bgp_neighbor>[0-9A-Z\:\.]+)'
                            '(, +vrf +(?P<vrf>[0-9A-Za-z]+))?, +remote AS '
                            '+(?P<remote_as_id>[0-9]+), '
                            '+(?P<internal_external_link>[a-z\s]+)$')
            m = p.match(line)
            if m:
                # Extract the neighbor corresponding VRF name
                bgp_neighbor = str(m.groupdict()['bgp_neighbor'])
                if bgp_neighbor == neighbor:
                    if m.groupdict()['vrf']:
                        vrf = str(m.groupdict()['vrf'])
                else:
                    continue

        # show bgp all neighbors {neighbor} routes
        cmd  = 'show bgp all neighbors {neighbor} routes'.format(
            neighbor=neighbor)
        out = self.device.execute(cmd)

        # Init dictionary
        route_dict = {}
        af_dict = {}

        # Init vars
        data_on_nextline =  False
        index = 1
        bgp_table_version = local_router_id = ''

        for line in out.splitlines():
            line = line.rstrip()

            # For address family: IPv4 Unicast
            p1 = re.compile(r'^\s*For +address +family:'
                             ' +(?P<address_family>[a-zA-Z0-9\s\-\_]+)$')
            m = p1.match(line)
            if m:
                neighbor_id = str(neighbor)
                address_family = str(m.groupdict()['address_family']).lower()
                original_address_family = address_family
                continue

            # BGP table version is 25, Local Router ID is 21.0.101.1
            p2 = re.compile(r'^\s*BGP +table +version +is'
                             ' +(?P<bgp_table_version>[0-9]+), +[Ll]ocal +[Rr]outer'
                             ' +ID +is +(?P<local_router_id>(\S+))$')
            m = p2.match(line)
            if m:
                bgp_table_version = int(m.groupdict()['bgp_table_version'])
                local_router_id = str(m.groupdict()['local_router_id'])

                # Init dict
                if 'vrf' not in route_dict:
                    route_dict['vrf'] = {}
                if vrf not in route_dict['vrf']:
                    route_dict['vrf'][vrf] = {}
                if 'neighbor' not in route_dict['vrf'][vrf]:
                    route_dict['vrf'][vrf]['neighbor'] = {}
                if neighbor_id not in route_dict['vrf'][vrf]['neighbor']:
                    route_dict['vrf'][vrf]['neighbor'][neighbor_id] = {}
                if 'address_family' not in route_dict['vrf'][vrf]['neighbor']\
                    [neighbor_id]:
                    route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                        ['address_family'] = {}
                if address_family not in route_dict['vrf'][vrf]['neighbor']\
                    [neighbor_id]['address_family']:
                    route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                        ['address_family'][address_family] = {}

                # Set af_dict
                af_dict = route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                    ['address_family'][address_family]

                # Init routes dict
                if 'routes' not in af_dict:
                    af_dict['routes'] = {}

                route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                    ['address_family'][address_family]['bgp_table_version'] = \
                        bgp_table_version
                route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                    ['address_family'][address_family]['local_router_id'] = \
                        local_router_id
                continue

            # Status: s-suppressed, x-deleted, S-stale, d-dampened, h-history, *-valid, >-best
            # Path type: i-internal, e-external, c-confed, l-local, a-aggregate, r-redist, I-injected
            # Origin codes: i - IGP, e - EGP, ? - incomplete, | - multipath, & - backup

            # *>i[2]:[77][7,0][9.9.9.9,1,151587081][29.1.1.1,22][19.0.101.1,29.0.1.30]/616
            # *>iaaaa:1::/113       ::ffff:19.0.101.1
            # *>i  20::/64          ::FFFF:200.0.4.1
            p3_1 = re.compile(r'^\s*(?P<status_codes>(s|x|S|d|h|\*|\>|\s)+)?'
                             '(?P<path_type>(i|e|c|l|a|r|I))? *'
                             '(?P<prefix>[a-zA-Z0-9\.\:\/\[\]\,]+)'
                             '(?: *(?P<next_hop>[a-zA-Z0-9\.\:\/\[\]\,]+))?$')
            m = p3_1.match(line)
            if m:
                # New prefix, reset index count
                index = 1
                data_on_nextline = True

                # Get keys
                if m.groupdict()['status_codes']:
                    status_codes = str(m.groupdict()['status_codes'].rstrip())
                if m.groupdict()['path_type']:
                    path_type = str(m.groupdict()['path_type'])
                if m.groupdict()['prefix']:
                    prefix = str(m.groupdict()['prefix'])

                # Init dict
                if 'routes' not in af_dict:
                    af_dict['routes'] = {}
                if prefix not in af_dict['routes']:
                    af_dict['routes'][prefix] = {}
                if 'index' not in af_dict['routes'][prefix]:
                    af_dict['routes'][prefix]['index'] = {}
                if index not in af_dict['routes'][prefix]['index']:
                    af_dict['routes'][prefix]['index'][index] = {}

                # Set keys
                if m.groupdict()['status_codes']:
                    af_dict['routes'][prefix]['index'][index]['status_codes'] = status_codes
                if m.groupdict()['path_type']:
                    af_dict['routes'][prefix]['index'][index]['path_type'] = path_type
                if m.groupdict()['next_hop']:
                    af_dict['routes'][prefix]['index'][index]['next_hop'] = str(m.groupdict()['next_hop'])
                continue

            # Network            Next Hop            Metric     LocPrf     Weight Path
            # *>i 15.1.2.0/24      1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
            # *>l1.1.1.0/24         0.0.0.0                           100      32768 i
            # *>r1.3.1.0/24         0.0.0.0               4444        100      32768 ?
            # *>r1.3.2.0/24         0.0.0.0               4444        100      32768 ?            
            # *>i  20.0.0.0/24      200.0.4.1                1    100      0 ?
            # *>i1.6.0.0/16         19.0.101.1                        100          0 10 20 30 40 50 60 70 80 90 i
            # *>i1.1.2.0/24         19.0.102.4                        100          0 {62112 33492 4872 41787 13166 50081 21461 58376 29755 1135} i
            # Condition placed to handle the situation of a long line that is
            # divided nto two lines while actually it is not another index.
            if not data_on_nextline:
                p3_2 = re.compile(r'^\s*(?P<status_codes>(s|x|S|d|h|\*|\>|\s)+)'
                                   '(?P<path_type>(i|e|c|l|a|r|I))? *'
                                   '(?P<prefix>(([0-9]+[\.][0-9]+[\.][0-9]+'
                                   '[\.][0-9]+[\/][0-9]+)|([a-zA-Z0-9]+[\:]'
                                   '[a-zA-Z0-9]+[\:][a-zA-Z0-9]+[\:]'
                                   '[a-zA-Z0-9]+[\:][\:][\/][0-9]+)|'
                                   '([a-zA-Z0-9]+[\:][a-zA-Z0-9]+[\:]'
                                   '[a-zA-Z0-9]+[\:][\:][\/][0-9]+)))'
                                   ' +(?P<next_hop>[a-zA-Z0-9\.\:]+)'
                                   ' +(?P<numbers>[a-zA-Z0-9\s\(\)\{\}]+)'
                                   ' +(?P<origin_codes>(i|e|\?|\&|\|))$')
                m = p3_2.match(line)
                if m:
                    # New prefix, reset index count
                    index = 1

                    # Get keys
                    if m.groupdict()['status_codes']:
                        status_codes = str(m.groupdict()['status_codes'].rstrip())
                    if m.groupdict()['path_type']:
                        path_type = str(m.groupdict()['path_type'])
                    if m.groupdict()['prefix']:
                        prefix = str(m.groupdict()['prefix'])
                    if m.groupdict()['next_hop']:
                        next_hop = str(m.groupdict()['next_hop'])
                    if m.groupdict()['origin_codes']:
                        origin_codes = str(m.groupdict()['origin_codes'])

                    # Init dict
                    if 'routes' not in af_dict:
                        af_dict['routes'] = {}
                    if prefix not in af_dict['routes']:
                        af_dict['routes'][prefix] = {}
                    if 'index' not in af_dict['routes'][prefix]:
                        af_dict['routes'][prefix]['index'] = {}
                    if index not in af_dict['routes'][prefix]['index']:
                        af_dict['routes'][prefix]['index'][index] = {}
                    if index not in af_dict['routes'][prefix]['index']:
                        af_dict['routes'][prefix]['index'][index] = {}

                    # Set keys
                    if m.groupdict()['status_codes']:
                        af_dict['routes'][prefix]['index'][index]['status_codes'] = status_codes
                    if m.groupdict()['path_type']:
                        af_dict['routes'][prefix]['index'][index]['path_type'] = path_type
                    if m.groupdict()['next_hop']:
                        af_dict['routes'][prefix]['index'][index]['next_hop'] = next_hop
                    if m.groupdict()['origin_codes']:
                        af_dict['routes'][prefix]['index'][index]['origin_codes'] = origin_codes

                    # Parse numbers
                    numbers = m.groupdict()['numbers']

                    # Metric     LocPrf     Weight Path
                    #    4444       100          0  10 3 10 20 30 40 50 60 70 80 90
                    m1 = re.compile(r'^(?P<metric>[0-9]+)'
                                     '(?P<space1>\s{4,10})'
                                     '(?P<localprf>[0-9]+)'
                                     '(?P<space2>\s{5,10})'
                                     '(?P<weight>[0-9]+)'
                                     '(?: *(?P<path>[0-9\{\}\s]+))?$').match(numbers)

                    #    100        ---          0 10 20 30 40 50 60 70 80 90
                    #    ---        100          0 10 20 30 40 50 60 70 80 90
                    #    100        ---      32788 ---
                    #    ---        100      32788 --- 
                    m2 = re.compile(r'^(?P<value>[0-9]+)'
                                     '(?P<space>\s{2,21})'
                                     '(?P<weight>[0-9]+)'
                                     '(?: *(?P<path>[0-9\{\}\s]+))?$').match(numbers)

                    #    ---        ---      32788 200 33299 51178 47751 {27016}
                    m3 = re.compile(r'^(?P<weight>[0-9]+)'
                                     ' +(?P<path>[0-9\{\}\s]+)$').match(numbers)

                    if m1:
                        af_dict['routes'][prefix]['index'][index]['metric'] = int(m1.groupdict()['metric'])
                        af_dict['routes'][prefix]['index'][index]['localprf'] = int(m1.groupdict()['localprf'])
                        af_dict['routes'][prefix]['index'][index]['weight'] = int(m1.groupdict()['weight'])
                        # Set path
                        if m1.groupdict()['path']:
                            af_dict['routes'][prefix]['index'][index]['path'] = m1.groupdict()['path'].strip()
                            continue
                    elif m2:
                        af_dict['routes'][prefix]['index'][index]['weight'] = int(m2.groupdict()['weight'])
                        # Set metric or localprf
                        if len(m2.groupdict()['space']) > 10:
                            af_dict['routes'][prefix]['index'][index]['metric'] = int(m2.groupdict()['value'])
                        else:
                            af_dict['routes'][prefix]['index'][index]['localprf'] = int(m2.groupdict()['value'])
                        # Set path
                        if m2.groupdict()['path']:
                            af_dict['routes'][prefix]['index'][index]['path'] = m2.groupdict()['path'].strip()
                            continue
                    elif m3:
                        af_dict['routes'][prefix]['index'][index]['weight'] = int(m3.groupdict()['weight'])
                        af_dict['routes'][prefix]['index'][index]['path'] = m3.groupdict()['path'].strip()
                        continue

            #                     0.0.0.0               100      32768 i
            #                     19.0.101.1            4444       100 0 3 10 20 30 40 50 60 70 80 90 i
            #*>i                  1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
            p3_3 = re.compile(r'^\s*(?P<status_codes>(s|x|S|d|h|\*|\>|\s)+)?'
                               '(?P<path_type>(i|e|c|l|a|r|I))?'
                               ' +(?P<next_hop>[a-zA-Z0-9\.\:]+)'
                               '(?: +(?P<numbers>[a-zA-Z0-9\s\(\)\{\}]+))? +'
                               '(?P<origin_codes>(i|e|\?|\|))$')
            m = p3_3.match(line)
            if m:
                # Get keys
                next_hop = str(m.groupdict()['next_hop'])
                origin_codes = str(m.groupdict()['origin_codes'])

                if data_on_nextline:
                    data_on_nextline =  False
                else:
                    index += 1

                # Init dict
                if 'routes' not in af_dict:
                    af_dict['routes'] = {}
                if prefix not in af_dict['routes']:
                    af_dict['routes'][prefix] = {}
                if 'index' not in af_dict['routes'][prefix]:
                    af_dict['routes'][prefix]['index'] = {}
                if index not in af_dict['routes'][prefix]['index']:
                    af_dict['routes'][prefix]['index'][index] = {}

                # Set keys
                af_dict['routes'][prefix]['index'][index]['next_hop'] = next_hop
                af_dict['routes'][prefix]['index'][index]['origin_codes'] = origin_codes
                try:
                    # Set values of status_codes and path_type from prefix line
                    af_dict['routes'][prefix]['index'][index]['status_codes'] = status_codes
                    af_dict['routes'][prefix]['index'][index]['path_type'] = path_type
                except Exception:
                    pass

                # Parse numbers
                numbers = m.groupdict()['numbers']

                # Metric     LocPrf     Weight Path
                #    4444       100          0  10 3 10 20 30 40 50 60 70 80 90
                m1 = re.compile(r'^(?P<metric>[0-9]+)'
                                 '(?P<space1>\s{4,10})'
                                 '(?P<localprf>[0-9]+)'
                                 '(?P<space2>\s{5,10})'
                                 '(?P<weight>[0-9]+)'
                                 '(?: *(?P<path>[0-9\{\}\s]+))?$').match(numbers)

                #    100        ---          0 10 20 30 40 50 60 70 80 90
                #    ---        100          0 10 20 30 40 50 60 70 80 90
                #    100        ---      32788 ---
                #    ---        100      32788 --- 
                m2 = re.compile(r'^(?P<value>[0-9]+)'
                                 '(?P<space>\s{2,21})'
                                 '(?P<weight>[0-9]+)'
                                 '(?: *(?P<path>[0-9\{\}\s]+))?$').match(numbers)

                #    ---        ---      32788 200 33299 51178 47751 {27016}
                m3 = re.compile(r'^(?P<weight>[0-9]+)'
                                 ' +(?P<path>[0-9\{\}\s]+)$').match(numbers)

                if m1:
                    af_dict['routes'][prefix]['index'][index]['metric'] = int(m1.groupdict()['metric'])
                    af_dict['routes'][prefix]['index'][index]['localprf'] = int(m1.groupdict()['localprf'])
                    af_dict['routes'][prefix]['index'][index]['weight'] = int(m1.groupdict()['weight'])
                    # Set path
                    if m1.groupdict()['path']:
                        af_dict['routes'][prefix]['index'][index]['path'] = m1.groupdict()['path'].strip()
                        continue
                elif m2:
                    af_dict['routes'][prefix]['index'][index]['weight'] = int(m2.groupdict()['weight'])
                    # Set metric or localprf
                    if len(m2.groupdict()['space']) > 10:
                        af_dict['routes'][prefix]['index'][index]['metric'] = int(m2.groupdict()['value'])
                    else:
                        af_dict['routes'][prefix]['index'][index]['localprf'] = int(m2.groupdict()['value'])
                    # Set path
                    if m2.groupdict()['path']:
                        af_dict['routes'][prefix]['index'][index]['path'] = m2.groupdict()['path'].strip()
                        continue
                elif m3:
                    af_dict['routes'][prefix]['index'][index]['weight'] = int(m3.groupdict()['weight'])
                    af_dict['routes'][prefix]['index'][index]['path'] = m3.groupdict()['path'].strip()
                    continue

            # Route Distinguisher: 200:1
            # Route Distinguisher: 300:1 (default for vrf VRF1) VRF Router ID 44.44.44.44
            p4 = re.compile(r'^\s*Route +Distinguisher *: '
                             '+(?P<route_distinguisher>(\S+))'
                             '( +\(default for vrf +(?P<default_vrf>(\S+))\))?'
                             '( +VRF Router ID (?P<vrf_router_id>(\S+)))?$')
            m = p4.match(line)
            if m:
                route_distinguisher = str(m.groupdict()['route_distinguisher'])
                new_address_family = original_address_family + ' RD ' + route_distinguisher
                
                # Init dict
                if 'address_family' not in route_dict['vrf'][vrf]['neighbor']\
                        [neighbor_id]:
                    route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                        ['address_family'] = {}
                if new_address_family not in route_dict['vrf'][vrf]['neighbor']\
                    [neighbor_id]['address_family']:
                    route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                        ['address_family'][new_address_family] = {}

                # Set keys
                route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                    ['address_family'][new_address_family]['bgp_table_version'] = bgp_table_version
                route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                    ['address_family'][new_address_family]['local_router_id'] = local_router_id
                route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                    ['address_family'][new_address_family]['route_distinguisher'] = route_distinguisher
                if m.groupdict()['default_vrf']:
                    route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                        ['address_family'][new_address_family]['default_vrf'] = \
                            str(m.groupdict()['default_vrf'])

                # Reset address_family key and af_dict for use in other regex
                address_family = new_address_family
                af_dict = route_dict['vrf'][vrf]['neighbor'][neighbor_id]\
                    ['address_family'][address_family]

                # Init routes dict
                if 'routes' not in af_dict:
                    af_dict['routes'] = {}
                    continue

        return route_dict


class ShowIpbgpTemplatePeerPolicySchema(MetaParser):
    """Schema show ip bgp template peer-policy <WORD>"""
    schema = {
                'peer_policy':
                    {Any():
                         {
                             Optional('local_policies'): str,
                             Optional('inherited_polices'): str,
                             Optional('local_disable_policies'): str,
                             Optional('inherited_disable_polices'): str,
                             Optional('allowas_in'): bool ,
                             Optional('allowas_in_as_number'): int,
                             Optional('as_override'): bool,
                             Optional('default_originate'): bool,
                             Optional('default_originate_route_map'): str,
                             Optional('route_map_name_in'): str,
                             Optional('route_map_name_out'): str,
                             Optional('maximum_prefix_max_prefix_no'): int,
                             Optional('maximum_prefix_threshold'): int,
                             Optional('maximum_prefix_restart'): int,
                             Optional('maximum_prefix_warning_only'): bool,
                             Optional('next_hop_self'): bool,
                             Optional('route_reflector_client'): bool,
                             Optional('send_community'): str,
                             Optional('soft_reconfiguration'): bool,
                             Optional('soo'): str,
                             Optional('index'): int,
                             Optional('inherited_policies'):
                                 {
                                     Optional('allowas_in'): bool,
                                     Optional('allowas_in_as_number'): int,
                                     Optional('as_override'): bool,
                                     Optional('default_originate'): bool,
                                     Optional('default_originate_route_map'): str,
                                     Optional('route_map_name_in'): str,
                                     Optional('route_map_name_out'): str,
                                     Optional('maximum_prefix_max_prefix_no'): int,
                                     Optional('maximum_prefix_threshold'): int,
                                     Optional('maximum_prefix_restart'): int,
                                     Optional('maximum_prefix_warning_only'): bool,
                                     Optional('next_hop_self'): bool,
                                     Optional('route_reflector_client'): bool,
                                     Optional('send_community'): str,
                                     Optional('soft_reconfiguration'): bool,
                                     Optional('soo'): str,
                                 },
                         },
                    },
                }

class ShowIpBgpTemplatePeerPolicy(ShowIpbgpTemplatePeerPolicySchema):
    """Parser for show ip bgp template peer-policy <WORD>"""

    def cli(self, template_name=""):
        # show ip bgp template peer-policy <WORD>
        cmd = 'show ip bgp template peer-policy {template_name}'.format(template_name=template_name)
        out = self.device.execute(cmd)

        # Init vars
        parsed_dict = {}

        for line in out.splitlines():
            if line.strip():
                line = line.rstrip()
            else:
                continue
            # Template:PEER-POLICY, index:1.
            p1 = re.compile(r'^\s*Template:+(?P<template_id>[0-9\s\S\w]+),'
                            ' +index:(?P<index>[0-9]+).$')
            m = p1.match(line)
            if m:
                template_id = m.groupdict()['template_id']
                index = int(m.groupdict()['index'])

                if 'peer_policy' not in parsed_dict:
                    parsed_dict['peer_policy'] = {}

                if template_id not in parsed_dict['peer_policy']:
                    parsed_dict['peer_policy'][template_id] = {}

                parsed_dict['peer_policy'][template_id]['index'] = index
                continue

            # Local policies:0x8002069C603, Inherited polices:0x0
            p2 = re.compile(r'^\s*Local +policies:+(?P<local_policies>0x[0-9A-F]+),'
                            ' +Inherited +polices:+(?P<inherited_polices>0x[0-9A-F]+)$')
            m = p2.match(line)
            if m:
                local_policy = m.groupdict()['local_policies']
                inherited_policy = m.groupdict()['inherited_polices']

                parsed_dict['peer_policy'][template_id]['local_policies'] = local_policy
                parsed_dict['peer_policy'][template_id]['inherited_polices'] = inherited_policy
                continue

            # Local disable policies:0x0, Inherited disable policies:0x0
            p3 = re.compile(r'^\s*Local +disable +policies:+(?P<local_disable_policies>0x[0-9A-F]+),'
                            ' +Inherited +disable +policies:+(?P<inherited_disable_polices>0x[0-9A-F]+)$')
            m = p3.match(line)
            if m:
                local_policy = m.groupdict()['local_disable_policies']
                inherited_policy = m.groupdict()['inherited_disable_polices']
                parsed_dict['peer_policy'][template_id]['local_disable_policies'] = local_policy
                parsed_dict['peer_policy'][template_id]['inherited_disable_polices'] = inherited_policy
                continue

            #Locally configured policies:
            p4 = re.compile(r'^\s*Locally +configured +policies:$')
            m = p4.match(line)
            if m:
                flag = False
                continue

            # route-map test in
            p5 = re.compile(r'^\s*route-map +(?P<remote_map_in>[0-9a-zA-Z]+) +in$')
            m = p5.match(line)
            if m:
                route_map_in = m.groupdict()['remote_map_in']
                if flag:
                    parsed_dict['peer_policy'][template_id]['inherited_policies'] \
                        ['route_map_name_in'] = route_map_in
                else:
                    parsed_dict['peer_policy'][template_id]['route_map_name_in'] = route_map_in
                continue

            # route-map test2 out
            p6 = re.compile(r'^\s*route-map +(?P<route_map_out>[0-9a-zA-Z]+) +out$')
            m = p6.match(line)
            if m:
                route_map_out = m.groupdict()['route_map_out']
                if flag:
                    parsed_dict['peer_policy'][template_id]['inherited_policies']\
                        ['route_map_name_out'] = route_map_out
                else:
                    parsed_dict['peer_policy'][template_id]['route_map_name_out'] = route_map_out
                continue

            # default-originate route-map test
            p7 = re.compile(r'^\s*default-originate +route-map'
                            ' +(?P<default_originate_route_map>[0-9a-zA-Z]+)$')
            m = p7.match(line)
            if m:
                default_originate_route_map = m.groupdict()['default_originate_route_map']
                if flag:
                    parsed_dict['peer_policy'][template_id]['inherited_policies']\
                        ['default_originate'] = True
                    parsed_dict['peer_policy'][template_id]['inherited_policies']\
                        ['default_originate_route_map'] = default_originate_route_map
                else:
                    parsed_dict['peer_policy'][template_id]['default_originate'] = True
                    parsed_dict['peer_policy'][template_id]['default_originate_route_map'] = \
                        default_originate_route_map
                continue

            # soft-reconfiguration inbound
            p8 = re.compile(r'^\s*soft-reconfiguration'
                            ' +(?P<soft_reconfiguration>[a-zA-Z]+)$')
            m = p8.match(line)
            if m:
                default_originate = m.groupdict()['soft_reconfiguration']
                if flag:
                    parsed_dict['peer_policy'][template_id]['inherited_policies']['soft_reconfiguration'] \
                        = True
                else:
                    parsed_dict['peer_policy'][template_id]['soft_reconfiguration'] \
                    = True
                continue

            # maximum-prefix 5555 70 restart 300
            p9 = re.compile(r'^\s*maximum-prefix'
                            ' +(?P<maximum_prefix_max_prefix_no>[0-9]+)'
                            ' ?(?P<maximum_prefix_threshold>[0-9]+)?'
                            ' +restart +(?P<maximum_prefix_restart>[0-9]+)$')
            m = p9.match(line)
            if m:
                maximum_prefix_max_prefix_no = int(m.groupdict()['maximum_prefix_max_prefix_no'])
                maximum_prefix_restart = int(m.groupdict()['maximum_prefix_restart'])
                maximum_prefix_threshold = m.groupdict()['maximum_prefix_threshold']
                if flag:
                    parsed_dict['peer_policy'][template_id]['inherited_policies']['maximum_prefix_max_prefix_no'] \
                        = maximum_prefix_max_prefix_no
                    if maximum_prefix_threshold:
                        parsed_dict['peer_policy'][template_id]['inherited_policies']['maximum_prefix_threshold'] \
                            = int(maximum_prefix_threshold)

                    parsed_dict['peer_policy'][template_id]['inherited_policies']['maximum_prefix_restart'] \
                        = maximum_prefix_restart
                else:
                    parsed_dict['peer_policy'][template_id]['maximum_prefix_max_prefix_no'] \
                        = maximum_prefix_max_prefix_no
                    if maximum_prefix_threshold:
                        parsed_dict['peer_policy'][template_id]['maximum_prefix_threshold'] \
                            = int(maximum_prefix_threshold)

                    parsed_dict['peer_policy'][template_id]['maximum_prefix_restart'] \
                        = maximum_prefix_restart
                continue

            # as-override
            p10 = re.compile(r'^\s*as-override$')
            m = p10.match(line)
            if m:
                if flag:
                    parsed_dict['peer_policy'][template_id]['inherited_policies']['as_override'] = True
                else:
                    parsed_dict['peer_policy'][template_id]['as_override'] = True
                continue

            # allowas-in 9
            p11 = re.compile(r'^\s*allowas-in +(?P<allowas_in_as_number>[0-9]+)$')
            m = p11.match(line)
            if m:
                if flag:
                    parsed_dict['peer_policy'][template_id]['inherited_policies']['allowas_in'] = True
                    parsed_dict['peer_policy'][template_id]['inherited_policies']['allowas_in_as_number'] = \
                         int(m.groupdict()['allowas_in_as_number'])
                else:
                    parsed_dict['peer_policy'][template_id]['allowas_in'] = True
                    parsed_dict['peer_policy'][template_id]['allowas_in_as_number'] = \
                        int(m.groupdict()['allowas_in_as_number'])
                continue

            # route-reflector-client
            p12 = re.compile(r'^\s*route-reflector-client$')
            m = p12.match(line)
            if m:
                if flag:
                    parsed_dict['peer_policy'][template_id]['inherited_policies']\
                        ['route_reflector_client'] = True
                else:
                    parsed_dict['peer_policy'][template_id]['route_reflector_client'] = True
                continue

            # next-hop-self
            p13 = re.compile(r'^\s*next-hop-self$')
            m = p13.match(line)
            if m:
                if flag:
                    parsed_dict['peer_policy'][template_id]['inherited_policies']['next_hop_self'] = True
                else:
                    parsed_dict['peer_policy'][template_id]['next_hop_self'] = True
                continue

            # send-community both
            p14 = re.compile(r'^\s*send-community +(?P<send_community>[\w]+)$')
            m = p14.match(line)
            if m:
                send_community = m.groupdict()['send_community']
                if flag:
                    parsed_dict['peer_policy'][template_id]['inherited_policies']\
                        ['send_community'] = send_community
                else:
                    parsed_dict['peer_policy'][template_id]['send_community'] = send_community
                continue

            # soo SoO:100:100
            p15 = re.compile(r'^\s*soo +(?P<soo>[\w\:\d]+)$')
            m = p15.match(line)
            if m:
                soo = m.groupdict()['soo']
                if flag:
                    parsed_dict['peer_policy'][template_id]['inherited_policies']['soo'] = soo
                else:
                    parsed_dict['peer_policy'][template_id]['soo'] = soo
                continue
            # Inherited policies:
            p15 = re.compile(r'^\s*Inherited policies:$')
            m = p15.match(line)
            if m:
                if 'inherited_policies' not in parsed_dict['peer_policy'][template_id]:
                    parsed_dict['peer_policy'][template_id]['inherited_policies'] = {}
                    flag = True

                continue

        if parsed_dict:
            for key, value in parsed_dict['peer_policy'].items():
                if 'inherited_policies' in parsed_dict['peer_policy'][key]:
                    if not len(parsed_dict['peer_policy'][key]['inherited_policies']):
                        del parsed_dict['peer_policy'][key]['inherited_policies']

        return parsed_dict


class ShowIpBgpAllDampeningParametersSchema(MetaParser):
    """Schema for show ip bgp all dampening parameters"""
    schema = {
        'vrf':
            {Any():
                 {
                 Optional('address_family'):
                      {Any():
                          {
                              Optional('dampening'): bool,
                              Optional('dampening_decay_time'): int,
                              Optional('dampening_half_life_time'): int,
                              Optional('dampening_reuse_time'): int,
                              Optional('dampening_max_suppress_penalty'): int,
                              Optional('dampening_suppress_time'): int,
                              Optional('dampening_max_suppress_time'): int,
                          },
                      },
                 },
             },
    }

class ShowIpBgpAllDampeningParameters(ShowIpBgpAllDampeningParametersSchema):
    """Parser for show ip bgp all dampening parameters"""

    def cli(self):

        cmd = 'show ip bgp all dampening parameters'
        out = self.device.execute(cmd)

        # Init vars
        parsed_dict = {}
        vrf_name = 'default'

        for line in out.splitlines():
            if line.strip():
                line = line.rstrip()
            else:
                continue

            # For address family: IPv4 Unicast
            p1 = re.compile(r'^\s*For +address +family:'
                            ' +(?P<address_family>[a-zA-Z0-9\-\s]+)$')
            m = p1.match(line)
            if m:
                af_name = m.groupdict()['address_family'].lower()
                if 'vrf' not in parsed_dict:
                    parsed_dict['vrf'] = {}
                if vrf_name not in parsed_dict['vrf']:
                    parsed_dict['vrf'][vrf_name] = {}
                if 'address_family' not in parsed_dict['vrf'][vrf_name]:
                    parsed_dict['vrf'][vrf_name]['address_family'] = {}
                if af_name not in parsed_dict['vrf'][vrf_name]['address_family']:
                    parsed_dict['vrf'][vrf_name]['address_family'][af_name] = {}
                continue

            # dampening 35 200 200 70
            p2 = re.compile(r'^\s*dampening'
                            ' +(?P<dampening_val>[\d\s\S]+)$')
            m = p2.match(line)
            if m:
                dampening_val = m.groupdict()['dampening_val']
                if vrf_name not in parsed_dict['vrf']:
                    parsed_dict['vrf'][vrf_name] = {}
                if 'address_family' not in parsed_dict['vrf'][vrf_name]:
                    parsed_dict['vrf'][vrf_name]['address_family'] = {}
                if af_name not in parsed_dict['vrf'][vrf_name]['address_family']:
                    parsed_dict['vrf'][vrf_name]['address_family'][af_name] = {}

                parsed_dict['vrf'][vrf_name]['address_family'][af_name]['dampening'] = True
                continue

            # Half-life time      : 35 mins       Decay Time       : 4200 secs
            p3 = re.compile(r'^\s*Half-life +time\s*:'
                            ' +(?P<half_life_time>[\d]+)'
                            ' mins +Decay +Time +: +(?P<decay_time>[\d]+) +secs$')
            m = p3.match(line)
            if m:
                half_life_time = int(m.groupdict()['half_life_time'])*60
                decay_time = int(m.groupdict()['decay_time'])
                parsed_dict['vrf'][vrf_name]['address_family'][af_name]\
                    ['dampening_half_life_time'] = half_life_time
                parsed_dict['vrf'][vrf_name]['address_family'][af_name] \
                    ['dampening_decay_time'] = decay_time
                continue

            # Max suppress penalty:   800         Max suppress time: 70 mins
            p4 = re.compile(r'^\s*Max +suppress +penalty:'
                            '\s+(?P<max_suppress_penalty>[0-9]+)'
                            '\s+Max +suppress +time:\s+(?P<max_suppress_time>[\d]+) +mins$')
            m = p4.match(line)
            if m:
                max_suppress_penalty = int(m.groupdict()['max_suppress_penalty'])
                max_suppress_time = int(m.groupdict()['max_suppress_time'])*60
                parsed_dict['vrf'][vrf_name]['address_family'][af_name] \
                    ['dampening_max_suppress_penalty'] = max_suppress_penalty
                parsed_dict['vrf'][vrf_name]['address_family'][af_name] \
                    ['dampening_max_suppress_time'] = max_suppress_time
                continue

            # Suppress penalty :   200         Reuse penalty : 200
            p5 = re.compile(r'^\s*Suppress +penalty +:'
                            ' +(?P<suppress_penalty>[\d]+)'
                            ' +Reuse +penalty +: +(?P<reuse_penalty>[\d]+)$')
            m = p5.match(line)
            if m:
                suppress_penalty = int(m.groupdict()['suppress_penalty'])
                reuse_time = int(m.groupdict()['reuse_penalty'])
                parsed_dict['vrf'][vrf_name]['address_family'][af_name] \
                    ['dampening_suppress_time'] = suppress_penalty
                parsed_dict['vrf'][vrf_name]['address_family'][af_name]\
                    ['dampening_reuse_time'] = reuse_time
                continue

            # % dampening not enabled for base
            p6 = re.compile(r'^\s*% +dampening +not +enabled +for +base$')
            m = p6.match(line)
            if m:
                continue

            # For vrf: VRF1
            p7 = re.compile(r'^\s*For +vrf: +(?P<vrf_name>[\w\d]+)$')
            m = p7.match(line)
            if m:
                vrf_name = m.groupdict()['vrf_name']
                if 'vrf' not in parsed_dict:
                    parsed_dict['vrf'] = {}
                if vrf_name not in parsed_dict['vrf']:
                    parsed_dict['vrf'][vrf_name] = {}
                continue

            # % dampening not enabled for vrf VRF1
            p8 = re.compile(r'^\s*% +dampening +not +enabled +for +vrf +(?P<vrf_name>[\d\w]+)$')
            m = p8.match(line)
            if m:
                continue

        if parsed_dict:
            for vrf_name in parsed_dict['vrf'].keys():
                if 'address_family' in parsed_dict['vrf'][vrf_name]:
                    for i in parsed_dict['vrf'][vrf_name]['address_family'].copy():
                        if not parsed_dict['vrf'][vrf_name]['address_family'][i]:
                            parsed_dict['vrf'][vrf_name]['address_family'].pop(i)

            for vrf_name in parsed_dict['vrf'].keys():
                for i in parsed_dict['vrf'][vrf_name].copy():
                    if not parsed_dict['vrf'][vrf_name][i]:
                        parsed_dict['vrf'][vrf_name].pop(i)

            for i in parsed_dict['vrf'].copy():
                if not parsed_dict['vrf'][i]:
                    parsed_dict['vrf'].pop(i)

            for i in parsed_dict.copy():
                if not parsed_dict[i]:
                    parsed_dict.pop(i)

        return parsed_dict


class ShowBgpAllSchema(MetaParser):
        """Schema for show bgp all"""

        schema = {
            'vrf':
                {Any():
                     {'address_family':
                          {Any():
                               {Optional('bgp_table_version'): int,
                                Optional('route_identifier'): str,
                                Optional('vrf_route_identifier'): str,
                                Optional('route_distinguisher'): str,
                                Optional('default_vrf'): str,
                                Optional('af_private_import_to_address_family'): str,
                                Optional('pfx_count'): int,
                                Optional('pfx_limit'): int,
                                Optional('routes'):
                                    {Optional(Any()):
                                         {Optional('index'):
                                              {Optional(Any()):
                                                   {Optional('next_hop'): str,
                                                    Optional('status_codes'): str,
                                                    Optional('metric'): int,
                                                    Optional('localpref'): int,
                                                    Optional('weight'): int,
                                                    Optional('path'): str,
                                                    Optional('origin_codes'): str,
                                                    },
                                               },
                                          },
                                     },
                                },
                           },
                      },
                 },
        }

class ShowBgpAll(ShowBgpAllSchema):
    """Parser for show bgp all"""

    def cli(self):
        # show bgp all
        cmd = 'show bgp all'
        out = self.device.execute(cmd)

        # Init dictionary
        route_dict = {}
        af_dict = {}
        vrf = 'default'

        # Init vars
        index = 1
        bgp_table_version = local_router_id = ''
        metric = localpref = weight = ''
        status_codes = ''
        prefix = ""
        origin_codes_info = origin_codes_data = ""

        for line in out.splitlines():
            line = line.rstrip()

            # For address family: IPv4 Unicast
            p1 = re.compile(r'^\s*For +address +family:'
                            ' +(?P<address_family>[a-zA-Z0-9\s\-\_]+)$')
            m = p1.match(line)
            if m:
                address_family = str(m.groupdict()['address_family']).lower()
                original_address_family = address_family
                continue

            # BGP table version is 25, Local Router ID is 21.0.101.1
            p2 = re.compile(r'^\s*BGP +table +version +is'
                            ' +(?P<bgp_table_version>[0-9]+), +[Ll]ocal +[Rr]outer'
                            ' +ID +is +(?P<local_router_id>(\S+))$')
            m = p2.match(line)
            if m:
                bgp_table_version = int(m.groupdict()['bgp_table_version'])
                local_router_id = str(m.groupdict()['local_router_id'])
                continue

            #     Network          Next Hop            Metric LocPrf Weight Path
            # *>   [5][65535:1][0][24][100.1.1.0]/17
            p3_1 = re.compile(r'^\s*(?P<status_codes>(s|x|S|d|h|\*|\>|\s)+)?'
                              '(?P<path_type>(i|e|c|l|a|r|I))?'
                              '(?P<prefix>[a-zA-Z0-9\.\:\/\[\]\,]+)'
                              '(?: *(?P<param>[a-zA-Z0-9\.\:\/\[\]\,]+))?$')
            m = p3_1.match(line)
            if m:
                # Get keys
                if m.groupdict()['status_codes']:
                    status_codes = m.groupdict()['status_codes']
                path_type = ''
                if m.groupdict()['path_type']:
                    path_type = str(m.groupdict()['path_type'])
                if path_type:
                    status_codes = status_codes + path_type
                else:
                    status_codes = status_codes.rstrip()

                if m.groupdict()['prefix']:
                    prefix = str(m.groupdict()['prefix'])
                index = 0

            #     Network          Next Hop            Metric LocPrf Weight Path
            # * i                  1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
            #                      0.0.0.0                  0         32768 ?
            # *>                    0.0.0.0                  0         32768 ?
            # * i                  ::FFFF:1.1.1.1        2219    100      0 200 33299 51178 47751 {27016} e
            p3_2 = re.compile(r'^\s*(?P<status_codes>(s|x|S|d|h|\*|\>|\s)+)?'
                              '(?P<path_type>(i|e|c|l|a|r|I))?'
                              ' +(?P<next_hop>[a-zA-Z0-9\.\:]+)'
                              ' +(?P<metric>[0-9]+)?'
                                '(?P<space>\s{1,4})'
                              ' +(?P<local_prf>[0-9]+)?'
                                '(?P<space1>\s{1,6})'
                              ' +(?P<weight>[0-9]+)'
                              '(?P<termination>[\s\S]+)$')

            m = p3_2.match(line)
            if m:
                # Get keys
                path_type = ""
                path_info = ""
                if m.groupdict()['status_codes']:
                    status_codes = m.groupdict()['status_codes']
                if m.groupdict()['path_type']:
                    path_type = m.groupdict()['path_type']

                if m.groupdict()['next_hop']:
                    next_hop = m.groupdict()['next_hop']

                if path_type:
                    status_codes = status_codes + path_type
                else:
                    status_codes = status_codes.rstrip()

                if m.groupdict()['termination']:
                    termination = m.groupdict()['termination']
                    m3 = re.compile(r'(?: *(?P<path>[0-9\{\}\s]+))?'
                                    ' +(?P<origin_codes>(i|e|\?|\|))$').match(termination)
                    if m3 and m3.groupdict()['path']:
                        path_info = m3.groupdict()['path']
                    if m3 and m3.groupdict()['origin_codes']:
                        origin_codes_info = m3.groupdict()['origin_codes']

                if m.groupdict()['metric']:
                    metric = int(m.groupdict()['metric'])
                if m.groupdict()['weight']:
                    weight = int(m.groupdict()['weight'])
                if m.groupdict()['local_prf']:
                    localpref = int(m.groupdict()['local_prf'])

                index += 1
                # Init dict
                if 'vrf' not in route_dict:
                    route_dict['vrf'] = {}
                if vrf not in route_dict['vrf']:
                    route_dict['vrf'][vrf] = {}
                if 'address_family' not in route_dict['vrf'][vrf]:
                    route_dict['vrf'][vrf]['address_family'] = {}

                if address_family not in route_dict['vrf'][vrf]['address_family']:
                    route_dict['vrf'][vrf]['address_family'][address_family] = {}

                # Set af_dict
                af_dict = route_dict['vrf'][vrf]['address_family'][address_family]

                if 'routes' not in af_dict:
                    af_dict['routes'] = {}
                if prefix not in af_dict['routes']:
                    af_dict['routes'][prefix] = {}
                if 'index' not in af_dict['routes'][prefix]:
                    af_dict['routes'][prefix]['index'] = {}
                if index not in af_dict['routes'][prefix]['index']:
                    af_dict['routes'][prefix]['index'][index] = {}
                if index not in af_dict['routes'][prefix]['index']:
                    af_dict['routes'][prefix]['index'][index] = {}

                # Set keys
                if status_codes:
                    af_dict['routes'][prefix]['index'][index]['status_codes'] = status_codes

                if m.groupdict()['next_hop']:
                    af_dict['routes'][prefix]['index'][index]['next_hop'] = next_hop
                if m.groupdict()['local_prf']:
                    af_dict['routes'][prefix]['index'][index]['localpref'] = localpref
                if m.groupdict()['weight']:
                    af_dict['routes'][prefix]['index'][index]['weight'] = weight
                if m.groupdict()['metric']:
                    af_dict['routes'][prefix]['index'][index]['metric'] = metric

                if path_info:
                     af_dict['routes'][prefix]['index'][index]['path'] = path_info
                if origin_codes_info:
                    af_dict['routes'][prefix]['index'][index]['origin_codes'] = origin_codes_info

                continue

            # Network            Next Hop            Metric     LocPrf     Weight Path
            # *    3.3.3.0/24       3.3.3.254                0             0 65530 ?
            # *>   100.1.1.0/24     0.0.0.0                  0         32768 ?
            # *>i 15.1.2.0/24      1.1.1.1               2219    100      0 200 33299 51178 47751 {27016} e
            # *>i 615:11:11::/64   ::FFFF:1.1.1.1        2219    100      0 200 33299 51178 47751 {27016} e

            p4 = re.compile(r'^\s*(?P<status_codes>(s|x|S|d|h|\*|\>|\s)+)?'
                            '(?P<path_type>(i|e|c|l|a|r|I))?'
                            ' +(?P<prefix>[0-9\.\:\/]+)'
                            ' +(?P<next_hop>[a-zA-Z0-9\.\:]+)'
                            '(?P<space1>\s{5,18})'
                            '(?P<metric>[0-9]+)?'
                            '(?P<space2>\s{4,8}?)'
                            '(?P<local_prf>[0-9]+)?'
                            '(?P<space3>\s{1,12})'
                            '(?P<weight>[0-9]+)'
                            '(?P<path>[0-9\s\S\{\}]+)$')
            m = p4.match(line)
            if m:
                path_type = ""
                path_data = ""
                if m.groupdict()['prefix']:
                    prefix = m.groupdict()['prefix']
                    index = 1

                # Get keys
                if m.groupdict()['status_codes']:
                    status_codes = m.groupdict()['status_codes']
                if m.groupdict()['path_type']:
                    path_type = m.groupdict()['path_type']

                if path_type:
                    status_codes = status_codes + path_type
                else:
                    status_codes = status_codes.rstrip()

                if m.groupdict()['path']:
                    path_1 = m.groupdict()['path']
                    m3 = re.compile(r'(?: *(?P<path_inner>[0-9\{\}\s]+))?'
                                    ' +(?P<origin_codes_inner>(i|e|\?|\|))$').match(path_1)
                    if m3:
                        path_data = m3.groupdict()['path_inner']
                        origin_codes_data = m3.groupdict()['origin_codes_inner']
                if m.groupdict()['next_hop']:
                    next_hop = m.groupdict()['next_hop']

                if m.groupdict()['metric']:
                    metric = int(m.groupdict()['metric'])
                if m.groupdict()['weight']:
                    weight = int(m.groupdict()['weight'])
                if m.groupdict()['local_prf']:
                    localpref = int(m.groupdict()['local_prf'])

                # Init dict
                if 'vrf' not in route_dict:
                    route_dict['vrf'] = {}
                if vrf not in route_dict['vrf']:
                    route_dict['vrf'][vrf] = {}
                if 'address_family' not in route_dict['vrf'][vrf]:
                    route_dict['vrf'][vrf]['address_family'] = {}

                if address_family not in route_dict['vrf'][vrf]['address_family']:
                    route_dict['vrf'][vrf]['address_family'][address_family] = {}

                # Set af_dict
                af_dict = route_dict['vrf'][vrf]['address_family'][address_family]
                if 'routes' not in af_dict:
                    af_dict['routes'] = {}
                if prefix not in af_dict['routes']:
                    af_dict['routes'][prefix] = {}
                if 'index' not in af_dict['routes'][prefix]:
                    af_dict['routes'][prefix]['index'] = {}
                if index not in af_dict['routes'][prefix]['index']:
                    af_dict['routes'][prefix]['index'][index] = {}
                if index not in af_dict['routes'][prefix]['index']:
                    af_dict['routes'][prefix]['index'][index] = {}

                # Set keys
                if status_codes:
                    af_dict['routes'][prefix]['index'][index]['status_codes'] = status_codes
                if path_data:
                    af_dict['routes'][prefix]['index'][index]['path'] = path_data
                if m.groupdict()['next_hop']:
                    af_dict['routes'][prefix]['index'][index]['next_hop'] = next_hop
                if m.groupdict()['local_prf']:
                    af_dict['routes'][prefix]['index'][index]['localpref'] = localpref
                if m.groupdict()['weight']:
                    af_dict['routes'][prefix]['index'][index]['weight'] = weight
                if m.groupdict()['metric']:
                    af_dict['routes'][prefix]['index'][index]['metric'] = metric
                if origin_codes_data:
                    af_dict['routes'][prefix]['index'][index]['origin_codes'] = origin_codes_data
                continue

            # AF-Private Import to Address-Family: L2VPN E-VPN, Pfx Count/Limit: 2/1000
            p5 = re.compile(r'^\s*AF-Private +Import +to +Address-Family:'
                            ' +(?P<af_private_import_to_address_family>[\s\S]+),'
                            ' +Pfx +Count/Limit:'
                            ' +(?P<pfx_count>[\d]+)\/+(?P<pfx_limit>[\d]+)$')
            m = p5.match(line)
            if m:
                af_private_import_to_address_family = m.groupdict()['af_private_import_to_address_family']
                pfx_count = int(m.groupdict()['pfx_count'])
                pfx_limit = int(m.groupdict()['pfx_limit'])

                if 'vrf' not in route_dict:
                    route_dict['vrf'] = {}
                if vrf not in route_dict['vrf']:
                    route_dict['vrf'][vrf] = {}

                if 'address_family' not in route_dict['vrf'][vrf]:
                    route_dict['vrf'][vrf]['address_family'] = {}
                if new_address_family not in route_dict['vrf'][vrf]['address_family']:
                    route_dict['vrf'][vrf]['address_family'][new_address_family] = {}

                route_dict['vrf'][vrf]['address_family'][new_address_family] \
                    ['af_private_import_to_address_family'] = af_private_import_to_address_family

                route_dict['vrf'][vrf]['address_family'][new_address_family] \
                    ['pfx_count'] = pfx_count

                route_dict['vrf'][vrf]['address_family'][new_address_family] \
                        ['pfx_limit'] = pfx_limit

                continue
            # Route Distinguisher: 200:1
            # Route Distinguisher: 300:1 (default for vrf VRF1) VRF Router ID 44.44.44.44
            p6 = re.compile(r'^\s*Route +Distinguisher *: '
                            '+(?P<route_distinguisher>(\S+))'
                            '( +\(default for vrf +(?P<default_vrf>(\S+))\))?'
                            '( +VRF Router ID (?P<vrf_router_id>(\S+)))?$')
            m = p6.match(line)
            if m:
                route_distinguisher = str(m.groupdict()['route_distinguisher'])
                new_address_family = original_address_family + ' RD ' + route_distinguisher

                # Init dict
                if m.groupdict()['default_vrf']:
                    vrf = m.groupdict()['default_vrf']

                if 'vrf' not in route_dict:
                    route_dict['vrf'] = {}
                if vrf not in route_dict['vrf']:
                    route_dict['vrf'][vrf] = {}

                if 'address_family' not in route_dict['vrf'][vrf]:
                    route_dict['vrf'][vrf]['address_family'] = {}
                if new_address_family not in route_dict['vrf'][vrf]['address_family']:
                    route_dict['vrf'][vrf]['address_family'][new_address_family] = {}

                # Set keys
                route_dict['vrf'][vrf]['address_family'][new_address_family]\
                    ['bgp_table_version'] = bgp_table_version
                route_dict['vrf'][vrf]['address_family'][new_address_family]\
                    ['route_identifier'] = local_router_id
                route_dict['vrf'][vrf]['address_family'][new_address_family]\
                    ['route_distinguisher'] = route_distinguisher

                if vrf:
                    route_dict['vrf'][vrf]['address_family'][new_address_family]['default_vrf'] = \
                    vrf

                if m.groupdict()['vrf_router_id']:
                    route_dict['vrf'][vrf]['address_family'][new_address_family]['vrf_route_identifier'] = \
                        str(m.groupdict()['vrf_router_id'])


                # Reset address_family key and af_dict for use in other regex
                address_family = new_address_family
                af_dict = route_dict['vrf'][vrf]['address_family'][address_family]

                # Init routes dict
                if 'routes' not in af_dict:
                    del af_dict
                    continue

        return route_dict
