# show_nve.py
#
# Copyright (c) 2023 by Cisco Systems, Inc.
# All rights reserved.
# ===========================================
''' show_nve.py

IOSXE parsers for the following show commands:

    * 'show nve peers'
    * 'show nve peers interface nve {nve}'
    * 'show nve peers peer-ip {peer_ip}'
    * 'show nve peers vni {vni}'
    * 'show nve interface {nve_intf} detail'
    * 'show nve vni'
    * 'show nve vni {vni}'

'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional
from genie.parsergen import oper_fill_tabular


# ====================================================
#  schema for show nve peers
# ====================================================
class ShowNvePeersSchema(MetaParser):
    '''Schema for:

       * 'show nve peers'
       * 'show nve peers interface nve {nve}'
       * 'show nve peers peer-ip {peer_ip}'
       * 'show nve peers vni {vni}'
    '''

    schema = {
        'interface': {
            Any(): {
                Optional('vni'): {
                    Any(): {
                        Optional('peer_ip'): {
                            Any(): {
                                'type': str,
                                'rmac_num_rt': str,
                                'evni': str,
                                'state': str,
                                'flags': str,
                                'uptime': str
                            }
                        }
                    }
                },
            },
        },
    }


# ============================================
# Super Parser for:
#   * 'show nve peers '
#   * 'show nve peers interface nve {nve}'
#   * 'show nve peers peer-ip {peer_ip}'
#   * 'show nve peers vni {vni}'
# ============================================
class ShowNvePeers(ShowNvePeersSchema):
    ''' Parser for the following show commands:

        * 'show nve peers'
        * 'show nve peers interface nve {nve}'
        * 'show nve peers peer-ip {peer_ip}'
        * 'show nve peers vni {vni}'
    '''

    cli_command = ['show nve peers',
                   'show nve peers interface nve {nve}',
                   'show nve peers peer-ip {peer_ip}',
                   'show nve peers vni {vni}']

    def cli(self, nve='', peer_ip='', vni='', output=None):

        if output is None:
            if nve:
                cmd = self.cli_command[1].format(nve=nve)
            elif peer_ip:
                cmd = self.cli_command[2].format(peer_ip=peer_ip)
            elif vni:
                cmd = self.cli_command[3].format(vni=vni)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd)
        else:
            out = output

        res_dict = {}
        # Interface  VNI      Type Peer-IP          RMAC/Num_RTs   eVNI     state flags UP time
        # nve1       3000101  L3CP 20.0.101.2       5c71.0dfe.fb60 3000101    UP  A/M/4 4d21h
        # nve1       3000101  L3CP 30.0.107.78      ac3a.6767.049f 3000101    UP  A/M/4 4d21h
        # nve1       200051   L2CP 20.0.101.2       3              200051     UP   N/A  4d17h
        # nve1       200051   L2CP 20.0.101.3       3              200051     UP   N/A  4d17h
        # nve1       200051   L2CP 30.0.107.78      6              200051     UP   N/A  4d17h
        # nve1       200052   L2CP 20.0.101.2       3              200052     UP   N/A  4d17h
        # nve1       200052   L2CP 20.0.101.3       3              200052     UP   N/A  4d17h
        # nve1       200052   L2CP 30.0.107.78      6              200052     UP   N/A  4d17h

        p1 = re.compile(r'^\s*(?P<nve_interface>[\w\/]+)\s+(?P<vni>[\d]+)\s+'
                        r'(?P<type>(L3CP|L2CP))\s+(?P<peer_ip>[\w\.\:]+)\s+(?P<rmac_num_rt>[\S]+)\s+'
                        r'(?P<evni>[\d]+)\s+(?P<state>(UP|DN|LP|NA|--|DOWN))\s+(?P<flags>[\S]+)\s+(?P<uptime>[\S]+)$')

        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                nve_interface = group['nve_interface']
                vni = group['vni']
                cp_type = group['type']
                peer_ip = group['peer_ip']
                rmac_num_rt = group['rmac_num_rt']
                evni = group['evni']
                state = group['state']
                flags = group['flags']
                uptime = group['uptime']
                intf_dict = res_dict.setdefault('interface', {}).setdefault(nve_interface, {})
                vni_dict = intf_dict.setdefault('vni', {}).setdefault(vni, {})
                peer_dict = vni_dict.setdefault('peer_ip', {}).setdefault(peer_ip, {})
                peer_dict.update({'type': cp_type})
                peer_dict.update({'rmac_num_rt': rmac_num_rt})
                peer_dict.update({'evni': evni})
                peer_dict.update({'state': state})
                peer_dict.update({'flags': flags})
                peer_dict.update({'uptime': uptime})

                continue

        return res_dict


# ====================================================
#  schema for show nve interface {nve_intf} detail
# ====================================================
class ShowNveInterfaceDetailSchema(MetaParser):
    '''Schema for:

    * 'show nve interface {nve_intf} detail'
    '''

    schema = {
        'interface': str,
        'admin_state': str,
        'oper_state': str,
        'encap': str,
        # mcast_encap is optional for backwards compatibility with older
        # version show outputs.
        Optional('mcast_encap'): str,
        'bgp_host_reachability': str,
        'vxlan_dport': int,
        'num_l3vni_cp': int,
        'num_l2vni_cp': int,
        'num_l2vni_dp': int,
        Optional('src_intf'): {
            Any(): {
                'primary_ip': str,
                Optional('secondary_ip'): str,
                'vrf': str,
            }
        },
        Optional('tunnel_intf'): {
            Any(): {
             'counters': {
                 'pkts_in': int,
                 'bytes_in': int,
                 'pkts_out': int,
                 'bytes_out': int
                }
            }
        },
        Optional('tunnel_primary'): str,
        Optional('tunnel_secondary'): str
    }


# ============================================
# Parser for:
# * show nve interface {nve_intf} detail
# ============================================
class ShowNveInterfaceDetail(ShowNveInterfaceDetailSchema):
    ''' Parser for the following show commands:

    * 'show nve interface {nve_intf} detail'
    '''

    cli_command = ['show nve interface {nve_intf} detail']

    # nve_num argument is kept for backwards compatibility with previous
    # version of parser when calling directly.
    def cli(self, nve_intf=None, nve_num=None, output=None):

        if output is None:
            if nve_num and nve_intf is None:
                nve_intf = 'nve {nve_num}'.format(nve_num=nve_num)

            if nve_intf:
                output = self.device.execute(self.cli_command[0].format(nve_intf=nve_intf))
            else:
                return {}

        parsed_dict = {}

        # Interface: nve1, State: Admin Up, Oper Down, Encapsulation: Vxlan,
        # Interface: nve1, State: Admin Up, Oper Down
        p1 = re.compile(r'^Interface:\s+(?P<interface>[a-zA-Z0-9 ]+),'
                        r'\s+State:\s+Admin\s+(?P<admin_state>[\w]+),'
                        r'\s+Oper\s+(?P<oper_state>[\w\s]+)(,'
                        r'\s+Encapsulation:\s+(?P<encap>[\w]+),)?$')

        # Encapsulation: Vxlan IPv4
        # Encapsulation: Vxlan dual stack prefer IPv4
        p2 = re.compile(r'^Encapsulation:\s+(?P<encap>[\w ]+)$')

        # Multicast BUM encapsulation: Vxlan IPv4
        p3 = re.compile(r'^Multicast BUM encapsulation:\s+(?P<encap>[\w ]+)$')

        # BGP host reachability: Enabled, VxLAN dport: 4789
        p4 = re.compile(r'^BGP host reachability:\s+(?P<bgp_host_reachability>[\w]+),'
                        r'\s+VxLAN dport:\s+(?P<vxlan_dport>\d+)$')

        # VNI number: L3CP 30 L2CP 3 L2DP 0
        p5 = re.compile(r'^VNI number:\s+L3CP\s+(?P<num_l3vni_cp>[\d]+)'
                        r'\s+L2CP\s+(?P<num_l2vni_cp>[\d]+)'
                        r'\s+L2DP\s+(?P<num_l2vni_dp>[\d]+)$')

        # source-interface: Loopback2 (primary: 1.1.1.3 vrf: 0)
        # source-interface: Loopback1 (primary: UNKNOWN vrf: 0)
        p6 = re.compile(r'^source-interface:\s+(?P<src_intf>[a-zA-Z0-9]+)\s+'
                        r'\(primary:\s*(?P<primary_ip>UNKNOWN|[0-9a-fA-F\.:]+)\s+'
                        r'vrf:\s*(?P<vrf>[a-zA-Z0-9]+)\)$')

        # source-interface: Loopback1 (primary: ABCD:1::2 1.1.1.2 vrf:0)
        p6_1 = re.compile(r'^source-interface:\s+(?P<src_intf>[a-zA-Z0-9]+)\s+'
                          r'\(primary:\s*(?P<primary_ip>[0-9a-fA-F\.:]+)\s+'
                          r'(?P<secondary_ip>[0-9a-fA-F\.:]+)\s+'
                          r'vrf:\s*(?P<vrf>[a-zA-Z0-9]+)\)$')

        # tunnel interface: Tunnel0
        # tunnel interface: Tunnel1 Tunnel4
        p7 = re.compile(r'^tunnel interface:\s+(?P<tunnel_intf>[a-zA-Z0-9 ]+)$')

        # 1          11          0          0
        p8 = re.compile(r'^(?P<pkts_in>[\d]+)\s+(?P<bytes_in>[\d]+)\s'
                        r'+(?P<pkts_out>[\d]+)\s+(?P<bytes_out>[\d]+)$')

        # Tunnel0 Tunnel4
        p9 = re.compile(r'^(?P<tunnel_primary>[a-zA-Z0-9]+)\s+(?P<tunnel_secondary>[a-zA-Z0-9]+)$')

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # Interface: nve1, State: Admin Up, Oper Down, Encapsulation: Vxlan,
            # Interface: nve1, State: Admin Up, Oper Down
            m = p1.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.update({'interface': group['interface'],
                                    'admin_state': group['admin_state'],
                                    'oper_state': group['oper_state']})
                if 'encap' in group:
                    parsed_dict.update({'encap': group['encap']})
                continue

            # Encapsulation: Vxlan IPv4
            # Encapsulation: Vxlan dual stack prefer IPv4
            m = p2.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.update({'encap': group['encap']})
                continue

            # Multicast BUM encapsulation: Vxlan IPv4
            m = p3.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.update({'mcast_encap': group['encap']})
                continue

            # BGP host reachability: Enabled, VxLAN dport: 4789
            m = p4.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.update({'bgp_host_reachability': group['bgp_host_reachability'],
                                    'vxlan_dport': int(group['vxlan_dport'])})
                continue

            # VNI number: L3CP 0 L2CP 3 L2DP 0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.update({'num_l3vni_cp': int(group['num_l3vni_cp']),
                                    'num_l2vni_cp': int(group['num_l2vni_cp']),
                                    'num_l2vni_dp': int(group['num_l2vni_dp'])})
                continue

            # source-interface: Loopback1 (primary:1.1.1.2 vrf:0)
            # source-interface: Loopback1 (primary: UNKNOWN vrf: 0)
            m = p6.match(line)
            if m:
                group = m.groupdict()
                src_intf = parsed_dict.setdefault('src_intf', {})
                src_intf.update({group['src_intf']: {
                                        'primary_ip': group['primary_ip'],
                                        'vrf': group['vrf']
                                    }
                                 })
                continue

            # source-interface: Loopback1 (primary: ABCD:1::2 1.1.1.2 vrf:0)
            m = p6_1.match(line)
            if m:
                group = m.groupdict()
                src_intf = parsed_dict.setdefault('src_intf', {})
                src_intf.update({group['src_intf']: {
                                       'primary_ip': group['primary_ip'],
                                       'secondary_ip': group['secondary_ip'],
                                       'vrf': group['vrf']
                                    }
                                 })
                continue

            # tunnel interface: Tunnel0
            # tunnel interface: Tunnel1 Tunnel4
            m = p7.match(line)
            if m:
                group = m.groupdict()
                tunnel_intf_dict = parsed_dict.setdefault('tunnel_intf', {})
                tunnel_intf = group['tunnel_intf']
                tunnel_intf_dict.update({tunnel_intf: {}})

                # if there are 2 tunnel interfaces, creating 2 additional keys in main dict:
                m_nested = p9.match(tunnel_intf)
                if m_nested:
                    group_nested = m_nested.groupdict()
                    parsed_dict.update({'tunnel_primary': group_nested['tunnel_primary'],
                                        'tunnel_secondary': group_nested['tunnel_secondary']})
                else:
                    parsed_dict.update({'tunnel_primary': tunnel_intf})

                continue

            #          1          11          0          0
            m = p8.match(line)
            if m:
                group = m.groupdict()
                tunnel_intf_dict.update({tunnel_intf: {
                                            'counters': {
                                                'pkts_in': int(group['pkts_in']),
                                                'bytes_in': int(group['bytes_in']),
                                                'pkts_out': int(group['pkts_out']),
                                                'bytes_out': int(group['bytes_out'])
                                                }
                                            }
                                         })
                continue

        return parsed_dict


# ====================================================
#  schema for show nve vni
# ====================================================
class ShowNveVniSchema(MetaParser):
    """Schema for:
        show nve vni
        show nve vni {vni}"""

    schema = {
        Any(): {
            Any(): {
                'interface': str,
                'vni': str,
                'mcast': str,
                'vni_state': str,
                'mode': str,
                Optional('vlan'): str,
                Optional('bd'): str,
                'cfg': str,
                'vrf': str,
            }
        }
    }


# ====================================================
#  Parser for show nve vni
# ====================================================
class ShowNveVni(ShowNveVniSchema):
    """parser for:
        show nve vni
        show nve vni {vni}"""

    cli_command = ['show nve vni',
                   'show nve vni {vni}']

    def cli(self, vni=None, output=None):

        if output is None:
            cmd = self.cli_command[0]
            if vni:
                cmd = self.cli_command[1].format(vni=vni)
            output = self.device.execute(cmd)

        parsed_dict_vlan = oper_fill_tabular(
            header_fields=["Interface", "VNI", "Multicast-group",
                           "VNI state", "Mode", "VLAN", "cfg", "vrf"],
            label_fields=['interface', 'vni', 'mcast', 'vni_state',
                          'mode', 'vlan', 'cfg', 'vrf'],
            index=[0, 1], device_output=output, device_os='iosxe'
        ).entries

        if parsed_dict_vlan:
            return parsed_dict_vlan

        parsed_dict_bd = oper_fill_tabular(
            header_fields=["Interface", "VNI", "Multicast-group",
                           "VNI state", "Mode", "BD", "cfg", "vrf"],
            label_fields=['interface', 'vni', 'mcast', 'vni_state',
                          'mode', 'bd', 'cfg', 'vrf'],
            index=[0, 1], device_output=output, device_os='iosxe'
        ).entries

        return parsed_dict_bd


# ====================================================
#  schema for show nve vni {vni} detail
# ====================================================
class ShowNveVniDetailSchema(MetaParser):
    '''Schema for:

    * 'show nve vni {vni} detail'
    '''

    schema = {
        'nve_interface': str,
        'vni_id': int,
        Optional('mcast_ip'): str,
        Optional('mcast_ipv6'): str,
        'vni_state': str,
        'vni_type': str,
        'vlan_id': str,
        Optional('l3_vlan_id'): str,
        'vni_origin': str,
        'vni_vrf': str,
        'svi_if_handler': str,
        'vtep_ip': str,
        Optional('vtep_ip_secondary'): str,
        Optional('local_routing'): str,
        Optional('l3_vni'): str,
        Optional('trm_ipv4'): str,
        Optional('trm_ipv6'): str,
        Optional('v4_topo_id'): str,
        Optional('v6_topo_id'): str,
        Optional('svi_mac'): str,
        'uc_input_packets': int,
        'uc_input_bytes': int,
        'uc_output_packets': int,
        'uc_output_bytes': int,
        Optional('mc_input_packets'): int,
        Optional('mc_input_bytes'): int,
        Optional('mc_output_packets'): int,
        Optional('mc_output_bytes'): int
    }


# ============================================
# Parser for show nve vni {vni} detail
# ============================================
class ShowNveVniDetail(ShowNveVniDetailSchema):
    ''' Parser for the following show commands:

    * 'show nve vni {vni} detail'
    '''

    cli_command = 'show nve vni {vni} detail'

    def cli(self, vni, output=None):

        if output is None:
            output = self.device.execute(self.cli_command.format(vni=vni))

        # nve1      20011      227.0.0.11       Down       L2CP  11    CLI red
        p1 = re.compile(r'^(?P<nve_if>nve[0-9]+)\s*(?P<vni_id>[0-9]*)\s*'
                        r'(?P<mcast_ip>(([0-9]{1,3}\.){3}[0-9]{1,3})|(N\/A))?\s(?P<mcast_ipv6>\S+)?\s+'
                        r'(?P<vni_state>\S+\s*\S*)\s+(?P<vni_type>L\S+)'
                        r'\s+(?P<vlan_id>\S+)\s+(?P<vni_origin>\S+)'
                        r'\s+(?P<vni_vrf>\S+)$')

        # nve1       1000420    239.0.4.120 FF04::4:120 \
        #                               BD Down/Re L2CP  N/A   CLI N/A
        # nve1       1000101    239.0.0.101 FF04::1:120 \
        #                               Up         L2CP  101   CLI VRF-101
        p1_1 = re.compile(r'^(?P<nve_if>nve[0-9]+)\s*(?P<vni_id>[0-9]*)\s*'
                          r'(?P<mcast_ip>\S+)\s(?P<mcast_ipv6>\S+)?\s+\\$')

        p1_2 = re.compile(r'^(?P<vni_state>\S+\s*\S*)\s+(?P<vni_type>L\S+)'
                          r'\s+(?P<vlan_id>\S+)\s+(?P<vni_origin>\S+)'
                          r'\s+(?P<vni_vrf>\S+)$')

        # SVI if handler: 0x2F
        p2 = re.compile(r'^(SVI|BDI) if handler:\s+(?P<svi_if>\S+)$')

        # Local VTEP: 1.1.1.2
        p3 = re.compile(r'^Local VTEP:\s+(?P<vtep_ip>\S+)$')

        # Local VTEP: 172.16.255.7 2000:172:16:255::7
        p3_1 = re.compile(r'^Local VTEP:\s+(?P<vtep_ip>\S+)\s+(?P<vtep_ip_secondary>\S+)$')

        # Local routing: Disabled
        p4 = re.compile(r'^Local routing:\s+(?P<local_routing>\S+)$')

        # L3VNI: 30000
        p5 = re.compile(r'^L3VNI:\s+(?P<l3_vni>\d+)$')

        # IPv4 TRM mdt group: N/A
        p6 = re.compile(r'^IPv4 TRM mdt group:\s+(?P<trm_ipv4>\S+)$')

        # IPv6 TRM mdt group: N/A
        p7 = re.compile(r'^IPv6 TRM mdt group:\s+(?P<trm_ipv6>\S+)$')

        # V4TopoID: 0x2
        p8 = re.compile(r'^V4TopoID:\s+(?P<v4_topo_id>\S+)$')

        # V6TopoID: 0x1E000002
        p9 = re.compile(r'^V6TopoID:\s+(?P<v6_topo_id>\S+)$')

        # SVI MAC: 6C8B.D36D.471F
        p10 = re.compile(r'^SVI MAC:\s+(?P<svi_mac>\S+)$')

        # Pkts In   Bytes In   Pkts Out  Bytes Out
        # 0          0          0          0
        p11 = re.compile(r'^(?P<uc_input_packets>\d+)\s+(?P<uc_input_bytes>\d+)'
                         r'\s+(?P<uc_output_packets>\d+)\s+'
                         r'(?P<uc_output_bytes>\d+)$')
        # UcastPkts  UcastBytes McastPkts McastBytes"
        # RX 0          0          0          0
        p12 = re.compile(r'^RX\s*(?P<uc_input_packets>\d+)\s+'
                         r'(?P<uc_input_bytes>\d+)\s+(?P<mc_input_packets>\d+)'
                         r'\s+(?P<mc_input_bytes>\d+)$')
        # TX 0          0          0          0
        p13 = re.compile(r'^TX\s*(?P<uc_output_packets>\d+)\s+'
                         r'(?P<uc_output_bytes>\d+)\s+(?P<mc_output_packets>'
                         r'\d+)\s+(?P<mc_output_bytes>\d+)$')

        # VLAN: 1000
        # BD: 1000
        p14 = re.compile(r'^(VLAN|BD):\s+(?P<vlan_id>\S+)$')

        parsed_dict = {}
        l3vni_found = False
        nve_line_splitted_nextline = False

        for line in output.splitlines():
            line = line.strip()

            if not line:
                continue

            if line == 'Core IRB info:' or line == 'L3CP VNI local VTEP info:':
                l3vni_found = True

            # nve1    20011    227.0.0.11      Down       L2CP  11    CLI red
            m = p1.match(line)
            if m:
                group = m.groupdict(default='')
                parsed_dict.update({'nve_interface': group['nve_if'],
                                    'vni_id': int(group['vni_id']),
                                    'mcast_ip': group['mcast_ip'],
                                    'vni_state': group['vni_state'].strip(),
                                    'vni_type': group['vni_type'],
                                    'vlan_id': group['vlan_id'],
                                    'vni_origin': group['vni_origin'],
                                    'vni_vrf': group['vni_vrf']})

                # if group['mcast_ipv6']:
                if group.get('mcast_ipv6'):
                    parsed_dict.update({'mcast_ipv6': group['mcast_ipv6']})
                continue

            # nve1       1000420    239.0.4.120 FF04::4:120 \
            m = p1_1.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.update({'nve_interface': group['nve_if'],
                                    'vni_id': int(group['vni_id']),
                                    'mcast_ip': group['mcast_ip']})
                if group['mcast_ipv6']:
                    parsed_dict.update({'mcast_ipv6': group['mcast_ipv6']})
                nve_line_splitted_nextline = True
                continue

            # in case nve line is splitted (p1_1 matches), we need to parse remaining line
            #                               BD Down/Re L2CP  N/A   CLI N/A
            # or
            #                               Up         L2CP  101   CLI VRF-101
            if nve_line_splitted_nextline:
                m = p1_2.match(line)
                if m:
                    group = m.groupdict()
                    parsed_dict.update({'vni_state': group['vni_state'].strip(),
                                        'vni_type': group['vni_type'],
                                        'vlan_id': group['vlan_id'],
                                        'vni_origin': group['vni_origin'],
                                        'vni_vrf': group['vni_vrf']})

                    # to avoid matching other lines
                    nve_line_splitted_nextline = False
                    continue

            # SVI if handler: 0x2F
            m = p2.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.update({'svi_if_handler': group['svi_if']})
                continue

            # Local VTEP: 1.1.1.2
            m = p3.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.update({'vtep_ip': group['vtep_ip']})
                continue

            # Local VTEP: 172.16.255.7 2000:172:16:255::7
            m = p3_1.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.update({'vtep_ip': group['vtep_ip'], 'vtep_ip_secondary': group['vtep_ip_secondary']})
                continue

            # Local routing: Disabled
            m = p4.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.update({'local_routing': group['local_routing']})
                continue

            if l3vni_found:
                # L3VNI: 30000
                p5 = re.compile(r'^L3VNI:\s+(?P<l3_vni>\S+)$')
                m = p5.match(line)
                if m:
                    group = m.groupdict()
                    parsed_dict.update({'l3_vni': group['l3_vni']})
                    continue

                # IPv4 TRM mdt group: N/A
                m = p6.match(line)
                if m:
                    group = m.groupdict()
                    parsed_dict.update({'trm_ipv4': group['trm_ipv4']})
                    continue

                # IPv6 TRM mdt group: N/A
                m = p7.match(line)
                if m:
                    group = m.groupdict()
                    parsed_dict.update({'trm_ipv6': group['trm_ipv6']})
                    continue

                # V4TopoID: 0x2
                m = p8.match(line)
                if m:
                    group = m.groupdict()
                    parsed_dict.update({'v4_topo_id': group['v4_topo_id']})
                    continue

                # V6TopoID: 0x1E000002
                m = p9.match(line)
                if m:
                    group = m.groupdict()
                    parsed_dict.update({'v6_topo_id': group['v6_topo_id']})
                    continue

                # SVI MAC: 6C8B.D36D.471F
                m = p10.match(line)
                if m:
                    group = m.groupdict()
                    parsed_dict.update({'svi_mac': group['svi_mac']})
                    continue

                # VLAN: 1000
                # BD: 1000
                m = p14.match(line)
                if m:
                    group = m.groupdict()
                    parsed_dict.update({'l3_vlan_id': group['vlan_id']})
                    continue

            # Pkts In   Bytes In   Pkts Out  Bytes Out
            # 0          0          0          0
            m = p11.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.update({'uc_input_packets': int(group['uc_input_packets']),
                                    'uc_input_bytes': int(group['uc_input_bytes']),
                                    'uc_output_packets': int(group['uc_output_packets']),
                                    'uc_output_bytes': int(group['uc_output_bytes']),
                                    'mc_input_packets': 0,
                                    'mc_input_bytes': 0,
                                    'mc_output_packets': 0,
                                    'mc_output_bytes': 0})
                continue
            # UcastPkts  UcastBytes McastPkts McastBytes"
            # RX 0          0          0          0
            m = p12.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.update({'uc_input_packets': int(group['uc_input_packets']),
                                    'uc_input_bytes': int(group['uc_input_bytes']),
                                    'mc_input_packets': int(group['mc_input_packets']),
                                    'mc_input_bytes': int(group['mc_input_bytes'])})
                continue

            # TX 0          0          0          0
            m = p13.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.update({'uc_output_packets': int(group['uc_output_bytes']),
                                    'uc_output_bytes': int(group['uc_output_bytes']),
                                    'mc_output_packets': int(group['mc_output_packets']),
                                    'mc_output_bytes': int(group['mc_output_bytes'])})
                continue
        return parsed_dict
