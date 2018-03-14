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
        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            # Interface Peer-IP          State LearnType Uptime   Router-Mac
            # nve1      201.202.1.1      Up    CP        01:15:09 n/a
            # nve1      204.1.1.1        Up    CP        00:03:05 5e00.0002.0007

            p1 = re.compile(r'^\s*(?P<nve_name>[\w\/]+) +(?P<peer_ip>[\w\.]+) +(?P<state>[\w]+)'
                           ' +(?P<learn_type>[\w]+) +(?P<uptime>[\w\:]+) +(?P<router_mac>[\w\.\/]+)$')
            m = p1.match(line)
            if m:
                nve_name = m.groupdict()['nve_name']
                peer_ip = m.groupdict()['peer_ip']
                state = m.groupdict()['state'].lower()
                learn_type = m.groupdict()['learn_type']
                uptime = m.groupdict()['uptime']
                router_mac = m.groupdict()['router_mac']

                if nve_name not in result_dict:
                    result_dict[nve_name] = {}
                result_dict[nve_name]['nve_name'] = nve_name
                if 'peer_ip' not in result_dict[nve_name]:
                    result_dict[nve_name]['peer_ip'] = {}
                if peer_ip not in result_dict[nve_name]['peer_ip']:
                    result_dict[nve_name]['peer_ip'][peer_ip] = {}

                result_dict[nve_name]['peer_ip'][peer_ip]['learn_type'] = learn_type
                result_dict[nve_name]['peer_ip'][peer_ip]['uptime'] = uptime
                result_dict[nve_name]['peer_ip'][peer_ip]['router_mac'] = router_mac
                result_dict[nve_name]['peer_ip'][peer_ip]['peer_state'] = state

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
        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            # Total CP VNIs: 21    [Up: 21, Down: 0]
            p1 = re.compile(r'^\s*Total +CP +VNIs: +(?P<cp_count>[\d]+) +\[Up: +(?P<cp_up>[\d]+), +Down: +(?P<cp_down>[\d]+)\]$')
            m = p1.match(line)
            if m:
                cp_count = m.groupdict()['cp_count']
                cp_up = m.groupdict()['cp_up']
                cp_down = m.groupdict()['cp_down']

                if 'vni' not in result_dict:
                    result_dict['vni'] = {}
                if 'summary' not in result_dict['vni']:
                    result_dict['vni']['summary'] = {}
                result_dict['vni']['summary']['cp_vni_count'] = int(cp_count)
                result_dict['vni']['summary']['cp_vni_up'] = int(cp_up)
                result_dict['vni']['summary']['cp_vni_down'] = int(cp_down)
                continue

            # Total DP VNIs: 0    [Up: 0, Down: 0]
            p2 = re.compile(
                r'^\s*Total +DP +VNIs: +(?P<dp_count>[\d]+) +\[Up: +(?P<dp_up>[\d]+), +Down: +(?P<dp_down>[\d]+)\]$')
            m = p2.match(line)
            if m:
                dp_count = m.groupdict()['dp_count']
                dp_up = m.groupdict()['dp_up']
                dp_down = m.groupdict()['dp_down']

                if 'vni' not in result_dict:
                    result_dict['vni'] = {}
                if 'summary' not in result_dict['vni']:
                    result_dict['vni']['summary'] = {}
                result_dict['vni']['summary']['dp_vni_count'] = int(dp_count)
                result_dict['vni']['summary']['dp_vni_up'] = int(dp_up)
                result_dict['vni']['summary']['dp_vni_down'] = int(dp_down)
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
        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            # Interface VNI      Multicast-group   State Mode Type [BD/VRF]      Flags
            #  --------- -------- ----------------- ----- ---- ------------------ -----
            # nve1      5001     234.1.1.1         Up    CP   L2 [1001]

            p1 = re.compile(r'^\s*(?P<nve_name>[\w\/]+) +(?P<vni>[\d]+) +(?P<multicast_group>[\w\.\/]+)'
                            ' +(?P<state>[\w]+) +(?P<mode>[\w]+) +(?P<type>[\w\s\-\[\]]+)( +(?P<flags>[\w]+))?$')
            m = p1.match(line)
            if m:
                nve_name = m.groupdict()['nve_name']
                vni = int(m.groupdict()['vni'])
                multicast_group = m.groupdict()['multicast_group']
                state = m.groupdict()['state'].lower()
                mode = m.groupdict()['mode']
                type = m.groupdict()['type']
                if m.groupdict()['flags']:
                    flags = m.groupdict()['flags']
                else:
                    flags= ""

                if nve_name not in result_dict:
                    result_dict[nve_name] = {}
                if 'vni' not in result_dict[nve_name]:
                    result_dict[nve_name]['vni'] = {}
                if vni not in result_dict[nve_name]['vni']:
                    result_dict[nve_name]['vni'][vni] = {}
                result_dict[nve_name]['vni'][vni]['vni'] = int(vni)
                result_dict[nve_name]['vni'][vni]['mcast'] = multicast_group
                result_dict[nve_name]['vni'][vni]['vni_state'] = state
                result_dict[nve_name]['vni'][vni]['mode'] = mode
                result_dict[nve_name]['vni'][vni]['type'] = type
                result_dict[nve_name]['vni'][vni]['flags'] = flags
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
        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            # Interface: nve1, State: Up, encapsulation: VXLAN
            p1 = re.compile(r'^\s*Interface: +(?P<nve_name>[\w\/]+), +State: +(?P<state>[\w]+),'
                            ' +encapsulation: +(?P<encapsulation>[\w]+)$')
            m = p1.match(line)
            if m:
                nve_name = m.groupdict()['nve_name']
                state = m.groupdict()['state'].lower()
                encapsulation = m.groupdict()['encapsulation'].lower()

                if nve_name not in result_dict:
                    result_dict[nve_name] = {}

                result_dict[nve_name]['if_name'] = nve_name
                result_dict[nve_name]['if_state'] = state
                result_dict[nve_name]['encap_type'] = encapsulation
                continue

            # VPC Capability: VPC-VIP-Only [notified]
            p2 = re.compile(r'^\s*VPC Capability: +(?P<vpc_capability>[\w\s\-\[\]]+)$')
            m = p2.match(line)
            if m:
                result_dict[nve_name]['vpc_capability'] = m.groupdict()['vpc_capability'].lower()
                continue

            #  Local Router MAC: 5e00.0005.0007
            p3 = re.compile(r'^\s*Local Router MAC: +(?P<local_router_mac>[\w\.]+)$')
            m = p3.match(line)
            if m:
                result_dict[nve_name]['local_rmac'] = m.groupdict()['local_router_mac']
                continue

            #  Host Learning Mode: Control-Plane
            p4 = re.compile(r'^\s*Host Learning Mode: +(?P<host_learning_mode>[\w\-]+)$')
            m = p4.match(line)
            if m:
                result_dict[nve_name]['host_reach_mode'] = m.groupdict()['host_learning_mode'].lower()
                continue

            #  Source-Interface: loopback1 (primary: 201.11.11.11, secondary: 201.12.11.22)
            p5 = re.compile(r'^\s*Source-Interface: +(?P<source_if>[\w\/]+)'
                            ' +\(primary: +(?P<primary_ip>[\w\.]+), +secondary: +(?P<secondary_ip>[\w\.]+)\)$')
            m = p5.match(line)
            if m:
                result_dict[nve_name]['source_if'] = m.groupdict()['source_if']
                result_dict[nve_name]['primary_ip'] = m.groupdict()['primary_ip']
                result_dict[nve_name]['secondary_ip'] = m.groupdict()['secondary_ip']
                continue

            #  Source Interface State: Up
            p6 = re.compile(r'^\s*Source +Interface +State: +(?P<source_state>[\w]+)$')
            m = p6.match(line)
            if m:
                result_dict[nve_name]['src_if_state'] = m.groupdict()['source_state'].lower()
                continue

            #  IR Capability Mode: No
            p7 = re.compile(r'^\s*IR +Capability +Mode: +(?P<mode>[\w]+)$')
            m = p7.match(line)
            if m:
                result_dict[nve_name]['ir_cap_mode'] = m.groupdict()['mode'].lower()
                continue

            #  Virtual RMAC Advertisement: Yes
            p8 = re.compile(r'^\s*Virtual +RMAC +Advertisement: +(?P<adv_vmac>[\w]+)$')
            m = p8.match(line)
            if m:
                result_dict[nve_name]['adv_vmac'] = True if m.groupdict()['adv_vmac'].lower() == 'yes' else False
                continue

            #  NVE Flags:
            p9 = re.compile(r'^\s*NVE +Flags:( +(?P<flags>[\w]+))?$')
            m = p9.match(line)
            if m:
                if m.groupdict()['flags']:
                    result_dict[nve_name]['nve_flags'] = m.groupdict()['flags']
                else:
                    result_dict[nve_name]['nve_flags'] = ""
                continue

            #  Interface Handle: 0x49000001
            p10 = re.compile(r'^\s*Interface +Handle: +(?P<intf_handle>[\w]+)$')
            m = p10.match(line)
            if m:
                result_dict[nve_name]['nve_if_handle'] = int(m.groupdict()['intf_handle'],0)
                continue

            #  Source Interface hold-down-time: 180
            p11 = re.compile(r'^\s*Source +Interface +hold-down-time: +(?P<hold_down_time>[\d]+)$')
            m = p11.match(line)
            if m:
                result_dict[nve_name]['src_if_holddown_tm'] = int(m.groupdict()['hold_down_time'])
                continue

            #  Source Interface hold-up-time: 30
            p12 = re.compile(r'^\s*Source +Interface +hold-up-time: +(?P<hold_up_time>[\d]+)$')
            m = p12.match(line)
            if m:
                result_dict[nve_name]['src_if_holdup_tm'] = int(m.groupdict()['hold_up_time'])
                continue

            #  Remaining hold-down time: 0 seconds
            p13 = re.compile(r'^\s*Remaining +hold-down +time: +(?P<hold_time_left>[\d]+) +seconds$')
            m = p13.match(line)
            if m:
                result_dict[nve_name]['src_if_holddown_left'] = int(m.groupdict()['hold_time_left'])
                continue

            #  Virtual Router MAC: 0200.c90c.0b16
            p14 = re.compile(r'^\s*Virtual +Router +MAC: +(?P<v_router_mac>[\w\.]+)$')
            m = p14.match(line)
            if m:
                result_dict[nve_name]['vip_rmac'] = m.groupdict()['v_router_mac']
                continue

            #  Virtual Router MAC Re-origination: 0200.6565.6565
            p15 = re.compile(r'^\s*Virtual +Router +MAC +Re\-origination: +(?P<v_router_mac_re>[\w\.]+)$')
            m = p15.match(line)
            if m:
                result_dict[nve_name]['vip_rmac_ro'] = m.groupdict()['v_router_mac_re']
                continue

            #  Interface state: nve-intf-add-complete
            p16 = re.compile(r'^\s*Interface +state: +(?P<intf_state>[\w\-]+)$')
            m = p16.match(line)
            if m:
                result_dict[nve_name]['sm_state'] = m.groupdict()['intf_state']
                continue

            #  unknown-peer-forwarding: disable
            p17 = re.compile(r'^\s*unknown-peer-forwarding: +(?P<peer_forwarding>[\w]+)$')
            m = p17.match(line)
            if m:
                result_dict[nve_name]['peer_forwarding_mode'] = False if m.groupdict()['peer_forwarding']== 'disable' else True
                continue

            #  down-stream vni config mode: n/a
            p18 = re.compile(r'^\s*down-stream +vni +config +mode: +(?P<vni_config_mode>[\w\/]+)$')
            m = p18.match(line)
            if m:
                result_dict[nve_name]['dwn_strm_vni_cfg_mode'] = m.groupdict()['vni_config_mode']
                continue

            # Nve Src node last notif sent: Port-up
            p19 = re.compile(r'^\s*Nve +Src +node +last +notif +sent: +(?P<last_notif_sent>[\w\-]+)$')
            m = p19.match(line)
            if m:
                result_dict[nve_name]['src_intf_last_reinit_notify_type'] = m.groupdict()['last_notif_sent'].lower()
                continue

            # Nve Mcast Src node last notif sent: None
            p20 = re.compile(r'^\s*Nve +Mcast +Src +node +last +notif +sent: +(?P<last_notif_sent>[\w\-]+)$')
            m = p20.match(line)
            if m:
                result_dict[nve_name]['mcast_src_intf_last_reinit_notify_type'] = m.groupdict()['last_notif_sent'].lower()
                continue

            # Nve MultiSite Src node last notif sent: None
            p23 = re.compile(r'^\s*Nve +MultiSite +Src +node +last +notif +sent: +(?P<notif_sent>[\w\-]+)$')
            m = p23.match(line)
            if m:
                result_dict[nve_name]['multi_src_intf_last_reinit_notify_type'] = m.groupdict()['notif_sent'].lower()

            # Multisite bgw-if: loopback2 (ip: 101.101.101.101, admin: Down, oper: Down)
            p21 = re.compile(r'^\s*Multisite +bgw\-if: +(?P<intf>[\w\/\-]+) +\(ip: +(?P<ip>[\w\.]+),'
                             ' +admin: +(?P<admin>[\w]+), +oper: +(?P<oper>[\w]+)\)$')
            m = p21.match(line)
            if m:
                result_dict[nve_name]['multisite_bgw_if'] = m.groupdict()['intf']
                result_dict[nve_name]['multisite_bgw_if_ip'] = m.groupdict()['ip']
                result_dict[nve_name]['multisite_bgw_if_admin_state'] = m.groupdict()['admin'].lower()
                result_dict[nve_name]['multisite_bgw_if_oper_state'] = m.groupdict()['oper'].lower()
                continue

            # Multisite bgw-if oper down reason: NVE not up.
            p22 = re.compile(r'^\s*Multisite +bgw\-if +oper +down +reason: +(?P<reason>[\w\.\s]+)$')
            m = p22.match(line)
            if m:
                result_dict[nve_name]['multisite_bgw_if_oper_state_down_reason']= m.groupdict()['reason']
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
        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            # Interface      State
            # ---------      -----
            # Ethernet1/53   Up

            p1 = re.compile(r'^\s*(?P<nve_name>(?!Interface)[\w\/]+) +(?P<state>[\w]+)$')
            m = p1.match(line)
            if m:
                if_name = m.groupdict()['nve_name']
                if_state = m.groupdict()['state'].lower()

                if 'multisite' not in result_dict:
                    result_dict['multisite'] = {}
                if if_name not in result_dict['multisite']:
                    result_dict['multisite'][if_name] = {}

                result_dict['multisite'][if_name]['if_name'] = if_name
                result_dict['multisite'][if_name]['if_state'] = if_state
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

        result_dict = {}
        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            # Interface      State
            # ---------      -----
            # Ethernet1/53   Up

            p1 = re.compile(r'^\s*(?P<nve_name>(?!Interface)[\w\/]+) +(?P<state>[\w]+)$')
            m = p1.match(line)
            if m:
                if_name = m.groupdict()['nve_name']
                if_state = m.groupdict()['state'].lower()

                if 'multisite' not in result_dict:
                    result_dict['multisite'] = {}
                if if_name not in result_dict['multisite']:
                    result_dict['multisite'][if_name] = {}

                result_dict['multisite'][if_name]['if_name'] = if_name
                result_dict['multisite'][if_name]['if_state'] = if_state
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
        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            # ESI: 0300.0000.0001.2c00.0309
            p1 = re.compile(r'^\s*ESI: +(?P<esi>[\w\.]+)$')
            p2 = re.compile(r'^\s*Parent +interface: +(?P<parent_intf>[\w\.\/]+)$')
            p3 = re.compile(r'^\s*ES +State: +(?P<es_state>[\w\/]+)$')
            p4 = re.compile(r'^\s*Port-channel +state: +(?P<po_state>[\w\/]+)$')
            p5 = re.compile(r'^\s*NVE +Interface: +(?P<nve_intf>[\w\.\/]+)$')

            m = p1.match(line)
            if m:
                group = m.groupdict()
                esi = group.pop('esi')
                esi_dict = result_dict.setdefault('ethernet_segment',{}).setdefault('esi',{}).setdefault(esi,{})
                esi_dict.update({'esi':esi})
                continue

            #    Parent interface: nve1
            m = p2.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'if_name': group.pop('parent_intf')})
                continue

            #   ES State: Up
            m = p3.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'es_state': group.pop('es_state').lower()})
                continue

            #   Port-channel state: N/A

            m = p4.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'po_state': group.pop('po_state').lower()})
                continue

            #   NVE Interface: nve1
            m = p5.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'nve_if_name': group.pop('nve_intf')})
                continue

            #    NVE State: Up
            p6 = re.compile(r'^\s*NVE +State: +(?P<nve_state>[\w\/]+)$')
            m = p6.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'nve_state': group.pop('nve_state').lower()})
                continue

            #    Host Learning Mode: control-plane
            p7 = re.compile(r'^\s*Host +Learning +Mode: +(?P<host_learning_mode>[\w\-]+)$')
            m = p7.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'host_reach_mode': group.pop('host_learning_mode').lower()})
                continue

            #   Active Vlans: 1,101-105,1001-1100,2001-2100,3001-3005
            p8 = re.compile(r'^\s*Active +Vlans: +(?P<active_vlans>[\d\-\,]+)$')
            m = p8.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'active_vlans': group.pop('active_vlans')})
                continue

            #  DF Vlans: 102,104,1002,1004,1006,1008,1010,1012,1014,1016,1018,1020,1022,1024
            p9 = re.compile(r'^\s*DF Vlans: +(?P<df_vlans>[\d\-\,]+)$')
            m = p9.match(line)
            if m:
                group = m.groupdict()
                df_vlans = group.pop('df_vlans')
                esi_dict.update({'df_vlans':df_vlans})

                continue

            # ,1026,1028,1030,1032,1034,1036,1038,1040,1042,1044,1046,1048,1050,1052,1054,1056
            p10 = re.compile(r'^\s*,(?P<df_vlans>[\d\-\,]+)$')
            m = p10.match(line)
            if m:
                group = m.groupdict()
                df_vlans = "{},{}".format(df_vlans, group.pop('df_vlans'))
                esi_dict.update({'df_vlans': df_vlans})
                continue

            #    Active VNIs: 501001-501100,502001-502100,503001-503005,600101-600105
            p11 = re.compile(r'^\s*Active +VNIs: +(?P<active_vnis>[\d\-\,]+)$')
            m = p11.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'active_vnis': group.pop('active_vnis')})
                continue

            #   CC failed for VLANs:
            p12 = re.compile(r'^\s*CC +failed +for +VLANs:( +(?P<cc_failed_vlans>[\w\/]+))?$')
            m = p12.match(line)
            if m:
                group = m.groupdict()
                if not group.pop('cc_failed_vlans'):
                    esi_dict.update({'cc_failed_vlans': ''})
                else:
                    esi_dict.update({'cc_failed_vlans': group.pop('cc_failed_vlans')})

                continue

            #   VLAN CC timer: 0
            p13 = re.compile(r'^\s*VLAN CC timer: +(?P<cc_timer_left>[\d]+)?$')
            m = p13.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'cc_timer_left': group.pop('cc_timer_left')})
                continue

            #   Number of ES members: 2
            p14 = re.compile(r'^\s*Number +of +ES +members: +(?P<num_es_mem>[\d]+)?$')
            m = p14.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'num_es_mem': int(group.pop('num_es_mem'))})
                continue

            #   My ordinal: 0
            p15 = re.compile(r'^\s*My +ordinal: +(?P<local_ordinal>[\d]+)$')
            m = p15.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'local_ordinal': int(group.pop('local_ordinal'))})
                continue

            #   DF timer start time: 00:00:00
            p16 = re.compile(r'^\s*DF +timer +start +time: +(?P<df_timer_start_time>[\w\:]+)$')
            m = p16.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'df_timer_st': group.pop('df_timer_start_time')})
                continue

            #   Config State: N/A
            p17 = re.compile(r'^\s*Config +State: +(?P<config_status>[\w\/]+)$')
            m = p17.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'config_status': group.pop('config_status').lower()})
                continue

            #   DF List: 201.0.0.55 201.0.0.66
            p18 = re.compile(r'^\s*DF +List: +(?P<df_list>[\d\s\.]+)$')
            m = p18.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'df_list': group.pop('df_list')})
                continue

            #  ES route added to L2RIB: True
            p19 = re.compile(r'^\s*ES +route +added +to +L2RIB: +(?P<is_es_added_to_l2rib>[\w]+)$')
            m = p19.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'es_rt_added': False if 'False' in group.pop('is_es_added_to_l2rib') else True})
                continue

            # EAD/ES routes added to L2RIB: False
            p20 = re.compile(r'^\s*EAD\/ES +routes +added +to +L2RIB: +(?P<ead_rt_added>[\w]+)$')
            m = p20.match(line)
            if m:
                group = m.groupdict()
                esi_dict.update({'ead_rt_added': False if 'False' in group.pop('ead_rt_added') else True})
                continue

            # #   EAD/EVI route timer age: not running
            p21 = re.compile(r'^\s*EAD/EVI +route +timer +age: +(?P<ead_evi_rt_timer_age>[\w\s]+)$')
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
        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue


            # ESI                      Orig Rtr. IP Addr  Prod  Ifindex      NFN Bitmap
            # ------------------------ -----------------  ----- ----------- ----------
            # 0300.0000.0001.2c00.0309 201.0.0.55         VXLAN nve1         64

            p1 = re.compile(r'^\s*(?P<ethernet_segment>(?!ESI)[\w\.]+) +(?P<originating_rtr>[\d\.]+)'
                             ' +(?P<prod_name>[\w]+) +(?P<int_ifhdl>[\w\/]+) +(?P<client_nfn>[\w\.]+)$')
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
        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue


            #Topology ID   Topology Name   Attributes
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
            p9 = re.compile(r'^\s*Flags: +(?P<flags>[\w]+), +Sub_Flags: +(?P<sub_flags>[\w\-]+), +Prev_Flags: +(?P<prev_flags>[\w\-]+)$')

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
        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            #Topology    Mac Address    Prod   Flags         Seq No     Next-Hops
            #----------- -------------- ------ ------------- ---------- ----------------
            #101         5e00.0002.0007 VXLAN  Rmac          0          204.1.1.1
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
        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

            #Topology    Mac Address    Prod   Flags         Seq No     Host IP         Next-Hops
            #----------- -------------- ------ ---------- --------------- ---------------
            #1001        fa16.3ec2.34fe BGP    --            0          5.1.10.11      204.1.1.1
            #1001        fa16.3ea3.fb66 HMM    --            0          5.1.10.55      Local
            #            Sent To: BGP
            #            SOO: 774975538
            #            L3-Info: 10001
            p1 = re.compile(r'^\s*(?P<topo_id>[\d]+) +(?P<mac_addr>[\w\.]+) +(?P<mac_ip_prod_type>[\w\,]+)'
                            ' +(?P<mac_ip_flags>[\w\,\-]+) +(?P<seq_num>[\d]+) +(?P<host_ip>[\w\/\.]+)'
                            ' +(?P<next_hop1>[\w\/\.]+)$')

            p2 = re.compile(r'^\s*Sent +To: +(?P<sent_to>[\w]+)$')
            p3 = re.compile(r'^\s*SOO: +(?P<soo>[\d]+)$')
            p4 = re.compile(r'^\s*L3-Info: +(?P<l3_info>[\d]+)$')

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
        for line in out.splitlines():
            if line:
                line = line.rstrip()
            else:
                continue

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


