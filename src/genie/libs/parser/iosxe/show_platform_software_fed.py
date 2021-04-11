'''
IOSXE C9300 parsers for the following show commands:
    * show platform soft fed sw active mpls forwd label <label> detail
'''
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

# parser utils
#from genie.libs.parser.utils.common import Common
# =============================================
# Parser for 'show platform soft fed sw active mpls forwd label <label> detail'
# Parser for 'show platform soft fed active mpls forwd label <label> detail'
# =============================================
class ShowPlatformSoftwareFedSchema(MetaParser):
    """ Schema for:
        *show platform soft fed sw active mpls forwd label <label> detail
    """
    schema = {
        'LENTRY_label':{
            Optional(Any()):{
                'label': int,
                Optional('nobj'): str,
                Optional('lentry_hdl'): str,
                Optional('modify_cnt'): int,
                Optional('backwalk_cnt'): int,
                Optional('lspa_handle'): str,
                Optional('AAL'):{
                    Optional('id'): int,
                    Optional('lbl'): int,
                    Optional('eos0'):{
                        Optional('adj_hdl'): str,
                        Optional('hw_hdl'): str,
                        },
                    Optional('eos1'):{
                        Optional('adj_hdl'): str,
                        Optional('hw_hdl'): str,
                    },
                    Optional('deagg_vrf_id'): int,
                    Optional('lspa_handle'): str,
                    },
                Optional('EOS'):{
                    Optional('objid'): int,
                    Optional('local_label'): int,
                    Optional('flags'): str,
                    Optional('pdflags'): str,
                    Optional('nobj0'): str,
                    Optional('nobj1'): str,
                    Optional('modify'): int,
                    Optional('bwalk'): int,     
                },
                Optional('LABEL'):{
                    Optional(Any()):{
                        Optional('link_type'): str,
                        Optional('local_label'): int,
                        Optional('outlabel'):str,
                        Optional('flags'): str,
                        Optional('pdflags'): str,
                        Optional('adj_handle'): str,
                        Optional('unsupported_recursion'): int,
                        Optional('olbl_changed'): int,
                        Optional('local_adj'): int,
                        Optional('modify_cnt'): int,
                        Optional('bwalk_cnt'): int,
                        Optional('subwalk_cnt'): int,
                        Optional('collapsed_oce'): int,
                        Optional('AAL'):{
                            Optional('id'):int,
                            Optional('lbl'): int,
                            Optional('smac'): str,
                            Optional('dmac'): str,
                            Optional('sub_type'): int,
                            Optional('link_type'): int,
                            Optional('adj_flags'): int,
                            Optional('label_type'): int,
                            Optional('rewrite_type'): str,
                            Optional('vlan_id'): int,
                            Optional('vrf_id'): int,
                            Optional('ri'): str,
                            Optional('ri_id'): str,
                            Optional('phdl'): str,
                            Optional('ref_cnt'):int,
                            Optional('si'): str,
                            Optional('si_id'): str,
                            Optional('di_id'): str,
                                },
                            },
                        },
                Optional('ADJ'):{
                    Optional(Any()):{
                        Optional('link_type'): str,
                        Optional('ifnum'): str,
                        Optional('adj'): str,
                        Optional('si'): str,
                        Optional('IPv4'): str,
                        },
                    },
                Optional('LB'):{
                    Optional(Any()):{
                        Optional('ecr_map_objid'): int,
                        Optional('link_type'): str, 
                        Optional('num_choices'): int,
                        Optional('flags'): str,
                        Optional('mpls_ecr'): int,
                        Optional('local_label'): int,
                        Optional('path_inhw'): int,
                        Optional('ecrh'): str,
                        Optional('old_ecrh'): str,
                        Optional('modify_cnt'): int,
                        Optional('bwalk_cnt'): int, 
                        Optional('subwalk_cnt'): int,
                        Optional('finish_cnt'): int,
                        Optional('bwalk'): str,
                        Optional('AAL'):{
                            Optional('ecr_id'): int,
                            Optional('af'): int,
                            Optional('ecr_type'): str,
                            Optional('ref'): int,
                            Optional('ecrh'): str,
                            Optional('hwhdl'): str,
                        }
                    },
                },
                Optional('Sw_Enh_ECR_scale'):{
                    Optional(Any()):{
                        Optional('llabel'): int,
                        Optional('eos'): int, 
                        Optional('adjs'): int,
                        Optional('mixed_adj'): str, 
                        Optional('reprogram_hw'): str,
                        Optional('ecrhdl'): str,
                        Optional('ecr_hwhdl'): str,
                        Optional('mod_cnt'): int,
                        Optional('prev_npath'): int,
                        Optional('pmismatch'): int,
                        Optional('pordermatch'): int,
                        Optional('ecr_adj'):{
                            Optional(Any()):{
                                Optional('is_mpls_adj'): int,
                                Optional('l3adj_flags'): str,
                                Optional('recirc_adj_id'): int,
                                Optional('sih'): str,
                                Optional('di_id'): int, 
                                Optional('rih'): str,
                                Optional('adj_lentry'): str,
                            }
                        },
                    },
                },    
           
            }
        }
    }
    
# ================================================================
# Parser for:
#   * 'show platform software fed '
# ================================================================
class ShowPlatformSoftwareFed(ShowPlatformSoftwareFedSchema):
    ''' Parser for:
        * ' show platform soft fed sw active mpls forwd label <label> detail '
    '''

    cli_command = ['show platform software fed active mpls forwarding label {label} detail', 'show platform software fed {switch} active mpls forwarding label {label} detail']
    def cli(self, label='',switch='',output=None):
        ''' cli for:
         ' show platform soft fed sw active mpls forwarding label <label> detail '
         ' show platform soft fed active mpls forwarding label <label> detail '
        '''
        if output is None:
            # Build command
            if not switch:
                cmd = self.cli_command[0].format(label=label)
            else:
                cmd = self.cli_command[1].format(switch=switch, label=label)
            # Execute command
            out = self.device.execute(cmd)
        else:
            out = output
        

        #LENTRY:label:18 nobj:(EOS, 76) lentry_hdl:0x13000005
        p1 = re.compile(r'^LENTRY:label:+(?P<label>\d+)\s+nobj:+'
                        r'(?P<nobj>[\S\s]+)\s+lentry_hdl:+(?P<lentry_hdl>\S+)$')
        #modify_cnt:1 backwalk_cnt:2
        p2 = re.compile(r'^modify_cnt:+(?P<modify_cnt>\d+)\s+'
                        r'backwalk_cnt:+(?P<backwalk_cnt>\d+)$')
        #lspa_handle:0
        p3 = re.compile(r'^lspa_handle:+(?P<lspa_handle>\w+)\s$')

        #AAL: id:318767109 lbl:18
        p4 = re.compile(r'^AAL:\s+id:+(?P<id>\d+)\s+lbl:+(?P<lbl>\d+)$')

        #eos0:[adj_hdl:0x76000024, hw_hdl:0x7ff7911bf758]
        p5 = re.compile(r'^eos0:\[+adj_hdl:+(?P<adj_hdl>\w+)+,\s+hw_hdl:+(?P<hw_hdl>\w+)+\]+$')

        #eos1:[adj_hdl:0xeb000022, hw_hdl:0x7ff7911bf548]
        p6 = re.compile(r'^eos1:\[+adj_hdl:+(?P<adj_hdl>\w+)+,\s+hw_hdl:+'
                        r'(?P<hw_hdl>\w+)+\]+$')

        #deagg_vrf_id = 0 lspa_handle:0
        p7 = re.compile(r'^deagg_vrf_id\s+=\s+(?P<deagg_vrf_id>\d+)+\s+lspa_handle:+'
                        r'(?P<lspa_handle>\w+)+$')
        #EOS:objid:76 local_label:0 flags:0:() pdflags:0
        p8 = re.compile(r'^EOS:+objid:+(?P<objid>\d+)\s+local_label:+'
                        r'(?P<local_label>\d+)\s+flags:+\S:+'
                        r'(?P<flags>[\S\s]+)\s+pdflags:+'
                        r'(?P<pdflags>\S+)$')
        #nobj0:(LABEL, 78), nobj1:(LABEL, 75) modify:1 bwalk:0
        p9 = re.compile(r'^nobj0:+(?P<nobj0>[\S\s]+)\s+nobj1:+'
                        r'(?P<nobj1>[\S\s]+)\s+modify:+'
                        r'(?P<modify>\d+)\s+bwalk:+(?P<bwalk>\d+)$')
        #LABEL:objid:78 link_type:MPLS local_label:18 outlabel:(3, 0)
        p10 = re.compile(r'LABEL:+objid:+(?P<objid>\d+)\s+link_type:+'
                         r'(?P<link_type>\w+)\s+local_label:+'
                         r'(?P<local_label>\d+)\s+outlabel:+(?P<outlabel>[\S\s]+)$')

        #flags:0x18:(POP,PHP,) pdflags:0:(INSTALL_HW_OK,) adj_handle:0x76000024
        p11 = re.compile(r'^flags:+\w+(?P<flags>[\S]+)\s+pdflags:+\w+'
                         r'(?P<pdflags>[\S]+)\s+adj_handle:+(?P<adj_handle>\w+)$')
        #unsupported recursion:0 olbl_changed 0 local_adj:0 modify_cnt:0
        p12 = re.compile(r'^unsupported\s+recursion:+(?P<unsupported_recursion>\d+)\s+olbl_changed\s+'
                         r'(?P<olbl_changed>\d+)\s+local_adj:+'
                         r'(?P<local_adj>\d+)\s+modify_cnt:+(?P<modify_cnt>\d+)$')

        #bwalk_cnt:0 subwalk_cnt:0 collapsed_oce:0
        p13 = re.compile(r'^bwalk_cnt:+(?P<bwalk_cnt>\d+)\s+subwalk_cnt:+'
                         r'(?P<subwalk_cnt>\d+)\s+collapsed_oce:+(?P<collapsed_oce>\d+)$')
        #AAL: id:1979711524 lbl:0 smac:7486.0b05.0d46 dmac:5897.bd7a.6f80
        p14 = re.compile(r'^AAL:\s+id:+(?P<id>\d+)\s+lbl:+(?P<lbl>\d+)\s+smac:+'
                         r'(?P<smac>\S+)\s+dmac:+(?P<dmac>\S+)\s$')
        #sub_type:0 link_type:2 adj_flags:0 label_type:1 rewrite_type:POP2MPLS(138)
        p15 = re.compile(r'^sub_type:+(?P<sub_type>\d+)\s+link_type:+'
                         r'(?P<link_type>\d+)\s+adj_flags:+(?P<adj_flags>\d+)\s+label_type:+'
                         r'(?P<label_type>\d+)\s+rewrite_type:+(?P<rewrite_type>\S+)\s$')
        #vlan_id:0 vrf_id:0 ri:0x7ff7911c7808, ri_id:0x22 phdl:0xe90000d3, ref_cnt:1
        p16 = re.compile(r'^vlan_id:+(?P<vlan_id>\d+)\s+vrf_id:+(?P<vrf_id>\d+)\s+ri:+'
                         r'(?P<ri>\w+)+,\s+ri_id:+(?P<ri_id>\w+)\s+phdl:+'
                         r'(?P<phdl>\w+)+,\s+ref_cnt:+(?P<ref_cnt>\d+)\s$')
        #si:0x7ff7911c6098, si_id:0x4007, di_id:0x5378
        p17 = re.compile(r'^si:+(?P<si>\w+)+,\s+si_id:+(?P<si_id>\w+)+,\s+di_id:+(?P<di_id>\w+)\s$')
        #ADJ:objid:71 {link_type:MPLS ifnum:0x7c, adj:0x53000020, si: 0x7ff791190278
        p18 = re.compile(r'ADJ:objid:+(?P<objid>\d+)+\s\{+link_type:+'
                         r'(?P<link_type>\w+)\s+ifnum:+(?P<ifnum>\w+)+,\s+adj:+'
                         r'(?P<adj>\w+)+,\s+si:+\s(?P<si>\w+)+  }$')
        #ADJ:objid:69 {link_type:IP ifnum:0x7c, adj:0xa000001f, si: 0x7ff791190278  IPv4:       93.1.1.11 }
        p19 = re.compile(r'ADJ:objid:+(?P<objid>\d+)+\s\{+link_type:+'
                         r'(?P<link_type>\w+)\s+ifnum:+(?P<ifnum>\w+)+,\s+adj:+'
                         r'(?P<adj>\w+)+,\s+si:+\s(?P<si>\w+)\s+IPv4:+\s+'
                         r'(?P<IPv4>[\d\.]+)\s+\}$')
        
        #LENTRY:label:75 not found...
        p20 = re.compile(r'^LENTRY:label:+(?P<label>\d+)\snot +found\S+$')
        
        #AAL: Handle not found:0
        p21 = re.compile(r'^AAL:\s+Handle\ not\ found:\S$')
       
        #LB:obj_id:38 ecr_map_objid:0 link_type:IP num_choices:2 Flags:0
        p22 = re.compile(r'LB:+obj_id:+(?P<obj_id>\d+)\s+ecr_map_objid:+'
                         r'(?P<ecr_map_objid>\d+)\s+link_type:+'
                         r'(?P<link_type>\w+)\s+num_choices:+'
                         r'(?P<num_choices>\d+)\s+Flags:+(?P<flags>\w+)$')
        #mpls_ecr:1 local_label:24 path_inhw:2 ecrh:0xf9000002 old_ecrh:0
        p23 = re.compile(r'mpls_ecr:+(?P<mpls_ecr>\d+)\s+local_label:+'
                         r'(?P<local_label>\d+)\s+path_inhw:+'
                         r'(?P<path_inhw>\d+)\s+ecrh:+'
                         r'(?P<ecrh>\w+)\s+old_ecrh:+(?P<old_ecrh>\w+)$')
        #modify_cnt:0 bwalk_cnt:0 subwalk_cnt:0 finish_cnt:0
        p24 = re.compile(r'modify_cnt:+(?P<modify_cnt>\d+)\s+bwalk_cnt:+'
                         r'(?P<bwalk_cnt>\d+)\s+subwalk_cnt:+'
                         r'(?P<subwalk_cnt>\d+)\s+finish_cnt:+'+
                         r'(?P<finish_cnt>\d+)$')
        #bwalk:[req:0 in_prog:0 nested:0]
        p25 = re.compile(r'bwalk:+(?P<bwalk>[\S\s]+)$')
        #AAL: ecr:id:4177526786 af:0 ecr_type:0 ref:3 ecrh:0x7f02737e49f8(28:2)
        
        p26 = re.compile(r'AAL:\s+ecr:id:+(?P<ecr_id>\d+)\s+af:(?P<af>\d+)\s+ecr_type:+'
                         r'(?P<ecr_type>\w+)\s+ref:+(?P<ref>\d+)\s+ecrh:+(?P<ecrh>\S+)\s+$')
        #hwhdl:1937656312 ::0x7f02737e11c8,0x7f02737e2728,0x7f02737e11c8,0x7f02737e2728
        p27 = re.compile(r'hwhdl+(?P<hwhdl>[\S\s]+)$')
        #Sw Enh ECR scale: objid:38 llabel:24 eos:1 #adjs:2 mixed_adj:0
        p28 = re.compile(r'Sw +Enh +ECR +scale:\s+objid:+(?P<objid>\d+)\s+llabel:+'
                         r'(?P<llabel>\d+)\s+eos:+(?P<eos>\d+)\s+\#adjs:+'
                         r'(?P<adjs>\d+)\s+mixed_adj:+(?P<mixed_adj>\w+)$')
        #reprogram_hw:0 ecrhdl:0xf9000002 ecr_hwhdl:0x7f02737e49f8
        p29 = re.compile(r'reprogram_hw:+(?P<reprogram_hw>\w+)\s+ecrhdl:+'
                         r'(?P<ecrhdl>\w+)\s+ecr_hwhdl:+(?P<ecr_hwhdl>\w+)$')
        # mod_cnt:0 prev_npath:0 pmismatch:0 pordermatch:0
        p30 = re.compile(r'mod_cnt:+(?P<mod_cnt>\d+)\s+prev_npath:+'
                         r'(?P<prev_npath>\d+)\s+pmismatch:+(?P<pmismatch>\d+)\s+pordermatch:+'
                         r'(?P<pordermatch>\d+)$')
        #ecr_adj: id:1644167265 is_mpls_adj:1 l3adj_flags:0x100000
        p31 = re.compile(r'(?P<ecr_adj>\S+):\s+id:+(?P<id>\d+)\s+is_mpls_adj:+'
                         r'(?P<is_mpls_adj>\d+)\s+l3adj_flags:+(?P<l3adj_flags>\w+)$')
        # recirc_adj_id:3120562239
        p32 = re.compile(r'recirc_adj_id:+(?P<recirc_adj_id>\d+)$')
        # sih:0x7f02737e11c8(182) di_id:20499 rih:0x7f02737e0bf8(74)
        p33 = re.compile(r'sih:+(?P<sih>\S+)\s+di_id:(?P<di_id>\d+)\s+rih:+(?P<rih>\S+)$')
        # adj_lentry [eos0:0x7f02734123b8 eos1:0x7f02737ec5e8]
        p34 = re.compile(r'adj_lentry\s+(?P<adj_lentry>[\S\s]+)$')
        #ecr_prefix_adj: id:2483028067 (ref:1)
        p35 = re.compile(r'(?P<ecr_prefix_adj>\S+):\s+id:+(?P<id>\d+)\s+\S+$')    
        # Init vars
        ret_dict = {}
        for line in out.splitlines():
            line = line.strip()
            eos_dict = {}
            m = p1.match(line)
            if m:
                group = m.groupdict()
                label_id = int(group['label'])
                lentry_dict = ret_dict.setdefault('LENTRY_label', {}).setdefault(label_id, {})
                lentry_dict['label'] = int(group['label'])
                lentry_dict['nobj'] = str(group['nobj'])
                lentry_dict['lentry_hdl'] = str(group['lentry_hdl'])
                continue
            m = p2.match(line)
            if m:
                group = m.groupdict()
                lentry_dict['modify_cnt'] = int(group['modify_cnt'])
                lentry_dict['backwalk_cnt'] = int(group['backwalk_cnt'])
                continue
            m = p3.match(line)
            if m:
                group = m.groupdict()
                lentry_dict['lspa_handle'] = str(group['lspa_handle'])
                continue
            m = p4.match(line)
            if m:
                group = m.groupdict()
                aal_dict = ret_dict['LENTRY_label'][label_id].setdefault('AAL', {})
                aal_dict['id'] = int(group['id'])
                aal_dict['lbl'] = int(group['lbl'])
                continue
            
            m = p5.match(line)
            if m:
                group = m.groupdict()
                eos0_dict = ret_dict['LENTRY_label'][label_id]['AAL'].setdefault('eos0', {})
                eos0_dict['adj_hdl'] = str(group['adj_hdl'])
                eos0_dict['hw_hdl'] = str(group['hw_hdl'])
                continue
            m = p6.match(line)
            if m:
                group = m.groupdict()
                eos1_dict = ret_dict['LENTRY_label'][label_id]['AAL'].setdefault('eos1', {})
                eos1_dict['adj_hdl'] = str(group['adj_hdl'])
                eos1_dict['hw_hdl'] = str(group['hw_hdl'])
                continue
            m = p7.match(line)
            if m:
                group = m.groupdict()
                aal_dict['deagg_vrf_id'] = int(group['deagg_vrf_id'])
                aal_dict['lspa_handle'] = str(group['lspa_handle'])
                continue
            
            m = p8.match(line)
            if m:
                group = m.groupdict()
                eos_dict = ret_dict['LENTRY_label'][label_id].setdefault('EOS', {})
                eos_dict['objid'] = int(group['objid'])
                eos_dict['local_label'] = int(group['local_label'])
                eos_dict['flags'] = str(group['flags'])
                eos_dict['pdflags'] = str(group['pdflags'])
                continue
            m = p9.match(line)
            if m:
                group = m.groupdict()
                eos_dict['nobj0'] = str(group['nobj0'])
                eos_dict['nobj1'] = str(group['nobj1'])
                eos_dict['modify'] = int(group['modify'])
                eos_dict['bwalk'] = int(group['bwalk'])
                continue
            
            m = p10.match(line)
            if m:
                group = m.groupdict()
                objid = int(group['objid'])
                label_dict = ret_dict['LENTRY_label'][label_id].setdefault('LABEL', {}).setdefault(objid, {})
                label_dict['link_type'] = str(group['link_type'])
                label_dict['local_label'] = int(group['local_label'])
                label_dict['outlabel'] = str(group['outlabel'])
                continue
             
            m = p11.match(line)
            if m:
                group = m.groupdict()
                label_dict['flags'] = str(group['flags'])
                label_dict['pdflags'] = str(group['pdflags'])
                label_dict['adj_handle'] = str(group['adj_handle'])
                continue
            m = p12.match(line)
            if m:
                group = m.groupdict()
                label_dict['unsupported_recursion'] = int(group['unsupported_recursion'])
                label_dict['olbl_changed'] = int(group['olbl_changed'])
                label_dict['local_adj'] = int(group['local_adj'])
                label_dict['modify_cnt'] = int(group['modify_cnt'])
                continue
            m = p13.match(line)
            if m:
                group = m.groupdict()
                label_dict['bwalk_cnt'] = int(group['bwalk_cnt'])
                label_dict['subwalk_cnt'] = int(group['subwalk_cnt'])
                label_dict['collapsed_oce'] = int(group['collapsed_oce'])
                continue
            m = p14.match(line)
            if m:
                group = m.groupdict()
                labelaal_dict = ret_dict['LENTRY_label'][label_id]['LABEL'][objid].setdefault('AAL', {})
                labelaal_dict['id'] = int(group['id'])
                labelaal_dict['lbl'] = str(group['lbl'])
                labelaal_dict['smac'] = int(group['smac'])
                labelaal_dict['dmac'] = str(group['dmac'])
                continue
            m = p15.match(line)
            if m:
                group = m.groupdict()
                labelaal_dict['sub_type'] = int(group['sub_type'])
                labelaal_dict['link_type'] = int(group['link_type'])
                labelaal_dict['adj_flags'] = int(group['adj_flags'])
                labelaal_dict['label_type'] = int(group['label_type'])
                labelaal_dict['rewrite_type'] = str(group['rewrite_type'])
                continue
            m = p16.match(line)
            if m:
                group = m.groupdict()
                labelaal_dict['vlan_id'] = int(group['vlan_id'])
                labelaal_dict['vrf_id'] = int(group['vrf_id'])
                labelaal_dict['ri'] = str(group['ri'])
                labelaal_dict['ri_id'] = str(group['ri_id'])
                labelaal_dict['phdl'] = str(group['phdl'])
                labelaal_dict['ref_cnt'] = int(group['ref_cnt'])
                continue
            m = p17.match(line)
            if m:
                group = m.groupdict()
                labelaal_dict['si'] = str(group['si'])
                labelaal_dict['si_id'] = str(group['si_id'])
                labelaal_dict['di_id'] = str(group['di_id'])
                continue
            m = p18.match(line)
            if m:
                group = m.groupdict()
                objid = int(group['objid'])
                adj_dict = ret_dict['LENTRY_label'][label_id].setdefault('ADJ', {}).setdefault(objid, {})
                adj_dict['link_type'] = str(group['link_type'])
                adj_dict['ifnum'] = str(group['ifnum'])
                adj_dict['adj'] = str(group['adj'])
                adj_dict['si'] = str(group['si'])
                continue
            m = p19.match(line)
            if m:
                group = m.groupdict()
                objid = int(group['objid'])
                adj_dict = ret_dict['LENTRY_label'][label_id].setdefault('ADJ', {}).setdefault(objid, {})
                adj_dict['link_type'] = str(group['link_type'])
                adj_dict['ifnum'] = str(group['ifnum'])
                adj_dict['adj'] = str(group['adj'])
                adj_dict['si'] = str(group['si'])
                adj_dict['IPv4'] = str(group['IPv4'])
                continue
            m = p20.match(line)
            if m:
                group = m.groupdict()
                label_id = int(group['label'])
                lentry_dict = ret_dict.setdefault('LENTRY_label', {}).setdefault(label_id,{})
                lentry_dict['label'] = int(group['label'])
                continue
            m = p21.match(line)
            if m:
                group = m.groupdict()
                labelaal_dict = ret_dict['LENTRY_label'][label_id].setdefault('AAL', {})
                continue
            m = p22.match(line)
            if m:
                group = m.groupdict()
                objid1 = int(group['obj_id'])
                lb_dict = ret_dict['LENTRY_label'][label_id].setdefault('LB', {}).setdefault(objid1, {})
                lb_dict['ecr_map_objid'] = int(group['ecr_map_objid'])
                lb_dict['link_type'] = str(group['link_type'])
                lb_dict['num_choices'] = int(group['num_choices'])
                continue

            m = p23.match(line)
            if m:
                group = m.groupdict()
                lb_dict['mpls_ecr'] = int(group['mpls_ecr'])
                lb_dict['local_label'] = int(group['local_label'])
                lb_dict['path_inhw'] = int(group['path_inhw'])
                lb_dict['ecrh'] = str(group['ecrh'])
                lb_dict['old_ecrh'] = str(group['old_ecrh'])
                continue
            m = p24.match(line)
            if m:
                group = m.groupdict()
                lb_dict['modify_cnt'] = int(group['modify_cnt'])
                lb_dict['bwalk_cnt'] = int(group['bwalk_cnt'])
                lb_dict['subwalk_cnt'] = int(group['subwalk_cnt'])
                lb_dict['finish_cnt'] = int(group['finish_cnt'])
                continue
            
            m = p25.match(line)
            if m:
                group = m.groupdict()
                lb_dict['bwalk'] = str(group['bwalk'])
                lb_dict['AAL'] = {}
                continue
            
            m = p26.match(line)
            if m:
                group = m.groupdict()
                lb_dict['AAL']['ecr_id'] = int(group['ecr_id'])
                lb_dict['AAL']['af'] = int(group['af'])
                lb_dict['AAL']['ecr_type'] = str(group['ecr_type'])
                lb_dict['AAL']['ref'] = int(group['ref'])
                lb_dict['AAL']['ecrh'] = str(group['ecrh'])
                continue
            m = p27.match(line)
            if m:
                group = m.groupdict()
                lb_dict['AAL']['hwhdl'] = str(group['hwhdl'])
                continue          
            m = p28.match(line)
            if m:
                group = m.groupdict()
                objid = int(group['objid'])
                ecr_dict = ret_dict['LENTRY_label'][label_id].setdefault('Sw_Enh_ECR_scale', {}).setdefault(objid, {})
                ecr_dict['llabel'] = int(group['llabel'])
                ecr_dict['eos'] = int(group['eos'])
                ecr_dict['adjs'] = int(group['adjs'])
                ecr_dict['mixed_adj'] = str(group['mixed_adj'])
                continue    
            m = p29.match(line)
            if m:
                group = m.groupdict()
                ecr_dict['reprogram_hw'] = str(group['reprogram_hw'])
                ecr_dict['ecrhdl'] = str(group['ecrhdl'])
                ecr_dict['ecr_hwhdl'] = str(group['ecr_hwhdl'])
                continue
            m = p30.match(line)
            if m:
                group = m.groupdict()
                ecr_dict['mod_cnt'] = int(group['mod_cnt'])
                ecr_dict['prev_npath'] = int(group['prev_npath'])
                ecr_dict['pmismatch'] = int(group['pmismatch'])
                ecr_dict['pordermatch'] = int(group['pordermatch'])
                ecr_dict['ecr_adj'] = {}
                continue
            
            m = p31.match(line)
            if m:
                group = m.groupdict()
                id1 = int(group['id'])
                ecr_dict['ecr_adj'][id1] = {}
                ecr_dict['ecr_adj'][id1]['is_mpls_adj'] = int(group['is_mpls_adj'])
                ecr_dict['ecr_adj'][id1]['l3adj_flags'] = str(group['l3adj_flags'])
                continue

            m = p32.match(line)
            if m:
                group = m.groupdict()
                ecr_dict['ecr_adj'][id1]['recirc_adj_id'] = int(group['recirc_adj_id'])
                continue
        
            m = p33.match(line)
            if m:
                group = m.groupdict()
                ecr_dict['ecr_adj'][id1]['sih'] = str(group['sih'])
                ecr_dict['ecr_adj'][id1]['di_id'] = int(group['di_id'])
                ecr_dict['ecr_adj'][id1]['rih'] = str(group['rih'])
                continue
            m = p34.match(line)
            if m:
                group = m.groupdict()
                ecr_dict['ecr_adj'][id1]['adj_lentry'] = str(group['adj_lentry'])
                continue   

        return ret_dict

    