''' show_bgp.py

show bgp parser class

'''

import re
import logging
import collections
from ipaddress import ip_address, ip_network

from metaparser import MetaParser
from metaparser.util.schemaengine import Any

from xbu_shared.parser.base import *

logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)
#logger.setLevel(logging.DEBUG)


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

    def __init__(self, rd=None, prefix=None, route_type=None, **kwargs):
        self.rd = rd
        self.prefix = prefix
        self.route_type = route_type
        super().__init__(**kwargs)

    def cli(self):
        ''' parsing mechanism: cli
        '''

        is_detail = False
        cmd = 'show bgp l2vpn evpn'
        if self.rd is not None:
            cmd += ' rd {}'.format(self.rd)
        if self.prefix is not None:
            cmd += ' {}'.format(self.prefix)
            is_detail = True
        if self.route_type is not None:
            cmd += ' route-type {}'.format(self.route_type)

        # XXXJST Workaround Csccon issue that doesn't quote Tcl arguments properly
        cmd = re.escape(cmd)
        out = self.device.execute(cmd)
        out = re.sub(r'\r+\n', r'\n', out)

        result = {
            'rds': collections.OrderedDict(),
        }

        def finalize_network_entry(network_entry):
            m = re.match(r'^(?P<prefix>\S+)/(?P<prefix_len>\d+)$', network_entry['network'])
            assert m, network_entry['network']
            network_entry.update(m.groupdict())
            for k, func in (
                    ('network', ip_network),
                    ('prefix', ip_address),
                    ('prefix_len', int),
            ):
                v = network_entry.get(k, None)
                if v is not None:
                    v = v.strip()
                    try:
                        v = func(v)
                    except (ValueError, TypeError):
                        pass
                    network_entry[k] = v

        def finalize_path_entry(path_entry):
            for k, func in (
                    ('nexthop', ip_address),
                    ('metric', int),
                    ('localpref', int),
                    ('weight', int),
            ):
                v = path_entry.get(k, None)
                if v is not None:
                    v = v.strip() or None
                    if v is not None:
                        try:
                            v = func(v)
                        except (ValueError, TypeError):
                            pass
                    path_entry[k] = v
            path_entry['status_codes'] = tuple((path_entry['status_codes'] or '').replace(' ', ''))

        if is_detail:

            lines = out.splitlines()
            while lines:
                orig_line = lines.pop(0)
                line = orig_line.rstrip()

                # BGP routing table entry for [2][0][48][fc00.0001.0006][0]/104, Route Distinguisher: 192.0.0.0:1
                # Versions:
                #   Process           bRIB/RIB  SendTblVer
                #   Speaker                114         114
                #     Local Label: 64000
                # Last Modified: Dec  5 14:54:21.410 for 1d00h
                # Paths: (2 available, best #1)
                #   Advertised to update-groups (with more than one peer):
                #     0.2
                #   Path #1: Received by speaker 0
                #   Advertised to update-groups (with more than one peer):
                #     0.2
                #   Local
                #     0.0.0.0 from 0.0.0.0 (192.0.0.0)
                #       Origin IGP, localpref 100, valid, redistributed, best, group-best, import-candidate, rib-install
                #       Received Path ID 0, Local Path ID 0, version 114
                #       Extended community: SoO:192.0.0.0:1 RT:4:1
                #       EVPN ESI: 0001.2222.2222.2200.000a
                #   Path #2: Received by speaker 0
                #   Not advertised to any peer
                #   65002
                #     192.0.0.1 from 192.0.0.1 (192.0.0.1)
                #       Received Label 68097
                #       Origin IGP, localpref 100, valid, external, group-best, import-candidate, imported, rib-install
                #       Received Path ID 0, Local Path ID 0, version 0
                #       Extended community: SoO:192.0.0.0:1 RT:4:1
                #       EVPN ESI: 0001.2222.2222.2200.000a
                #       Source AFI: L2VPN EVPN, Source VRF: default, Source Route Distinguisher: 192.0.0.1:1

                logger.debug('Unmatched line: %r', line)

        else:

            m_network_heading = None
            lines = out.splitlines()
            while lines:
                orig_line = lines.pop(0)
                line = orig_line.rstrip()

                if not m_network_heading:

                    # BGP router identifier 192.0.0.1, local AS number 100
                    m = re.match(r'^BGP router identifier (?P<router_id>\d+\.\d+\.\d+\.\d+), local AS number (?P<local_asn>\d+)$', line)
                    if m:
                        result['router_id'] = ip_address(m.group('router_id'))
                        result['local_asn'] = int(m.group('local_asn'))
                        continue

                    # BGP generic scan interval 60 secs
                    # Non-stop routing is enabled
                    # BGP table state: Active
                    # Table ID: 0x0   RD version: 0
                    # BGP main routing table version 41
                    # BGP NSR Initial initsync version 7 (Reached)
                    # BGP NSR/ISSU Sync-Group versions 0/0
                    # BGP scan interval 60 secs

                    # Status codes: s suppressed, d damped, h history, * valid, > best
                    #               i - internal, r RIB-failure, S stale, N Nexthop-discard
                    # Origin codes: i - IGP, e - EGP, ? - incomplete

                    #    Network            Next Hop            Metric LocPrf Weight Path
                    m = re.match(r'(?P<status_codes>   )(?P<network>Network +)(?P<nexthop>Next Hop +)(?P<metric>Metric +)(?P<localpref>LocPrf +)(?P<weight>Weight )(?P<path>Path)$', line)
                    if m:
                        m_network_heading = m
                        # Notes:
                        #  - Network column value could be too long to fit. In this case, the first line will contain only path status codes and the network, the following line will contain Next Hop and the other columns.
                        #  - Values for Metric and LocPrf are optional
                        #  - Path column always contains the path's origin code which could be preceeded be an aspath specification
                        #  - After the first path, more paths for the same network can appear with a blank network column

                        _re_status_codes = r'[sdh*>irSN ]' * len(m_network_heading.group('status_codes'))
                        _re_skip_status_codes = r' ' * len(m_network_heading.group('status_codes'))
                        _re_path_end = r'\S+(?: +\d+)?(?: +\d+)? +\d+(?: +(?:\S.* )?\S)$'
                        _re_network_lookahead = r'(?=[0-9:\[])'
                        _re_network = _re_network_lookahead + r'.' * len(m_network_heading.group('network'))
                        _re_skip_network = r' ' * len(m_network_heading.group('network'))
                        re_net_and_first_path = _re_status_codes + _re_network + _re_path_end
                        re_status_and_net = r'(?P<status_codes>' + _re_status_codes + ')' + r'(?P<network>' + _re_network_lookahead + '\S+)$'
                        re_continued_first_path = _re_skip_status_codes + _re_skip_network + _re_path_end
                        re_more_path = _re_status_codes + _re_skip_network + _re_path_end

                        logger.debug('re_net_and_first_path = %r', re_net_and_first_path)
                        logger.debug('re_status_and_net = %r', re_status_and_net)
                        logger.debug('re_continued_first_path = %r', re_continued_first_path)
                        logger.debug('re_more_path = %r', re_more_path)

                        # Example:
                        #   re_net_and_first_path = '[sdh*>irSN ][sdh*>irSN ][sdh*>irSN ](?=[0-9:\\[])...................\\S+(?: +\\d+)?(?: +\\d+)? +\\d+(?: +(?:\\S.* )?\\S)$'
                        #   re_status_and_net = '(?P<status_codes>[sdh*>irSN ][sdh*>irSN ][sdh*>irSN ])(?P<network>(?=[0-9:\\[])\\S+)$'
                        #   re_continued_first_path = '                      \\S+(?: +\\d+)?(?: +\\d+)? +\\d+(?: +(?:\\S.* )?\\S)$'
                        #   re_more_path = '[sdh*>irSN ][sdh*>irSN ][sdh*>irSN ]                   \\S+(?: +\\d+)?(?: +\\d+)? +\\d+(?: +(?:\\S.* )?\\S)$'

                        path_slices = {
                            'status_codes': slice(*m_network_heading.span('status_codes')),
                            'network': slice(*m_network_heading.span('network')),
                            'nexthop': slice(*m_network_heading.span('nexthop')),
                            'metric': slice(*m_network_heading.span('metric')),
                            'localpref': slice(*m_network_heading.span('localpref')),
                            'weight': slice(*m_network_heading.span('weight')),
                            'path': slice(m_network_heading.start('path'), None),
                        }

                        def extract_path_entry(line):
                            path_entry = {k: line[v].strip() or None for k, v in path_slices.items()}
                            path = path_entry.pop('path')
                            m = re.match(r'^(?:(?P<aspath>.+) )?(?P<origin_code>\S)$', path)
                            assert m, (line, path)
                            path_entry.update(m.groupdict())
                            return path_entry

                        continue

                if m_network_heading:

                    # Route Distinguisher: 192.0.0.4:0
                    # Route Distinguisher: 192.0.0.5:0 (default for vrf ES:GLOBAL)
                    # Route Distinguisher: 192.0.0.5:1 (default for vrf bd1)
                    m = re.match(r'^Route Distinguisher: (?P<rd>\S+)(?: \(default for vrf (?P<vrf>\S+)\))?$', line)
                    if m:
                        rd_entry = {
                            'rd': m.group('rd'),
                            'vrf': m.group('vrf'),
                            'networks': collections.OrderedDict(),
                        }
                        rd_key = rd_entry['rd']
                        assert rd_key not in result['rds']
                        result['rds'][rd_key] = rd_entry
                        network_entry = None
                        path_entry = None
                        continue

                    m = re.match(re_net_and_first_path, line)
                    if m:
                        path_entry = extract_path_entry(line)
                        network_entry = {
                            'network': path_entry.pop('network'),
                            'paths': collections.OrderedDict(),
                        }
                        finalize_network_entry(network_entry)
                        rd_entry['networks'][str(network_entry['network'])] = network_entry
                        finalize_path_entry(path_entry)
                        network_entry['paths'][str(path_entry['nexthop'])] = path_entry
                        continue

                    # *>i[4][0001.2222.2222.2200.000a][32][192.0.0.4]/128
                    # *> [1][192.0.0.1:1][0001.2222.2222.2200.000a][4294967295]/184
                    m = re.match(re_status_and_net, line)
                    if m:
                        line2 = lines.pop(0).rstrip()
                        #                       0.0.0.0                                0 i
                        #                       192.0.0.4                     100      0 i
                        m2 = re.match(re_continued_first_path, line2)
                        assert m2, (line, line2)
                        path_entry = extract_path_entry(line2)
                        path_entry.update(m.groupdict())
                        network_entry = {
                            'network': path_entry.pop('network'),
                            'paths': collections.OrderedDict(),
                        }
                        finalize_network_entry(network_entry)
                        rd_entry['networks'][str(network_entry['network'])] = network_entry
                        finalize_path_entry(path_entry)
                        network_entry['paths'][str(path_entry['nexthop'])] = path_entry
                        continue

                    # * i                   192.0.0.4                     100      0 i
                    m = re.match(re_more_path, line)
                    if m:
                        path_entry = extract_path_entry(line)
                        path_entry.pop('network')
                        finalize_path_entry(path_entry)
                        network_entry['paths'][str(path_entry['nexthop'])] = path_entry
                        continue

                # Processed 36 prefixes, 40 paths
                m = re.match(r'^Processed (?P<prefixes_cnt>\d+) prefixes, (?P<paths_cnt>\d+) paths$', line)
                if m:
                    result.setdefault('stats', {})
                    result['stats'].update({
                        'prefixes_cnt': int(m.group('prefixes_cnt')),
                        'paths_cnt': int(m.group('paths_cnt')),
                    })
                    continue

                logger.debug('Unmatched line: %r', line)

        return result


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
                entry.update({
                    'paths': [],
                })
                path_info = None
                attr_info = None
                continue

            #  Path info:
            m = re.match(r'^ +Path info:$', line)
            if m:
                assert 'path_info' not in entry
                path_info = entry['path_info'] = {}
                continue

            #    neighbor: Local           neighbor router id: 8.8.8.8
            m = re.match(r'^ +neighbor: (?P<neighbor>\S+) +neighbor router id: (?P<neighbor_router_id>\S+)$', line)
            if m:
                if attr_info:
                    attr_info.update(m.groupdict())
                else:
                    path_info.update(m.groupdict())
                continue

            #    valid  redistributed  best  import-candidate
            m = re.match(r'^ +(?P<flags>[A-Za-z-]+(?:  [A-Za-z-]+)*)$', line)
            if m:
                path_info['flags'] = m.group('flags').split()

            # Received Path ID 0, Local Path ID 0, version 193217
            m = re.match(r'^ *Received Path ID (?P<rx_path_id>\d+), Local Path ID (?P<local_path_id>\d+), version (?P<pelem_version>\d+)$', line)
            if m:
                path_info = m.groupdict()
                entry['paths'].append(path_info)
                continue

            #  Attributes after inbound policy was applied:
            m = re.match(r'^ *Attributes after inbound policy was applied:$', line)
            if m:
                assert 'attr_in' not in path_info
                attr_info = path_info['attr_in'] = {}
                continue

            #  Attributes after outbound policy was applied:
            m = re.match(r'^ *Attributes after outbound policy was applied:$', line)
            if m:
                assert 'attr_out' not in path_info
                attr_info = path_info['attr_out'] = {}
                continue

            #    next hop: 8.8.8.8
            m = re.match(r'^ +next hop: (?P<next_hop>\S+)$', line)
            if m:
                attr_info.update(m.groupdict())
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
