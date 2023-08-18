"""
    show_ip.py
    IOSXR parsers for the following show commands:

    * show ip bgp {route}

"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional, Or, And,\
                                         Default, Use


from genie.libs.parser.utils.common import Common

# ======================================================
# Parser for 'show ip bgp {route}'
# ======================================================

class ShowIpBgpSchema(MetaParser):
    """Schema for show ip bgp {route}"""

    schema = {
        'vrf': {
            Any(): {
                'address_family': {
                    Any(): {
                        'prefix': str,
                        'last_modified': str,
                        'paths': {
                            'total_available_paths': int,
                            'best_path': int,
                            'best_advertised_peer': str,
                            'path': {
                                Any(): {
                                    'advertised_peer': str,
                                    'as_path': {
                                        Any(): {
                                            'bgp_peer_neighbor_ip': {
                                                Any(): {
                                                    Optional('metric'): int,
                                                    'bgp_peer_neighbor_ip': str,
                                                    'origin_neighbors_ip': str,
                                                    'origin_router_id': str,
                                                    'origin_metric': int,
                                                    Optional('localpref'): int,
                                                    Optional('origin'): str,
                                                    Optional('valid'): bool,
                                                    Optional('best'): bool,
                                                    Optional('state'): str,
                                                    Optional('weight'): int,
                                                    'received_path_id': int,
                                                    'local_path_id': int,
                                                    'version': int
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

class ShowIpBgp(ShowIpBgpSchema):
    """Parser for show ip bgp {route}"""

    cli_command = ['show ip bgp {route}']

    def cli(self, route, output=None):
        if output is None:
            output = self.device.execute(self.cli_command[0].format(route=route))

        # BGP routing table entry for 70.3.3.3/32
        p1 = re.compile(r'^BGP\s+routing\s+table\s+entry\s+for\s+(?P<prefix>(?P<ip>[a-z0-9.:\/]+)\/(?P<mask>\d+))$')

        # Last Modified: Mar 27 02:45:20.105 for 1d15h
        p2 = re.compile(r'^Last +Modified: (?P<last_modified>.*)$')

        # Paths: (1 available, best #1)
        p3 = re.compile(r'^Paths:\s+\((?P<total_available_paths>\d+)\s+available,\s+best\s+#(?P<best_path>\d+)\)$')

        # Path #1: Received by speaker 0
        p4 = re.compile(r'^Path\s+#(?P<path_num>\d+):.*$')

        # 0.2
        p5 = re.compile(r'^(?P<advertised_peer>[\d\.]+)$')

        # 7000, (Received from a RR-client)
        # Local, (Received from a RR-client)
        p6 = re.compile(r'^(?P<as_path>[a-zA-Z0-9]+),.*$')

        # 50.1.1.1 (metric 4) from 50.1.1.8 (50.1.1.1)
        # 2000:90:33:1::2 from 2000:90:33:1::2 (70.3.3.3)
        # :: from :: (50.1.1.4)
        p7 = re.compile(r'^(?P<bgp_peer_neighbor_ip>[\w.:]+)\s+(?:\(metric\s+(?P<metric>\d+)\)\s+)?from\s+(?P<origin_neighbors_ip>[\w.:]+)\s*(?:\((?P<origin_router_id>[\w.:]+)\))?')

        # Origin incomplete, metric 0, localpref 100, valid, internal, best, group-best
        # Origin IGP, metric 0, localpref 100, valid, external, best, group-best
        # Origin incomplete, metric 0, localpref 100, weight 32768, valid, redistributed, best, group-best
        p8 = re.compile(r'^Origin +(?P<origin>[a-zA-Z]+),'
                         r'(?: +metric (?P<metric>[0-9]+),?)?'
                         r'(?: +localpref (?P<localpref>[0-9]+),?)?'
                         r'(?: +weight (?P<weight>[0-9]+),?)?'
                         r'(?: +(?P<valid>valid?),)?'
                         r'(?: (?P<redistributed>redistributed?),)?'
                         r'(?: +(?P<state>(internal|external|local)?),)?'
                         r'(\,*)?(?: (?P<best>best))?'
                         r'(\,*)?(?: (?P<group_best>group-best?),*)?$')

        #  Received Path ID 0, Local Path ID 0, version 715
        p9 = re.compile(r'^Received\s+Path\s+ID\s+(?P<received_path_id>(\d+)),\s+'
                         r'Local\s+Path\s+ID\s+(?P<local_path_id>(\d+)),\s+'
                         r'version\s+(?P<version>(\d+))$')

        # Initialize dictionary
        ret_dict = {}
        address_family = 'ipv4 unicast'
        vrf = 'default'
        count = 0

        for line in output.splitlines():
            line = line.strip()

            # BGP routing table entry for 2000:71:1:1::1/128, Route Distinguisher: 50.1.1.4:2
            m = p1.match(line)
            if m:
                group = m.groupdict()
                address_family = address_family.replace(' ','_')
                vrf_dict = ret_dict.setdefault('vrf', {}).\
                                    setdefault(vrf, {}).\
                                    setdefault('address_family', {}).\
                                    setdefault(address_family, {})
                
                vrf_dict['prefix'] = group['prefix']
                continue

            # Last Modified: Mar 27 02:45:20.105 for 1d15h
            m = p2.match(line)
            if m:
                group = m.groupdict()
                vrf_dict['last_modified'] = group['last_modified']
                continue

            # Paths: (1 available, best #1)
            m = p3.match(line)
            if m:
                group = m.groupdict()
                paths_dict = vrf_dict.setdefault('paths', {})
                paths_dict['total_available_paths'] = int(group['total_available_paths'])
                paths_dict['best_path'] = int(group['best_path'])
                continue

            # Path #1: Received by speaker 0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                path = group['path_num']
                each_path_dict = paths_dict.setdefault('path', {}).setdefault(path,{})
                continue

            # 0.2
            m = p5.match(line)
            if m:
                group = m.groupdict()
                advertised_peer = group['advertised_peer']

                if count == 0:
                    paths_dict['best_advertised_peer'] = advertised_peer
                    count += 1
                else:
                    each_path_dict['advertised_peer'] = advertised_peer
                continue

            # 7000, (Received from a RR-client)
            # Local, (Received from a RR-client)
            m = p6.match(line)
            if m:
                group = m.groupdict()
                as_path = group['as_path']
                as_path_dict = each_path_dict.setdefault('as_path', {}).setdefault(as_path, {})
                continue

            # 50.1.1.1 (metric 4) from 50.1.1.8 (50.1.1.1)
            # 2000:90:33:1::2 from 2000:90:33:1::2 (70.3.3.3)
            # :: from :: (50.1.1.4)
            m = p7.match(line)
            if m:
                group = m.groupdict()
                bgp_peer_neighbor_ip = group['bgp_peer_neighbor_ip']
                next_hop_dict = as_path_dict.setdefault('bgp_peer_neighbor_ip', {}).setdefault(bgp_peer_neighbor_ip, {})
                if group['metric']:
                    next_hop_dict['metric'] = int(group['metric'])
                next_hop_dict['bgp_peer_neighbor_ip'] = bgp_peer_neighbor_ip
                next_hop_dict['origin_neighbors_ip'] = group['origin_neighbors_ip']
                next_hop_dict['origin_router_id'] = group['origin_router_id']
                continue

            # Origin incomplete, metric 0, localpref 100, valid, internal, best, group-best
            # Origin IGP, metric 0, localpref 100, valid, external, best, group-best
            # Origin incomplete, metric 0, localpref 100, weight 32768, valid, redistributed, best, group-best
            m = p8.match(line)
            if m:
                group = m.groupdict()
                if group['metric']:
                    next_hop_dict['origin_metric'] = int(group['metric'])
                if group['localpref']:
                    next_hop_dict['localpref'] = int(group['localpref'])
                if group['weight']:
                    next_hop_dict['weight'] = int(group['weight'])

                if group['origin']:
                    next_hop_dict['origin'] = group['origin']

                if group['valid']:
                    next_hop_dict['valid'] = True
                if group['best']:
                    next_hop_dict['best'] = True
                if group['state']:
                    next_hop_dict['state'] = group['state']
                continue

            # Received Path ID 0, Local Path ID 0, version 715
            m = p9.match(line)
            if m:
                group = m.groupdict()
                next_hop_dict['received_path_id'] = int(group['received_path_id'])
                next_hop_dict['local_path_id'] = int(group['local_path_id'])
                next_hop_dict['version'] = int(group['version'])
                continue

        return ret_dict
