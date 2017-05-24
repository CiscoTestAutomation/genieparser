''' show_bgp.py

Example parser class

'''
# Python
import re

# Metaparser
from metaparser import MetaParser
from metaparser.util.schemaengine import Schema, Any, Optional, Or, And,\
                                         Default, Use


class ShowBgpVrfAllAllDampeningParametersSchema(MetaParser):
    """ Schema class - Initialize the data structure.
    """
    schema = {'vrf':
              {Any():
               {'address_family':
                {Any():
                 {Optional('dampening'): str,
                  Optional('dampening_route_map'): str,
                  Optional('dampening_half_life_time'): str,
                  Optional('dampening_reuse_time'): str,
                  Optional('dampening_suppress_time'): str,
                  Optional('dampening_max_suppress_time'): str,
                  Optional('dampening_max_suppress_penalty'): str,
                  Optional('route_distinguisher'):
                   {Optional(Any()):
                    {Optional('dampening'): str,
                     Optional('rd_vrf'): str,
                     Optional('dampening_route_map'): str,
                     Optional('dampening_half_life_time'): str,
                     Optional('dampening_reuse_time'): str,
                     Optional('dampening_suppress_time'): str,
                     Optional('dampening_max_suppress_time'): str,
                     Optional('dampening_max_suppress_penalty'): str,
             }}, }}, }}, }


class ShowBgpVrfAllAllDampeningParameters(
               ShowBgpVrfAllAllDampeningParametersSchema):
    """ Parser class - Parse out the data and create hierarchical structure
                       for cli, xml, and yang output.
    """
    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        cmd = 'show bgp vrf all all dampening parameters'
        out = self.device.execute(cmd)
        bgp_dict = {}
        sub_dict = {}

        for line in out.splitlines():
            line = line.strip()
            p1 = re.compile(r'^Route +(?P<route>\w+) +Dampening +Parameters '
                             '+for +VRF +(?P<vrf>\w+) +Address +family '
                             '+(?P<af_name>[a-zA-Z0-9 ]+):$')
            m = p1.match(line)
            if m:
                if 'vrf' not in bgp_dict:
                    bgp_dict['vrf'] = {}

                vrf = m.groupdict()['vrf']
                if vrf not in bgp_dict['vrf']:
                    bgp_dict['vrf'][vrf] = {}
                    bgp_dict['vrf'][vrf]['address_family'] = {}

                af_name = m.groupdict()['af_name'].lower()
                if af_name not in bgp_dict['vrf'][vrf]['address_family']:
                    bgp_dict['vrf'][vrf]['address_family'][af_name] = {}
                    # trim the coding lines for adopting pep8
                    sub_dict = bgp_dict['vrf'][vrf]['address_family'][af_name]
                    sub_dict['dampening'] = 'True'
                continue

            p9 = re.compile(r'^Route +Distinguisher: +(?P<rd>[0-9\.:]+) +'
                             '\(VRF +(?P<rd_vrf>\w+)\)$')
            m = p9.match(line)
            if m:
                if 'route_distinguisher' not in \
                  bgp_dict['vrf'][vrf]['address_family'][af_name]:
                   bgp_dict['vrf'][vrf]['address_family']\
                     [af_name]['route_distinguisher'] = {}
                rd = m.groupdict()['rd']
                if rd and rd not in bgp_dict['vrf'][vrf]['address_family']\
                  [af_name]['route_distinguisher']:
                    sub_dict = bgp_dict['vrf'][vrf]['address_family']\
                      [af_name]['route_distinguisher'][rd] = {}

                rd_vrf = m.groupdict()['rd_vrf']
                if rd_vrf:
                    sub_dict['rd_vrf'] = rd_vrf
                continue

            p2 = re.compile(r'^Dampening +policy +configured: '
                             '+(?P<route_map>\w+)$')
            m = p2.match(line)
            if m:
                sub_dict['dampening_route_map'] = m.groupdict()['route_map']
                continue

            p3 = re.compile(r'^Half-life +time +: +'
                             '(?P<half_time>[a-zA-Z0-9 ]+)$')
            m = p3.match(line)
            if m:
                sub_dict['dampening_half_life_time'] =\
                   m.groupdict()['half_time']
                continue

            p4 = re.compile(r'^Suppress +penalty +: +'
                             '(?P<suppress_pen>[a-zA-Z0-9 ]+)$')
            m = p4.match(line)
            if m:
                sub_dict['dampening_suppress_time'] =\
                  m.groupdict()['suppress_pen']
                continue

            p5 = re.compile(r'^Reuse +penalty +: +'
                             '(?P<reuse_pen>[a-zA-Z0-9 ]+)$')
            m = p5.match(line)
            if m:
                sub_dict['dampening_reuse_time'] =\
                  m.groupdict()['reuse_pen']
                continue

            p6 = re.compile(r'^Max +suppress +time +: +'
                             '(?P<max_sup_time>[a-zA-Z0-9 ]+)$')
            m = p6.match(line)
            if m:
                sub_dict['dampening_max_suppress_time'] =\
                  m.groupdict()['max_sup_time']
                continue

            p7 = re.compile(r'^Max +suppress +penalty +: '
                             '+(?P<max_sup_pen>[a-zA-Z0-9 ]+)$')
            m = p7.match(line)
            if m:
                sub_dict['dampening_max_suppress_penalty'] =\
                  m.groupdict()['max_sup_pen']
                continue
        return bgp_dict
