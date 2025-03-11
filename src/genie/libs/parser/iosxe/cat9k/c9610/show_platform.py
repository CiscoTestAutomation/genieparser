'''show_platform.py

IOSXE c9610 parsers for the following show commands:
    * show platform hardware fed active fwd-asic resource tcam utilization
    * show platform software fed {switch} {mode} acl info db detail
    * show platform software fed {mode} acl info db detail
    * show platform hardware fed {switch} {switch_var} qos queue stats interface {interface}
    * show platform hardware fed switch {switch_num} qos queue stats interface {interface} clear
    * show platform hardware fed {mode} qos scheduler sdk interface {interface}
    * show platform hardware fed {switch} {mode} qos scheduler sdk interface {interface}
    * show platform hardware fed active qos queue config interface {interface}
    * show platform hardware fed switch {switch_var} qos queue config interface {interface}
    * show platform hardware authentication status
'''
from genie.metaparser import MetaParser
from genie.libs.parser.utils.common import Common
import re
from genie.metaparser.util.schemaengine import Schema, Any, Or, Optional, Use, And
from genie.libs.parser.iosxe.cat9k.c9600.show_platform import ShowPlatformFedActiveTcamUtilization as ShowPlatformFedActiveTcamUtilization_c9600


class ShowPlatformFedActiveTcamUtilization(ShowPlatformFedActiveTcamUtilization_c9600):
    """ Parser for show platform hardware fed active fwd-asic resource tcam utilization"""
    pass


class ShowPlatformSoftwareFedActiveAclInfoDbDetailSchema(MetaParser):
    """Schema for show platform software fed switch active acl info db detail"""

    schema = {
        'cg_name': {
            Any(): {
                'cg_id':int,
                'feature':str,
                'prot':str,
                'region':str,
                'dir':str,
                'sdk_handles': list,
                'seq':{
                    Any():{
                        Optional('ipv4_src_value'):str,
                        Optional('ipv4_src_mask'):str,
                        Optional('ipv4_dst_value'):str,
                        Optional('ipv4_dst_mask'):str,
                        Optional('ipv6_src_value'):str,
                        Optional('ipv6_src_mask'):str,
                        Optional('ipv6_dst_value'):str,
                        Optional('ipv6_dst_mask'):str,
                        'proto':{
                                'value':str,
                                'mask':str,
                                'tcp_flg':str,
                                'tcp_op':str,
                                'src_port':str,
                                'dst_port':str,
                        },
                        'tos':{
                                'value':str,
                                'mask':str,
                                'ttl':str,
                                'cos':str,
                                'v4_opt':str,
                                'src_obj':str,
                                'dst_obj':str,
                        },
                        'action':str,
                        'logging':str,
                        Optional('counter_handles'): list,
                    },
                },
            },
        },
    }

# ============================================================================
#  Parser for
#  * 'show platform software fed switch active acl info db detail'
# ============================================================================
class ShowPlatformSoftwareFedActiveAclInfoDbDetail(ShowPlatformSoftwareFedActiveAclInfoDbDetailSchema):
    '''Parser for:
        * 'show platform software fed switch active acl info db detail'
    '''
    cli_command = ['show platform software fed {switch} {mode} acl info db detail',
                   'show platform software fed {mode} acl info db detail']

    def cli(self, mode, switch=None, output=None):
        if not output:
            if switch:
                cmd = self.cli_command[0].format(switch=switch, mode=mode)
            else:
                cmd = self.cli_command[1].format(mode=mode)
            output = self.device.execute(cmd)

        proto_flag = False
        tos_flag = False

        # [CG ID: 8]    CG Name: racl_ingress
        # [Racl, CG ID: 8]    CG Name: racl_permitv6_egress
        p1 = re.compile(r'^\[.*CG ID:\s+(?P<cg_id>\d+)\]\s+CG\s+Name:\s+(?P<cg_name>[\w\-]+)$')

        # [Feature: Racl    Prot: IPv4
        p2 = re.compile(r'^Feature:\s+(?P<feature>\w+)\s+Prot:\s+(?P<prot>\w+)$')

        # Region grp: 0x2c0603d8    Dir: Ingress
        p3 = re.compile(r'^Region\s+grp:\s+(?P<region>0x[\da-fA-F]+)\s+Dir:\s+(?P<dir>\w+)$')

        # SDK-handle(asic: 0, OID: 0x44D)
        p4 = re.compile(r'^SDK-handle\(asic:\s+(?P<asic>\d+),\s+OID:\s+(?P<oid>0x\w+)\)$')

        # Seq Num:10
        p5 = re.compile(r'^Seq Num:+(?P<seq>[\d\w]+)$')

        # ipv4_src: value = 0x00000000       mask = 0x00000000
        p6 = re.compile(r'^ipv4_src:\s+value+\s=\s+(?P<ipv4_src_value>[\d\w]+)+\s+mask+\s=\s+(?P<ipv4_src_mask>[\d\w]+)$')

        # ipv4_dst: value = 0x00000000       mask = 0x00000000
        p7 = re.compile(r'^ipv4_dst:\s+value+\s=\s+(?P<ipv4_dst_value>[\d\w]+)+\s+mask+\s=\s+(?P<ipv4_dst_mask>[\d\w]+)$')

        # ipv6_src: value = 0x00001100.0x01000000.0x00000000.0x30000000
        p7_1 = re.compile(r'^ipv6_src:\s+value+\s=\s+(?P<ipv6_src_value>[\S]+)$')

        # ipv6_dst: value = 0x00001100.0x00000000.0x00000000.0x3000000
        p7_2 = re.compile(r'^ipv6_dst:\s+value+\s=\s+(?P<ipv6_dst_value>[\S]+)$')

        # mask = 0xffffffff.0xffffffff.0xffffffff.0xffffffff
        p7_3 = re.compile(r'^mask+\s=\s+(?P<ipv6_mask>[\S]+)$')

        # proto    frag    tcp_flg    tcp_op    src_port    dst_port
        p8_0=re.compile(r'^proto+\s+frag+\s+tcp_flg+\s+tcp_op+\s+src_port+\s+dst_port$')

        #  tos      ttl       cos      v4_opt    src_obj     dst_obj
        p8_1 = re.compile(r'^tos+\s+ttl+\s+cos+\s+[v4_opt|ext_hdr]+\s+src_obj+\s+dst_obj$')

        # V:  0x1       0x0      0x0         0x0        0x0          0x0
        # M:  0xff       0x0      0x0         0x0        0x0          0x0
        p8 = re.compile(r'^(?P<type>[\w\_]+)+:\s+(?P<proto>[\w]+)+\s+(?P<frag>[\w]+)+\s+(?P<tcp_flg>[\w]+)+\s+(?P<tcp_op>[\w]+)+\s+(?P<src_port>[\w]+)+\s+(?P<dst_port>[\w]+)$')
        # V:  0x0       0x0      0x0         0x0        0x0          0x0
        # M:  0x0       0x0      0x0         0x0        0x0          0x0
        p9 = re.compile(r'^(?P<type>[\w\_]+)+:\s+(?P<tos>[\w]+)+\s+(?P<ttl>[\w]+)+\s+(?P<cos>[\w]+)+\s+(?P<v4_opt>[\w]+)+\s+(?P<src_obj>[\w]+)+\s+(?P<dst_obj>[\w]+)$')

        # Result  action: DENY    Logging: NO_LOG
        p10 = re.compile(r'Result\s+action:\s+(?P<action>\S+)\s+Logging:\s+(?P<logging>\S+)$')

        # Counter handle: (asic: 0 , OID: 0x577 (0))
        p11 = re.compile(r'^Counter\s+handle:\s+\(asic:\s+(?P<asic>\d+)\s*,\s*OID:\s+(?P<oid>0x[\da-fA-F]+)\s*\(\d+\)\)$')

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # [CG ID: 8]    CG Name: racl_ingress
            m = p1.match(line)
            if m:
                group = m.groupdict()
                cg_name_dict = ret_dict.setdefault('cg_name', {}).setdefault(group['cg_name'], {})
                cg_name_dict['cg_id'] = int(group['cg_id'])
                continue

            # Feature: Racl    Prot: IPv4
            m = p2.match(line)
            if m:
                group = m.groupdict()
                cg_name_dict['feature'] = group['feature']
                cg_name_dict['prot'] = group['prot']
                continue

            # Region grp: 0x2c0603d8    Dir: Ingress
            m = p3.match(line)
            if m:
                group = m.groupdict()
                cg_name_dict['region'] = group['region']
                cg_name_dict['dir'] = group['dir']
                continue

            # SDK-handle(asic: 0, OID: 0x44D)
            m = p4.match(line)
            if m:
                group = m.groupdict()
                sdk_handles = cg_name_dict.setdefault('sdk_handles', [])
                sdk_handles.append({'asic': int(group['asic']), 'oid': group['oid']})
                continue

            # Seq Num:10
            m = p5.match(line)
            if m:
                group = m.groupdict()
                seq_dict = cg_name_dict.setdefault('seq', {}).setdefault(group['seq'], {})
                continue

            # ipv4_src: value = 0x78010500       mask = 0xffffff00
            m = p6.match(line)
            if m:
                group = m.groupdict()
                if 'seq_dict' in locals():
                    seq_dict['ipv4_src_value'] = group['ipv4_src_value']
                    seq_dict['ipv4_src_mask'] = group['ipv4_src_mask']
                continue

            # ipv4_dst: value = 0x7a010502       mask = 0xffffffff
            m = p7.match(line)
            if m:
                group = m.groupdict()
                if 'seq_dict' in locals():
                    seq_dict['ipv4_dst_value'] = group['ipv4_dst_value']
                    seq_dict['ipv4_dst_mask'] = group['ipv4_dst_mask']
                continue

            # ipv6_src: value = 0x00001100.0x01000000.0x00000000.0x30000000
            m = p7_1.match(line)
            if m:
                group = m.groupdict()
                if 'seq_dict' in locals():
                    seq_dict['ipv6_src_value'] = group['ipv6_src_value']
                continue

            # ipv6_dst: value = 0x00001100.0x00000000.0x00000000.0x3000000
            m = p7_2.match(line)
            if m:
                group = m.groupdict()
                if 'seq_dict' in locals():
                    seq_dict['ipv6_dst_value'] = group['ipv6_dst_value']
                continue

            # mask = 0xffffffff.0xffffffff.0xffffffff.0xffffffff
            m = p7_3.match(line)
            if m:
                group = m.groupdict()
                if 'seq_dict' in locals():
                    if 'ipv6_src_value' in seq_dict:
                        seq_dict['ipv6_src_mask'] = group['ipv6_mask']
                    elif 'ipv6_dst_value' in seq_dict:
                        seq_dict['ipv6_dst_mask'] = group['ipv6_mask']
                continue

            # proto    frag    tcp_flg    tcp_op    src_port    dst_port
            m = p8_0.match(line)
            if m:
                proto_flag = True
                continue

            # tos      ttl       cos      v4_opt    src_obj     dst_obj
            m = p8_1.match(line)
            if m:
                tos_flag = True
                proto_flag = False
                continue

            # V:  0x1       0x0      0x0         0x0        0x0          0x0
            m = p8.match(line)
            if m and proto_flag:
                group = m.groupdict()
                seq_dict['proto'] = {
                    'value': group['proto'],
                    'mask': group['frag'],
                    'tcp_flg': group['tcp_flg'],
                    'tcp_op': group['tcp_op'],
                    'src_port': group['src_port'],
                    'dst_port': group['dst_port'],
                }
                continue

            # M:  0x0       0x0      0x0         0x0        0x0          0x0
            m = p9.match(line)
            if m and tos_flag:
                group = m.groupdict()
                seq_dict['tos'] = {
                    'value': group['tos'],
                    'mask': group['ttl'],
                    'ttl': group['ttl'],
                    'cos': group['cos'],
                    'v4_opt': group['v4_opt'],
                    'src_obj': group['src_obj'],
                    'dst_obj': group['dst_obj'],
                }
                continue

            # Result action: DENY    Logging: NO_LOG
            m = p10.match(line)
            if m:
                group = m.groupdict()
                seq_dict['action'] = group['action']
                seq_dict['logging'] = group['logging']
                continue

            # Counter handle: (asic: 0 , OID: 0x577 (0))
            m = p11.match(line)
            if m:
                group = m.groupdict()
                counter_handles = seq_dict.setdefault('counter_handles', [])
                counter_handles.append({'asic': int(group['asic']), 'oid': group['oid']})
                continue

        return ret_dict



class ShowPlatformHardwareFedSwitchQosQueueStatsInterfaceSchema(MetaParser):
    """Schema for show platform hardware fed {switch} {switch_var} qos queue stats interface {interface}"""

    schema = {
        'interface': {
            Any(): {
                'asic': {
                    Any(): {
                        'voq_id': {
                            Any(): {
                                'packets': {
                                    'enqueued': int,
                                    'dropped': int,
                                    'total': int
                                },
                                'bytes': {
                                    'enqueued': int,
                                    'dropped': int,
                                    'total': int
                                },
                                'slice': {
                                    Any(): {
                                        'sms_bytes': int,
                                        'hbm_blocks': int,
                                        'hbm_bytes': int
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }


class ShowPlatformHardwareFedSwitchQosQueueStatsInterface(ShowPlatformHardwareFedSwitchQosQueueStatsInterfaceSchema):
    """Parser for show platform hardware fed {switch} {switch_var} qos queue stats interface {interface}"""

    cli_command = ['show platform hardware fed active qos queue stats interface {interface}',
        'show platform hardware fed switch {switch_num} qos queue stats interface {interface}']

    def cli(self, interface, switch_num=None, output=None):
        if output is None:
            if switch_num:
                cmd = self.cli_command[1].format(switch_num=switch_num, interface=interface)
            else:
                cmd = self.cli_command[0].format(interface=interface)

            output = self.device.execute(cmd)

        # VOQ Stats For : HundredGigE1/0/5 [ 0x544 ]
        # VOQ Stats For : HundredGigE2/0/2.1 [ 0x550 ]
        p0 = re.compile(r'^VOQ Stats For : (?P<interface>[\w\/\.]+)\s+.*$')

        #          | Asic     |                                 0
        # |----------|-----------------------------------------------------------------------|
        p1 = re.compile(r'^\|\s+Asic\s+\|\s+(?P<asic>\d+)$')

        # 0      | Enqueued |                        1194566957 |                       78841419162 |
        # | Dropped  |                                 0 |                                 0 |
        # | Total    |                        1194566957 |                       78841419162 |
        # |----------|-----------------------------------------------------------------------|
        p2 = re.compile(r'^(?P<voq_id>\d+)?\s*\|\s+(?P<header>\w+)\s+\|\s+(?P<packets>\d+)\s+\|\s+(?P<bytes>\d+)\s+\|$')

        # |   Slice  |         0 |         1 |         2 |         3 |         4 |         5 |
        p3 = re.compile(r'^\|\s+Slice\s+\|\s+(?P<slice0>\d+)\s\|\s+(?P<slice1>\d+)\s\|\s+(?P<slice2>\d+)\s\|'
                    r'\s+(?P<slice3>\d+)\s\|\s+(?P<slice4>\d+)\s\|\s+(?P<slice5>\d+)\s\|$')

        # |SMS Bytes |         0 |         0 |         0 |         0 |         0 |         0 |
        p4 = re.compile(r'^\|\s*(?P<slice_type>SMS Bytes|HBM Blocks|HBM Bytes)\s*\|\s+(?P<slice0>\d+)\s\|\s+(?P<slice1>\d+)\s\|'
            r'\s+(?P<slice2>\d+)\s\|\s+(?P<slice3>\d+)\s\|\s+(?P<slice4>\d+)\s\|\s+(?P<slice5>\d+)\s\|$')

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # VOQ Stats For : HundredGigE1/0/5 [ 0x544 ]
            m = p0.match(line)
            if m:
                int_dict = ret_dict.setdefault('interface', {}).setdefault(Common.convert_intf_name(m.groupdict()['interface']), {})
                continue

            #          | Asic     |                                 0
            m = p1.match(line)
            if m:
                asic_dict = int_dict.setdefault('asic', {}).setdefault(int(m.groupdict()['asic']), {})
                continue
            # 0      | Enqueued |                        1194566957 |                       78841419162 |
            # | Dropped  |                                 0 |                                 0 |
            # | Total    |                        1194566957 |                       78841419162 |
            # |----------|-----------------------------------------------------------------------|
            m = p2.match(line)
            if m:
                res_dict = m.groupdict()
                if res_dict['voq_id']:
                    voq_dict = asic_dict.setdefault('voq_id', {}).setdefault(res_dict['voq_id'], {})

                pkts_dict = voq_dict.setdefault('packets', {})
                bytes_dict = voq_dict.setdefault('bytes', {})
                pkts_dict.setdefault(res_dict['header'].lower(), int(res_dict['packets']))
                bytes_dict.setdefault(res_dict['header'].lower(), int(res_dict['bytes']))
                continue

            # |   Slice  |         0 |         1 |         2 |         3 |         4 |         5 |
            m = p3.match(line)
            if m:
                slice_dict = voq_dict.setdefault('slice', {})
                group = m.groupdict()
                slice_dict0 = slice_dict.setdefault(group['slice0'], {})
                slice_dict1 = slice_dict.setdefault(group['slice1'], {})
                slice_dict2 = slice_dict.setdefault(group['slice2'], {})
                slice_dict3 = slice_dict.setdefault(group['slice3'], {})
                slice_dict4 = slice_dict.setdefault(group['slice4'], {})
                slice_dict5 = slice_dict.setdefault(group['slice5'], {})
                continue

            # |SMS Bytes |         0 |         0 |         0 |         0 |         0 |         0 |
            m = p4.match(line)
            if m:
                grp_output = m.groupdict()
                slice_type = grp_output['slice_type'].replace(' ', '_').lower()
                slice_dict0.setdefault(slice_type, int(grp_output['slice0']))
                slice_dict1.setdefault(slice_type, int(grp_output['slice1']))
                slice_dict2.setdefault(slice_type, int(grp_output['slice2']))
                slice_dict3.setdefault(slice_type, int(grp_output['slice3']))
                slice_dict4.setdefault(slice_type, int(grp_output['slice4']))
                slice_dict5.setdefault(slice_type, int(grp_output['slice5']))
                continue

        return ret_dict


class ShowPlatformHardwareFedSwitchQosQueueStatsInterfaceClear(ShowPlatformHardwareFedSwitchQosQueueStatsInterface):
    """Parser for show platform hardware fed switch {switch} qos queue stats interface {interface} clear"""

    cli_command = ['show platform hardware fed active qos queue stats interface {interface} clear',
            'show platform hardware fed switch {switch_num} qos queue stats interface {interface} clear']

    def cli(self, interface, switch_num=None, output=None):

        return super().cli(interface=interface, switch_num=switch_num, output=output)


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
                    Optional('oid'): {
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
                                    'rate': Or(int, str),
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
        p3_1 = re.compile(r'^(?P<oid>\d+)\s+\|\s+(?P<c_pb>[\w\-\/]+)\s+\|\s+(?P<cir>\d+)\s+\|\s+(?P<burst>\d+)\s+\|\s+(?P<tx_cir>\d+)\s+\|\s+(?P<tx_burst>\d+)\s+\|\s+(?P<eir_wfq>\d+)\s+\|\s+(?P<act_wfq>\d+)\s+\|\s+(?P<pg_type>[\w\-]+)(\s+\|\s+(?P<child_type>\w+)\s+\|\s+(?P<child_oid>\d+))?$')

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
        # |        | PIR      | 2000000000    | DEFLT | 255    | 67     | PARENT       | 12         | CSTSE     | 1360    |        |
        # | 1026   | CIR      | UNLIMITED     | DEFLT | 255    | 8555   | PARENT       | 0          | OQHSE     | 2653    |        |
        p6_1 = re.compile(r'^(?P<oid>\d+)?\s*\|*\s*(?P<cep_ir>(CIR|EIR|PIR))\s*\|\s*(?P<rate>\w+)\s*\|\s*(?P<burst>\w+)\s*\|'
                          r'\s*(?P<weight>\d+)\s*\|\s*(?P<hw_id>\d+)\s*\|\s*(?P<type>\w+)\s*\|\s*(?P<link_point>\d+)\s*\|'
                          r'\s*(?P<hse_type>\w+)\s*\|\s*(?P<hse_oid>\d+)(\s*\|\s+(?P<voq_id>\d+)\s*\|\s*(?P<in_device>\d+)\|\s*(?P<in_slice>\d+))?$')

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
                if group_dict['oid']:
                    oqhse_sch_dict = svcse_scheduler_dict.setdefault('oid', {}).setdefault(group_dict['oid'], {})
                cep_ir_dict = oqhse_sch_dict.setdefault('cep_ir', {}).setdefault(group_dict['cep_ir'], {})
                try:
                    cep_ir_dict['rate'] = int(group_dict['rate'])
                except ValueError:
                    cep_ir_dict['rate'] = group_dict['rate']
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


class ShowPlatformHardwareFedSwitchQosQueueConfigSchema(MetaParser):
    """
    Schema for
        * 'show platform hardware fed switch {switch_var} qos queue config interface {interface}'
    """

    schema = {
        "interface": {
            Any(): {
                "interface_id": str,
                "voq_id": str,
                "voq_oid": str,
                "voq_set_size": str,
                "base_voq_id": str,
                "base_vsc_ids": list,
                "voq_state": str,
                "voq_flush": str,
                "is_empty": str,
                "profile_oid": {
                    Any(): {
                        "profile_id": str,
                        "device_id": str,
                        "cgm_type": str,
                        "profile_reference_count": str,
                        "is_reserved": str,
                        "for_speeds": str,
                        "associated_voq_offsets": Or(str, list),
                        "hbm_enabled": str,
                        Optional("hgm_block_size"): str,
                        Optional("red_enabled"): str,
                        Optional("fcn_enabled"): str,
                        Optional("queue_user_config"): {
                            Optional("q_limit_hbm_blocks"): str,
                            "red_ema_coefficient": str,
                            Optional("red_flag"): {
                                Any(): {
                                    Optional("minimun_hbm_blocks"): str,
                                    Optional("maximum_hbm_blocks"): str,
                                    Optional("maximum_probability"): str,
                                },
                            },
                        },
                        Optional("queue_hw_values"): {
                            "red_action": str,
                            Optional("red_drop_thresholds"): list,
                            Optional("hbm_free_thresholds"): list,
                            Optional("hbm_voq_age_thresholds"): list,
                            Optional("hbm_voq_thresholds"): list,
                            Optional("red_flag"): {
                                Any(): {
                                    "red_drop_probabilities": list,
                                }
                            },
                        },
                    }
                },
            }
        }
    }


class ShowPlatformHardwareFedSwitchQosQueueConfig(
    ShowPlatformHardwareFedSwitchQosQueueConfigSchema
):
    """
    Parser for
        * 'show platform hardware fed switch {switch_var} qos queue config interface {interface}'
    """

    cli_command = [
        "show platform hardware fed active qos queue config interface {interface}",
        "show platform hardware fed switch {switch_var} qos queue config interface {interface}",
    ]

    def cli(self, interface, switch_var=None, output=None):
        if output is None:
            if switch_var:
                cmd = self.cli_command[1].format(
                    switch_var=switch_var, interface=interface
                )
            else:
                cmd = self.cli_command[0].format(interface=interface)

            output = self.device.execute(cmd)

        # Interface : HundredGigE2/0/34.100 (0x54C)
        p0 = re.compile(
            r"^Interface\s+: (?P<interface>\S+) \((?P<interface_id>\S+)\)$"
        )

        # VOQ OID        : 2114(0x842)
        p1 = re.compile(r"^VOQ OID\s+: (?P<voq_oid>\S+)\((?P<voq_id>\S+)\)$")

        # VOQ Set Size   : 3
        p2 = re.compile(r"^VOQ Set Size\s+: (?P<voq_set_size>\S+)$")

        # Base VOQ ID    : 28952
        p3 = re.compile(r"^Base VOQ ID\s+: (?P<base_voq_id>\S+)$")

        # Base VSC IDs   : 728, 792, 856, 920, 984, 1048
        p4 = re.compile(r"^Base VSC IDs\s+: (?P<base_vsc_ids>[\w\s\,]+)$")

        # VOQ State      : Active
        p5 = re.compile(r"^VOQ State\s+: (?P<voq_state>\S+)$")

        # VOQ Flush      : Flush not active
        p6 = re.compile(r"^VOQ Flush\s+: (?P<voq_flush>.+)$")

        # Is Empty       : Yes
        p7 = re.compile(r"^Is Empty\s+: (?P<is_empty>.+)$")

        # Profile OID            : 433(0x1B1)
        p8_1 = re.compile(
            r"^Profile OID\s+: (?P<profile_oid>\d+)\((?P<profile_id>\w+)\)$"
        )

        # Device ID              : 0
        p9 = re.compile(r"^Device ID\s+: (?P<device_id>\d+)$")

        # CGM Type               : Unicast
        p10 = re.compile(r"^CGM Type\s+: (?P<cgm_type>\w+)$")

        # Profile reference count: 73
        p11 = re.compile(
            r"^Profile reference count\s*: (?P<profile_reference_count>\d+)$"
        )

        # Is Reserved            : Yes
        p12 = re.compile(r"^Is Reserved\s+: (?P<is_reserved>[\w\s]+)$")

        # For speeds             : 10000000000
        p13 = re.compile(r"^For speeds\s+: (?P<for_speeds>\d+)$")

        # Associated VOQ Offsets : 0
        p14 = re.compile(
            r"^Associated VOQ Offsets\s+: (?P<associated_voq_offsets>[\d, ]+)$"
        )

        # HBM Enabled            : Enabled
        p15 = re.compile(r"^HBM Enabled\s+: (?P<hbm_enabled>\w+)$")

        # HBM Block Size         : 6144
        p16 = re.compile(r"^HBM Block Size\s+: (?P<hgm_block_size>\w+)$")

        # RED Enabled            : Enabled
        p17 = re.compile(r"^RED Enabled\s+: (?P<red_enabled>\w+)$")

        # FCN Enabled            : Disabled
        p18 = re.compile(r"^FCN Enabled\s+: (?P<fcn_enabled>\w+)$")

        # Queue User Config      :
        p19 = re.compile(r"^Queue User Config\s+:$")

        # Q-Limit(HBM Blocks)    : 4882
        p19_1 = re.compile(
            r"^Q-Limit\(HBM Blocks\)\s+: (?P<q_limit_hbm_blocks>\d+)$"
        )

        # RED EMA Coefficient    : 1.000000
        p19_2 = re.compile(
            r"^RED EMA Coefficient\s+: (?P<red_ema_coefficient>[\w\.]+)$"
        )

        # RED Green :
        p19_3 = re.compile(r"^RED\s+(?P<red_flag>\w+)\s:$")

        # Minium(HBM BLOCKS)   : 0
        p19_4 = re.compile(
            r"^Minium\(HBM BLOCKS\)\s*: (?P<minimun_hbm_blocks>\d+)$"
        )

        # Maximum(HBM BLOCKS)  : 1220
        p19_5 = re.compile(
            r"^Maximum\(HBM BLOCKS\)\s*: (?P<maximum_hbm_blocks>\d+)$"
        )

        # Maximum Probability  : 0
        p19_6 = re.compile(
            r"^Maximum Probability\s*: (?P<maximum_probability>\d+)$"
        )

        # Queue H/W Values       :
        p20 = re.compile(r"^Queue H/W Values\s+:$")

        # RED Action                     : Drop
        p20_1 = re.compile(r"^RED Action\s+: (?P<red_action>\w+)$")

        # RED Drop thresholds            : 0, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220
        p20_2 = re.compile(
            r"^RED Drop thresholds\s+: (?P<red_drop_thresholds>[\w\s\,]+)$"
        )

        # RED Drop Probabilities[Green]  : 0.000000, 0.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000
        p20_3 = re.compile(
            r"^RED Drop Probabilities\[(?P<red_flag>[\w]+)\]\s+: (?P<red_drop_probabilities>[\w\s\,\.]+)$"
        )

        # HBM Free Thresholds            : 10000, 20000, 40000, 60000, 124992, 250000, 500000, 1000000
        p20_4 = re.compile(
            r"^HBM Free Thresholds\s+: (?P<hbm_free_thresholds>[\w\s\,\.]+)$"
        )

        # HBM VOQ Age Thresholds         : 1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 16, 24, 32, 64, 128
        p20_5 = re.compile(
            r"^HBM VOQ Age Thresholds\s+: (?P<hbm_voq_age_thresholds>[\w\s\,\.]+)$"
        )

        # HBM VOQ Thresholds             : 96, 992, 2000, 4000, 6000, 8000, 12000, 16000, 24000, 32000, 40000, 48000, 56000, 64000, 64512, 65536,
        p20_6 = re.compile(
            r"^HBM VOQ Thresholds\s+: (?P<hbm_voq_thresholds>[\w\s\,\.]+)$"
        )

        ret_dict = {}

        for line in output.splitlines():
            line = line.strip()

            # Interface              : HundredGigE1/0/5 (0x54A)
            m = p0.match(line)
            if m:
                int_dict = ret_dict.setdefault("interface", {}).setdefault(
                    Common.convert_intf_name(m.groupdict()["interface"]), {}
                )
                int_dict["interface_id"] = m.groupdict()["interface_id"]
                continue

            # VOQ OID        : 2114(0x842)
            m = p1.match(line)
            if m:
                int_dict["voq_id"] = m.groupdict()["voq_id"]
                int_dict["voq_oid"] = m.groupdict()["voq_oid"]
                continue

            # VOQ Set Size   : 3
            m = p2.match(line)
            if m:
                int_dict["voq_set_size"] = m.groupdict()["voq_set_size"]
                continue

            # Base VOQ ID    : 28952
            m = p3.match(line)
            if m:
                int_dict["base_voq_id"] = m.groupdict()["base_voq_id"]
                continue

            # Base VSC IDs   : 728, 792, 856, 920, 984, 1048
            m = p4.match(line)
            if m:
                int_dict["base_vsc_ids"] = (
                    m.groupdict()["base_vsc_ids"].replace(" ", "").split(",")
                )
                continue

            # VOQ State      : Active
            m = p5.match(line)
            if m:
                int_dict["voq_state"] = m.groupdict()["voq_state"]
                continue

            # VOQ Flush      : Flush not active
            m = p6.match(line)
            if m:
                int_dict["voq_flush"] = m.groupdict()["voq_flush"]
                continue

            # Is Empty       : Yes
            m = p7.match(line)
            if m:
                int_dict["is_empty"] = m.groupdict()["is_empty"]
                continue

            # Profile OID            : 433(0x1B1)
            m = p8_1.match(line)
            if m:
                profile_dict = int_dict.setdefault("profile_oid", {}).setdefault(
                    m.groupdict()["profile_oid"], {}
                )
                profile_dict["profile_id"] = m.groupdict()["profile_id"]
                continue

            # Device ID              : 0
            m = p9.match(line)
            if m:
                profile_dict["device_id"] = m.groupdict()["device_id"]
                continue

            # CGM Type               : Unicast
            m = p10.match(line)
            if m:
                profile_dict["cgm_type"] = m.groupdict()["cgm_type"]
                continue

            # Profile reference count: 73
            m = p11.match(line)
            if m:
                profile_dict["profile_reference_count"] = m.groupdict()[
                    "profile_reference_count"
                ]
                continue

            # Is Reserved            : Yes
            m = p12.match(line)
            if m:
                profile_dict["is_reserved"] = m.groupdict()["is_reserved"]
                continue

            # For speeds             : 10000000000
            m = p13.match(line)
            if m:
                profile_dict["for_speeds"] = m.groupdict()["for_speeds"]
                continue

            # Associated VOQ Offsets : 0
            m = p14.match(line)
            if m:
                profile_dict["associated_voq_offsets"] = (
                    m.groupdict()["associated_voq_offsets"]
                    .replace(" ", "")
                    .split(",")
                )
                continue

            # HBM Enabled            : Enabled
            m = p15.match(line)
            if m:
                profile_dict["hbm_enabled"] = m.groupdict()["hbm_enabled"]
                continue

            # HBM Block Size         : 6144
            m = p16.match(line)
            if m:
                profile_dict["hgm_block_size"] = m.groupdict()["hgm_block_size"]
                continue

            # RED Enabled            : Enabled
            m = p17.match(line)
            if m:
                profile_dict["red_enabled"] = m.groupdict()["red_enabled"]
                continue

            # FCN Enabled            : Disabled
            m = p18.match(line)
            if m:
                profile_dict["fcn_enabled"] = m.groupdict()["fcn_enabled"]
                continue

            # Queue User Config      :
            m = p18.match(line)
            if m:
                profile_dict["fcn_enabled"] = m.groupdict()["fcn_enabled"]
                continue

            # Queue User Config      :
            m = p19.match(line)
            if m:
                queue_config_dict = profile_dict.setdefault("queue_user_config", {})
                continue

            # Q-Limit(HBM Blocks)    : 1220
            m = p19_1.match(line)
            if m:
                queue_config_dict["q_limit_hbm_blocks"] = m.groupdict()[
                    "q_limit_hbm_blocks"
                ]
                continue

            # RED EMA Coefficient    : 1.000000
            m = p19_2.match(line)
            if m:
                queue_config_dict["red_ema_coefficient"] = m.groupdict()[
                    "red_ema_coefficient"
                ]
                continue

            # RED Green :
            m = p19_3.match(line)
            if m:
                red_dict = queue_config_dict.setdefault("red_flag", {}).setdefault(
                    m.groupdict()["red_flag"], {}
                )
                continue

            # Minium(HBM BLOCKS)   : 0
            m = p19_4.match(line)
            if m:
                red_dict["minimun_hbm_blocks"] = m.groupdict()["minimun_hbm_blocks"]
                continue

            # Maximum(HBM BLOCKS)  : 1220
            m = p19_5.match(line)
            if m:
                red_dict["maximum_hbm_blocks"] = m.groupdict()["maximum_hbm_blocks"]
                continue

            # Maximum Probability  : 0
            m = p19_6.match(line)
            if m:
                red_dict["maximum_probability"] = m.groupdict()[
                    "maximum_probability"
                ]
                continue

            # Queue H/W Values       :
            m = p20.match(line)
            if m:
                queue_hw_dict = profile_dict.setdefault("queue_hw_values", {})
                continue

            # RED Action                     : Drop
            m = p20_1.match(line)
            if m:
                queue_hw_dict["red_action"] = m.groupdict()["red_action"]
                continue

            # RED Drop thresholds            : 0, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220, 1220
            m = p20_2.match(line)
            if m:
                queue_hw_dict["red_drop_thresholds"] = (
                    m.groupdict()["red_drop_thresholds"].replace(" ", "").split(",")
                )
                continue

            # RED Drop Probabilities[Green]  : 0.000000, 0.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000, 1.000000
            m = p20_3.match(line)
            if m:
                red_hw_dict = queue_hw_dict.setdefault("red_flag", {}).setdefault(
                    m.groupdict()["red_flag"], {}
                )
                red_hw_dict["red_drop_probabilities"] = (
                    m.groupdict()["red_drop_probabilities"]
                    .replace(" ", "")
                    .split(",")
                )
                continue

            # HBM Free Thresholds            : 10000, 20000, 40000, 60000, 124992, 250000, 500000, 1000000
            m = p20_4.match(line)
            if m:
                queue_hw_dict["hbm_free_thresholds"] = (
                    m.groupdict()["hbm_free_thresholds"].replace(" ", "").split(",")
                )
                continue

            # HBM VOQ Age Thresholds         : 1, 2, 3, 4, 5, 6, 7, 8, 10, 12, 16, 24, 32, 64, 128
            m = p20_5.match(line)
            if m:
                queue_hw_dict["hbm_voq_age_thresholds"] = (
                    m.groupdict()["hbm_voq_age_thresholds"]
                    .replace(" ", "")
                    .split(",")
                )
                continue

            # HBM VOQ Thresholds             : 96, 992, 2000, 4000, 6000, 8000, 12000, 16000, 24000, 32000, 40000, 48000, 56000, 64000, 64512, 65536,
            m = p20_6.match(line)
            if m:
                queue_hw_dict["hbm_voq_thresholds"] = (
                    m.groupdict()["hbm_voq_thresholds"].replace(" ", "").split(",")
                )
                continue
        
        return ret_dict


class ShowPlatformHardwareAuthenticationStatusSchema(MetaParser):
    """Schema for show platform hardware authentication status."""

    schema = {
        Any(): str
    }


# =====================================
# Parser for:
#  * 'show platform hardware authentication status'
# =====================================
class ShowPlatformHardwareAuthenticationStatus(
    ShowPlatformHardwareAuthenticationStatusSchema
):
    """Parser for show platform hardware authentication status"""

    cli_command = "show platform hardware authentication status"

    def cli(self, output=None):
        if output is None:
            output = self.device.execute(self.cli_command)

        ret_dict = {}

        # SUP 0 Authentication:  pass
        # SUP 1 Authentication:  pass
        # Line Card 1 Authentication:  pass
        # Line Card 2 Authentication:  pass
        # Line Card 5 Authentication:  pass
        # Line Card 6 Authentication:  pass
        # Fan Tray 1 Authentication:  pass
        # Chassis Authentication: pass
        p0 = re.compile(
            r"(?P<hardware>.+Authentication):\s+(?P<Slot>(pass|Not Available|fail|Passed))$"
        )

        for line in output.splitlines():
            line = line.strip()

            # SUP 0 Authentication:  pass
            # SUP 1 Authentication:  pass
            # Line Card 1 Authentication:  pass
            # Line Card 2 Authentication:  pass
            # Line Card 5 Authentication:  pass
            # Line Card 6 Authentication:  pass
            # Fan Tray 1 Authentication:  pass
            # Chassis Authentication: pass
            m = p0.match(line)
            if m:
                group = m.groupdict()
                ret_dict[group['hardware']] = group['Slot']
                continue

        return ret_dict
