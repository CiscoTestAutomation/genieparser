"""show_vxlan.py

NXOS parser for the following show commands:
    * show nve peers
    * show nve interface <nve> detail
    * show nve ethernet-segment
    * show nve vni
    * show nve vni summary
    * show nve multisite dci-links
    * show nve multisite fabric-links
"""

# Python
import re

# Metaparser
from metaparser import MetaParser
from metaparser.util.schemaengine import Schema, Any, Optional

from parser.utils.common import Common
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
                Any(): { # Conf/Ops Int 5001
                    'vni': int, # Conf/Ops Int 5001
                    'mcast': str, # Conf/Ops Str '234.1.1.1'
                    'vni_state': str, # Ops Str 'up'
                    'mode': str, # Ops Str 'cp'
                    'type': str, # Ops Str 'L2 [1001]'
                    'flags': str, # Ops Str ''
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
                nve_dict.update({'mcast': group.pop('mcast')})
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
#  schema for show nve interface <nve> detail
# ====================================================
class ShowNveInterfaceDetailSchema(MetaParser):
    """Schema for:
        show nve interface <nve> detail"""

    schema ={
        Any(): {
            'if_name': str,
            'if_state': str,
            'encap_type': str,
            'vpc_capability': str,
            'local_rmac': str,
            'host_reach_mode': str,
            'source_if': str,
            'primary_ip': str,
            'secondary_ip': str,
            'src_if_state': str,
            Optional('ir_cap_mode'): str,
            'adv_vmac': bool,
            'nve_flags': str,
            'nve_if_handle': int,
            'src_if_holddown_tm': int,
            'src_if_holdup_tm': int,
            'src_if_holddown_left': int,
            'vip_rmac': str,
            Optional('vip_rmac_ro'): str,
            'sm_state': str,
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
        out = self.device.execute('show nve interface {} detail'.format(intf))

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
        p23 = re.compile(r'^\s*Nve +MultiSite +Src +node +last +notif +sent: +(?P<notif_sent>[\w\-]+)$')
        p21 = re.compile(
            r'^\s*Multisite +bgw\-if: +(?P<multisite_bgw_if>[\w\/\-]+) +\(ip: +(?P<multisite_bgw_if_ip>[\w\.]+),'
            ' +admin: +(?P<multisite_bgw_if_admin_state>[\w]+), +oper: +(?P<multisite_bgw_if_oper_state>[\w]+)\)$')
        p22 = re.compile(r'^\s*Multisite +bgw\-if +oper +down +reason: +(?P<reason>[\w\.\s]+)$')


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
                nve_dict.update({'if_name': nve_name})
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
            m = p23.match(line)
            if m:
                group = m.groupdict()
                nve_dict.update({'multi_src_intf_last_reinit_notify_type': group.pop('notif_sent').lower()})
                continue

            # Multisite bgw-if: loopback2 (ip: 101.101.101.101, admin: Down, oper: Down)
            m = p21.match(line)
            if m:
                group = m.groupdict()
                nve_dict.update({'multisite_bgw_if': group.pop('intf')})
                nve_dict.update({'multisite_bgw_if_ip': group.pop('ip')})
                nve_dict.update({'multisite_bgw_if_admin_state': group.pop('admin').lower()})
                nve_dict.update({'multisite_bgw_if_oper_state': group.pop('oper').lower()})
                continue

            # Multisite bgw-if oper down reason: NVE not up.
            m = p22.match(line)
            if m:
                group = m.groupdict()
                nve_dict.update({'multisite_bgw_if_oper_state_down_reason': group.pop('reason')})
                continue
        return result_dict


# ====================================================
#  schema for show nve multisite
# ====================================================
class ShowNveMultisiteSchema(MetaParser):
    """Schema for:
        show nve multisite dci-links
        show nve multisite fabric-links"""

    schema ={
        'multisite': {
            Any():{
                'if_name': str,
                'if_state': str
            },
        },
    }

# ====================================================
#  Parser for show nve multisite dci-link
# ====================================================
class ShowNveMultisiteDciLinks(ShowNveMultisiteSchema):
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
                if_dict = result_dict.setdefault('multisite', {}).setdefault(if_name, {})

                if_dict.update({'if_name': if_name})
                if_dict.update({'if_state': if_state.lower()})
                continue

        return result_dict


# ====================================================
#  Parser for show nve multisite fabric-link
# ====================================================
class ShowNveMultisiteFabricLinks(ShowNveMultisiteSchema):
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
                if_dict = result_dict.setdefault('multisite',{}).setdefault(if_name,{})

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
                    'df_vlans': str,
                    'active_vnis': str,
                    'cc_failed_vlans': str,
                    'cc_timer_left': str,
                    'num_es_mem': int,
                    'local_ordinal': int,
                    'df_timer_st': str,
                    'config_status': str,
                    'df_list': str,
                    'es_rt_added': bool,
                    'ead_rt_added': bool,
                    'ead_evi_rt_timer_age': str,
                }
            }
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
                esi_dict = result_dict.setdefault('ethernet_segment',{}).setdefault('esi',{}).setdefault(esi,{})
                esi_dict.update({'esi':esi})
                continue

            m = p2.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'if_name': group.pop('parent_intf')})
                continue

            m = p3.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'es_state': group.pop('es_state').lower()})
                continue

            m = p4.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'po_state': group.pop('po_state').lower()})
                continue

            m = p5.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'nve_if_name': group.pop('nve_intf')})
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
                Any(): {  # Conf/Ops Int '101'
                    'topo_name': {
                        Any(): {  # Ops Str 'Vxlan-10001'
                            'topo_name': str,  # Ops Str 'Vxlan-10001'
                            'topo_type': str,  # Ops Str 'vni'
                            'vni': int,  # Ops Int 10001
                            'encap_type': int,  # Ops Int 0
                            'iod': int,  # Ops Int 0
                            'if_hdl': int,  # Ops Int 1224736769
                            'vtep_ip': str,  # Conf/Ops Str '201.11.11.11'
                            'emulated_ip': str,  # Ops Str '201.12.11.12'
                            'emulated_ro_ip': str,  # Ops Str '201.12.11.22'
                            'tx_id': int,  # Ops Int 20
                            'rcvd_flag': int,  # Ops Int 0
                            'rmac': str,  # Ops Str '5e00.0005.0007'
                            'vrf_id': int,  # Ops Int 3
                            'vmac': str,  # Ops Str '0200.c90c.0b16'
                            'flags': str,  # Ops Str 'l3cp'
                            'sub_flags': str,  # Ops Str '--'
                            'prev_flags': str,  # Ops Str '-'
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
        p1 = re.compile(r'^\s*(?P<topo_id>[\d]+) +(?P<topo_name>[\w\-]+) +(?P<topo_type>[\w]+): +(?P<vni>[\d]+)$')
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
                vni = int(group.pop('vni'))
                topo_dict = result_dict.setdefault('topology', {}).setdefault('topo_id', {}).setdefault(topo_id,{}).\
                                        setdefault('topo_name',{}).setdefault(topo_name,{})

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
                Any(): {  # Conf/Ops Int 101
                    'mac': {
                        Any(): {  # Ops Str '5e00.0002.0007'
                            'mac_addr': str,  # Ops Str 't300.0002.0007'
                            'prod_type': str,  # Ops Str 'vxlan'
                            'flags': str,  # Ops Str 'rmac'
                            'seq_num': int,  # Ops Int 0
                            'next_hop1': str,  # Ops Str '204.1.1.1'
                            'rte_res': str,  # Ops Str 'regular'
                            'fwd_state': str,  # Ops Str 'Resolved (PeerID: 2)'
                            Optional('sent_to'): str,  # Ops Str 'bgp'
                            Optional('soo'): int,  # Ops Int 774975538
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
        p3 = re.compile(r'^\s*Forwarding +State: +(?P<fwd_state>[\w\s\:\(\)]+)$')
        p4 = re.compile(r'^\s*Sent +To: +(?P<sent_to>[\w]+)$')
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
                topo_dict.update({k:v for k, v in group.items()})
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
                Any(): {  # Conf/Ops Int 101
                    'mac_ip': {
                        Any(): {  # Ops Str '5e00.0002.0007'
                            'mac_addr': str,  # Ops Str 't300.0002.0007'
                            'mac_ip_prod_type': str,  # Ops Str 'bgp'
                            'mac_ip_flags': str,  # Ops Str '--'
                            'seq_num': int,  # Ops Int 0
                            'next_hop1': str,  # Ops Str '204.1.1.1'
                            'host_ip': str,  # Ops Str '5.1.10.11'
                            Optional('sent_to'): str,  # Ops Str 'bgp'
                            Optional('soo'): int,  # Ops Int 774975538
                            Optional('l3_info'): int,  # Ops Int 10001
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

        return result_dict

# ====================================================
#  schema for show l2route summary
# ====================================================
class ShowL2routeSummarySchema(MetaParser):
    """Schema for:
        show l2route summary"""

    schema ={
        'summary': {
            'total_memory': int, # Ops Int 6967
            'numof_converged_tables': int, # Ops Int 47
            'table_name': {
                Any(): { # Ops Str 'Topology'
                    'producer_name': {
                        Any(): { # Ops Str 'vxlan'
                            'producer_name': str, # Ops Str 'vxlan'
                            'id': int, # Ops Int 11
                            'objects': int, # Ops Int 21
                            'memory': int, # Ops Int 5927
                        },
                        'total_obj': int, # Ops Int 21
                        'total_mem': int, # Ops Int 5927
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


