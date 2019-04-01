''' show_policy_map.py

IOSXE parsers for the following show commands:
    * show policy map control plane

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
#   *'show policy map control plane'
#   *'show policy-map interface {interface}'
#   *'show policy-map interface {interface} output class {class_name}'
# ======================================================================
class ShowPolicyMapControlPlaneSchema(MetaParser):

    ''' Schema for "show policy map control plane" '''

    schema = {
        Any(): # Control Plane
            {'service_policy': 
                {Any(): # input/output
                    {'policy_name': 
                        {Any(): # Control_Plane_in 
                            {'class_map': 
                                {Any(): # Ping_Class
                                    {'match_all': bool,
                                     Optional('packets'): int,
                                     Optional('bytes'): int,
                                     Optional('queueing'):
                                         {Optional('queue_limit'): str,
                                          Optional('queue_depth'): int,
                                          Optional('total_drops'): int,
                                          Optional('no_buffer_drops'): int,
                                          Optional('pkts_output'): int,
                                          Optional('bytes_output'): int,
                                          Optional('shape_cir_bps'): int,
                                          Optional('shape_bc_bps'): int,
                                          Optional('shape_be_bps'): int,
                                          Optional('target_shape_rate'): int,
                                         },
                                     Optional('rate'):
                                         {Optional('interval'): int,
                                          Optional('offered_rate_bps'): int,
                                          Optional('drop_rate_bps'): int,
                                         },
                                     'match': str,
                                     Optional('qos_set'):
                                         {'ip_precedence': int,
                                          'marker_statistics': str,
                                         },
                                     Optional('police'):
                                         {Optional('cir_bps'): int,
                                          Optional('bc_bytes'): int,
                                          Optional('police_bps'): int,
                                          Optional('police_limit'): int,
                                          Optional('extended_limit'): int,
                                          Optional('conformed'):
                                              {'packets': int,
                                               'bytes': int,
                                               'bps': int,
                                               'actions': str,
                                              },
                                          Optional('exceeded'):
                                              {'packets': int,
                                               'bytes': int,
                                               'bps': int,
                                               'actions': str,
                                              },
                                          Optional('violated'):
                                              {'packets': int,
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
#   * 'show policy map control plane'
#   * 'show policy-map interface {interface} output class {class_name}'
#   * 'show policy-map interface {interface}'
# =====================================================================
class ShowPolicyMapType(ShowPolicyMapControlPlaneSchema):
    ''' Parser for
        * "show policy map control plane"
        * "show policy-map interface {interface} output class {class_name}"
        * "show policy-map interface {interface}"
    '''

    cli_command = ['show policy-map interface {interface} output class {class_name}',
                   'show policy-map interface {interface}',
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
        p0 = re.compile(r'^(?P<top_level>(Control Plane|GigabitEthernet.*))$')

        # Service-policy input: Control_Plane_In
        # Service-policy output: shape-out
        # Service-policy input:TEST
        p1 = re.compile(r'^Service-policy +(?P<service_policy>(input|output)):+ *(?P<policy_name>([\w\-]+))$')

        # Class-map: Ping_Class (match-all)
        # Class-map:TEST (match-all)
        p2 = re.compile(r'^Class-map *:+(?P<class_map>([\s\w\-]+)) +(?P<match_all>(.*))$')

        # 8 packets, 800 bytes
        p3 = re.compile(r'^(?P<packets>(\d+)) packets, (?P<bytes>(\d+)) +bytes')

        # 5 minute offered rate 0000 bps, drop rate 0000 bps
        p4 = re.compile(r'^(?P<interval>(\d+)) +minute +offered +rate +(?P<offered_rate>(\d+)) bps, +drop +rate +(?P<drop_rate>(\d+)) bps$')

        # 5 minute offered rate 0000 bps
        p4_1 = re.compile(r'^(?P<interval>(\d+)) +minute +offered +rate +(?P<offered_rate>(\d+)) bps$')

        # Match: access-group name Ping_Option
        p5 = re.compile(r'^Match *:+(?P<match>([\w\-\s]+))$')

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
        p14 = re.compile(r'^ip +precedence +(?P<ip_precedence>(\d+))$')

        # Marker statistics: Disabled
        p15 = re.compile(r'^Marker +statistics: +(?P<marker_statistics>(\w+))$')

        # Queueing
        p16 = re.compile(r'^Queueing$')

        #queue limit 64 packets
        p16_1 = re.compile(r'^queue +limit +(?P<queue_limit>([\s\w]+))$')

        # (queue depth/total drops/no-buffer drops) 0/0/0
        p16_2 = re.compile(r'\(+queue +depth/+total +drops/+no-buffer +drops+\) +(?P<queue_depth>(\d+))/'
                            '+(?P<total_drops>(\d+))/+(?P<no_buffer_drops>(\d+))$')
        # (pkts output/bytes output) 0/0
        p16_3 = re.compile(r'\(+pkts +output/+bytes +output+\) +(?P<pkts_output>(\d+))/+(?P<bytes_output>(\d+))')

        # shape (average) cir 474656, bc 1899, be 1899
        p16_4 = re.compile(r'^shape +\(average\) +cir +(?P<shape_cir_bps>(\d+)), +bc +'
                            '(?P<shape_bc_bps>(\d+)), +be +(?P<shape_be_bps>(\d+))$')

        # target shape rate 474656
        p16_5 = re.compile(r'^target +shape +rate +(?P<target_shape_rate>(\d+))$')

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
                service_policy = group['service_policy']
                policy_name = group['policy_name']
                # Set dict
                service_dict = top_level_dict.setdefault('service_policy', {}).\
                                              setdefault(service_policy, {}).\
                                              setdefault('policy_name', {}).\
                                              setdefault(policy_name, {})
                continue

            # Class-map: Ping_Class (match-all)
            m = p2.match(line)
            if m:
                class_map = m.groupdict()['class_map']
                class_map_dict = service_dict.setdefault('class_map', {}).\
                                              setdefault(class_map, {})
                if "match-all" in m.groupdict()['match_all']:
                    class_map_dict['match_all'] = True
                else:
                    class_map_dict['match_all'] = False
                continue

            # 8 packets, 800 bytes
            m = p3.match(line)
            if m:
                group = m.groupdict()
                packets = group['packets']
                bytes = group['bytes']
                #import pdb;pdb.set_trace()
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

            # Match: access-group name Ping_Option
            m = p5.match(line)
            if m:
                class_map_dict['match'] = m.groupdict()['match']
                continue

            # police:
            m = p6.match(line)
            if m:
                police_dict = class_map_dict.setdefault('police', {})
                continue

            # cir 8000 bps, bc 1500 bytes
            m = p7.match(line)
            if m:
                police_dict['cir_bps'] = int(m.groupdict()['cir_bps'])
                police_dict['bc_bytes'] = int(m.groupdict()['bc_bytes'])
                continue

            # police:  cir 64000 bps, bc 8000 bytes
            m = p6_1.match(line)
            if m:
                police_dict = class_map_dict.setdefault('police', {})
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
            m = p14.match(line)
            if m:
                qos_dict['ip_precedence'] = int(m.groupdict()['ip_precedence'])
                continue

            # Marker statistics: Disabled
            m = p15.match(line)
            if m:
                qos_dict['marker_statistics'] = m.groupdict()['marker_statistics']
                continue

            # Queueing
            m = p16.match(line)
            if m:
                queue_dict = class_map_dict.setdefault('queueing', {})
                continue

            # queue limit 64 packets
            m = p16_1.match(line)
            if m:
                queue_dict['queue_limit'] = m.groupdict()['queue_limit']
                continue

            # (queue depth/total drops/no-buffer drops) 0/0/0
            m = p16_2.match(line)
            if m:
                queue_dict['queue_depth'] = int(m.groupdict()['queue_depth'])
                queue_dict['total_drops'] = int(m.groupdict()['total_drops'])
                queue_dict['no_buffer_drops'] = int(m.groupdict()['no_buffer_drops'])
                continue

            # (pkts output/bytes output) 0/0
            m = p16_3.match(line)
            if m:
                queue_dict['pkts_output'] = int(m.groupdict()['pkts_output'])
                queue_dict['bytes_output'] = int(m.groupdict()['bytes_output'])
                continue

            # shape (average) cir 474656, bc 1899, be 1899
            m = p16_4.match(line)
            if m:
                queue_dict['shape_cir_bps'] = int(m.groupdict()['shape_cir_bps'])
                queue_dict['shape_bc_bps'] = int(m.groupdict()['shape_bc_bps'])
                queue_dict['shape_be_bps'] = int(m.groupdict()['shape_be_bps'])
                continue

            # target shape rate 474656
            m = p16_5.match(line)
            if m:
                queue_dict['target_shape_rate'] = int(m.groupdict()['target_shape_rate'])
                continue

        return ret_dict


# ===================================
# Schema for:
#   * 'show policy-map'
#   * 'show policy-map {name}'
# ===================================
class ShowPolicyMapSchema(MetaParser):

    schema = {
        'policy_map': 
            {Any():
                {'class':
                    {Any():
                        {Optional('priority_level'):
                            {Any():
                                {'kbps': int}},
                        Optional('police'):
                            {Optional('cir_bps'): int,
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
                        Optional('cir_bps'): int,
                        Optional('weighted_fair_queueing'):
                            {'bandwidth_percent': int,
                             'exponential_weight': int,
                             'explicit_congestion_notification': bool,
                             'class':
                                 {Any():
                                     {'min_threshold': str,
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
                           '+(?P<mark_probability>([\d\/]+))')

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