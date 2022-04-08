"""show_vxlan.py

NXOS parser for the following show commands:
    * show nve peers
    * show nve interface <nve> detail
    * show nve ethernet-segment
    * show nve vni
    * show nve vni summary
    * show nve multisite dci-links
    * show nve multisite fabric-links
    * show l2route fl all
    * show l2route evpn ethernet-segment all
    * show l2route topology detail
    * show l2route mac all detail
    * show l2route mac-ip all detail
    * show l2route summary
    * show nve vni ingress-replication
    * show l2route evpn mac-ip all
    * show l2route evpn mac-ip evi <evi>
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

from genie.libs.parser.utils.common import Common


class ShowL2routeEvpnImetAllDetailSchema(MetaParser):
    schema = {
        'vni': {
            Any(): {
                'ip': {
                    Any(): {
                        'topo_id': int,
                        'vni': int,
                        'prod_type': str,
                        'ip_addr': str,
                        'eth_tag_id': int,
                        'pmsi_flags': int,
                        'flags': str,
                        'type': int,
                        'vni_label': int,
                        'tunnel_id': str,
                        'client_nfn': int,
                    }
                }
            }
        }
    }

class ShowL2routeEvpnImetAllDetail(ShowL2routeEvpnImetAllDetailSchema):

    """Parser for show l2route evpn imet all detail """

    cli_command = 'show l2route evpn imet all detail'

    def cli(self, output=None):
        # excute command to get output
        out = output if output else self.device.execute(self.cli_command)

        # Topology ID  VNI         Prod  IP Addr                                 Eth Tag PMSI-Flags Flags   Type Label(VNI)  Tunnel ID                               NFN Bitmap
        # -----------  ----------- ----- --------------------------------------- ------- ---------- ------- ---- ----------- --------------------------------------- ----------
        # 201          20001       BGP   2001:db8:646:a2bb:0:abcd:1234:3                  0       0          -       6    20001        2001:db8:646:a2bb:0:abcd:1234:3                  32
        # 201          20001       BGP   2001:db8:646:a2bb:0:abcd:5678:1                  0       0          -       6    20001        2001:db8:646:a2bb:0:abcd:5678:1                  32


        p1 = re.compile(r'^(?P<topo_id>[\d]+) + (?P<vni>[\d]+)'
                         ' + (?P<prod_type>[\w]+) * (?P<ip_addr>[\w\:]+)'
                         ' + (?P<eth_tag_id>[\d]+) + + (?P<pmsi_flags>[\d]+)'
                         ' + (?P<flags>[\w-]) + (?P<type>[\d]+) + (?P<vni_label>[\d]+)'
                         ' + (?P<tunnel_id>[\w\:]+) + (?P<client_nfn>[\d]+)$')

        result_dict = {}

        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                vni = int(group['vni'])
                ip = group['ip_addr']
                vni_dict = result_dict.setdefault('vni', {}).\
                            setdefault(vni, {}).\
                            setdefault('ip', {}).\
                            setdefault(ip, {})

                vni_dict['topo_id'] = int(group['topo_id'])
                vni_dict['vni'] = vni
                vni_dict['prod_type'] = group['prod_type']
                vni_dict['ip_addr'] = ip
                vni_dict['eth_tag_id'] = int(group['eth_tag_id'])
                vni_dict['pmsi_flags'] = int(group['pmsi_flags'])
                vni_dict['flags'] = group['flags']
                vni_dict['type'] = int(group['type'])
                vni_dict['vni_label'] = int(group['vni_label'])
                vni_dict['tunnel_id'] = group['tunnel_id']
                vni_dict['client_nfn'] = int(group['client_nfn'])
                continue

        return result_dict



# ====================================================
#  schema for show nve peers
# ====================================================
class ShowNvePeersSchema(MetaParser):
    """Schema for:
        show nve peers"""

    schema = {
        Any(): {
            'nve_name': str,
            'peer_ip': {
                Any(): {
                    'peer_state': str,
                    'learn_type': str,
                    'uptime': str,
                    'router_mac': str,
                },
            },
        },
    }


# ====================================================
#  parser for show nve peers
# ====================================================
class ShowNvePeers(ShowNvePeersSchema):
    """Parser for :
       show nve peers"""

    cli_command = 'show nve peers'
    exclude = [
        'uptime']

    def cli(self, output=None):
        # excute command to get output
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        result_dict = {}
        # Interface Peer-IP          State LearnType Uptime   Router-Mac
        # nve1      192.168.16.1      Up    CP        01:15:09 n/a
        # nve1      192.168.106.1        Up    CP        00:03:05 5e00.00ff.0209
        # nve1      2001:db8:646:a2bb:0:abcd:1234:3                  Up    CP        21:47:20 5254.00ff.3162
        # nve1      2001:db8:646:a2bb:0:abcd:1234:5                  Up    CP        21:47:20 5254.00ff.3a82
        # nve1      172.31.201.40   Down  CP        0.000000 n/a

        p1 = re.compile(r'^\s*(?P<nve_name>[\w\/]+) +(?P<peer_ip>[\w\.\:]+) +(?P<peer_state>[\w]+)'
                        ' +(?P<learn_type>[\w]+) +(?P<uptime>[\w\:\.]+) +(?P<router_mac>[\w\.\/]+)$')

        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                nve_name = group.pop('nve_name')
                peer_ip = group.pop('peer_ip')
                nve_dict = result_dict.setdefault(nve_name,{})
                nve_dict.update({'nve_name': nve_name})

                peer_dict = nve_dict.setdefault('peer_ip',{}).setdefault(peer_ip,{})

                peer_dict.update({'learn_type': group.pop('learn_type')})
                peer_dict.update({'uptime': group.pop('uptime')})
                peer_dict.update({'router_mac': group.pop('router_mac')})
                peer_dict.update({'peer_state': group.pop('peer_state').lower()})

                continue

        return result_dict

# ====================================================
#  schema for show nve vni summary
# ====================================================
class ShowNveVniSummarySchema(MetaParser):
    """Schema for:
        show nve vni summary"""

    schema = {
        'vni': {
            'summary': {
                'cp_vni_count': int,
                'cp_vni_up': int,
                'cp_vni_down': int,
                'dp_vni_count': int,
                'dp_vni_up': int,
                'dp_vni_down': int,
            },
        },
    }
# ====================================================
#  parser for show nve vni summary
# ====================================================
class ShowNveVniSummary(ShowNveVniSummarySchema):
    """Parser for :
       show nve vni summary"""

    cli_command = 'show nve vni summary'

    def cli(self, output=None):
        # excute command to get output
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        result_dict = {}
        # Total CP VNIs: 21    [Up: 21, Down: 0]
        # Total DP VNIs: 0    [Up: 0, Down: 0]
        p1 = re.compile(
            r'^\s*Total +CP +VNIs: +(?P<cp_vni_count>[\d]+) +\[Up: +(?P<cp_vni_up>[\d]+), +Down: +(?P<cp_vni_down>[\d]+)\]$')
        p2 = re.compile(
            r'^\s*Total +DP +VNIs: +(?P<dp_vni_count>[\d]+) +\[Up: +(?P<dp_vni_up>[\d]+), +Down: +(?P<dp_vni_down>[\d]+)\]$')
        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                vni_dict = result_dict.setdefault('vni',{}).setdefault('summary',{})
                vni_dict.update({k:int(v) for k,v in group.items()})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                vni_dict.update({k: int(v) for k, v in group.items()})
                continue

        return result_dict

# ====================================================
#  schema for show nve vni
# ====================================================
class ShowNveVniSchema(MetaParser):
    """Schema for:
        show nve vni"""

    schema ={
        Any(): {
            'vni': {
                Any(): {
                    'vni': int,
                    'mcast': str,
                    'vni_state': str,
                    'mode': str,
                    'type': str,
                    'flags': str,
                }
            }
        }
    }

# ====================================================
#  Parser for show nve vni
# ====================================================
class ShowNveVni(ShowNveVniSchema):
    """parser for:
        show nve vni"""

    cli_command = 'show nve vni'

    def cli(self, output=None):
        # excute command to get output
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        result_dict = {}

        # Interface VNI      Multicast-group   State Mode Type [BD/VRF]      Flags
        #  --------- -------- ----------------- ----- ---- ------------------ -----
        # nve1      5001     234.1.1.1         Up    CP   L2 [1001]
        # nve1      5001     192.168.0.1         Up    CP   L2 [1001]          SA MS-IR
        p1 = re.compile(r'^(?P<nve_name>[\w\/]+) +(?P<vni>[\d]+) +(?P<mcast>[\w\.\/]+) +'
                        r'(?P<vni_state>[\w]+) +(?P<mode>[\w]+) +(?P<type>\w+ +\[[\w\-]+\])'
                        r'(?: +(?P<flags>[\w\-\s]+))?$')
        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                nve_name = group.pop('nve_name')
                vni = int(group.pop('vni'))
                nve_dict = result_dict.setdefault(nve_name,{}).setdefault('vni',{}).setdefault(vni,{})
                nve_dict.update({'vni': vni})
                nve_dict.update({'mcast': group.pop('mcast').lower()})
                nve_dict.update({'vni_state': group.pop('vni_state').lower()})
                nve_dict.update({'mode': group.pop('mode')})
                nve_dict.update({'type': group.pop('type')})
                if group.get('flags'):
                    nve_dict.update({'flags': group.pop('flags')})
                else:
                    nve_dict.update({'flags': ''})

                continue

        return result_dict

# ====================================================
#  schema for show interface | i nve
# ====================================================
class ShowNveInterfaceSchema(MetaParser):
    """Schema for:
        show nve interface | i nve"""

    schema = {
        'nves':
            {Any():
                 {'nve_name': str,
                  'nve_state': str,
                 },
             },
    }
#=======================================
#  show interface | i nve
#=======================================
class ShowNveInterface(ShowNveInterfaceSchema):
    """Parser for show interface | i nve"""

    cli_command = 'show interface | i nve'

    def cli(self, output=None):
        # excute command to get output
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Init vars
        result_dict = {}
        # nve1 is down (other)
        p1 = re.compile(r'^\s*nve(?P<nve>(\d+)) +is +(?P<nve_state>[\w]+)( +(?P<other>[\w\(\)]+))?$')

        for line in out.splitlines():
            line = line.rstrip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                nve_name = "{}{}".format('nve',group.pop('nve'))
                nve_dict = result_dict.setdefault('nves', {}).setdefault(nve_name,{})
                nve_dict.update({'nve_name': nve_name})
                nve_dict.update({'nve_state': group.pop('nve_state').lower()})
                continue
        return result_dict
# ====================================================
#  schema for show nve interface <nve> detail
# ====================================================
class ShowNveInterfaceDetailSchema(MetaParser):
    """Schema for:
        show nve interface <nve> detail"""

    schema ={
        Any(): {
            'nve_name': str,
            Optional('if_state'): str,
            Optional('encap_type'): str,
            Optional('vpc_capability'): str,
            Optional('local_rmac'): str,
            Optional('host_reach_mode'): str,
            Optional('source_if'): str,
            Optional('primary_ip'): str,
            Optional('anycast_if'): str,
            Optional('secondary_ip'): str,
            Optional('src_if_state'): str,
            Optional('ir_cap_mode'): str,
            Optional('adv_vmac'): bool,
            Optional('nve_flags'): str,
            Optional('nve_if_handle'): int,
            Optional('src_if_holddown_tm'): int,
            Optional('src_if_holdup_tm'): int,
            Optional('src_if_holddown_left'): int,
            Optional('multisite_convergence_time'): int,
            Optional('multisite_convergence_time_left'): int,
            Optional('vip_rmac'): str,
            Optional('vip_rmac_ro'): str,
            Optional('sm_state'): str,
            Optional('peer_forwarding_mode'): bool,
            Optional('dwn_strm_vni_cfg_mode'): str,
            Optional('src_intf_last_reinit_notify_type'): str,
            Optional('mcast_src_intf_last_reinit_notify_type'): str,
            Optional('multi_src_intf_last_reinit_notify_type'): str,
            Optional('multisite_bgw_if'): str,
            Optional('multisite_bgw_if_ip'): str,
            Optional('multisite_bgw_if_admin_state'): str,
            Optional('multisite_bgw_if_oper_state'): str,
            Optional('multisite_bgw_if_oper_state_down_reason'): str,
            Optional('multisite_dci_advertise_pip'): bool,
        }
    }

# ====================================================
#  schema for show nve interface <nve> detail
# ====================================================
class ShowNveInterfaceDetail(ShowNveInterfaceDetailSchema):
    """parser for:
        show nve interface <nve> detail"""
    cli_command = 'show nve interface {interface} detail'
    def cli(self, interface="", output=None):
        nve_list = []

        if interface:
            nve_list.append(interface)
        elif output:
            # Output is given, do not attempt discovery of interfaces from a
            # different command.
            # Add a placeholder to the nve_list just to perform one iteration of
            # the parsing loop.
            nve_list.append('placeholder')
        elif not interface and not output:
            # No interface given, and no output given, find nve interfaces
            cmd1 = 'show interface | i nve'
            out1 = self.device.execute(cmd1)
            # Init vars

            # nve1 is down (other)
            p1 = re.compile(r'^\s*nve(?P<nve>(\d+)) +is +(?P<nve_state>[\w]+)( +(?P<other>[\w\(\)]+))?$')

            for line in out1.splitlines():
                line = line.rstrip()

                m = p1.match(line)
                if m:
                    group = m.groupdict()
                    nve_name = '{}{}'.format('nve', group.get('nve'))
                    nve_list.append(nve_name)
                    continue

        result_dict = {}
        # Interface: nve1, State: Up, encapsulation: VXLAN
        p1 = re.compile(r'^\s*Interface: +(?P<nve_name>[\w\/]+), +State: +(?P<state>[\w]+),'
                        ' +encapsulation: +(?P<encapsulation>[\w]+)$')
        p2 = re.compile(r'^\s*VPC Capability: +(?P<vpc_capability>[\w\s\-\[\]]+)$')
        p3 = re.compile(r'^\s*Local Router MAC: +(?P<local_router_mac>[\w\.]+)$')
        p4 = re.compile(r'^\s*Host Learning Mode: +(?P<host_learning_mode>[\w\-]+)$')
        p5 = re.compile(r'^\s*Source-Interface: +(?P<source_if>[\w\/]+)'
                        ' +\(primary: +(?P<primary_ip>[\w\.]+), +secondary: +(?P<secondary_ip>[\w\.]+)\)$')

        # Source-Interface: loopback1 (primary: 2001:db8:646:a2bb:0:abcd:1234:4)
        # Anycast-Interface: loopback2 (secondary: 2001:db8:646:a2bb:0:abcd:5678:5)
        p5_1 = re.compile(r'^\s*Source-Interface: +(?P<source_if>[\w\/]+) +\(primary: +(?P<primary_ip>[\w\.\:]+)\)')
        p5_2 = re.compile(r'^\s*Anycast-Interface: +(?P<anycast_if>[\w\/]+) +\(secondary: +(?P<secondary_ip>[\w\.\:]+)\)')


        p6 = re.compile(r'^\s*Source +Interface +State: +(?P<source_state>[\w]+)$')
        p7 = re.compile(r'^\s*IR +Capability +Mode: +(?P<mode>[\w]+)$')
        p8 = re.compile(r'^\s*Virtual +RMAC +Advertisement: +(?P<adv_vmac>[\w]+)$')
        p9 = re.compile(r'^\s*NVE +Flags:( +(?P<flags>[\w]+))?$')
        p10 = re.compile(r'^\s*Interface +Handle: +(?P<intf_handle>[\w]+)$')
        p11 = re.compile(r'^\s*Source +Interface +hold-down-time: +(?P<hold_down_time>[\d]+)$')
        p12 = re.compile(r'^\s*Source +Interface +hold-up-time: +(?P<hold_up_time>[\d]+)$')
        p13 = re.compile(r'^\s*Remaining +hold-down +time: +(?P<hold_time_left>[\d]+) +seconds$')
        # Virtual Router MAC: N/A
        p14 = re.compile(r'^\s*Virtual +Router +MAC: +(?P<v_router_mac>\S+)$')
        p15 = re.compile(r'^\s*Virtual +Router +MAC +Re\-origination: +(?P<v_router_mac_re>[\w\.]+)$')
        p16 = re.compile(r'^\s*Interface +state: +(?P<intf_state>[\w\-]+)$')
        p17 = re.compile(r'^\s*unknown-peer-forwarding: +(?P<peer_forwarding>[\w]+)$')
        p18 = re.compile(r'^\s*down-stream +vni +config +mode: +(?P<vni_config_mode>[\w\/]+)$')
        p19 = re.compile(r'^\s*Nve +Src +node +last +notif +sent: +(?P<last_notif_sent>[\w\-]+)$')
        p20 = re.compile(r'^\s*Nve +Mcast +Src +node +last +notif +sent: +(?P<last_notif_sent>[\w\-]+)$')
        p20_1 = re.compile(r'^\s*Nve +MultiSite +Src +node +last +notif +sent: +(?P<notif_sent>[\w\-]+)$')
        p21 = re.compile(
            r'^\s*Multisite +bgw\-if: +(?P<multisite_bgw_if>[\w\/\-]+) +\(ip: +(?P<multisite_bgw_if_ip>[\w\.]+),'
            ' +admin: +(?P<multisite_bgw_if_admin_state>[\w]+), +oper: +(?P<multisite_bgw_if_oper_state>[\w]+)\)$')
        p22 = re.compile(r'^\s*Multisite +bgw\-if +oper +down +reason: +(?P<reason>[\w\.\s]+)$')
        # Multi-Site delay-restore time: 180 seconds
        p23 = re.compile(r'^\s*Multi(-S|s)ite +delay\-restore +time: +(?P<multisite_convergence_time>\d+) +seconds$')
        # Multi-Site delay-restore time left: 0 seconds
        p24 = re.compile(
            r'^\s*Multi(-S|s)ite +bgw\-if +oper +down +reason: +(?P<multisite_convergence_time_left>\d+) +seconds$')
        p25 = re.compile(r'Multisite +delay-restore +time +left: +(?P<multisite_convergence_time_left>\d+) +seconds$')
        # Multisite dci-advertise-pip configured: True
        p26 = re.compile(r'Multisite +dci-advertise-pip +configured: +(?P<multisite_dci_advertise_pip>\S+)')

        for nve in nve_list:
            if not output:
                out = self.device.execute(self.cli_command.format(interface=nve))
            else:
                out = output
            for line in out.splitlines():
                if line:
                    line = line.rstrip()
                else:
                    continue

                m = p1.match(line)
                if m:
                    group = m.groupdict()
                    nve_name = group.pop('nve_name')
                    nve_dict = result_dict.setdefault(nve_name , {})
                    nve_name = m.groupdict()['nve_name']
                    nve_dict.update({'nve_name': nve_name})
                    nve_dict.update({'if_state': group.pop('state').lower()})
                    nve_dict.update({'encap_type': group.pop('encapsulation').lower()})
                    continue

                # VPC Capability: VPC-VIP-Only [notified]
                m = p2.match(line)
                if m:
                    group = m.groupdict()
                    nve_dict.update({'vpc_capability': group.pop('vpc_capability').lower()})
                    continue

                #  Local Router MAC: 5e00.00ff.050c
                m = p3.match(line)
                if m:
                    group = m.groupdict()
                    nve_dict.update({'local_rmac': group.pop('local_router_mac')})
                    continue

                #  Host Learning Mode: Control-Plane
                m = p4.match(line)
                if m:
                    group = m.groupdict()
                    nve_dict.update({'host_reach_mode': group.pop('host_learning_mode').lower()})
                    continue

                #  Source-Interface: loopback1 (primary: 192.168.4.11, secondary: 192.168.196.22)
                m = p5.match(line)
                m_1 = p5_1.match(line)
                m_2 = p5_2.match(line)
                if m:
                    group = m.groupdict()
                    nve_dict.update({k:v for k,v in group.items()})
                if m_1:
                    group1 = m_1.groupdict()
                    nve_dict.update({'source_if': group1.pop('source_if')})
                    nve_dict.update({'primary_ip': group1.pop('primary_ip')})
                    continue
                if m_2:
                    group2 = m_2.groupdict()
                    nve_dict.update({'anycast_if': group2.pop('anycast_if')})
                    nve_dict.update({'secondary_ip': group2.pop('secondary_ip')})
                    continue

                m = p5.match(line)
                if m:
                    group = m.groupdict()
                    nve_dict.update({k:v for k,v in group.items()})
                    continue

                #  Source Interface State: Up
                m = p6.match(line)
                if m:
                    group = m.groupdict()
                    nve_dict.update({'src_if_state': group.pop('source_state').lower()})
                    continue

                #  IR Capability Mode: No
                m = p7.match(line)
                if m:
                    group = m.groupdict()
                    nve_dict.update({'ir_cap_mode': group.pop('mode').lower()})
                    continue

                #  Virtual RMAC Advertisement: Yes
                m = p8.match(line)
                if m:
                    group = m.groupdict()
                    nve_dict.update({'adv_vmac': True if group.pop('adv_vmac').lower() == 'yes' else False})
                    continue

                #  NVE Flags:
                m = p9.match(line)
                if m:
                    group = m.groupdict()
                    if group.get("flags"):
                        nve_dict.update({'nve_flags': group.pop('flags')})
                    else:
                        nve_dict.update({'nve_flags': ""})
                    continue

                #  Interface Handle: 0x49000001
                m = p10.match(line)
                if m:
                    group = m.groupdict()
                    nve_dict.update({'nve_if_handle': int(group.pop('intf_handle'),0)})
                    continue

                #  Source Interface hold-down-time: 180
                m = p11.match(line)
                if m:
                    group = m.groupdict()
                    nve_dict.update({'src_if_holddown_tm': int(group.pop('hold_down_time'))})
                    continue

                #  Source Interface hold-up-time: 30
                m = p12.match(line)
                if m:
                    group = m.groupdict()
                    nve_dict.update({'src_if_holdup_tm': int(group.pop('hold_up_time'))})
                    continue

                #  Remaining hold-down time: 0 seconds
                m = p13.match(line)
                if m:
                    group = m.groupdict()
                    nve_dict.update({'src_if_holddown_left': int(group.pop('hold_time_left'))})
                    continue

                #  Virtual Router MAC: 0200.c9ff.1722
                m = p14.match(line)
                if m:
                    group = m.groupdict()
                    nve_dict.update({'vip_rmac': group.pop('v_router_mac')})
                    continue

                #  Virtual Router MAC Re-origination: 0200.65ff.caca
                m = p15.match(line)
                if m:
                    group = m.groupdict()
                    nve_dict.update({'vip_rmac_ro': group.pop('v_router_mac_re')})
                    continue

                #  Interface state: nve-intf-add-complete
                m = p16.match(line)
                if m:
                    group = m.groupdict()
                    nve_dict.update({'sm_state': group.pop('intf_state')})
                    continue

                #  unknown-peer-forwarding: disable
                m = p17.match(line)
                if m:
                    group = m.groupdict()
                    nve_dict.update({'peer_forwarding_mode': False if group.pop('peer_forwarding') == 'disable' else True})
                    continue

                #  down-stream vni config mode: n/a
                m = p18.match(line)
                if m:
                    group = m.groupdict()
                    nve_dict.update({'dwn_strm_vni_cfg_mode': group.pop('vni_config_mode')})
                    continue

                # Nve Src node last notif sent: Port-up
                m = p19.match(line)
                if m:
                    group = m.groupdict()
                    nve_dict.update({'src_intf_last_reinit_notify_type': group.pop('last_notif_sent').lower()})
                    continue

                # Nve Mcast Src node last notif sent: None
                m = p20.match(line)
                if m:
                    group = m.groupdict()
                    nve_dict.update({'mcast_src_intf_last_reinit_notify_type': group.pop('last_notif_sent').lower()})
                    continue

                # Nve MultiSite Src node last notif sent: None
                m = p20_1.match(line)
                if m:
                    group = m.groupdict()
                    nve_dict.update({'multi_src_intf_last_reinit_notify_type': group.pop('notif_sent').lower()})
                    continue

                # Multisite bgw-if: loopback2 (ip: 10.4.101.101, admin: Down, oper: Down)
                m = p21.match(line)
                if m:
                    group = m.groupdict()
                    nve_dict.update({'multisite_bgw_if': group.pop('multisite_bgw_if')})
                    nve_dict.update({'multisite_bgw_if_ip': group.pop('multisite_bgw_if_ip')})
                    nve_dict.update({'multisite_bgw_if_admin_state': group.pop('multisite_bgw_if_admin_state').lower()})
                    nve_dict.update({'multisite_bgw_if_oper_state': group.pop('multisite_bgw_if_oper_state').lower()})
                    continue

                # Multisite bgw-if oper down reason: NVE not up.
                m = p22.match(line)
                if m:
                    group = m.groupdict()
                    nve_dict.update({'multisite_bgw_if_oper_state_down_reason': group.pop('reason')})
                    continue

                m = p23.match(line)
                if m:
                    group = m.groupdict()
                    nve_dict.update({'multisite_convergence_time': int(group.pop('multisite_convergence_time'))})
                    continue

                m = p24.match(line)
                if m:
                    group = m.groupdict()
                    nve_dict.update({'multisite_convergence_time_left': int(group.pop('multisite_convergence_time_left'))})
                    continue

                m = p25.match(line)
                if m:
                    group = m.groupdict()
                    nve_dict.update({'multisite_convergence_time_left': int(group.pop('multisite_convergence_time_left'))})
                    continue
                # Multisite dci-advertise-pip configured: True
                m = p26.match(line)
                if m:
                    group = m.groupdict()
                    nve_dict.update({'multisite_dci_advertise_pip': group.pop('multisite_dci_advertise_pip')=="True"})
                    continue

        return result_dict


# ====================================================
#  schema for show nve multisite dci-links
# ====================================================
class ShowNveMultisiteDciLinksSchema(MetaParser):
    """Schema for:
        show nve multisite dci-links"""

    schema ={
        'multisite': {
            Optional('dci_links'): {
                Any():{
                    'if_name': str,
                    'if_state': str
                },
            },
        },
    }

# ====================================================
#  Parser for show nve multisite dci-link
# ====================================================
class ShowNveMultisiteDciLinks(ShowNveMultisiteDciLinksSchema):
    """parser for:
        show nve multisite dci-links"""

    cli_command = 'show nve multisite dci-links'

    def cli(self, output=None):
        # excute command to get output
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        result_dict = {}

        # Interface      State
        # ---------      -----
        # Ethernet1/53   Up
        # port-channel11 Up
        p1 = re.compile(r'^\s*(?P<if_name>(?!Interface)[\S]+) +(?P<if_state>[\w]+)$')
        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                if_name = group.pop('if_name')
                if_state = group.pop('if_state')
                if_dict = result_dict.setdefault('multisite', {}).setdefault('dci_links', {}).setdefault(if_name, {})

                if_dict.update({'if_name': if_name})
                if_dict.update({'if_state': if_state.lower()})
                continue

        return result_dict

# ====================================================
#  schema for show nve multisite fabric-links
# ====================================================
class ShowNveMultisiteFabricLinksSchema(MetaParser):
    """Schema for:
        show nve multisite fabric-links"""

    schema = {
        'multisite': {
            'fabric_links': {
                Any(): {
                    'if_name': str,
                    'if_state': str
                },
            },
        },
    }

# ====================================================
#  Parser for show nve multisite fabric-link
# ====================================================
class ShowNveMultisiteFabricLinks(ShowNveMultisiteFabricLinksSchema):
    """parser for:
        show nve multisite fabric-links"""

    cli_command = 'show nve multisite fabric-links'

    def cli(self, output=None):
        # excute command to get output
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Interface      State
        # ---------      -----
        # Ethernet1/53   Up
        # port-channel11 Up
        p1 = re.compile(r'^\s*(?P<if_name>(?!Interface)[\S]+) +(?P<if_state>[\w]+)$')

        result_dict = {}
        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                if_name = group.pop('if_name')
                if_state = group.pop('if_state')
                if_dict = result_dict.setdefault('multisite',{}).setdefault('fabric_links',{}).setdefault(if_name,{})

                if_dict.update({'if_name': if_name})
                if_dict.update({'if_state': if_state.lower()})
                continue

        return result_dict


# ==================================================
#   Schema for show nve ethernet-segment
# ==================================================
class ShowNveEthernetSegmentSchema(MetaParser):
    """Schema for:
          show nve ethernet-segment"""

    schema ={
        'nve':{
            Any():{
                'ethernet_segment': {
                    'esi': {
                        Any(): {
                            'esi': str,
                            'if_name': str,
                            'es_state': str,
                            'po_state': str,
                            'nve_if_name': str,
                            'nve_state': str,
                            'host_reach_mode': str,
                            'active_vlans': str,
                            Optional('df_vlans'): str,
                            'active_vnis': str,
                            'cc_failed_vlans': str,
                            'cc_timer_left': str,
                            'num_es_mem': int,
                            Optional('local_ordinal'): int,
                            'df_timer_st': str,
                            'config_status': str,
                            Optional('df_list'): str,
                            'es_rt_added': bool,
                            'ead_rt_added': bool,
                            'ead_evi_rt_timer_age': str,
                        },
                    },
                },
            },
        }
    }

# ==================================================
#   Schema for show nve ethernet-segment
# ==================================================
class ShowNveEthernetSegment(ShowNveEthernetSegmentSchema):
    """parser for:
        show nve ethernet-segment"""

    cli_command = 'show nve ethernet-segment'

    def cli(self, output=None):
        # excute command to get output
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        df_vlans = ""
        result_dict = {}

        # ESI: 0300.00ff.0001.2c00.0309
        #   Parent interface: nve1
        #   ES State: Up
        #   Port-channel state: N/A
        #   NVE Interface: nve1
        #   NVE State: Up
        #  Host Learning Mode: control-plane
        #   Active Vlans: 1,101-105,1001-1100,2001-2100,3001-3005
        #  DF Vlans: 102,104,1002,1004,1006,1008,1010,1012,1014,1016,1018,1020,1022,1024
        # ,1026,1028,1030,1032,1034,1036,1038,1040,1042,1044,1046,1048,1050,1052,1054,1056
        #    Active VNIs: 501001-501100,502001-502100,503001-503005,600101-600105
        #   CC failed for VLANs:
        #   VLAN CC timer: 0
        #   Number of ES members: 2
        #  My ordinal: 0
        #  DF timer start time: 00:00:00
        #  Config State: N/A
        #  DF List: 192.168.111.55 192.168.111.66
        #  ES route added to L2RIB: True
        #  EAD/ES routes added to L2RIB: False
        #  EAD/EVI route timer age: not running
        p1 = re.compile(r'^\s*ESI: +(?P<esi>[\w\.]+)$')
        p2 = re.compile(r'^\s*Parent +interface: +(?P<parent_intf>[\w\.\/]+)$')
        p3 = re.compile(r'^\s*ES +State: +(?P<es_state>[\w\/]+)$')
        p4 = re.compile(r'^\s*Port-channel +state: +(?P<po_state>[\w\/]+)$')
        p5 = re.compile(r'^\s*NVE +Interface: +(?P<nve_intf>[\w\.\/]+)$')
        p6 = re.compile(r'^\s*NVE +State: +(?P<nve_state>[\w\/]+)$')
        p7 = re.compile(r'^\s*Host +Learning +Mode: +(?P<host_learning_mode>[\w\-]+)$')
        p8 = re.compile(r'^\s*Active +Vlans: +(?P<active_vlans>[\d\-\,]+)$')
        p9 = re.compile(r'^\s*DF Vlans: +(?P<df_vlans>[\d\-\,]+)$')
        # 1026,1028,1030,1032,1034,1036,1038
        p10 = re.compile(r'^\s*,?(?P<df_vlans>[\d\-\,]+)$')
        p11 = re.compile(r'^\s*Active +VNIs: +(?P<active_vnis>[\d\-\,]+)$')
        p12 = re.compile(r'^\s*CC +failed +for +VLANs:( +(?P<cc_failed_vlans>[\w\/]+))?$')
        #   VLAN CC timer: no-timer
        p13 = re.compile(r'^\s*VLAN +CC +timer: +(?P<cc_timer_left>\S+)?$')
        p14 = re.compile(r'^\s*Number +of +ES +members: +(?P<num_es_mem>[\d]+)?$')
        p15 = re.compile(r'^\s*My +ordinal: +(?P<local_ordinal>[\d]+)$')
        p16 = re.compile(r'^\s*DF +timer +start +time: +(?P<df_timer_start_time>[\w\:]+)$')
        p17 = re.compile(r'^\s*Config +State: +(?P<config_status>[\w\/]+)$')
        p18 = re.compile(r'^\s*DF +List: +(?P<df_list>[\d\s\.]+)$')
        p19 = re.compile(r'^\s*ES +route +added +to +L2RIB: +(?P<is_es_added_to_l2rib>[\w]+)$')
        p20 = re.compile(r'^\s*EAD\/ES +routes +added +to +L2RIB: +(?P<ead_rt_added>[\w]+)$')
        p21 = re.compile(r'^\s*EAD/EVI +route +timer +age: +(?P<ead_evi_rt_timer_age>[\w\s]+)$')

        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                esi = group.pop('esi')
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                if_name = group.pop('parent_intf')
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                es_state = group.pop('es_state').lower()
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                po_state =  group.pop('po_state').lower()
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                nve_if_name = group.pop('nve_intf')
                esi_dict = result_dict.setdefault('nve', {}).setdefault(nve_if_name, {}).\
                                       setdefault('ethernet_segment', {}).setdefault('esi', {}).\
                                       setdefault(esi, {})
                esi_dict.update({'esi': esi})
                esi_dict.update({'nve_if_name': nve_if_name})
                esi_dict.update({'po_state': po_state})
                esi_dict.update({'if_name': if_name})
                esi_dict.update({'es_state': es_state})
                continue

            m = p6.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'nve_state': group.pop('nve_state').lower()})
                continue

            m = p7.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'host_reach_mode': group.pop('host_learning_mode').lower()})
                continue

            m = p8.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'active_vlans': group.pop('active_vlans')})
                continue

            m = p9.match(line)
            if m:
                group = m.groupdict()
                df_vlans = group.pop('df_vlans')
                esi_dict.update({'df_vlans':df_vlans})
                continue

            m = p10.match(line)
            if m:
                group = m.groupdict()
                df_vlans = "{},{}".format(df_vlans, group.pop('df_vlans'))
                esi_dict.update({'df_vlans': df_vlans})
                continue

            m = p11.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'active_vnis': group.pop('active_vnis')})
                continue

            m = p12.match(line)
            if m:
                group = m.groupdict()
                if not group.pop('cc_failed_vlans'):
                    esi_dict.update({'cc_failed_vlans': ''})
                else:
                    esi_dict.update({'cc_failed_vlans': group.pop('cc_failed_vlans')})
                continue

            m = p13.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'cc_timer_left': group.pop('cc_timer_left')})
                continue

            m = p14.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'num_es_mem': int(group.pop('num_es_mem'))})
                continue

            m = p15.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'local_ordinal': int(group.pop('local_ordinal'))})
                continue

            m = p16.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'df_timer_st': group.pop('df_timer_start_time')})
                continue

            m = p17.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'config_status': group.pop('config_status').lower()})
                continue

            m = p18.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'df_list': group.pop('df_list')})
                continue

            m = p19.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'es_rt_added': False if 'False' in group.pop('is_es_added_to_l2rib') else True})
                continue

            m = p20.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'ead_rt_added': False if 'False' in group.pop('ead_rt_added') else True})
                continue

            m = p21.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'ead_evi_rt_timer_age': group.pop('ead_evi_rt_timer_age')})
                continue
        return result_dict


# ====================================================
#  schema for show l2route evpn ethernet-segment all
# ====================================================
class ShowL2routeEvpnEternetSegmentAllSchema(MetaParser):
    """Schema for:
        show l2route evpn ethernet-segment all"""

    schema ={
        'evpn': {
            'ethernet_segment': {
                Any(): {
                    'ethernet_segment': str,
                    'originating_rtr': str,
                    'prod_name': str,
                    'int_ifhdl': str,
                    'client_nfn': int,
                }
            }
        }
    }
# ====================================================
#  Parser for show l2route evpn ethernet-segment all
# ====================================================
class ShowL2routeEvpnEternetSegmentAll(ShowL2routeEvpnEternetSegmentAllSchema):
    """parser for:
        show l2route evpn ethernet-segment all"""

    cli_command = 'show l2route evpn ethernet-segment all'

    def cli(self, output=None):
        # excute command to get output
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        result_dict = {}
        index = 1
        # ESI                      Orig Rtr. IP Addr  Prod  Ifindex      NFN Bitmap
        # ------------------------ -----------------  ----- ----------- ----------
        # 0300.00ff.0001.2c00.0309 192.168.111.55         VXLAN nve1         64

        p1 = re.compile(r'^\s*(?P<ethernet_segment>(?!ESI)[\w\.]+) +(?P<originating_rtr>[\d\.]+)'
                        ' +(?P<prod_name>[\w]+) +(?P<int_ifhdl>[\w\/]+) +(?P<client_nfn>[\w\.]+)$')
        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            m = p1.match(line)
            if m:
                evpn_dict = result_dict.setdefault('evpn',{}).setdefault('ethernet_segment', {}).setdefault(index, {})
                group = m.groupdict()
                for k, v in group.items():
                    try:
                        v = int(v)
                    except:
                        v = v.lower()
                    evpn_dict.update({k:v})

                index += 1
                continue

        return result_dict

# ====================================================
#  schema for show l2route topology detail
# ====================================================
class ShowL2routeTopologyDetailSchema(MetaParser):
    """Schema for:
        show l2route topology detail"""

    schema ={
        'topology': {
            'topo_id': {
                Any(): {
                    'topo_name': {
                        Any(): {
                            'topo_name': str,
                            Optional('topo_type'): str,
                            Optional('vni'): int,
                            Optional('encap_type'): int,
                            Optional('iod'): int,
                            Optional('if_hdl'): int,
                            Optional('vtep_ip'): str,
                            Optional('emulated_ip'): str,
                            Optional('emulated_ro_ip'): str,
                            Optional('tx_id'): int,
                            Optional('rcvd_flag'): int,
                            Optional('rmac'): str,
                            Optional('vrf_id'): int,
                            Optional('vmac'): str,
                            Optional('flags'): str,
                            Optional('sub_flags'): str,
                            Optional('prev_flags'): str,
                        }
                    }
                }
            }
        }
    }
# ====================================================
#  Parser for show l2route topology detail
# ====================================================
class ShowL2routeTopologyDetail(ShowL2routeTopologyDetailSchema):
    """parser for:
        show l2route topology detail"""

    cli_command = 'show l2route topology detail'
    exclude = [
        'tx_id']

    def cli(self, output=None):
        # excute command to get output
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        result_dict = {}
        # Topology ID   Topology Name   Attributes
        # -----------   -------------   ----------
        # 101           Vxlan-10001     VNI: 10001
        #                   Encap:0 IOD:0 IfHdl:1224736769
        #                   VTEP IP: 192.168.4.11
        #                   Emulated IP: 192.168.196.22
        #                   Emulated RO IP: 192.168.196.22
        #                   TX-ID: 20 (Rcvd Ack: 0)
        #                   RMAC: 5e00.00ff.050c, VRFID: 3
        #                   VMAC: 0200.c9ff.1722
        #                   Flags: L3cp, Sub_Flags: --, Prev_Flags: -
        p1 = re.compile(r'^\s*(?P<topo_id>[\d]+) +(?P<topo_name>[\w\-]+) +(?P<topo_type>[\w\/]+)(: +(?P<vni>[\d]+))?$')
        p2 = re.compile(r'^\s*Encap:(?P<encap_type>[\d]+) +IOD:(?P<iod>[\d]+) +IfHdl:(?P<if_hdl>[\d]+)$')
        p3 = re.compile(r'^\s*VTEP +IP: +(?P<vtep_ip>[\d\.]+)$')
        p4 = re.compile(r'^\s*Emulated +IP: +(?P<emulated_ip>[\d\.]+)$')
        p5 = re.compile(r'^\s*Emulated +RO +IP: +(?P<emulated_ro_ip>[\d\.]+)$')
        p6 = re.compile(r'^\s*TX-ID: +(?P<tx_id>[\d]+) +\((Rcvd +Ack: +(?P<rcvd_flag>[\d]+))\)$')
        p7 = re.compile(r'^\s*RMAC: +(?P<rmac>[\w\.]+), VRFID: +(?P<vrf_id>[\d]+)$')
        p8 = re.compile(r'^\s*VMAC: +(?P<vmac>[\w\.]+)$')
        p9 = re.compile(
            r'^\s*Flags: +(?P<flags>[\w]+), +Sub_Flags: +(?P<sub_flags>[\w\-]+), +Prev_Flags: +(?P<prev_flags>[\w\-]+)$')

        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            m0 = p1.match(line)
            if m0:
                group = m0.groupdict()
                topo_id = int(group.pop('topo_id'))
                topo_name = group.pop('topo_name')
                topo_type = group.pop('topo_type').lower()
                topo_dict = result_dict.setdefault('topology', {}).setdefault('topo_id', {}).setdefault(topo_id,{}).\
                                        setdefault('topo_name',{}).setdefault(topo_name,{})

                if m0.groupdict()['vni']:
                    vni = int(group.pop('vni'))
                    topo_dict.update({'vni': vni})

                topo_dict.update({'topo_type': topo_type})
                topo_dict.update({'topo_name': topo_name})
                continue

            m2 = m = ""
            if p2.match(line):
                m2 = p2.match(line)
            if p6.match(line):
                m2 = p6.match(line)
            if m2:
                group = m2.groupdict()
                topo_dict.update({k:int(v) for k,v in group.items() })
                continue

            if p3.match(line):
                m= p3.match(line)
            if p4.match(line):
                m = p4.match(line)
            if p5.match(line):
                m = p5.match(line)
            if p8.match(line):
                m = p8.match(line)
            if p9.match(line):
                m = p9.match(line)
            if m:
                group = m.groupdict()
                topo_dict.update({k:v for k, v in group.items()})
                continue

            m3 = p7.match(line)
            if m3:
                group = m3.groupdict()
                topo_dict.update({'rmac': group.pop('rmac')})
                topo_dict.update({'vrf_id': int(group.pop('vrf_id'))})
                continue
        return result_dict

# ====================================================
#  schema for show l2route mac all detail
# ====================================================
class ShowL2routeMacAllDetailSchema(MetaParser):
    """Schema for:
        show l2route mac all detail"""

    schema ={
        'topology': {
            'topo_id': {
                Any(): {
                    'mac': {
                        Any(): {
                            'mac_addr': str,
                            'prod_type': str,
                            'flags': str,
                            'seq_num': int,
                            'next_hop1': str,
                            'rte_res': str,
                            'fwd_state': str,
                            Optional('label'): int,
                            Optional('peer_id'): int,
                            Optional('res_pl'): str,
                            Optional('sent_to'): str,
                            Optional('soo'): int,
                            Optional('esi'): str,
                            Optional('encap'): int,
                            Optional('pl_flag'): bool,
                        }
                    }
                }
            }
        }
    }
# ====================================================
#  Parser for show l2route mac all detail
# ====================================================
class ShowL2routeMacAllDetail(ShowL2routeMacAllDetailSchema):
    """parser for:
            show l2route mac all detail"""

    cli_command = ['show l2route evpn mac all detail',
                   'show l2route evpn mac evi {evi} detail',
                   'show l2route evpn mac evi {evi} mac {mac} detail']
    exclude = [
        'mac']

    def cli(self, output=None, evi=None, mac=None):
        # excute command to get output
        if output is None:
            if evi and mac:
                cmd = self.cli_command[2].format(evi=evi, mac=mac)
            elif evi:
                cmd = self.cli_command[1].format(evi=evi)
            else:
                cmd = self.cli_command[0]
            out = self.device.execute(cmd, timeout=180)
        else:
            out = output

        result_dict = {}
        # Topology    Mac Address    Prod   Flags         Seq No     Next-Hops
        # ----------- -------------- ------ ------------- ---------- ----------------
        # 101         5e00.00ff.0209 VXLAN  Rmac          0          192.168.106.1
        #            Route Resolution Type: Regular
        #            Forwarding State: Resolved (PeerID: 2)
        #            Sent To: BGP
        #            SOO: 774975538
        #
        # 11          0000.1111.0108 BGP    Spl           0          3.2.2.1 (Label: 10011)
        #                                                            3.2.2.2 (Label: 10011)
        #             Route Resolution Type: ESI
        #             Forwarding State: Resolved (PL)
        #             Resultant PL: 3.2.2.1, 3.2.2.2
        #             Sent To: L2FM
        #             ESI : 0300.0000.0000.0000.0347
        #             Encap: 1

        #  11          0000.1111.0108 BGP    Spl           0          3.2.2.1 (Label: 10011)
        p1 = re.compile(r'^\s*(?P<topo_id>[\d]+) +(?P<mac_addr>[\w\.]+) +(?P<prod_type>[\w\,]+)'
                        ' +(?P<flags>[\w\,\-]+) +(?P<seq_num>[\d]+) +(?P<next_hop1>[\w\/\.]+)\s*'
                        '(?:\(Label: (?P<label>\d+)\).*)?$')
        #  3.2.2.2 (Label: 10011)
        p2 = re.compile(r'^\s*(?P<next_hop2>[\d\/\.]+)')
        #  Route Resolution Type: ESI
        p3 = re.compile(r'^\s*Route +Resolution +Type: +(?P<rte_res>[\w]+)$')
        #  Forwarding State: Resolved (PeerID: 2)
        p4 = re.compile(r'^\s*Forwarding +State: +(?P<fwd_state>[\w]+)( +\(PeerID: +(?P<peer_id>[\d]+)\))?$')
        #  Forwarding State: Resolved
        p10 = re.compile(r'^\s*Forwarding +State: +(?P<fwd_state>[\w]+)$')
        #  Forwarding State: Resolved (PL)
        p11 = re.compile(r'^\s*Forwarding +State: +(?P<fwd_state>[\w]+)( +\(PL\))$')
        #  Resultant PL: 3.2.2.1, 3.2.2.2
        p5 = re.compile(r'^\s*Resultant +PL: +(?P<res_pl>.*$)')
        #  ESI : 0300.0000.0000.0000.0347
        p6 = re.compile(r'^\s*ESI\s*: +(?P<esi>[\w\.]+)\s*$')
        #  Sent To: L2FM
        #  SOO: 774975538
        #  Encap: 1
        p7 = re.compile(r'^\s*(?P<key>[\w ]+) *: +(?P<value>\S+)\s*$')

        for line in out.splitlines():
            if line:
                line = line.rstrip()

            m = p1.match(line)
            if m:
                group = m.groupdict()
                topo_id = int(group.pop('topo_id'))
                mac_addr = group.pop('mac_addr')
                topo_dict = result_dict.setdefault('topology', {}).setdefault('topo_id', {}).setdefault(topo_id, {}). \
                                        setdefault('mac', {}).setdefault(mac_addr, {})

                flags = group.pop('flags')
                if flags.endswith(','):
                    flags = flags[:-1]

                topo_dict.update({'flags':  flags.lower()})
                topo_dict.update({'prod_type':  group.pop('prod_type').lower()})
                topo_dict.update({'seq_num':  int(group.pop('seq_num'))})
                topo_dict.update({'mac_addr':  mac_addr})
                try:
                    next_hop1 = Common.convert_intf_name(group.pop('next_hop1'))
                except:
                    next_hop1 = group.pop('next_hop1')
                topo_dict.update({'next_hop1': next_hop1})
                if group['label']:
                    topo_dict['label'] = int(group['label'])

                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                next_hop2 = group['next_hop2']
                prev_nexthop = topo_dict['next_hop1']
                next_hops = prev_nexthop + ',' + next_hop2
                topo_dict['next_hop1'] = next_hops
                continue

            m1 = ""
            if p3.match(line):
                m1 = p3.match(line)
            if p5.match(line):
                m1 = p5.match(line)
            if p6.match(line):
                m1 = p6.match(line)
            if m1:
                group = m1.groupdict()
                topo_dict.update({k:v.lower() for k,v in group.items()})
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                topo_dict.update({'fwd_state': group.get('fwd_state')})
                if group.get('peer_id'):
                    topo_dict.update({'peer_id': int(group.get('peer_id'))})
                continue

            m = p10.match(line)
            if m:
                group = m.groupdict()
                topo_dict.update({'fwd_state': group.get('fwd_state')})
                continue

            m = p11.match(line)
            if m:
                group = m.groupdict()
                topo_dict.update({
                    'fwd_state': group.get('fwd_state'),
                    'pl_flag': True
                })
                continue

            m = p7.match(line)
            if m:
                groups = m.groupdict()
                key = groups['key'].replace(' ', '_').replace('-', '_').lower()
                value = int(groups['value']) if groups['value'].isdigit() else groups['value'].lower()
                topo_dict.update({key:value})

        return result_dict

# ====================================================
#  schema for show l2route mac-ip all detail
# ====================================================
class ShowL2routeMacIpAllDetailSchema(MetaParser):
    """Schema for:
        show l2route mac-ip all detail"""

    schema ={
        'topology': {
            'topo_id': {
                Any(): {
                    'mac_ip': {
                        Any(): {
                            'mac_addr': str,
                            'mac_ip_prod_type': str,
                            Optional('mac_ip_flags'): str,
                            Optional('seq_num'): int,
                            'next_hop1': str,
                            'host_ip': str,
                            Optional('sent_to'): str,
                            Optional('soo'): int,
                            Optional('l3_info'): int,
                        }
                    }
                }
            }
        }
    }
# ====================================================
#  Parser for show l2route mac-ip all detail
# ====================================================
class ShowL2routeMacIpAllDetail(ShowL2routeMacIpAllDetailSchema):
    """parser for:
        show l2route mac-ip all detail"""

    cli_command = 'show l2route mac-ip all detail'

    def cli(self, output=None):
        # excute command to get output
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        result_dict = {}
        # Topology    Mac Address    Prod   Flags         Seq No     Host IP         Next-Hops
        # ----------- -------------- ------ ---------- --------------- ---------------
        # 1001        fa16.3eff.f6c1 BGP    --            0          10.36.10.11      192.168.106.1
        # 1001        fa16.3eff.9f0a HMM    --            0          10.36.10.55      Local
        #            Sent To: BGP
        #            SOO: 774975538
        #            L3-Info: 10001
        # 101         fa16.3eff.0987 HMM    --            0          10.111.1.3    Local
        # 101         fa16.3eff.e94e BGP    --            0          10.111.8.3    10.84.66.66
        # 101         0011.00ff.0034 BGP  10.36.3.2                      10.70.0.2
        p1 = re.compile(r'^\s*(?P<topo_id>[\d]+) +(?P<mac_addr>[\w\.]+) +(?P<mac_ip_prod_type>[\w\,]+)'
                        '( +(?P<mac_ip_flags>[\w\,\-]+))?( +(?P<seq_num>[\d]+))? +(?P<host_ip>[\w\/\.]+)'
                        ' +(?P<next_hop1>[\w\/\.]+)$')

        p2 = re.compile(r'^\s*Sent +To: +(?P<sent_to>[\w]+)$')
        p3 = re.compile(r'^\s*SOO: +(?P<soo>[\d]+)$')
        p4 = re.compile(r'^\s*L3-Info: +(?P<l3_info>[\d]+)$')

        # Topology    Mac Address    Host IP         Prod   Flags         Seq No     Next-Hops
        # ----------- -------------- --------------- ------ ---------- ---------------
        # 101         0000.9cff.2293 10.111.1.3     BGP    --            0         10.76.23.23
        # 201         0011.01ff.0001 10.1.1.2       BGP    --            0         2001:db8:646:a2bb:0:abcd:5678:1
        p5 = re.compile(r'^\s*(?P<topo_id>[\d]+) +(?P<mac_addr>[\w\.]+) +(?P<host_ip>[\w\/\.]+)'
                        ' +(?P<mac_ip_prod_type>[\w\,]+)'
                        ' +(?P<mac_ip_flags>[\w\,\-]+) +(?P<seq_num>[\d]+) +(?P<next_hop1>[\w\/\.]+)$')

        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                topo_id = int(group.pop('topo_id'))
                mac_addr = group.pop('mac_addr')
                topo_dict = result_dict.setdefault('topology', {}).setdefault('topo_id', {}).setdefault(topo_id,{}).\
                                        setdefault('mac_ip',{}).setdefault(mac_addr,{})
                if group['mac_ip_flags']:
                    flags = group.pop('mac_ip_flags')
                    topo_dict.update({'mac_ip_flags':  flags.lower()})
                if group['seq_num']:
                    topo_dict.update({'seq_num': int(group.pop('seq_num'))})
                topo_dict.update({'mac_ip_prod_type':  group.pop('mac_ip_prod_type').lower()})
                topo_dict.update({'mac_addr': mac_addr})
                topo_dict.update({'host_ip': group.pop('host_ip')})
                topo_dict.update({'next_hop1': group.pop('next_hop1').lower()})
                continue

            m1 = ""
            if p3.match(line):
                m1 = p3.match(line)
            if p4.match(line):
                m1 = p4.match(line)
            if m1:
                group = m1.groupdict()
                topo_dict.update({k:int(v) for k,v in group.items() })
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                topo_dict.update({k:v.lower() for k, v in group.items()})
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                topo_id = int(group.pop('topo_id'))
                mac_addr = group.pop('mac_addr')
                topo_dict = result_dict.setdefault('topology', {}).setdefault('topo_id', {}).setdefault(topo_id, {}). \
                    setdefault('mac_ip', {}).setdefault(mac_addr, {})

                flags = group.pop('mac_ip_flags')
                topo_dict.update({'mac_ip_flags': flags.lower()})
                topo_dict.update({'mac_ip_prod_type': group.pop('mac_ip_prod_type').lower()})
                topo_dict.update({'seq_num': int(group.pop('seq_num'))})
                topo_dict.update({'mac_addr': mac_addr})
                topo_dict.update({'host_ip': group.pop('host_ip')})
                topo_dict.update({'next_hop1': group.pop('next_hop1').lower()})
                continue

        return result_dict

# ====================================================
#  schema for show l2route summary
# ====================================================
class ShowL2routeSummarySchema(MetaParser):
    """Schema for:
        show l2route summary"""

    schema ={
        'summary': {
            'total_memory': int,
            'numof_converged_tables': int,
            Optional('table_name'): {
                Any(): {
                    'producer_name': {
                        Any(): {
                            'producer_name': str,
                            'id': int,
                            'objects': int,
                            'memory': int,
                        },
                        'total_obj': int,
                        'total_mem': int,
                    }
                }
            }
        }
    }

# ====================================================
#  Parser for show l2route summary
# ====================================================
class ShowL2routeSummary(ShowL2routeSummarySchema):
    """parser for:
        show l2route summary"""

    cli_command = 'show l2route summary'
    exclude = [
        'total_memory',
        'total_mem',
        'total_obj',
        'memory',
        'objects']

    def cli(self, output=None):
        # excute command to get output
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        result_dict = {}
        # L2ROUTE Summary
        # Total Memory: 6967
        # Number of Converged Tables: 47
        # Table Name: Topology
        # Producer   (ID)   Objects      Memory (Bytes)
        # ---------------   ----------   --------------
        # VXLAN     (11 )   21           5927
        # ---------------------------------------------
        # Total             21           5927
        # ---------------------------------------------
        p1 = re.compile(r'^\s*Total +Memory: +(?P<total_memory>[\d]+)$')
        p2 = re.compile(r'^\s*Number +of +Converged +Tables: +(?P<numof_converged_tables>[\d]+)$')
        p3 = re.compile(r'^\s*Table +Name: +(?P<table_name>[\w\-]+)$')
        p4 = re.compile(r'^\s*(?P<producer_name>[\w]+) +\((?P<id>[\d\s]+)\) +(?P<objects>[\d]+) +(?P<memory>[\d]+)$')
        p5 = re.compile(r'^\s*Total +(?P<total_obj>[\d]+) +(?P<total_mem>[\d]+)$')

        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                total_memory = int(group.pop('total_memory'))
                summary_dict = result_dict.setdefault('summary', {})
                summary_dict.update({'total_memory': total_memory})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                numof_converged_tables = int(group.pop('numof_converged_tables'))
                summary_dict.update({'numof_converged_tables': numof_converged_tables})
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                table_name = group.pop('table_name')
                table_dict = summary_dict.setdefault('table_name',{}).setdefault(table_name,{})
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                producer_name = group.pop('producer_name').lower()
                producer_dict = table_dict.setdefault('producer_name', {}).setdefault(producer_name, {})
                producer_dict.update({k:int(v) for k, v in group.items()})
                producer_dict.update({'producer_name':producer_name})
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                producer_dict = table_dict.setdefault('producer_name', {})
                producer_dict.update({k:int(v) for k,v in group.items() })
                continue

        return result_dict


# ====================================================
#  schema for show l2route fl all
# ====================================================
class ShowL2routeFlAllSchema(MetaParser):
    """Schema for:
        show l2route fl all"""

    schema = {
        'topology': {
            'topo_id': {
                Any():{
                    Optional('num_of_peer_id'): int,
                    'peer_id':{
                        Any():{
                            'topo_id': int,
                            'peer_id': int,
                            'flood_list': str,
                            'is_service_node': str,
                        },
                    },
                },
            },
        },
    }

# ====================================================
#  Parser for show l2route fl all
# ====================================================
class ShowL2routeFlAll(ShowL2routeFlAllSchema):
    """parser for:
        show l2route fl all"""

    cli_command = 'show l2route fl all'
    exclude = [
        'peer_id']

    def cli(self, output=None):
        # excute command to get output
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        result_dict = {}
        index = 0
        # Topology ID Peer-id     Flood List      Service Node
        # ----------- ----------- --------------- ------------

        p1 = re.compile(r'^\s*(?P<topo_id>[\d]+) +(?P<peer_id>[\d]+) +(?P<flood_list>[\w\.d]+) +(?P<is_service_node>[\w]+)$')

        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                topo_id = int(group.pop('topo_id'))
                peer_id = int(group.pop('peer_id'))
                peer_dict = result_dict.setdefault('topology', {}).setdefault('topo_id', {}).setdefault(topo_id, {}). \
                                setdefault('peer_id', {}).setdefault(peer_id, {})
                peer_dict.update({'topo_id': topo_id})
                peer_dict.update({'peer_id': peer_id})
                peer_dict.update({'flood_list': group.pop('flood_list')})
                peer_dict.update({'is_service_node': group.pop('is_service_node').lower()})
                continue

        if result_dict:
            for topo_id in result_dict['topology']['topo_id']:
                num_of_peer_id = len(result_dict['topology']['topo_id'][topo_id]['peer_id'])
                result_dict['topology']['topo_id'][topo_id]['num_of_peer_id'] = num_of_peer_id

        return result_dict

# ===================================================
#   Schema for show running-config nv ovelay
# ===================================================
class ShowRunningConfigNvOverlaySchema(MetaParser):
    """Schema for:
        show running-config nv overlay"""

    schema = {
            Optional('evpn_multisite_border_gateway'): int,
            Optional('multisite_convergence_time') : int,
            Optional('enabled_nv_overlay'): bool,
            Any():{
                Optional('nve_name'):str,
                Optional('if_state'): str,
                Optional('host_reachability_protocol'): str,
                Optional('adv_vmac'): bool,
                Optional('source_if'): str,
                Optional('multisite_bgw_if'): str,
                Optional('vni'):{
                    Any():{
                        Optional('vni'): int,
                        Optional('associated_vrf'): bool,
                        Optional('multisite_ingress_replication'): bool,
                        Optional('multisite_ingress_replication_optimized'): bool,
                        Optional('ingress_replication_protocol_bgp'): bool,
                        Optional('mcast_group'): str,
                        Optional('multisite_mcast_group'): str,
                        Optional('suppress_arp'): bool,
                        Optional('vni_type'): str,
                    },
                },
            },
            Optional('multisite'):{
                Optional('dci_links'):{
                    Any():{
                      'if_name': str,
                      'if_state': str,
                    },
                },
                Optional('fabric_links'): {
                    Any(): {
                        'if_name': str,
                        'if_state': str,
                    },
                },
            },
        }

# ====================================================
#  Parser for show running-config nv overlay
# =====================================================
class ShowRunningConfigNvOverlay(ShowRunningConfigNvOverlaySchema):
    """parser for:
        show running-config nv overlay"""

    cli_command = 'show running-config nv overlay'

    def cli(self, output=None):
        # execute command to get output
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        result_dict = {}
        # feature nv overlay
        p0 = re.compile(r'^\s*feature nv overlay$')
        #   evpn multisite border-gateway 111111
        p1 = re.compile(r'^\s*evpn multisite border-gateway +(?P<evpn_multisite_border_gateway>[\w]+)$')
        #   delay-restore time 185
        p2 = re.compile(r'^\s*delay-restore time +(?P<evpn_msite_bgw_delay_restore_time>[\d]+)$')
        #   interface nve1
        p3 = re.compile(r'^\s*interface +(?P<nve_name>nve[\d]+)$')
        #   no shutdown
        p4 = re.compile(r'^\s*no shutdown$')
        #   host-reachability protocol bgp
        p5 = re.compile(r'^\s*host-reachability protocol +(?P<host_reachability_protocol>[\w]+)$')
        #   advertise virtual-rmac
        p6 = re.compile(r'^\s*advertise virtual-rmac$')
        #   source-interface loopback1
        p7 = re.compile(r'^\s*source-interface +(?P<source_if>[\w]+)$')
        #   multisite border-gateway interface loopback3
        p8 = re.compile(r'^\s*multisite +border\-gateway +interface +(?P<multisite_bgw_if>[\w]+)$')
        #   member vni 10100 associate-vrf
        #   member vni 10100-10105 associate-vrf
        p9 = re.compile(r'^\s*member vni +(?P<nve_vni>[\d-]+)( +(?P<associated_vrf>[\w\-]+))?$')
        #   multisite ingress-replication
        p10 = re.compile(r'^\s*multisite ingress-replication$')
        #   mcast-group 231.100.1.1
        p11 = re.compile(r'^\s*mcast-group +(?P<mcast_group>[\d\.]+)$')
        #   interface Ethernet1/1
        #   interface port-channel11
        p12 = re.compile(r'^\s*interface +(?P<interface>(?!nve)[\w\/\-]+)$')
        #   evpn multisite fabric-tracking
        #   evpn multisite dci-tracking
        p13 = re.compile(r'^\s*evpn multisite +(?P<fabric_dci_tracking>[\w\-]+)$')
        # global suppress-arp
        p14 = re.compile(r'^global +suppress-arp$')
        # global mcast-group 192.168.0.1 L2
        p15 = re.compile(r'^global +mcast-group +(?P<address>[\d\.]+) +(?P<layer>L2|L3)')
        #   multisite ingress-replication optimized
        p16 = re.compile(r'^multisite +ingress-replication +optimized$')
        #   ingress-replication protocol bgp
        p17 = re.compile(r'^ingress-replication +protocol +bgp$')
        #   multisite mcast-group 226.1.1.1
        p18 = re.compile(r'^multisite mcast-group +(?P<multisite_mcast_group>[\d\.]+)$')


        for line in out.splitlines():
            line = line.strip()

            m = p0.match(line)
            if m:
                result_dict.update({'enabled_nv_overlay': True})
                continue

            m = p1.match(line)
            if m:
                multisite_border_gateway = m.groupdict().pop('evpn_multisite_border_gateway')
                result_dict.update({'evpn_multisite_border_gateway': int(multisite_border_gateway)})
                continue

            m = p2.match(line)
            if m:
                evpn_msite_bgw_delay_restore_time = m.groupdict().pop('evpn_msite_bgw_delay_restore_time')
                result_dict.update({'multisite_convergence_time': int(evpn_msite_bgw_delay_restore_time)})
                continue

            m = p3.match(line)
            if m:
                global_suppress_arp_flag = False
                global_mcast_group_flag = False
                nve_name = m.groupdict().pop('nve_name')
                nve_dict = result_dict.setdefault(nve_name, {})
                nve_dict.update({'nve_name': nve_name})
                continue

            m = p4.match(line)
            if m:
                nve_dict.update({'if_state': "up"})
                continue

            m = p5.match(line)
            if m:
                host_reachability_protocol = m.groupdict().pop('host_reachability_protocol')
                nve_dict.update({'host_reachability_protocol': host_reachability_protocol})
                continue

            m = p6.match(line)
            if m:
                nve_dict.update({'adv_vmac': True})
                continue

            m = p7.match(line)
            if m:
                source_if = m.groupdict().pop('source_if')
                nve_dict.update({'source_if': source_if})
                continue

            m = p8.match(line)
            if m:
                multisite_bgw_if = m.groupdict().pop('multisite_bgw_if')
                nve_dict.update({'multisite_bgw_if': multisite_bgw_if})
                continue

            m = p9.match(line)
            if m:
                group = m.groupdict()

                nve_vni = group.pop('nve_vni')
                if '-' in nve_vni:
                    nve_vni = nve_vni.split('-')
                    nve_vni_list = list(range(int(nve_vni[0]), int(nve_vni[1])+1))
                else:
                    nve_vni_list = [int(nve_vni)]

                for vni in nve_vni_list:
                    vni_dict = nve_dict.setdefault('vni', {}).setdefault(vni, {})
                    vni_dict.update({'vni': vni})
                    if group.get('associated_vrf'):
                        vni_dict.update({'associated_vrf': True})
                    else:
                        vni_dict.update({'associated_vrf': False})

                    if global_suppress_arp_flag:
                        vni_dict.update({'suppress_arp': True})

                    if global_mcast_group_flag:
                        vni_dict.update({'mcast_group': global_mcast_group_flag[0]})
                        vni_dict.update({'vni_type': global_mcast_group_flag[1]})

                continue

            m = p10.match(line)
            if m:
                for vni in nve_vni_list:
                    vni_dict = nve_dict.setdefault('vni', {}).setdefault(vni, {})
                    vni_dict.update({'multisite_ingress_replication': True})
                continue

            m = p11.match(line)
            if m:
                mcast = m.groupdict().pop('mcast_group')

                for vni in nve_vni_list:
                    vni_dict = nve_dict.setdefault('vni', {}).setdefault(vni, {})
                    vni_dict.update({'mcast_group': mcast})
                continue

            m = p12.match(line)
            if m:
                interface = m.groupdict().pop('interface')
                continue

            # interface port-channel11
            # interface Ethernet1/1
            m = p13.match(line)
            if m:
                tracking = m.groupdict().pop('fabric_dci_tracking')
                tracking_dict = result_dict.setdefault('multisite', {})
                if 'fabric' in tracking:
                    fabric_dict = tracking_dict.setdefault('fabric_links', {}).setdefault(interface, {})
                    fabric_dict.update({'if_name': interface})
                    fabric_dict.update({'if_state': 'up'})
                if 'dci' in tracking:
                    dci_dict = tracking_dict.setdefault('dci_links', {}).setdefault(interface, {})
                    dci_dict.update({'if_name': interface})
                    dci_dict.update({'if_state': 'up'})
                continue

            m = p14.match(line)
            if m:
                global_suppress_arp_flag = True
                continue

            m = p15.match(line)
            if m:
                global_mcast_group_flag = (m.groupdict()['address'], m.groupdict()['layer'])
                continue

            m = p16.match(line)
            if m:
                for vni in nve_vni_list:
                    vni_dict = nve_dict.setdefault('vni', {}).setdefault(vni, {})
                    vni_dict.update({'multisite_ingress_replication_optimized': True})
                continue

            m = p17.match(line)
            if m:
                for vni in nve_vni_list:
                    vni_dict = nve_dict.setdefault('vni', {}).setdefault(vni, {})
                    vni_dict.update({'ingress_replication_protocol_bgp': True})
                continue

            m = p18.match(line)
            if m:
                multisite_mcast = m.groupdict().pop('multisite_mcast_group')

                for vni in nve_vni_list:
                    vni_dict = nve_dict.setdefault('vni', {}).setdefault(vni, {})
                    vni_dict.update({'multisite_mcast_group': multisite_mcast})
                continue

        return result_dict

# ====================================================
#  schema for show nve vni ingress-replication
# ====================================================
class ShowNveVniIngressReplicationSchema(MetaParser):
    """Schema for:
        show nve vni ingress-replication"""

    schema ={
        Any(): {
            'vni': {
                Any(): {
                    'vni': int,
                     Optional('repl_ip'): {
                         Any(): {
                            Optional('repl_ip'): str,
                            Optional('source'): str,
                            Optional('up_time'): str,
                         }
                    }
                }
            }
        }
    }

# ====================================================
#  Parser for show nve vni ingress-replication
# ====================================================
class ShowNveVniIngressReplication(ShowNveVniIngressReplicationSchema):
    """parser for:
        show nve vni Ingress-replication"""

    cli_command = 'show nve vni ingress-replication'

    def cli(self, output=None):
        # excute command to get output
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        result_dict = {}

        # Interface VNI      Replication List  Source  Up Time
        # --------- -------- ----------------- ------- -------
        # nve1      10101    10.196.7.7           BGP-IMET 1d02h
        # nve1      10011    2001:db8:1:1::1:1           BGP-IMET   00:46:55
        # nve1      10211    fe80::2fe:c8ff:fe09:8fff           BGP-IMET   00:46:55

        p1 = re.compile(r'^(?P<nve_name>[\w]+) +(?P<vni>[\d]+)( '
                        r'+(?P<replication_list>[\d\.]+|[\w\:]+) '
                        r'+(?P<source>[\w\-]+) +(?P<uptime>[\w\:]+))?$')

        # 192.168.51.51        BGP-IMET 03:21:19
        # 192.168.154.52        BGP-IMET 03:15:18
        # 192.168.154.51        BGP-IMET 03:21:19
        # 2001:db8:1:4::1:4           BGP-IMET   00:48:12
        # fe80::2fe:c8ff:fe09:8fff BGP-IMET   00:47:54
        p2 = re.compile(r'^(?P<replication_list>[\d\.]+|[\w\:]+) '
                        r'+(?P<source>[\w\-]+) +(?P<uptime>[\w\:]+)$')

        for line in out.splitlines():
            line = line.strip()

            # nve1      10101    10.196.7.7           BGP-IMET 1d02h
            # nve1      10011    2001:db8:1:1::1:1           BGP-IMET   00:46:55
            # nve1      10211    fe80::2fe:c8ff:fe09:8fff           BGP-IMET   00:46:55
            m = p1.match(line)
            if m:
                group = m.groupdict()
                nve_name = group['nve_name']
                vni = int(group['vni'])
                nve_dict = result_dict.setdefault(nve_name,{}).setdefault('vni',{}).setdefault(vni,{})
                nve_dict.update({'vni': vni})

                if group['replication_list']:
                    repl_ip = group['replication_list'].strip()
                    repl_dict = nve_dict.setdefault('repl_ip', {}).setdefault(repl_ip, {})
                    repl_dict.update({'repl_ip': repl_ip})
                    repl_dict.update({'source': group['source'].lower()})
                    repl_dict.update({'up_time': group['uptime']})

                continue

            # 192.168.51.51        BGP-IMET 03:21:19
            # 192.168.154.52        BGP-IMET 03:15:18
            # 192.168.154.51        BGP-IMET 03:21:19
            # 2001:db8:1:4::1:4           BGP-IMET   00:48:12
            # fe80::2fe:c8ff:fe09:8fff BGP-IMET   00:47:54
            m2 = p2.match(line)
            if m2:
                group = m2.groupdict()
                repl_ip = group['replication_list'].strip()
                repl_dict = nve_dict.setdefault('repl_ip', {}).setdefault(repl_ip, {})
                repl_dict.update({'repl_ip': repl_ip})
                repl_dict.update({'source': group['source'].lower()})
                repl_dict.update({'up_time': group['uptime']})

                continue

        return result_dict

# ====================================================
#  schema for show fabric multicast globals
# ====================================================
class ShowFabricMulticastGlobalsSchema(MetaParser):
    """Schema for:
        show fabric multicast globals"""

    schema ={
        'multicast': {
            'globals': {
                'pruning': str,
                'switch_role': str,
                'fabric_control_seg': str,
                'peer_fabric_ctrl_addr': str,
                'advertise_vpc_rpf_routes': str,
                'created_vni_list': str,
                'fwd_encap': str,
                'overlay_distributed_dr': bool,
                'overlay_spt_only': bool,
                }
            }
        }

# ====================================================
#  Parser for show fabric multicast globals
# ====================================================
class ShowFabricMulticastGlobals(ShowFabricMulticastGlobalsSchema):
    """parser for:
        show fabric multicast globals"""

    cli_command = 'show fabric multicast globals'

    def cli(self, output=None):
        # excute command to get output
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        result_dict = {}

        # Pruning: segment-based
        p1 = re.compile(r'^\s*Pruning: +(?P<pruning>[\w\-]+)$')

        # Switch role:
        p2 = re.compile(r'^\s*Switch +role:( +(?P<switch_role>[\w]+))?$')

        # Fabric Control Seg: Null
        p3 = re.compile(r'^\s*Fabric +Control +Seg: +(?P<fabric_control_seg>[\w]+)$')

        # Peer Fabric Control Address: 0.0.0.0
        p4 = re.compile(r'^\s*Peer +Fabric +Control +Address: +(?P<peer_fabric_ctrl_addr>[\w\.]+)$')

        # Advertising vPC RPF routes: Disabled
        p5 = re.compile(r'^\s*Advertising +vPC +RPF +routes: +(?P<advertise_vpc_rpf_routes>[\w]+)$')

        # Created VNI List: -
        p6 = re.compile(r'^\s*Created +VNI +List: +(?P<created_vni_list>[\w\-]+)$')

        # Fwd Encap: (null)
        # Fwd Encap: Invalid encapsulation
        p7 = re.compile(r'^\s*Fwd +Encap: +(?P<fwd_encap>[\w\\(\)\s]+)$')

        # Overlay Distributed-DR: FALSE
        p8 = re.compile(r'^\s*Overlay +Distributed\-DR: +(?P<overlay_distributed_dr>[\w]+)$')

        # Overlay spt-only: TRUE
        p9 = re.compile(r'^\s*Overlay +spt\-only: +(?P<overlay_spt_only>[\w]+)$')

        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                global_dict = result_dict.setdefault('multicast', {}).setdefault('globals', {})
                global_dict.update({'pruning': group['pruning']})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                if group['switch_role']:
                    global_dict.update({'switch_role': group['switch_role']})
                else:
                    global_dict.update({'switch_role': ""})
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                global_dict.update({'fabric_control_seg': group['fabric_control_seg']})
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                global_dict.update({'peer_fabric_ctrl_addr': group['peer_fabric_ctrl_addr']})
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                global_dict.update({'advertise_vpc_rpf_routes': group['advertise_vpc_rpf_routes'].lower()})
                continue

            m = p6.match(line)
            if m:
                group = m.groupdict()
                global_dict.update({'created_vni_list': group['created_vni_list']})
                continue

            m = p7.match(line)
            if m:
                group = m.groupdict()
                global_dict.update({'fwd_encap': group['fwd_encap']})
                continue

            m = p8.match(line)
            if m:
                group = m.groupdict()
                global_dict.update({'overlay_distributed_dr': False if \
                    group['overlay_distributed_dr'].lower()=='false' else True})
                continue

            m = p9.match(line)
            if m:
                group = m.groupdict()
                global_dict.update({'overlay_spt_only': False if\
                    group['overlay_spt_only'].lower()=='false' else True})
                continue

        return result_dict

# ==========================================================
#  schema for show fabric multicast ipv4 sa-ad-route vrf all
# ==========================================================
class ShowFabricMulticastIpSaAdRouteSchema(MetaParser):
    """Schema for:
        show fabric multicast ipv4 sa-ad-route
        show fabric multicast ipv4 sa-ad-route vrf <vrf>
        show fabric multicast ipv4 sa-ad-route vrf all"""

    schema ={
        "multicast": {
            "vrf": {
                Any(): {
                    "vnid": str,
                    Optional("address_family"): {
                        Any(): {
                            "sa_ad_routes": {
                                "gaddr": {
                                    Any(): {
                                        "grp_len": int,
                                        "saddr": {
                                            Any(): {
                                                "src_len": int,
                                                "uptime": str,
                                                Optional("interested_fabric_nodes"): {
                                                    Any(): {
                                                        "uptime": str,
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

# ===========================================================
#  Parser for show fabric multicast ipv4 sa-ad-route vrf all
# ==========================================================
class ShowFabricMulticastIpSaAdRoute(ShowFabricMulticastIpSaAdRouteSchema):
    """parser for:
        show fabric multicast ipv4 sa-ad-route
        show fabric multicast ipv4 sa-ad-route vrf <vrf>
        show fabric multicast ipv4 sa-ad-route vrf all"""

    cli_command = ['show fabric multicast ipv4 sa-ad-route vrf {vrf}','show fabric multicast ipv4 sa-ad-route']
    exclude = [
        'uptime']

    def cli(self,vrf="",output=None):
        if vrf:
            cmd = self.cli_command[0].format(vrf=vrf)
        else:
            vrf = "default"
            cmd = self.cli_command[1]

        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output

        result_dict = {}
        # VRF "default" MVPN SA AD Route Database VNI: 0
        # VRF "vni_10100" MVPN SA AD Route Database VNI: 10100
        # VRF "vpc-keepalive" MVPN SA AD Route Database VNI: 0

        p1 = re.compile(r'^\s*VRF +\"(?P<vrf_name>\S+)\" +MVPN +SA +AD +Route +Database'
                        ' +VNI: +(?P<vnid>[\d]+)$')

        # Src Active AD route: (1.1.11.3/32, 226.0.0.1/32) uptime: 00:12:32
        # SA-AD Route: (1.1.11.3/32, 226.0.0.1/32) uptime: 00:12:32
        p2 = re.compile(r'((^\s*SA\-AD +Route:)|(^\s*Src +Active +AD +route:)) +\((?P<saddr>[\w\/\.]+), +(?P<gaddr>[\w\/\.]+)\)'
                        ' +uptime: +(?P<uptime>[\w\.\:]+)$')

        #  Interested Fabric Nodes:
        p3 = re.compile(r'^\s*Interested Fabric Nodes:$')


        #    This node, uptime: 00:01:01
        #    100.100.100.4, uptime: 00:01:01
        p4 = re.compile(r'^\s*(?P<interested_fabric_nodes>[\w\s\.]+), +uptime: +(?P<interest_uptime>[\w\.\:]+)$')

        for line in out.splitlines():
            if not line:
                continue
            line = line.strip()

            # VRF "vni_10100" MVPN SA AD Route Database VNI: 10100
            m = p1.match(line)
            if m:
                group = m.groupdict()
                vrf_dict = result_dict.setdefault('multicast', {}).setdefault('vrf', {}).\
                    setdefault(group['vrf_name'], {})
                vrf_dict.update({'vnid': group['vnid']})
                continue

            # SA-AD Route: (1.1.11.3/32, 226.0.0.1/32) uptime: 00:12:32
            m = p2.match(line)
            if m:
                group = m.groupdict()
                address_family_dict = vrf_dict.setdefault('address_family', {}).setdefault('ipv4', {})
                saddr = group['saddr']
                gaddr = group['gaddr']
                gaddr_dict = address_family_dict.setdefault('sa_ad_routes', {}).\
                    setdefault('gaddr', {}).setdefault(gaddr ,{})
                gaddr_dict.update({'grp_len': int(gaddr.split('/')[1])})

                saddr_dict = gaddr_dict.setdefault('saddr', {}).setdefault(saddr, {})
                saddr_dict.update({'src_len': int(saddr.split('/')[1])})
                saddr_dict.update({'uptime': group['uptime']})
                continue

            #    This node, uptime: 00:01:01
            #    100.100.100.4, uptime: 00:01:01
            m = p4.match(line)
            if m:
                group = m.groupdict()
                group['interested_fabric_nodes'] = group['interested_fabric_nodes']
                interested_dict = saddr_dict.setdefault('interested_fabric_nodes', {}).\
                    setdefault(group['interested_fabric_nodes'], {})
                interested_dict.update({'uptime': group['interest_uptime']})
                continue

        return result_dict

# ==========================================================
#  schema for show fabric multicast ipv4 mroute vrf all
# ==========================================================
class ShowFabricMulticastIpMrouteSchema(MetaParser):
    """Schema for:
        show fabric multicast ipv4 mroute
        show fabric multicast ipv4 mroute vrf <vrf>
        show fabric multicast ipv4 mroute vrf all"""

    schema ={
        "multicast": {
            "vrf": {
                Any(): {
                    "vnid": str,
                    Optional("address_family"): {
                        Any(): {
                            "fabric_mroutes": {
                                "gaddr": {
                                    Any(): {
                                        "grp_len": int,
                                        "saddr": {
                                            Any(): {
                                                Optional("src_len"): int,
                                                "uptime": str,
                                                Optional("rd_rt_ext_vri"): str,
                                                Optional("interested_fabric_nodes"): {
                                                    Any(): {
                                                        "uptime": str,
                                                        "rpfneighbor": str,
                                                        Optional("loc"): str,
                                                    }
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }

# ===========================================================
#  Parser for show fabric multicast ipv4 mroute vrf all
# ==========================================================
class ShowFabricMulticastIpMroute(ShowFabricMulticastIpMrouteSchema):
    """parser for:
        show fabric multicast ipv4 mroute
        show fabric multicast ipv4 mroute vrf <vrf>
        show fabric multicast ipv4 mroute vrf all"""

    cli_command = ['show fabric multicast ipv4 mroute vrf {vrf}','show fabric multicast ipv4 mroute']
    exclude = [
        'uptime']

    def cli(self,vrf="",output=None):
        if vrf:
            cmd = self.cli_command[0].format(vrf=vrf)
        else:
            vrf = "default"
            cmd = self.cli_command[1]

        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output

        result_dict = {}

        # VRF "trm-vxlan-3001" Fabric mroute Database VNI: 203001

        p1 = re.compile(r'^\s*VRF +\"(?P<vrf_name>\S+)\" +Fabric +mroute +Database'\
                        ' +VNI: +(?P<vnid>[\d]+)$')


        # Fabric Mroute: (179.1.12.11 / 32, 225.1.1.1 / 32) ptr: 0x56207780cbcc flags:0 uptime:00:01:01

        p2 = re.compile(r'^\s*Fabric +Mroute: +\((?P<saddr>[\w\/\.\*]+), +(?P<gaddr>[\w\/\.]+)\) +ptr: +0[xX][0-9a-'\
                        'fA-F]+ flags: +[0-9]+ +uptime: +(?P<uptime>[\w\.\:]+)$')

        # RD-RT ext comm Route-Import:  0b 64 64 64 06 0b b9 00 01 5a 5a 5a 06 80 0b e8 03 00 00
        p3 = re.compile(r'^\s*RD-RT ext comm Route-Import: +(?P<vri>[\w\s]+)$')
        #  Interested Fabric Nodes:
        p4 = re.compile(r'^\s*Interested Fabric Nodes:$')

        #   This node, uptime: 00:30:25    RPF Neighbor: 102.1.1.1
        #   100.100.100.1 (core), uptime: 00:30:25    RPF Neighbor: 102.1.1.1
        p5 = re.compile(r'^\s*(?P<interested_fabric_nodes>[\w\s\.]+) *(\((?P<loc>[\w]+)\))? *, +uptime: +'\
                         '(?P<interest_uptime>[\w\.\:]+) +RPF +Neighbor: +(?P<rpfneighbor>[\w\/\.]+)$')

        for line in out.splitlines():
            if not line:
                continue
            line = line.strip()

            # VRF "trm-vxlan-3001" Fabric mroute Database VNI: 203001
            m = p1.match(line)
            if m:
                group = m.groupdict()
                vrf_dict = result_dict.setdefault('multicast', {}).setdefault('vrf', {}).\
                    setdefault(group['vrf_name'], {})
                vrf_dict.update({'vnid': group['vnid']})
                continue

            # Fabric Mroute: (179.1.12.11 / 32, 225.1.1.1 / 32) ptr: 0x56207780cbcc flags:0 uptime:00:01:01
            m = p2.match(line)
            if m:
                group = m.groupdict()
                address_family_dict = vrf_dict.setdefault('address_family', {}).setdefault('ipv4', {})
                saddr = group['saddr']
                gaddr = group['gaddr']
                gaddr_dict = address_family_dict.setdefault('fabric_mroutes', {}).\
                    setdefault('gaddr', {}).setdefault(gaddr ,{})
                gaddr_dict.update({'grp_len': int(gaddr.split('/')[1])})
                saddr_dict = gaddr_dict.setdefault('saddr', {}).setdefault(saddr, {})
                if saddr != "*":
                    saddr_dict.update({'src_len': int(saddr.split('/')[1])})
                saddr_dict.update({'uptime': group['uptime']})
                continue
            # RD-RT ext comm Route-Import:  0b 64 64 64 06 0b b9 00 01 5a 5a 5a 06 80 0b e8 03 00 00
            m = p3.match(line)
            if m:
                group = m.groupdict()
                group["rd_rt_ext_vri"] = group['vri'].strip()
                saddr_dict.update({'rd_rt_ext_vri': group['rd_rt_ext_vri']})

            #   This node, uptime: 00:30:25    RPF Neighbor: 102.1.1.1
            #   100.100.100.1 (core), uptime: 00:30:25    RPF Neighbor: 102.1.1.1
            m = p5.match(line)
            if m:
                group = m.groupdict()
                group['interested_fabric_nodes'] = group['interested_fabric_nodes'].strip()
                group['loc'] = group['loc']
                interested_dict = saddr_dict.setdefault('interested_fabric_nodes', {}).\
                    setdefault(group['interested_fabric_nodes'], {})
                interested_dict.update({'uptime': group['interest_uptime']})
                interested_dict.update({'rpfneighbor': group['rpfneighbor']})
                if group.get('loc',None):
                    interested_dict.update({'loc': group['loc']})
                continue
        return result_dict


# ==========================================================
#  schema for show fabric multicast ipv4 l2-mroute vni all
# ==========================================================
class ShowFabricMulticastIpL2MrouteSchema(MetaParser):
    """Schema for:
        show fabric multicast ipv4 l2-mroute
        show fabric multicast ipv4 l2-mroute vni <vni>
        show fabric multicast ipv4 l2-mroute vni all"""

    schema = {
        'multicast': {
            "l2_mroute": {
                "vni": {
                    Any(): {
                        "vnid": str,
                        Optional("fabric_l2_mroutes"): {
                            "gaddr": {
                                Any(): {
                                    "saddr": {
                                        Any(): {
                                            "interested_fabric_nodes": {
                                                Any(): {
                                                    "node": str,
                                                }
                                            }
                                        }
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }


# ===========================================================
#  Parser for show fabric multicast ipv4 l2-mroute vni all
# ==========================================================
class ShowFabricMulticastIpL2Mroute(ShowFabricMulticastIpL2MrouteSchema):
    """parser for:
        show fabric multicast ipv4 l2-mroute
        show fabric multicast ipv4 l2-mroute vni <vni>
        show fabric multicast ipv4 l2-mroute vni all"""

    cli_command = ['show fabric multicast ipv4 l2-mroute vni {vni}','show fabric multicast ipv4 l2-mroute vni all']

    def cli(self, vni="",output=None):
        if vni:
            cmd = self.cli_command[0].format(vni=vni)
        else:
            cmd = self.cli_command[1]

        if output is None:
            out = self.device.execute(cmd)
        else:
            out = output

        result_dict = {}
        # EVPN C-Mcast Route Database for VNI: 10101
        p1 = re.compile(r'^\s*EVPN +C\-Mcast +Route +Database +for +VNI: +(?P<vni>[\d]+)$')

        # Fabric L2-Mroute: (*, 231.1.3.101/32)
        p2 = re.compile(r'^\s*Fabric +L2\-Mroute: +\((?P<saddr>[\w\/\.\*]+), +(?P<gaddr>[\w\/\.]+)\)$')

        #  Interested Fabric Nodes:
        p3 = re.compile(r'^\s*Interested Fabric Nodes:$')

        #   This node
        p4 = re.compile(r'^(?P<space>\s{4})(?P<interested_fabric_nodes>[\w\s\.]+)$')

        interested_flag = False
        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                vni = group['vni']
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                mroute_dict = result_dict.setdefault('multicast', {}). \
                    setdefault('l2_mroute', {}).setdefault('vni', {}). \
                    setdefault(vni, {})
                mroute_dict.update({'vnid': vni})
                fabric_dict = mroute_dict.setdefault('fabric_l2_mroutes', {})
                saddr = group['saddr']
                gaddr = group['gaddr']
                gaddr_dict = fabric_dict.setdefault('gaddr', {}).setdefault(gaddr, {})
                saddr_dict = gaddr_dict.setdefault('saddr', {}).setdefault(saddr, {})

                interested_flag = False
                continue

            m = p3.match(line)
            if m:
                interested_flag=True
                continue

            m = p4.match(line)
            if m:
                if interested_flag:
                    group = m.groupdict()
                    interested_fabric_nodes = group['interested_fabric_nodes']
                    interested_dict = saddr_dict.setdefault('interested_fabric_nodes', {}). \
                        setdefault(interested_fabric_nodes, {})
                    interested_dict.update({'node': interested_fabric_nodes})
                    continue

        return result_dict

# ====================================================
#  parser for 'show l2route evpn mac-ip all'
# ====================================================
class ShowL2routeEvpnMacIpAll(ShowL2routeMacIpAllDetail):
    """Parser for show l2route evpn mac-ip all"""
    cli_command = 'show l2route evpn mac-ip all'

    def cli(self, output=None):
        if output is None:
            show_output = self.device.execute(self.cli_command)
        else:
            show_output = output
        return super().cli(output=show_output)

# ====================================================
#  parser for 'show l2route evpn mac-ip evi <evi>'
# ====================================================
class ShowL2routeEvpnMacIpEvi(ShowL2routeMacIpAllDetail):
    """Parser for show l2route evpn mac-ip evi <evi>"""
    cli_command = 'show l2route evpn mac-ip evi {evi}'

    def cli(self, evi, output=None):
        if output is None:
            show_output = self.device.execute(self.cli_command.format(evi=evi))
        else:
            show_output = output
        return super().cli(output=show_output)
