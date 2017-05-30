''' show_routing.py

Example parser class

'''
# Python
import re

# Metaparser
from metaparser import MetaParser
from metaparser.util.schemaengine import Schema, Any, Optional, Or, And,\
                                         Default, Use


class ShowRoutingVrfAllSchema(MetaParser):
    """ Schema class - Initialize the data structure.
    """
    schema = {'vrf':
              {Any():
               {'ip/mask':
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
                        Optional('attibute'): str,
                        Optional('tag'): str, }}, }}, }}, }}, }}, }


class ShowRoutingVrfAll(ShowRoutingVrfAllSchema):
    """ Parser class - Parse out the data and create hierarchical structure
                       for cli, xml, and yang output.
    """
    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        cmd = 'show routing vrf all'
        out = self.device.execute(cmd)
        bgp_dict = {}
        sub_dict = {}

        for line in out.splitlines():
            line = line.strip()

            p1 = re.compile(r'^IP +Route +Table +for +VRF +"(?P<vrf>\w+)"$')
            m = p1.match(line)
            if m:
                vrf = m.groupdict()['vrf']
                continue

            p2 = re.compile(r'^(?P<ip_mask>.*), +ubest/mbest: +(?P<ubest>\d+)'
                             '/(?P<mbest>\d+),? *(?P<attach>\w+)?$')
            m = p2.match(line)
            if m:
                if 'vrf' not in bgp_dict:
                    bgp_dict['vrf'] = {}
                if vrf and vrf not in bgp_dict['vrf']:
                    bgp_dict['vrf'][vrf] = {}
                    bgp_dict['vrf'][vrf]['ip/mask'] = {}

                ip_mask = m.groupdict()['ip_mask']
                if ip_mask not in bgp_dict['vrf'][vrf]['ip/mask']:
                    bgp_dict['vrf'][vrf]['ip/mask'][ip_mask] = {}
                    bgp_dict['vrf'][vrf]['ip/mask'][ip_mask]['best_route'] = {}
                    bgp_dict['vrf'][vrf]['ip/mask'][ip_mask]['ubest_num'] = \
                        m.groupdict()['ubest']
                    bgp_dict['vrf'][vrf]['ip/mask'][ip_mask]['mbest_num'] = \
                        m.groupdict()['mbest']
                    attach = m.groupdict()['attach']
                    if attach:
                        bgp_dict['vrf'][vrf]['ip/mask'][ip_mask]['attach'] = \
                          attach
                continue

            p3 = re.compile(r'^(?P<cast>.*)via +(?P<nexthop>[a-zA-Z0-9 \.:]+)'
                             '%?(?P<table>\w+)?, *'
                             '(?P<int>[a-zA-Z0-9\./_]+)?,? +'
                             '\[(?P<preference>\d+)/(?P<metric>\d+)\], +'
                             '(?P<up_time>.*), +'
                             '(?:(?P<protocol>\w+)-(?P<process>\d+), +'
                             '(?P<attibute>\w+), +tag +(?P<tag>.*)'
                             '|(?P<prot>\w+))$')
            m = p3.match(line)
            if m:
                cast = m.groupdict()['cast']
                cast = {'1': 'unicast',
                        '2': 'multicast'}['{}'.format(cast.count('*'))]
                if cast not in \
                   bgp_dict['vrf'][vrf]['ip/mask'][ip_mask]['best_route']:
                    bgp_dict['vrf'][vrf]['ip/mask'][ip_mask]\
                      ['best_route'][cast] = {}
                    bgp_dict['vrf'][vrf]['ip/mask'][ip_mask]\
                      ['best_route'][cast]['nexthop'] = {}

                nexthop = m.groupdict()['nexthop']
                if nexthop not in bgp_dict['vrf'][vrf]\
                   ['ip/mask'][ip_mask]['best_route'][cast]['nexthop']:
                    bgp_dict['vrf'][vrf]['ip/mask'][ip_mask]\
                      ['best_route'][cast]['nexthop'][nexthop] = {}
                    sub_dict = bgp_dict['vrf'][vrf]['ip/mask'][ip_mask]\
                      ['best_route'][cast]['nexthop'][nexthop]['protocol'] = {}

                protocol = m.groupdict()['protocol'] if \
                    m.groupdict()['protocol'] else m.groupdict()['prot']
                if protocol not in sub_dict:
                    sub_dict[protocol] = {}

                table = m.groupdict()['table']
                if table:
                    sub_dict[protocol]['route_table'] = table

                intf = m.groupdict()['int']
                if intf:
                    sub_dict[protocol]['interface'] = intf

                preference = m.groupdict()['preference']
                if preference:
                    sub_dict[protocol]['preference'] = preference

                metric = m.groupdict()['metric']
                if metric:
                    sub_dict[protocol]['metric'] = metric

                up_time = m.groupdict()['up_time']
                if up_time:
                    sub_dict[protocol]['uptime'] = up_time

                process = m.groupdict()['process']
                if process:
                    sub_dict[protocol]['protocol_id'] = process

                attibute = m.groupdict()['attibute']
                if attibute:
                    sub_dict[protocol]['attibute'] = attibute

                tag = m.groupdict()['tag']
                if tag:
                    sub_dict[protocol]['tag'] = tag
                continue

        return bgp_dict

class ShowRouteMapSchema(MetaParser):
    """ Schema class - Initialize the data structure.
    """

    schema = {'route_map':
              {Any():
                {'match_clause':
                        {Optional('ip_address_prefix_list'): str,
                         Optional('ip_route_source_prefix_list'): str,
                         Optional('community'): str,
                         Optional('ipv6_address_prefix_list'): str,
                         Optional('ipv6_route_source_prefix_list'): str,
                         Optional('as-path'): str,
                         Optional('extcommunity'): str},
                 'set_clause':
                        {Optional('ip_address_prefix_list'): str,
                         Optional('ip_route_source_prefix_list'): str,
                         Optional('community'): str,
                         Optional('ipv6_address_prefix_list'): str,
                         Optional('ipv6_route_source_prefix_list'): str,
                         Optional('as-path'): str,
                         Optional('extcommunity'): str},
                 'permit_deny': str,
                 'sequence': str}
              },
            }

class ShowRouteMap(ShowRouteMapSchema):
    """ Parser class - Parse out the data and create hierarchical structure
                       for cli, xml, and yang output.
    """
    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        cmd = 'show route-map'
        out = self.device.execute(cmd)
        route_map_dict = {}

        for line in out.splitlines():
            line = line.strip()

            p1 = re.compile(r'^\s*route-map +(?P<name>[A-Z0-9\_]+),'
              ' +(?P<permit_deny>[a-zA-Z]+), +sequence +(?P<sequence>[0-9]+)$')
            m = p1.match(line)
            if m:
                route_map = m.groupdict()['name']
                permit_deny = m.groupdict()['permit_deny']
                sequence = m.groupdict()['sequence']
                if 'route_map' not in route_map_dict:
                    route_map_dict['route_map'] = {}
                if route_map not in route_map_dict['route_map']:
                    route_map_dict['route_map'][route_map] = {}
                route_map_dict['route_map'][route_map]['permit_deny'] = \
                  m.groupdict()['permit_deny']
                route_map_dict['route_map'][route_map]['sequence'] = \
                  m.groupdict()['sequence']
                continue

            p2 = re.compile(r'^\s*Match clauses:$')
            m = p2.match(line)
            if m:
                if 'match_clause' not in route_map_dict['route_map'][route_map]:
                    route_map_dict['route_map'][route_map]['match_clause'] = {}
                continue

            p3 = re.compile(r'^\s*(?P<ip_type>[a-z0-9]+) +address'
              ' +prefix-lists: +(?P<prefix_list>[A-Z0-9\_]+)$')
            m = p3.match(line)
            if m:
                ip_type = m.groupdict()['ip_type']
                if ip_type == 'ip':
                    route_map_dict['route_map'][route_map]['match_clause']\
                      ['ip_address_prefix_list'] = m.groupdict()['prefix_list']
                else:
                    route_map_dict['route_map'][route_map]['match_clause']\
                      ['ipv6_address_prefix_list'] = m.groupdict()['prefix_list']
                continue

            p4 = re.compile(r'^\s*(?P<ip_type>[a-z0-9]+) +route-source'
              ' +prefix-lists: +(?P<prefix_list>[A-Z0-9\_]+)$')
            m = p4.match(line)
            if m:
                ip_type = m.groupdict()['ip_type']
                if ip_type == 'ip':
                    route_map_dict['route_map'][route_map]['match_clause']\
                      ['ip_route_source_prefix_list'] = \
                        m.groupdict()['prefix_list']
                else:
                    route_map_dict['route_map'][route_map]['match_clause']\
                      ['ipv6_route_source_prefix_list'] = \
                        m.groupdict()['prefix_list']
                continue

            p5 = re.compile(r'^\s*as-path \(as-path filter\):'
              ' +(?P<as_path>[A-Z\_]+)$')
            m = p5.match(line)
            if m:
                route_map_dict['route_map'][route_map]['match_clause']\
                  ['as-path'] = m.groupdict()['as_path']
                continue

            p6 = re.compile(r'^\s*community +(?P<community>[a-z0-9\:\s]+)$')
            m = p6.match(line)
            if m:
                route_map_dict['route_map'][route_map]['match_clause']\
                  ['community'] = m.groupdict()['community']
                continue

            p7 = re.compile(r'^\s*Set clauses:$')
            m = p7.match(line)
            if m:
                if 'set_clause' not in route_map_dict['route_map'][route_map]:
                    route_map_dict['route_map'][route_map]['set_clause'] = {}
                continue

            p8 = re.compile(r'^\s*(?P<ip_type>[a-z0-9]+) +address'
              ' +(prefix-list): +(?P<prefix_list>[A-Z0-9\_]+)$')
            m = p8.match(line)
            if m:
                ip_type = m.groupdict()['ip_type']
                if ip_type == 'ip':
                    route_map_dict['route_map'][route_map]['set_clause']\
                      ['ip_address_prefix_list'] = m.groupdict()['prefix_list']
                else:
                    route_map_dict['route_map'][route_map]['set_clause']\
                      ['ipv6_address_prefix_list'] = m.groupdict()['prefix_list']
                continue

            p9 = re.compile(r'^\s*(?P<ip_type>[a-z0-9]+) +route-source'
              ' +(prefix-list): +(?P<prefix_list>[A-Z0-9\_]+)$')
            m = p9.match(line)
            if m:
                ip_type = m.groupdict()['ip_type']
                if ip_type == 'ip':
                    route_map_dict['route_map'][route_map]['set_clause']\
                      ['ip_route_source_prefix_list'] = \
                        m.groupdict()['prefix_list']
                else:
                    route_map_dict['route_map'][route_map]['set_clause']\
                      ['ipv6_route_source_prefix_list'] = \
                        m.groupdict()['prefix_list']
                continue

            p10 = re.compile(r'^\s*as-path +(?P<as_path>[A-Z\_]+)$')
            m = p10.match(line)
            if m:
                route_map_dict['route_map'][route_map]['set_clause']\
                  ['as-path'] = m.groupdict()['as_path']
                continue

            p11 = re.compile(r'^\s*community +(?P<community>[a-z0-9\:\s]+)$')
            m = p11.match(line)
            if m:
                route_map_dict['route_map'][route_map]['set_clause']\
                  ['community'] = m.groupdict()['community']
                continue

            p12 = re.compile(r'^\s*extcommunity +(?P<extcommunity>[A-Za-z0-9\:\s]+)$')
            m = p12.match(line)
            if m:
                route_map_dict['route_map'][route_map]['set_clause']\
                  ['extcommunity'] = m.groupdict()['extcommunity']
                continue

        return route_map_dict
