''' show_bgp.py

show bgp parser class

'''

import re
import logging

from metaparser import MetaParser
from metaparser.util.schemaengine import Any

from xbu_shared.parser.base import *

logger = logging.getLogger(__name__)


class ShowBgpSessions(MetaParser):
    '''Parser class for 'show bgp sessions' CLI.'''

    # TODO schema

    def cli(self):
        '''parsing mechanism: cli
        '''

        cmd = 'show bgp sessions'

        tcl_package_require_caas_parsers()
        kl = tcl_invoke_caas_abstract_parser(
            device=self.device, exec=cmd)

        return kl


class ShowBgpVrfDbVrfAll(MetaParser):
    '''Parser class for 'show bgp vrf-db vrf all'' CLI.'''

    # TODO schema

    def cli(self):
        ''' parsing mechanism: cli
        '''

        cmd = 'show bgp vrf-db vrf all'

        out = self.device.execute(cmd)

        result = {
            'entries': [],
        }

        vrf_entry = None
        afs_col = None

        for line in out.splitlines():
            line = line.rstrip()

            if not line:
                continue

            if afs_col is not None:
                # Continuation of address families column

                if len(line) >= afs_col \
                        and line[:afs_col].isspace():
                    # default                          0x60000000  0:0:0           6   v4u, Vv4u,
                    #                                                                  L2evpn
                    assert vrf_entry['afs'][-1] == ''
                    vrf_entry['afs'][-1:] = [s.strip() for s in line[afs_col:].split(',')]
                    if vrf_entry['afs'][-1] != '':
                        afs_col = None
                    continue

                logger.warning('Failed to parse continuation of VRF address families')
                afs_col = None

            # VRF                              ID          RD              REF AFs

            # irb1                             0x6000003a  192.0.0.0:2     4   v4u
            # default                          0x60000000  0:0:0           6   v4u, Vv4u,
            # bd1                              -           192.0.0.3:1     2   L2evpn
            # bd2                              -           192.0.0.3:2     2   L2evpn
            # ES:GLOBAL                        -           192.0.0.3:0     2   L2evpn
            m = re.match(r'^(?P<name>\S+)' r' +(?:-|(?P<id>0x[A-Fa-f0-9]+))' r' +(?P<rd>\S+)' r' +(?P<refs>\d+)' r' +(?P<afs>.+)' r'$', line)
            if m:
                vrf_entry = {
                    'name': m.group('name'),
                    'id': m.group('id') and eval(m.group('id')),
                    'rd': m.group('rd'),
                    'refs': int(m.group('refs')),
                    'afs': [s.strip() for s in m.group('afs').split(',')],
                }
                result['entries'].append(vrf_entry)
                # NOTE: a ',' at the end of afs will leave an empty element which will be completed later
                if vrf_entry['afs'][-1] == '':
                    afs_col = m.span('afs')[0]
                continue

        return result


class ShowBgpL2vpnEvpn(MetaParser):
    '''Parser class for 'show bgp l2vpn evpn' CLI.'''

    # TODO schema

    def cli(self):
        ''' parsing mechanism: cli
        '''

        cmd = 'show bgp l2vpn evpn'

        tcl_package_require_caas_parsers()
        kl = tcl_invoke_caas_abstract_parser(
            device=self.device, exec=cmd)

        return kl


class ShowBgpL2vpnEvpnAdvertised(MetaParser):
    '''Parser class for 'show bgp l2vpn evpn advertised' CLI.'''

    # TODO schema

    def cli(self):
        cmd = 'show bgp l2vpn evpn advertised'.format()

        out = self.device.execute(cmd)

        result = {
            'entries': [],
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
            m = re.match(r'^(?: +' + re_attr_string + r')+$', line)
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
