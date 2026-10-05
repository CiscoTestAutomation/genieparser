"""show_policy_map.py

NXOS parsers for the following show commands:
    * show policy-map interface control-plane
"""

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, ListOf


# ==========================================================
# Schema for:
#   * show policy-map interface control-plane
# ==========================================================
class ShowPolicyMapInterfaceControlPlaneSchema(MetaParser):
    """Schema for show policy-map interface control-plane"""

    schema = {
        'control_plane': {
            'service_policy': {
                Any(): {
                    'policy_name': str,
                    Optional('class_map'): {
                        Any(): {
                            'match_type': str,
                            Optional('matches'): ListOf(str),
                            'set_cos': int,
                            'police': {
                                'cir': int,
                                'cir_unit': str,
                                'bc': int,
                                'bc_unit': str,
                            },
                            'module': {
                                Any(): {
                                    Optional('transmitted_bytes'): int,
                                    Optional('transmitted_packets'): int,
                                    Optional('offered_rate'): {
                                        'interval': str,
                                        'rate': int,
                                        'unit': str,
                                    },
                                    Optional('conformed'): {
                                        'peak_rate': int,
                                        'unit': str,
                                        Optional('time'): str,
                                    },
                                    Optional('dropped_bytes'): int,
                                    Optional('dropped_packets'): int,
                                    Optional('violate_rate'): {
                                        'interval': str,
                                        'rate': int,
                                        'unit': str,
                                    },
                                    Optional('violated'): {
                                        'peak_rate': int,
                                        'unit': str,
                                        Optional('time'): str,
                                    },
                                },
                            },
                        },
                    },
                },
            },
        },
    }


# ==========================================================
# Parser for:
#   * show policy-map interface control-plane
# ==========================================================
class ShowPolicyMapInterfaceControlPlane(
    ShowPolicyMapInterfaceControlPlaneSchema
):
    """Parser for show policy-map interface control-plane"""

    cli_command = 'show policy-map interface control-plane'

    def cli(self, command='', output=None, **kwargs):
        if output is None:
            command = command or self.cli_command
            output = self.device.execute(command)

        ret_dict = {}
        service_policy_dict = None
        class_map_dict = None
        module_dict = None
        current_peak_dict = None

        # Control Plane
        p1 = re.compile(r'^Control +Plane$')

        # Service-policy  input: copp-system-p-policy-strict
        p2 = re.compile(
            r'^Service-policy +(?P<direction>\S+): +'
            r'(?P<policy_name>\S+)$'
        )

        # class-map copp-system-p-class-l3uc-data (match-any)
        p3 = re.compile(
            r'^class-map +(?P<class_map>\S+) +'
            r'\((?P<match_type>[^)]+)\)$'
        )

        # match exception glean
        # match access-group name copp-system-p-acl-bgp
        p4 = re.compile(r'^match +(?P<match>[^\r\n]+)$')

        # set cos 1
        p5 = re.compile(r'^set +cos +(?P<cos>\d+)$')

        # police cir 800 kbps , bc 32000 bytes
        # police cir 50 mbps , bc 8192000 bytes
        p6 = re.compile(
            r'^police +cir +(?P<cir>\d+) +(?P<cir_unit>\S+) +, +'
            r'bc +(?P<bc>\d+) +(?P<bc_unit>\S+)$'
        )

        # module 1 :
        p7 = re.compile(r'^module +(?P<module>\d+) *:$')

        # transmitted 0 bytes;
        # transmitted 0 packets;
        p8 = re.compile(
            r'^transmitted +(?P<transmitted>\d+) +'
            r'(?P<unit>bytes|byte|packets|packet);$'
        )

        # 5-minute offered rate 0 bytes/sec
        p9 = re.compile(
            r'^(?P<interval>\S+) +offered +rate +(?P<rate>\d+) +(?P<unit>\S+)$'
        )

        # conformed 0 peak-rate bytes/sec
        # violated 0 peak-rate byte/sec
        p10 = re.compile(
            r'^(?P<counter>conformed|violated) +(?P<peak_rate>\d+) +'
            r'peak-rate +(?P<unit>\S+)$'
        )

        # at Fri Sep 04 09:42:34 2026
        p11 = re.compile(r'^at +(?P<time>[^\r\n]+)$')

        # dropped 0 bytes;
        # dropped 0 packets;
        p12 = re.compile(
            r'^dropped +(?P<dropped>\d+) +'
            r'(?P<unit>bytes|byte|packets|packet);$'
        )

        # 5-min violate rate 0 byte/sec
        p13 = re.compile(
            r'^(?P<interval>\S+) +violate +rate +(?P<rate>\d+) +(?P<unit>\S+)$'
        )

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # Control Plane
            m = p1.match(line)
            if m:
                continue

            # Service-policy  input: copp-system-p-policy-strict
            m = p2.match(line)
            if m:
                groups = m.groupdict()
                service_policy_dict = ret_dict.setdefault(
                    'control_plane', {}
                ).setdefault(
                    'service_policy', {}
                ).setdefault(groups['direction'], {})
                service_policy_dict['policy_name'] = groups['policy_name']
                class_map_dict = None
                module_dict = None
                current_peak_dict = None
                continue

            # class-map copp-system-p-class-l3uc-data (match-any)
            m = p3.match(line)
            if m and service_policy_dict is not None:
                groups = m.groupdict()
                class_map_dict = service_policy_dict.setdefault(
                    'class_map', {}
                ).setdefault(groups['class_map'], {})
                class_map_dict['match_type'] = groups['match_type']
                module_dict = None
                current_peak_dict = None
                continue

            # match exception glean
            # match access-group name copp-system-p-acl-bgp
            m = p4.match(line)
            if m and class_map_dict is not None:
                groups = m.groupdict()
                matches = class_map_dict.setdefault('matches', [])
                matches.append(groups['match'])
                continue

            # set cos 1
            m = p5.match(line)
            if m and class_map_dict is not None:
                groups = m.groupdict()
                class_map_dict['set_cos'] = int(groups['cos'])
                continue

            # police cir 800 kbps , bc 32000 bytes
            # police cir 50 mbps , bc 8192000 bytes
            m = p6.match(line)
            if m and class_map_dict is not None:
                groups = m.groupdict()
                class_map_dict['police'] = {
                    'cir': int(groups['cir']),
                    'cir_unit': groups['cir_unit'],
                    'bc': int(groups['bc']),
                    'bc_unit': groups['bc_unit'],
                }
                continue

            # module 1 :
            m = p7.match(line)
            if m and class_map_dict is not None:
                groups = m.groupdict()
                module_dict = class_map_dict.setdefault('module', {}) \
                    .setdefault(int(groups['module']), {})
                current_peak_dict = None
                continue

            # transmitted 0 bytes;
            # transmitted 0 packets;
            m = p8.match(line)
            if m and module_dict is not None:
                groups = m.groupdict()
                unit = (
                    'packets'
                    if groups['unit'].startswith('packet')
                    else 'bytes'
                )
                key = 'transmitted_{}'.format(unit)
                module_dict[key] = int(groups['transmitted'])
                continue

            # 5-minute offered rate 0 bytes/sec
            m = p9.match(line)
            if m and module_dict is not None:
                groups = m.groupdict()
                module_dict['offered_rate'] = {
                    'interval': groups['interval'],
                    'rate': int(groups['rate']),
                    'unit': groups['unit'],
                }
                continue

            # conformed 0 peak-rate bytes/sec
            # violated 0 peak-rate byte/sec
            m = p10.match(line)
            if m and module_dict is not None:
                groups = m.groupdict()
                current_peak_dict = module_dict.setdefault(
                    groups['counter'], {}
                )
                current_peak_dict.update({
                    'peak_rate': int(groups['peak_rate']),
                    'unit': groups['unit'],
                })
                continue

            # at Fri Sep 04 09:42:34 2026
            m = p11.match(line)
            if m and current_peak_dict is not None:
                groups = m.groupdict()
                current_peak_dict['time'] = groups['time']
                continue

            # dropped 0 bytes;
            # dropped 0 packets;
            m = p12.match(line)
            if m and module_dict is not None:
                groups = m.groupdict()
                unit = (
                    'packets'
                    if groups['unit'].startswith('packet')
                    else 'bytes'
                )
                key = 'dropped_{}'.format(unit)
                module_dict[key] = int(groups['dropped'])
                continue

            # 5-min violate rate 0 byte/sec
            m = p13.match(line)
            if m and module_dict is not None:
                groups = m.groupdict()
                module_dict['violate_rate'] = {
                    'interval': groups['interval'],
                    'rate': int(groups['rate']),
                    'unit': groups['unit'],
                }
                continue

        return ret_dict
