'''
show_segment_routing.py

IOSXE parsers for the following show commands:
    * 'show segment-routing mpls lb'
    * 'show segment-routing mpls state'
    * 'show segment-routing mpls lb lock'
    * 'show segment-routing mpls connected-prefix-sid-map ipv4'
    * 'show segment-routing mpls connected-prefix-sid-map ipv6'
    * 'show segment-routing mpls gb'
    * 'show segment-routing mpls gb lock'
    * 'show segment-routing mpls connected-prefix-sid-map local ipv4'
    * 'show segment-routing mpls connected-prefix-sid-map local ipv6'
'''

# Python
import re

# Genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# =============================================================
# Schema for:
#    * 'show segment-routing mpls connected-prefix-sid-map ipv4'
#    * 'show segment-routing mpls connected-prefix-sid-map local ipv4'
#    * 'show segment-routing mpls connected-prefix-sid-map ipv6'
#    * 'show segment-routing mpls connected-prefix-sid-map local ipv6'
# =============================================================
class ShowSegmentRoutingMplsConnectedPrefixSidMapSchema(MetaParser):
    ''' Schema for:
        * 'show segment-routing mpls connected-prefix-sid-map ipv4'
        * 'show segment-routing mpls connected-prefix-sid-map local ipv4'
        * 'show segment-routing mpls connected-prefix-sid-map ipv6'
        * 'show segment-routing mpls connected-prefix-sid-map local ipv6'
    '''

    schema = {
        'segment_routing':
            {'bindings':
                {Optional('connected_prefix_sid_map'):
                    {Optional('ipv4'):
                        {'ipv4_prefix_sid':
                            {Any():
                                {'algorithm':
                                    {Any():
                                        {'prefix': str,
                                        'value_type': str,
                                        'sid': str,
                                        'range': str,
                                        'srgb': str,
                                        Optional('source'): str,
                                        'algorithm': str,
                                        },
                                    },
                                },
                            },
                        },
                    Optional('ipv6'):
                        {'ipv6_prefix_sid':
                            {Any():
                                {'algorithm':
                                    {Any():
                                        {'prefix': str,
                                        'value_type': str,
                                        'sid': str,
                                        'range': str,
                                        'srgb': str,
                                        Optional('source'): str,
                                        'algorithm': str,
                                        },
                                    },
                                },
                            },
                        },
                    },
                    Optional('local_prefix_sid'): {
                        Optional('ipv4'): {
                            'ipv4_prefix_sid_local':{
                                Any():{
                                    'algorithm': {
                                        Any():{
                                            'prefix': str,
                                            'value_type': str,
                                            'sid': str,
                                            'range': str,
                                            'srgb': str,
                                            'algorithm': str
                                        }
                                    }
                                }
                            }
                        },
                        Optional('ipv6'): {
                            'ipv6_prefix_sid_local':{
                                Any():{
                                    'algorithm': {
                                        Any():{
                                            'prefix': str,
                                            'value_type': str,
                                            'sid': str,
                                            'range': str,
                                            'srgb': str,
                                            'algorithm': str
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
            },
        }

# ====================================================================
# Parser for:
#    * 'show segment-routing mpls connected-prefix-sid-map ipv4'
#    * 'show segment-routing mpls connected-prefix-sid-map ipv6'
# ====================================================================
class ShowSegmentRoutingMplsConnectedPrefixSidMap(ShowSegmentRoutingMplsConnectedPrefixSidMapSchema):
    ''' Parser for:
        * 'show segment-routing mpls connected-prefix-sid-map ipv4'
        * 'show segment-routing mpls connected-prefix-sid-map ipv6'
    '''
    
    cli_command = 'show segment-routing mpls connected-prefix-sid-map {address_family}'
    
    def cli(self, address_family, output=None):

        assert address_family in ['ipv4', 'ipv6']

        # Get output
        if output is None:
            out = self.device.execute(self.cli_command.format(address_family=address_family))
        else:
            out = output

        # Mapping dict
        mapping_dict = {
            'ipv4': 'ipv4_prefix_sid',
            'ipv6': 'ipv6_prefix_sid',
        }

        mapping_dict_local = {
            'ipv4': 'ipv4_prefix_sid_local',
            'ipv6': 'ipv6_prefix_sid_local',
        }

        # Init
        ret_dict = {}

        # PREFIX_SID_CONN_MAP ALGO_0
        # PREFIX_SID_CONN_MAP ALGO_1
        p1 = re.compile(r'^PREFIX_SID_CONN_MAP +(?P<algorithm>(.*))$')

        # PREFIX_SID_PROTOCOL_ADV_MAP ALGO_0
        # PREFIX_SID_PROTOCOL_ADV_MAP ALGO_1
        p2 = re.compile(r'^PREFIX_SID_PROTOCOL_ADV_MAP +(?P<algorithm>(.*))$')

        # Prefix/masklen   SID Type Range Flags SRGB
        # 10.4.1.1/32         1 Indx     1         Y
        p3 = re.compile(r'(?P<prefix>(\S+))\/(?P<masklen>(\d+)) +(?P<sid>(\d+))'
                         ' +(?P<type>(\S+)) +(?P<range>(\d+))'
                         '(?: +(?P<flags>(\S+)))? +(?P<srgb>(Y|N))$')

        # Prefix/masklen   SID Type Range Flags SRGB Source
        # 10.4.1.1/32         1 Indx     1         Y  OSPF Area 8 10.4.1.1
        # 10.16.2.2/32         2 Indx     1         Y  OSPF Area 8 10.16.2.2
        p4 = re.compile(r'(?P<prefix>(\S+))\/(?P<masklen>(\d+)) +(?P<sid>(\d+))'
                         ' +(?P<type>(\S+)) +(?P<range>(\d+))'
                         '(?: +(?P<flags>(\S+)))? +(?P<srgb>(Y|N))'
                         ' +(?P<source>(.*))$')

        for line in out.splitlines():
            line = line.strip()

            # PREFIX_SID_CONN_MAP ALGO_0
            # PREFIX_SID_CONN_MAP ALGO_1
            m = p1.match(line)
            if m:
                algorithm = m.groupdict()['algorithm']
                address_family_dict = ret_dict.setdefault('segment_routing', {}). \
                                    setdefault('bindings', {}). \
                                    setdefault('local_prefix_sid', {}). \
                                    setdefault(address_family, {}). \
                                    setdefault(mapping_dict_local[address_family], {})
                continue

            # PREFIX_SID_PROTOCOL_ADV_MAP ALGO_0
            # PREFIX_SID_PROTOCOL_ADV_MAP ALGO_1
            m = p2.match(line)
            if m:
                algorithm = m.groupdict()['algorithm']
                continue

            # Prefix/masklen   SID Type Range Flags SRGB
            # 10.4.1.1/32         1 Indx     1         Y
            m = p3.match(line)
            if m:
                group = m.groupdict()
                prefix = group['prefix'] + '/' + group['masklen']
                algo_dict = address_family_dict.setdefault(prefix, {}). \
                                setdefault('algorithm', {}). \
                                setdefault(algorithm, {})
                # Set values
                algo_dict['prefix'] = prefix
                algo_dict['algorithm'] = algorithm
                algo_dict['value_type'] = group['type']
                algo_dict['sid'] = group['sid']
                algo_dict['range'] = group['range']
                algo_dict['srgb'] = group['srgb']
                if group['flags']:
                    algo_dict['flags'] = group['flags']
                continue

            # Prefix/masklen   SID Type Range Flags SRGB Source
            # 10.4.1.1/32         1 Indx     1         Y  OSPF Area 8 10.4.1.1
            m = p4.match(line)
            if m:
                group = m.groupdict()
                prefix = group['prefix'] + '/' + group['masklen']
                # Set dict
                algo_dict = ret_dict.setdefault('segment_routing', {}).\
                                     setdefault('bindings', {}).\
                                     setdefault('connected_prefix_sid_map', {}).\
                                     setdefault(address_family, {}).\
                                     setdefault(mapping_dict[address_family], {}).\
                                     setdefault(prefix, {}).\
                                     setdefault('algorithm', {}).\
                                     setdefault(algorithm, {})
                # Set values
                algo_dict['prefix'] = prefix
                algo_dict['algorithm'] = algorithm
                algo_dict['value_type'] = group['type']
                algo_dict['sid'] = group['sid']
                algo_dict['range'] = group['range']
                algo_dict['srgb'] = group['srgb']
                algo_dict['source'] = group['source']
                if group['flags']:
                    algo_dict['flags'] = group['flags']
                continue

        return ret_dict

# ==================================
# Schema for:
#   * 'show segment-routing mpls gb'
# ==================================
class ShowSegmentRoutingMplsGbSchema(MetaParser):
    ''' Schema for:
        * 'show segment-routing mpls gb'
    '''

    schema = {
        'label_min': int,
        'label_max': int,
        'state': str,
        'default': str,
        }


# ==================================
# Parser for:
#   * 'show segment-routing mpls gb'
# ==================================
class ShowSegmentRoutingMplsGb(ShowSegmentRoutingMplsGbSchema):
    ''' Parser for:
        * 'show segment-routing mpls gb'
    '''
    
    cli_command = 'show segment-routing mpls gb'
    
    def cli(self, output=None):

        # Get output
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init
        ret_dict = {}

        # LABEL-MIN  LABEL_MAX  STATE           DEFAULT  
        # 16000      23999      ENABLED         Yes  
        p1 = re.compile(r'^(?P<label_min>(\d+)) +(?P<label_max>(\d+))'
                         ' +(?P<state>(\S+)) +(?P<default>(\S+))$')

        for line in out.splitlines():
            line = line.strip()

            # LABEL-MIN  LABEL_MAX  STATE           DEFAULT  
            # 16000      23999      ENABLED         Yes  
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['label_min'] = int(group['label_min']) 
                ret_dict['label_max'] = int(group['label_max'])
                ret_dict['state'] = group['state']
                ret_dict['default'] = group['default']
                continue

        return ret_dict


# =============================================
# Parser for 'show segment-routing mpls lb'
# =============================================

class ShowSegmentRoutingMplsLBSchema(MetaParser):
    """Schema for show segment-routing mpls lb
    """

    schema = {
        'label_min': int,
        'label_max': int,
        'state': str,
        'default': str
    }

class ShowSegmentRoutingMplsLB(ShowSegmentRoutingMplsLBSchema):
    """ Parser for show segment-routing mpls lb"""
    
    cli_command = 'show segment-routing mpls lb'
    
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        # 15000      15999      ENABLED         Yes
        p1 = re.compile(r'^(?P<label_min>\d+) +(?P<label_max>\d+) +'
                        '(?P<state>\S+) +(?P<default>\S+)$')
        
        # initial variables
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # 15000      15999      ENABLED         Yes
            m = p1.match(line)
            if m:
                group = m.groupdict()
                label_min = int(group['label_min'])
                label_max = int(group['label_max'])
                state = group['state']
                default = group['default']

                ret_dict.update({'label_min': label_min})
                ret_dict.update({'label_max': label_max})
                ret_dict.update({'state': state})
                ret_dict.update({'default': default})
                
                continue
        
        return ret_dict

# =============================================
# Parser for 'show segment-routing mpls state'
# =============================================

class ShowSegmentRoutingMplsStateSchema(MetaParser):
    """Schema for show segment-routing mpls state
    """

    schema = {
        'sr_mpls_state': str
    }

class ShowSegmentRoutingMplsState(ShowSegmentRoutingMplsStateSchema):
    """ Parser for show segment-routing mpls state"""
    
    cli_command = 'show segment-routing mpls state'
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
            
        # Segment Routing MPLS State : ENABLED
        p1 = re.compile(r'^Segment +Routing +MPLS +State +: +(?P<state>\S+)$')
        
        # initial variables
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # Segment Routing MPLS State : ENABLED
            m = p1.match(line)
            if m:
                group = m.groupdict()
                state = group['state']
                ret_dict.update({'sr_mpls_state': state})
                continue
        
        return ret_dict

# ==============================================
# Parser for 'show segment-routing mpls lb lock'
# ==============================================

class ShowSegmentRoutingMplsLbLockSchema(MetaParser):
    """Schema for show segment-routing mpls lb lock
    """

    schema = {
        'label_min': int,
        'label_max': int
    }

class ShowSegmentRoutingMplsLbLock(ShowSegmentRoutingMplsLbLockSchema):
    """ Parser for show segment-routing mpls lb lock"""

    cli_command = 'show segment-routing mpls lb lock'
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        # SR LB (15000, 15999) Lock Users :
        p1 = re.compile(r'^SR +LB +\((?P<label_min>\d+)\, +'
            '(?P<label_max>\d+)\) +Lock +Users +:')

        # initial variables
        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            # SR LB (15000, 15999) Lock Users :
            m = p1.match(line)
            if m:
                group = m.groupdict()
                label_min = int(group['label_min'])
                label_max = int(group['label_max'])

                ret_dict.update({'label_min': label_min})
                ret_dict.update({'label_max': label_max})

                continue

        return ret_dict

# ==============================================
# Parser for 'show segment-routing mpls gb lock'
# ==============================================
class ShowSegmentRoutingMplsGbLock(ShowSegmentRoutingMplsLbLockSchema):
    """ Parser for 'show segment-routing mpls gb lock'
    """

    cli_command = 'show segment-routing mpls gb lock'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # SR GB (9000, 10000) Lock Users :
        p1 = re.compile(r'^SR +GB +\((?P<label_min>\d+), +(?P<label_max>\d+)\) +Lock +Users +:$')

        ret_dict = {}

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict.update({k: int(v) for k, v in group.items() if v})
                continue

        return ret_dict

# ====================================================================
# Parser for:
#    * 'show segment-routing mpls connected-prefix-sid-map local ipv4'
#    * 'show segment-routing mpls connected-prefix-sid-map local ipv6'
# ====================================================================
class ShowSegmentRoutingMplsConnectedPrefixSidMapLocal(ShowSegmentRoutingMplsConnectedPrefixSidMap):
    ''' Parser for:
        * 'show segment-routing mpls connected-prefix-sid-map local ipv4'
        * 'show segment-routing mpls connected-prefix-sid-map local ipv6'
    '''
    
    cli_command = 'show segment-routing mpls connected-prefix-sid-map local {address_family}'
    
    def cli(self, address_family, output=None):

        assert address_family in ['ipv4', 'ipv6']

        # Get output
        if output is None:
            out = self.device.execute(self.cli_command.format(address_family=address_family))
        else:
            out = output
        return super().cli(address_family=address_family, output=out)


# ==================================================================
# Parser for:
#    * 'show segment-routing traffic-eng topology ipv4'
# ==================================================================
class ShowSegmentRoutingTrafficEngTopologySchema(MetaParser):
    """ Schema for 
        'show segment-routing traffic-eng topology ipv4'
    """
    schema = {
        "nodes": {
            Any(): {
                "ospf_router_id": str,
                "area_id": int,
                "domain_id": int,
                "asn": int,
                "prefix_sid": {
                    "prefix": str,
                    "label": int,
                    "label_type": str,
                    "domain_id": int,
                    "flags": str,
                },
                "links": {
                    Any(): {
                        "local_address": str,
                        "remote_address": str,
                        "local_node": {
                            "ospf_router_id": str,
                            "area_id": int,
                            "domain_id": int,
                            "asn": int,
                        },
                        "remote_node": {
                            "ospf_router_id": str,
                            "area_id": int,
                            "domain_id": int,
                            "asn": int,
                        },
                        "metric": str,
                        "bandwidth_total": int,
                        "bandwidth_reservable": int,
                        "admin_groups": str,
                        "adj_sid": str,
                    },
                },
            },
        },
    }

class ShowSegmentRoutingTrafficEngTopology(ShowSegmentRoutingTrafficEngTopologySchema):
    """ Parser for 
        'show segment-routing traffic-eng topology ipv4'
    """

    cli_command = 'show segment-routing traffic-eng topology ipv4'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Node 1:
        p1 = re.compile(r'^Node +(?P<node>\d+):$')

        #   TE router ID: 27.86.198.239
        p2 = re.compile(r'^TE +router +ID: +(?P<te_router_id>\S+)\)$')

        #   OSPF router ID: 27.86.198.239 area ID: 8 domain ID: 0 ASN: 9996
        p3 = re.compile(r'^OSPF router ID: +(?P<ospf_router_id>\S+) +area ID: '
                         '+(?P<area_id>\d+) +domain ID: +(?P<domain_id>\d+) '
                         '+ASN: +(?P<asn>\d+)$')

        #   Prefix SID:
        #     Prefix 27.86.198.239, label 16073 (regular), domain ID 0, flags: N , E
        p4 = re.compile(r'^Prefix +(?P<prefix>\S+), +label +(?P<label>\d+) '
                         '+\((?P<label_type>\S+)\), +domain +ID +(?P<domain_id>\d+), '
                         '+flags: +(?P<flags>[\S\s]+)$')

        #   Link[0]: local address 27.86.198.26, remote address 27.86.198.25
        p5 = re.compile(r'^Link\[(?P<link>\d+)\]: +local +address +(?P<local_address>\S+), '
                         '+remote +address +(?P<remote_address>\S+)$')

        #     Local node:
        p6 = re.compile(r'^Local +node:$')

        #     Remote node:
        p6_1 = re.compile(r'^Remote +node:$')

        #     Metric: IGP 1000, TE 1000, Delay 1000
        p7 = re.compile(r'^Metric: +(?P<metric>[\S\s]+)$')

        #     Bandwidth: Total 125000000, Reservable 0
        p8 = re.compile(r'^Bandwidth: +Total +(?P<total>\d+), +Reservable +(?P<reservable>\d+)$')

        #     Admin-groups: 0x00000000
        p9 = re.compile(r'^Admin-groups: +(?P<admin_groups>\S+)$')

        #     Adj SID: 18 (unprotected)  36 (protected)
        p10 = re.compile(r'^Adj +SID: +(?P<adj_sid>[\S\s]+)$')

        # initial variables
        ret_dict = {}
        index = 0

        for line in out.splitlines():
            line = line.strip()
            if not line:
                continue

            # Node 1:
            m = p1.match(line)
            if m:
                group = m.groupdict()
                node = int(group['node'])
                node_dict = ret_dict.setdefault('nodes', {}).setdefault(node, {})
                index = 0
                continue

            #   TE router ID: 27.86.198.239
            m = p2.match(line)
            if m:
                group = m.groupdict()
                if index == 0:
                    target = node_dict
                elif index == 1:
                    target = local_dict
                else:
                    target = remote_dict
                target.update({'te_router_id': group['te_router_id']})
                continue

            #   OSPF router ID: 27.86.198.239 area ID: 8 domain ID: 0 ASN: 9996
            m = p3.match(line)
            if m:
                group = m.groupdict()
                if index == 0:
                    target = node_dict
                elif index == 1:
                    target = local_dict
                else:
                    target = remote_dict
                target.update({k: (int(v) if v.isdigit() else v) for k, v in group.items()})
                continue

            #   Prefix SID:
            #     Prefix 27.86.198.239, label 16073 (regular), domain ID 0, flags: N , E
            m = p4.match(line)
            if m:
                group = m.groupdict()
                pref_dict = node_dict.setdefault('prefix_sid', {})
                pref_dict.update({k: (int(v) if v.isdigit() else v) for k, v in group.items()})
                continue

            #   Link[0]: local address 27.86.198.26, remote address 27.86.198.25
            m = p5.match(line)
            if m:
                group = m.groupdict()
                link = int(group['link'])
                link_dict = node_dict.setdefault('links', {}).setdefault(link, {})
                link_dict.update({'local_address': group['local_address']})
                link_dict.update({'remote_address': group['remote_address']})
                continue

            #     Local node:
            m = p6.match(line)
            if m:
                local_dict = link_dict.setdefault('local_node', {})
                index = 1
                continue

            #     Remote node:
            m = p6_1.match(line)
            if m:
                remote_dict = link_dict.setdefault('remote_node', {})
                index = 2
                continue

            #     Metric: IGP 1000, TE 1000, Delay 1000
            m = p7.match(line)
            if m:
                group = m.groupdict()
                link_dict.update({'metric': group['metric']})
                continue

            #     Bandwidth: Total 125000000, Reservable 0
            m = p8.match(line)
            if m:
                group = m.groupdict()
                link_dict.update({'bandwidth_total': int(group['total'])})
                link_dict.update({'bandwidth_reservable': int(group['reservable'])})
                continue

            #     Admin-groups: 0x00000000
            m = p9.match(line)
            if m:
                group = m.groupdict()
                link_dict.update({'admin_groups': group['admin_groups']})
                continue

            #     Adj SID: 18 (unprotected)  36 (protected)
            m = p10.match(line)
            if m:
                group = m.groupdict()
                link_dict.update({'adj_sid': group['adj_sid']})
                continue

        return ret_dict
