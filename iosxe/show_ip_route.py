''' show_ip_route.py

IOSXE parsers for the following show commands:
    * 'show ip route bgp'
    * 'show ip route vrf <WORD> bgp'
    * 'show ipv6 route bgp'
    * 'show ipv6 route vrf <WORD> bgp'
'''
import re   
from metaparser import MetaParser   
from metaparser.util.schemaengine import Any, Optional 


class ShowIPRouteSchema(MetaParser):

    ''' Schema for:
        # 'show ip route bgp'
        # 'show ip route vrf <WORD> bgp'
        # 'show ipv6 route bgp'
        # 'show ipv6 route vrf <WORD> bgp'
    '''

    schema = {
        'vrf':
            {Any():
                {Optional('address_family'):
                    {Any():
                        {Optional('bgp_distance'): int,
                         'ip':
                            {Any():
                                {Optional('nexthop'):
                                    {Optional(Any()):
                                        {Optional('protocol'):
                                            {Optional(Any()):
                                                {Optional('route_table'): str,
                                                Optional('uptime'): str,
                                                Optional('preference'): str,
                                                Optional('metric'): str,
                                                Optional('attribute'): str,
                                                }
                                            },
                                        }
                                    },
                                }
                            },
                        }
                    },
                }
            },
        }


class ShowIpRoute(ShowIPRouteSchema):

    def cli(self, vrf='', ip=''):

        # Calling the corresponding show command
        if ip:
            if vrf:
                cmd = 'show {ip} route vrf {vrf} bgp'.format(ip=ip, vrf=vrf)
            else:
                vrf = 'default'
                cmd = 'show {ip} route bgp'.format(ip=ip)
        else:
            if vrf:
                cmd = 'show ip route vrf {vrf} bgp'.format(vrf=vrf)
            else:
                vrf = 'default'
                cmd = 'show route bgp'

        out = self.device.execute(cmd)

        # Init dict
        bgp_dict = {}
        sub_dict = {}
        address_family = None
        preference = None
        metric = None

        # Setting the address_family
        if vrf == 'default' and not ip:
            address_family = 'ipv4 unicast'
        elif vrf != 'default' and not ip:
            address_family = 'vpnv4 unicast'
        elif vrf == 'default' and ip:
            address_family = 'ipv6 unicast'
        elif vrf != 'default' and ip:
            address_family = 'vpnv6 unicast'

        for line in out.splitlines():
            line = line.strip()

            # B   646:11:11:1::/64 [20/2219]
            # B   646:22:22::/64 [20/2219]
            # B   615:11:11::/64 [200/2219]
            # B   2001:2:2:2::2/128 [200/0]
            # B        15.1.1.0 [200/2219] via 1.1.1.1, 01:40:40
            # B        46.2.2.0 [20/2219] via 20.4.6.6 (VRF2), 01:36:26
            p1 = re.compile(r'^\s*(?P<protocol>[a-zA-Z0-9\+\%]+)'
                             ' +(?P<ip_add>[0-9\.\:\/]+)'
                             ' +(\[(?P<preference>[0-9]+)/(?P<metric>[0-9]+)\])'
                             '( +via +(?P<next_hop>[0-9\.]+)(\s)?(\()?'
                             '(?P<table>[a-zA-Z0-9]+)?(\)?),'
                             ' +(?P<up_time>[0-9\:]+))?$')
            m = p1.match(line)
            if m:
                protocol = str(m.groupdict()['protocol'])
                if protocol == 'B':
                    protocol = 'bgp'
                ip_add = str(m.groupdict()['ip_add'])
                preference = m.groupdict()['preference']
                metric = m.groupdict()['metric']

                # Init vrf dict
                if 'vrf' not in bgp_dict:
                    bgp_dict['vrf'] = {}
                if vrf and vrf not in bgp_dict['vrf']:
                    bgp_dict['vrf'][vrf] = {}

                # Init address_family dict
                if 'address_family' not in bgp_dict['vrf'][vrf]:
                    bgp_dict['vrf'][vrf]['address_family'] = {}
                if address_family is not None and \
                   address_family not in bgp_dict['vrf'][vrf]['address_family']:
                   bgp_dict['vrf'][vrf]['address_family'][address_family] = {}

                # Create sub_dict
                sub_dict = bgp_dict['vrf'][vrf]['address_family'][address_family]

                # Init address_family dict
                if 'ip' not in sub_dict:
                    sub_dict['ip'] = {}
                if ip_add not in sub_dict['ip']:
                    sub_dict['ip'][ip_add] = {}
                if m.groupdict()['next_hop']:
                    next_hop = str(m.groupdict()['next_hop'])
                    if 'nexthop' not in sub_dict['ip'][ip_add]:
                        sub_dict['ip'][ip_add]['nexthop'] = {}
                    if next_hop not in sub_dict['ip'][ip_add]['nexthop']:
                        sub_dict['ip'][ip_add]['nexthop'][next_hop] = {}
                    if 'protocol' not in sub_dict['ip'][ip_add]['nexthop'][next_hop]:
                        sub_dict['ip'][ip_add]['nexthop'][next_hop]['protocol'] = {}
                    if protocol not in sub_dict['ip'][ip_add]['nexthop'][next_hop]['protocol']:
                        sub_dict['ip'][ip_add]['nexthop'][next_hop]['protocol'][protocol] = {}

                    # Create sub_dict
                    prot_dict = sub_dict['ip'][ip_add]['nexthop'][next_hop]['protocol']
                    if m.groupdict()['table']:
                        table = m.groupdict()['table']
                        prot_dict[protocol]['route_table'] = table

                    prot_dict[protocol]['preference'] = preference
                    if protocol == 'bgp':
                        sub_dict['bgp_distance'] = int(preference)

                    metric = m.groupdict()['metric']
                    prot_dict[protocol]['metric'] = metric

                    if m.groupdict()['up_time']:
                        up_time = m.groupdict()['up_time']
                        prot_dict[protocol]['uptime'] = up_time

                continue

            #      via 2001:DB8:1:1::2
            #      via 1.1.1.1%default, indirectly connected
            #      via 2001:DB8:4:6::6
            #      via 2001:DB8:20:4:6::6%VRF2
            p2 = re.compile(r'^\s*via +(?P<next_hop>[a-zA-Z0-9\.\/\:]+)'
                             '(\%(?P<table>[a-zA-Z0-9]+))?'
                             '(,)?(\s+)?(?P<attribute>[a-zA-Z\s]+)?$')
            m = p2.match(line)
            if m:
                next_hop = str(m.groupdict()['next_hop'])
                if 'nexthop' not in sub_dict['ip'][ip_add]:
                    sub_dict['ip'][ip_add]['nexthop'] = {}
                if next_hop not in sub_dict['ip'][ip_add]['nexthop']:
                    sub_dict['ip'][ip_add]['nexthop'][next_hop] = {}
                if 'protocol' not in sub_dict['ip'][ip_add]['nexthop'][next_hop]:
                    sub_dict['ip'][ip_add]['nexthop'][next_hop]['protocol'] = {}
                if protocol not in sub_dict['ip'][ip_add]['nexthop'][next_hop]['protocol']:
                    sub_dict['ip'][ip_add]['nexthop'][next_hop]['protocol'][protocol] = {}

                # Create sub_dict
                prot_dict = sub_dict['ip'][ip_add]['nexthop'][next_hop]['protocol']

                if m.groupdict()['table']:
                    table = m.groupdict()['table']
                    prot_dict[protocol]['route_table'] = table

                if m.groupdict()['attribute']:
                    attribute = m.groupdict()['attribute']
                    prot_dict[protocol]['attribute'] = attribute

                if preference:
                    prot_dict[protocol]['preference'] = preference
                    if protocol == 'bgp':
                        sub_dict['bgp_distance'] = int(preference)

                if metric:
                    prot_dict[protocol]['metric'] = metric

        return bgp_dict


class ShowIpv6Route(ShowIpRoute):
    def cli(self, vrf = ''):
        return(super().cli(ip='ipv6', vrf=vrf))
