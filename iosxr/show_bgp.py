''' show_bgp.py

show bgp parser class

'''

import re

from ats import tcl
from ats.tcl import tclobj, tclstr
from metaparser import MetaParser
from metaparser.util.schemaengine import Any
from xbu_shared.parser.iosxr import IosxrCaasMetaParser


class ShowBgpL2vpnEvpn(IosxrCaasMetaParser):
    '''Parser class for 'show bgp l2vpn evpn' CLI.'''
    # TODO schema

    def cli(self):
        ''' parsing mechanism: cli

        Function cli() defines the cli type output parsing mechanism which
        typically contains 3 steps: executing, transforming, returning
        '''
        result = tcl.q.caas.abstract(device=self.device.handle,
                                     exec='show bgp l2vpn evpn')
        return tcl.cast_any(result[1])


class ShowBgpL2vpnEvpnAdvertised(MetaParser):
    '''Parser class for 'show bgp l2vpn evpn advertised' CLI.'''

    # TODO schema

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def cli(self):
        cmd = 'show bgp l2vpn evpn advertised'.format()

        out = self.device.execute(cmd)

        result = {
            'entries': []
        }

        attr_strings = (
            'MET',
            'ORG',
            'AS',
            'LOCAL',
            'AGG',
            'COMM',
            'ATOM',
            'EXTCOMM',
            'ATTRSET',
            'LBLIDX',
        )
        re_attr_string = r'(?:' + r'|'.join(attr_strings) + ')'

        entry = None
        for line in out.splitlines():
            line = line.rstrip()

            # [2][0][48][7777.7777.0002][0]/104 is advertised to 100.0.0.10
            m = re.match(r'^(?P<prefix>\[[^/]+\])/(?P<prefix_length>[0-9]+) is advertised to (?P<neighbor>\S+)$', line)
            if m:
                entry = m.groupdict()
                result['entries'].append(entry)
                path_info = None
                attr_info = None
                continue

            #  Path info:
            m = re.match(r'^ +Path info:$', line)
            if m:
                assert 'path_in' not in entry
                path_info = entry['path_in'] = {}
                continue

            #    neighbor: Local           neighbor router id: 8.8.8.8
            m = re.match(r'^ +neighbor: (?P<neighbor>\S+) +neighbor router id: (?P<neighbor_router_id>\S+)$', line)
            if m:
                path_info.update(m.groupdict())
                continue

            #    valid  redistributed  best  import-candidate  
            # TODO many different strings/formats and not necessarily the next line

            # Received Path ID 0, Local Path ID 0, version 193217
            m = re.match(r'^ *Received Path ID (?P<rx_path_id>\d+), Local Path ID (?P<local_path_id>\d+), version (?P<pelem_version>\d+)$', line)
            if m:
                path_info.update(m.groupdict())
                continue

            #  Attributes after inbound policy was applied:
            m = re.match(r'^ *Attributes after inbound policy was applied:$', line)
            if m:
                assert 'attr_in' not in entry
                attr_info = entry['attr_in'] = {}
                path_info = entry.setdefault('path_in', {})
                continue

            #  Attributes after outbound policy was applied:
            m = re.match(r'^ *Attributes after outbound policy was applied:$', line)
            if m:
                assert 'attr_out' not in entry
                attr_info = entry['attr_out'] = {}
                path_info = entry['path_out'] = {}
                continue

            #    next hop: 8.8.8.8
            m = re.match(r'^ +next hop: (?P<next_hop>\S+)$', line)
            if m:
                path_info.update(m.groupdict())
                continue

            #    EXTCOMM 
            #    ORG AS EXTCOMM 
            m = re.match(r'^(?: +' + re_attr_string + r')+$' , line)
            if m:
                attr_info['attributes'] = set(line.split())
                continue

            #    origin: IGP  
            m = re.match(r'^ +origin: (?P<origin>.+)$', line)
            if m:
                attr_info.update(m.groupdict())
                continue

            #    aspath: 
            m = re.match(r'^ +aspath: (?P<aspath>.+)$', line)
            if m:
                attr_info.update(m.groupdict())
                continue

            #    community: no-export
            m = re.match(r'^ +community: (?P<comms>.+)$', line)
            if m:
                attr_info['comms'] = m.group('comms').split()
                continue

            #    extended community: SoO:0.0.0.0:0 RT:100:7 
            m = re.match(r'^ +extended community: (?P<extcomms>.+)$', line)
            if m:
                attr_info['extcomms'] = extcomms = []
                s = ' ' + m.group('extcomms')
                while s:
                    ms = re.match(' +(?P<type>[^:]+):(?P<value>[^ +]+)(?P<next_extcomm> +.+)?$', s)
                    assert ms
                    extcomm = ms.groupdict()
                    s = extcomm.pop('next_extcomm')
                    extcomms.append(extcomm)
                continue

        return result


# vim: ft=python ts=8 sw=4 et
