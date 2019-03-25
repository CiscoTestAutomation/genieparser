''' show_policy_map.py

IOSXE parsers for the following show commands:
    * show policy map control plane

'''


# Python
import re
import xmltodict
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
        'service_policy_input':
            {Any():
                {'class_map':
                    {Any():
                        {'match_all': bool,
                         'packets': int,
                         'bytes': int,
                         'minute': int,
                         'offered_rate': int,
                         'drop_rate': int,
                         'match': str,
                         Optional('qos_set'):
                             {'ip_precedence': int,
                              'marker_statistics': str,
                             },
                         Optional('police'):
                             {'cir_bps': int,
                              'bc_bytes': int,
                              'conformed':
                                  {'packets': int,
                                   'bytes': int,
                                   'bps': int,
                                   'actions': str,
                                  },
                              'exceeded':
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
        }


# ===========================================
# Parser for 'show policy map control plane'
# ===========================================
class ShowPolicyMapControlPlane(ShowPolicyMapControlPlaneSchema):
    ''' Parser for
      "show policy map control plane"
    '''

    cli_command = 'show policy-map control-plane'

    def cli(self, output=None):
        if output is None:
            # Execute command on device
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init vars
        ret_dict = {}

        # Service-policy input: Control_Plane_In
        p1 = re.compile(r'^Service-policy +input: +(?P<service_policy_input>(\w+))$')

        # Class-map: Ping_Class (match-all)
        p2 = re.compile(r'^Class-map: +(?P<class_map>([\s\w\-]+)) +(?P<match_all>(.*))$')

        # 8 packets, 800 bytes
        p3 = re.compile(r'^(?P<packets>(\d+)) packets, (?P<bytes>(\d+)) +bytes')

        # 5 minute offered rate 0000 bps, drop rate 0000 bps
        p4 = re.compile(r'^(?P<minute>(\d+)) +minute +offered +rate +(?P<offered_rate>(\d+)) bps, +drop +rate +(?P<drop_rate>(\d+)) bps$')

        # Match: access-group name Ping_Option
        p5 = re.compile(r'^Match: +(?P<match>([\w\-\s]+))$')

        # police:
        p6 = re.compile(r'^police:+$')

        # cir 8000 bps, bc 1500 bytes
        p7 = re.compile(r'^cir (?P<cir_bps>(\d+)) bps, bc (?P<bc_bytes>(\d+)) bytes$')

        # conformed 8 packets, 800 bytes; actions:
        p8 = re.compile(r'^conformed (?P<packets>(\d+)) packets, +(?P<bytes>(\d+)) bytes; actions:$')

        # exceeded 0 packets, 0 bytes; actions:
        p9 = re.compile(r'^exceeded (?P<packets>(\d+)) packets, +(?P<bytes>(\d+)) bytes; actions:$')

        # conformed 0000 bps, exceeded 0000 bps
        p10=re.compile(r'^conformed +(?P<c_bps>(\d+)) bps, exceeded (?P<e_bps>(\d+)) bps$')

        # drop
        # transmit
        # start
        p11 = re.compile(r'^(?P<action>(drop|transmit|start))$')

        #QoS Set
        p12 = re.compile(r'^QoS +Set+$')

        #ip precedence 6
        p13 = re.compile(r'^ip +precedence +(?P<ip_precedence>(\d+))$')

        #Marker statistics: Disabled
        p14 = re.compile(r'^Marker +statistics: +(?P<marker_statistics>(\w+))$')

        for line in out.splitlines():
            line = line.strip()

            # Service-policy input: Control_Plane_In
            m = p1.match(line)
            if m:
                service_policy_input = m.groupdict()['service_policy_input']
                service_dict = ret_dict.setdefault('service_policy_input', {}).setdefault(service_policy_input, {})
                continue

            # Class-map: Ping_Class (match-all)
            m = p2.match(line)
            if m:
                class_map = m.groupdict()['class_map']
                class_map_dict = service_dict.setdefault('class_map', {}).setdefault(class_map, {})
                if "match-all" in m.groupdict()['match_all']:
                    class_map_dict['match_all'] = True
                else:
                    class_map_dict['match_all'] = False
                continue

            # 8 packets, 800 bytes
            m = p3.match(line)
            if m:
                class_map_dict['packets'] = int(m.groupdict()['packets'])
                class_map_dict['bytes'] = int(m.groupdict()['bytes'])
                continue

            # 5 minute offered rate 0000 bps, drop rate 0000 bps
            m = p4.match(line)
            if m:
                class_map_dict['minute'] = int(m.groupdict()['minute'])
                class_map_dict['offered_rate'] = int(m.groupdict()['offered_rate'])
                class_map_dict['drop_rate'] = int(m.groupdict()['drop_rate'])
                continue

            # Match: access-group name Ping_Option
            m = p5.match(line)
            if m:
                class_map_dict['match'] = str(m.groupdict()['match'])
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

            # conformed 8 packets, 800 bytes; actions:
            m = p8.match(line)
            if m:
                conformed_line = True
                exceeded_line = False
                conformed_dict = police_dict.setdefault('conformed', {})
                conformed_dict['packets'] = int(m.groupdict()['packets'])
                conformed_dict['bytes'] = int(m.groupdict()['bytes'])
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

            # conformed 0000 bps, exceeded 0000 bps
            m = p10.match(line)
            if m:
                conformed_dict['bps'] = int(m.groupdict()['c_bps'])
                exceeded_dict['bps'] = int(m.groupdict()['e_bps'])
                continue

            # drop
            # transmit
            # start
            m=p11.match(line)
            if m:
                if conformed_line:
                    conformed_dict['actions'] = m.groupdict()['action']
                elif exceeded_line:
                    exceeded_dict['actions'] = m.groupdict()['action']
                continue

            # QoS Set
            m = p12.match(line)
            if m:
                qos_dict = class_map_dict.setdefault('qos_set', {})
                continue

            # ip precedence 6
            m = p13.match(line)
            if m:
                qos_dict['ip_precedence'] = int(m.groupdict()['ip_precedence'])
                continue

            # Marker statistics: Disabled
            m = p14.match(line)
            if m:
                qos_dict['marker_statistics'] = str(m.groupdict()['marker_statistics'])
                continue

        return ret_dict
