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


# ===========================================
# Schema for 'show policy map control plane'
# ===========================================
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
                                     'rate':
                                         {'interval': int,
                                          'offered_rate_bps': int,
                                          'drop_rate_bps': int,
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


# ===========================================
# Parser for 'show policy map control plane'
# ===========================================
class ShowPolicyMapControlPlane(ShowPolicyMapControlPlaneSchema):
    ''' Parser for
        * "show policy map control plane"
    '''

    cli_command = 'show policy-map control-plane'

    def cli(self, output=None):
        if output is None:
            cmd = self.cli_command
            # Execute command on device
            out = self.device.execute(cmd)
        else:
            out = output

        # Init vars
        ret_dict = {}
        ret_dict = collections.OrderedDict(ret_dict)

        # Control Plane
        # Interface
        # Something else
        p0 = re.compile(r'^(?P<top_level>(Control Plane|Interface))$')

        # Service-policy input: Control_Plane_In
        # Service-policy output: Control_Plane_Out
        # Service-policy input:TEST
        p1 = re.compile(r'^Service-policy +(?P<service_policy>(input|output)):+ *(?P<policy_name>([\w\-]+))$')

        # Class-map: Ping_Class (match-all)
        # Class-map:TEST (match-all)
        p2 = re.compile(r'^Class-map *:+(?P<class_map>([\s\w\-]+)) +(?P<match_all>(.*))$')

        # 8 packets, 800 bytes
        p3 = re.compile(r'^(?P<packets>(\d+)) packets, (?P<bytes>(\d+)) +bytes')

        # 5 minute offered rate 0000 bps, drop rate 0000 bps
        p4 = re.compile(r'^(?P<interval>(\d+)) +minute +offered +rate +(?P<offered_rate>(\d+)) bps, +drop +rate +(?P<drop_rate>(\d+)) bps$')

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

        return ret_dict


# ===================================
# Schema for:
#   * 'show policy-map'
#   * 'show policy-map {name}'
# ===================================
class ShowPolicyMapSchema(MetaParser):

    schema = {
        'policy_map': 
            {Any(): # policy1
                {'class': 
                    {Any(): # police
                        {Optional('police_cir'): int,
                        Optional('conform_burst'): int,
                        Optional('pir'): int,
                        Optional('peak_burst'): int,
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
            if name and name != 'interface':
                cmd = self.cli_command[0].format(name=name)
            else:
                cmd = self.cli_command[1]
            # Execute command on device
            out = self.device.execute(cmd)
        else:
            out = output

        # Policy Map policy1
        p1 = {}
        
        # Class police
        p2 = {}
   
        # police cir 500000 conform-burst 10000 pir 1000000 peak-burst 10000 conform-action transmit exceed-action set-prec-transmit 2 violate-action drop
        p3 = {}

        # continue parsing


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