"""  show_clns.py
   supported commands:
        *  show clns interface
        *  show clns interface <interface>
        *  show clns protocol
        *  show clns neighbors detail
        *  show clns is-neighbors detail
        *  show clns traffic
"""

import re

from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, \
                                               Any, \
                                               Optional

from genie.libs.parser.utils.common import Common


class ShowClnsInterfaceSchema(MetaParser):
    """Schema for show clns interface,
                  show clns interface {interface}"""

    schema = {
        'interfaces':{
            Any():{
                'status':str,
                'line_protocol': str,
                Optional('clns_protocol_processing'): bool,
                Optional('checksum_enabled'): bool,
                Optional('mtu'): int,
                Optional('encapsulation'): str,
                Optional('erpdus_enabled'): bool,
                Optional('min_interval_msec'): int,
                Optional('clns_fast_switching'): bool,
                Optional('clns_sse_switching'): bool,
                Optional('dec_compatibility_mode'): str,
                Optional('next_esh_ish_in'): int,
                Optional('routing_protocol'): {
                    Any(): {
                        'process_id': {
                            Any(): {
                                'level_type': str,
                                'interface_number': str,
                                'local_circuit_id': str,
                                Optional('neighbor_extended_local_circuit_id'): str,
                                Optional('if_state'): str,
                                'hello_interval': {
                                    Any(): {
                                        Optional('next_is_is_lan_hello_in'): int,
                                        Optional('next_is_is_lan_hello_in_ms'): int,
                                    },
                                    Optional('next_is_is_hello_in'): int,
                                    Optional('next_is_is_hello_in_ms'): int,
                                },
                                Any(): {  # level-1 , level-2
                                    'metric': int,
                                    Optional('dr_id'): str,
                                    'circuit_id': str,
                                    'ipv6_metric': int,
                                },
                                'priority': {
                                    Any(): {  # level-1 , level-2
                                        'priority': int,
                                    },
                                },
                                Optional('adjacencies'): {
                                    Any(): {   # level-1 level-2
                                        'number_of_active_adjancies': int
                                    },
                                }
                            }
                        },
                    }
                }
            }
        }
    }

class ShowClnsInterface(ShowClnsInterfaceSchema):
    """Parser for show clns interface
                  show clns interface {interface}"""

    cli_command = ['show clns interface {interface}','show clns interface']
    exclude = ['next_esh_ish_in', 'next_is_is_lan_hello_in', 'next_is_is_lan_hello_in_ms']

    def cli(self,interface="",output=None):
        if output is None:
            if interface:
                cmd = self.cli_command[0].format(interface=interface)
            else:
                cmd = self.cli_command[1]

            out = self.device.execute(cmd)
        else:
            out = output

        # initial return dictionary
        result_dict = {}
        flag_level_1 = False
        flag_level_2 = False

        # GigabitEthernet1 is up, line protocol is up
        # TokenRing 0 is administratively down, line protocol is down
        p1 = re.compile(r'^(?P<interface>[\w]+[\d/.|\s]+) +is +'
                        r'(?P<status>[\w\s]+), +line +protocol +is +'
                        r'(?P<line_protocol>\w+)$')
        #   CLNS protocol processing disabled
        p2 = re.compile(r'^CLNS +protocol +processing +disabled$')
        #   Checksums enabled, MTU 1497, Encapsulation SAP
        p3 = re.compile(r'^Checksums +(?P<checksum>\w+), +MTU +(?P<mtu>\d+), '
                        r'+Encapsulation +(?P<encapsulation>\w+)$')
        #   ERPDUs enabled, min. interval 10 msec.
        p4 = re.compile(r'^ERPDUs +(?P<erpdus>\w+), +min. +interval +'
                        r'(?P<min_interval>\d+) +msec.$')
        #   CLNS fast switching enabled
        #   CLNS SSE switching disabled
        p5 = re.compile(r'^CLNS +(?P<fast_sse>\w+) +switching +'
                        r'(?P<switching_status>\w+)$')
        #   DEC compatibility mode OFF for this interface
        p6 = re.compile(r'^DEC +compatibility +mode +'
                        r'(?P<dec_compatibilty_mod>\w+) +for +this +interface$')
        #   Next ESH/ISH in 20 seconds
        p7 = re.compile(r'^Next +ESH/ISH +in +(?P<next_esh_ish>\d+) +seconds$')
        #   Routing Protocol: IS-IS (test)
        p8 = re.compile(r'^Routing +Protocol: +(?P<routing_protocol>[\S]+)'
                        r'( +\((?P<process_id>\w+)\))?$')
        #     Circuit Type: level-1-2
        p9 = re.compile(r'^Circuit +Type: +(?P<circuit_type>\S+)$')
        #     Interface number 0x1, local circuit ID 0x1
        p10 = re.compile(r'^Interface +number +(?P<interface_number>\w+), '
                         r'+local +circuit +ID +(?P<local_circuit>\w+)$')
        #     Neighbor Extended Local Circuit ID: 0x0
        p11 = re.compile(r'^Neighbor +Extended +Local +Circuit +ID: +'
                         r'(?P<neighbor_extended_local_circute_id>\w+)$')
        #     Level-1 Metric: 10, Priority: 64, Circuit ID: R2.01
        p12 = re.compile(r'^(?P<level>\S+) +Metric: +(?P<level_metric>\d+), '
                         r'+Priority: +(?P<priority>\d+), +Circuit +ID:'
                         r' +(?P<circuit_id>\S+)$')
        #     DR ID: R2.01
        p13 = re.compile(r'^DR +ID: +(?P<dr_id>\S+)$')
        #     Level-1 IPv6 Metric: 10
        p14 = re.compile(r'^(?P<level>\S+) +IPv6 +Metric: +'
                         r'(?P<level_ipv6_metric>\d+)$')
        #     Number of active level-1 adjacencies: 1
        p15 = re.compile(r'^Number +of +active +(?P<level>\S+) +adjacencies: '
                         r'+(?P<adjacencies>\d+)$')
        #     Next IS-IS LAN Level-1 Hello in 1 seconds
        #     Next IS-IS LAN Level-2 Hello in 645 milliseconds
        p16 = re.compile(r'^Next +IS\-IS +LAN (?P<level>\S+) +Hello +in +'
                         r'(?P<level_hello>\d+) +(?P<milli>[\w\(\)]+)?seconds$')
        # Next IS-IS Hello in 0 seconds
        p17 = re.compile(r'Next\s+IS\-IS\s+Hello\s+in\s+(?P<hello>\d+)\s+'
                         r'(?P<milli>[\w\(\)]+)?seconds')
        # if state DOWN
        p18 = re.compile(r'if\s+state\s+(?P<if_state>DOWN|UP)')       

        for line in out.splitlines():
            line = line.strip()

            # GigabitEthernet1 is up, line protocol is up
            m = p1.match(line)
            if m:
                group = m.groupdict()
                clns_dict = result_dict.setdefault('interfaces', {}).setdefault(group['interface'], {})
                clns_dict.update({'line_protocol': group['line_protocol']})
                clns_dict.update({'status': group['status']})
                continue

            #   CLNS protocol processing disabled
            m = p2.match(line)
            if m:
                clns_dict.update({'clns_protocol_processing': False})
                continue

            #   Checksums enabled, MTU 1497, Encapsulation SAP
            m = p3.match(line)
            if m:
                group = m.groupdict()
                clns_dict.update({'checksum_enabled': True if 'enabled' in group['checksum'] else False})
                clns_dict.update({'mtu': int(group['mtu'])})
                clns_dict.update({'encapsulation': group['encapsulation']})
                continue

            #   ERPDUs enabled, min. interval 10 msec.
            m = p4.match(line)
            if m:
                group = m.groupdict()
                clns_dict.update({'erpdus_enabled': True if 'enabled' in group['erpdus'] else False})
                clns_dict.update({'min_interval_msec': int(group['min_interval'])})
                continue

            #   CLNS fast switching enabled
            #   CLNS SSE switching disabled
            m = p5.match(line)
            if m:
                group = m.groupdict()
                fast_sse =  group['fast_sse'].lower()
                clns_dict.update({'clns_{}_switching'.format(fast_sse): True if 'enabled' in group['switching_status'] else False})
                continue

            #   DEC compatibility mode OFF for this interface
            m = p6.match(line)
            if m:
                group = m.groupdict()
                clns_dict.update({'dec_compatibility_mode': group['dec_compatibilty_mod']})
                continue

            #   Next ESH/ISH in 20 seconds
            m = p7.match(line)
            if m:
                group = m.groupdict()
                clns_dict.update({'next_esh_ish_in': int(group['next_esh_ish'])})
                continue

            # Routing Protocol: IS-IS (test)
            # Routing Protocol: IS-IS
            m = p8.match(line)
            if m:
                group = m.groupdict()
                if not group['process_id']:
                    process_id = ""
                else:
                    process_id = group['process_id']
                isis_dict = clns_dict.setdefault('routing_protocol',{}).\
                                      setdefault(group['routing_protocol'],{}).\
                                      setdefault('process_id' ,{}).setdefault(process_id, {})
                continue

            #     Circuit Type: level-1-2
            m = p9.match(line)
            if m:
                group = m.groupdict()
                isis_dict.update({'level_type': group['circuit_type']})
                continue

            #     Interface number 0x1, local circuit ID 0x1
            m = p10.match(line)
            if m:
                group = m.groupdict()
                isis_dict.update({'interface_number': group['interface_number']})
                isis_dict.update({'local_circuit_id': group['local_circuit']})
                continue

            #     Neighbor Extended Local Circuit ID: 0x0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                isis_dict.update({'neighbor_extended_local_circuit_id': group['neighbor_extended_local_circute_id']})
                continue

            #     Level-1 Metric: 10, Priority: 64, Circuit ID: R2.01
            m = p12.match(line)
            if m:
                group = m.groupdict()
                level = group['level'].lower()
                if 'level-1' in level:
                    flag_level_1 = True
                    flag_level_2 = False

                if 'level-2' in level:
                    flag_level_2 = True
                    flag_level_1 = False

                level_dict = isis_dict.setdefault( level, {})
                level_dict.update({'metric': int(group['level_metric'])})
                level_dict.update({'circuit_id': group['circuit_id']})
                priority_dict = isis_dict.setdefault('priority', {}).setdefault(level, {})
                priority_dict.update({'priority': int(group['priority'])})
                continue

            #     DR ID: R2.01
            m = p13.match(line)
            if m:
                group = m.groupdict()
                if flag_level_1:
                    level_dict = isis_dict.setdefault('level-1', {})
                if flag_level_2:
                    level_dict = isis_dict.setdefault('level-2', {})

                level_dict.update({'dr_id': group['dr_id']})
                continue

            #     Level-1 IPv6 Metric: 10
            m = p14.match(line)
            if m:
                group = m.groupdict()
                level_dict = isis_dict.setdefault(group['level'].lower(),{})
                level_dict.update({'ipv6_metric': int(group['level_ipv6_metric'])})
                continue

            #     Number of active level-1 adjacencies: 1
            m = p15.match(line)
            if m:
                group = m.groupdict()
                active_dict = isis_dict.setdefault('adjacencies',{}).setdefault(group['level'].lower(), {})
                active_dict.update({'number_of_active_adjancies': int(group['adjacencies'])})
                continue

            # Next IS-IS LAN Level-1 Hello in 1 seconds
            m = p16.match(line)
            if m:
                group = m.groupdict()
                next_dict = isis_dict.setdefault('hello_interval', {}).setdefault(group['level'].lower(), {})
                if group['milli']:
                    if 'milli' in group['milli']:
                        next_dict.update({'next_is_is_lan_hello_in_ms': int(group['level_hello'])})
                else:
                    next_dict.update({'next_is_is_lan_hello_in': int(group['level_hello'])})
                continue

            # Next IS-IS Hello in 0 seconds
            m = p17.match(line)
            if m:
                group = m.groupdict()
                hello = group['hello']
                next_dict = isis_dict\
                    .setdefault('hello_interval', {})
                if group['milli']:
                    if 'milli' in group['milli']:
                        next_dict['next_is_is_hello_in_ms'] = int(hello)
                else:
                    next_dict['next_is_is_hello_in'] = int(hello)
                continue

            # if state DOWN
            m = p18.match(line)
            if m:
                group = m.groupdict()
                isis_dict['if_state'] = group['if_state'].title()
                continue

        return result_dict


class ShowClnsProtocolSchema(MetaParser):
    """Schema for show clns protocol"""

    schema = {
        'instance': {
             Any(): {
                'system_id': str,
                'nsel': str,
                Optional('process_handle'): str,
                'is_type': str,
                Optional('manual_area_address'): list,
                Optional('routing_for_area_address'): list,
                Optional('interfaces'): {
                    Any(): {
                        'topology': list,
                    },
                },
                'redistribute': str,
                'distance_for_l2_clns_routes': int,
                'rrr_level': str,
                'metrics': {
                  'generate_narrow': str,
                  'accept_narrow': str,
                  'generate_wide': str,
                  'accept_wide': str,
                }
            }
        }
    }

class ShowClnsProtocol(ShowClnsProtocolSchema):
    """Parser for show clns protocol"""

    cli_command = 'show clns protocol'

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        result_dict = {}
        manaual_area_address_flag = False
        routing_area_address_flag = False
        redistribute = False

        # IS-IS Router: VRF1 (0x10001)
        # IS-IS Router: <Null Tag> (0x10000)
        # IS-IS Router: test
        p1 = re.compile(r'^\s*IS-IS Router: +(?P<tag_process>[\S\s]+?)( +\((?P<tag>\w+)\))?$')
        # System Id: 2222.22ff.4444.00  IS-Type: level-1-2
        p2 = re.compile(r'^\s*System Id: +(?P<system_id>[\w\.]+) +IS\-Type: +(?P<is_type>[\w\-]+)$')
        # Manual area address(es):
        p3 = re.compile(r'^\s*Manual +area +address\(es\):$')
        # 49.0001
        p4 = re.compile(r'^\s*(?P<area_address>[\d\.]+)$')
        # Routing for area address(es):
        p5 = re.compile(r'^\s*Routing +for +area +address\(es\):$')
        # Interfaces supported by IS-IS:
        p6 = re.compile(r'^\s*Interfaces +supported +by +IS\-IS:$')
        # GigabitEthernet4 - IP - IPv6
        # Loopback1 - IP - IPv6
        p7 = re.compile(r'^\s*(?P<interface>[A-Za-z]+[\d/.]+) \- +(?P<topology>[\w\-\ ]+)$')
        # Redistribute:
        p8 = re.compile(r'^\s*Redistribute:$')
        #   static (on by default)
        p9 = re.compile(r'^(?P<space>\s{4})(?P<redistribute>[a-z\s\(\)]+)$')
        # Distance for L2 CLNS routes: 110
        p10 = re.compile(r'^\s*Distance +for +L2 +CLNS +routes: +(?P<distance>\d+)$')
        # RRR level: none
        # RRR level: level-1
        p11 = re.compile(r'^\s*RRR +level: +(?P<rrr_level>\S+)$')
        # Generate narrow metrics: none
        p12 = re.compile(r'^\s*Generate +narrow +metrics: +(?P<generate_narrow_metric>\S+)$')
        # Accept narrow metrics:   none
        p13 = re.compile(r'^\s*Accept +narrow +metrics: +(?P<accept_narrow_metric>\S+)$')
        # Generate wide metrics:   level-1-2
        p14 = re.compile(r'^\s*Generate +wide +metrics: +(?P<generate_wide_metric>\S+)$')
        # Accept wide metrics:     level-1-2
        p15 = re.compile(r'^\s*Accept +wide +metrics: +(?P<accept_wide_metric>\S+)$')

        for line in out.splitlines():
            line = line.rstrip()

            # IS-IS Router: VRF1 (0x10001)
            # IS-IS Router: <Null Tag> (0x10000)
            m = p1.match(line)
            if m:
                group = m.groupdict()
                tag_process = group['tag_process']
                tag = group['tag']
                if tag_process == '<Null Tag>':
                    tag_process = 'null'
                clns_dict = result_dict.setdefault('instance', {}).setdefault(tag_process, {})

                if tag:
                    clns_dict.update({'process_handle': tag})
                continue

            # System Id: 2222.22ff.4444.00  IS-Type: level-1-2
            m = p2.match(line)
            if m:
                group = m.groupdict()
                clns_dict.update({'is_type': group['is_type']})
                clns_dict.update({'system_id': group['system_id'][:-3]})
                clns_dict.update({'nsel': group['system_id'][-2:]})
                continue

            # Manual area address(es):
            m = p3.match(line)
            if m:
                manaual_area_address_flag = True
                routing_area_address_flag = False
                manual_area_list = []
                continue

            # 49.0001
            m = p4.match(line)
            if m:
                group = m.groupdict()
                if manaual_area_address_flag:
                    manual_area_list.append(group['area_address'])
                    clns_dict.update({'manual_area_address': manual_area_list})

                if routing_area_address_flag:
                    routing_area_list.append(group['area_address'])
                    clns_dict.update({'routing_for_area_address': routing_area_list})
                continue

            # Routing for area address(es):
            m = p5.match(line)
            if m:
                routing_area_address_flag = True
                manaual_area_address_flag = False
                routing_area_list = []
                continue

            # Interfaces supported by IS-IS:
            m = p6.match(line)
            if m:
                interface_dict = clns_dict.setdefault('interfaces', {})
                continue

            # GigabitEthernet4 - IP - IPv6
            # Loopback1 - IP - IPv6
            m = p7.match(line)
            if m:
                group = m.groupdict()
                topology = group['topology'].lower().split('-')
                interface_dict.setdefault(group['interface'],{}).\
                    update({'topology': [x.strip() if x.strip() !='ip' else 'ipv4' for x in topology ]})
                continue

            # Redistribute:
            m = p8.match(line)
            if m:
                redistribute = True
                continue

            #   static (on by default)
            m = p9.match(line)
            if m:
                group = m.groupdict()
                if redistribute:
                    clns_dict.update({'redistribute': group['redistribute'].strip()})

                redistribute = False
                continue

            # Distance for L2 CLNS routes: 110
            m = p10.match(line)
            if m:
                group = m.groupdict()
                clns_dict.update({'distance_for_l2_clns_routes': int(group['distance'])})
                continue

            # RRR level: none
            # RRR level: level-1
            m = p11.match(line)
            if m:
                group = m.groupdict()
                clns_dict.update({'rrr_level': group['rrr_level']})
                continue

            # Generate narrow metrics: none
            m = p12.match(line)
            if m:
                group = m.groupdict()
                metric_dict = clns_dict.setdefault('metrics', {})
                metric_dict.update({'generate_narrow': group['generate_narrow_metric']})
                continue

            # Accept narrow metrics:   none
            m = p13.match(line)
            if m:
                group = m.groupdict()
                metric_dict = clns_dict.setdefault('metrics', {})
                metric_dict.update({'accept_narrow': group['accept_narrow_metric']})
                continue

            # Generate wide metrics:   level-1-2
            m = p14.match(line)
            if m:
                group = m.groupdict()
                metric_dict = clns_dict.setdefault('metrics', {})
                metric_dict.update({'generate_wide': group['generate_wide_metric']})
                continue

            # Accept wide metrics:     level-1-2
            m = p15.match(line)
            if m:
                group = m.groupdict()
                metric_dict = clns_dict.setdefault('metrics', {})
                metric_dict.update({'accept_wide': group['accept_wide_metric']})
                continue

        return result_dict


class ShowClnsNeighborsDetailSchema(MetaParser):
    """Schema for show clns neighbors detail"""

    schema = {
        'tag': {
            Any(): {
                Optional('system_id'):{
                    Any() : {
                        'type': {
                            Any(): {
                                'interface': str,
                                'state': str,
                                'snpa': str,
                                'holdtime': int,
                                'protocol': str,
                                'area_address': list,
                                Optional('ip_address'): list,
                                Optional('ipv6_address'): list,
                                'uptime': str,
                                Optional('nsf'): str,
                                Optional('topology'): list,
                            }
                        }
                    }
                },
            }
        }
    }

class ShowClnsNeighborsDetail(ShowClnsNeighborsDetailSchema):
    """Parser for show clns neighbors detail"""

    cli_command = 'show clns neighbors detail'

    exclude = ['holdtime', 'uptime', 'chars_in', 'chars_out', 'pkts_in', 'pkts_out']

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        result_dict = {}

        # Tag VRF1:
        p1 = re.compile(r'^Tag +(?P<tag>\S+):$')
        # System Id       Interface     SNPA                State  Holdtime  Type Protocol
        # R7              Gi4           5e00.c0ff.060d      Up     26        L2   M-ISIS
        # R2_xr           Gi2.115       fa16.3eff.9418      Up     26        L1L2 M-ISIS
        # Genie           Te0/3/0       sdfs.0asd.49sd      Up     25        L1   IS-IS //missing neighbor, instead Genie2 shows in JSON.
        p2 = re.compile(r'^(?P<system_id>[\w\.]+) +(?P<interface>\S+) '
                        r'+(?P<snpa>[\w\.]+) +(?P<state>\w+) +'
                        r'(?P<holdtime>\d+) +(?P<level>[L\d]+) +'
                        r'(?P<protocol>[\S ]+)$')
        #   Area Address(es): 49.0002
        p3 = re.compile(r'^Area +Address\(es\): +(?P<area_address>\S+)$')
        #   IP Address(es):  10.229.7.7*
        p4 = re.compile(r'^IP +Address\(es\): +(?P<ip_address>\S+)$')
        #   IPv6 Address(es): FE80::5C00:C0FF:FEFF:60D
        p5 = re.compile(r'^IPv6 +Address\(es\): +(?P<ipv6_address>\S+)$')
        #   Uptime: 00:23:58
        p6 = re.compile(r'^Uptime: +(?P<uptime>[\w\:]+)$')
        #   NSF capable
        p7 = re.compile(r'^NSF +(?P<nsf>\w+)$')
        #   Topology: IPv4, IPv6
        p8 = re.compile(r'^Topology: +(?P<topology>[\S\s]+)$')
        #   Interface name: GigabitEthernet4
        p9 = re.compile(r'^Interface +name: +(?P<interface>\S+)$')
        
        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                clns_dict = result_dict.setdefault('tag', {})\
                                       .setdefault(group['tag'], {})
                continue
            # System Id       Interface     SNPA                State  Holdtime  Type Protocol
            # R7              Gi4           5e00.c0ff.060d      Up     26        L2   M-ISIS
            m = p2.match(line)
            if m:
                group = m.groupdict()
                type_1 = group['level']

                if 'tag' not in result_dict:
                    clns_dict = result_dict.setdefault('tag', {})\
                                          .setdefault("", {})
                type_dict = clns_dict.setdefault('system_id', {})\
                                       .setdefault(group['system_id'],{})\
                                       .setdefault('type', {})\
                                       .setdefault(type_1, {})
                type_dict.update({'holdtime': int(group['holdtime'])})
                type_dict.update({'state': group['state'].lower()})
                type_dict.update({'snpa': group['snpa']})
                type_dict.update({'protocol': group['protocol']})
                type_dict.update({'interface': Common\
                         .convert_intf_name(group['interface'])})

                continue

            #   Area Address(es): 49.0002
            m = p3.match(line)
            if m:
                group = m.groupdict()
                type_dict.update({'area_address': group['area_address'].split()})

                continue

            #   IP Address(es):  10.229.7.7*
            m = p4.match(line)
            if m:
                group = m.groupdict()
                type_dict.update({'ip_address': group['ip_address'].split()})

                continue

            #   IPv6 Address(es): FE80::5C00:C0FF:FEFF:60D
            m = p5.match(line)
            if m:
                group = m.groupdict()
                type_dict.update({'ipv6_address': group['ipv6_address'].split()})

                continue

            #   Uptime: 00:23:58
            m = p6.match(line)
            if m:
                group = m.groupdict()
                type_dict.update({'uptime': group['uptime']})

                continue

            #   NSF capable
            m = p7.match(line)
            if m:
                group = m.groupdict()
                type_dict.update({'nsf': group['nsf']})

                continue

            #   Topology: IPv4, IPv6
            m = p8.match(line)
            if m:
                group = m.groupdict()
                type_dict.update({'topology': group['topology'].lower()\
                         .replace(" ","").split(',')})

                continue

            #   Interface name: GigabitEthernet4
            m = p9.match(line)
            if m:
                group = m.groupdict()
                type_dict.update({'interface': Common\
                         .convert_intf_name(group['interface'])})
                continue
        return result_dict


class ShowClnsIsNeighborsDetailSchema(MetaParser):
    """Schema for show clns is-neighbors detail"""

    schema = {
        'tag': {
            Any(): {
                Optional('system_id'): {
                    Any(): {
                       'type': {
                           Any(): {
                               'interface': str,
                               'state': str,
                               'format': str,
                               'priority': int,
                               'circuit_id': str,
                               'area_address': list,
                               Optional('ip_address'): list,
                               Optional('ipv6_address'): list,
                               'uptime': str,
                               Optional('nsf'): str,
                               Optional('topology'): list,
                           }
                       }
                    }
                }
            }
        }
    }

class ShowClnsIsNeighborsDetail(ShowClnsIsNeighborsDetailSchema):
    """Parser for show clns is-neighbors detail"""

    cli_command = 'show clns is-neighbors detail'

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        result_dict = {}

        # Tag VRF1:
        p1 = re.compile(r'^Tag +(?P<tag>\S+):$')

        # System Id       Interface     State  Type Priority  Circuit Id         Format
        # R7              Gi4           Up     L2   64        R2.01              Phase V
        # R3_nx           Gi3.115       Up     L1L2 64/64     R1_xe.02           Phase V
        p2 = re.compile(r'^(?P<system_id>[\w\.]+)\s+(?P<interface>\S+)\s+'
                        '(?P<state>\w+)\s+(?P<type>\S+)\s+(?P<priority>\d+)'
                        '(\/\d+)*\s+(?P<circuit_id>[\w\.]+)\s+(?P<format>[\S\s]+)$')

        #   Area Address(es): 49.0002
        p3 = re.compile(r'^Area +Address\(es\): +(?P<area_address>\S+)$')

        #   IP Address(es):  10.229.7.7*
        p4 = re.compile(r'^IP +Address\(es\): +(?P<ip_address>\S+)$')

        #   IPv6 Address(es): FE80::5C00:C0FF:FEFF:60D
        p5 = re.compile(r'^IPv6 +Address\(es\): +(?P<ipv6_address>\S+)$')

        #   Uptime: 00:24:24
        p6 = re.compile(r'^Uptime: +(?P<uptime>[\w\:]+)$')

        #   NSF capable
        p7 = re.compile(r'^NSF +(?P<nsf>\w+)$')

        #   Topology: IPv4, IPv6
        p8 = re.compile(r'^Topology: +(?P<topology>[\S\s]+)$')

        #   Interface name: GigabitEthernet4
        p9 = re.compile(r'^Interface +name: +(?P<interface>\S+)$')

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                clns_dict = result_dict.setdefault('tag', {}).setdefault(group['tag'], {})
                continue

            # System Id       Interface     State  Type Priority  Circuit Id         Format
            # R7              Gi4           Up     L2   64        R2.01              Phase V
            m = p2.match(line)
            if m:
                group = m.groupdict()
                if 'tag' not in result_dict:
                     clns_dict = result_dict.setdefault('tag', {}).setdefault("", {})
                type_dict = clns_dict.setdefault('system_id', {}). \
                                      setdefault(group['system_id'], {}). \
                                      setdefault('type', {}). \
                                      setdefault(group['type'], {})

                type_dict.update({'state': group['state'].lower()})
                type_dict.update({'circuit_id': group['circuit_id']})
                type_dict.update({'format': group['format']})
                type_dict.update({'priority': int(group['priority'])})
                type_dict.update({'interface': Common.convert_intf_name(group['interface'])})

                continue

            # Area Address(es): 49.0002
            m = p3.match(line)
            if m:
                group = m.groupdict()
                type_dict.update({'area_address': group['area_address'].split()})
                continue

            # IP Address(es):  10.229.7.7*
            m = p4.match(line)
            if m:
                group = m.groupdict()
                type_dict.update({'ip_address': group['ip_address'].split()})
                continue

            # IPv6 Address(es): FE80::5C00:C0FF:FEFF:60D
            m = p5.match(line)
            if m:
                group = m.groupdict()
                type_dict.update({'ipv6_address': group['ipv6_address'].split()})
                continue

            # Uptime: 00:23:58
            m = p6.match(line)
            if m:
                group = m.groupdict()
                type_dict.update({'uptime': group['uptime']})
                continue

            # NSF capable
            m = p7.match(line)
            if m:
                group = m.groupdict()
                type_dict.update({'nsf': group['nsf']})
                continue

            # Topology: IPv4, IPv6
            m = p8.match(line)
            if m:
                group = m.groupdict()
                type_dict.update({'topology': group['topology'].lower().replace(" ", "").split(',')})
                continue

            # Interface name: GigabitEthernet4
            m = p9.match(line)
            if m:
                group = m.groupdict()
                type_dict.update({'interface': Common.convert_intf_name(group['interface'])})
                continue
        return result_dict


class ShowClnsTrafficSchema(MetaParser):
    """Schema for show clns traffic"""

    schema = {
        'clns': {
            'last_clear': str,
            'output': int,
            'input': int,
            'local': int,
            'forward': int,
            'dropped_protocol': int,
            'discards': {
                'hdr_syntax': int,
                'checksum': int,
                'lifetime': int,
                'output_cngstn': int,
                'no_route': int,
                'discard_route': int,
                'dst_unreachable': int,
                'encaps_failed': int,
                'nlp_unknown': int,
                'not_an_is': int,
            },
            'options': {
                'packets': int,
                'total': int,
                'bad': int,
                'gqos': int,
                'cngstn_exprncd': int,
            },
            'segments': {
                'segmented': int,
                'failed': int,
            },
            'broadcasts': {
                'sent': int,
                'rcvd': int,
            },
        },
        'echos': {
            Any(): {
                'requests': int,
                'replied': int,
            },
        },
        'packet_counters': {
            'level': {
                'level-all': {
                    Any(): {
                        'rcvd': int,
                        'sent': int,
                    },
                },
            },
        },
        'tunneling': {
            Any(): {
                'rcvd': int,
                'sent': int,
                'rcvd_dropped': int,
            },
        },
        'iso-igrp': {
            Any(): {
                'rcvd': int,
                'sent': int,
            },
            'syntax_errors': int
        },
        'tag': {
            Any() : {
                'IS-IS': {
                    'last_clear': str,
                    'hello': {
                        Any(): {
                            'rcvd': int,
                            'sent': int,
                        }
                    },
                    'lsp_sourced': {
                        Any(): {
                            'new': int,
                            'refresh': int,
                        },
                    },
                    'lsp_flooded': {
                        Any(): {
                            'sent': int,
                            'rcvd': int,
                        },
                    },
                    'lsp_retransmissions': int,
                    'csnp': {
                        Any(): {
                            'rcvd': int,
                            'sent': int,
                        },
                    },
                    'psnp': {
                        Any(): {
                            'rcvd': int,
                            'sent': int,
                        },
                    },
                    'dr_election': {
                        Optional('level-1'): int,
                        Optional('level-2'): int,
                    },
                    'spf_calculation': {
                        Optional('level-1'): int,
                        Optional('level-2'): int,
                    },
                    'partial_route_calculation': {
                        Optional('level-1'): int,
                        Optional('level-2'): int,
                    },
                    'lsp_checksum_errors_received': int,
                    'update_process_queue_depth': str,
                    'update_process_packets_dropped': int
                }
            }
        }
    }

class ShowClnsTraffic(ShowClnsTrafficSchema):
    """Parser for show clns traffic"""

    cli_command = 'show clns traffic'

    def cli(self,output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # initial return dictionary
        result_dict = {}

        # CLNS:  Time since last clear: never
        p1 = re.compile(r'^CLNS:  +Time +since +last +clear: (?P<last_clear>\w+)$')
        # CLNS & ESIS Output: 168, Input: 4021
        p2 = re.compile(r'^CLNS \& +ESIS +Output: +(?P<clns_output>\d+), +Input: +(?P<clns_input>\d+)$')
        # Dropped Protocol not enabled on interface: 0
        p3 = re.compile(r'^Dropped Protocol not enabled on interface: +(?P<dropped_protocol>\d+)$')
        # CLNS Local: 0, Forward: 0
        p4 = re.compile(r'^CLNS +Local: +(?P<clns_local>\d+), Forward: +(?P<clns_forward>\d+)$')
        # CLNS Discards:
        p5 = re.compile(r'CLNS +Discards:$')
        #   Hdr Syntax: 0, Checksum: 0, Lifetime: 0, Output cngstn: 0
        p6 = re.compile(r'^Hdr +Syntax: +(?P<hdr_syntax>\d+), +Checksum: +(?P<checksum>\d+),'
                        ' +Lifetime: +(?P<lifetime>\d+), +Output +cngstn: +(?P<output_cngstn>\d+)$')
        #   No Route: 0, Discard Route: 0, Dst Unreachable 0, Encaps. Failed: 0
        p7 = re.compile(r'^No +Route: +(?P<no_route>\d+), +Discard +Route: +(?P<discard_route>\d+),'
                        r' +Dst +Unreachable +(?P<dst_unreachable>\d+), +Encaps. +Failed: +(?P<encaps_failed>\d+)$')
        #   NLP Unknown: 0, Not an IS: 0
        p8 = re.compile(r'^NLP +Unknown: +(?P<nlp_unknown>\d+), +Not +an +IS: +(?P<not_an_is>\d+)$')
        # CLNS Options: Packets 0, total 0 , bad 0, GQOS 0, cngstn exprncd 0
        p9 = re.compile(r'^CLNS +Options: +Packets +(?P<packets>\d+), +total +(?P<total>\d+) ,'
                        r' +bad +(?P<bad>\d+), +GQOS +(?P<gqos>\d+), +cngstn +exprncd +(?P<cngstn_exprncd>\d+)$')
        # CLNS Segments:  Segmented: 0, Failed: 0
        p10 = re.compile(r'^CLNS +Segments:  +Segmented: +(?P<segmented>\d+), +Failed: +(?P<failed>\d+)$')
        # CLNS Broadcasts: sent: 0, rcvd: 0
        p11 = re.compile(r'^CLNS +Broadcasts: sent: +(?P<sent>\d+), +rcvd: +(?P<rcvd>\d+)$')
        # Echos: Rcvd 0 requests, 0 replies
        p12 = re.compile(r'^Echos: +Rcvd +(?P<requests>\d+) +requests, +(?P<replied>\d+) +replies$')
        #       Sent 0 requests, 0 replies
        p13 = re.compile(r'^Sent +(?P<requests>\d+) +requests, +(?P<replied>\d+) +replies$')
        # ESIS(sent/rcvd): ESHs: 0/0, ISHs: 168/0, RDs: 0/0, QCF: 0/0
        p14 = re.compile(r'^ESIS\(sent\/rcvd\): +ESHs: +(?P<esh_sent>\d+)/(?P<esh_rcvd>\d+),'
                         r' +ISHs: +(?P<ish_sent>\d+)/(?P<ish_rcvd>\d+),'
                         r' +RDs: +(?P<rd_sent>\d+)/(?P<rd_rcvd>\d+), +QCF: +(?P<qcf_sent>\d+)/(?P<qcf_rcvd>\d+)$')
        # Tunneling (sent/rcvd): IP: 0/0, IPv6: 0/0
        p15 = re.compile(r'^Tunneling +\(sent\/rcvd\): +IP: +(?P<ip_sent>\d+)/(?P<ip_rcvd>\d+),'
                         r' +IPv6: +(?P<ipv6_sent>\d+)/(?P<ipv6_rcvd>\d+)$')
        # Tunneling dropped (rcvd) IP/IPV6:  0
        p16 = re.compile(r'^Tunneling +dropped +\(rcvd\) +IP\/IPV6:  +(?P<tunneling_dropped>\d+)$')
        # ISO-IGRP: Querys (sent/rcvd): 0/0 Updates (sent/rcvd): 0/0
        p17 = re.compile(r'^ISO-IGRP: +Querys +\(sent\/rcvd\): (?P<query_sent>\d+)/(?P<query_rcvd>\d+)'
                         ' +Updates +\(sent\/rcvd\): +(?P<update_sent>\d+)/(?P<update_rcvd>\d+)$')
        # ISO-IGRP: Router Hellos: (sent/rcvd): 0/0
        p18 = re.compile(r'^ISO-IGRP: +Router +Hellos: +\(sent\/rcvd\): +(?P<hello_sent>\d+)\/+(?P<hello_rcvd>\d+)$')
        # ISO-IGRP Syntax Errors: 0
        p19 = re.compile(r'^ISO\-IGRP +Syntax +Errors: +(?P<syntax_errors>\d+)$')
        # Tag VRF1:
        p20 = re.compile(r'^Tag +(?P<tag>\S+):$')
        #     IS-IS: Time since last clear: never
        p21 = re.compile(r'^IS\-IS: +Time +since +last +clear: +(?P<last_clear>\S+)$')
        #     IS-IS: Level-1 Hellos (sent/rcvd): 497/533
        p22 = re.compile(r'^IS\-IS: +Level\-1 +Hellos \(sent\/rcvd\): +(?P<sent>\d+)\/(?P<rcvd>\d+)$')
        #     IS-IS: Level-2 Hellos (sent/rcvd): 843/611
        p23 = re.compile(r'^IS\-IS: +Level\-2 +Hellos \(sent\/rcvd\): +(?P<sent>\d+)\/(?P<rcvd>\d+)$')
        #     IS-IS: PTP Hellos     (sent/rcvd): 0/0
        p24 = re.compile(r'^IS\-IS: +PTP +Hellos *\(sent\/rcvd\): +(?P<sent>\d+)\/(?P<rcvd>\d+)$')
        #     IS-IS: Level-1 LSPs sourced (new/refresh): 3/4
        p25 = re.compile(r'^IS\-IS: +Level\-1 +LSPs +sourced \(new\/refresh\): +(?P<new>\d+)\/(?P<refresh>\d+)$')
        #     IS-IS: Level-2 LSPs sourced (new/refresh): 4/5
        p26 = re.compile(r'^IS\-IS: +Level\-2 +LSPs +sourced \(new\/refresh\): +(?P<new>\d+)\/(?P<refresh>\d+)$')
        #     IS-IS: Level-1 LSPs flooded (sent/rcvd): 0/0
        p27 = re.compile(r'^IS\-IS: +Level\-1 +LSPs +flooded \(sent\/rcvd\): +(?P<sent>\d+)\/(?P<rcvd>\d+)$')
        #     IS-IS: Level-2 LSPs flooded (sent/rcvd): 5/5
        p28 = re.compile(r'^IS\-IS: +Level\-2 +LSPs +flooded \(sent\/rcvd\): +(?P<sent>\d+)\/(?P<rcvd>\d+)$')
        #     IS-IS: LSP Retransmissions: 0
        p29 = re.compile(r'^IS\-IS: +LSP +Retransmissions: +(?P<lsp_retransmissions>\d+)$')
        #     IS-IS: Level-1 CSNPs (sent/rcvd): 0/0
        p30 = re.compile(r'^IS\-IS: +Level\-1 +CSNPs \(sent\/rcvd\): +(?P<sent>\d+)\/(?P<rcvd>\d+)$')
        #     IS-IS: Level-2 CSNPs (sent/rcvd): 170/0
        p31 = re.compile(r'^IS\-IS: +Level\-2 +CSNPs \(sent\/rcvd\): +(?P<sent>\d+)\/(?P<rcvd>\d+)$')
        #     IS-IS: Level-1 PSNPs (sent/rcvd): 0/0
        p32 = re.compile(r'^IS\-IS: +Level\-1 +PSNPs \(sent\/rcvd\): +(?P<sent>\d+)\/(?P<rcvd>\d+)$')
        #     IS-IS: Level-2 PSNPs (sent/rcvd): 0/0
        p33 = re.compile(r'^IS\-IS: +Level\-2 +PSNPs \(sent\/rcvd\): +(?P<sent>\d+)\/(?P<rcvd>\d+)$')
        #     IS-IS: Level-1 DR Elections: 1
        p34 = re.compile(r'^IS\-IS: +Level\-1 +DR +Elections: +(?P<dr_elections>\d+)$')
        #     IS-IS: Level-2 DR Elections: 2
        p35 = re.compile(r'^IS\-IS: +Level\-2 +DR +Elections: +(?P<dr_elections>\d+)$')
        #     IS-IS: Level-1 SPF Calculations: 14
        p36 = re.compile(r'^IS\-IS: +Level\-1 +SPF +Calculations: +(?P<spf_calculation>\d+)$')
        #     IS-IS: Level-2 SPF Calculations: 17
        p37 = re.compile(r'^IS\-IS: +Level\-2 +SPF +Calculations: +(?P<spf_calculation>\d+)$')
        #     IS-IS: Level-1 Partial Route Calculations: 0
        p38 = re.compile(r'^IS\-IS: +Level\-1 +Partial +Route +Calculations: +(?P<partial_route_calculations>\d+)$')
        #     IS-IS: Level-2 Partial Route Calculations: 1
        p39 = re.compile(r'^IS\-IS: +Level\-2 +Partial +Route +Calculations: +(?P<partial_route_calculations>\d+)$')
        #     IS-IS: LSP checksum errors received: 0
        p40 = re.compile(r'^IS\-IS: +LSP +checksum +errors +received: +(?P<lsp_checksum_errors_received>\d+)$')
        #     IS-IS: Update process queue depth: 0/200
        p41 = re.compile(r'^IS\-IS: +Update +process +queue +depth: +(?P<update_process_queue_depth>[\d\/]+)$')
        #     IS-IS: Update process packets dropped: 0
        p42 = re.compile(r'^IS\-IS: +Update +process +packets +dropped: +(?P<update_process_packets_dropped>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # CLNS:  Time since last clear: never
            m = p1.match(line)
            if m:
                group = m.groupdict()
                clns_dict = result_dict.setdefault('clns', {})
                clns_dict.update({'last_clear': group['last_clear']})
                continue

            # CLNS & ESIS Output: 168, Input: 4021
            m = p2.match(line)
            if m:
                group = m.groupdict()
                clns_dict.update({'input': int(group['clns_input'])})
                clns_dict.update({'output': int(group['clns_output'])})
                continue

            # Dropped Protocol not enabled on interface: 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                clns_dict.update({'dropped_protocol': int(group['dropped_protocol'])})
                continue

            # CLNS Local: 0, Forward: 0
            m = p4.match(line)
            if m:
                group = m.groupdict()
                clns_dict.update({'local': int(group['clns_local'])})
                clns_dict.update({'forward': int(group['clns_forward'])})
                continue

            # CLNS Discards:
            m = p5.match(line)
            if m:
                group = m.groupdict()
                discard_dict = clns_dict.setdefault('discards',{})
                continue

            #   Hdr Syntax: 0, Checksum: 0, Lifetime: 0, Output cngstn: 0
            m = p6.match(line)
            if m:
                group = m.groupdict()
                discard_dict.update({k:int(val) for k,val in group.items()})
                continue

            #   No Route: 0, Discard Route: 0, Dst Unreachable 0, Encaps. Failed: 0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                discard_dict.update({k: int(val) for k, val in group.items()})
                continue

            #   NLP Unknown: 0, Not an IS: 0
            m = p8.match(line)
            if m:
                group = m.groupdict()
                discard_dict.update({k: int(val) for k, val in group.items()})
                continue

            # CLNS Options: Packets 0, total 0 , bad 0, GQOS 0, cngstn exprncd 0
            m = p9.match(line)
            if m:
                group = m.groupdict()
                option_dict = clns_dict.setdefault('options', {})
                option_dict.update({k: int(val) for k, val in group.items()})
                continue

            # CLNS Segments:  Segmented: 0, Failed: 0
            m = p10.match(line)
            if m:
                group = m.groupdict()
                segment_dict = clns_dict.setdefault('segments', {})
                segment_dict.update({k: int(val) for k, val in group.items()})
                continue

            # CLNS Broadcasts: sent: 0, rcvd: 0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                broadcast_dict = clns_dict.setdefault('broadcasts', {})
                broadcast_dict.update({k: int(val) for k, val in group.items()})
                continue

            # Echos: Rcvd 0 requests, 0 replies
            m = p12.match(line)
            if m:
                group = m.groupdict()
                echo_dict = result_dict.setdefault('echos', {}).setdefault('rcvd', {})
                echo_dict.update({k: int(val) for k, val in group.items()})
                continue

            #       Sent 0 requests, 0 replies
            m = p13.match(line)
            if m:
                group = m.groupdict()
                echo_dict = result_dict.setdefault('echos', {}).setdefault('sent', {})
                echo_dict.update({k: int(val) for k, val in group.items()})
                continue

            # ESIS(sent/rcvd): ESHs: 0/0, ISHs: 168/0, RDs: 0/0, QCF: 0/0
            m = p14.match(line)
            if m:
                group = m.groupdict()
                esis_dict = result_dict.setdefault('packet_counters', {}).\
                                        setdefault('level', {}).\
                                        setdefault('level-all', {})
                esis_dict.setdefault('esh', {}).update({'rcvd': int(group['esh_rcvd'])})
                esis_dict.setdefault('esh', {}).update({'sent': int(group['esh_sent'])})
                esis_dict.setdefault('ish', {}).update({'rcvd': int(group['ish_rcvd'])})
                esis_dict.setdefault('ish', {}).update({'sent': int(group['ish_sent'])})
                esis_dict.setdefault('rd', {}).update({'sent': int(group['rd_sent'])})
                esis_dict.setdefault('rd', {}).update({'rcvd': int(group['rd_rcvd'])})
                esis_dict.setdefault('qcf', {}).update({'rcvd': int(group['qcf_rcvd'])})
                esis_dict.setdefault('qcf', {}).update({'sent': int(group['qcf_sent'])})
                continue

            # Tunneling (sent/rcvd): IP: 0/0, IPv6: 0/0
            m = p15.match(line)
            if m:
                group = m.groupdict()
                tunneling_dict = result_dict.setdefault('tunneling', {})
                tunneling_dict.setdefault('ip', {}).update({'rcvd': int(group['ip_rcvd'])})
                tunneling_dict.setdefault('ip', {}).update({'sent': int(group['ip_sent'])})
                tunneling_dict.setdefault('ipv6', {}).update({'rcvd': int(group['ipv6_rcvd'])})
                tunneling_dict.setdefault('ipv6', {}).update({'sent': int(group['ipv6_sent'])})
                continue

            # Tunneling dropped (rcvd) IP/IPV6:  0
            m = p16.match(line)
            if m:
                group = m.groupdict()
                tunneling_dict = result_dict.setdefault('tunneling', {})
                tunneling_dict.setdefault('ip', {}).update({'rcvd_dropped': int(group['tunneling_dropped'])})
                tunneling_dict.setdefault('ipv6', {}).update({'rcvd_dropped': int(group['tunneling_dropped'])})
                continue

            # ISO-IGRP: Querys (sent/rcvd): 0/0 Updates (sent/rcvd): 0/0
            m = p17.match(line)
            if m:
                group = m.groupdict()
                iso_dict = result_dict.setdefault('iso-igrp', {})
                iso_dict.setdefault('query', {}).update({'rcvd': int(group['query_rcvd'])})
                iso_dict.setdefault('query', {}).update({'sent': int(group['query_sent'])})
                iso_dict.setdefault('update', {}).update({'rcvd': int(group['update_rcvd'])})
                iso_dict.setdefault('update', {}).update({'sent': int(group['update_sent'])})
                continue

            # ISO-IGRP: Router Hellos: (sent/rcvd): 0/0
            m = p18.match(line)
            if m:
                group = m.groupdict()
                iso_dict = result_dict.setdefault('iso-igrp', {})
                iso_dict.setdefault('router_hello', {}).update({'rcvd': int(group['hello_rcvd'])})
                iso_dict.setdefault('router_hello', {}).update({'sent': int(group['hello_sent'])})
                continue

            # ISO-IGRP Syntax Errors: 0
            m = p19.match(line)
            if m:
                group = m.groupdict()
                iso_dict.update({'syntax_errors': int(group['syntax_errors']) })
                continue

            # Tag VRF1:
            m = p20.match(line)
            if m:
                group = m.groupdict()
                isis_dict = result_dict.setdefault('tag',{}).setdefault(group['tag'], {}).setdefault('IS-IS', {})
                continue

            #     IS-IS: Time since last clear: never
            m = p21.match(line)
            if m:
                group = m.groupdict()
                isis_dict.update({'last_clear': group['last_clear']})
                continue
            #     IS-IS: Level-1 Hellos (sent/rcvd): 497/533
            m = p22.match(line)
            if m:
                group = m.groupdict()
                hello_dict = isis_dict.setdefault('hello',{}).setdefault('level-1',{})
                hello_dict.update({key:int(value) for key,value in group.items()})
                continue

            #     IS-IS: Level-2 Hellos (sent/rcvd): 843/611
            m = p23.match(line)
            if m:
                group = m.groupdict()
                hello_dict = isis_dict.setdefault('hello', {}).setdefault('level-2', {})
                hello_dict.update({key: int(value) for key, value in group.items()})
                continue

            #     IS-IS: PTP Hellos     (sent/rcvd): 0/0
            m = p24.match(line)
            if m:
                group = m.groupdict()
                hello_dict = isis_dict.setdefault('hello', {}).setdefault('ptp', {})
                hello_dict.update({key: int(value) for key, value in group.items()})
                continue

            #     IS-IS: Level-1 LSPs sourced (new/refresh): 3/4
            m = p25.match(line)
            if m:
                group = m.groupdict()
                hello_dict = isis_dict.setdefault('lsp_sourced', {}).setdefault('level-1', {})
                hello_dict.update({key: int(value) for key, value in group.items()})
                continue

            #     IS-IS: Level-2 LSPs sourced (new/refresh): 4/5
            m = p26.match(line)
            if m:
                group = m.groupdict()
                hello_dict = isis_dict.setdefault('lsp_sourced', {}).setdefault('level-2', {})
                hello_dict.update({key: int(value) for key, value in group.items()})
                continue

            #     IS-IS: Level-1 LSPs flooded (sent/rcvd): 0/0
            m = p27.match(line)
            if m:
                group = m.groupdict()
                hello_dict = isis_dict.setdefault('lsp_flooded', {}).setdefault('level-1', {})
                hello_dict.update({key: int(value) for key, value in group.items()})
                continue

            #     IS-IS: Level-2 LSPs flooded (sent/rcvd): 5/5
            m = p28.match(line)
            if m:
                group = m.groupdict()
                hello_dict = isis_dict.setdefault('lsp_flooded', {}).setdefault('level-2', {})
                hello_dict.update({key: int(value) for key, value in group.items()})
                continue

            #     IS-IS: LSP Retransmissions: 0
            m = p29.match(line)
            if m:
                group = m.groupdict()
                isis_dict.update({'lsp_retransmissions': int(group['lsp_retransmissions'])})
                continue

            #     IS-IS: Level-1 CSNPs (sent/rcvd): 0/0
            m = p30.match(line)
            if m:
                group = m.groupdict()
                csnp_dict = isis_dict.setdefault('csnp', {}).setdefault('level-1', {})
                csnp_dict.update({key: int(value) for key, value in group.items()})
                continue

            #     IS-IS: Level-2 CSNPs (sent/rcvd): 170/0
            m = p31.match(line)
            if m:
                group = m.groupdict()
                csnp_dict = isis_dict.setdefault('csnp', {}).setdefault('level-2', {})
                csnp_dict.update({key: int(value) for key, value in group.items()})
                continue

            #     IS-IS: Level-1 PSNPs (sent/rcvd): 0/0
            m = p32.match(line)
            if m:
                group = m.groupdict()
                psnp_dict = isis_dict.setdefault('psnp', {}).setdefault('level-1', {})
                psnp_dict.update({key: int(value) for key, value in group.items()})
                continue

            #     IS-IS: Level-2 PSNPs (sent/rcvd): 0/0
            m = p33.match(line)
            if m:
                group = m.groupdict()
                psnp_dict = isis_dict.setdefault('psnp', {}).setdefault('level-2', {})
                psnp_dict.update({key: int(value) for key, value in group.items()})
                continue

            #     IS-IS: Level-1 DR Elections: 1
            m = p34.match(line)
            if m:
                group = m.groupdict()
                isis_dict.setdefault('dr_election', {}).update({'level-1': int(group['dr_elections'])})
                continue

            #     IS-IS: Level-2 DR Elections: 2
            m = p35.match(line)
            if m:
                group = m.groupdict()
                isis_dict.setdefault('dr_election', {}).update({'level-2': int(group['dr_elections'])})
                continue

            #     IS-IS: Level-1 SPF Calculations: 14
            m = p36.match(line)
            if m:
                group = m.groupdict()
                isis_dict.setdefault('spf_calculation', {}).update({'level-1': int(group['spf_calculation'])})
                continue

            #     IS-IS: Level-2 SPF Calculations: 17
            m = p37.match(line)
            if m:
                group = m.groupdict()
                isis_dict.setdefault('spf_calculation', {}).update({'level-2': int(group['spf_calculation'])})
                continue

            #     IS-IS: Level-1 Partial Route Calculations: 0
            m = p38.match(line)
            if m:
                group = m.groupdict()
                isis_dict.setdefault('partial_route_calculation', {}).update({'level-1': int(group['partial_route_calculations'])})
                continue

            #     IS-IS: Level-2 Partial Route Calculations: 1
            m = p39.match(line)
            if m:
                group = m.groupdict()
                isis_dict.setdefault('partial_route_calculation', {}).update({'level-2': int(group['partial_route_calculations'])})
                continue

            #     IS-IS: LSP checksum errors received: 0
            m = p40.match(line)
            if m:
                group = m.groupdict()
                isis_dict.update({'lsp_checksum_errors_received': int(group['lsp_checksum_errors_received'])})
                continue

            #     IS-IS: Update process queue depth: 0/200
            m = p41.match(line)
            if m:
                group = m.groupdict()
                isis_dict.update({'update_process_queue_depth': group['update_process_queue_depth']})
                continue

            #     IS-IS: Update process packets dropped: 0
            m = p42.match(line)
            if m:
                group = m.groupdict()
                isis_dict.update({'update_process_packets_dropped': int(group['update_process_packets_dropped'])})
                continue

        return result_dict
