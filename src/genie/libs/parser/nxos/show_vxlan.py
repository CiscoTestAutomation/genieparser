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
"""

# Python
import re

# Metaparser
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Schema, Any, Optional

from genie.libs.parser.utils.common import Common
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

    def cli(self):
        out = self.device.execute('show nve peers')

        result_dict = {}
        # Interface Peer-IP          State LearnType Uptime   Router-Mac
        # nve1      201.202.1.1      Up    CP        01:15:09 n/a
        # nve1      204.1.1.1        Up    CP        00:03:05 5e00.0002.0007

        p1 = re.compile(r'^\s*(?P<nve_name>[\w\/]+) +(?P<peer_ip>[\w\.]+) +(?P<peer_state>[\w]+)'
                        ' +(?P<learn_type>[\w]+) +(?P<uptime>[\w\:]+) +(?P<router_mac>[\w\.\/]+)$')

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

    def cli(self):
        out = self.device.execute('show nve vni summary')

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

    def cli(self):
        out = self.device.execute('show nve vni')

        result_dict = {}

        # Interface VNI      Multicast-group   State Mode Type [BD/VRF]      Flags
        #  --------- -------- ----------------- ----- ---- ------------------ -----
        # nve1      5001     234.1.1.1         Up    CP   L2 [1001]

        p1 = re.compile(r'^\s*(?P<nve_name>[\w\/]+) +(?P<vni>[\d]+) +(?P<mcast>[\w\.\/]+)'
                        ' +(?P<vni_state>[\w]+) +(?P<mode>[\w]+) +(?P<type>[\w\s\-\[\]]+)( +(?P<flags>[\w]+))?$')
        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue


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
                    nve_dict.update({'flags': ""})
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

    def cli(self):
        cmd = 'show interface | i nve'
        out = self.device.execute(cmd)
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
        }
    }

# ====================================================
#  schema for show nve interface <nve> detail
# ====================================================
class ShowNveInterfaceDetail(ShowNveInterfaceDetailSchema):
    """parser for:
        show nve interface <nve> detail"""

    def cli(self, intf=""):
        nve_list = []

        if intf:
            nve_list.append(intf)
        if not intf:
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
        p6 = re.compile(r'^\s*Source +Interface +State: +(?P<source_state>[\w]+)$')
        p7 = re.compile(r'^\s*IR +Capability +Mode: +(?P<mode>[\w]+)$')
        p8 = re.compile(r'^\s*Virtual +RMAC +Advertisement: +(?P<adv_vmac>[\w]+)$')
        p9 = re.compile(r'^\s*NVE +Flags:( +(?P<flags>[\w]+))?$')
        p10 = re.compile(r'^\s*Interface +Handle: +(?P<intf_handle>[\w]+)$')
        p11 = re.compile(r'^\s*Source +Interface +hold-down-time: +(?P<hold_down_time>[\d]+)$')
        p12 = re.compile(r'^\s*Source +Interface +hold-up-time: +(?P<hold_up_time>[\d]+)$')
        p13 = re.compile(r'^\s*Remaining +hold-down +time: +(?P<hold_time_left>[\d]+) +seconds$')
        p14 = re.compile(r'^\s*Virtual +Router +MAC: +(?P<v_router_mac>[\w\.]+)$')
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

        for nve in nve_list:
            out = self.device.execute('show nve interface {} detail'.format(nve))
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

                #  Local Router MAC: 5e00.0005.0007
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

                #  Source-Interface: loopback1 (primary: 201.11.11.11, secondary: 201.12.11.22)
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

                #  Virtual Router MAC: 0200.c90c.0b16
                m = p14.match(line)
                if m:
                    group = m.groupdict()
                    nve_dict.update({'vip_rmac': group.pop('v_router_mac')})
                    continue

                #  Virtual Router MAC Re-origination: 0200.6565.6565
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

                # Multisite bgw-if: loopback2 (ip: 101.101.101.101, admin: Down, oper: Down)
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

    def cli(self):
        out = self.device.execute('show nve multisite dci-links')

        result_dict = {}
        # Interface      State
        # ---------      -----
        # Ethernet1/53   Up

        p1 = re.compile(r'^\s*(?P<if_name>(?!Interface)[\w\/]+) +(?P<if_state>[\w]+)$')
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

    def cli(self):
        out = self.device.execute('show nve multisite fabric-links')

        # Interface      State
        # ---------      -----
        # Ethernet1/53   Up

        p1 = re.compile(r'^\s*(?P<if_name>(?!Interface)[\w\/]+) +(?P<if_state>[\w]+)$')

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

    def cli(self):
        out = self.device.execute('show nve ethernet-segment')
        df_vlans = ""
        result_dict = {}

        # ESI: 0300.0000.0001.2c00.0309
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
        #  DF List: 201.0.0.55 201.0.0.66
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
        p10 = re.compile(r'^\s*,(?P<df_vlans>[\d\-\,]+)$')
        p11 = re.compile(r'^\s*Active +VNIs: +(?P<active_vnis>[\d\-\,]+)$')
        p12 = re.compile(r'^\s*CC +failed +for +VLANs:( +(?P<cc_failed_vlans>[\w\/]+))?$')
        p13 = re.compile(r'^\s*VLAN CC timer: +(?P<cc_timer_left>[\d]+)?$')
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

    def cli(self):
        out = self.device.execute('show l2route evpn ethernet-segment all')

        result_dict = {}
        index = 1
        # ESI                      Orig Rtr. IP Addr  Prod  Ifindex      NFN Bitmap
        # ------------------------ -----------------  ----- ----------- ----------
        # 0300.0000.0001.2c00.0309 201.0.0.55         VXLAN nve1         64

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

    def cli(self):
        out = self.device.execute('show l2route topology detail')

        result_dict = {}
        # Topology ID   Topology Name   Attributes
        # -----------   -------------   ----------
        # 101           Vxlan-10001     VNI: 10001
        #                   Encap:0 IOD:0 IfHdl:1224736769
        #                   VTEP IP: 201.11.11.11
        #                   Emulated IP: 201.12.11.22
        #                   Emulated RO IP: 201.12.11.22
        #                   TX-ID: 20 (Rcvd Ack: 0)
        #                   RMAC: 5e00.0005.0007, VRFID: 3
        #                   VMAC: 0200.c90c.0b16
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
                            Optional('peer_id'): int,
                            Optional('sent_to'): str,
                            Optional('soo'): int,
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

    def cli(self):
        out = self.device.execute('show l2route mac all detail')

        result_dict = {}
        # Topology    Mac Address    Prod   Flags         Seq No     Next-Hops
        # ----------- -------------- ------ ------------- ---------- ----------------
        # 101         5e00.0002.0007 VXLAN  Rmac          0          204.1.1.1
        #            Route Resolution Type: Regular
        #            Forwarding State: Resolved (PeerID: 2)
        #            Sent To: BGP
        #            SOO: 774975538
        p1 = re.compile(r'^\s*(?P<topo_id>[\d]+) +(?P<mac_addr>[\w\.]+) +(?P<prod_type>[\w\,]+)'
                        ' +(?P<flags>[\w\,\-]+) +(?P<seq_num>[\d]+) +(?P<next_hop1>[\w\/\.]+)$')

        p2 = re.compile(r'^\s*Route +Resolution +Type: +(?P<rte_res>[\w]+)$')
        p3 = re.compile(r'^\s*Forwarding +State: +(?P<fwd_state>[\w]+)( +\(PeerID: +(?P<peer_id>[\d]+)\))?$')
        p4 = re.compile(r'^\s*Sent +To: +(?P<sent_to>[\w\,]+)$')
        p5 = re.compile(r'^\s*SOO: +(?P<soo>[\d]+)$')

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
                                        setdefault('mac',{}).setdefault(mac_addr,{})

                flags = group.pop('flags')
                if flags.endswith(','):
                    flags = flags[:-1]

                topo_dict.update({'flags':  flags.lower()})
                topo_dict.update({'prod_type':  group.pop('prod_type').lower()})
                topo_dict.update({'seq_num': int(group.pop('seq_num'))})
                topo_dict.update({'mac_addr': mac_addr})
                try:
                    next_hop1 = Common.convert_intf_name(group.pop('next_hop1'))
                except:
                    next_hop1 = group.pop('next_hop1')
                topo_dict.update({'next_hop1': next_hop1})

                continue

            m1 = ""
            if p2.match(line):
                m1 = p2.match(line)
            if p4.match(line):
                m1 = p4.match(line)
            if m1:
                group = m1.groupdict()
                topo_dict.update({k:v.lower() for k,v in group.items() })
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                topo_dict.update({'fwd_state': group.get('fwd_state')})
                if group.get('peer_id'):
                    topo_dict.update({'peer_id': int(group.get('peer_id'))})
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                topo_dict.update({k:int(v) for k, v in group.items()})
                continue

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
                            'mac_ip_flags': str,
                            'seq_num': int,
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

    def cli(self):
        out = self.device.execute('show l2route mac-ip all detail')

        result_dict = {}
        # Topology    Mac Address    Prod   Flags         Seq No     Host IP         Next-Hops
        # ----------- -------------- ------ ---------- --------------- ---------------
        # 1001        fa16.3ec2.34fe BGP    --            0          5.1.10.11      204.1.1.1
        # 1001        fa16.3ea3.fb66 HMM    --            0          5.1.10.55      Local
        #            Sent To: BGP
        #            SOO: 774975538
        #            L3-Info: 10001
        p1 = re.compile(r'^\s*(?P<topo_id>[\d]+) +(?P<mac_addr>[\w\.]+) +(?P<mac_ip_prod_type>[\w\,]+)'
                        ' +(?P<mac_ip_flags>[\w\,\-]+) +(?P<seq_num>[\d]+) +(?P<host_ip>[\w\/\.]+)'
                        ' +(?P<next_hop1>[\w\/\.]+)$')

        p2 = re.compile(r'^\s*Sent +To: +(?P<sent_to>[\w]+)$')
        p3 = re.compile(r'^\s*SOO: +(?P<soo>[\d]+)$')
        p4 = re.compile(r'^\s*L3-Info: +(?P<l3_info>[\d]+)$')
        # Topology    Mac Address    Host IP         Prod   Flags         Seq No     Next-Hops
        # ----------- -------------- --------------- ------ ---------- ---------------
        # 101         0000.9cfc.2596 100.101.1.3     BGP    --            0         23.23.23.23
        p5 = re.compile(r'^\s*(?P<topo_id>[\d]+) +(?P<mac_addr>[\w\.]+) +(?P<host_ip>[\w\/\.]+)'
                        ' +(?P<mac_ip_prod_type>[\w\,]+)'
                        ' +(?P<mac_ip_flags>[\w\,\-]+) +(?P<seq_num>[\d]+)'
                        ' +(?P<next_hop1>[\w\/\.]+)$')

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

                flags = group.pop('mac_ip_flags')
                topo_dict.update({'mac_ip_flags':  flags.lower()})
                topo_dict.update({'mac_ip_prod_type':  group.pop('mac_ip_prod_type').lower()})
                topo_dict.update({'seq_num': int(group.pop('seq_num'))})
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

    def cli(self):
        out = self.device.execute('show l2route summary')

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

    def cli(self):
        out = self.device.execute('show l2route fl all')

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
                        Optional('mcast_group'): str
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

    def cli(self):
        out = self.device.execute('show running-config nv overlay')

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
        #   multisite border-gateway interface loopback3
        p8 = re.compile(r'^\s*multisite +border\-gateway +interface +(?P<multisite_bgw_if>[\w]+)$')
        #   member vni 10100 associate-vrf
        p9 = re.compile(r'^\s*member vni +(?P<nve_vni>[\d]+)( +(?P<associated_vrf>[\w\-]+))?$')
        #   multisite ingress-replication
        p10 = re.compile(r'^\s*multisite ingress-replication$')
        #   mcast-group 231.100.1.1
        p11 = re.compile(r'^\s*mcast-group +(?P<mcast_group>[\d\.]+)$')
        #   interface Ethernet1/1
        p12 = re.compile(r'^\s*interface +(?P<interface>(?!nve)[\w\/]+)$')
        #   evpn multisite fabric-tracking
        #   evpn multisite dci-tracking
        p13 = re.compile(r'^\s*evpn multisite +(?P<fabric_dci_tracking>[\w\-]+)$')

        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

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
                nve_vni = int(group.pop('nve_vni'))
                vni_dict = nve_dict.setdefault('vni',{}).setdefault(nve_vni,{})
                vni_dict.update({'vni':nve_vni})

                if group.get('associated_vrf'):
                    vni_dict.update({'associated_vrf':True})
                    group.pop('associated_vrf')
                else:
                    vni_dict.update({'associated_vrf': False})

                continue

            m = p10.match(line)
            if m:
                vni_dict.update({'multisite_ingress_replication': True})
                continue

            m = p11.match(line)
            if m:
                mcast = m.groupdict().pop('mcast_group')
                vni_dict.update({'mcast_group': mcast})
                continue

            m = p12.match(line)
            if m:
                interface = m.groupdict().pop('interface')
                continue

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

    def cli(self):
        out = self.device.execute('show nve vni ingress-replication')

        result_dict = {}

        # Interface VNI      Replication List  Source  Up Time
        # --------- -------- ----------------- ------- -------
        # nve1      10101    7.7.7.7           BGP-IMET 1d02h

        p1 = re.compile(r'^\s*(?P<nve_name>[\w]+) +(?P<vni>[\d]+)( +(?P<replication_list>[\w\.]+)'
                        ' +(?P<source>[\w\-]+) +(?P<uptime>[\w\:]+))?$')
        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue


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

    def cli(self):
        out = self.device.execute('show fabric multicast globals')

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
        p7 = re.compile(r'^\s*Fwd +Encap: +(?P<fwd_encap>[\w\\(\)]+)$')

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

    def cli(self,vrf=""):
        if vrf:
            out = self.device.execute('show fabric multicast ipv4 sa-ad-route vrf {}'.format(vrf))
        else:
            vrf = "default"
            out = self.device.execute('show fabric multicast ipv4 sa-ad-route')

        result_dict = {}
        # VRF "default" MVPN SA AD Route Database VNI: 0
        # VRF "vni_10100" MVPN SA AD Route Database VNI: 10100
        # VRF "vpc-keepalive" MVPN SA AD Route Database VNI: 0

        p1 = re.compile(r'^\s*VRF +\"(?P<vrf_name>\S+)\" +MVPN +SA +AD +Route +Database'
                        ' +VNI: +(?P<vnid>[\d]+)$')

        # Src Active AD Route: (100.101.1.3/32, 238.8.4.101/32) uptime: 00:01:01
        p2 = re.compile(r'^\s*Src +Active +AD +Route: +\((?P<saddr>[\w\/\.]+), +(?P<gaddr>[\w\/\.]+)\)'
                        ' +uptime: +(?P<uptime>[\w\.\:]+)$')
        #  Interested Fabric Nodes:
        p3 = re.compile(r'^\s*Interested Fabric Nodes:$')

        #    This node, uptime: 00:01:01
        p4 = re.compile(r'^\s*(?P<interested_fabric_nodes>[\w\s\.]+), +uptime: +(?P<interest_uptime>[\w\.\:]+)$')

        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            m = p1.match(line)
            if m:
                group = m.groupdict()
                vrf_dict = result_dict.setdefault('multicast', {}).setdefault('vrf', {}).\
                    setdefault(group['vrf_name'], {})
                vrf_dict.update({'vnid': group['vnid']})
                continue

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

    def cli(self, vni=""):
        if vni:
            out = self.device.execute('show fabric multicast ipv4 l2-mroute vni {}'.format(vni))
        else:
            out = self.device.execute('show fabric multicast ipv4 l2-mroute vni all')

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





