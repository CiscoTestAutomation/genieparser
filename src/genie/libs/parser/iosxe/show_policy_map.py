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
            'service_policy': {
                Any(): {
                    'policy_name': {
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
                                    Optional('bandwidth_max_threshold_packets'): int,
                                    Optional('priority_level'): int,
                                    Optional('random_detect'):{
                                        Optional('exp_weight_constant'): str,
                                        Optional('exponential_weight'): str,
                                        Optional('mean_queue_depth'): int,
                                        Optional('class'): {
                                            Any(): {
                                                'transmitted': str,
                                                'random_drop': str,
                                                'tail_drop': str,
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
                                        Optional('exceed_drops'): int},
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
                                        Any(): {
                                            Any(): {
                                                Optional('packets_marked'): int,
                                                Optional('marker_statistics'): str,
                                            },
                                        },
                                    },
                                    Optional('police'): {
                                        Optional('cir_bps'): int,
                                        Optional('bc_bytes'): int,
                                        Optional('police_bps'): int,
                                        Optional('police_limit'): int,
                                        Optional('extended_limit'): int,
                                        Optional('bandwidth_remaining_ratio'): int,
                                        Optional('conformed'): {
                                            'packets': int,
                                            'bytes': int,
                                            'bps': int,
                                            'actions': str,
                                        },
                                        Optional('exceeded'): {
                                            'packets': int,
                                            'bytes': int,
                                            'bps': int,
                                            'actions': str,
                                        },
                                        Optional('violated'): {
                                            'packets': int,
                                            'bytes': int,
                                            'bps': int,
                                            'actions': str,
                                        },
                                    },
                                },
                            },
                            Optional('queue_stats_for_all_priority_classes'): {
                                'priority_level': {
                                    Any(): {
                                        Optional('queueing'): bool,
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

        # Control Plane
        # GigabitEthernet0/1/5
        # Something else
        p0 = re.compile(r'^(?P<top_level>(Control Plane|Giga.*|[Pp]seudo.*|Fast.*|[Ss]erial.*|'
                         'Ten.*|[Ee]thernet.*|[Tt]unnel.*))$')

        # Port-channel1: Service Group 1
        p0_1 = re.compile(r'^(?P<top_level>([Pp]ort.*)): +Service Group +(?P<service_group>(\d+))$')

        # Service-policy input: Control_Plane_In
        # Service-policy output: shape-out
        # Service-policy input:TEST
        p1 = re.compile(r'^[Ss]ervice-policy +(?P<service_policy>(input|output)):+ *(?P<policy_name>([\w\-]+).*)')

        # service policy : child
        p1_1 = re.compile(r'^Service-policy *:+ *(?P<policy_name>([\w\-]+))$')

        # Class-map: Ping_Class (match-all)
        # Class-map:TEST (match-all)
        p2 = re.compile(r'^[Cc]lass-map *:+(?P<class_map>([\s\w\-]+)) +(?P<match_all>(.*))$')

        # queue stats for all priority classes:
        p2_1 = re.compile(r'^queue +stats +for +all +priority +classes:$')

        # priority level 2
        p2_1_1 = re.compile(r'^priority +level +(?P<priority_level>(\d+))$')

        # 8 packets, 800 bytes
        p3 = re.compile(r'^(?P<packets>(\d+)) packets, (?P<bytes>(\d+)) +bytes')

        # 5 minute offered rate 0000 bps, drop rate 0000 bps
        p4 = re.compile(r'^(?P<interval>(\d+)) +minute +offered +rate +(?P<offered_rate>(\d+)) bps, +drop +rate +(?P<drop_rate>(\d+)) bps$')

        # 5 minute offered rate 0000 bps
        # 5 minute rate 0 bps
        p4_1 = re.compile(r'^(?P<interval>(\d+)) +minute(offered| )+rate +(?P<offered_rate>(\d+)) bps$')

        # 30 second offered rate 15000 bps, drop rate 300 bps
        p4_2 = re.compile(r'^(?P<interval>(\d+)) +second +offered +rate +(?P<offered_rate>(\d+)) bps, +drop +rate +(?P<drop_rate>(\d+)) bps$')

        # Match: access-group name Ping_Option
        p5 = re.compile(r'^[Mm]atch *:+(?P<match>([\(\w\-\s\)]+))$')

        # police:
        p6 = re.compile(r'^police:+$')

        #  police:  cir 64000 bps, bc 8000 bytes
        p6_1 = re.compile(r'^police: +cir (?P<cir_bps>(\d+)) bps, bc (?P<bc_bytes>(\d+)) bytes$')

        # cir 8000 bps, bc 1500 bytes
        # cir 10000000 bps, be 312500 bytes
        p7 = re.compile(r'^cir (?P<cir_bps>(\d+)) bps, (?P<key>(bc|be)) (?P<bc_bytes>(\d+)) bytes$')

        # 8000 bps, 1500 limit, 1500 extended limit
        p7_1 = re.compile(r'^(?P<police_bps>(\d+)) bps, +(?P<police_limit>(\d+)) limit, +'
                           '(?P<extended_limit>(\d+))(.*)$')

        # conformed 8 packets, 800 bytes; actions:
        p8 = re.compile(r'^conformed (?P<packets>(\d+)) packets, +(?P<bytes>(\d+)) bytes; actions:$')

        # conformed 15 packets, 6210 bytes; action:transmit
        p8_1 = re.compile(r'^conformed (?P<packets>(\d+)) packets, +(?P<bytes>(\d+)) bytes;'
                           ' action:(?P<action>(\w+))$')
        # exceeded 0 packets, 0 bytes; actions:
        p9 = re.compile(r'^exceeded (?P<packets>(\d+)) packets, +(?P<bytes>(\d+)) bytes; actions:$')

        # exceeded 5 packets, 5070 bytes; action:drop
        p9_1 = re.compile(r'^exceeded (?P<packets>(\d+)) packets, +(?P<bytes>(\d+)) bytes;'
                           ' action:(?P<action>(\w+))$')

        # violated 0 packets, 0 bytes; action:drop
        p10 = re.compile(r'^violated (?P<packets>(\d+)) packets, +(?P<bytes>(\d+)) bytes;'
                          ' action:(?P<action>(\w+))$')

        # violated 0 packets, 0 bytes; actions:
        p10_1 = re.compile(r'^violated (?P<packets>(\d+)) packets, +(?P<bytes>(\d+)) bytes; actions:$')

        # conformed 0000 bps, exceeded 0000 bps
        p11 = re.compile(r'^conformed +(?P<c_bps>(\d+)) bps, excee(ded|d) (?P<e_bps>(\d+)) bps$')

        # conformed 0 bps, exceed 0 bps, violate 0 bps
        p11_1 = re.compile(r'^conformed +(?P<c_bps>(\d+)) bps,+ excee(d|ded) (?P<e_bps>(\d+)) bps, '
                            'violat(e|ed) (?P<v_bps>(\d+)) bps$')

        # drop
        # transmit
        # start
        p12 = re.compile(r'^(?P<action>(drop|transmit|start))$')

        # QoS Set
        p13 = re.compile(r'^QoS +Set+$')

        # ip precedence 6
        # dscp af41
        # qos-group 20
        p13_1 = re.compile(r'^(?P<key>(ip precedence|qos-group|dscp)) +(?P<value>(\w+))$')

        # Marker statistics: Disabled
        p13_2 = re.compile(r'^Marker +statistics: +(?P<marker_statistics>(\w+))$')

        # Packets marked 500
        p13_3 = re.compile(r'^Packets +marked +(?P<packets_marked>(\d+))$')

        # Queueing
        p14 = re.compile(r'^Queueing$')

        # queue size 0, queue limit 4068
        p15 = re.compile(r'^queue +size +(?P<queue_size>(\d+)), +queue +limit +(?P<queue_limit>(\d+))$')

        # queue limit 64 packets
        p16 = re.compile(r'^queue +limit +(?P<queue_limit>(\d+)) packets')

        # queue limit 62500 bytes
        p16_1 = re.compile(r'^queue +limit +(?P<queue_limit_bytes>(\d+)) bytes$')

        # (queue depth/total drops/no-buffer drops) 0/0/0
        p17 = re.compile(r'^\(+queue +depth/+total +drops/+no-buffer +drops+\) +(?P<queue_depth>(\d+))/'
                            '+(?P<total_drops>(\d+))/+(?P<no_buffer_drops>(\d+))$')

        # depth/total drops/no-buffer drops) 147/38/0
        p17_1 = re.compile(r'^depth/+total +drops/+no-buffer +drops+\) +(?P<queue_depth>(\d+))/+'
                             '(?P<total_drops>(\d+))/+(?P<no_buffer_drops>(\d+))$')

        # (pkts output/bytes output) 0/0
        p18_1 = re.compile(r'^\(+pkts +output/+bytes +output+\) +(?P<pkts_output>(\d+))/+(?P<bytes_output>(\d+))$')

        # (pkts matched/bytes matched) 363/87120
        p18_2 = re.compile(r'^\(+pkts +matched/+bytes +matched+\) +(?P<pkts_matched>(\d+))/+(?P<bytes_matched>(\d+))$')

        # (pkts queued/bytes queued) 0/0
        p18_3 = re.compile(r'^\(+pkts +queued/+bytes +queued+\) +(?P<pkts_queued>(\d+))/+(?P<bytes_queued>(\d+))$')

        # shape (average) cir 474656, bc 1899, be 1899
        p19 = re.compile(r'^shape +\(+(?P<shape_type>(\w+))+\) +cir +(?P<shape_cir_bps>(\d+)), +'
                            'bc +(?P<shape_bc_bps>(\d+)), +be +(?P<shape_be_bps>(\d+))$')

        # target shape rate 474656
        p20 = re.compile(r'^target +shape +rate +(?P<target_shape_rate>(\d+))$')

        # Output Queue: Conversation 266
        p21 = re.compile(r'^Output +Queue: +(?P<output_queue>([\w\s]+))$')

        # Bandwidth 10 (%)
        p22 = re.compile(r'^Bandwidth +(?P<bandwidth>(\d+)) .*$')

        # bandwidth 1000 (kbps)
        p23 = re.compile(r'^bandwidth (?P<bandwidth_kbps>(\d+)) \(kbps\)$')

        # exponential weight: 9
        # exponential weight:9
        # Exp-weight-constant: 9 (1/512)
        # Exp-weight-constant:9 (1/512)
        p24 = re.compile(r'^(?P<key>(Exp-weight-constant|exponential.*)):+ *(?P<value>([\w\(\)\s\/]+))')

        # mean queue depth: 25920
        # Mean queue depth: 0 bytes
        # Mean queue depth:0
        p26 = re.compile(r'^(M|m)ean +queue +depth:+ *(?P<mean_queue_depth>(\d+))')

        # class     Transmitted       Random drop      Tail drop     Minimum Maximum Mark
        # class     Transmitted       Random drop      Tail drop     Minimum Maximum Mark
        p27_1 = re.compile(r'^class +Transmitted +Random +drop +Tail +drop +Minimum +Maximum +Mark$')

        # Class Random       Tail    Minimum    Maximum     Mark      Output
        p27_2 = re.compile(r'^Class +Random +Tail +Minimum +Maximum +Mark +Output$')

        # class     Transmitted       Random drop      Tail drop     Minimum Maximum Mark
        #   0             0/0               0/0               0/0      20000    40000  1/10
        #   1           328/78720          38/9120            0/0      22000    40000  1/10
        #   2             0/0               0/0               0/0      24000    40000  1/10
        #   3             0/0               0/0               0/0      26000    40000  1/10
        #   4             0/0               0/0               0/0      28000    40000  1/10     
        # Class         Random             Tail            Minimum    Maximum   Mark   Output
        #   0             0                 0                 0        0        1/10   0
        p27 = re.compile(r'^(?P<class>(\w+)) +(?P<value1>([\d\/]+)) +(?P<value2>([\d\/]+)) +'
                          '(?P<value3>([\d\/]+)) +(?P<value4>([\d\/]+)) +'
                          '(?P<value5>([\d\/]+)) +(?P<value6>([\d\/]+))$')

        # policy wred-policy
        p28 = re.compile(r'^policy +(?P<policy>([\w\-]+))$')

        # class prec2
        p29 = re.compile(r'^class +(?P<class>([\w\-]+))$')

        # bandwidth 1000
        p30 = re.compile(r'^bandwidth +(?P<bandwidth>(\d+))$')

        # bandwidth:class-based wfq, weight 25
        p31 = re.compile(r'^bandwidth(:| )?(?P<bandwidth>([\s\w\-\,]+))$')

        # bandwidth remaining ratio 1
        p32 = re.compile(r'^bandwidth +remaining +ratio +(?P<bandwidth_remaining_ratio>(\d+))$')

        # random-detect
        p33 = re.compile(r'^random-detect$')

        # random-detect precedence 2 100 bytes 200 bytes 10
        p33_1 = re.compile(r'^random-detect +precedence +(?P<precedence>(\d+)) +'
                            '(?P<bytes1>(\d+)) bytes +(?P<bytes2>(\d+)) bytes +(?P<bytes3>(\d+))$')

        # packet output 90, packet drop 0
        p34 = re.compile(r'^packet +output +(?P<packet_output>(\d+)), +packet +drop +(?P<packet_drop>(\d+))$')

        # tail/random drop 0, no buffer drop 0, other drop 0
        p35 = re.compile(r'^tail/random drop +(?P<tail_random_drops>(\d+)), +no buffer drop +(?P<no_buffer_drops>(\d+)), '
                          '+other drop +(?P<other_drops>(\d+))$')

        # queue limit 1966 us/ 49152 bytes
        p37 = re.compile(r'^queue +limit +(?P<queue_limit_us>(\d+)) +us/ +(?P<queue_limit_bytes>(\d+)) bytes$')

        # Priority: 10% (100000 kbps), burst bytes 2500000, b/w exceed drops: 44577300
        p38 = re.compile(r'^Priority: +(?P<percent>(\d+))% +\((?P<kbps>(\d+)) kbps\), +burst bytes +(?P<burst_bytes>(\d)+), +'
                          'b/w exceed drops: +(?P<exceed_drops>(\d+))$')

        # Priority Level: 1
        p39 = re.compile(r'^Priority +Level: +(?P<priority_level>(\d+))$')

        # bandwidth remaining 70%
        p40 = re.compile(r'^bandwidth +remaining +(?P<bandwidth_remaining_percent>(\d+))%$')

        for line in out.splitlines():
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
                group = m.groupdict()
                service_policy = group['service_policy'].strip()
                policy_name = group['policy_name'].strip()
                # Set dict
                service_policy_dict = top_level_dict.setdefault('service_policy', {}).\
                                                     setdefault(service_policy, {})
                policy_name_dict = service_policy_dict.setdefault('policy_name', {}).\
                                                       setdefault(policy_name, {})
                continue

            # Service policy : child
            m = p1_1.match(line)
            if m:
                policy_name = m.groupdict()['policy_name'].strip()
                policy_name_dict = service_policy_dict.setdefault('policy_name', {}).\
                                                       setdefault(policy_name, {})
                continue

            # Class-map: Ping_Class (match-all)
            m = p2.match(line)
            if m:
                match_list = []
                class_line_type = None
                queue_stats = 0
                class_map = m.groupdict()['class_map'].strip()
                class_match = m.groupdict()['match_all'].strip()
                class_map_dict = policy_name_dict.setdefault('class_map', {}).\
                                                  setdefault(class_map, {})
                class_map_dict['match_evaluation'] = class_match.replace('(', '').replace(')', '')
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
                priority_level = m.groupdict()['priority_level']
                priority_dict = queue_dict.setdefault('priority_level', {}).setdefault(priority_level, {})
                priority_dict['queueing'] = queueing_val
                continue

            # 8 packets, 800 bytes
            m = p3.match(line)
            if m:
                group = m.groupdict()
                packets = group['packets'].strip()
                bytes = group['bytes'].strip()
                class_map_dict['packets'] = int(packets)
                class_map_dict['bytes'] = int(bytes)
                continue

            # 5 minute offered rate 0000 bps, drop rate 0000 bps
            m = p4.match(line)
            if m:
                rate_dict = class_map_dict.setdefault('rate', {})
                rate_dict['interval'] = int(m.groupdict()['interval']) * 60
                rate_dict['offered_rate_bps'] = int(m.groupdict()['offered_rate'])
                rate_dict['drop_rate_bps'] = int(m.groupdict()['drop_rate'])
                continue

            # 5 minute offered rate 0000 bps
            m = p4_1.match(line)
            if m:
                rate_dict = class_map_dict.setdefault('rate', {})
                rate_dict['interval'] = int(m.groupdict()['interval']) * 60
                rate_dict['offered_rate_bps'] = int(m.groupdict()['offered_rate'])
                continue

            # 30 second offered rate 15000 bps, drop rate 300 bps
            m = p4_2.match(line)
            if m:
                rate_dict = class_map_dict.setdefault('rate', {})
                rate_dict['interval'] = int(m.groupdict()['interval'])
                rate_dict['offered_rate_bps'] = int(m.groupdict()['offered_rate'])
                rate_dict['drop_rate_bps'] = int(m.groupdict()['drop_rate'])
                continue

            # Match: access-group name Ping_Option
            m = p5.match(line)
            if m:
                match_list.append(m.groupdict()['match'].lstrip())
                class_map_dict['match'] = match_list
                continue

            # police:
            m = p6.match(line)
            if m:
                police_dict = class_map_dict.setdefault('police', {})
                continue

            # police:  cir 64000 bps, bc 8000 bytes
            m = p6_1.match(line)
            if m:
                police_dict = class_map_dict.setdefault('police', {})
                police_dict['cir_bps'] = int(m.groupdict()['cir_bps'])
                police_dict['bc_bytes'] = int(m.groupdict()['bc_bytes'])
                continue

            # cir 8000 bps, bc 1500 bytes
            m = p7.match(line)
            if m:
                police_dict['cir_bps'] = int(m.groupdict()['cir_bps'])
                police_dict['bc_bytes'] = int(m.groupdict()['bc_bytes'])
                continue

            # 8000 bps, 1500 limit, 1500 extended limit
            m = p7_1.match(line)
            if m:
                police_dict['police_bps'] = int(m.groupdict()['police_bps'])
                police_dict['police_limit'] = int(m.groupdict()['police_limit'])
                police_dict['extended_limit'] = int(m.groupdict()['extended_limit'])

            # conformed 8 packets, 800 bytes; actions:
            m = p8.match(line)
            if m:
                conformed_line = True
                exceeded_line = False
                violated_line = False
                conformed_dict = police_dict.setdefault('conformed', {})
                conformed_dict['packets'] = int(m.groupdict()['packets'])
                conformed_dict['bytes'] = int(m.groupdict()['bytes'])
                continue

            # conformed 15 packets, 6210 bytes; action:transmit
            m = p8_1.match(line)
            if m:
                conformed_dict = police_dict.setdefault('conformed', {})
                conformed_dict['packets'] = int(m.groupdict()['packets'])
                conformed_dict['bytes'] = int(m.groupdict()['bytes'])
                conformed_dict['actions'] = m.groupdict()['action']
                continue

            # exceeded 0 packets, 0 bytes; actions:
            m = p9.match(line)
            if m:
                conformed_line = False
                violated_line = False
                exceeded_line = True
                exceeded_dict = police_dict.setdefault('exceeded', {})
                exceeded_dict['packets'] = int(m.groupdict()['packets'])
                exceeded_dict['bytes'] = int(m.groupdict()['bytes'])
                continue

            # exceeded 5 packets, 5070 bytes; action:drop
            m = p9_1.match(line)
            if m:
                exceeded_dict = police_dict.setdefault('exceeded', {})
                exceeded_dict['packets'] = int(m.groupdict()['packets'])
                exceeded_dict['bytes'] = int(m.groupdict()['bytes'])
                exceeded_dict['actions'] = m.groupdict()['action']
                continue

            # violated 0 packets, 0 bytes; action:drop
            m = p10.match(line)
            if m:
                violated_dict = police_dict.setdefault('violated', {})
                violated_dict['packets'] = int(m.groupdict()['packets'])
                violated_dict['bytes'] = int(m.groupdict()['bytes'])
                violated_dict['actions'] = m.groupdict()['action']
                continue

            # violated 0 packets, 0 bytes; action:
            m = p10_1.match(line)
            if m:
                conformed_line = False
                exceeded_line = False
                violated_line = True
                violated_dict = police_dict.setdefault('violated', {})
                violated_dict['packets'] = int(m.groupdict()['packets'])
                violated_dict['bytes'] = int(m.groupdict()['bytes'])
                continue

            # conformed 0000 bps, exceeded 0000 bps
            m = p11.match(line)
            if m:
                conformed_dict['bps'] = int(m.groupdict()['c_bps'])
                exceeded_dict['bps'] = int(m.groupdict()['e_bps'])
                continue

            # conformed 0 bps, exceed 0 bps, violate 0 bps
            m = p11_1.match(line)
            if m:
                conformed_dict['bps'] = int(m.groupdict()['c_bps'])
                exceeded_dict['bps'] = int(m.groupdict()['e_bps'])
                violated_dict['bps'] = int(m.groupdict()['v_bps'])
                continue

            # drop
            # transmit
            # start
            m = p12.match(line)
            if m:
                if conformed_line:
                    conformed_dict['actions'] = m.groupdict()['action']
                elif exceeded_line:
                    exceeded_dict['actions'] = m.groupdict()['action']
                elif violated_line:
                    violated_dict['actions'] = m.groupdict()['action']
                continue

            # QoS Set
            m = p13.match(line)
            if m:
                qos_dict = class_map_dict.setdefault('qos_set', {})
                continue

            # ip precedence 6
            m = p13_1.match(line)
            if m:
                group = m.groupdict()
                key = group['key'].strip()
                value = group['value'].strip()
                qos_dict_map = qos_dict.setdefault(key, {}).setdefault(value, {})
                continue

            # Marker statistics: Disabled
            m = p13_2.match(line)
            if m:
                qos_dict_map['marker_statistics'] = m.groupdict()['marker_statistics']
                continue

            # Packets marked 500
            m = p13_3.match(line)
            if m:
                qos_dict_map['packets_marked'] = int(m.groupdict()['packets_marked'])
                continue

            # Queueing
            m = p14.match(line)
            if m:
                if queue_stats == 1:
                    queueing_val = True
                    # priority_dict['queueing'] = True
                else:
                    class_map_dict['queueing'] = True
                continue

            # queue size 0, queue limit 4068
            m = p15.match(line)
            if m:
                class_map_dict['queue_size'] = int(m.groupdict()['queue_size'])
                class_map_dict['queue_limit'] = int(m.groupdict()['queue_limit'])
                continue

            # queue limit 64 packets
            m = p16.match(line)
            if m:
                class_map_dict['queue_limit_packets'] = m.groupdict()['queue_limit']
                continue

            # queue limit 62500 bytes
            m = p16_1.match(line)
            if m:
                class_map_dict['queue_limit_bytes'] = int(m.groupdict()['queue_limit_bytes'])
                continue

            # (queue depth/total drops/no-buffer drops) 0/0/0
            m = p17.match(line)
            if m:
                if queue_stats == 1:
                    priority_dict['queue_depth'] = int(m.groupdict()['queue_depth'])
                    priority_dict['total_drops'] = int(m.groupdict()['total_drops'])
                    priority_dict['no_buffer_drops'] = int(m.groupdict()['no_buffer_drops'])
                else:
                    class_map_dict['queue_depth'] = int(m.groupdict()['queue_depth'])
                    class_map_dict['total_drops'] = int(m.groupdict()['total_drops'])
                    class_map_dict['no_buffer_drops'] = int(m.groupdict()['no_buffer_drops'])
                continue

            # depth/total drops/no-buffer drops) 147/38/0
            m = p17_1.match(line)
            if m:
                class_map_dict['queue_depth'] = int(m.groupdict()['queue_depth'])
                class_map_dict['total_drops'] = int(m.groupdict()['total_drops'])
                class_map_dict['no_buffer_drops'] = int(m.groupdict()['no_buffer_drops'])
                continue

            # (pkts output/bytes output) 0/0
            m = p18_1.match(line)
            if m:
                if queue_stats == 1:
                    priority_dict['pkts_output'] = int(m.groupdict()['pkts_output'])
                    priority_dict['bytes_output'] = int(m.groupdict()['bytes_output'])
                else:
                    class_map_dict['pkts_output'] = int(m.groupdict()['pkts_output'])
                    class_map_dict['bytes_output'] = int(m.groupdict()['bytes_output'])
                continue

            # (pkts matched/bytes matched) 363/87120
            m = p18_2.match(line)
            if m:
                class_map_dict['pkts_matched'] = int(m.groupdict()['pkts_matched'])
                class_map_dict['bytes_matched'] = int(m.groupdict()['bytes_matched'])
                continue

            # (pkts queued/bytes queued) 0/0
            m = p18_3.match(line)
            if m:
                class_map_dict['pkts_queued'] = int(m.groupdict()['pkts_queued'])
                class_map_dict['bytes_queued'] = int(m.groupdict()['bytes_queued'])
                continue

            # shape (average) cir 474656, bc 1899, be 1899
            m = p19.match(line)
            if m:
                class_map_dict['shape_type'] = m.groupdict()['shape_type']
                class_map_dict['shape_cir_bps'] = int(m.groupdict()['shape_cir_bps'])
                class_map_dict['shape_bc_bps'] = int(m.groupdict()['shape_bc_bps'])
                class_map_dict['shape_be_bps'] = int(m.groupdict()['shape_be_bps'])
                continue

            # target shape rate 474656
            m = p20.match(line)
            if m:
                class_map_dict['target_shape_rate'] = int(m.groupdict()['target_shape_rate'])
                continue

            # Output Queue: Conversation 266
            m = p21.match(line)
            if m:
                class_map_dict['output_queue'] = m.groupdict()['output_queue']
                continue

            # Bandwidth 10 (%)
            m = p22.match(line)
            if m:
                class_map_dict['bandwidth_percent'] = int(m.groupdict()['bandwidth'])
                continue

            # bandwidth 1000 (kbps)
            m = p23.match(line)
            if m:
                class_map_dict['bandwidth_kbps'] = int(m.groupdict()['bandwidth_kbps'])
                continue

            # exponential weight: 9
            m = p24.match(line)
            if m:
                group = m.groupdict()
                key = group['key'].strip()
                value = group['value'].strip()
                random_detect_dict = class_map_dict.setdefault('random_detect', {})
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
                    value1 = 'transmitted'
                    value2 = 'random_drop'
                    value3 = 'tail_drop'
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
                class_dict = random_detect_dict.setdefault('class', {}).\
                                            setdefault(class_val, {})
                class_dict[value1] = group['value1']
                class_dict[value2] = group['value2']
                class_dict[value3] = group['value3']
                class_dict[value4] = group['value4']
                class_dict[value5] = group['value5']
                class_dict[value6] = group['value6']
                continue

            # policy wred-policy
            m = p28.match(line)
            if m:
                policy = m.groupdict()['policy']
                policy_dict = class_map_dict.setdefault('policy', {}).\
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

            # bandwidth:class-based wfq, weight 25
            m = p31.match(line)
            if m:
                class_map_dict['bandwidth'] = m.groupdict()['bandwidth']
                continue

            # bandwidth remaining ratio 1
            m = p32.match(line)
            if m:
                class_map_dict['bandwidth_remaining_ratio'] = m.groupdict()['bandwidth_remaining_ratio']
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
                class_map_dict['packet_output'] = int(m.groupdict()['packet_output'])
                class_map_dict['packet_drop'] = int(m.groupdict()['packet_drop'])
                continue

            # tail/random drop 0, no buffer drop 0, other drop 0
            m = p35.match(line)
            if m:
                class_map_dict['tail_random_drops'] = int(m.groupdict()['tail_random_drops'])
                class_map_dict['no_buffer_drops'] = int(m.groupdict()['no_buffer_drops'])
                class_map_dict['other_drops'] = int(m.groupdict()['other_drops'])
                continue

            # queue limit 1966 us/ 49152 bytes
            m = p37.match(line)
            if m:
                if queue_stats == 1 :
                    priority_dict['queue_limit_us'] = int(m.groupdict()['queue_limit_us'])
                    priority_dict['queue_limit_bytes'] = int(m.groupdict()['queue_limit_bytes'])
                else:
                    class_map_dict['queue_limit_us'] = int(m.groupdict()['queue_limit_us'])
                    class_map_dict['queue_limit_bytes'] = int(m.groupdict()['queue_limit_bytes'])
                continue

            # Priority: 10% (100000 kbps), burst bytes 2500000, b/w exceed drops: 44577300
            m = p38.match(line)
            if m:
                pri_dict = class_map_dict.setdefault('priority', {})
                pri_dict['percent'] = int(m.groupdict()['percent'])
                pri_dict['kbps'] = int(m.groupdict()['kbps'])
                pri_dict['burst_bytes'] = int(m.groupdict()['burst_bytes'])
                pri_dict['exceed_drops'] = int(m.groupdict()['exceed_drops'])
                continue

            # Priority Level: 1
            m = p39.match(line)
            if m:
                class_map_dict['priority_level'] = int(m.groupdict()['priority_level'])
                continue

            # bandwidth remaining 70%
            m = p40.match(line)
            if m:
                class_map_dict['bandwidth_remaining_percent'] = int(m.groupdict()['bandwidth_remaining_percent'])
                continue

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

    def cli(self, class_name='', output=None):

        if output is None:
            # Build command
            if class_name:
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
                'class': {
                    Any(): {
                        Optional('priority_level'): {
                            Any(): {
                                'kbps': int}},
                        Optional('police'): {
                            Optional('cir_bps'): int,
                            Optional('bc_bytes'): int,
                            Optional('be_bytes'): int,
                            Optional('conform_color'): str,
                            Optional('conform_action'): list,
                            Optional('exceed_action'): list,
                            Optional('violate_action'): list,
                            Optional('service_policy'): str,
                            Optional('conform_burst'): int,
                            Optional('pir'): int,
                            Optional('peak_burst'): int,
                            Optional('cir_percent'): int,
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
                        Optional('priority_levels'): int,
                        Optional('peak_burst'): int,
                        Optional('average_rate_traffic_shaping'): bool,
                        Optional('adaptive_rate_traffic_shaping'): bool,
                        Optional('cir_percent'): int,
                        Optional('bc_msec'): int,
                        Optional('be_msec'): int,
                        Optional('cir_bps'): int,
                        Optional('cir_upper_bound_bps'): int,
                        Optional('cir_lower_bound_bps'): int,
                        Optional('random_detect'): {
                            Optional('exponential_weight'): int,
                            Optional('bandwidth_percent'): int,
                            Optional('time_based'): str,
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


        # Policy Map police-in
        p1 = re.compile(r'^Policy +Map +(?P<policy_map>([\w\-]+))$')
        
        # Class class-default
        # Class class c1
        p2 = re.compile(r'^Class +(?P<class_map>([\w\-\s]+))$')

        # police 8000 9216 0
        p2_0 = re.compile(r'^police +(?P<cir_bps>(\d+)) +(?P<bc_bytes>(\d+)) +(?P<be_bytes>(\d+))$')

        # police cir percent 20 bc 300 ms pir percent 40 be 400 ms
        p2_1 = re.compile(r'^police +cir +percent +(?P<cir_percent>(\d+)) +bc +(?P<bc_ms>(\d+)) +ms +pir +percent +'
                           '(?P<pir_percent>(\d+)) +be +(?P<be_ms>(\d+)) ms$')

        # police cir 1000000 bc 31250 pir 2000000 be 31250
        p2_2 = re.compile(r'^police +cir +(?P<cir_bps>(\d+)) +bc +(?P<bc_bytes>(\d+)) +pir +(?P<pir>(\d+)) +be +(?P<be_bytes>(\d+))$')

        # police cir 445500 bc 83619
        p3 = re.compile(r'^police +cir +(?P<cir_bps>(\d+)) +bc +(?P<bc_bytes>(\d+))$')

        # police cir 50000 bc 3000 be 3000
        p3_0 = re.compile(r'^police +cir +(?P<cir_bps>(\d+)) +bc +(?P<bc_bytes>(\d+)) +be +(?P<be_bytes>(\d+))$')

        # conform-action transmit
        p3_1 = re.compile(r'^conform-action +(?P<conform_action>([\w\-\s]+))$')

        # exceed-action drop
        p3_2 = re.compile(r'^exceed-action +(?P<exceed_action>([\w\-\s]+))$')

        # conform-color hipri-conform
        p3_3 = re.compile(r'^conform-color +(?P<conform_color>([\w\-\s]+))$')

        # violate - action drop
        p3_4 = re.compile(r'^violate-action +(?P<violate_action>([\w\-\s]+))$')

        # service - policy child - policy
        p3_5 = re.compile(r'^service-policy +(?P<service_policy>([\w\-\s]+))$')

        # Average Rate Traffic Shaping
        p4 = re.compile(r'^Average +Rate +Traffic +Shaping$')

        # Adaptive Rate Traffic Shaping
        p4_0 = re.compile(r'Adaptive +Rate +Traffic +Shaping$')

        #cir upper-bound 2120000 (bps) cir lower-bound 1120000 (bps)
        p4_1 = re.compile(r'^cir +upper-bound +(?P<cir_upper_bound_bps>(\d+)) \(bps\) +cir +lower-bound +(?P<cir_lower_bound_bps>(\d+)) \(bps\)$')

        # cir 1000000 (bps)
        p5 = re.compile(r'^cir +(?P<cir_bps>(\d+)) \(bps\)$')

        # cir 100%
        p5_0 = re.compile(r'cir +(?P<cir_percent>(\d+))%$')

        # priority level 1 20000 (kb/s)
        p6 = re.compile(r'^priority +level +(?P<pri_level>(\d+)) +(?P<kb_per_sec>(\d+)) \(kb\/s\)$')

        # bandwidth 20000 (kb/s)
        p7_0 = re.compile(r'^bandwidth +(?P<bandwidth>(\d+)) \(kb\/s\)$')

        # bandwidth 100
        p7_1 = re.compile(r'^bandwidth +(?P<bandwidth>(\d+))$')

        # Bandwidth 70 (%)
        # bandwidth 80 (%)
        p7 = re.compile(r'^[bB]andwidth +(?P<bandwidth>(\d+)) \(%\)$')

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

        p8_3 = re.compile(r'^(?P<class_val>(\w+)) +(?P<min_threshold>([\w\-]+)) +(?P<max_threshold>([\w\-]+)) '
                           '+(?P<mark_probability>([0-9]+)/([0-9]+))$')

        # cir 30% bc 10 (msec) be 10 (msec)
        p9 = re.compile(r'^cir +(?P<cir_percent>(\d+))% +bc (?P<bc_msec>(\d+)) \(msec\) +'
                         'be (?P<be_msec>(\d+)) \(msec\)$')

        # priority
        p10 = re.compile(r'^priority$')

        # priority level 1
        p10_1 = re.compile(r'^priority +level +(?P<priority_levels>(\d+))$')

        #  Set cos 5
        p11 = re.compile(r'^Set +(?P<set>([\w\s]+))$')

        # Shape average 30m
        p12 = re.compile(r'^Shape +average +(?P<shape_average_min>(\d+))m$')

        # bandwidth 100
        p13 = re.compile(r'^bandwidth +(?P<bandwidth>(\d+))$')

        #  bandwidth remaining percent 50
        p14 = re.compile(r'^bandwidth remaining percent +(?P<bandwidth_remaining_percent>(\d+))$')

        # bandwidth remaining 80 (%)
        p14_0 = re.compile(r'^bandwidth remaining +(?P<bandwidth_remaining_percent>(\d+)) \(%\)$')

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
        p16 = re.compile(r'^time-based +(?P<time_based>(\w+)), +exponential +weight +(?P<exponential_weight>(\d+))$')

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
                vioate_list = []
                police_dict = class_map_dict.setdefault('police', {})
                police_dict['cir_bps'] = int(m.groupdict()['cir_bps'])
                police_dict['bc_bytes'] = int(m.groupdict()['bc_bytes'])
                police_dict['be_bytes'] = int(m.groupdict()['be_bytes'])
                continue

            #police cir percent 20 bc 300 ms pir percent 40 be 400 ms
            m = p2_1.match(line)
            if m:
                police_line = 1
                conform_list = []
                exceed_list = []
                vioate_list = []
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
                vioate_list = []
                police_dict = class_map_dict.setdefault('police', {})
                police_dict['cir_bps'] = int(m.groupdict()['cir_bps'])
                police_dict['bc_bytes'] = int(m.groupdict()['bc_bytes'])
                police_dict['pir'] = int(m.groupdict()['pir'])
                police_dict['be_bytes'] = int(m.groupdict()['be_bytes'])
                continue


            # police cir 445500 bc 83619
            m = p3.match(line)
            if m:
                police_line = 1
                conform_list = []
                exceed_list = []
                vioate_list = []
                police_dict = class_map_dict.setdefault('police', {})
                police_dict['cir_bps'] = int(m.groupdict()['cir_bps'])
                police_dict['bc_bytes'] = int(m.groupdict()['bc_bytes'])
                continue

            # police cir 50000 bc 3000 be 3000
            m = p3_0.match(line)
            if m:
                police_line = 1
                conform_list = []
                exceed_list = []
                vioate_list = []
                police_dict = class_map_dict.setdefault('police', {})
                police_dict['cir_bps'] = int(m.groupdict()['cir_bps'])
                police_dict['bc_bytes'] = int(m.groupdict()['bc_bytes'])
                police_dict['be_bytes'] = int(m.groupdict()['be_bytes'])
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
                vioate_list.append(m.groupdict()['violate_action'])
                police_dict['violate_action'] = vioate_list
                continue

            # service - policy child - policy
            m = p3_5.match(line)
            if m:
                if police_line == 1:
                    police_dict['service_policy'] = m.groupdict()['service_policy']
                else :
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

            # cir 1000000 (bps)
            m = p5.match(line)
            if m:
                class_map_dict['cir_bps'] = int(m.groupdict()['cir_bps'])
                continue

            # cir 100%
            m = p5_0.match(line)
            if m:
                class_map_dict['cir_percent'] = int(m.groupdict()['cir_percent'])
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
            m = p7_0.match(line)
            if m:
                class_map_dict['bandwidth_kbps'] = int(m.groupdict()['bandwidth'])
                continue

            m = p7_1.match(line)
            if m:
                class_map_dict['bandwidth_kbps'] = int(m.groupdict()['bandwidth'])
                continue

            # Bandwidth 70( %)
            # bandwidth 80 (%)
            m = p7.match(line)
            if m:
                if weight_line == 1 :
                    weight_dict['bandwidth_percent'] = int(m.groupdict()['bandwidth'])
                elif weight_line != 1 :
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

            # priority
            m = p10.match(line)
            if m:
                class_map_dict['priority'] = True
                continue

            # priority level 1
            m = p10_1.match(line)
            if m:
                priority_level = int(m.groupdict()['priority_levels'])
                #import pdb;pdb.set_trace()
                class_map_dict['priority_levels'] = priority_level

                continue

            #  Set cos 5
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

            #  bandwidth remaining percent 50
            m = p14.match(line)
            if m:
                class_map_dict['bandwidth_remaining_percent'] = int(m.groupdict()['bandwidth_remaining_percent'])
                continue

            # bandwidth remaining 80 (%)
            m = p14_0.match(line)
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
                vioate_list = []
                police_dict = class_map_dict.setdefault('police', {})
                police_dict['cir_bps'] = int(m.groupdict()['cir_bps'])
                police_dict['conform_burst'] = int(m.groupdict()['conform_burst'])
                police_dict['pir'] = int(m.groupdict()['pir'])
                police_dict['peak_burst'] = int(m.groupdict()['peak_burst'])
                police_dict['conform_action'] = conform_list.append(m.groupdict()['conform_action'])
                police_dict['exceed_action'] = exceed_list.append(m.groupdict()['exceed_action'])
                police_dict['violate_action'] = vioate_list.append(m.groupdict()['violate_action'])
                continue

            # police percent 5 2 ms 0 ms conform-action transmit exceed-action drop violate-action drop
            m = p15_1.match(line)
            if m:
                police_line = 1
                conform_list = []
                exceed_list = []
                vioate_list = []
                conform_list.append(m.groupdict()['conform_action'])
                exceed_list.append(m.groupdict()['exceed_action'])
                vioate_list.append(m.groupdict()['violate_action'])
                police_dict = class_map_dict.setdefault('police', {})
                police_dict['cir_percent'] = int(m.groupdict()['cir_percent'])
                police_dict['bc_ms'] = int(m.groupdict()['bc_ms'])
                police_dict['be_ms'] = int(m.groupdict()['be_ms'])
                police_dict['conform_action'] = conform_list
                police_dict['exceed_action'] = exceed_list
                police_dict['violate_action'] = vioate_list
                continue

            #  time-based wred, exponential weight 9
            m = p16.match(line)
            if m:
                random_detect['time_based'] = m.groupdict()['time_based']
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
