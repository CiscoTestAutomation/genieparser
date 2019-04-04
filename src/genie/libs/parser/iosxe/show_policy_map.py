''' show_policy_map.py

IOSXE parsers for the following show commands:
    * show policy-map control-plane

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


# =====================================================================
# Schema for :
#   *'show policy-map control-plane'
#   *'show policy-map interface {interface}'
#   *'show policy-map interface {interface} output class {class_name}'
# ======================================================================
class ShowPolicyMapTypeSchema(MetaParser):

    ''' Schema for "show policy-map control-plane" '''

    schema = {
        Any(): {
            'service_policy': {
                Any(): {
                    'policy_name': {
                        Any(): {
                            'class_map': {
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
                                    Optional('bandwidth_remaining_percent'):int,
                                    Optional('bandwidth_max_threshold_packets'): int,
                                    Optional('exponential_weight'): int,
                                    Optional('exp_weight_constant'): str,
                                    Optional('mean_queue_depth'): int,
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
                                    Optional('qos_set'): {
                                        Optional('ip_precedence'): int,
                                        Optional('marker_statistics'): str,
                                        Optional('qos_group'): int,
                                        Optional('packets_marked'): int,
                                        Optional('dscp'): str,
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
                        },
                    },
                },
            },
        },
    }


# =====================================================================
# Parser for:
#   * 'show policy-map control-plane'
#   * 'show policy-map interface {interface} output class {class_name}'
#   * 'show policy-map interface {interface}'
#   * 'show policy-map interface '
# =====================================================================
class ShowPolicyMapType(ShowPolicyMapTypeSchema):
    ''' Parser for
        * "show policy-map control-plane"
        * "show policy-map interface {interface} output class {class_name}"
        * "show policy-map interface {interface}"
        * "show policy-map interface"
    '''

    cli_command = ['show policy-map interface {interface} output class {class_name}',
                   'show policy-map interface {interface}',
                   'show policy-map interface',
                   'show policy-map control-plane']

    def cli(self, class_name='', interface='', output=None):
        if output is None:
            if interface and class_name:
                cmd = self.cli_command[0].format(class_name=class_name,interface=interface)
            elif interface:
                cmd = self.cli_command[1].format(interface=interface)
            else:
                cmd = self.cli_command[2]
            # Execute command on device
            out = self.device.execute(cmd)
        else:
            out = output

        # Init vars
        ret_dict = {}
        ret_dict = collections.OrderedDict(ret_dict)

        # Control Plane
        # GigabitEthernet0/1/5
        # Something else
        p0 = re.compile(r'^(?P<top_level>(Control Plane|Giga.*|[Pp]seudo.*|Fast.*|[Ss]erial.*|'
                         'Ten.*|[Ee]thernet.*|[Tt]unnel.*|[Pp]ort.*))$')

        # Service-policy input: Control_Plane_In
        # Service-policy output: shape-out
        # Service-policy input:TEST
        p1 = re.compile(r'^[Ss]ervice-policy +(?P<service_policy>(input|output)):+ *(?P<policy_name>([\w\-]+).*)')

        # service policy : child
        p1_1 = re.compile(r'^Service-policy *:+ *(?P<policy_name>([\w\-]+))$')

        # Class-map: Ping_Class (match-all)
        # Class-map:TEST (match-all)
        p2 = re.compile(r'^[Cc]lass-map *:+(?P<class_map>([\s\w\-]+)) +(?P<match_all>(.*))$')

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

        # conformed 0000 bps, exceeded 0000 bps
        p11 = re.compile(r'^conformed +(?P<c_bps>(\d+)) bps, exceeded (?P<e_bps>(\d+)) bps$')

        # conformed 0 bps, exceed 0 bps, violate 0 bps
        p11_1 = re.compile(r'^conformed +(?P<c_bps>(\d+)) bps, exceed (?P<e_bps>(\d+)) bps,'
                            ' violate (?P<v_bps>(\d+)) bps$')

        # drop
        # transmit
        # start
        p12 = re.compile(r'^(?P<action>(drop|transmit|start))$')

        # QoS Set
        p13 = re.compile(r'^QoS +Set+$')

        # ip precedence 6
        p13_1 = re.compile(r'^ip +precedence +(?P<ip_precedence>(\d+))$')

        # Marker statistics: Disabled
        p13_2 = re.compile(r'^Marker +statistics: +(?P<marker_statistics>(\w+))$')

        # qos-group 20
        p13_3 = re.compile(r'^qos-group +(?P<qos_group>(\d+))$')

        # Packets marked 500
        p13_4 = re.compile(r'^Packets +marked +(?P<packets_marked>(\d+))$')

        # Queueing
        p14 = re.compile(r'^Queueing$')

        # queue size 0, queue limit 4068
        p15 = re.compile(r'^queue +size +(?P<queue_size>(\d+)), +queue +limit +(?P<queue_limit>(\d+))$')

        # queue limit 64 packets
        p16 = re.compile(r'^queue +limit +(?P<queue_limit>(\d+)) .*$')

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
        p24 = re.compile(r'^exponential +weight:+ *(?P<exponential_weight>(\d+))$')

        # Exp-weight-constant: 9 (1/512)
        # Exp-weight-constant:9 (1/512)
        p25 = re.compile(r'^Exp-weight-constant:+ *(?P<exp_weight_constant>([\w\(\)\s\/]+))')

        # mean queue depth: 25920
        # Mean queue depth: 0 bytes
        # Mean queue depth:0
        p26 = re.compile(r'^(M|m)ean +queue +depth:+ *(?P<mean_queue_depth>(\d+))')

        # class     Transmitted       Random drop      Tail drop     Minimum Maximum Mark
        #           pkts/bytes        pkts/bytes       pkts/bytes    thresh  thresh  prob
        #                                                            (bytes)  (bytes)
        #   0             0/0               0/0               0/0      20000    40000  1/10
        #   1           328/78720          38/9120            0/0      22000    40000  1/10
        #   2             0/0               0/0               0/0      24000    40000  1/10
        #   3             0/0               0/0               0/0      26000    40000  1/10
        #   4             0/0               0/0               0/0      28000    40000  1/10
        p27 = re.compile(r'^(?P<class>(\w+)) +(?P<transmitted>([\d\/]+)) +(?P<random_drop>([\d\/]+)) +'
                          '(?P<tail_drop>([\d\/]+)) +(?P<minimum_thresh>([\d\/]+)) +'
                          '(?P<maximum_thresh>([\d\/]+)) +(?P<mark_prob>([\d\/]+))$')

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

        for line in out.splitlines():
            line = line.strip()

            # Control Plane 
            m = p0.match(line)
            if m:
                top_level = m.groupdict()['top_level']
                top_level_dict = ret_dict.setdefault(top_level, {})
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
                class_map = m.groupdict()['class_map'].strip()
                class_match = m.groupdict()['match_all'].strip()
                class_map_dict = policy_name_dict.setdefault('class_map', {}).\
                                                  setdefault(class_map, {})
                class_map_dict['match_evaluation'] = class_match.replace('(', '').replace(')', '')
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
                continue

            # QoS Set
            m = p13.match(line)
            if m:
                qos_dict = class_map_dict.setdefault('qos_set', {})
                continue

            # ip precedence 6
            m = p13_1.match(line)
            if m:
                qos_dict['ip_precedence'] = int(m.groupdict()['ip_precedence'])
                continue

            # Marker statistics: Disabled
            m = p13_2.match(line)
            if m:
                qos_dict['marker_statistics'] = m.groupdict()['marker_statistics']
                continue

            # qos-group 20
            m = p13_3.match(line)
            if m:
                qos_dict['qos_group'] = int(m.groupdict()['qos_group'])
                continue

            # Packets marked 500
            m = p13_4.match(line)
            if m:
                qos_dict['packets_marked'] = int(m.groupdict()['packets_marked'])
                continue

            # Queueing
            m = p14.match(line)
            if m:
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

            # (queue depth/total drops/no-buffer drops) 0/0/0
            m = p17.match(line)
            if m:
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
                class_map_dict['exponential_weight'] = int(m.groupdict()['exponential_weight'])
                continue

            # Exp-weight-constant: 9 (1/512)
            m = p25.match(line)
            if m:
                class_map_dict['exp_weight_constant'] = m.groupdict()['exp_weight_constant'].strip()
                continue

            # mean queue depth: 25920
            # Mean queue depth: 0 bytes
            m = p26.match(line)
            if m:
                class_map_dict['mean_queue_depth'] = int(m.groupdict()['mean_queue_depth'])
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
                group = m.groupdict()
                class_val = group['class']
                class_dict = class_map_dict.setdefault('class', {}).\
                                            setdefault(class_val, {})
                class_dict['transmitted'] = group['transmitted']
                class_dict['random_drop'] = group['random_drop']
                class_dict['tail_drop'] = group['tail_drop']
                class_dict['minimum_thresh'] = group['minimum_thresh']
                class_dict['maximum_thresh'] = group['maximum_thresh']
                class_dict['mark_prob'] = group['mark_prob']
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

        return ret_dict


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
                            Optional('conform_action'): str,
                            Optional('exceed_action'): str,
                            Optional('violate_action'): str,
                            Optional('service_policy'): str,
                            },
                        Optional('bandwidth_kbps'): int,
                        Optional('conform_burst'): int,
                        Optional('pir'): int,
                        Optional('peak_burst'): int,
                        Optional('average_rate_traffic_shaping'): bool,
                        Optional('cir_percent'): int,
                        Optional('bc_msec'): int,
                        Optional('be_msec'): int,
                        Optional('cir_bps'): int,
                        Optional('weighted_fair_queueing'): {
                            'bandwidth_percent': int,
                            'exponential_weight': int,
                            'explicit_congestion_notification': bool,
                            'class': {
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
            if name:
                cmd = self.cli_command[0].format(name=name)
            else:
                cmd = self.cli_command[1]
            # Execute command on device
            out = self.device.execute(cmd)
        else:
            out = output

        # Init vars
        ret_dict = {}

        # Policy Map police-in
        p1 = re.compile(r'^Policy +Map +(?P<policy_map>([\w\-]+))$')
        
        # Class class-default
        p2 = re.compile(r'^Class +(?P<class_map>([\w\-]+))$')

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

        # cir 1000000 (bps)
        p5 = re.compile(r'^cir +(?P<cir_bps>(\d+))')

        # priority level 1 20000 (kb/s)
        p6 = re.compile(r'^priority +level +(?P<priority_level>(\d+)) +(?P<kb_per_sec>(\d+))')

        # bandwidth 20000 (kb/s)
        # Bandwidth 70 (%)
        p7 = re.compile(r'^(?P<key>bandwidth|Bandwidth) +(?P<bandwidth>(\d+))')

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

        p8_3 = re.compile(r'^(?P<class>(\w+)) +(?P<min_threshold>([\w\-]+)) +(?P<max_threshold>([\w\-]+)) '
                           '+(?P<mark_probability>([\d\/]+))$')

        # cir 30% bc 10 (msec) be 10 (msec)
        p9 = re.compile(r'^cir +(?P<cir_percent>(\d+))% +bc (?P<bc_msec>(\d+)) \(msec\) +'
                         'be (?P<be_msec>(\d+)) \(msec\)$')

        for line in out.splitlines():

            line = line.strip()

            # Policy Map police-in
            m = p1.match(line)
            if m:
                policy_map = m.groupdict()['policy_map']
                policy_map_dict = ret_dict.setdefault('policy_map', {}).setdefault(policy_map, {})
                continue

            # Class class-default
            m = p2.match(line)
            if m:
                class_map = m.groupdict()['class_map']
                class_map_dict = policy_map_dict.setdefault('class', {}).setdefault(class_map, {})
                continue

            # police cir 445500 bc 83619
            m = p3.match(line)
            if m:
                police_dict = class_map_dict.setdefault('police', {})
                police_dict['cir_bps'] = int(m.groupdict()['cir_bps'])
                police_dict['bc_bytes'] = int(m.groupdict()['bc_bytes'])
                continue

            # police cir 50000 bc 3000 be 3000
            m = p3_0.match(line)
            if m:
                police_dict = class_map_dict.setdefault('police', {})
                police_dict['cir_bps'] = int(m.groupdict()['cir_bps'])
                police_dict['bc_bytes'] = int(m.groupdict()['bc_bytes'])
                police_dict['be_bytes'] = int(m.groupdict()['be_bytes'])
                continue

            # conform-action transmit
            m = p3_1.match(line)
            if m:
                police_dict['conform_action'] = m.groupdict()['conform_action']
                continue

            # exceed-action drop
            m = p3_2.match(line)
            if m:
                police_dict['exceed_action'] = m.groupdict()['exceed_action']
                continue

            # conform-color hipri-conform
            m = p3_3.match(line)
            if m:
                police_dict['conform_color'] = m.groupdict()['conform_color']
                continue

            # violate - action drop
            m = p3_4.match(line)
            if m:
                police_dict['violate_action'] = m.groupdict()['violate_action']
                continue

            # service - policy child - policy
            m = p3_5.match(line)
            if m:
                police_dict['service_policy'] = m.groupdict()['service_policy']
                continue

            # Average Rate Traffic Shaping
            m = p4.match(line)
            if m:
                class_map_dict['average_rate_traffic_shaping'] = True
                continue

            # cir 1000000 (bps)
            m = p5.match(line)
            if m:
                class_map_dict['cir_bps'] = int(m.groupdict()['cir_bps'])
                continue

            # priority level 1 20000 (kb/s)
            m = p6.match(line)
            if m:
                priority_level = m.groupdict()['priority_level']
                kb_per_sec = m.groupdict()['kb_per_sec']
                priority_dict = class_map_dict.setdefault('priority_level', {}).setdefault(priority_level, {})
                priority_dict['kbps'] = int(kb_per_sec)
                continue

            # bandwidth 20000 (kb/s)
            # Bandwidth 70( %)
            m = p7.match(line)
            if m:
                key = m.groupdict()['key']
                if key == 'bandwidth':
                    class_map_dict['bandwidth_kbps'] = int(m.groupdict()['bandwidth'])
                elif key == 'Bandwidth':
                    weight_dict['bandwidth_percent'] = int(m.groupdict()['bandwidth'])
                continue

            # Weighted Fair Queueing
            m = p8.match(line)
            if m:
                weight_dict = class_map_dict.setdefault('weighted_fair_queueing', {})
                continue

            # exponential weight 9
            m = p8_1.match(line)
            if m:
                weight_dict['exponential_weight'] = int(m.groupdict()['exponential_weight'])
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
                class_val = group['class']
                class_dict = weight_dict.setdefault('class', {}).setdefault(class_val, {})
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

        return ret_dict


# ======================================
# Schema for 'show policy-map interface'
# ======================================
class ShowPolicyMapInterfaceSchema(MetaParser):

    schema = {}


# ===================================
# Parser for 'show policy map {name}'
# ===================================
class ShowPolicyMapInterface(ShowPolicyMapInterfaceSchema):

    ''' Parser for
        * 'show policy-map interface {interface} class {class_name}'
        * 'show policy-map interface {interface}'
        * 'show policy-map interface'
    '''

    cli_command = ['show policy-map interface {interface} class {class_name}',
                   'show policy-map interface {interface}',
                   'show policy-map interface',
                   ]

    def cli(self, interface='', class_name='', output=None):

        if output is None:
            if interface and class_name:
                cmd = self.cli_command[0].format(interface=interface, class_name=class_name)
            elif interface:
                cmd = self.cli_command[1].format(interface=interface)
            else:
                cmd = self.cli_command[2]
            # Execute command on device
            out = self.device.execute(cmd)
        else:
            out = output

        # continue parsing