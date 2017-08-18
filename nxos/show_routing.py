''' show_routing.py

NXOS parser for the following show commands:
    * show routing vrf all
    * show routing ipv6 vrf all
'''

# Python
import re

# Metaparser
from metaparser import MetaParser
from metaparser.util.schemaengine import Schema, Any, Optional, Or, And,\
                                         Default, Use

# =================================
# Parser for 'show routing vrf all'
# =================================

class ShowRoutingVrfAllSchema(MetaParser):
    
    ''' Schema for 'show routing vrf all' '''

    schema = {
        'vrf':
            {Any():
                {Optional('address_family'):
                    {Any():
                        {Optional('bgp_distance_extern_as'): int,
                        Optional('bgp_distance_internal_as'): int,
                        Optional('bgp_distance_local'): int,
                        'ip':
                            {Any():
                                {'ubest_num': str,
                                'mbest_num': str,
                                Optional('attach'): str,
                                Optional('best_route'):
                                    {Optional(Any()):
                                        {Optional('nexthop'):
                                            {Optional(Any()):
                                                {Optional('protocol'):
                                                    {Optional(Any()):
                                                        {Optional('route_table'): str,
                                                        Optional('uptime'): str,
                                                        Optional('interface'): str,
                                                        Optional('preference'): str,
                                                        Optional('metric'): str,
                                                        Optional('protocol_id'): str,
                                                        Optional('attribute'): str,
                                                        Optional('tag'): str, 
                                                        Optional('mpls'): bool,
                                                        Optional('mpls_vpn'): bool,
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
            },
        },
    }


class ShowRoutingVrfAll(ShowRoutingVrfAllSchema):
   
    ''' Parser for 'show routing vrf all' '''

    def convert_intf_name(self, intf):
        # Please add more when face other type of interface
        convert = {'Eth': 'Ethernet',
                   'Lo': 'Loopback',
                   'Null': 'Null',
                   'mgmt': 'mgmt'}
        int_type = re.search('([a-zA-Z]+)', intf).group(0)
        int_port = re.search('([\d\/\.]+)', intf).group(0)
        if int_type in convert.keys():
            return(convert[int_type] + int_port)
        else:
            return(intf)

    
    def cli(self, ip=''):

        cmd = 'show routing {} vrf all'.format(ip) if ip else 'show routing vrf all'
        out = self.device.execute(cmd)
        
        # Init dict
        bgp_dict = {}
        sub_dict = {}
        address_family = None

        for line in out.splitlines():
            line = line.strip()

            # IP Route Table for VRF "default"
            # IPv6 Routing Table for VRF "default"
            p1 = re.compile(r'^(IP|IPv6) +(Route|Routing) +Table +for +VRF +"(?P<vrf>\w+)"$')
            m = p1.match(line)
            if m:
                vrf = str(m.groupdict()['vrf'])
                if vrf == 'default' and not ip:
                    address_family = 'ipv4 unicast'
                elif vrf != 'default' and not ip:
                    address_family = 'vpnv4 unicast'
                elif vrf == 'default' and ip:
                    address_family = 'ipv6 unicast'
                elif vrf != 'default' and ip:
                    address_family = 'vpnv6 unicast'
                continue

            p2 = re.compile(r'^(?P<ip_mask>[\w\:\.\/]+), +ubest/mbest: +(?P<ubest>\d+)'
                             '/(?P<mbest>\d+),? *(?P<attach>\w+)?$')
            m = p2.match(line)
            if m:
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

                # Init ip dict
                ip_mask = m.groupdict()['ip_mask']
                if 'ip' not in sub_dict:
                    sub_dict['ip'] = {}
                if ip_mask not in sub_dict['ip']:
                    sub_dict['ip'][ip_mask] = {}
                
                sub_dict['ip'][ip_mask]['ubest_num'] = m.groupdict()['ubest']
                sub_dict['ip'][ip_mask]['mbest_num'] = m.groupdict()['mbest']
                if m.groupdict()['attach']:
                    sub_dict['ip'][ip_mask]['attach'] = m.groupdict()['attach']
                    continue

            # *via fec1::1002%default, Eth1/1, [200/4444], 15:57:39, bgp-333, internal, tag 333
            # *via 3.3.3.3%default, [33/0], 5w0d, bgp-100, internal, tag 100 (mpls-vpn)
            # *via 2001:db8::5054:ff:fed5:63f9, Eth1/1, [0/0], 00:15:46, direct,
            # *via 2001:db8:2:2::2, Eth1/1, [0/0], 00:15:46, direct, , tag 222
            p3 = re.compile(r'^(?P<cast>.*)via +(?P<nexthop>[\w\.\:\s]+)(%(?P<table>[\w\:]+))?, *'
                             '((?P<int>[a-zA-Z0-9\./_]+),)? *'
                             '\[(?P<preference>\d+)/(?P<metric>\d+)\], *'
                             '(?P<up_time>[\w\:\.]+), *'
                             '(?P<protocol>\w+)(\-(?P<process>\d+))?,? *'
                             '(?P<attribute>\w+)?,? *'
                             '(tag *(?P<tag>\w+))?,? *(?P<vpn>[a-zA-Z\(\)\-]+)?$')
            m = p3.match(line)
            if m:
                cast = m.groupdict()['cast']
                cast = {'1': 'unicast',
                        '2': 'multicast'}['{}'.format(cast.count('*'))]

                 # Init 'best_route' dict
                if 'best_route' not in sub_dict['ip'][ip_mask]:
                    sub_dict['ip'][ip_mask]['best_route'] = {}
                if cast not in sub_dict['ip'][ip_mask]['best_route']:
                    sub_dict['ip'][ip_mask]['best_route'][cast] = {}
                    sub_dict['ip'][ip_mask]['best_route'][cast]\
                        ['nexthop'] = {}

                nexthop = m.groupdict()['nexthop']
                if nexthop not in sub_dict\
                   ['ip'][ip_mask]['best_route'][cast]['nexthop']:
                    sub_dict['ip'][ip_mask]\
                      ['best_route'][cast]['nexthop'][nexthop] = {}
                    prot_dict = sub_dict['ip'][ip_mask]\
                      ['best_route'][cast]['nexthop'][nexthop]['protocol'] = {}

                protocol = m.groupdict()['protocol'] if \
                    m.groupdict()['protocol'] else m.groupdict()['prot']
                if protocol not in prot_dict:
                    prot_dict[protocol] = {}

                table = m.groupdict()['table']
                if table:
                    prot_dict[protocol]['route_table'] = table

                intf = m.groupdict()['int']
                if intf:
                    prot_dict[protocol]['interface'] = self.convert_intf_name(intf)

                preference = m.groupdict()['preference']
                if preference:
                    prot_dict[protocol]['preference'] = preference

                metric = m.groupdict()['metric']
                if metric:
                    prot_dict[protocol]['metric'] = metric

                up_time = m.groupdict()['up_time']
                if up_time:
                    prot_dict[protocol]['uptime'] = up_time

                process = m.groupdict()['process']
                if process:
                    prot_dict[protocol]['protocol_id'] = process

                attribute = m.groupdict()['attribute']
                if attribute:
                    prot_dict[protocol]['attribute'] = attribute
                
                tag = m.groupdict()['tag']
                if tag:
                    prot_dict[protocol]['tag'] = tag.strip()
                
                vpn = m.groupdict()['vpn']
                if vpn and 'mpls-vpn' in vpn:
                    prot_dict[protocol]['mpls_vpn'] = True
                elif vpn and 'mpls' in vpn:
                    prot_dict[protocol]['mpls'] = True

                # Set extra values for BGP Ops
                if attribute == 'external' and protocol == 'bgp':
                    sub_dict['bgp_distance_extern_as'] = int(preference)
                elif attribute == 'internal' and protocol == 'bgp':
                    sub_dict['bgp_distance_internal_as'] = int(preference)
                elif attribute == 'discard' and protocol == 'bgp':
                    sub_dict['bgp_distance_local'] = int(preference)
                    continue

        return bgp_dict


class ShowRoutingIpv6VrfAll(ShowRoutingVrfAll):
    def cli(self):
        return(super().cli(ip='ipv6'))
