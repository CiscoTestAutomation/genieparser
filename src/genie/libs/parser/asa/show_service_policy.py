''' show_service_policy.py

Parser for the following show commands:
    * show service-policy
'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import (Schema, 
                                                Any,
                                                Optional)

# =============================================
# Schema for 'show service-policy'
# =============================================
class ShowServicePolicySchema(MetaParser):
    """Schema for
        * show service-policy
    """

    schema = {
        'global_policy': {
            'service_policy': {
                str: {
                    'class_map': {
                        str: {
                            'inspect': {
                                str: {
                                    Optional('inspect_map'): str,
                                    'packet': int,
                                    'lock_fail': int,
                                    'drop': int,
                                    'reset_drop': int,
                                    'five_minute_pkt_rate': int,
                                    'v6_fail_close': int,
                                    'sctp_drop_override': int,
                                    Optional('tcp_proxy'): {
                                        'bytes_in_buffer': int,
                                        'bytes_dropped': int,
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

# =============================================
# Parser for 'show service-policy'
# =============================================
class ShowServicePolicy(ShowServicePolicySchema):
    """Parser for
        * show service-policy
    """

    cli_command = 'show service-policy'

    def cli(self, output=None):
        if output is None:
            # execute command to get output
            out = self.device.execute(self.cli_command)
        else:
            out = output

        ret_dict = {}
        inspect_index = 0

        # Service-policy: global_policy
        p1 = re.compile(r'Service-policy: +(?P<service_policy>\S+)$')

        # Class-map: inspection_default
        p2 = re.compile(r'^Class-map: (?P<class_map>\S+)$')

        # Inspect: ip-options _default_ip_options_map, packet 0, lock fail 0, drop 0, reset-drop 0, 
        # 5-min-pkt-rate 0 pkts/sec, v6-fail-close 0 sctp-drop-override 0
        p3 = re.compile(r'^Inspect: +(((?P<inspect_3>\S+ +\S+) +(?P<map_3>\S+))|'
                        r'((?P<inspect_2>\S+) +(?P<map_2>\S+))|(?P<inspect_1>\S+)) *, +'
                        r'packet +(?P<packet>\d+), +lock +fail +(?P<lock_fail>\d+), +'
                        r'drop +(?P<drop>\d+), +reset-drop +(?P<reset_drop>\d+), +'
                        r'5-min-pkt-rate +(?P<five_minute_pkt_rate>\d+) +pkts\/sec, +'
                        r'v6-fail-close +(?P<v6_fail_close>\d+) +sctp-drop-override +'
                        r'(?P<sctp_drop_override>\d+)$')

        # tcp-proxy: bytes in buffer 0, bytes dropped 0
        p4 = re.compile(r'^tcp-proxy: +bytes +in +buffer +(?P<bytes_in_buffer>\d+), +'
                        r'bytes +dropped +(?P<bytes_dropped>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # Service-policy: global_policy
            m = p1.match(line)
            if m:
                group = m.groupdict()
                service_policy = group['service_policy']
                service_policy_dict = ret_dict.setdefault('global_policy', {}). \
                    setdefault('service_policy', {}). \
                        setdefault(service_policy, {})
                continue

            # Class-map: inspection_default
            m = p2.match(line)
            if m:
                group = m.groupdict()
                class_map = group['class_map']
                class_map_dict = service_policy_dict.setdefault('class_map', {}). \
                    setdefault(class_map, {})
                continue

            # Inspect: ip-options _default_ip_options_map, packet 0, lock fail 0, drop 0, reset-drop 0, 
            # 5-min-pkt-rate 0 pkts/sec, v6-fail-close 0 sctp-drop-override 0
            p3 = re.compile(r'^Inspect: +(((?P<inspect_3>\S+ +\S+) +(?P<map_3>\S+))|'
                        r'((?P<inspect_2>\S+) +(?P<map_2>\S+))|(?P<inspect_1>\S+)) *, +'
                        r'packet +(?P<packet>\d+), +lock +fail +(?P<lock_fail>\d+), +'
                        r'drop +(?P<drop>\d+), +reset-drop +(?P<reset_drop>\d+), +'
                        r'5-min-pkt-rate +(?P<five_minute_pkt_rate>\d+) +pkts\/sec, +'
                        r'v6-fail-close +(?P<v6_fail_close>\d+) +sctp-drop-override +'
                        r'(?P<sctp_drop_override>\d+)$')
            m = p3.match(line)
            if m:
                group = m.groupdict()
                # inspect_index += 1
                inspect_3 = group.get('inspect_3', None)
                map_3 = group.get('map_3', None)
                inspect_2 = group.get('inspect_2', None)
                map_2 = group.get('map_2', None)
                inspect_1 = group.get('inspect_1', None)
                
                if inspect_3:
                    inspect_dict = class_map_dict.setdefault('inspect', {}). \
                        setdefault(inspect_3, {})
                    inspect_dict.update({'inspect_map': map_3})
                elif inspect_2:
                    inspect_dict = class_map_dict.setdefault('inspect', {}). \
                        setdefault(inspect_2, {})
                    inspect_dict.update({'inspect_map': map_2})
                else:
                    inspect_dict = class_map_dict.setdefault('inspect', {}). \
                        setdefault(inspect_1, {})
                inspect_dict.update({'packet': int(group['packet'])})
                inspect_dict.update({'lock_fail': int(group['lock_fail'])})
                inspect_dict.update({'drop': int(group['drop'])})
                inspect_dict.update({'reset_drop': int(group['reset_drop'])})
                inspect_dict.update({'five_minute_pkt_rate': int(group['five_minute_pkt_rate'])})
                inspect_dict.update({'v6_fail_close': int(group['v6_fail_close'])})
                inspect_dict.update({'sctp_drop_override': int(group['sctp_drop_override'])})
                continue

            # tcp-proxy: bytes in buffer 0, bytes dropped 0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                tcp_proxy_dict = inspect_dict.setdefault('tcp_proxy', {})
                tcp_proxy_dict.update({'bytes_in_buffer': int(group['bytes_in_buffer'])})
                tcp_proxy_dict.update({'bytes_dropped': int(group['bytes_dropped'])})
                continue
        return ret_dict