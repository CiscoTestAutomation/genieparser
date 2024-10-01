'''show_platform.py

IOSXE c9610 parsers for the following show commands:
    * show platform hardware fed active fwd-asic resource tcam utilization
    * show platform software fed {switch} {mode} acl info db detail
    * show platform software fed {mode} acl info db detail
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
