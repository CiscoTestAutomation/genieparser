'''show_platform.py

IOSXE c9350 parsers for the following show commands:
   * show platform hardware fed {mode} qos scheduler sdk interface {interface}
   * show platform hardware fed {switch} {mode} qos scheduler sdk interface {interface}
'''

# Python
import re
import logging

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, And, Default, Use

# import parser utils
from genie.libs.parser.utils.common import Common


class ShowPlatformHardwareFedQosSchedulerSdkInterfaceSchema(MetaParser):
    """Schema for show platform hardware fed {switch} {mode} qos scheduler sdk interface {interface}"""

    schema = {
        'interface': {
            Any(): {
                'interface_id': str,
                'priority_propagation': str,
                'sub_interface_q_mode': str,
                'logical_port': str,
                'tc_profile': {
                    'sdk_oid': int,
                    'tc': {
                        Any(): {
                            'voq_offset': int
                        }
                    }
                },
                'interface_scheduler': {
                    'oid': {
                        Any(): {
                            'ct_r': {
                                Any(): {
                                    'cir': int,
                                    'eir_pir': int,
                                    'is_eir': str,
                                    'wfq_weights': str,
                                    'hw_id': int
                                }
                            }
                        }
                    }
                },
                'system_port_scheduler': {
                    'oid': {
                        Any(): {
                            'c_pb': {
                                Any(): {
                                    'cir': int,
                                    'burst': int,
                                    'tx_cir': int,
                                    'tx_burst': int,
                                    'eir_wfq': int,
                                    'act_wfq': int,
                                    'pg_type': str,
                                    'child_oid': {
                                        Any(): {
                                            'child_type': str
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                'oqhse_scheduler': {
                    'oid': {
                        Any(): {
                            'mode': str,
                            'cep_ir': {
                                Any(): {
                                    'rate': str,
                                    'burst': str,
                                    'weight': int,
                                    'hw_id': int,
                                    'type': str,
                                    Optional('link_point'): str,
                                    'hse_type': str,
                                    'hse_oid': int
                                }
                            },
                            'child_group': {
                                Any(): {
                                    'child': {
                                        Any(): {
                                            'hse_oid': int,
                                            Optional('link'): {
                                                Any(): {
                                                    'link_point': int
                                                }
                                            },
                                            'hse_type': str
                                        }
                                    },
                                    'branch': str,
                                    'weights': list,
                                    'load_balance_type': {
                                        Any(): {
                                            's': int,
                                            'c': int
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                'cstse_scheduler': {
                    'oid': {
                        Any(): {
                            'mode': str,
                            'cep_ir': {
                                Any(): {
                                    'rate': str,
                                    'burst': str,
                                    'weight': int,
                                    'hw_id': int,
                                    'type': str,
                                    Optional('link_point'): str,
                                    'hse_type': str,
                                    'hse_oid': int
                                }
                            },
                            'child_group': {
                                Any(): {
                                    'child': {
                                        Any(): {
                                            'hse_oid': int,
                                            Optional('link'): {
                                                Any(): {
                                                    'link_point': int
                                                }
                                            },
                                            'hse_type': str
                                        }
                                    },
                                    'branch': str,
                                    Optional('weights'): list,
                                    'load_balance_type': {
                                        Any(): {
                                            's': int,
                                            'c': int
                                        }
                                    }
                                }
                            }
                        }
                    }
                },
                'svcse_scheduler': {
                    'oid': {
                        Any(): {
                            'cep_ir': {
                                Any(): {
                                    'rate': int,
                                    'burst': str,
                                    'weight': int,
                                    'hw_id': int,
                                    'type': str,
                                    'link_point': int,
                                    'hse_type': str,
                                    'hse_oid': int
                                }
                            },
                            'child': {
                                'hse_oid': {
                                    Any(): {
                                        'voq_id': int,
                                        'in_device': int,
                                        'in_slice': int,
                                        'hse_type': str
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }


class ShowPlatformHardwareFedQosSchedulerSdkInterface(ShowPlatformHardwareFedQosSchedulerSdkInterfaceSchema):
    """Parser for show platform hardware fed {switch} {mode} qos scheduler sdk interface {interface}"""

    cli_command = ['show platform hardware fed {mode} qos scheduler sdk interface {interface}',
        'show platform hardware fed {switch} {mode} qos scheduler sdk interface {interface}']

    def cli(self, mode, interface, switch=None, output=None):
        if output is None:
            if switch:
                cmd = self.cli_command[1].format(switch=switch, mode=mode, interface=interface)
            else:
                cmd = self.cli_command[0].format(mode=mode, interface=interface)

            output = self.device.execute(cmd)

        # Interface              : HundredGigE1/0/5 (0x54A)
        p1_0 = re.compile(r'^Interface\s+: (?P<interface>\S+) \((?P<interface_id>\S+)\)$')

        # Priority Propagation  : Disabled
        p1_1 = re.compile(r'^Priority Propagation\s+:\s*(?P<priority_propagation>\w+)$')

        # Sub-interface Q Mode  : Disabled - No Priority Propagation
        p1_2 = re.compile(r'^Sub-interface Q Mode  : (?P<sub_interface_q_mode>.+)$')

        # Logical Port          : Enabled
        p1_3 = re.compile(r'^Logical Port\s+: (?P<logical_port>\w+)$')

        # TC Profile            : SDK OID    :   209
        p1_4 = re.compile(r'^TC Profile\s+: SDK OID\s+:\s+(?P<sdk_oid>\d+)$')

        # : TC         : TC0 | TC1 | TC2 | TC3 | TC4 | TC5 | TC6 | TC7
        p1_5 = re.compile(r'^: TC         : (?P<tc>[\w\s\|]+)$')

        # : VOQ Offset :   0 |   1 |   2 |   3 |   4 |   5 |   6 |   7
        p1_6 = re.compile(r'^: VOQ Offset :\s+(?P<voq_offset>[\d\s\|]+)$')

        # Interface Scheduler Configuration
        p2_0 = re.compile(r'^Interface Scheduler Configuration$')

        # | 755    | C-R   | 11000000512   | 11000000512   | PIR    | C(1   ) E(1   ) | 755    |
        p2_1 = re.compile(r'^(?P<oid>\d+)\s+\|\s+(?P<ct_r>[\w\-]+)\s+\|\s+(?P<cir>\d+)\s+\|\s+(?P<eir_pir>\d+)\s+\|\s+(?P<is_eir>\w+)\s+\|\s+(?P<wfq_weights>.+)\s+\|\s+(?P<hw_id>\d+)$')

        # System Port - Scheduler Configuration 
        p3_0 = re.compile(r'^System Port - Scheduler Configuration$')

        # | 759    | P-CIR | 11000000512   | 12    | 11000000512   | 12       | 1       | 7       | OQPG-7  |      |      |
        p3_1 = re.compile(r'^(?P<oid>\d+)\s+\|\s+(?P<c_pb>[\w\-]+)\s+\|\s+(?P<cir>\d+)\s+\|\s+(?P<burst>\d+)\s+\|\s+(?P<tx_cir>\d+)\s+\|\s+(?P<tx_burst>\d+)\s+\|\s+(?P<eir_wfq>\d+)\s+\|\s+(?P<act_wfq>\d+)\s+\|\s+(?P<pg_type>[\w\-]+)(\s+\|\s+(?P<child_type>\w+)\s+\|\s+(?P<child_oid>\d+))?$')

        # |        |       |     |       |     |          |         |         |         | OQHSE      | 760       |
        p3_2 = re.compile(r'^(?P<child_type>\w+)\s+\|\s+(?P<child_oid>\d+)$')

        # OQHSE - Scheduler Configuration
        p4_0 = re.compile(r'^OQHSE - Scheduler Configuration$')

        # | 760    | 2-I  | CIR   | UNLIMITED  | DEFLT | 7    | 7      | PARENT   |     | OQPG-7     | Sys-P SCH | 0   |
        p4_1 = re.compile(r'^((?P<oid>\d+)\s+\|\s+(?P<mode>[\w\-]+)\s+\|\s+)?(?P<cep_ir>\w+)\s+\|\s+(?P<rate>\w+)\s+\|\s+(?P<burst>\w+)\s+\|\s+(?P<weight>\d+)\s+\|\s+(?P<hw_id>\d+)\s+\|\s+(?P<type>\w+)\s+\|\s+((?P<branch>\w+)\s+\|\s+(?P<lr_sp>\w+)\s+\|\s+(?P<wfq>\d+)\s+)?\|\s+(?P<link_point>[\w\-]+)\s+\|\s+(?P<hse_type>[\w\-\s]+)\|\s+(?P<hse_oid>\d+)$')

        # |    |      |   |     |       |        |     |    | Left   [SP( 0: 2) WFQ( 2: 2)]   |      |     |      |
        p4_2 = re.compile(r'^(?P<branch>Left|Right)\s+\[(?P<load_balance_type1>\w+)\s*\(\s*(?P<s1>\d+):\s*(?P<c1>\d+)\)\s+(?P<load_balance_type2>\w+)\s*\(\s*(?P<s2>\d+):\s*(?P<c2>\d+)\)\]$')

        # |  |      |   |    |       |        |        |     :   0   0 255 255   0   0   0   0
        p4_3 = re.compile(r'^:\s+(?P<weights>[\s\d]+)$')

        # |   |      |   |   |       |        |        |   |    SP-Link | 0          |   |   |
        p4_4 = re.compile(r'^(?P<link>\S+)\s+\|\s*(?P<link_point>\d+)$')

        # |  |      |     |   |       |        |  | CHILD        |         |  | CSTSE     | 763     |
        p4_5 = re.compile(r'^CHILD\s*\|\s+\|\s+\|\s*(?P<hse_type>\w+)\s*\|\s*(?P<hse_oid>\d+)$')

        # CSTSE - Scheduler Configuration
        p5_0 = re.compile(r'^CSTSE - Scheduler Configuration$')

        # SVCSE - Scheduler Configuration 
        p6_0 = re.compile(r'^SVCSE - Scheduler Configuration$')

        # | 772    | CIR      | 2000000000    | DEFLT | 0      | 55     | PARENT       | 0          | CSTSE     | 763     |        |
        p6_1 = re.compile(r'^(?P<oid>\d+)?\s*\|\s*(?P<cep_ir>\w+)\s*\|\s*(?P<rate>\d+)\s*\|\s*(?P<burst>\w+)\s*\|\s*(?P<weight>\d+)\s*\|\s*(?P<hw_id>\d+)\s*\|\s*(?P<type>\w+)\s*\|\s*(?P<link_point>\d+)\s*\|\s*(?P<hse_type>\w+)\s*\|\s*(?P<hse_oid>\d+)(\s*\|\s+(?P<voq_id>\d+)\s*\|\s*(?P<in_device>\d+)\|\s*(?P<in_slice>\d+))?$')

        # |    |   |   |       |    |    | CHILD   |    | VSC       | 327     | 327    | 0    | 0   |
        p6_2 = re.compile(r'^CHILD\s*\|\s+\|\s*(?P<hse_type>\w+)\s*\|\s*(?P<hse_oid>\d+)\s*\|\s*(?P<voq_id>\d+)\s*\|\s*(?P<in_device>\d+)\s+\|\s*(?P<in_slice>\d+)$')

        ret_dict = {}
        child_group = 0
        child = 0
        for line in output.splitlines():
            line = line.strip(' |')

            # Interface              : HundredGigE1/0/5 (0x54A)
            m = p1_0.match(line)
            if m:
                int_dict = ret_dict.setdefault('interface', {}).setdefault(Common.convert_intf_name(m.groupdict()['interface']), {})
                int_dict['interface_id'] = m.groupdict()['interface_id']
                continue

            # Priority Propagation  : Disabled
            m = p1_1.match(line)
            if m:
                int_dict['priority_propagation'] = m.groupdict()['priority_propagation']
                continue

            # Sub-interface Q Mode  : Disabled - No Priority Propagation
            m = p1_2.match(line)
            if m:
                int_dict['sub_interface_q_mode'] = m.groupdict()['sub_interface_q_mode']
                continue

            # Logical Port          : Enabled
            p1_3 = re.compile(r'^Logical Port\s+: (?P<logical_port>\w+)$')
            m = p1_3.match(line)
            if m:
                int_dict['logical_port'] = m.groupdict()['logical_port']
                continue

            # TC Profile            : SDK OID    :   209
            m = p1_4.match(line)
            if m:
                tc_profile_dict = int_dict.setdefault('tc_profile', {})
                tc_profile_dict['sdk_oid'] = int(m.groupdict()['sdk_oid'])
                continue

            # : TC         : TC0 | TC1 | TC2 | TC3 | TC4 | TC5 | TC6 | TC7
            m = p1_5.match(line)
            if m:
                tc_list = m.groupdict()['tc'].lower().split(' | ')
                tc_dict = tc_profile_dict.setdefault('tc', {})
                continue

            # : VOQ Offset :   0 |   1 |   2 |   3 |   4 |   5 |   6 |   7
            m = p1_6.match(line)
            if m:
                voq_offset_list = m.groupdict()['voq_offset'].lower().split(' | ')
                [tc_dict.setdefault(tc_id, {}).setdefault('voq_offset', int(voq_offset)) for tc_id, voq_offset in zip(tc_list, voq_offset_list)]
                continue

            # Interface Scheduler Configuration
            m = p2_0.match(line)
            if m:
                scheduler_dict = int_dict.setdefault('interface_scheduler', {})
                continue

            # | 755    | C-R   | 11000000512   | 11000000512   | PIR    | C(1   ) E(1   ) | 755    |
            m = p2_1.match(line)
            if m:
                group_dict = m.groupdict()
                interface_sch_dict = scheduler_dict.setdefault('oid', {}).setdefault(group_dict['oid'], {})
                ct_r_dict = interface_sch_dict.setdefault('ct_r', {}).setdefault(group_dict['ct_r'], {})
                ct_r_dict['cir'] = int(group_dict['cir'])
                ct_r_dict['eir_pir'] = int(group_dict['eir_pir'])
                ct_r_dict['is_eir'] = group_dict['is_eir']
                ct_r_dict['wfq_weights'] = group_dict['wfq_weights']
                ct_r_dict['hw_id'] = int(group_dict['hw_id'])
                continue

            # System Port - Scheduler Configuration
            m = p3_0.match(line)
            if m:
                system_port_sch_dict = int_dict.setdefault('system_port_scheduler', {})
                continue

            # | 759    | P-CIR | 11000000512   | 12    | 11000000512   | 12       | 1       | 7       | OQPG-7  |      |      |
            m = p3_1.match(line)
            if m:
                group_dict = m.groupdict()
                sys_port_sch_dict = system_port_sch_dict.setdefault('oid', {}).setdefault(group_dict['oid'], {})
                c_pb_dict = sys_port_sch_dict.setdefault('c_pb', {}).setdefault(group_dict['c_pb'], {})
                c_pb_dict['cir'] = int(group_dict['cir'])
                c_pb_dict['burst'] = int(group_dict['burst'])
                c_pb_dict['tx_cir'] = int(group_dict['tx_cir'])
                c_pb_dict['tx_burst'] = int(group_dict['tx_burst'])
                c_pb_dict['eir_wfq'] = int(group_dict['eir_wfq'])
                c_pb_dict['act_wfq'] = int(group_dict['act_wfq'])
                c_pb_dict['pg_type'] = group_dict['pg_type']
                continue

            # |        |       |     |       |     |          |         |         |         | OQHSE      | 760       |
            m = p3_2.match(line)
            if m:
                child_dict = c_pb_dict.setdefault('child_oid', {}).setdefault(m.groupdict()['child_oid'], {})
                child_dict['child_type'] = m.groupdict()['child_type']
                continue

            # OQHSE - Scheduler Configuration
            m = p4_0.match(line)
            if m:
                oqhse_scheduler_dict = int_dict.setdefault('oqhse_scheduler', {})
                continue

            # | 760    | 2-I  | CIR   | UNLIMITED  | DEFLT | 7    | 7      | PARENT   |     | OQPG-7     | Sys-P SCH | 0   |
            m = p4_1.match(line)
            if m:
                child_group = 0
                group_dict = m.groupdict()
                if group_dict['oid']:
                    oqhse_sch_dict = oqhse_scheduler_dict.setdefault('oid', {}).setdefault(group_dict['oid'], {})
                if group_dict['mode']:
                    oqhse_sch_dict['mode'] = group_dict['mode']
                cep_ir_dict = oqhse_sch_dict.setdefault('cep_ir', {}).setdefault(group_dict['cep_ir'], {})
                cep_ir_dict['rate'] = group_dict['rate']
                cep_ir_dict['burst'] = group_dict['burst']
                cep_ir_dict['type'] = group_dict['type']
                cep_ir_dict['weight'] = int(group_dict['weight'])
                cep_ir_dict['hw_id'] = int(group_dict['hw_id'])
                cep_ir_dict['hse_type'] = group_dict['hse_type'].strip()
                cep_ir_dict['hse_oid'] = int(group_dict['hse_oid'])
                if group_dict['link_point']:
                    cep_ir_dict['link_point'] = group_dict['link_point']
                continue

            # |    |      |   |     |  |   |     |    | Left   [SP( 0: 2) WFQ( 2: 2)]   |      |     |      |
            m = p4_2.match(line)
            if m:
                group_dict = m.groupdict()
                child_group_dict = oqhse_sch_dict.setdefault('child_group', {}).setdefault(child_group, {})
                child_group += 1
                child = 0
                child_group_dict['branch'] = group_dict['branch']
                load_balance_dict = child_group_dict.setdefault('load_balance_type', {})
                load_balance_dict.setdefault(group_dict['load_balance_type1'], {'s': int(group_dict['s1']), 'c': int(group_dict['c1'])})
                load_balance_dict.setdefault(group_dict['load_balance_type2'], {'s': int(group_dict['s2']), 'c': int(group_dict['c2'])})
                continue

            # |  |      |   |    |       |        |        |     :   0   0 255 255   0   0   0   0
            m = p4_3.match(line)
            if m:
                child_group_dict['weights'] = list(map(int, m.groupdict()['weights'].split()))
                continue

            # |   |      |   |   |       |        |        |   |    SP-Link | 0          |   |   |
            m = p4_4.match(line)
            if m:
                child_dict = child_group_dict.setdefault('child', {})
                each_child_dict = child_dict.setdefault(child, {})
                each_child_dict.setdefault('link', {}).setdefault(m.groupdict()['link'], {'link_point': int(m.groupdict()['link_point'])})
                continue

            # |  |      |     |   |       |        |  | CHILD        |         |  | CSTSE     | 763     |
            m = p4_5.match(line)
            if m:
                child += 1
                each_child_dict['hse_type'] = m.groupdict()['hse_type'].strip()
                each_child_dict['hse_oid'] = int(m.groupdict()['hse_oid'])
                continue

            # CSTSE - Scheduler Configuration
            m = p5_0.match(line)
            if m:
                oqhse_scheduler_dict = int_dict.setdefault('cstse_scheduler', {})
                child_group = 0
                continue

            # SVCSE - Scheduler Configuration
            m = p6_0.match(line)
            if m:
                svcse_scheduler_dict = int_dict.setdefault('svcse_scheduler', {})
                continue

            # # | 772    | CIR      | 2000000000    | DEFLT | 0      | 55     | PARENT       | 0          | CSTSE     | 763     |        |
            m = p6_1.match(line)
            if m:
                group_dict = m.groupdict()
                oqhse_sch_dict = svcse_scheduler_dict.setdefault('oid', {}).setdefault(group_dict['oid'], {})
                cep_ir_dict = oqhse_sch_dict.setdefault('cep_ir', {}).setdefault(group_dict['cep_ir'], {})
                cep_ir_dict['rate'] = int(group_dict['rate'])
                cep_ir_dict['burst'] = group_dict['burst']
                cep_ir_dict['type'] = group_dict['type']
                cep_ir_dict['weight'] = int(group_dict['weight'])
                cep_ir_dict['hw_id'] = int(group_dict['hw_id'])
                cep_ir_dict['hse_type'] = group_dict['hse_type'].strip()
                cep_ir_dict['hse_oid'] = int(group_dict['hse_oid'])
                if group_dict['link_point']:
                    cep_ir_dict['link_point'] = int(group_dict['link_point'])
                continue

            # |    |   |   |       |    |    | CHILD   |    | VSC       | 327     | 327    | 0    | 0   |
            m = p6_2.match(line)
            if m:
                group_dict = m.groupdict()
                hse_oid_dict = oqhse_sch_dict.setdefault('child', {}).setdefault('hse_oid', {}).setdefault(group_dict['hse_oid'], {})
                hse_oid_dict['voq_id'] = int(group_dict['voq_id'])
                hse_oid_dict['in_device'] = int(group_dict['in_device'])
                hse_oid_dict['in_slice'] = int(group_dict['in_slice'])
                hse_oid_dict['hse_type'] = group_dict['hse_type'].strip()
                continue

        return ret_dict
