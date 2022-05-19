''' show_policy_map.py

IOSXR parser for the following show command:
    * 'show policy-map interface {interface}'
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

# ================================================================================
# Schema for : "show policy-map interface {interface}"
# ================================================================================
class ShowPolicyMapInterfaceSchema(MetaParser):
    '''Schema for:
            * 'show policy-map interface {interface}'
    '''

    schema = {
        'interface':{
            Any(): {
                Optional('service_policy'): {
                    Any():{
                        Optional('policy_status'): str,
                        Optional('policy_name'): {
                            Any(): {
                                Optional('class'): {
                                    Optional(Any()):
                                    {
                                        Optional('classification_statistics'):{
                                            Optional('matched'): Any(),
                                            Optional('transmitted'): Any(),
                                            Optional('total_dropped'): Any()
                                       },
                                        Optional('queueing_statistics'): {
                                            Optional('queue_id'): int,
                                            Optional('high_watermark'): str,
                                            Optional('inst_queue_len'): str,
                                            Optional('avg_queue_len'): str,
                                            Optional('taildropped'): str,
                                            Optional('queue_conform_packets'): int,
                                            Optional('queue_conform_bytes'): int,
                                            Optional('queue_conform_rate'): int,
                                            Optional('red_random_drops_packets'): int,
                                            Optional('red_random_drops_bytes'): int,
                                        },
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }


# =================================================================================
# Parser for:
#   * 'show policy-map interface {interface}'
# ================================================================================
class ShowPolicyMapInterface(ShowPolicyMapInterfaceSchema):
    '''Parser for :
    * show policy-map interface {interface} '''

    cli_command = ['show policy-map interface {interface}']

    def cli(self, interface, output=None):
        if output is None:
            out = self.device.execute(self.cli_command[0].\
                                      format(interface=interface))
        else:
            out = output

        # Initialize dictionary
        ret_dict = {}

        # TenGigE0/2/0/3 direction input: Service Policy not installed
        p1 = re.compile(r'^.*direction +input: +Service +Policy +not +installed$')

        # TenGigE0/2/0/3 direction input: cap
        # GigabitEthernet0/0/0/1 input: 4gig
        p2 = re.compile(r'^.*(direction)? +input: +(?P<input>\w+)$')

        # TenGigE0/2/0/3 output: Service Policy not installed
        p3 = re.compile(r'^.*output: +Service +Policy +not +installed$')

        # TenGigE0/2/0/3 output: cap
        p4 = re.compile(r'^.*output: +(?P<output>[-\w]+)$')

        # Class cap
        p5 = re.compile(r'^Class +(?P<class_name>\D+)$')

        # Matched             : N / A
        p6 = re.compile(r'^Matched\s+: +(?P<matched>[\D\s]+)$')

        # Matched             :                 638/42108                10
        p7 =  re.compile(r'^Matched\s+\:\s+(?P<packets_bytes>[\d\/]+)\s+(?P<rate_kbps>[\d]+)$')

        # Transmitted         : N / A
        p8 = re.compile(r'^Transmitted\s+: +(?P<transmitted>[\D\s]+)$')

        # Transmitted             :                 638/42108                10
        p9 = re.compile(r'^Transmitted\s+\:\s+(?P<packets_bytes>[\d\/]+)\s+(?P<rate_kbps>[\d]+)$')

        # Total Dropped       : N/A
        p10 = re.compile(r'^Total Dropped\s+: +(?P<total_dropped>[\D\s]+)$')

        # Total Dropped             :                 638/42108                10
        p11 = re.compile(r'^Total Dropped\s+\:\s+(?P<packets_bytes>[\d\/]+)\s+(?P<rate_kbps>[\d]+)$')

        # Queue ID                             : 44
        p12 = re.compile(r'^Queue ID\s+: +(?P<queue_id>[\d]+)$')

        # High watermark  (bytes)/(ms)         : 0/0
        p13 = re.compile(r'^High +watermark[\S\D]+:\s+(?P<high_watermark>[\d\S]+)$')

        # Inst-queue-len  (bytes)/(ms)         : 0/0
        p14 = re.compile(r'^Inst-queue-len[\S\D]+:\s+(?P<inst_queue_len>[\d\S]+)$')

        # Avg-queue-len   (bytes)/(ms)         : 0/0
        p15 = re.compile(r'^Avg-queue-len[\S\D]+:\s+(?P<avg_queue_len>[\d\S]+)$')

        # Taildropped(packets/bytes)           : 0/0
        p16 = re.compile(r'^Taildropped[\S\D]+:\s+(?P<taildropped>[\d\S]+)$')

        # Queue(conform)      :                   0/0                    0
        p17 = re.compile(r'^Queue\(conform\)\s*:\s*(?P<packets>\d+)\/(?P<bytes>\d+)\s+(?P<rate>\d+)$')

        # RED random drops(packets/bytes)      : 0/0
        p18 = re.compile(r'^RED\s+random\s+drops\(packets/bytes\)\s*:\s*(?P<packets>\d+)\/(?P<bytes>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # TenGigE0/2/0/3 direction input: Service Policy not installed
            m = p1.match(line)
            if m:
                group = m.group()

                # define interface_dict dictionary
                interface_dict = ret_dict.setdefault('interface', {}). \
                    setdefault(interface, {})

                # define serv_policy_dict dictionary and set to 'service_policy'
                serv_policy_dict = interface_dict.setdefault('service_policy', {}).\
                    setdefault('input', {}). \
                    setdefault('policy_status', 'Service Policy not installed')

                continue

            # TenGigE0/2/0/3 direction input: cap
            m = p2.match(line)
            if m:
                group = m.groupdict()
                input = group['input']

                # define interface_dict dictionary
                interface_dict = ret_dict.setdefault('interface', {}). \
                    setdefault(interface, {})

                # define serv_policy_dict dictionary and set to 'service_policy'
                serv_policy_dict = interface_dict.setdefault('service_policy', {}). \
                    setdefault('input', {})

                # define name_dict dictionary and assigned to serv_policy_dict
                name_dict = serv_policy_dict.setdefault('policy_name', {}). \
                    setdefault(input, {})

            # TenGigE0/2/0/3 output: Service Policy not installed
            m = p3.match(line)
            if m:
                group = m.group()

                # define interface_dict dictionary
                interface_dict = ret_dict.setdefault('interface', {}). \
                    setdefault(interface, {})

                # define serv_policy_dict dictionary and set to 'service_policy'
                serv_policy_dict = interface_dict.setdefault('service_policy', {}). \
                    setdefault('output', {}). \
                    setdefault('policy_status', 'Service Policy not installed')

                continue

            # TenGigE0/2/0/3 output: cap
            m = p4.match(line)
            if m:
                group = m.groupdict()
                output = group['output']

                # define interface_dict dictionary
                interface_dict = ret_dict.setdefault('interface', {}). \
                    setdefault(interface, {})

                # define serv_policy_dict dictionary and set to 'service_policy'
                serv_policy_dict = interface_dict.setdefault('service_policy', {}). \
                    setdefault('output', {})

                # define name_dict dictionary and assigned to serv_policy_dict
                name_dict = serv_policy_dict.setdefault('policy_name', {}).\
                            setdefault(output, {})

                continue

            # Class cap
            m = p5.match(line)
            if m:
                group = m.groupdict()
                class_name = group['class_name']
                class_dict = name_dict.setdefault('class', {}).\
                             setdefault(class_name, {})

                #Initialize Classification statistics
                class_stat_dict = class_dict.setdefault('classification_statistics', {})
                continue

            # Matched             : N / A
            m = p6.match(line)
            if m:
                group = m.groupdict()
                class_stat_dict.update({
                    'matched': group['matched']
                })
                continue

            # Matched             :                 638/42108                10
            m = p7.match(line)
            if m:
                group = m.groupdict()
                match_dict = class_stat_dict.setdefault('matched', {})
                match_dict.update({
                    'packets/bytes': group['packets_bytes'],
                    'rate/kbps': int(group['rate_kbps'])
                })
                continue

            # Transmitted         : N / A
            m = p8.match(line)
            if m:
                group = m.groupdict()
                class_stat_dict.update({
                    'transmitted': group['transmitted']
                })
                continue

            # Transmitted             :                 638/42108                10
            m = p9.match(line)
            if m:
                group = m.groupdict()

                transmit_dict = class_stat_dict.setdefault('transmitted', {})
                transmit_dict.update({
                    'packets/bytes': group['packets_bytes'],
                    'rate/kbps': int(group['rate_kbps'])
                })
                continue

            # Total Dropped       : N/A
            m = p10.match(line)
            if m:
                group = m.groupdict()
                class_stat_dict.update({
                    'total_dropped': group['total_dropped']
                })
                continue

            # Total Dropped             :                 638/42108                10
            m = p11.match(line)
            if m:
                group = m.groupdict()
                total_dict = class_stat_dict.setdefault('total_dropped', {})
                total_dict.update({
                    'packets/bytes': group['packets_bytes'],
                    'rate/kbps': int(group['rate_kbps'])
                })
                continue

            # Queue ID                             : 44
            m = p12.match(line)
            if m:
                group = m.groupdict()

                # Initialize Queueing statistics
                queue_stat_dict = class_dict.setdefault('queueing_statistics', {})
                queue_stat_dict.update({'queue_id': int(group['queue_id'])})
                continue

            # High watermark  (bytes)/(ms)         : 0/0
            m = p13.match(line)
            if m:
                group = m.groupdict()
                queue_stat_dict.update({'high_watermark': group['high_watermark']})
                continue

            # Inst-queue-len  (bytes)/(ms)         : 0/0
            m = p14.match(line)
            if m:
                group = m.groupdict()
                queue_stat_dict.update({'inst_queue_len': group['inst_queue_len']})
                continue

            # Avg-queue-len   (bytes)/(ms)         : 0/0
            m = p15.match(line)
            if m:
                group = m.groupdict()
                queue_stat_dict.update({'avg_queue_len': group['avg_queue_len']})
                continue

            # Taildropped(packets/bytes)           : 0/0
            m = p16.match(line)
            if m:
                group = m.groupdict()
                queue_stat_dict.update({'taildropped': group['taildropped']})
                continue

            # Queue(conform)      :                   0/0                    0
            m = p17.match(line)
            if m:
                group = m.groupdict()
                queue_stat_dict.update({
                    'queue_conform_packets': int(group['packets']),
                    'queue_conform_bytes': int(group['bytes']),
                    'queue_conform_rate': int(group['rate'])
                })
                continue

            # RED random drops(packets/bytes)      : 0/0
            m = p18.match(line)
            if m:
                group = m.groupdict()
                queue_stat_dict.update({
                    'red_random_drops_packets': int(group['packets']),
                    'red_random_drops_bytes': int(group['bytes']),
                })
                continue

        return ret_dict