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
    
    def cli(self, address_family, local=False, output=None):

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