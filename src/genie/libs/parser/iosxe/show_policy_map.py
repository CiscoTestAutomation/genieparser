''' show_policy_map.py

IOSXE parsers for the following show commands:
    * 'show policy-map interface {interface} input class {class_name}',
    * 'show policy-map interface {interface} output class {class_name}',
    * 'show policy-map interface {interface} input',
    * 'show policy-map interface {interface} output',
    * 'show policy-map interface {interface}',
    * 'show policy-map interface class {class_name}',
    * 'show policy-map target service-group {num}',
    * 'show policy-map control-plane'
    * 'show policy-map interface',
    * 'show policy-map type control subscriber binding <policymap name>',
    * 'show policy-map type queueing interface {interface} output class {class_name}',
    * 'show policy-map type queueing interface {interface} output',
'''

# Python
import re
import xmltodict
import collections
from netaddr import IPAddress, IPNetwork

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, And, Default, Use

# import parser utils
from genie.libs.parser.utils.common import Common


# ==========================================================================
# Schema for :
#   * 'show policy-map interface {interface} input class {class_name}',
#   * 'show policy-map interface {interface} output class {class_name}',
#   * 'show policy-map interface {interface} input',
#   * 'show policy-map interface {interface} output',
#   * 'show policy-map interface {interface}',
#   * 'show policy-map interface class {class_name}',
#   * 'show policy-map target service-group {num}',
#   * 'show policy-map control-plane'
#   * 'show policy-map interface',
#   * 'show policy-map type queueing interface {interface} output class {class_name}'
#   * 'show policy-map type queueing interface {interface} output'
# ===========================================================================
class ShowPolicyMapTypeSchema(MetaParser):

    ''' Schema for :
        * 'show policy-map interface {interface} input class {class_name}',
        * 'show policy-map interface {interface} output class {class_name}',
        * 'show policy-map interface {interface} input',
        * 'show policy-map interface {interface} output',
        * 'show policy-map interface {interface}',
        * 'show policy-map interface class {class_name}',
        * 'show policy-map control-plane'
        * 'show policy-map interface',
    '''

    schema = {
        Any(): {
            Optional('service_group'): int,
            Optional('service_policy'): {
                Any(): {
                    Optional('policy_name'): {
                        Any(): {
                            Optional('class_map'): {
                                Any(): {
                                    'match_evaluation': str,
                                    'match': list,
                                    Optional('packets'): int,
                                    Optional('packet_output'): int,
                                    Optional('packet_drop'): int,
                                    Optional('tail_random_drops'): int,
                                    Optional('other_drops'): int,
                                    Optional('bytes'): int,
                                    Optional('queueing'): bool,
                                    Optional('queue_limit_packets'): str,
                                    Optional('queue_size'): int,
                                    Optional('queue_limit'): int,
                                    Optional('queue_limit_bytes'): int,
                                    Optional('queue_limit_us'): int,
                                    Optional('queue_depth'): int,
                                    Optional('total_drops'): int,
                                    Optional('no_buffer_drops'): int,
                                    Optional('pkts_output'): int,
                                    Optional('bytes_output'): int,
                                    Optional('pkts_matched'): int,
                                    Optional('bytes_matched'): int,
                                    Optional('pkts_queued'): int,
                                    Optional('bytes_queued'): int,
                                    Optional('shape_type'): str,
                                    Optional('shape_cir_bps'): int,
                                    Optional('shape_bc_bps'): int,
                                    Optional('shape_be_bps'): int,
                                    Optional('target_shape_rate'): int,
                                    Optional('output_queue'): str,
                                    Optional('bandwidth_percent'): int,
                                    Optional('bandwidth_kbps'): int,
                                    Optional('bandwidth'): str,
                                    Optional('bandwidth_remaining_ratio'): int,
                                    Optional('bandwidth_remaining_percent'): int,
                                    Optional('fair_queue_limit_per_flow'): int,
                                    Optional('bandwidth_max_threshold_packets'): int,
                                    Optional('priority_level'): int,
                                    Optional('overhead_accounting'): str,
                                    Optional('random_detect'): {
                                        Optional('exp_weight_constant'): str,
                                        Optional('exponential_weight'): str,
                                        Optional('mean_queue_depth'): int,
                                        Optional('class'): {
                                            Any(): {
                                                'transmitted_packets': str,
                                                'transmitted_bytes': str,
                                                'random_drop_packets': str,
                                                'random_drop_bytes': str,
                                                'tail_drop_packets': str,
                                                'tail_drop_bytes': str,
                                                'minimum_thresh': str,
                                                'maximum_thresh': str,
                                                'mark_prob': str,
                                                Optional('ecn_mark'): str
                                            },
                                        },
                                    },
                                    Optional('priority'): {
                                        Optional('percent'): int,
                                        Optional('kbps'): int,
                                        Optional('burst_bytes'): int,
                                        Optional('exceed_drops'): int,
                                        Optional('type'): str},
                                    Optional('rate'): {
                                        Optional('interval'): int,
                                        Optional('offered_rate_bps'): int,
                                        Optional('drop_rate_bps'): int
                                    },
                                    Optional('policy'): {
                                        Any(): {
                                            'class': {
                                                Any(): {
                                                    Optional('bandwidth'): int,
                                                    Optional('random_detect'): {
                                                        'precedence': list,
                                                        'bytes1': list,
                                                        'bytes2': list,
                                                        'bytes3': list,
                                                    },
                                                },
                                            },
                                        },
                                    },
                                    Optional('qos_set'): {
                                        Optional('mpls_experimental_imposition'): int,
                                        Any(): {
                                            Any(): {
                                                Optional('packets_marked'): int,
                                                Optional('marker_statistics'): str,  
                                            },
                                        },
                                    },
                                    Optional('police'): {
                                        Optional('cir_bps'): int,
                                        Optional('pir_bps'): int,
                                        Optional('cir_bc_bytes'): int,
                                        Optional('cir_be_bytes'): int,
                                        Optional('pir_bc_bytes'): int,
                                        Optional('pir_be_bytes'): int,
                                        Optional('police_bps'): int,
                                        Optional('police_limit'): int,
                                        Optional('extended_limit'): int,
                                        Optional('bandwidth_remaining_ratio'): int,
                                        Optional('conformed'): {
                                            Optional('packets'): int,
                                            'bytes': int,
                                            'bps': int,
                                            Optional('actions'): {
                                                Any(): Or(bool, str),
                                            }
                                        },
                                        Optional('exceeded'): {
                                            Optional('packets'): int,
                                            'bytes': int,
                                            'bps': int,
                                            Optional('actions'): {
                                                Any(): Or(bool, str),
                                            }
                                        },
                                        Optional('violated'): {
                                            Optional('packets'): int,
                                            'bytes': int,
                                            'bps': int,
                                            Optional('actions'): {
                                                Any(): Or(bool, str),
                                            }
                                        },
                                    },
                                    Optional('afd_wred_stats'): {
                                        'virtual_class': {
                                            Any(): {
                                                'dscp': int,
                                                'min': int,
                                                'max': int,
                                                'transmit_bytes': int,
                                                'transmit_packets': int,
                                                'random_drop_bytes': int,
                                                'random_drop_packets': int,
                                                'afd_weight': int
                                            }
                                        },
                                        'total_drops_bytes': int,
                                        'total_drops_packets': int
                                    },
                                    Optional('child_policy_name'): {
                                        Any(): {
                                            Optional('class_map'): {
                                                Any():{
                                                    'match_evaluation': str,
                                                    'match': list,
                                                    Optional('packets'): int,
                                                    Optional('packet_output'): int,
                                                    Optional('packet_drop'): int,
                                                    Optional('tail_random_drops'): int,
                                                    Optional('other_drops'): int,
                                                    Optional('bytes'): int,
                                                    Optional('queueing'): bool,
                                                    Optional('queue_limit_packets'): str,
                                                    Optional('queue_size'): int,
                                                    Optional('queue_limit'): int,
                                                    Optional('queue_limit_bytes'): int,
                                                    Optional('queue_limit_us'): int,
                                                    Optional('queue_depth'): int,
                                                    Optional('total_drops'): int,
                                                    Optional('no_buffer_drops'): int,
                                                    Optional('pkts_output'): int,
                                                    Optional('bytes_output'): int,
                                                    Optional('pkts_matched'): int,
                                                    Optional('bytes_matched'): int,
                                                    Optional('pkts_queued'): int,
                                                    Optional('bytes_queued'): int,
                                                    Optional('shape_type'): str,
                                                    Optional('shape_cir_bps'): int,
                                                    Optional('shape_bc_bps'): int,
                                                    Optional('shape_be_bps'): int,
                                                    Optional('target_shape_rate'): int,
                                                    Optional('output_queue'): str,
                                                    Optional('bandwidth_percent'): int,
                                                    Optional('bandwidth_kbps'): int,
                                                    Optional('bandwidth'): str,
                                                    Optional('bandwidth_remaining_ratio'): int,
                                                    Optional('bandwidth_remaining_percent'): int,
                                                    Optional('fair_queue_limit_per_flow'): int,
                                                    Optional('bandwidth_max_threshold_packets'): int,
                                                    Optional('priority_level'): int,
                                                    Optional('overhead_accounting'): str,
                                                    Optional('random_detect'): {
                                                        Optional('exp_weight_constant'): str,
                                                        Optional('exponential_weight'): str,
                                                        Optional('mean_queue_depth'): int,
                                                        Optional('class'): {
                                                            Any(): {
                                                                'transmitted_packets': str,
                                                                'transmitted_bytes': str,
                                                                'random_drop_packets': str,
                                                                'random_drop_bytes': str,
                                                                'tail_drop_packets': str,
                                                                'tail_drop_bytes': str,
                                                                'minimum_thresh': str,
                                                                'maximum_thresh': str,
                                                                'mark_prob': str,
                                                                Optional('ecn_mark'): str
                                                            },
                                                        },
                                                    },
                                                    Optional('priority'): {
                                                        Optional('percent'): int,
                                                        Optional('kbps'): int,
                                                        Optional('burst_bytes'): int,
                                                        Optional('exceed_drops'): int,
                                                        Optional('type'): str},
                                                    Optional('rate'): {
                                                        Optional('interval'): int,
                                                        Optional('offered_rate_bps'): int,
                                                        Optional('drop_rate_bps'): int
                                                    },
                                                    Optional('policy'): {
                                                        Any(): {
                                                            'class': {
                                                                Any(): {
                                                                    Optional('bandwidth'): int,
                                                                    Optional('random_detect'): {
                                                                        'precedence': list,
                                                                        'bytes1': list,
                                                                        'bytes2': list,
                                                                        'bytes3': list,
                                                                    },
                                                                },
                                                            },
                                                        },
                                                    },
                                                    Optional('qos_set'): {
                                                        Optional('mpls_experimental_imposition'): int,
                                                        Any(): {
                                                            Any(): {
                                                                Optional('packets_marked'): int,
                                                                Optional('marker_statistics'): str,
                                                            },
                                                        },
                                                    },
                                                    Optional('police'): {
                                                        Optional('cir_bps'): int,
                                                        Optional('pir_bps'): int,
                                                        Optional('cir_bc_bytes'): int,
                                                        Optional('cir_be_bytes'): int,
                                                        Optional('pir_bc_bytes'): int,
                                                        Optional('pir_be_bytes'): int,
                                                        Optional('police_bps'): int,
                                                        Optional('police_limit'): int,
                                                        Optional('extended_limit'): int,
                                                        Optional('bandwidth_remaining_ratio'): int,
                                                        Optional('conformed'): {
                                                            Optional('packets'): int,
                                                            'bytes': int,
                                                            'bps': int,
                                                            Optional('actions'): {
                                                                Any(): Or(bool, str),
                                                            }
                                                        },
                                                        Optional('exceeded'): {
                                                            Optional('packets'): int,
                                                            'bytes': int,
                                                            'bps': int,
                                                            Optional('actions'): {
                                                                Any(): Or(bool, str),
                                                            }
                                                        },
                                                        Optional('violated'): {
                                                            Optional('packets'): int,
                                                            'bytes': int,
                                                            'bps': int,
                                                            Optional('actions'): {
                                                                Any(): Or(bool, str),
                                                            }
                                                        },
                                                    },
                                                    Optional('afd_wred_stats'): {
                                                        'virtual_class': {
                                                            Any(): {
                                                                'dscp': int,
                                                                'min': int,
                                                                'max': int,
                                                                'transmit_bytes': int,
                                                                'transmit_packets': int,
                                                                'random_drop_bytes': int,
                                                                'random_drop_packets': int,
                                                                'afd_weight': int
                                                            }
                                                        },
                                                        'total_drops_bytes': int,
                                                        'total_drops_packets': int
                                                    },
                                                    Optional('child_policy_name'): {
                                                        Any():{
                                                            Optional('class_map'): {
                                                                Any():{
                                                                    'match_evaluation': str,
                                                                    'match': list,
                                                                    Optional('packets'): int,
                                                                    Optional('packet_output'): int,
                                                                    Optional('packet_drop'): int,
                                                                    Optional('tail_random_drops'): int,
                                                                    Optional('other_drops'): int,
                                                                    Optional('bytes'): int,
                                                                    Optional('queueing'): bool,
                                                                    Optional('queue_limit_packets'): str,
                                                                    Optional('queue_size'): int,
                                                                    Optional('queue_limit'): int,
                                                                    Optional('queue_limit_bytes'): int,
                                                                    Optional('queue_limit_us'): int,
                                                                    Optional('queue_depth'): int,
                                                                    Optional('total_drops'): int,
                                                                    Optional('no_buffer_drops'): int,
                                                                    Optional('pkts_output'): int,
                                                                    Optional('bytes_output'): int,
                                                                    Optional('pkts_matched'): int,
                                                                    Optional('bytes_matched'): int,
                                                                    Optional('pkts_queued'): int,
                                                                    Optional('bytes_queued'): int,
                                                                    Optional('shape_type'): str,
                                                                    Optional('shape_cir_bps'): int,
                                                                    Optional('shape_bc_bps'): int,
                                                                    Optional('shape_be_bps'): int,
                                                                    Optional('target_shape_rate'): int,
                                                                    Optional('output_queue'): str,
                                                                    Optional('bandwidth_percent'): int,
                                                                    Optional('bandwidth_kbps'): int,
                                                                    Optional('bandwidth'): str,
                                                                    Optional('bandwidth_remaining_ratio'): int,
                                                                    Optional('bandwidth_remaining_percent'): int,
                                                                    Optional('fair_queue_limit_per_flow'): int,
                                                                    Optional('bandwidth_max_threshold_packets'): int,
                                                                    Optional('priority_level'): int,
                                                                    Optional('overhead_accounting'): str,
                                                                    Optional('random_detect'): {
                                                                        Optional('exp_weight_constant'): str,
                                                                        Optional('exponential_weight'): str,
                                                                        Optional('mean_queue_depth'): int,
                                                                        Optional('class'): {
                                                                            Any(): {
                                                                                'transmitted_packets': str,
                                                                                'transmitted_bytes': str,
                                                                                'random_drop_packets': str,
                                                                                'random_drop_bytes': str,
                                                                                'tail_drop_packets': str,
                                                                                'tail_drop_bytes': str,
                                                                                'minimum_thresh': str,
                                                                                'maximum_thresh': str,
                                                                                'mark_prob': str,
                                                                                Optional('ecn_mark'): str
                                                                            },
                                                                        },
                                                                    },
                                                                    Optional('priority'): {
                                                                        Optional('percent'): int,
                                                                        Optional('kbps'): int,
                                                                        Optional('burst_bytes'): int,
                                                                        Optional('exceed_drops'): int,
                                                                        Optional('type'): str},
                                                                    Optional('rate'): {
                                                                        Optional('interval'): int,
                                                                        Optional('offered_rate_bps'): int,
                                                                        Optional('drop_rate_bps'): int
                                                                    },
                                                                    Optional('policy'): {
                                                                        Any(): {
                                                                            'class': {
                                                                                Any(): {
                                                                                    Optional('bandwidth'): int,
                                                                                    Optional('random_detect'): {
                                                                                        'precedence': list,
                                                                                        'bytes1': list,
                                                                                        'bytes2': list,
                                                                                        'bytes3': list,
                                                                                    },
                                                                                },
                                                                            },
                                                                        },
                                                                    },
                                                                    Optional('qos_set'): {
                                                                        Optional('mpls_experimental_imposition'): int,
                                                                        Any(): {
                                                                            Any(): {
                                                                                Optional('packets_marked'): int,
                                                                                Optional('marker_statistics'): str,
                                                                            }, 
                                                                        },
                                                                    },
                                                                    Optional('police'): {
                                                                        Optional('cir_bps'): int,
                                                                        Optional('pir_bps'): int,
                                                                        Optional('cir_bc_bytes'): int,
                                                                        Optional('cir_be_bytes'): int,
                                                                        Optional('pir_bc_bytes'): int,
                                                                        Optional('pir_be_bytes'): int,
                                                                        Optional('police_bps'): int,
                                                                        Optional('police_limit'): int,
                                                                        Optional('extended_limit'): int,
                                                                        Optional('bandwidth_remaining_ratio'): int,
                                                                        Optional('conformed'): {
                                                                            Optional('packets'): int,
                                                                            'bytes': int,
                                                                            'bps': int,
                                                                            Optional('actions'): {
                                                                                Any(): Or(bool, str),
                                                                            }
                                                                        },
                                                                        Optional('exceeded'): {
                                                                            Optional('packets'): int,
                                                                            'bytes': int,
                                                                            'bps': int,
                                                                            Optional('actions'): {
                                                                                Any(): Or(bool, str),
                                                                            }
                                                                        },
                                                                        Optional('violated'): {
                                                                            Optional('packets'): int,
                                                                            'bytes': int,
                                                                            'bps': int,
                                                                            Optional('actions'): {
                                                                                Any(): Or(bool, str),
                                                                            }
                                                                        },
                                                                    },
                                                                    Optional('afd_wred_stats'): {
                                                                        'virtual_class': {
                                                                            Any(): {
                                                                                'dscp': int,
                                                                                'min': int,
                                                                                'max': int,
                                                                                'transmit_bytes': int,
                                                                                'transmit_packets': int,
                                                                                'random_drop_bytes': int,
                                                                                'random_drop_packets': int,
                                                                                'afd_weight': int
                                                                            }
                                                                        },
                                                                        'total_drops_bytes': int,
                                                                        'total_drops_packets': int
                                                                    },
                                                                },
                                                            },
                                                            Optional('queue_stats_for_all_priority_classes'): {
                                                                Optional('priority_level'): {
                                                                    Any(): {
                                                                        Optional('queueing'): bool,
                                                                        Optional('queue_limit_packets'): str,
                                                                        Optional('queue_limit_bytes'): int,
                                                                        Optional('queue_limit_us'): int,
                                                                        Optional('queue_depth'): int,
                                                                        Optional('total_drops'): int,
                                                                        Optional('no_buffer_drops'): int,
                                                                        Optional('pkts_output'): int,
                                                                        Optional('bytes_output'): int,
                                                                    },
                                                                },
                                                            },
                                                        },
                                                    },
                                                },
                                            },
                                            Optional('queue_stats_for_all_priority_classes'): {
                                                Optional('priority_level'): {
                                                    Any(): {
                                                        Optional('queueing'): bool,
                                                        Optional('queue_limit_packets'): str,
                                                        Optional('queue_limit_bytes'): int,
                                                        Optional('queue_limit_us'): int,
                                                        Optional('queue_depth'): int,
                                                        Optional('total_drops'): int,
                                                        Optional('no_buffer_drops'): int,
                                                        Optional('pkts_output'): int,
                                                        Optional('bytes_output'): int,
                                                    },
                                                },
                                            },
                                        },
                                    },   
                                },
                            },
                            Optional('queue_stats_for_all_priority_classes'): {
                                Optional('priority_level'): {
                                    Any(): {
                                        Optional('queueing'): bool,
                                        Optional('queue_limit_packets'): str,
                                        Optional('queue_limit_bytes'): int,
                                        Optional('queue_limit_us'): int,
                                        Optional('queue_depth'): int,
                                        Optional('total_drops'): int,
                                        Optional('no_buffer_drops'): int,
                                        Optional('pkts_output'): int,
                                        Optional('bytes_output'): int,
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }

    BOOL_ACTION_LIST = ['drop', 'transmit', 'set_clp_transmit']


# =====================================================================
# Super Parser for:
#   * 'show policy-map interface {interface} input class {class_name}',
#   * 'show policy-map interface {interface} output class {class_name}',
#   * 'show policy-map interface {interface} input',
#   * 'show policy-map interface {interface} output',
#   * 'show policy-map interface {interface}',
#   * 'show policy-map interface class {class_name}',
#   * 'show policy-map target service-group {num}',
#   * 'show policy-map control-plane'
#   * 'show policy-map interface',
# =====================================================================
class ShowPolicyMapTypeSuperParser(ShowPolicyMapTypeSchema):
    ''' Super Parser for
        * 'show policy-map interface {interface} input class {class_name}',
        * 'show policy-map interface {interface} output class {class_name}',
        * 'show policy-map interface {interface} input',
        * 'show policy-map interface {interface} output',
        * 'show policy-map interface {interface}',
        * 'show policy-map interface class {class_name}',
        * 'show policy-map target service-group {num},
        * 'show policy-map control-plane'
        * 'show policy-map interface',
    '''

    def cli(self, interface='', class_name='', num='', output=None):

        # Init vars
        out = output
        ret_dict = {}
        class_line_type = None
        queue_stats = 0
        priority_dict = {}
        priority_level_status = False

        # To capture the length of whitespaces before start of the string
        p0 = re.compile(r'^(?P<whitespace>\s*)\S.*$')

        # Control Plane
        # GigabitEthernet0/1/5
        # Something else
        p1 = re.compile(r'^(?P<top_level>(Control Plane|Giga.*|FiveGiga.*|[Pp]seudo.*|Fast.*|[Ss]erial.*|'
                        'Ten.*|[Ee]thernet.*|[Tt]unnel.*))$')
        
        # GigabitEthernet0/1/5 : Service Group 1
        p1_0 = re.compile(r'^(?P<top_level>(Giga.*)): +Service Group +(?P<service_group>(\d+))$')
        
        # Port-channel1: Service Group 1
        p1_1 = re.compile(r'^(?P<top_level>([Pp]ort.*)): +Service Group +(?P<service_group>(\d+))$')

        # Service-policy input: Control_Plane_In
        # Service-policy output: shape-out
        # Service-policy input:TEST
        p2 = re.compile(r'^[Ss]ervice-policy +(?P<service_policy>(input|output)):+ *(?P<policy_name>([\w\-]+).*)')

        # service-policy : child
        p2_1 = re.compile(r'^Service-policy *:+ *(?P<policy_name>(.*))$')    

        # Class-map: Ping_Class (match-all)
        # Class-map:TEST (match-all)
        # Class-map: TEST-OTTAWA_CANADA#PYATS (match-any)
        p3 = re.compile(r'^[Cc]lass-map *:( +)?(?P<class_map>\S+) +(?P<match_all>(.*))$')

        # queue stats for all priority classes:
        p3_1 = re.compile(r'^queue +stats +for +all +priority +classes:$')


        # priority level 2
        p3_1_1 = re.compile(r'^priority +level +(?P<priority_level>(\d+))$')

        # 8 packets, 800 bytes
        p4 = re.compile(r'^(?P<packets>(\d+)) packets, (?P<bytes>(\d+)) +bytes$')

        # 8 packets
        p4_1 = re.compile(r'^(?P<packets>(\d+)) packets$')

        # 5 minute offered rate 0000 bps, drop rate 0000 bps
        p5 = re.compile(r'^(?P<interval>(\d+)) +minute +offered +rate +(?P<offered_rate>(\d+)) bps, +drop +rate +(?P<drop_rate>(\d+)) bps$')

        # 5 minute offered rate 0000 bps
        # 5 minute rate 0 bps
        p5_1 = re.compile(r'^(?P<interval>(\d+)) +minute(offered| )+rate +(?P<offered_rate>(\d+)) bps$')

        # 30 second offered rate 15000 bps, drop rate 300 bps
        p5_2 = re.compile(r'^(?P<interval>(\d+)) +second +offered +rate +(?P<offered_rate>(\d+)) bps, +drop +rate +(?P<drop_rate>(\d+)) bps$')

        # Match: access-group name Ping_Option
        # Match: access-group name PYATS-MARKING_IN#CUSTOM__ACL
        p6 = re.compile(r'^[Mm]atch:( +)?(?P<match>([\S\s]+))$')

        # police:
        p7 = re.compile(r'^police:+$')

        #  police:  cir 64000 bps, bc 8000 bytes
        p7_1 = re.compile(r'^police: +cir (?P<cir_bps>(\d+)) bps, bc (?P<cir_bc_bytes>(\d+)) bytes$')

        # cir 8000 bps, bc 1500 bytes
        p8 = re.compile(r'^cir (?P<cir_bps>(\d+)) bps, +bc +(?P<cir_bc_bytes>(\d+)) bytes$')

        # 8000 bps, 1500 limit, 1500 extended limit
        p8_1 = re.compile(r'^(?P<police_bps>(\d+)) bps, +(?P<police_limit>(\d+)) limit, +'
                          r'(?P<extended_limit>(\d+))(.*)$')

        # cir 10000000 bps, be 312500 bytes
        p8_2 = re.compile(r'^cir (?P<cir_bps>(\d+)) bps, +be +(?P<cir_be_bytes>(\d+)) bytes$')

        # pir 20000 bps, be 658 bytes
        p8_3 = re.compile(r'^pir (?P<pir_bps>(\d+)) bps, +be +(?P<pir_be_bytes>(\d+)) bytes$')

        # pir 20000 bps, bc 658 bytes
        p8_4 = re.compile(r'^pir (?P<pir_bps>(\d+)) bps, +bc +(?P<pir_bc_bytes>(\d+)) bytes$')

        # cir 10000000000 bps, bc 30000000 bytes, be 60000000 bytes
        p8_5 = re.compile(r'^cir (?P<cir_bps>(\d+)) bps, +bc +(?P<pir_bc_bytes>(\d+)) bytes, +be +(?P<cir_be_bytes>(\d+)) bytes$')

        # conformed 8 packets, 800 bytes; actions:
        p9 = re.compile(r'^conformed (?P<packets>(\d+)) packets, +(?P<bytes>(\d+)) bytes; actions:$')

        # conformed 800 bytes; actions:
        p9_0 = re.compile(r'^conformed +(?P<bytes>\d+) bytes; actions:$')

        # conformed 15 packets, 6210 bytes; action:transmit
        p9_1 = re.compile(r'^conformed (?P<packets>(\d+)) packets, +(?P<bytes>(\d+)) bytes;'
                          r' action:(?P<action>(\w+))$')

        # exceeded 0 packets, 0 bytes; actions:
        p10 = re.compile(r'^exceeded (?P<packets>(\d+)) packets, +(?P<bytes>(\d+)) bytes; actions:$')

        # exceeded 0 bytes; actions:
        p10_0 = re.compile(r'^exceeded +(?P<bytes>\d+) bytes; actions:$')

        # exceeded 5 packets, 5070 bytes; action:drop
        p10_1 = re.compile(r'^exceeded (?P<packets>(\d+)) packets, +(?P<bytes>(\d+)) bytes;'
                           r' action:(?P<action>(\w+))$')

        # violated 0 packets, 0 bytes; action:drop
        p11 = re.compile(r'^violated (?P<packets>(\d+)) packets, +(?P<bytes>(\d+)) bytes;'
                         r' action:(?P<action>(\w+))$')

        # violated 0 packets, 0 bytes; actions:
        p11_1 = re.compile(r'^violated (?P<packets>(\d+)) packets, +(?P<bytes>(\d+)) bytes; actions:$')

        # violated 0 bytes; actions:
        p11_2 = re.compile(r'^violated +(?P<bytes>(\d+)) bytes; actions:$')

        # conformed 0000 bps, exceeded 0000 bps
        p12 = re.compile(r'^conformed +(?P<c_bps>(\d+)) bps, excee(ded|d) (?P<e_bps>(\d+)) bps$')

        # conformed 0 bps, exceed 0 bps, violate 0 bps
        p12_1 = re.compile(r'^conformed +(?P<c_bps>(\d+)) bps,+ excee(d|ded) (?P<e_bps>(\d+)) bps, '
                           r'violat(e|ed) (?P<v_bps>(\d+)) bps$')

        # drop
        # transmit
        # start
        # set-qos-transmit 7
        # set-mpls-exp-imposition-transmit 7
        # set-dscp-transmit ef
        # filter 'Queueing' and 'random-detect'
        # set-dscp-transmit dscp table policed-dscp
        p13 = re.compile(r'^(?![Qr])(?P<action>drop|transmit|start|set-qos-transmit|set-mpls-exp-imposition-transmit|set-dscp-transmit|filter)( +(?P<value>.+))?$')

        # QoS Set
        p14 = re.compile(r'^QoS +Set+$')

        # ip precedence 6
        # dscp af41
        # qos-group 20
        p14_1 = re.compile(r'^(?P<key>(ip precedence|qos-group|dscp)) +(?P<value>(\w+))$')

        # Marker statistics: Disabled
        p14_2 = re.compile(r'^Marker +statistics: +(?P<marker_statistics>(\w+))$')

        # Packets marked 500
        p14_3 = re.compile(r'^Packets +marked +(?P<packets_marked>(\d+))$')

        # mpls experimental imposition 1
        p14_4 = re.compile(r'^mpls experimental imposition +(?P<value>.+)$')

        # Queueing
        p15 = re.compile(r'^Queueing$')

        # queue size 0, queue limit 4068
        p16 = re.compile(r'^queue +size +(?P<queue_size>(\d+)), +queue +limit +(?P<queue_limit>(\d+))$')

        # queue limit 64 packets
        p17 = re.compile(r'^queue +limit +(?P<queue_limit>(\d+)) packets')

        # queue limit 62500 bytes
        p17_1 = re.compile(r'^queue +limit +(?P<queue_limit_bytes>(\d+)) bytes$')

        # (queue depth/total drops/no-buffer drops) 0/0/0
        p18 = re.compile(r'^\(+queue +depth/+total +drops/+no-buffer +drops+\) +(?P<queue_depth>(\d+))/'
                         r'+(?P<total_drops>(\d+))/+(?P<no_buffer_drops>(\d+))$')

        # depth/total drops/no-buffer drops) 147/38/0
        p18_1 = re.compile(r'^depth/+total +drops/+no-buffer +drops+\) +(?P<queue_depth>(\d+))/+'
                           r'(?P<total_drops>(\d+))/+(?P<no_buffer_drops>(\d+))$')

        # (pkts output/bytes output) 0/0
        p19 = re.compile(r'^\(+pkts +output/+bytes +output+\) +(?P<pkts_output>(\d+))/+(?P<bytes_output>(\d+))$')

        # (pkts matched/bytes matched) 363/87120
        p19_0 = re.compile(r'^\(+pkts +matched/+bytes +matched+\) +(?P<pkts_matched>(\d+))/+(?P<bytes_matched>(\d+))$')

        # (pkts queued/bytes queued) 0/0
        p19_1 = re.compile(r'^\(+pkts +queued/+bytes +queued+\) +(?P<pkts_queued>(\d+))/+(?P<bytes_queued>(\d+))$')

        # shape (average) cir 474656, bc 1899, be 1899
        p20 = re.compile(r'^shape +\(+(?P<shape_type>(\w+))+\) +cir +(?P<shape_cir_bps>(\d+)), +'
                         r'bc +(?P<shape_bc_bps>(\d+)), +be +(?P<shape_be_bps>(\d+))$')

        # target shape rate 474656
        p21 = re.compile(r'^target +shape +rate +(?P<target_shape_rate>(\d+))$')

        # Output Queue: Conversation 266
        p22 = re.compile(r'^Output +Queue: +(?P<output_queue>([\w\s]+))$')

        # Bandwidth 10 (%)
        p23 = re.compile(r'^Bandwidth +(?P<bandwidth>(\d+)) .*$')

        # bandwidth 1000 (kbps)
        p24 = re.compile(r'^bandwidth (?P<bandwidth_kbps>(\d+)) \(?kbps\)?$')

        # bandwidth 5% (234 kbps)
        p24_1 = re.compile(r'^bandwidth (?P<bandwidth_percent>(\d+))\% +\((?P<bandwidth_kbps>(\d+)) +kbps\)$')

        # exponential weight: 9
        # exponential weight:9
        # Exp-weight-constant: 9 (1/512)
        # Exp-weight-constant:9 (1/512)
        p25 = re.compile(r'^(?P<key>(Exp-weight-constant|exponential.*)):+ *(?P<value>([\w\(\)\s\/]+))')

        # mean queue depth: 25920
        # Mean queue depth: 0 bytes
        # Mean queue depth:0
        p26 = re.compile(r'^(M|m)ean +queue +depth:+ *(?P<mean_queue_depth>(\d+))')

        # class     Transmitted       Random drop      Tail drop     Minimum Maximum Mark
        # class     Transmitted       Random drop      Tail drop     Minimum Maximum Mark
        # dscp      Transmitted       Random drop      Tail drop     Minimum Maximum Mark
        p27_1 = re.compile(r'^(class|dscp) +Transmitted +Random +drop +(Tail|Tail/Flow) +drop +Minimum +Maximum +Mark$')

        # Class  Random    Tail    Minimum    Maximum     Mark      Output
        p27_2 = re.compile(r'^Class +Random +Tail +Minimum +Maximum +Mark +Output$')

        # class     Transmitted       Random drop      Tail drop     Minimum Maximum Mark
        #   0             0/0               0/0               0/0      20000    40000  1/10
        #   1           328/78720          38/9120            0/0      22000    40000  1/10
        #   2             0/0               0/0               0/0      24000    40000  1/10
        #   3             0/0               0/0               0/0      26000    40000  1/10
        #   4             0/0               0/0               0/0      28000    40000  1/10     
        # Class         Random             Tail            Minimum    Maximum   Mark   Output
        #   0             0                 0                 0        0        1/10   0
        p27 = re.compile(r'^(?P<class>(\w+)) +(?P<value1_pkts>(\d+))/+(?P<value1_bytes>(\d+)) +'
                         r'(?P<value2_pkts>(\d+))/+(?P<value2_bytes>(\d+)) +'
                         r'(?P<value3_pkts>(\d+))/+(?P<value3_bytes>(\d+)) +'
                         r'(?P<value4>([\d\/]+)) +(?P<value5>([\d\/]+)) +(?P<value6>([\d\/]+))$')

        # policy wred-policy
        p28 = re.compile(r'^policy +(?P<policy>([\w\-]+))$')

        # class prec2
        p29 = re.compile(r'^class +(?P<class>([\w\-]+))$')

        # bandwidth 1000
        p30 = re.compile(r'^bandwidth +(?P<bandwidth>(\d+))$')

        # bandwidth remaining ratio 1
        p31 = re.compile(r'^bandwidth +remaining +ratio +(?P<bandwidth_remaining_ratio>(\d+))$')

        # bandwidth:class-based wfq, weight 25
        p32 = re.compile(r'^bandwidth(:| )?(?P<bandwidth>([\s\w\-\,]+))$')

        # random-detect
        p33 = re.compile(r'^random-detect$')

        # random-detect precedence 2 100 bytes 200 bytes 10
        p33_1 = re.compile(r'^random-detect +precedence +(?P<precedence>(\d+)) +'
                            '(?P<bytes1>(\d+)) bytes +(?P<bytes2>(\d+)) bytes +(?P<bytes3>(\d+))$')

        # packet output 90, packet drop 0
        p34 = re.compile(r'^packet +output +(?P<packet_output>(\d+)), +packet +drop +(?P<packet_drop>(\d+))$')

        # tail/random drop 0, no buffer drop 0, other drop 0
        p35 = re.compile(r'^tail/random drop +(?P<tail_random_drops>(\d+)), +no buffer drop +(?P<no_buffer_drops>(\d+)), '
                         r'+other drop +(?P<other_drops>(\d+))$')

        # queue limit 1966 us/ 49152 bytes
        p36 = re.compile(r'^queue +limit +(?P<queue_limit_us>(\d+)) +us/ +(?P<queue_limit_bytes>(\d+)) bytes$')

        # Priority: 10% (100000 kbps), burst bytes 2500000, b/w exceed drops: 44577300
        p37 = re.compile(r'^Priority:\s+(?P<percent>(\d+))%\s+\((?P<kbps>(\d+))\s+kbps\),\s+burst\sbytes\s+(?P<burst_bytes>(\d)+),(\s+'
                         r'b/w\sexceed\sdrops:\s+(?P<exceed_drops>(\d+)))?$')

        # Priority Level: 1
        p38 = re.compile(r'^Priority +Level: +(?P<priority_level>(\d+))$')

        # bandwidth remaining 70%
        p39 = re.compile(r'^bandwidth +remaining +(?P<bandwidth_remaining_percent>(\d+))%$')

        # Priority: Strict, b/w exceed drops: 0
        p40 = re.compile(r'^Priority: +(?P<type>(\w+)), +b/w exceed drops: +(?P<exceed_drops>(\d+))$')

        # cos 5
        p41 = re.compile(r'^(?P<key>cos)\s+(?P<value>\d+)$')

        # Virtual Class   min/max        Transmit                 Random drop                 AFD Weight
        #       0         10 / 20    (Byte)33459183360             27374016                     12
        p42 = re.compile(r'^(?P<virtual_class>\d+)\s+(?P<min>\d+)\s*/\s*(?P<max>\d+)\s+\(Byte\)(?P<tx_bytes>\d+)\s+(?P<random_drop_bytes>\d+)\s+(?P<afd_weight>\d+)\s*$')

        #                                (Pkts)68692637637             0
        p43 = re.compile(r'^\(Pkts\)(?P<tx_packets>\d+)\s+(?P<random_drop_packets>\d+)')

        #         dscp : 1
        p44 = re.compile(r'^dscp\s*:\s*(?P<dscp>\d+)$')

        #     Total Drops(Bytes)   : 0
        p45 = re.compile(r'^Total Drops\(Bytes\)\s*:\s*(?P<total_drops_bytes>\d+)$')

        #     Total Drops(Packets) : 0
        p46 = re.compile(r'^Total Drops\(Packets\)\s*:\s*(?P<total_drops_packets>\d+)$')

        # (total drops) 0
        p47 = re.compile(r'^\(total +drops\) +(?P<total_drops>(\d+))$')

        # (bytes output) 3392
        p48 = re.compile(r'^\(bytes +output\) +(?P<bytes_output>(\d+))$')

        # Overhead Accounting Enabled
        p49 = re.compile(r'Overhead +Accounting +(?P<enabled>([\w\-]+))$')

        # Fair-queue: per-flow queue limit 128 packets
        p50 = re.compile(r'^Fair-queue: +per-flow +queue +limit +(?P<queue_limit>\d+) +packets$')

        # -1 depth since the top policy-map is a child element, but has depth 0
        dict_stack = [(-1, ret_dict)]

        for line in out.splitlines():

            m = p0.match(line)
            if m:
                # get length of prepended whitespace
                len_white = len(m.groupdict()['whitespace'])

            else:
                # no contents in this line, skip
                continue

            line = line.strip()
            if not line:
                continue
            
            # Control Plane 
            # GigabitEthernet9/5: Service Group 1
            m = p1_0.match(line) or p1.match(line)
            if m:
                
                top_level = m.groupdict()['top_level']
                # check if previous dict on stack is more deeply nested than the current item
                while dict_stack[-1][0] >= len_white:
                    dict_stack.pop()

                top_level_dict = ret_dict.setdefault(top_level, {})
                dict_stack.append((len_white, top_level_dict,))
                if 'service_group' in m.groupdict():
                    top_level_dict['service_group'] = int(m.groupdict()['service_group'])
                continue

            # Port-channel1: Service Group 1
            m = p1_1.match(line)
            if m:

                # check if previous dict on stack is more deeply nested than the current item
                while dict_stack[-1][0] >= len_white:
                    dict_stack.pop()

                top_level = m.groupdict()['top_level']
                service_group = int(m.groupdict()['service_group'])
                top_level_dict = ret_dict.setdefault(top_level, {})
                dict_stack.append((len_white, top_level_dict,))
                top_level_dict['service_group'] = service_group
                continue

            # Service-policy input: Control_Plane_In
            # Service-policy output: Control_Plane_Out
            m = p2.match(line)
            if m:
                try:
                    top_level_dict
                except UnboundLocalError:
                    top_level_dict = ret_dict.setdefault(interface, {})
                    dict_stack.append((len_white, top_level_dict,))

                service_policy = m.groupdict()['service_policy']
                policy_name = m.groupdict()['policy_name']
                
                while dict_stack[-1][0] >= len_white:
                    dict_stack.pop()

                service_policy_dict = top_level_dict.setdefault('service_policy', {}).setdefault(service_policy, {})
                dict_stack.append((len_white, service_policy_dict,))
                policy_dict = service_policy_dict.setdefault('policy_name', {}).setdefault(policy_name, {})
                dict_stack.append((len_white, policy_dict,))
                continue

            # Service policy : child
            m = p2_1.match(line)
            if m:

                child_policy = m.groupdict()['policy_name']
                while dict_stack[-1][0] >= len_white:
                    dict_stack.pop()
                
                class_map_dict = dict_stack[-1][1]
                child_dict = class_map_dict.setdefault('child_policy_name', {}).setdefault(child_policy, {})
                dict_stack.append((len_white, child_dict,))
                continue
            
            # Class-map: Ping_Class (match-all)
            # Class-map:TEST (match-all)
            # Class-map: TEST-OTTAWA_CANADA#PYATS (match-any)
            m = p3.match(line)
            if m:
                
                match_list = []
                class_line_type = None
                queue_stats = 0
                class_map = m.groupdict()['class_map']
                class_match = m.groupdict()['match_all'].replace('(', '').replace(')', '')

                
                while dict_stack[-1][0] >= len_white:
                    dict_stack.pop()

                # add class_map to whatever dict is on the stack.
                class_dict = dict_stack[-1][1].setdefault('class_map', {}).setdefault(class_map, {})
                dict_stack.append((len_white, class_dict,))
                class_dict['match_evaluation'] = class_match
                continue
            
            # queue stats for all priority classes:
            m = p3_1.match(line)
            if m:

                queue_stats = 1
                while dict_stack[-1][0] >= len_white:
                    dict_stack.pop()

                queue_dict = policy_dict.setdefault('queue_stats_for_all_priority_classes', {})
                dict_stack.append((len_white, queue_dict,))
                continue

            # priority level 2
            m = p3_1_1.match(line)
            if m:

                while dict_stack[-1][0] >= len_white:
                    dict_stack.pop()

                priority_level_status = True
                priority_level = m.groupdict()['priority_level']
                priority_dict = queue_dict.setdefault('priority_level', {}).setdefault(priority_level, {})
                priority_dict['queueing'] = queueing_val
                continue

            # 8 packets, 800 bytes
            m = p4.match(line)
            if m:
                
                pkts = m.groupdict()['packets']
                byte = m.groupdict()['bytes']
                class_dict.setdefault('packets', int(pkts))
                class_dict.setdefault('bytes', int(byte))
                continue

            # 8 packets
            m = p4_1.match(line)
            if m:

                pkts = m.groupdict()['packets']
                class_dict.setdefault('packets', int(pkts))
                continue

            # 5 minute offered rate 0000 bps, drop rate 0000 bps
            m = p5.match(line)
            if m:

                rate_dict = class_dict.setdefault('rate', {})
                dict_stack.append((len_white, rate_dict,))

                rate_dict['interval'] = int(m.groupdict()['interval']) * 60
                rate_dict['offered_rate_bps'] = int(m.groupdict()['offered_rate'])
                rate_dict['drop_rate_bps'] = int(m.groupdict()['drop_rate'])
                continue

            # 5 minute offered rate 0000 bps
            m = p5_1.match(line)
            if m:

                rate_dict = class_dict.setdefault('rate', {})
                dict_stack.append((len_white, rate_dict,))
                rate_dict['interval'] = int(m.groupdict()['interval']) * 60
                rate_dict['offered_rate_bps'] = int(m.groupdict()['offered_rate'])
                continue

            # 30 second offered rate 15000 bps, drop rate 300 bps
            m = p5_2.match(line)
            if m:

                rate_dict = class_dict.setdefault('rate', {})
                dict_stack.append((len_white, rate_dict,))
                rate_dict['interval'] = int(m.groupdict()['interval'])
                rate_dict['offered_rate_bps'] = int(m.groupdict()['offered_rate'])
                rate_dict['drop_rate_bps'] = int(m.groupdict()['drop_rate'])
                continue

            # Match: access-group name Ping_Option
            # Match: access-group name PYATS-MARKING_IN#CUSTOM__ACL

            m = p6.match(line)
            if m:

                # check if previous dict on stack is more deeply nested than the current item
                while dict_stack[-1][0] >= len_white:
                    dict_stack.pop()

                match_list.append(m.groupdict()['match'])
                class_dict.setdefault('match', match_list)
                continue
            
            # police:
            m = p7.match(line)
            if m:

                police_dict = class_dict.setdefault('police', {})
                dict_stack.append((len_white, police_dict,))
                continue

            # police:  cir 64000 bps, bc 8000 bytes
            m = p7_1.match(line)
            if m:

                police_dict = class_dict.setdefault('police', {})
                dict_stack.append((len_white, police_dict,))
                police_dict['cir_bps'] = int(m.groupdict()['cir_bps'])
                police_dict['cir_bc_bytes'] = int(m.groupdict()['cir_bc_bytes'])
                continue

            # cir 8000 bps, bc 1500 bytes
            m = p8.match(line)
            if m:

                police_dict['cir_bps'] = int(m.groupdict()['cir_bps'])
                police_dict['cir_bc_bytes'] = int(m.groupdict()['cir_bc_bytes'])
                continue

            # 8000 bps, 1500 limit, 1500 extended limit
            m = p8_1.match(line)
            if m:
                police_dict['police_bps'] = int(m.groupdict()['police_bps'])
                police_dict['police_limit'] = int(m.groupdict()['police_limit'])
                police_dict['extended_limit'] = int(m.groupdict()['extended_limit'])
                continue
            
            # cir 10000000 bps, be 312500 bytes
            m = p8_2.match(line)
            if m:
                police_dict['cir_bps'] = int(m.groupdict()['cir_bps'])
                police_dict['cir_be_bytes'] = int(m.groupdict()['cir_be_bytes'])
                continue

            # pir 20000 bps, be 658 bytes
            m = p8_3.match(line)
            if m:
                police_dict['pir_bps'] = int(m.groupdict()['pir_bps'])
                police_dict['pir_be_bytes'] = int(m.groupdict()['pir_be_bytes'])
                continue

            # pir 20000 bps, bc 658 bytes
            m = p8_4.match(line)
            if m:
                police_dict['pir_bps'] = int(m.groupdict()['pir_bps'])
                police_dict['pir_bc_bytes'] = int(m.groupdict()['pir_bc_bytes'])
                continue
            
            # cir 10000000000 bps, bc 30000000 bytes, be 60000000 bytes
            m = p8_5.match(line)
            if m:
                police_dict['cir_bps'] = int(m.groupdict()['cir_bps'])
                police_dict['pir_bc_bytes'] = int(m.groupdict()['pir_bc_bytes'])
                police_dict['cir_be_bytes'] = int(m.groupdict()['cir_be_bytes'])
                continue

            # conformed 8 packets, 800 bytes; actions:
            m = p9.match(line)
            if m:

                while dict_stack[-1][0] >= len_white:
                    dict_stack.pop()

                conformed_line = True
                exceeded_line = False
                violated_line = False
                conformed_dict = police_dict.setdefault('conformed', {})
                dict_stack.append((len_white, conformed_dict,))
                conformed_dict['packets'] = int(m.groupdict()['packets'])
                conformed_dict['bytes'] = int(m.groupdict()['bytes'])
                conf_action_dict = conformed_dict.setdefault('actions', {})
                dict_stack.append((len_white, conf_action_dict,))
                continue

            # conformed 0 bytes; actions:
            m = p9_0.match(line)
            if m:
                while dict_stack[-1][0] >= len_white:
                    dict_stack.pop()

                conformed_line = True
                exceeded_line = False
                violated_line = False
                conformed_dict = police_dict.setdefault('conformed', {})
                dict_stack.append((len_white, conformed_dict,))
                conformed_dict['bytes'] = int(m.groupdict()['bytes'])
                conf_action_dict = conformed_dict.setdefault('actions', {})
                dict_stack.append((len_white, conf_action_dict,))
                continue

            # conformed 15 packets, 6210 bytes; action:transmit
            m = p9_1.match(line)
            if m:
                while dict_stack[-1][0] >= len_white:
                    dict_stack.pop()
                conformed_dict = police_dict.setdefault('conformed', {})
                dict_stack.append((len_white, conformed_dict,))
                conformed_dict['packets'] = int(m.groupdict()['packets'])
                conformed_dict['bytes'] = int(m.groupdict()['bytes'])
                conf_action_dict = conformed_dict.setdefault('actions', {})
                dict_stack.append((len_white, conf_action_dict,))
                action = m.groupdict()['action']
                conf_action_dict.update({action: True})
                continue

            # exceeded 0 packets, 0 bytes; actions:
            m = p10.match(line)
            if m:
            
                while dict_stack[-1][0] >= len_white:
                    dict_stack.pop()

                conformed_line = False
                violated_line = False
                exceeded_line = True
                exceeded_dict = police_dict.setdefault('exceeded', {})
                exceeded_dict['packets'] = int(m.groupdict()['packets'])
                exceeded_dict['bytes'] = int(m.groupdict()['bytes'])
                exc_action_dict = exceeded_dict.setdefault('actions', {})
                continue

            # exceeded 0 bytes; actions:
            m = p10_0.match(line)
            if m:
                conformed_line = False
                violated_line = False
                exceeded_line = True
                exceeded_dict = police_dict.setdefault('exceeded', {})
                exceeded_dict['bytes'] = int(m.groupdict()['bytes'])
                exc_action_dict = exceeded_dict.setdefault('actions', {})
                continue

            # exceeded 5 packets, 5070 bytes; action:drop
            m = p10_1.match(line)
            if m:
                exceeded_dict = police_dict.setdefault('exceeded', {})
                exceeded_dict['packets'] = int(m.groupdict()['packets'])
                exceeded_dict['bytes'] = int(m.groupdict()['bytes'])
                exc_action_dict = exceeded_dict.setdefault('actions', {})
                action = m.groupdict()['action']
                exc_action_dict.update({action: True})
                continue

            # violated 0 packets, 0 bytes; action:drop
            m = p11.match(line)
            if m:
                violated_dict = police_dict.setdefault('violated', {})
                violated_dict['packets'] = int(m.groupdict()['packets'])
                violated_dict['bytes'] = int(m.groupdict()['bytes'])
                viol_action_dict = violated_dict.setdefault('actions', {})
                action = m.groupdict()['action']
                viol_action_dict.update({action: True})
                continue

            # violated 0 packets, 0 bytes; actions:
            m = p11_1.match(line)
            if m:
                conformed_line = False
                exceeded_line = False
                violated_line = True
                violated_dict = police_dict.setdefault('violated', {})
                violated_dict['packets'] = int(m.groupdict()['packets'])
                violated_dict['bytes'] = int(m.groupdict()['bytes'])
                viol_action_dict = violated_dict.setdefault('actions', {})
                continue

            #violated 0 bytes; actions:
            m = p11_2.match(line)
            if m:
                violated_dict = police_dict.setdefault('violated', {})
                violated_dict['bytes'] = int(m.groupdict()['bytes'])
                viol_action_dict = violated_dict.setdefault('actions', {})
                continue

            # conformed 0000 bps, exceeded 0000 bps
            m = p12.match(line)
            if m:
                conformed_dict['bps'] = int(m.groupdict()['c_bps'])
                exceeded_dict['bps'] = int(m.groupdict()['e_bps'])
                continue

            # conformed 0 bps, exceed 0 bps, violate 0 bps
            m = p12_1.match(line)
            if m:
                conformed_dict['bps'] = int(m.groupdict()['c_bps'])
                exceeded_dict['bps'] = int(m.groupdict()['e_bps'])
                violated_dict['bps'] = int(m.groupdict()['v_bps'])
                continue

            # QoS Set
            m = p14.match(line)
            if m:
                qos_dict = class_dict.setdefault('qos_set', {})
                continue

            # ip precedence 6
            # cos 5
            m = p14_1.match(line) or p41.match(line)
            if m:

                while dict_stack[-1][0] >= len_white:
                    dict_stack.pop()

                group = m.groupdict()
                key = group['key'].strip()
                value = group['value'].strip()
                qos_dict_map = qos_dict.setdefault(key, {}).setdefault(value, {})
                continue

            # Marker statistics: Disabled
            m = p14_2.match(line)
            if m:
                qos_dict_map['marker_statistics'] = m.groupdict()['marker_statistics']
                continue

            # Packets marked 500
            m = p14_3.match(line)
            if m:
                qos_dict_map['packets_marked'] = int(m.groupdict()['packets_marked'])
                continue
            
            # mpls experimental imposition 1
            m = p14_4.match(line)
            if m:
                qos_dict['mpls_experimental_imposition'] = int(m.groupdict()['value'])
                continue
            
            # drop
            # transmit
            # start
            # set-qos-transmit 7
            # set-mpls-exp-imposition-transmit 7
            m = p13.match(line)
            if m:
                action = m.groupdict()['action'].replace('-', '_')
                if action in self.BOOL_ACTION_LIST:
                    value = True
                else:
                    value = m.groupdict()['value']
                try:
                    if conformed_line:
                        conf_action_dict.update({action: value})
                    elif exceeded_line:
                        exc_action_dict.update({action: value})
                    elif violated_line:
                        viol_action_dict.update({action: value})
                    continue
                except Exception as e:
                    pass

            # Queueing
            m = p15.match(line)
            if m:
                if queue_stats == 1:
                    queueing_val = True
                    # priority_dict['queueing'] = True
                else:
                    class_dict['queueing'] = True
                continue

            # queue size 0, queue limit 4068
            m = p16.match(line)
            if m:
                class_dict['queue_size'] = int(m.groupdict()['queue_size'])
                class_dict['queue_limit'] = int(m.groupdict()['queue_limit'])
                continue

            # queue limit 64 packets
            m = p17.match(line)
            if m:
                if queue_stats == 1:
                    if not priority_level_status:
                        priority_dict = dict_stack[-1][1].setdefault('priority_level',
                                                                     {}).setdefault('default', {})
                        priority_dict['queueing'] = queueing_val
                    priority_dict['queue_limit_packets'] = m.groupdict()['queue_limit']
                else:
                    class_dict['queue_limit_packets'] = m.groupdict()['queue_limit']
                continue

            # queue limit 62500 bytes
            m = p17_1.match(line)
            if m:
                class_dict['queue_limit_bytes'] = int(m.groupdict()['queue_limit_bytes'])
                continue

            # (queue depth/total drops/no-buffer drops) 0/0/0
            m = p18.match(line)
            if m:
                if queue_stats == 1:
                    if not priority_dict:
                        priority_dict = dict_stack[-1][1].setdefault('priority_level',
                                                                     {}).setdefault('default', {})
                    priority_dict['queue_depth'] = int(m.groupdict()['queue_depth'])
                    priority_dict['total_drops'] = int(m.groupdict()['total_drops'])
                    priority_dict['no_buffer_drops'] = int(m.groupdict()['no_buffer_drops'])

                else:
                    class_dict['queue_depth'] = int(m.groupdict()['queue_depth'])
                    class_dict['total_drops'] = int(m.groupdict()['total_drops'])
                    class_dict['no_buffer_drops'] = int(m.groupdict()['no_buffer_drops'])
                continue

            # depth/total drops/no-buffer drops) 147/38/0
            m = p18_1.match(line)
            if m:
                class_dict['queue_depth'] = int(m.groupdict()['queue_depth'])
                class_dict['total_drops'] = int(m.groupdict()['total_drops'])
                class_dict['no_buffer_drops'] = int(m.groupdict()['no_buffer_drops'])
                continue

            # (pkts output/bytes output) 0/0
            m = p19.match(line)
            if m:
                if queue_stats == 1:
                    priority_dict['pkts_output'] = int(m.groupdict()['pkts_output'])
                    priority_dict['bytes_output'] = int(m.groupdict()['bytes_output'])
                else:
                    class_dict['pkts_output'] = int(m.groupdict()['pkts_output'])
                    class_dict['bytes_output'] = int(m.groupdict()['bytes_output'])
                continue

            # (pkts matched/bytes matched) 363/87120
            m = p19_0.match(line)
            if m:
                class_dict['pkts_matched'] = int(m.groupdict()['pkts_matched'])
                class_dict['bytes_matched'] = int(m.groupdict()['bytes_matched'])
                continue

            # (pkts queued/bytes queued) 0/0
            m = p19_1.match(line)
            if m:
                class_dict['pkts_queued'] = int(m.groupdict()['pkts_queued'])
                class_dict['bytes_queued'] = int(m.groupdict()['bytes_queued'])
                continue

            # shape (average) cir 474656, bc 1899, be 1899
            m = p20.match(line)
            if m:
                class_dict['shape_type'] = m.groupdict()['shape_type']
                class_dict['shape_cir_bps'] = int(m.groupdict()['shape_cir_bps'])
                class_dict['shape_bc_bps'] = int(m.groupdict()['shape_bc_bps'])
                class_dict['shape_be_bps'] = int(m.groupdict()['shape_be_bps'])
                continue

            # target shape rate 474656
            m = p21.match(line)
            if m:
                class_dict['target_shape_rate'] = int(m.groupdict()['target_shape_rate'])
                continue

            # Output Queue: Conversation 266
            m = p22.match(line)
            if m:
                class_dict['output_queue'] = m.groupdict()['output_queue']
                continue

            # Bandwidth 10 (%)
            m = p23.match(line)
            if m:
                class_dict['bandwidth_percent'] = int(m.groupdict()['bandwidth'])
                continue

            # bandwidth 1000 (kbps)
            m = p24.match(line)
            if m:
                class_dict['bandwidth_kbps'] = int(m.groupdict()['bandwidth_kbps'])
                continue

            # bandwidth 1000 (kbps)
            m = p24_1.match(line)
            if m:
                class_dict['bandwidth_percent'] = int(m.groupdict()['bandwidth_percent'])
                class_dict['bandwidth_kbps'] = int(m.groupdict()['bandwidth_kbps'])
                continue

            # exponential weight: 9
            m = p25.match(line)
            if m:
                group = m.groupdict()
                key = group['key'].strip()
                value = group['value'].strip()
                random_detect_dict = class_dict.setdefault('random_detect', {})
                if key.startswith('exponential'):
                    random_detect_dict['exponential_weight'] = value
                else:
                    random_detect_dict['exp_weight_constant'] = value
                continue

            # mean queue depth: 25920
            # Mean queue depth: 0 bytes
            m = p26.match(line)
            if m:
                random_detect_dict['mean_queue_depth'] = int(m.groupdict()['mean_queue_depth'])
                continue

            # class     Transmitted       Random drop      Tail drop     Minimum Maximum Mark
            m = p27_1.match(line)
            if m:
                class_line_type = 1
                continue

            # Class Random       Tail    Minimum    Maximum     Mark      Output
            m = p27_2.match(line)
            if m:
                class_line_type = 2
                continue

            # class     Transmitted       Random drop      Tail drop     Minimum Maximum Mark
            #           pkts/bytes        pkts/bytes       pkts/bytes    thresh  thresh  prob
            #                                                            (bytes)  (bytes)
            #   0             0/0               0/0               0/0      20000    40000  1/10
            #   1           328/78720          38/9120            0/0      22000    40000  1/10
            #   2             0/0               0/0               0/0      24000    40000  1/10
            #   3             0/0               0/0               0/0      26000    40000  1/10
            #   4             0/0               0/0               0/0      28000    40000  1/10
            m = p27.match(line)
            if m:
                if class_line_type == 1:
                    value1_pkts = 'transmitted_packets'
                    value1_bytes = 'transmitted_bytes'
                    value2_pkts = 'random_drop_packets'
                    value2_bytes = 'random_drop_bytes'
                    value3_pkts = 'tail_drop_packets'
                    value3_bytes = 'tail_drop_bytes'
                    value4 = 'minimum_thresh'
                    value5 = 'maximum_thresh'
                    value6 = 'mark_prob'
                elif class_line_type == 2:
                    value1 = 'random_drop'
                    value2 = 'tail_drop'
                    value3 = 'minimum_thresh'
                    value4 = 'maximum_thresh'
                    value5 = 'mark_prob'
                    value6 = 'output'
                else:
                    continue
                group = m.groupdict()
                class_val = group['class']
                class_random_dict = random_detect_dict.setdefault('class', {}).\
                                            setdefault(class_val, {})
                class_random_dict[value1_pkts] = group['value1_pkts']
                class_random_dict[value1_bytes] = group['value1_bytes']
                class_random_dict[value2_pkts] = group['value2_pkts']
                class_random_dict[value2_bytes] = group['value2_bytes']
                class_random_dict[value3_pkts] = group['value3_pkts']
                class_random_dict[value3_bytes] = group['value3_bytes']
                class_random_dict[value4] = group['value4']
                class_random_dict[value5] = group['value5']
                class_random_dict[value6] = group['value6']
                continue

            # policy wred-policy
            m = p28.match(line)
            if m:
                policy = m.groupdict()['policy']
                policy_dict = class_dict.setdefault('policy', {}).\
                                         setdefault(policy, {})
                continue

            # class prec2
            m = p29.match(line)
            if m:
                precedence_list,bytes1_list,bytes2_list,bytes3_list = ([] for _ in range(4))
                class_value = m.groupdict()['class']
                class_dictionary = policy_dict.setdefault('class', {}).\
                                               setdefault(class_value, {})
                continue

            # bandwidth 1000
            m = p30.match(line)
            if m:
                class_dictionary['bandwidth'] = int(m.groupdict()['bandwidth'])
                continue

            # bandwidth remaining ratio 1
            m = p31.match(line)
            if m:
                class_dict['bandwidth_remaining_ratio'] = int(m.groupdict()['bandwidth_remaining_ratio'])
                continue

            # bandwidth:class-based wfq, weight 25
            m = p32.match(line)
            if m:
                class_dict['bandwidth'] = m.groupdict()['bandwidth']
                continue

            # random-detect
            m = p33.match(line)
            if m:
                random_dict = class_dictionary.setdefault('random_detect', {})
                continue

            # random-detect precedence 2 100 bytes 200 bytes 10
            m = p33_1.match(line)
            if m:
                precedence_list.append(int(m.groupdict()['precedence']))
                bytes1_list.append(int(m.groupdict()['bytes1']))
                bytes2_list.append(int(m.groupdict()['bytes2']))
                bytes3_list.append(int(m.groupdict()['bytes3']))
                random_dict['precedence'] = precedence_list
                random_dict['bytes1'] = bytes1_list
                random_dict['bytes2'] = bytes2_list
                random_dict['bytes3'] = bytes3_list
                continue

            # packet output 90, packet drop 0
            m = p34.match(line)
            if m:
                class_dict['packet_output'] = int(m.groupdict()['packet_output'])
                class_dict['packet_drop'] = int(m.groupdict()['packet_drop'])
                continue

            # tail/random drop 0, no buffer drop 0, other drop 0
            m = p35.match(line)
            if m:
                class_dict['tail_random_drops'] = int(m.groupdict()['tail_random_drops'])
                class_dict['no_buffer_drops'] = int(m.groupdict()['no_buffer_drops'])
                class_dict['other_drops'] = int(m.groupdict()['other_drops'])
                continue

            # queue limit 1966 us/ 49152 bytes
            m = p36.match(line)
            if m:
                if queue_stats == 1 :
                    priority_dict['queue_limit_us'] = int(m.groupdict()['queue_limit_us'])
                    priority_dict['queue_limit_bytes'] = int(m.groupdict()['queue_limit_bytes'])
                else:
                    class_dict['queue_limit_us'] = int(m.groupdict()['queue_limit_us'])
                    class_dict['queue_limit_bytes'] = int(m.groupdict()['queue_limit_bytes'])
                continue

            # Priority: 10% (100000 kbps), burst bytes 2500000, b/w exceed drops: 44577300
            m = p37.match(line)
            if m:
                pri_dict = class_dict.setdefault('priority', {})
                pri_dict['percent'] = int(m.groupdict()['percent'])
                pri_dict['kbps'] = int(m.groupdict()['kbps'])
                pri_dict['burst_bytes'] = int(m.groupdict()['burst_bytes'])
                if m.group('exceed_drops'):
                    pri_dict['exceed_drops'] = int(m.groupdict()['exceed_drops'])
                continue

            # Priority Level: 1
            m = p38.match(line)
            if m:
                class_dict['priority_level'] = int(m.groupdict()['priority_level'])
                continue

            # bandwidth remaining 70%
            m = p39.match(line)
            if m:
                class_dict['bandwidth_remaining_percent'] = int(m.groupdict()['bandwidth_remaining_percent'])
                continue

            # Priority: Strict, b/w exceed drops: 0
            m = p40.match(line)
            if m:
                pri_dict = class_dict.setdefault('priority', {})
                pri_dict['type'] = m.groupdict()['type']
                pri_dict['exceed_drops'] = int(m.groupdict()['exceed_drops'])
                continue

            # Virtual Class   min/max        Transmit                     Random drop                 AFD Weight
            # 0          10 / 20        (Byte)33459183360             27374016                     12
            m = p42.match(line)
            if m:
                afd_wred_dict = class_dict.setdefault('afd_wred_stats', {})
                afc_wred_vc_dict = afd_wred_dict.setdefault('virtual_class', {}).setdefault(int(m.groupdict()['virtual_class']), {})
                afc_wred_vc_dict['min'] = int(m.groupdict()['min'])
                afc_wred_vc_dict['max'] = int(m.groupdict()['max'])
                afc_wred_vc_dict['transmit_bytes'] = int(m.groupdict()['tx_bytes'])
                afc_wred_vc_dict['random_drop_bytes'] = int(m.groupdict()['random_drop_bytes'])
                afc_wred_vc_dict['afd_weight'] = int(m.groupdict()['afd_weight'])
                continue

            # (Pkts)68692637637             0
            m = p43.match(line)
            if m:
                afc_wred_vc_dict['transmit_packets'] = int(m.groupdict()['tx_packets'])
                afc_wred_vc_dict['random_drop_packets'] = int(m.groupdict()['random_drop_packets'])
                continue

            # dscp : 1
            m = p44.match(line)
            if m:
                afc_wred_vc_dict['dscp'] = int(m.groupdict()['dscp'])
                continue

            # Total Drops(Bytes)   : 0
            m = p45.match(line)
            if m:
                afd_wred_dict['total_drops_bytes'] = int(m.groupdict()['total_drops_bytes'])
                continue

            # Total Drops(Packets) : 0
            m = p46.match(line)
            if m:
                afd_wred_dict['total_drops_packets'] = int(m.groupdict()['total_drops_packets'])
                continue
            
            # (total drops) 0
            m = p47.match(line)
            if m:
                if queue_stats == 1:
                    priority_dict['total_drops'] = int(m.groupdict()['total_drops'])
                else:
                    class_dict['total_drops'] = int(m.groupdict()['total_drops'])
                continue
            
            # (bytes output) 0
            m = p48.match(line)
            if m:
                if queue_stats == 1:
                    priority_dict['bytes_output'] = int(m.groupdict()['bytes_output'])
                else:
                    class_dict['bytes_output'] = int(m.groupdict()['bytes_output'])
                continue

            # Overhead Accounting Enabled
            m = p49.match(line)
            if m:
                class_dict['overhead_accounting'] = m.groupdict()['enabled']
            
            # Fair-queue: per-flow queue limit 128 packets
            m = p50.match(line)
            if m:
                class_dict['fair_queue_limit_per_flow'] = int(m.groupdict()['queue_limit'])

        
        return ret_dict


# ===================================
# Parser for:
#   * 'show policy-map control-plane'
# ===================================
class ShowPolicyMapControlPlane(ShowPolicyMapTypeSuperParser, ShowPolicyMapTypeSchema):
    
    ''' Parser for:
        * 'show policy-map control-plane'
    '''

    cli_command = ['show policy-map control-plane']

    def cli(self, output=None):

        if output is None:
            # Build command
            cmd = self.cli_command[0]
            # Execute command
            show_output = self.device.execute(cmd)
        else:
            show_output = output

        # Call super
        return super().cli(output=show_output)


# ===========================================
# Parser for:
#   * 'show policy-map interface {interface}'
#   * 'show policy-map interface'
# ===========================================
class ShowPolicyMapInterface(ShowPolicyMapTypeSuperParser, ShowPolicyMapTypeSchema):
    
    ''' Parser for:
        * 'show policy-map interface {interface}'
        * 'show policy-map interface'
    '''

    cli_command = ['show policy-map interface {interface}',
                   'show policy-map interface',
                   ]

    def cli(self, interface='', output=None):

        if output is None:
            # Build command
            if interface:
                cmd = self.cli_command[0].format(interface=interface)
            else:
                cmd = self.cli_command[1]
            # Execute command
            show_output = self.device.execute(cmd)
        else:
            show_output = output

        # Call super
        return super().cli(output=show_output)


# =====================================================================
# Parser for:
#   * 'show policy-map interface {interface} input class {class_name}'
#   * 'show policy-map interface {interface} input'
# =====================================================================
class ShowPolicyMapInterfaceInput(ShowPolicyMapTypeSuperParser, ShowPolicyMapTypeSchema):
    
    ''' Parser for:
        * 'show policy-map interface {interface} input class {class_name}'
        * 'show policy-map interface {interface} input'
    '''
    cli_command = ['show policy-map interface {interface} input class {class_name}',
                   'show policy-map interface {interface} input'
                   ]

    def cli(self, interface='', class_name='', output=None):

        if output is None:
            # Build command
            if interface and class_name:
                cmd = self.cli_command[0].format(interface=interface, class_name=class_name)
            else:
                cmd = self.cli_command[1].format(interface=interface)
            # Execute command
            show_output = self.device.execute(cmd)
        else:
            show_output = output

        # Call super
        return super().cli(output=show_output, interface=interface, class_name=class_name)


# =====================================================================
# Parser for:
#   * 'show policy-map interface {interface} output class {class_name}'
#   * 'show policy-map interface {interface} output'
# =====================================================================
class ShowPolicyMapInterfaceOutput(ShowPolicyMapTypeSuperParser, ShowPolicyMapTypeSchema):
    
    ''' Parser for:
        * 'show policy-map interface {interface} output class {class_name}'
        * 'show policy-map interface {interface} output'
    '''

    cli_command = ['show policy-map interface {interface} output class {class_name}',
                   'show policy-map interface {interface} output'
                   ]

    def cli(self, interface, class_name='', output=None):

        if output is None:
            # Build command
            if interface and class_name:
                cmd = self.cli_command[0].format(interface=interface, class_name=class_name)
            else:
                cmd = self.cli_command[1].format(interface=interface)
            # Execute command
            show_output = self.device.execute(cmd)
        else:
            show_output = output

        # Call super
        return super().cli(output=show_output, interface=interface, class_name=class_name)


# ================================================================
# Parser for:
#   * 'show policy-map interface class {class_name}'
# ================================================================
class ShowPolicyMapInterfaceClass(ShowPolicyMapTypeSuperParser, ShowPolicyMapTypeSchema):
    
    ''' Parser for:
        * 'show policy-map interface class {class_name}'
    '''

    cli_command = ['show policy-map interface class {class_name}',
                   ]

    def cli(self, class_name, output=None):

        if output is None:
            # Build command
            
            cmd = self.cli_command[0].format(class_name=class_name)
            # Execute command
            show_output = self.device.execute(cmd)
        else:
            show_output = output

        # Call super
        return super().cli(output=show_output,class_name=class_name)


# ==============================================================
# Parser for:
#   * 'show policy-map target service-group {num}'
# ==============================================================
class ShowPolicyMapTargetClass(ShowPolicyMapTypeSuperParser, ShowPolicyMapTypeSchema):
    ''' Parser for:
        * 'show policy-map target service-group {num}'
    '''

    cli_command = ['show policy-map target service-group {num}']

    def cli(self, num='', output=None):

        if output is None:
            # Build command
            if num :
                cmd = self.cli_command[0].format(num=num)
            # Execute command
            show_output = self.device.execute(cmd)
        else:
            show_output = output

        # Call super
        return super().cli(output=show_output, num=num)


# ===================================
# Schema for:
#   * 'show policy-map'
#   * 'show policy-map {name}'
# ===================================
class ShowPolicyMapSchema(MetaParser):

    schema = {
        'policy_map': {
            Any(): {
                Optional('class'): {
                    Any(): {
                        Optional('priority_level'): {
                            Any(): {
                                'kbps': int}},
                        Optional('police'): {
                            Optional('rate_pps'): int,
                            Optional('cir_bps'): int,
                            Optional('cir_bc_bytes'): int,
                            Optional('cir_be_bytes'): int,
                            Optional('conform_color'): str,
                            Optional('conform_action'): list,
                            Optional('exceed_action'): list,
                            Optional('violate_action'): list,
                            Optional('service_policy'): str,
                            Optional('conform_burst'): int,
                            Optional('pir'): int,
                            Optional('pir_bc_bytes'): int,
                            Optional('pir_be_bytes'): int,
                            Optional('peak_burst'): int,
                            Optional('cir_percent'): int,
                            Optional('rate_percent'): int,
                            Optional('bc_ms'): int,
                            Optional('pir_percent'): int,
                            Optional('be_ms'): int,
                            },
                        Optional('queue_limit_ms'): int,
                        Optional('queue_limit_packets'): int,
                        Optional('service_policy'): str,
                        Optional('bandwidth_kbps'): int,
                        Optional('bandwidth'): int,
                        Optional('bandwidth_remaining_percent'): int,
                        Optional('bandwidth_remaining_ratio'): int,
                        Optional('shape_average_min'): int,
                        Optional('set'): str,
                        Optional('conform_burst'): int,
                        Optional('priority'): bool,
                        Optional('priority_kbps'): int,
                        Optional('priority_levels'): int,
                        Optional('peak_burst'): int,
                        Optional('average_rate_traffic_shaping'): bool,
                        Optional('adaptive_rate_traffic_shaping'): bool,
                        Optional('cir_percent'): int,
                        Optional('bc_msec'): int,
                        Optional('be_msec'): int,
                        Optional('be_bits'): int,
                        Optional('bc_bits'): int,
                        Optional('cir_bps'): int,
                        Optional('cir_upper_bound_bps'): int,
                        Optional('cir_lower_bound_bps'): int,
                        Optional('random_detect'): {
                            Optional('exponential_weight'): int,
                            Optional('bandwidth_percent'): int,
                            Optional('wred_type'): str,
                            Optional('class_val'): {
                                Any(): {
                                    'min_threshold': str,
                                    'max_threshold': str,
                                    'mark_probability': str,
                                },
                            },
                        },
                        Optional('weighted_fair_queueing'): {
                            'bandwidth_percent': int,
                            'exponential_weight': int,
                            'explicit_congestion_notification': bool,
                            'class_val': {
                                Any(): {
                                    'min_threshold': str,
                                    'max_threshold': str,
                                    'mark_probability': str,
                                    },
                                },
                            },
                        },
                    },
                },
            },
        }



# ===================================
# Parser for:
#   * 'show policy-map'
#   * 'show policy-map {name}'
# ===================================
class ShowPolicyMap(ShowPolicyMapSchema):
    
    ''' Parser for
        * "show policy-map"
        * "show policy-map {name}"
    '''

    cli_command = ['show policy-map {name}', 'show policy-map']

    def cli(self, name='', output=None):
        if output is None:
            if name and (name != 'interface') and (name != 'control-plane'):
                cmd = self.cli_command[0].format(name=name)
            else:
                cmd = self.cli_command[1]
            # Execute command on device
            out = self.device.execute(cmd)
        else:
            out = output

        # Init vars
        ret_dict = {}
        police_line = 0
        weight_line = None

        unit_dict = {'%': 'percent',
                     'bits': 'bits',
                     'bps': 'bps',
                     'b/s': 'bps',
                     'bytes': 'bytes',
                     'kbps': 'kbps',
                     'kb/s': 'kbps',
                     'msec': 'msec'}

        # Policy Map police-in
        # Policy Map policy_4-6-3~6
        # Policy-map egress policy
        p1 = re.compile(r'^Policy(\-map| Map) +(?P<policy_map>([\S\s]+))$')
        
        # Class class-default
        # Class class c1
        # Class class_4-6-3
        p2 = re.compile(r'^Class +(?P<class_map>([\S\s]+))$')

        # police 8000 9216 0
        p2_0 = re.compile(r'^police +(?P<cir_bps>(\d+)) +(?P<cir_bc_bytes>(\d+)) +(?P<cir_be_bytes>(\d+))$')

        # police cir percent 20 bc 300 ms pir percent 40 be 400 ms
        p2_1 = re.compile(r'^police +cir +percent +(?P<cir_percent>(\d+)) +bc +(?P<bc_ms>(\d+)) +ms +pir +percent +'
                           '(?P<pir_percent>(\d+)) +be +(?P<be_ms>(\d+)) ms$')

        # police cir 1000000 bc 31250 pir 2000000 be 31250
        p2_2 = re.compile(r'^police +cir +(?P<cir_bps>(\d+)) +bc +(?P<cir_bc_bytes>(\d+)) +pir +(?P<pir>(\d+)) +be +(?P<pir_be_bytes>(\d+))$')

        # police rate 2000 pps
        p2_3 = re.compile(r'^police +rate +(?P<rate_pps>\d+) +pps$')

        # police rate percent 10
        p2_4 = re.compile(r'^police +rate +percent +(?P<rate_percent>\d+)$')

        # police cir 445500 bc 83619
        p3 = re.compile(r'^police +cir +(?P<cir_bps>(\d+)) +bc +(?P<cir_bc_bytes>(\d+))$')

        # police cir 50000 bc 3000 be 3000
        p3_0 = re.compile(r'^police +cir +(?P<cir_bps>(\d+)) +bc +(?P<cir_bc_bytes>(\d+)) +be +(?P<cir_be_bytes>(\d+))$')

        # conform-action transmit
        p3_1 = re.compile(r'^conform-action +(?P<conform_action>([\w\-\s]+))$')

        # exceed-action drop
        p3_2 = re.compile(r'^exceed-action +(?P<exceed_action>([\w\-\s]+))$')

        # conform-color hipri-conform
        p3_3 = re.compile(r'^conform-color +(?P<conform_color>([\w\-\s]+))$')

        # violate - action drop
        p3_4 = re.compile(r'^violate-action +(?P<violate_action>([\w\-\s]+))$')

        # service-policy child-policy
        p3_5 = re.compile(r'^service-policy +(?P<service_policy>([\w\-\s]+))$')

        # Average Rate Traffic Shaping
        p4 = re.compile(r'^Average +Rate +Traffic +Shaping$')

        # Adaptive Rate Traffic Shaping
        p4_0 = re.compile(r'Adaptive +Rate +Traffic +Shaping$')

        #cir upper-bound 2120000 (bps) cir lower-bound 1120000 (bps)
        p4_1 = re.compile(r'^cir +upper-bound +(?P<cir_upper_bound_bps>(\d+)) \(bps\) +cir +lower-bound +(?P<cir_lower_bound_bps>(\d+)) \(bps\)$')

        # cir 1000000 (bps) bc 10000000 (bits) be 1000000 (bits)
        p5 = re.compile(r'^cir +(?P<cir>(\d+)) *\(?(?P<cir_unit>[\w%]+)\)?( +bc +(?P<bc>(\d+)) +\((?P<bc_unit>\w+)\))?( +be +(?P<be>(\d+)) +\((?P<be_unit>\w+)\))?$')

        # priority level 1 20000 (kb/s)
        p6 = re.compile(r'^priority +level +(?P<pri_level>(\d+)) +(?P<kb_per_sec>(\d+)) \(kb\/s\)$')

        # bandwidth 20000 (kb/s)
        # bandwidth 100
        p7_0 = re.compile(r'^bandwidth +(?P<bandwidth>(\d+))(?: \(kb[p/]s\))?$')

        # Bandwidth 70 (%)
        # bandwidth 80 (%)
        # bandwidth percent 5
        p7 = re.compile(r'^[bB]andwidth(:? percent)? +(?P<bandwidth>(\d+))(?: \(%\))?$')

        # Weighted Fair Queueing
        p8 = re.compile(r'^Weighted +Fair +Queueing$')

        # exponential weight 9
        p8_1 = re.compile(r'^exponential +weight +(?P<exponential_weight>(\d+))$')

        # explicit congestion notification
        p8_2 = re.compile(r'^explicit +congestion +notification$')

        # class    min-threshold    max-threshold    mark-probability
        # ----------------------------------------------------------
        # ----------------------------------------------------------
        # 0        -                -                1/10
        # 1        -                -                1/10
        # 2        -                -                1/10
        # 3        -                -                1/10
        # 4        -                -                1/10
        # 5        -                -                1/10
        # 6        -                -                1/10
        # 7        -                -                1/10
        # rsvp     -                -                1/10
        # default (0)   -                -                1/10

        p8_3 = re.compile(r'^(?P<class_val>(\w+(\s+\(\d+\))?)) +(?P<min_threshold>([\w\-]+)) +(?P<max_threshold>([\w\-]+)) '
                           '+(?P<mark_probability>([0-9]+)/([0-9]+))$')

        # cir 30% bc 10 (msec) be 10 (msec)
        p9 = re.compile(r'^cir +(?P<cir_percent>(\d+))% +bc (?P<bc_msec>(\d+)) \(msec\) +'
                         'be (?P<be_msec>(\d+)) \(msec\)$')

        # priority
        p10 = re.compile(r'^priority( +(?P<priority_kbps>\d+) +\(kbps\))?$')

        # priority level 1
        p10_1 = re.compile(r'^priority +level +(?P<priority_levels>(\d+))$')

        # Set cos 5
        # set dscp cs1
        p11 = re.compile(r'^[sS]et +(?P<set>([\w\s]+))$')

        # Shape average 30m
        p12 = re.compile(r'^Shape +average +(?P<shape_average_min>(\d+))m$')

        # bandwidth 100
        p13 = re.compile(r'^bandwidth +(?P<bandwidth>(\d+))$')

        # bandwidth remaining percent 50
        # bandwidth remaining 80 (%)
        p14 = re.compile(r'^^bandwidth remaining(?: percent)? +(?P<bandwidth_remaining_percent>(\d+))(:? \(%\))?$')

        # bandwidth remaining ratio 100
        p14_1 = re.compile(r'^bandwidth remaining ratio +(?P<bandwidth_remaining_ratio>(\d+))$')

        # police cir 500000 conform-burst 10000 pir 1000000 peak-burst 10000 conform-action transmit exceed-action set-prec-transmit 2 violate-action drop
        p15 = re.compile(r'^police +cir +(?P<cir_bps>(\d+)) +conform-burst +(?P<conform_burst>(\d+)) +'
                          'pir +(?P<pir>(\d+)) +peak-burst +(?P<peak_burst>(\d+)) +conform-action +'
                          '(?P<conform_action>(\w+)) +exceed-action +(?P<exceed_action>([\w\-\s]+)) +'
                          'violate-action +(?P<violate_action>(\w+))$')

        # police percent 5 2 ms 0 ms conform-action transmit exceed-action drop violate-action drop
        p15_1 = re.compile(r'^police +percent +(?P<cir_percent>(\d+)) +(?P<bc_ms>(\d+)) ms +(?P<be_ms>(\d+)) ms +conform-action +(?P<conform_action>(\w+)) '
                            '+exceed-action +(?P<exceed_action>([\w\-\s]+)) +violate-action +(?P<violate_action>(\w+))$')

        # time-based wred, exponential weight 9
        p16 = re.compile(r'^(?P<wred_type>[\w-]+) +wred, +exponential +weight +(?P<exponential_weight>(\d+))$')

        # queue-limit 200 ms
        p17 = re.compile(r'^queue-limit +(?P<queue_limit_ms>(\d+)) ms$')

        # queue-limit 77 packets
        p17_1 = re.compile(r'^queue-limit +(?P<queue_limit_packets>(\d+)) packets$')

        for line in out.splitlines():

            line = line.strip()

            # Policy Map police-in
            m = p1.match(line)
            if m:
                policy_map = m.groupdict()['policy_map']
                policy_map_dict = ret_dict.setdefault('policy_map', {}).setdefault(policy_map, {})
                continue

            # Class class-default
            # Class class c1
            m = p2.match(line)
            if m:
                class_map = m.groupdict()['class_map']
                class_map_dict = policy_map_dict.setdefault('class', {}).setdefault(class_map, {})
                continue

            # police 8000 9216 0
            m = p2_0.match(line)
            if m:
                police_line=1
                conform_list = []
                exceed_list = []
                violate_list = []
                police_dict = class_map_dict.setdefault('police', {})
                police_dict['cir_bps'] = int(m.groupdict()['cir_bps'])
                police_dict['cir_bc_bytes'] = int(m.groupdict()['cir_bc_bytes'])
                police_dict['cir_be_bytes'] = int(m.groupdict()['cir_be_bytes'])
                continue

            #police cir percent 20 bc 300 ms pir percent 40 be 400 ms
            m = p2_1.match(line)
            if m:
                police_line = 1
                conform_list = []
                exceed_list = []
                violate_list = []
                police_dict = class_map_dict.setdefault('police', {})
                police_dict['cir_percent'] = int(m.groupdict()['cir_percent'])
                police_dict['bc_ms'] = int(m.groupdict()['bc_ms'])
                police_dict['pir_percent'] = int(m.groupdict()['pir_percent'])
                police_dict['be_ms'] = int(m.groupdict()['be_ms'])
                continue

            # police cir 1000000 bc 31250 pir 2000000 be 31250
            m = p2_2.match(line)
            if m:
                police_line = 1
                conform_list = []
                exceed_list = []
                violate_list = []
                police_dict = class_map_dict.setdefault('police', {})
                police_dict['cir_bps'] = int(m.groupdict()['cir_bps'])
                police_dict['cir_bc_bytes'] = int(m.groupdict()['cir_bc_bytes'])
                police_dict['pir'] = int(m.groupdict()['pir'])
                police_dict['pir_be_bytes'] = int(m.groupdict()['pir_be_bytes'])
                continue

            # police rate 1800 pps
            m = p2_3.match(line)
            if m:
                police_line = 1
                conform_list = []
                exceed_list = []
                violate_list = []
                police_dict = class_map_dict.setdefault('police', {})
                police_dict['rate_pps'] = int(m.groupdict()['rate_pps'])
                continue

            # police rate percent 10
            m = p2_4.match(line)
            if m:
                police_line = 1
                conform_list = []
                exceed_list = []
                violate_list = []
                police_dict = class_map_dict.setdefault('police', {})
                police_dict['rate_percent'] = int(m.groupdict()['rate_percent'])
                continue

            # police cir 445500 bc 83619
            m = p3.match(line)
            if m:
                police_line = 1
                conform_list = []
                exceed_list = []
                violate_list = []
                police_dict = class_map_dict.setdefault('police', {})
                police_dict['cir_bps'] = int(m.groupdict()['cir_bps'])
                police_dict['cir_bc_bytes'] = int(m.groupdict()['cir_bc_bytes'])
                continue

            # police cir 50000 bc 3000 be 3000
            m = p3_0.match(line)
            if m:
                police_line = 1
                conform_list = []
                exceed_list = []
                violate_list = []
                police_dict = class_map_dict.setdefault('police', {})
                police_dict['cir_bps'] = int(m.groupdict()['cir_bps'])
                police_dict['cir_bc_bytes'] = int(m.groupdict()['cir_bc_bytes'])
                police_dict['cir_be_bytes'] = int(m.groupdict()['cir_be_bytes'])
                continue

            # conform-action transmit
            m = p3_1.match(line)
            if m:
                conform_list.append(m.groupdict()['conform_action'])
                police_dict['conform_action'] = conform_list
                continue

            # exceed-action drop
            m = p3_2.match(line)
            if m:
                exceed_list.append(m.groupdict()['exceed_action'])
                police_dict['exceed_action'] = exceed_list
                continue

            # conform-color hipri-conform
            m = p3_3.match(line)
            if m:
                police_dict['conform_color'] = m.groupdict()['conform_color']
                continue

            # violate - action drop
            m = p3_4.match(line)
            if m:
                violate_list.append(m.groupdict()['violate_action'])
                police_dict['violate_action'] = violate_list
                continue

            # service-policy child-policy
            m = p3_5.match(line)
            if m:
                if police_line == 1:
                    police_dict['service_policy'] = m.groupdict()['service_policy']
                else:
                    class_map_dict['service_policy'] = m.groupdict()['service_policy']
                continue

            # Average Rate Traffic Shaping
            m = p4.match(line)
            if m:
                class_map_dict['average_rate_traffic_shaping'] = True
                continue

            # Adaptive Rate Traffic Shaping
            m = p4_0.match(line)
            if m:
                class_map_dict['adaptive_rate_traffic_shaping'] = True
                continue

            # cir upper-bound 2120000 (bps) cir lower-bound 1120000 (bps)
            m = p4_1.match(line)
            if m:
                class_map_dict['cir_upper_bound_bps'] = int(m.groupdict()['cir_upper_bound_bps'])
                class_map_dict['cir_lower_bound_bps'] = int(m.groupdict()['cir_lower_bound_bps'])
                continue

            # cir 1000000 (bps) bc 10000000 (bits) be 1000000 (bits)
            m = p5.match(line)
            if m:
                cir_unit=unit_dict[m.groupdict()['cir_unit']]
                class_map_dict['cir'+'_'+cir_unit] = int(m.groupdict()['cir'])
                if m.group('bc'):
                    bc_unit = unit_dict[m.groupdict()['bc_unit']]
                    class_map_dict['bc' + '_' + bc_unit] = int(m.groupdict()['bc'])
                if m.group('be'):
                    be_unit = unit_dict[m.groupdict()['be_unit']]
                    class_map_dict['be' + '_' + be_unit] = int(m.groupdict()['be'])
                continue

            # priority level 1 20000 (kb/s)
            m = p6.match(line)
            if m:
                pri_level = m.groupdict()['pri_level']
                kb_per_sec = m.groupdict()['kb_per_sec']
                priority_dict = class_map_dict.setdefault('priority_level', {}).setdefault(pri_level, {})
                priority_dict['kbps'] = int(kb_per_sec)
                continue

            # bandwidth 20000 (kb/s)
            # bandwidth 100
            m = p7_0.match(line)
            if m:
                class_map_dict['bandwidth_kbps'] = int(m.groupdict()['bandwidth'])
                continue

            # Bandwidth 70( %)
            # bandwidth 80 (%)
            m = p7.match(line)
            if m:
                if weight_line == 1:
                    weight_dict['bandwidth_percent'] = int(m.groupdict()['bandwidth'])
                elif weight_line != 1:
                    random_detect = class_map_dict.setdefault('random_detect', {})  # initialize random_detect{}
                    random_detect['bandwidth_percent'] = int(m.groupdict()['bandwidth'])
                continue

            # Weighted Fair Queueing
            m = p8.match(line)
            if m:
                weight_line = 1
                weight_dict = class_map_dict.setdefault('weighted_fair_queueing', {})
                continue

            # exponential weight 9
            m = p8_1.match(line)
            if m:
                if weight_line == 1:
                    weight_dict['exponential_weight'] = int(m.groupdict()['exponential_weight'])
                else:
                    random_detect = class_map_dict.setdefault('random_detect', {})
                    random_detect['exponential_weight'] = int(m.groupdict()['exponential_weight'])
                continue

            # explicit congestion notification
            m = p8_2.match(line)
            if m:
                weight_dict['explicit_congestion_notification'] = True
                continue

            # class    min-threshold    max-threshold    mark-probability
            # ----------------------------------------------------------
            # ----------------------------------------------------------
            # 0        -                -                1/10
            # 1        -                -                1/10
            # 2        -                -                1/10
            # 3        -                -                1/10
            # 4        -                -                1/10
            # 5        -                -                1/10
            # 6        -                -                1/10
            # 7        -                -                1/10
            # rsvp     -                -                1/10
            # default (0)   -                -                1/10
            m = p8_3.match(line)
            if m:
                group = m.groupdict()
                class_val = group['class_val']
                if weight_line == 1:
                    class_dict = weight_dict.setdefault('class_val', {}).setdefault(class_val, {})
                    class_dict['min_threshold'] = group['min_threshold']
                    class_dict['max_threshold'] = group['max_threshold']
                    class_dict['mark_probability'] = group['mark_probability']
                else:
                    random_detect = class_map_dict.setdefault('random_detect', {})
                    class_dict = random_detect.setdefault('class_val', {}).setdefault(class_val, {})
                    class_dict['min_threshold'] = group['min_threshold']
                    class_dict['max_threshold'] = group['max_threshold']
                    class_dict['mark_probability'] = group['mark_probability']
                continue

            # cir 30% bc 10 (msec) be 10 (msec)
            m = p9.match(line)
            if m:
                class_map_dict['cir_percent'] = int(m.groupdict()['cir_percent'])
                class_map_dict['bc_msec'] = int(m.groupdict()['bc_msec'])
                class_map_dict['be_msec'] = int(m.groupdict()['be_msec'])
                continue

            # priority 1000000 kbps
            m = p10.match(line)
            if m:
                class_map_dict['priority'] = True
                if m.group('priority_kbps'):
                    class_map_dict['priority_kbps'] = int(m.groupdict()['priority_kbps'])
                continue

            # priority level 1
            m = p10_1.match(line)
            if m:
                priority_level = int(m.groupdict()['priority_levels'])
                class_map_dict['priority_levels'] = priority_level

                continue

            # Set cos 5
            # set dscp cs1
            m = p11.match(line)
            if m:
                class_map_dict['set'] = m.groupdict()['set']
                continue

            # Shape average 30m
            m = p12.match(line)
            if m:
                class_map_dict['shape_average_min'] = int(m.groupdict()['shape_average_min'])
                continue

            # bandwidth 100
            m = p13.match(line)
            if m:
                class_map_dict['bandwidth'] = int(m.groupdict()['bandwidth'])
                continue

            # bandwidth remaining percent 50
            # bandwidth remaining 80 (%)
            m = p14.match(line)
            if m:
                class_map_dict['bandwidth_remaining_percent'] = int(m.groupdict()['bandwidth_remaining_percent'])
                continue

            # bandwidth remaining ratio 100
            m = p14_1.match(line)
            if m:
                class_map_dict['bandwidth_remaining_ratio'] = int(m.groupdict()['bandwidth_remaining_ratio'])
                continue

            # police cir 500000 conform-burst 10000 pir 1000000 peak-burst 10000 conform-action transmit exceed-action set-prec-transmit 2 violate-action drop
            m = p15.match(line)
            if m:
                police_line = 1
                conform_list = []
                exceed_list = []
                violate_list = []
                police_dict = class_map_dict.setdefault('police', {})
                police_dict['cir_bps'] = int(m.groupdict()['cir_bps'])
                police_dict['conform_burst'] = int(m.groupdict()['conform_burst'])
                police_dict['pir'] = int(m.groupdict()['pir'])
                police_dict['peak_burst'] = int(m.groupdict()['peak_burst'])
                police_dict['conform_action'] = conform_list.append(m.groupdict()['conform_action'])
                police_dict['exceed_action'] = exceed_list.append(m.groupdict()['exceed_action'])
                police_dict['violate_action'] = violate_list.append(m.groupdict()['violate_action'])
                continue

            # police percent 5 2 ms 0 ms conform-action transmit exceed-action drop violate-action drop
            m = p15_1.match(line)
            if m:
                police_line = 1
                conform_list = []
                exceed_list = []
                violate_list = []
                conform_list.append(m.groupdict()['conform_action'])
                exceed_list.append(m.groupdict()['exceed_action'])
                violate_list.append(m.groupdict()['violate_action'])
                police_dict = class_map_dict.setdefault('police', {})
                police_dict['cir_percent'] = int(m.groupdict()['cir_percent'])
                police_dict['bc_ms'] = int(m.groupdict()['bc_ms'])
                police_dict['be_ms'] = int(m.groupdict()['be_ms'])
                police_dict['conform_action'] = conform_list
                police_dict['exceed_action'] = exceed_list
                police_dict['violate_action'] = violate_list
                continue

            #  time-based wred, exponential weight 9
            m = p16.match(line)
            if m:
                random_detect = class_map_dict.setdefault('random_detect', {})
                random_detect['wred_type'] = m.groupdict()['wred_type']
                random_detect['exponential_weight'] = int(m.groupdict()['exponential_weight'])
                continue

            # queue-limit 200 ms
            m = p17.match(line)
            if m:
                class_map_dict['queue_limit_ms'] = int(m.groupdict()['queue_limit_ms'])
                continue

            # queue-limit 77 packets
            m = p17_1.match(line)
            if m:
                class_map_dict['queue_limit_packets'] = int(m.groupdict()['queue_limit_packets'])
                continue

        return ret_dict
        

#================================================================================
#Schema for :
#   * "show policy-map type control subscriber binding <policymap name>" 
#================================================================================
class ShowPolicyMapTypeControlSubscriberBindingPolicyName_Schema (MetaParser) :
    '''Schema for :
    * "show policy-map type control subscriber binding <policymap name>" '''  
    
    schema = {
        "policy_map_name" : str,
        "interfaces_list" : list,
    }


#=================================================================================
#Parser for:
#   * "show policy-map type control subscriber binding <policymap name>" 
# ================================================================================
class ShowPolicyMapTypeControlSubscriberBindingPolicyName(ShowPolicyMapTypeControlSubscriberBindingPolicyName_Schema) :
    '''Parser for :
    *"show policy-map type control subscriber binding <policymap name>" '''
      
    cli_command = ['show policy-map type control subscriber binding {policy_map_name}']           

    def cli(self,policy_map_name="",output=None):      
        if output is None:
            cmd = self.cli_command[0].format(policy_map_name=policy_map_name)
            output = self.device.execute(cmd)          
        
        ret_dict = {}

        #PMAP_DefaultWiredDot1xClosedAuth_1X_MAB          Gi1/0/1
        p1 = re.compile('^(?P<pname>\S+)?\s+(?P<int>[\w\/]+)$')

        #                                                 Gi1/1/1
        p2 = re.compile('^(?P<int>[\w\/]+)$')

        for line in output.splitlines():
            line = line.strip()
            
            # PMAP_DefaultWiredDot1xClosedAuth_1X_MAB         Gi1/0/1
            # dot1x_group                                     Gi1/0/1
            m = p1.match(line)
            if m:
                group = m.groupdict()
                ret_dict['policy_map_name'] = group['pname']
                ret_dict.setdefault('interfaces_list', []).append(group['int'])
                continue
        
            # Gi1/1/1
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ret_dict.setdefault('interfaces_list', []).append(group['int'])

        return ret_dict


#=====================================================
# Schema for 
#         show policy-map {} class {}
#====================================================

class ShowPolicyMapClassSchema(MetaParser):
    '''
    Schema for
        show policy-map {} class {}
    '''

    schema = {
        'class_names': {
            Any(): {
                Optional('priority_level'): int,
                Optional('priority_percent'): int,
                Optional('bandwidth_remaining_percent'): int,
            }
        }
    }

class ShowPolicyMapClass(ShowPolicyMapClassSchema):
    '''
    Parser for
        show policy-map {} class {}
    '''

    cli_command = ['show policy-map {policy_name} class {class_name}']

    def cli(self, policy_name='', class_name='', output=None):
        if not output:
            cmd = self.cli_command[0].format(policy_name=policy_name, class_name=class_name)
            output = self.device.execute(cmd)

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Class AutoQos-4.0-Output-Priority-Queue
            p1 = re.compile(r'^Class\s+(?P<class_name>\S+)$')

            # priority level 1 10 (%)
            p2 = re.compile(r'^priority\slevel\s(?P<priority_level>\d+)\s+(?P<priority_percent>\d+)\s+\(\%\)$')

            # bandwidth remaining 10 (%)
            p3 = re.compile(r'^bandwidth\sremaining\s+(?P<bandwidth_remaining_percent>\d+)\s+\(\%\)$')

            # Class AutoQos-4.0-Output-Priority-Queue
            m = p1.match(line)
            if m:
                group = m.groupdict()
                class_name = group['class_name']
                class_dict = ret_dict.setdefault('class_names', {}).setdefault(class_name, {})
                continue

            # priority level 1 10 (%)
            m = p2.match(line)
            if m:
                group = m.groupdict()
                class_dict.update({'priority_level': int(group['priority_level'])})
                class_dict.update({'priority_percent': int(group['priority_percent'])})
                continue

            # bandwidth remaining 10 (%)
            m = p3.match(line)
            if m:
                group = m.groupdict()
                class_dict.update({'bandwidth_remaining_percent': int(group['bandwidth_remaining_percent'])})
                continue

        return ret_dict

# =====================================================================
# Super Parser for:
#   * 'show policy-map type queueing interface {interface} output class {class_name}',
#   * 'show policy-map type queueing interface {interface} output',
# =====================================================================
class ShowPolicyMapTypeQueueingSuperParser(ShowPolicyMapTypeSchema):
    ''' Super Parser for
        * 'show policy-map type queueing interface {interface} output class {class_name}',
        * 'show policy-map type queueing interface {interface} output',
    '''    

    def cli(self, interface='', class_name='', output=None):

        # Init vars
        ret_dict = {}
        priority_level_status = False

        # GigabitEthernet0/1/5
        p0 = re.compile(r'^(?P<top_level>(Control Plane|Giga.*|FiveGiga.*|[Pp]seudo.*|Fast.*|[Ss]erial.*|'
                         'Ten.*|[Ee]thernet.*|[Tt]unnel.*))$')

        # Port-channel1: Service Group 1
        p0_1 = re.compile(r'^(?P<top_level>([Pp]ort.*)): +Service Group +(?P<service_group>(\d+))$')

        # Service-policy queueing output: parent
        # Service-policy queueing : child
        p1 = re.compile(r'^[Ss]ervice-policy queueing +(?P<service_policy>(|output)):+ *(?P<policy_name>([\w\-]+).*)')

        # service policy : child
        p1_1 = re.compile(r'^Service-policy *:+ *(?P<policy_name>([\w\-]+))$')

        # Class-map: Ping_Class (match-all)
        # Class-map:TEST (match-all)
        # Class-map: TEST-OTTAWA_CANADA#PYATS (match-any)
        p2 = re.compile(r'^[Cc]lass-map *:(\s*)?(?P<class_map>\S+) +\((?P<match_all>[\w-]+)\)$')

        # queue stats for all priority classes:
        p2_1 = re.compile(r'^queue +stats +for +all +priority +classes:$')

        # priority level 2
        p2_1_1 = re.compile(r'^priority +level +(?P<priority_level>(\d+))$')

        # 8 packets, 800 bytes
        p3 = re.compile(r'^(?P<packets>(\d+)) packets(, (?P<bytes>(\d+)) +bytes)?')

        # 8 packets
        p3_1 = re.compile(r'^(?P<packets>(\d+)) packets')


        # Match: access-group name Ping_Option
        # Match: access-group name PYATS-MARKING_IN#CUSTOM__ACL
        # Match: traffic-class 7
        p4 = re.compile(r'^[Mm]atch:( +)?(?P<match>([\S\s]+))$')


        # Queueing
        p5 = re.compile(r'^Queueing$')

        # queue size 0, queue limit 4068
        p6 = re.compile(r'^queue +size +(?P<queue_size>(\d+)), +queue +limit +(?P<queue_limit>(\d+))$')

        # queue limit 64 packets
        p7 = re.compile(r'^queue +limit +(?P<queue_limit>(\d+)) packets$')

        # queue limit 62500 bytes
        p8 = re.compile(r'^queue +limit +(?P<queue_limit_bytes>(\d+)) bytes$')
        
        # (total drops) 0
        p9 = re.compile(r'^\(total +drops\) +(?P<total_drops>(\d+))$')

        # (bytes output) 0
        p10 = re.compile(r'^\(bytes +output\) +(?P<bytes_output>(\d+))$')
        
        # shape (average) cir 474656, bc 1899, be 1899
        p11 = re.compile(r'^shape +\(+(?P<shape_type>(\w+))+\) +cir +(?P<shape_cir_bps>(\d+)), +'
                            'bc +(?P<shape_bc_bps>(\d+)), +be +(?P<shape_be_bps>(\d+))$')

        # target shape rate 474656
        p12 = re.compile(r'^target +shape +rate +(?P<target_shape_rate>(\d+))$')

        # queue limit 1966 us/ 49152 bytes
        p13 = re.compile(r'^queue +limit +(?P<queue_limit_us>(\d+)) +us/ +(?P<queue_limit_bytes>(\d+)) bytes$')

        # Priority: 10% (100000 kbps), burst bytes 2500000, b/w exceed drops: 44577300
        p14 = re.compile(r'^Priority:\s+(?P<percent>(\d+))%\s+\((?P<kbps>(\d+))\s+kbps\),\s+burst\sbytes\s+(?P<burst_bytes>(\d)+),(\s+'
                          'b/w\sexceed\sdrops:\s+(?P<exceed_drops>(\d+)))?$')

        # Priority Level: 1
        p15 = re.compile(r'^Priority +Level: +(?P<priority_level>(\d+))$')
        
        # Priority: Strict, b/w exceed drops: 0
        p16 = re.compile(r'^Priority: +(?P<type>(\w+)), +b/w exceed drops: +(?P<exceed_drops>(\d+))$')

        count=0
        for line in output.splitlines():
            line = line.strip()

            # Control Plane 
            m = p0.match(line)
            if m:
                top_level = m.groupdict()['top_level']
                top_level_dict = ret_dict.setdefault(top_level, {})
                continue

            # Port-channel1: Service Group 1
            m = p0_1.match(line)
            if m:
                top_level = m.groupdict()['top_level']
                service_group = int(m.groupdict()['service_group'])
                top_level_dict = ret_dict.setdefault(top_level, {})
                top_level_dict['service_group'] = service_group
                continue

            # Service-policy input: Control_Plane_In
            # Service-policy output: Control_Plane_Out
            m = p1.match(line)
            if m:
                 
                top_level_dict = ret_dict.setdefault(interface, {})
                group = m.groupdict()
                if group['service_policy'] == '':
                    count=count+1
                    service_policy = 'output'+str(count)
                else:
                    service_policy = group['service_policy']
                policy_name = group['policy_name']

                # Set dict
                service_policy_dict = top_level_dict.setdefault('service_policy', {}).\
                                                     setdefault(service_policy, {})
                policy_name_dict = service_policy_dict.setdefault('policy_name', {}).\
                                                       setdefault(policy_name, {})
                parent_policy_dict = policy_name_dict
                continue

            # Service policy : child
            m = p1_1.match(line)
            if m:
                policy_name = m.groupdict()['policy_name']
                policy_name_dict = parent_policy_dict.setdefault('child_policy_name', {}).\
                                                       setdefault(policy_name, {})
                continue

            # Class-map: Ping_Class (match-all)
            # Class-map:TEST (match-all)
            # Class-map: TEST-OTTAWA_CANADA#PYATS (match-any)
            m = p2.match(line)
            if m:
                match_list = []
                class_line_type = None
                queue_stats = 0
                class_map = m.groupdict()['class_map']
                class_map_dict = policy_name_dict.setdefault('class_map', {}).\
                                                  setdefault(class_map, {})
                class_map_dict['match_evaluation'] =  m.groupdict()['match_all']
                continue

            # queue stats for all priority classes:
            m = p2_1.match(line)
            if m:
                queue_stats = 1
                queue_dict = policy_name_dict.setdefault('queue_stats_for_all_priority_classes', {})
                continue

            # priority level 2
            m = p2_1_1.match(line)
            if m:
                priority_level_status = True
                priority_level = m.groupdict()['priority_level']
                priority_dict = queue_dict.setdefault('priority_level', {}).setdefault(priority_level, {})
                priority_dict['queueing'] = queueing_val
                continue

            # 8 packets, 800 bytes
            m = p3.match(line)
            if m:
                group = m.groupdict()
                packets = group['packets']
                class_map_dict['packets'] = int(packets)
                if 'bytes' in group and group['bytes']:
                    bytes = group['bytes']
                    class_map_dict['bytes'] = int(bytes)
                continue

            # 8 packets
            m = p3_1.match(line)
            if m:
                group = m.groupdict()
                packets = group['packets'].strip()
                class_map_dict['packets'] = int(packets)
                continue

            # Match: access-group name Ping_Option
            # Match: access-group name PYATS-MARKING_IN#CUSTOM__ACL
            # Match: traffic-class 7
            m = p4.match(line)
            if m:
                match_list.append(m.groupdict()['match'])
                class_map_dict['match'] = match_list
                continue

            # Queueing
            m = p5.match(line)
            if m:
                if queue_stats == 1:
                    queueing_val = True
                    
                else:
                    class_map_dict['queueing'] = True
                continue

            # queue size 0, queue limit 4068
            m = p6.match(line)
            if m:
                class_map_dict['queue_size'] = int(m.groupdict()['queue_size'])
                class_map_dict['queue_limit'] = int(m.groupdict()['queue_limit'])
                continue

            # queue limit 64 packets
            m = p7.match(line)
            if m:
                if queue_stats == 1:
                    if not priority_level_status:
                        priority_dict = queue_dict.setdefault('priority_level',
                                                              {}).setdefault('default', {})
                        priority_dict['queueing'] = queueing_val
                    priority_dict['queue_limit_packets'] = m.groupdict()['queue_limit']
                else:
                    class_map_dict['queue_limit_packets'] = m.groupdict()['queue_limit']
                continue

            # queue limit 62500 bytes
            m = p8.match(line)
            if m:
                class_map_dict['queue_limit_bytes'] = int(m.groupdict()['queue_limit_bytes'])
                continue
                
            # (total drops) 0
            m = p9.match(line)
            if m:
                class_map_dict['total_drops'] = int(m.groupdict()['total_drops'])
                continue
            
            # (bytes output) 0
            m = p10.match(line)
            if m:
                class_map_dict['bytes_output'] = int(m.groupdict()['bytes_output'])
                continue
                
            # shape (average) cir 474656, bc 1899, be 1899
            m = p11.match(line)
            if m:
                class_map_dict.update({k : v if k =='shape_type' else int(v)  for k,v in m.groupdict().items()})
                continue

            # target shape rate 474656
            m = p12.match(line)
            if m:
                class_map_dict['target_shape_rate'] = int(m.groupdict()['target_shape_rate'])
                continue

            # queue limit 1966 us/ 49152 bytes
            m = p13.match(line)
            if m:
                if queue_stats == 1 :
                    priority_dict['queue_limit_us'] = int(m.groupdict()['queue_limit_us'])
                    priority_dict['queue_limit_bytes'] = int(m.groupdict()['queue_limit_bytes'])
                else:
                    class_map_dict['queue_limit_us'] = int(m.groupdict()['queue_limit_us'])
                    class_map_dict['queue_limit_bytes'] = int(m.groupdict()['queue_limit_bytes'])
                continue

            # Priority: 10% (100000 kbps), burst bytes 2500000, b/w exceed drops: 44577300
            m = p14.match(line)
            if m:
                pri_dict = class_map_dict.setdefault('priority', {})
                pri_dict.update({k:int(v) for k,v in m.groupdict().items()})
                continue

            # Priority Level: 1
            m = p15.match(line)
            if m:
                class_map_dict['priority_level'] = int(m.groupdict()['priority_level'])
                continue


            # Priority: Strict, b/w exceed drops: 0
            m = p16.match(line)
            if m:
                pri_dict = class_map_dict.setdefault('priority', {})
                pri_dict['type'] = m.groupdict()['type']
                pri_dict['exceed_drops'] = int(m.groupdict()['exceed_drops'])
                continue
      
        return ret_dict



# =====================================================================
# Parser for:
#   * 'show policy-map type queueing interface {interface} output class {class_name}'
#   * 'show policy-map type queueing interface {interface} output'
# =====================================================================
class ShowPolicyMapTypeQueueingInterfaceOutput(ShowPolicyMapTypeQueueingSuperParser, ShowPolicyMapTypeSchema):
    
    ''' Parser for:
        * 'show policy-map type queueing interface {interface} output class {class_name}'
        * 'show policy-map type queueing interface {interface} output'
    '''
    cli_command = ['show policy-map type queueing interface {interface} output class {class_name}',
                   'show policy-map type queueing interface {interface} output'
                   ]
    
    def cli(self, interface, class_name='', output=None):

        if output is None:
            # Build command
            if interface and class_name:
                cmd = self.cli_command[0].format(interface=interface, class_name=class_name)
            else:
                cmd = self.cli_command[1].format(interface=interface)

            # Execute command
            output = self.device.execute(cmd)
        
        # Call super      
        return super().cli(output=output, interface=interface, class_name=class_name)


