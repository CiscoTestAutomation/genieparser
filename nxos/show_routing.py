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
