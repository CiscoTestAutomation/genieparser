''' show_nve.py

IOSXE parsers for the following show commands:

    * 'show nve peers'
    * 'show nve peers interface nve {nve}'
    * 'show nve peers peer-ip {peer_ip}'
    * 'show nve peers vni {vni}'
    * 'show nve interface nve {nve_num} detail'
    * 'show nve vni'
    * 'show nve vni {vni}'

'''

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional, Or, Schema
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
                            Any (): {
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
                            r'(?P<evni>[\d]+)\s+(?P<state>(UP|DOWN))\s+(?P<flags>[\S]+)\s+(?P<uptime>[\S]+)$')

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
#  schema for show nve interface nve {nve_num} detail
# ====================================================
class ShowNveInterfaceDetailSchema(MetaParser):
    '''Schema for:

    * 'show nve interface nve {nve_num} detail'
    '''

    schema = {
        'interface': str,
        'admin_state': str,
        'oper_state': str,
        'encap': str,
        'bgp_host_reachability': str,
        'vxlan_dport': int,
        'num_l3vni_cp': int,
        'num_l2vni_cp': int,
        'num_l2vni_dp': int,
        Optional('src_intf'): {
            Any(): {
                'primary_ip': str,
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
        }
    }

# ============================================
# Parser for:
# * show nve interface nve {nve_num} detail
# ============================================
class ShowNveInterfaceDetail(ShowNveInterfaceDetailSchema):
    ''' Parser for the following show commands:

    * 'show nve interface nve {nve_num} detail'
    '''

    cli_command = ['show nve interface nve {nve_num} detail']

    def cli(self, nve_num=None, output=None):

        if output is None:
            if nve_num:
                output = self.device.execute(self.cli_command[0].format(nve_num=nve_num))
            else:
                return

        parsed_dict = {}

        # Interface: nve1, State: Admin Up, Oper Down, Encapsulation: Vxlan,
        p1 = re.compile(r'^Interface:\s+(?P<interface>[a-zA-Z0-9 ]+),'
                        r'\s+State:\s+Admin\s+(?P<admin_state>[\w]+),'
                        r'\s+Oper\s+(?P<oper_state>[\w\s]+),'
                        r'\s+Encapsulation:\s+(?P<encap>[\w]+),$')

        # BGP host reachability: Enabled, VxLAN dport: 4789
        p2 = re.compile(r'^BGP host reachability:\s+(?P<bgp_host_reachability>[\w]+),'
                        r'\s+VxLAN dport:\s+(?P<vxlan_dport>[\d]+)$')

        # VNI number: L3CP 30 L2CP 3 L2DP 0
        p3 = re.compile(r'^VNI number:\s+L3CP\s+(?P<num_l3vni_cp>[\d]+)'
                        r'\s+L2CP\s+(?P<num_l2vni_cp>[\d]+)'
                        r'\s+L2DP\s+(?P<num_l2vni_dp>[\d]+)$')

        # source-interface: Loopback1 (primary:1.1.1.2 vrf:0)
        p4 = re.compile(r'^source-interface:\s+(?P<src_intf>[a-zA-Z0-9 ]+)'
                        r'\(primary:(?P<primary_ip>[0-9a-fA-F\.:]+)\s'
                        r'+vrf:(?P<vrf>[a-zA-Z0-9 ]+)\)$')

        # tunnel interface: Tunnel0
        p5 = re.compile(r'^tunnel interface:\s+(?P<tunnel_intf>[a-zA-Z0-9 ]+)$')

        # 1          11          0          0
        p6 = re.compile(r'^(?P<pkts_in>[\d]+)\s+(?P<bytes_in>[\d]+)\s'
                        r'+(?P<pkts_out>[\d]+)\s+(?P<bytes_out>[\d]+)$')

        for line in output.splitlines():
            line = line.strip()
            if not line:
                continue

            # Interface: nve1, State: Admin Up, Oper Down, Encapsulation: Vxlan,
            m = p1.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.update({'interface': group['interface'],
                                    'admin_state': group['admin_state'],
                                    'oper_state': group['oper_state'],
                                    'encap': group['encap']})
                continue

            # BGP host reachability: Enabled, VxLAN dport: 4789
            m = p2.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.update({'bgp_host_reachability': group['bgp_host_reachability'],
                                    'vxlan_dport': int(group['vxlan_dport'])})
                continue

            # VNI number: L3CP 0 L2CP 3 L2DP 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                parsed_dict.update({'num_l3vni_cp': int(group['num_l3vni_cp']),
                                    'num_l2vni_cp': int(group['num_l2vni_cp']),
                                    'num_l2vni_dp': int(group['num_l2vni_dp'])})
                continue

            # source-interface: Loopback1 (primary:1.1.1.2 vrf:0)
            m = p4.match(line)
            if m:
                group = m.groupdict()
                src_intf = parsed_dict.setdefault('src_intf', {})
                src_intf.update({group['src_intf'] : {
                                        'primary_ip': group['primary_ip'],
                                        'vrf': group['vrf']
                                    }
                                 })
                continue

            # tunnel interface: Tunnel0
            m = p5.match(line)
            if m:
                group = m.groupdict()
                tunnel_intf_dict = parsed_dict.setdefault('tunnel_intf', {})
                tunnel_intf = group['tunnel_intf']
                tunnel_intf_dict.update({tunnel_intf : {}})
                continue

            #          1          11          0          0
            m = p6.match(line)
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

    schema ={
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

        if parsed_dict_vlan :
            return parsed_dict_vlan

        parsed_dict_bd = oper_fill_tabular(
            header_fields=["Interface", "VNI", "Multicast-group",
                           "VNI state", "Mode", "BD", "cfg", "vrf"],
            label_fields=['interface', 'vni', 'mcast', 'vni_state',
                          'mode', 'bd', 'cfg', 'vrf'],
            index=[0, 1], device_output=output, device_os='iosxe'
        ).entries

        return parsed_dict_bd
