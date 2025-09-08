"""show_platform_software_fed_ip.py

    * 'show platform software fed {switch} {active} ipv6 mfib vrf {vrf_name} {group} {source}',
    * 'show platform software fed {switch} {active} ipv6 mfib {group} {source}',
    * 'show platform software fed {active} ipv6 mfib vrf {vrf_name} {group} {source}',
    * 'show platform software fed {active} ipv6 mfib {group} {source}'
"""
# Python
import re
import logging

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, ListOf

log = logging.getLogger(__name__)

class ShowPlatformSoftwareFedSwitchActiveIpMfibVrfSchema(MetaParser):
    """Schema for show platform software fed switch active ipv6 mfib vrf {vrf_name} {group} {source}"""
    schema = {
        'mfib': {
            int : {
                'mvrf': int,
                'group': str,
                'source': str,
                'attrs': {
                    'hw_flag': str,
                    'mlist_flags': str,
                    'mlist_hndl_id': str,
                    'mlist_urid': str,
                    'fset_urid_hash': str,
                    Optional('fset_aux_urid'): str,
                    'rpf_adjacency_id': str,
                    'cpu_credit': int,
                    Optional('total_packets'): int,
                    Optional('pps_approx'): int,
                    'oif_count': int,
                    'oif_details': ListOf({
                        'adjid': str,
                        'interface': str,
                        Optional('parentif'): str,
                        Optional('hwflag'): str,
                        'flags': ListOf(str),
                        Optional('intf_type'): str,
                        Optional('msg_type'): str,
                        }),
                    'gid': int,
                    'asic': {
                        int: {
                            'mcid_oid_asic': int,
                        },
                    },
                    Optional('hw_asic_info'): {
                        int: {
                            Optional('ip_mcid_oid'): int,
                            Optional('cookie'): str,
                            Optional('rpf_port_oid'): int,
                            Optional('rpfid'): int,
                            Optional('use_rpfid'): int,
                            Optional('punt_and_forward'): int,
                            Optional('punt_on_rpf_fail'): int,
                            Optional('enable_rpf_check'): int,
                            }
                        }
                    }
                }
            }
        }
    
class ShowPlatformSoftwareFedSwitchActiveIpMfibVrf(ShowPlatformSoftwareFedSwitchActiveIpMfibVrfSchema):
    """Parser for show platform software fed switch active ipv6 mfib vrf {vrf_name} {group} {source}"""

    cli_command = [
        'show platform software fed {switch} {active} ipv6 mfib vrf {vrf_name} {group} {source}',
        'show platform software fed {switch} {active} ipv6 mfib {group} {source}',
        'show platform software fed {active} ipv6 mfib vrf {vrf_name} {group} {source}',
        'show platform software fed {active} ipv6 mfib {group} {source}'
    ]

    def cli(self, switch='', active='', vrf_name='', group='', source='', output=None):
        if output is None:
            if vrf_name:
                if switch:
                    cmd = self.cli_command[0].format(switch=switch, active=active, vrf_name=vrf_name, group=group, source=source)
                else:
                    cmd = self.cli_command[2].format(active=active, vrf_name=vrf_name, group=group, source=source)
            else:
                if switch:
                    cmd = self.cli_command[1].format(switch=switch, active=active, group=group, source=source)
                else:
                    cmd = self.cli_command[3].format(active=active, group=group, source=source)
            output = self.device.execute(cmd)

        ret_dict = {}

        # Mvrf: 3  ( 40::2, ff1e::1 ) Attrs:
        p0 = re.compile(r'^Mvrf: +(?P<mvrf>\d+) +\( +(?P<source>[\w\:\.\/\*]+), +(?P<group>[\w\:\.\/]+) +\) +Attrs:( C)?$')

        # Hw Flag                 : InHw
        # Hw Flag                 : InHw  EntryActive
        p1 = re.compile(r'^Hw Flag +: +(?P<hw_flag>[\w\s]+)$')        

        # Mlist Flags             : None
        p2 = re.compile(r'^Mlist Flags +: +(?P<mlist_flags>\w+)$')

        # Mlist_hndl (Id)         : 0x11889275ea0 ( 0xc823 )
        p3 = re.compile(r'^Mlist_hndl \(Id\) +: +(?P<mlist_hndl_id>[\w\(\)\s]+)$')

        # Mlist Urid              : 0x10000000003238e8
        p4 = re.compile(r'^Mlist Urid +: +(?P<mlist_urid>[\w]+)$')

        # Fset Urid (Hash)        : 0x300000000031f715 ( 68af2994 )
        p5 = re.compile(r'^Fset Urid \(Hash\) +: +(?P<fset_urid_hash>[\w\(\)\s]+)$')

        # Fset Aux Urid           : 0x0
        p5_1 = re.compile(r'^Fset Aux Urid +: +(?P<fset_aux_urid>[\w]+)$')

        # RPF Adjacency ID        : 0xf80059d2
        p6 = re.compile(r'^RPF Adjacency ID +: +(?P<rpf_adjacency_id>[\w]+)$')

        # CPU Credit              : 0
        p7 = re.compile(r'^CPU Credit +: +(?P<cpu_credit>\d+)$')

        # Total Packets           : 4643 ( 9 pps approx.)
        p8 = re.compile(r'^Total Packets +: +(?P<total_packets>\d+) +\( +(?P<pps_approx>\d+) pps approx\.\)$')

        # OIF Count               : 3
        p9 = re.compile(r'^OIF Count +: +(?P<oif_count>\d+)$')

        # OIF Details:
        p10 = re.compile(r'^OIF Details:$')

        # AdjID          Interface          ParentIf        HwFlag      Flags      IntfType       MsgType
        p10_1 = re.compile(r'^AdjID\s+Interface\s+ParentIf\s+HwFlag\s+Flags(\s+IntfType\s+MsgType)?$')

        # 0xc851         Tu315              --------         ---        F NS
        p11 = re.compile(r'^(?P<adjid>[\w]+) +(?P<interface>[\w\/]+) +(?P<parentif>[\w\-]+) +(?P<hwflag>[\w\-]+) +(?P<flags>[A|F|NS|\s]+)(\s+(?P<intf_type>[\w]+))?(\s+(?P<msg_type>[\w\s]+))?$')

        # GID                   : 8631
        p12 = re.compile(r'^GID +: +(?P<gid>\d+)$')

        # MCID OID Asic[0]      : 1346
        p13 = re.compile(r'^MCID OID Asic\[(?P<asic>[\d]+)] +: +(?P<mcid_oid_asic>\d+)$')

        # Hardware Info ASIC[0] :
        p14 = re.compile(r'^Hardware Info ASIC\[(?P<asic_number>[\d]+)] +:$')

        # IP MCID OID         :3272 (cookie:urid:0x30::1b6)
        p15 = re.compile(r'^IP MCID OID +:(?P<ip_mcid_oid>\d+) +\(cookie:urid:(?P<cookie>[\w\:\.\/]+)\)$')

        # RPF PORT OID        :1493
        p16 = re.compile(r'^RPF PORT OID +:(?P<rpf_port_oid>\d+)$')

        # punt_on_rpf_fail    :1
        p17 = re.compile(r'^punt_on_rpf_fail +:(?P<punt_on_rpf_fail>\d+)$')

        # punt_and_forward    :1
        p18 = re.compile(r'^punt_and_forward +:(?P<punt_and_forward>\d+)$')

        # use_rpfid           :0
        p19 = re.compile(r'^use_rpfid +:(?P<use_rpfid>\d+)$')

        # rpfid               :0
        p20 = re.compile(r'^rpfid +:(?P<rpfid>\d+)$')

        # enable_rpf_check    :1
        p21 = re.compile(r'^enable_rpf_check +:(?P<enable_rpf_check>\d+)$')

        index = 1
        for line in output.splitlines():
            line = line.strip()

            # Mvrf: 3  ( 40::2, ff1e::1 ) Attrs:
            m = p0.match(line)
            if m:
                group = m.groupdict()
                mfib_dict = ret_dict.setdefault("mfib", {}).setdefault(index, {})
                mfib_dict['mvrf'] = int(group['mvrf'])
                mfib_dict['group'] = group['group']
                mfib_dict['source'] = group['source']
                attrs_dict = mfib_dict.setdefault('attrs', {})
                index += 1
                continue

            # Hw Flag                 : InHw
            m = p1.match(line)
            if m:
                attrs_dict['hw_flag'] = m.groupdict()['hw_flag']
                continue

            # Mlist Flags             : None
            m = p2.match(line)
            if m:
                attrs_dict['mlist_flags'] = m.groupdict()['mlist_flags']
                continue

            # Mlist_hndl (Id)         : 0x11889275ea0 ( 0xc823 )
            m = p3.match(line)
            if m:
                attrs_dict['mlist_hndl_id'] = m.groupdict()['mlist_hndl_id']
                continue

            # Mlist Urid              : 0x10000000003238e8
            m = p4.match(line)
            if m:
                attrs_dict['mlist_urid'] = m.groupdict()['mlist_urid']
                continue

            # Fset Urid (Hash)        : 0x300000000031f715 ( 68af2994 )
            m = p5.match(line)
            if m:
                attrs_dict['fset_urid_hash'] = m.groupdict()['fset_urid_hash']
                continue

            # Fset Aux Urid           : 0x0
            m = p5_1.match(line)
            if m:
                attrs_dict['fset_aux_urid'] = m.groupdict()['fset_aux_urid']
                continue

            # RPF Adjacency ID        : 0xf80059d2
            m = p6.match(line)
            if m:
                attrs_dict['rpf_adjacency_id'] = m.groupdict()['rpf_adjacency_id']
                continue

            # CPU Credit              : 0
            m = p7.match(line)
            if m:
                attrs_dict['cpu_credit'] = int(m.groupdict()['cpu_credit'])
                continue

            # Total Packets           : 4643 ( 9 pps approx.)
            m = p8.match(line)
            if m:
                attrs_dict['total_packets'] = int(m.groupdict()['total_packets'])
                attrs_dict['pps_approx'] = int(m.groupdict()['pps_approx'])
                continue

            # OIF Count               : 3
            m = p9.match(line)
            if m:
                attrs_dict['oif_count'] = int(m.groupdict()['oif_count'])
                continue

            # OIF Details:
            m = p10.match(line)
            if m:
                oif_list = attrs_dict.setdefault('oif_details', [])
                continue

            # AdjID          Interface          ParentIf        HwFlag      Flags      IntfType       MsgType
            m=p10_1.match(line)
            if m:
                continue

            # 0xc851         Tu315              --------         ---        F NS
            m = p11.match(line)
            if m:
                oif_list.append({
                    'adjid': m.groupdict()['adjid'],
                    'interface': m.groupdict()['interface'],
                    'flags': m.groupdict()['flags'].strip().split(),
                })
                if '--' not in m.groupdict()['parentif']:
                    oif_list[-1].update({'parentif': m.groupdict()['parentif']})
                if '--' not in m.groupdict()['hwflag']:
                    oif_list[-1].update({'hwflag': m.groupdict()['hwflag']})
                if m.groupdict()['intf_type']:
                    oif_list[-1].update({'intf_type': m.groupdict()['intf_type']})
                if m.groupdict()['msg_type']:
                    oif_list[-1].update({'msg_type': m.groupdict()['msg_type']})
                continue

            # GID                   : 8631
            m = p12.match(line)
            if m:
                attrs_dict['gid'] = int(m.groupdict()['gid'])
                continue

            # MCID OID Asic[0]      : 1346
            m = p13.match(line)
            if m:
                group = m.groupdict()
                asic_dict = attrs_dict.setdefault('asic', {}).setdefault(int(group['asic']), {})            
                asic_dict['mcid_oid_asic'] = int(group['mcid_oid_asic'])
                continue

            # Hardware Info ASIC[0] :
            m = p14.match(line)
            if m:
                group = m.groupdict()
                hw_dict = attrs_dict.setdefault('hw_asic_info', {}).setdefault(int(group['asic_number']), {})            
                continue

            # IP MCID OID         :3272 (cookie:urid:0x30::1b6)
            m = p15.match(line)
            if m:
                group = m.groupdict()
                hw_dict['ip_mcid_oid'] = int(group['ip_mcid_oid'])
                hw_dict['cookie'] = group['cookie']
                continue

            # RPF PORT OID        :1493
            m = p16.match(line)
            if m:
                hw_dict['rpf_port_oid'] = int(m.groupdict()['rpf_port_oid'])
                continue

            # punt_on_rpf_fail    :1
            m = p17.match(line)
            if m:
                hw_dict['punt_on_rpf_fail'] = int(m.groupdict()['punt_on_rpf_fail'])
                continue

            # punt_and_forward    :1
            m = p18.match(line)
            if m:
                hw_dict['punt_and_forward'] = int(m.groupdict()['punt_and_forward'])
                continue

            # use_rpfid           :0
            m = p19.match(line)
            if m:
                hw_dict['use_rpfid'] = int(m.groupdict()['use_rpfid'])
                continue

            # rpfid               :0
            m = p20.match(line)
            if m:
                hw_dict['rpfid'] = int(m.groupdict()['rpfid'])
                continue

            # enable_rpf_check    :1
            m = p21.match(line)
            if m:
                hw_dict['enable_rpf_check'] = int(m.groupdict()['enable_rpf_check'])
                continue

        return ret_dict
