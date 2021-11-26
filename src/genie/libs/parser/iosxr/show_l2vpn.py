"""show_l2vpn.py

show l2vpn parser class
show l2vpn bridge-domain
show l2vpn bridge-domain summary
show l2vpn bridge-domain brief
show l2vpn bridge-domain detail
"""
# Python
import re
from ipaddress import ip_address

# Genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any, Optional
from genie.libs.parser.utils.common import Common


# ================================================================================
# Parser for 'show l2vpn mac-learning {mac_type} all location {location}'
# ================================================================================
class ShowL2vpnMacLearningSchema(MetaParser):
    """Schema for:
        * 'show l2vpn mac-learning {mac_type} all location {location}'
    """
    schema = {
        'topo_id': {
            Any(): {
                'producer': {
                    Any(): {
                        'next_hop': {
                            Any(): {
                                'mac_address': {
                                    Any(): {
                                        Optional('ip_address'): list
                                    }
                                }
                            }
                        }
                    }
                }
            }
        }
    }


class ShowL2vpnMacLearning(ShowL2vpnMacLearningSchema):
    """Parser class for show l2vpn mac-learning <mac_type> all location <location>"""

    cli_command = ['show l2vpn mac-learning {mac_type} all location {location}']

    def cli(self, mac_type='', location='', output=None):
        if output is None:
            cmd = self.cli_command[0].format(
                mac_type=mac_type, location=location)
            out = self.device.execute(cmd)
        else:
            out = output

        # Topo ID  Producer  Next Hop(s)  Mac Address     IP Address

        # 6        0/0/CPU0   BV1        1000.00ff.0102      10.1.1.11
        # 6        0/0/CPU0   BV1        0000.f6ff.8fd6      fe80::200:f6ff:feff:8fd6
        # 1        0/0/CPU0   BE1.7      7777.77ff.7779

        p = re.compile(r'^(?P<topo_id>\d+) +'
                       r'(?P<producer>\S+) +'
                       r'(?P<next_hop>\S+) +'
                       r'(?P<mac_address>\S+)'
                       '( +(?P<ip_address>\S+))?$')

        parsed_dict = {}

        for line in out.splitlines():
            line = line.strip()

            result = p.match(line)

            if result:
                group_dict = result.groupdict()
                # ip_address_dict = {}

                str_ip_address = group_dict.get('ip_address')

                ip_address_dict = parsed_dict.setdefault(
                    'topo_id', {}).setdefault(group_dict['topo_id'],
                                              {}).setdefault(
                    'producer',
                    {}).setdefault(
                    group_dict['producer'], {}
                ).setdefault('next_hop', {}).setdefault(
                    group_dict['next_hop'], {}
                ).setdefault('mac_address', {}).setdefault(
                    group_dict['mac_address'], {}
                )
                ip_address_list = ip_address_dict.setdefault('ip_address', [])
                if str_ip_address:
                    ip_address_list.append(str_ip_address)

                continue

        return parsed_dict


# ================================================================================
# Parser for 'show l2vpn forwarding bridge-domain mac-address location {location}'
# ================================================================================

class ShowL2vpnForwardingBridgeDomainMacAddressSchema(MetaParser):
    """Schema for:
        show l2vpn forwarding bridge-domain mac-address location {location}
        show l2vpn forwarding bridge-domain {bridge_domain} mac-address location {location}
    """

    schema = {
        'mac_table': {
            Any(): {
                'mac_address': {
                    Any(): {
                        'type': str,
                        'learned_from': str,
                        'lc_learned': str,
                        'resync_age': str,
                        'mapped_to': str,
                    },
                }
            },
        }
    }


class ShowL2vpnForwardingBridgeDomainMacAddress(
    ShowL2vpnForwardingBridgeDomainMacAddressSchema):
    """Parser for:
        show l2vpn forwarding bridge-domain mac-address location <location>
        show l2vpn forwarding bridge-domain <bridge_domain> mac-address location <location>
    """

    cli_command = [
        'show l2vpn forwarding bridge-domain mac-address location {location}',
        'show l2vpn forwarding bridge-domain {bridge_domain} mac-address location {location}']

    def cli(self, location, bridge_domain=None, output=None):
        if output is None:
            if bridge_domain:
                cmd = self.cli_command[1].format(
                    location=location, bridge_domain=bridge_domain)
            else:
                cmd = self.cli_command[0].format(location=location)

            out = self.device.execute(cmd)
        else:
            out = output

        # Mac Address Type Learned from/Filtered on LC learned Resync Age/Last
        # Change Mapped to
        p1 = re.compile(
            r'^Mac +Address +Type +Learned +from\/Filtered +on +LC +learned +Resync Age\/Last +Change +Mapped +to$')

        # 1.01.1 EVPN    BD id: 0                    N/A        N/A
        # N/A
        p2 = re.compile(
            r'^(?P<mac_address>\S+) +(?P<type>\S+) +BD +id: +(?P<bridge_domain>\d+)'
            ' +(?P<lc_learned>\S+) +(?P<resync_age>[\S\s]+) +(?P<mapped_to>\S+)$')

        # 3.3.5          dynamic BE1.2                       N/A        14 Mar 12:46:04        N/A
        # 0001.00ff.0002 dynamic Te0/0/1/0/3.3               N/A        0d 0h
        # 0m 14s           N/A
        p3 = re.compile(
            r'^(?P<mac_address>\S+) +(?P<type>\S+) +(?P<learned_from>[\w\/\.\d]+)'
            ' +(?P<lc_learned>\S+) +(?P<resync_age>[\S\s]+) +(?P<mapped_to>\S+)$')

        # 2.2.2          dynamic (10.25.40.40, 10007)        N/A        14 Mar
        # 12:46:04        N/A
        p4 = re.compile(
            r'^(?P<mac_address>\S+) +(?P<type>\w+) +(?P<learned_from>[\d\(\)\.\,\s]+)'
            ' +(?P<lc_learned>\S+) +(?P<resync_age>[\S\s]+) +(?P<mapped_to>\S+)$')

        # Init dict
        ret_dict = {}

        # Init vars
        start_parsing = False

        for line in out.splitlines():
            line = line.strip()

            if '------' in line or not line:
                continue

            # Mac Address Type Learned from/Filtered on LC learned Resync
            # Age/Last Change Mapped to
            m = p1.match(line)
            if m:
                start_parsing = True
                continue

            # 1.01.1 EVPN    BD id: 0                    N/A        N/A
            # N/A
            m = p2.match(line)
            if m and start_parsing:
                group = m.groupdict()

                mac_address = group['mac_address']
                learned_from = 'BD id:' + group['bridge_domain']
                final_dict = ret_dict.setdefault('mac_table', {}).setdefault(
                    learned_from, {}).setdefault('mac_address', {}).setdefault(
                    mac_address, {})

                keys_list = ['type', 'lc_learned', 'resync_age', 'mapped_to']
                for key in keys_list:
                    final_dict.update({key: group[key].strip()})
                final_dict.update({'learned_from': learned_from})
                continue

            # 3.3.5          dynamic BE1.2                       N/A        14 Mar 12:46:04        N/A
            # 0001.00ff.0002 dynamic Te0/0/1/0/3.3               N/A        0d
            # 0h 0m 14s           N/A
            m = p3.match(line)
            if m and start_parsing:
                group = m.groupdict()

                mac_address = group['mac_address']
                learned_from = group['learned_from']
                final_dict = ret_dict.setdefault('mac_table', {}).setdefault(
                    learned_from, {}).setdefault('mac_address', {}).setdefault(
                    mac_address, {})

                keys_list = [
                    'type',
                    'learned_from',
                    'lc_learned',
                    'resync_age',
                    'mapped_to']
                for key in keys_list:
                    final_dict.update({key: group[key].strip()})
                continue

            # 2.2.2          dynamic (10.25.40.40, 10007)        N/A        14
            # Mar 12:46:04        N/A
            m = p4.match(line)
            if m and start_parsing:
                group = m.groupdict()

                mac_address = group['mac_address']
                learned_from = group['learned_from'].strip()
                final_dict = ret_dict.setdefault('mac_table', {}).setdefault(
                    learned_from, {}).setdefault('mac_address', {}).setdefault(
                    mac_address, {})

                keys_list = [
                    'type',
                    'learned_from',
                    'lc_learned',
                    'resync_age',
                    'mapped_to']
                for key in keys_list:
                    final_dict.update({key: group[key].strip()})
                continue

        return ret_dict


# ================================================================================
# Parser for 'show l2vpn forwarding protection main-interface location {location}'
# ================================================================================


class ShowL2vpnForwardingProtectionMainInterfaceSchema(MetaParser):
    """Schema for:
        show l2vpn forwarding protection main-interface location {location}
    """

    schema = {
        'main_interface_id': {
            Any(): {
                'instance': {
                    Any(): {
                        'state': str,
                    },
                }
            },
        }
    }


class ShowL2vpnForwardingProtectionMainInterface(
    ShowL2vpnForwardingProtectionMainInterfaceSchema):
    """Parser for:
        show l2vpn forwarding protection main-interface location {location}
    """

    cli_command = [
        'show l2vpn forwarding protection main-interface location {location}']

    def cli(self, location, output=None):
        if output is None:
            cmd = self.cli_command[0].format(location=location)
            out = self.device.execute(cmd)
        else:
            out = output

        # Main Interface ID                Instance      State
        p1 = re.compile(r'^Main +Interface +ID +Instance +State$')

        # VFI:ves-vfi-1                    0          FORWARDING
        # PW:10.25.40.40,10001             0          FORWARDING
        p2 = re.compile(
            r'^(?P<main_interface_id>\S+) +(?P<instance>\d+) +(?P<state>\S+)$')

        # Init dict
        ret_dict = {}

        # Init vars
        start_parsing = False

        for line in out.splitlines():
            line = line.strip()

            if '------' in line or not line:
                continue

            # Main Interface ID                Instance      State
            m = p1.match(line)
            if m:
                start_parsing = True
                continue

            # VFI:ves-vfi-1                    0          FORWARDING
            # PW:10.25.40.40,10001             0          FORWARDING
            m = p2.match(line)
            if m and start_parsing:
                group = m.groupdict()

                main_interface_id = group['main_interface_id']
                instance = group['instance']
                state = group['state']
                ret_dict.setdefault(
                    'main_interface_id',
                    {}).setdefault(
                    main_interface_id,
                    {}).setdefault(
                    'instance',
                    {}).setdefault(
                    instance,
                    {}).setdefault(
                    'state',
                    state)
                continue

        return ret_dict


# ====================================
# Schema for 'show l2vpn bridge-domain'
# ====================================

class ShowL2vpnBridgeDomainSchema(MetaParser):
    """Schema for show l2vpn bridge-domain
    """
    schema = {
        'bridge_group': {
            Any(): {
                'bridge_domain': {
                    Any(): {
                        'id': int,
                        'state': str,
                        Optional('shg_id'): int,
                        Optional('mst_i'): int,
                        Optional('mac_aging_time'): int,
                        Optional('mac_limit'): int,
                        Optional('mac_limit_action'): str,
                        Optional('mac_limit_notification'): str,
                        Optional('filter_mac_address'): int,
                        'ac': {
                            'num_ac': int,
                            'num_ac_up': int,
                            Optional('interfaces'): {
                                Any(): {
                                    'state': str,
                                    Optional('static_mac_address'): int,
                                    Optional('bvi_mac_address'): int,
                                    Optional('mst_i'): int,
                                    Optional('mst_i_state'): str
                                }
                            }
                        },
                        Optional('vfi'): {
                            'num_vfi': int,
                            Any(): {
                                Optional('state'): str,
                                Optional('neighbor'): {
                                    Any(): {
                                        'pw_id': {
                                            Any(): {
                                                'state': str,
                                                'static_mac_address': int
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        'pw': {
                            'num_pw': int,
                            'num_pw_up': int,
                            Optional("neighbor"): {
                                Any(): {
                                    "pw_id": {
                                        Any(): {
                                            "state": str, 
                                            "static_mac_address": int
                                        }
                                    }
                                }
                            }
                        },
                        Optional('pbb'): {
                            'num_pbb': int,
                            'num_pbb_up': int,
                        },
                        Optional('vni'): {
                            'num_vni': int,
                            'num_vni_up': int,
                        },
                        Optional('evpn'): {
                            Any(): {
                                'state': str,
                            }
                        }
                    },
                }
            }
        }
    }


class ShowL2vpnBridgeDomain(ShowL2vpnBridgeDomainSchema):
    """Parser for show l2vpn bridge-domain"""

    cli_command = 'show l2vpn bridge-domain'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output        
        ret_dict = {}

        # Bridge group: g1, bridge-domain: bd1, id: 0, state: up, ShgId: 0, MSTi: 0
        # Bridge group: ev-Multicast, bridge-domain: ev-Multicast-TV, id: 1, state: up, ShgId: 0, MSTi: 0
        # Bridge group: a_b, bridge-domain: CD, id: 2, state: admin down (Shutdown), ShgId: 0, MSTi: 0
        p1 = re.compile(r'^Bridge +group: +(?P<bridge_group>\S+), +bridge\-domain: +'
            '(?P<bridge_domain>\S+), +id: +(?P<id>\d+), +state: +(?P<state>[\w\s\(\)]+), +'
            'ShgId: +(?P<shg_id>\d+), +MSTi: +(?P<mst_i>\d+)$')

        # Aging: 300 s, MAC limit: 4000, Action: none, Notification: syslog
        # Aging: 300 s, MAC limit: 100, Action: limit, no-flood, Notification: syslog, trap
        p2 = re.compile(r'^Aging: +(?P<mac_aging_time>\d+) s, +MAC +limit: +(?P<mac_limit>\d+), +'
                r'Action: +(?P<mac_limit_action>[\S ]+), +Notification: +'
                r'(?P<mac_limit_notification>[\S ]+)$')

        # Filter MAC addresses: 0
        p3 = re.compile(r'^Filter +MAC +addresses: +(?P<filter_mac_address>\d+)$')

        # ACs: 1 (1 up), VFIs: 1, PWs: 1 (1 up)
        p4 = re.compile(r'^ACs: +(?P<ac>\d+) +\((?P<ac_up>\d+) +up\), +VFIs: +(?P<vfi>\d+), +'
            'PWs: +(?P<pw>\d+) +\((?P<pw_up>\d+) +\w+\)(, +PBBs: +(?P<pbb>\d+)'
            ' +\((?P<pbb_up>\d+) +up\))?(, +VNIs: +(?P<vni>\d+) +\((?P<vni_up>\d+) +up\))?$')

        # Gi0/1/0/0, state: up, Static MAC addresses: 2, MSTi: 0 (unprotected)
        p5 = re.compile(r'^(?P<interface>\S+), +state: +(?P<state>\w+), +Static +'
            'MAC +addresses: +(?P<static_mac_address>\d+)(, +MSTi: +(?P<mst_i>\d+)'
            '( +\((?P<mst_i_state>\w+)\))?)?$')
        
        # BV100, state: up, BVI MAC addresses: 1
        p5_1 = re.compile(r'^(?P<interface>\S+), +state: +(?P<state>\w+), +BVI +'
            'MAC +addresses: +(?P<bvi_mac_address>\S+)$')

        # VFI 1
        # VFI vfi60 (up)
        # VFI string_LABEL_01 (up)
        p6 = re.compile(r'^VFI\s+(?P<vfi>\S+)(\s*(\((?P<state>[\w\s]+)\))?\s*)$')

        # Neighbor 10.1.1.1 pw-id 1, state: up, Static MAC addresses: 0
        p7 = re.compile(r'Neighbor +(?P<neighbor>\S+) +pw-id +(?P<pw_id>\d+), +state: +'
            '(?P<state>\w+), +Static +MAC +addresses: +(?P<static_mac_address>\d+)$')

        # g1/bd1                           0     up         1/1            1/1 
        p8 = re.compile(r'^(?P<bridge_group>\S+)\/(?P<bridge_domain_name>\S+) +(?P<id>\d+) +'
            '(?P<state>\w+) +(?P<ac>\d+)\/(?P<ac_up>\d+) +(?P<pw>\d+)\/(?P<pw_up>\d+)$')
        
        # EVPN, state: up
        p9 = re.compile(r'^(?P<evpn>\S+), +state: +(?P<state>\w+)$')
        
        for line in out.splitlines():
            line = line.strip()
            
            # Bridge group: g1, bridge-domain: bd1, id: 0, state: up, ShgId: 0, MSTi: 0
            # Bridge group: EVPN-Multicast, bridge-domain: EVPN-Multicast-BTV, id: 0, state: up, ShgId: 0, MSTi: 0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                bridge_group = group['bridge_group']
                bridge_domain = group['bridge_domain']
                id = int(group['id'])
                state = group['state']
                shg_id = int(group['shg_id'])
                mst_i = int(group['mst_i'])

                bridge_domain_dict = ret_dict.setdefault('bridge_group', {}). \
                    setdefault(bridge_group, {}). \
                    setdefault('bridge_domain', {}). \
                    setdefault(bridge_domain, {})

                bridge_domain_dict.update({'id': id})  
                bridge_domain_dict.update({'state': state}) 
                bridge_domain_dict.update({'shg_id': shg_id}) 
                bridge_domain_dict.update({'mst_i': mst_i}) 
                continue
            
            # Aging: 300 s, MAC limit: 4000, Action: none, Notification: syslog
            m = p2.match(line)
            if m:
                group = m.groupdict()
                for k,v in group.items():
                    bridge_domain_dict.update({k: int(v) if v.isdigit() else v})
                continue
            
            # Filter MAC addresses: 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                filter_mac_address = int(group['filter_mac_address'])
                bridge_domain_dict.update({'filter_mac_address': filter_mac_address})
                continue
                
            # ACs: 1 (1 up), VFIs: 1, PWs: 1 (1 up)
            m = p4.match(line)
            if m:
                group = m.groupdict()
                ac = int(group['ac'])
                ac_up = int(group['ac_up'])
                vfi = int(group['vfi'])
                pw = int(group['pw'])
                pw_up = int(group['pw_up'])
                
                ac_dict = bridge_domain_dict.setdefault('ac', {})
                ac_dict.update({'num_ac': ac})
                ac_dict.update({'num_ac_up': ac_up})

                vfi_dict = bridge_domain_dict.setdefault('vfi', {})
                vfi_dict.update({'num_vfi': vfi})

                pw_dict = bridge_domain_dict.setdefault('pw', {})
                pw_dict.update({'num_pw': pw})
                pw_dict.update({'num_pw_up': pw_up})

                pbb = group['pbb']
                pbb_up = group['pbb_up']
                if pbb:
                    pbb_dict = bridge_domain_dict.setdefault('pbb', {})
                    pbb_dict.update({'num_pbb': int(pbb)})
                    pbb_dict.update({'num_pbb_up': int(pbb_up)})

                vni = group['vni']
                vni_up = group['vni_up']
                if vni:
                    vni_dict = bridge_domain_dict.setdefault('vni', {})
                    vni_dict.update({'num_vni': int(vni)})
                    vni_dict.update({'num_vni_up': int(vni_up)})

                continue
            
            # Gi0/1/0/0, state: up, Static MAC addresses: 2, MSTi: 0 (unprotected)
            m = p5.match(line)
            if m:
                group = m.groupdict()
                interface = Common.convert_intf_name(group['interface'])
                state = group['state']
                static_mac_address = int(group['static_mac_address'])
                interface_dict = ac_dict.setdefault('interfaces', {}). \
                    setdefault(interface, {})
                interface_dict.update({'state': state})
                interface_dict.update({'static_mac_address': static_mac_address})
                if group['mst_i']:
                    mst_i = int(group['mst_i'])
                    interface_dict.update({'mst_i': mst_i})
                mst_i_state = group['mst_i_state']
                if mst_i_state:
                    interface_dict.update({'mst_i_state': mst_i_state})
                continue

            # BV100, state: up, BVI MAC addresses: 1
            m = p5_1.match(line)
            if m:
                group = m.groupdict()
                interface = Common.convert_intf_name(group['interface'])
                state = group['state']
                bvi_mac_address = int(group['bvi_mac_address'])

                interface_dict = ac_dict.setdefault('interfaces', {}). \
                    setdefault(interface, {})
                interface_dict.update({'state': state})
                interface_dict.update({'bvi_mac_address': bvi_mac_address})
                continue

            # VFI 1
            # VFI vfi60 (up)
            m = p6.match(line)
            if m:
                # clear state from earlier
                state = ''
                group = m.groupdict()
                vfi = group['vfi']
                vfi_dict = bridge_domain_dict.setdefault('vfi', {}). \
                    setdefault(vfi, {})
                if group['state']:   
                    state = group['state']
                if state:
                    vfi_dict.update({'state': state})
                continue

            # Neighbor 10.1.1.1 pw-id 1, state: up, Static MAC addresses: 0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                neighbor = group['neighbor']
                pw_id = int(group['pw_id'])
                state = group['state']
                static_mac_address = int(group['static_mac_address'])

                if vfi:
                    neighbor_dict = vfi_dict.setdefault('neighbor', {}). \
                        setdefault(neighbor, {}). \
                        setdefault('pw_id', {}). \
                        setdefault(pw_id, {})
                else:
                    neighbor_dict = pw_dict.setdefault('neighbor', {}). \
                        setdefault(neighbor, {}). \
                        setdefault('pw_id', {}). \
                        setdefault(pw_id, {})    

                neighbor_dict.update({'state': state})
                neighbor_dict.update({'static_mac_address': static_mac_address})
                continue

            # g1/bd1                           0     up         1/1            1/1 
            m = p8.match(line)
            if m:
                group = m.groupdict()
                bridge_group = group['bridge_group']
                bridge_domain = group['bridge_domain_name']
                bridge_domain_id = int(group['id'])
                state = group['state']
                ac = int(group['ac'])
                ac_up = int(group['ac_up'])
                pw = int(group['pw'])
                pw_up = int(group['pw_up'])

                bridge_domain_dict = ret_dict.setdefault('bridge_group', {}). \
                    setdefault(bridge_group, {}). \
                    setdefault('bridge_domain', {}). \
                    setdefault(bridge_domain, {})

                bridge_domain_dict.update({'id': bridge_domain_id})  
                bridge_domain_dict.update({'state': state})

                ac_dict = bridge_domain_dict.setdefault('ac', {})
                ac_dict.update({'num_ac': ac})
                ac_dict.update({'num_ac_up': ac_up})

                pw_dict = bridge_domain_dict.setdefault('pw', {})
                pw_dict.update({'num_pw': pw})
                pw_dict.update({'num_pw_up': pw_up})

                continue
            
            # EVPN, state: up
            m = p9.match(line)
            if m:
                group = m.groupdict()
                evpn = group['evpn']
                evpn_state = group['state']
                evpn_dict = bridge_domain_dict.setdefault('evpn', {}). \
                                setdefault(evpn, {})
                evpn_dict.update({'state': state})
                continue

        return ret_dict


# =================================================
# Parser for:
#   * 'show l2vpn bridge-domain brief'
# =================================================
class ShowL2vpnBridgeDomainBriefSchema(MetaParser):
    schema = {
        'bridge_group': {
            Any(): {
                'bridge_domain': {
                    Any(): {
                        'id': int,
                        'state': str,
                        'ac': {
                            'num_ac': int,
                            'num_ac_up': int
                        },
                        'pw': {
                            'num_pw': int,
                            'num_pw_up': int
                        },
                        Optional('pbb'): {
                            'num_pbb': int,
                            'num_pbb_up': int
                        },
                        Optional('vni'): {
                            'num_vni': int,
                            'num_vni_up': int
                        }
                    }
                }
            }
        }
    }


# =====================================================
# Parser for:
#   * 'show l2vpn bridge-domain brief'
# =====================================================
class ShowL2vpnBridgeDomainBrief(ShowL2vpnBridgeDomainBriefSchema):
    """Parser class for 'show l2vpn bridge-domain brief'"""

    cli_command = 'show l2vpn bridge-domain brief'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output

        # Bridge Group/Bridge-Domain
        # Bridge Group:Bridge-Domain Name  ID    State          Num ACs/up   Num PWs/up    Num PBBs/up Num VNIs/up
        # g1/bd1                           0     up         1/1            1/1
        # G-t:BDA                  1     up             3/2          3/2           0/0         0/0
        # g_D:a1                     2     admin down     1/0          1/0           0/0         0/0
        p1 = re.compile(r"^(?P<group>([\w\-]+))(?:\:|\/)(?P<domain>([\w\-]+)) "
                        r"+(?P<id>([\d]+)) +(?P<state>(\S+(?: \S+)?)) "
                        r"+(?P<acs>([\d]+))\/(?P<acup>([\d]+)) "
                        r"+(?P<pws>([\d]+))\/(?P<pwup>([\d]+))(?: "
                        r"+(?P<pbbs>([\d]+))\/(?P<pbbup>([\d]+)) "
                        r"+(?P<vnis>([\d]+))\/(?P<vniup>([\d]+)))?$")
        # regex only takes values from under the table headers. Table headers static, so no regex needed.

        ret_dict = {}
        for line in out.splitlines():
            line = line.strip()

            m = p1.match(line)
            if m:
                bridge_dict = ret_dict.setdefault('bridge_group', {}).setdefault(m.groupdict()['group'], {}). \
                    setdefault('bridge_domain', {}).setdefault(m.groupdict()['domain'], {})

                bridge_dict.update({'id': int(m.groupdict()['id'])})
                bridge_dict.update({'state': m.groupdict()['state']})

                ac_dict = bridge_dict.setdefault('ac', {})
                ac_dict.update({'num_ac': int(m.groupdict()['acs'])})
                ac_dict.update({'num_ac_up': int(m.groupdict()['acup'])})

                pw_dict = bridge_dict.setdefault('pw', {})
                pw_dict.update({'num_pw': int(m.groupdict()['pws'])})
                pw_dict.update({'num_pw_up': int(m.groupdict()['pwup'])})

                if m.groupdict()['pbbs'] and m.groupdict()['pbbup']:
                    pbb_dict = bridge_dict.setdefault('pbb', {})
                    pbb_dict.update({'num_pbb': int(m.groupdict()['pbbs'])})
                    pbb_dict.update({'num_pbb_up': int(m.groupdict()['pbbup'])})

                if m.groupdict()['vnis'] and m.groupdict()['vniup']:
                    vni_dict = bridge_dict.setdefault('vni', {})
                    vni_dict.update({'num_vni': int(m.groupdict()['vnis'])})
                    vni_dict.update({'num_vni_up': int(m.groupdict()['vniup'])})

        return ret_dict


# =============================================
# Schema for 'show l2vpn bridge-domain summary'
# =============================================
class ShowL2vpnBridgeDomainSummarySchema(MetaParser):
    """Schema for show l2vpn bridge-domain summary
    """
    schema = {
        'number_of_groups': int,
        'bridge_domains': {
            'total': int,
            'up': int,
            'shutdown': int,
        },
        'ac': {
            'total': int,
            'up': int,
            'down': int,
        },
        'pw': {
            'total': int,
            'up': int,
            'down': int,
        }
    }

class ShowL2vpnBridgeDomainSummary(ShowL2vpnBridgeDomainSummarySchema):
    """Parser for show l2vpn bridge-domain summary"""

    cli_command = 'show l2vpn bridge-domain summary'
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        ret_dict = {}

        # Number of groups: 1, bridge-domains: 1, Up: 1, Shutdown: 0
        p1 = re.compile(r'^Number +of +groups: +(?P<number_of_groups>\d+), +'
            'bridge-domains: +(?P<bridge_domains>\d+), +Up: +(?P<up>\d+), +Shutdown: +'
            '(?P<shutdown>\d+)$')
        
        # Number of ACs: 1 Up: 1, Down: 0
        p2 = re.compile(r'^Number +of +ACs: +(?P<ac>\d+) +Up: +(?P<up>\d+), +Down: +'
            '(?P<down>\d+)$')
        
        # Number of PWs: 1 Up: 1, Down: 0
        p3 = re.compile(r'^Number +of +PWs: +(?P<pw>\d+) +Up: +(?P<up>\d+), +Down: +'
            '(?P<down>\d+)$')

        for line in out.splitlines():
            line = line.strip()

            # Number of groups: 1, bridge-domains: 1, Up: 1, Shutdown: 0
            m = p1.match(line)
            if m:
                group = m.groupdict()
                number_of_groups = int(group['number_of_groups'])
                bridge_domains = int(group['bridge_domains'])
                up = int(group['up'])
                shutdown = int(group['shutdown'])
                ret_dict.update({'number_of_groups': number_of_groups})
                bridge_domains_dict = ret_dict.setdefault('bridge_domains', {})
                bridge_domains_dict.update({'total': bridge_domains})
                bridge_domains_dict.update({'up': up})
                bridge_domains_dict.update({'shutdown': shutdown})
                continue
            
            # Number of ACs: 1 Up: 1, Down: 0
            m = p2.match(line)
            if m:
                group = m.groupdict()
                ac = int(group['ac'])
                up = int(group['up'])
                down = int(group['down'])
                ac_dict = ret_dict.setdefault('ac', {})
                ac_dict.update({'total': ac})
                ac_dict.update({'up': up})
                ac_dict.update({'down': down})
                continue
            
            # Number of PWs: 1 Up: 1, Down: 0
            m = p3.match(line)
            if m:
                group = m.groupdict()
                pw = int(group['pw'])
                up = int(group['up'])
                down = int(group['down'])
                pw_dict = ret_dict.setdefault('pw', {})
                pw_dict.update({'total': ac})
                pw_dict.update({'up': up})
                pw_dict.update({'down': down})
                continue

        return ret_dict

# =============================================
# Schema for 'show l2vpn bridge-domain detail'
# =============================================

class ShowL2vpnBridgeDomainDetailSchema(MetaParser):
    """Schema for show l2vpn bridge-domain detail
    """
    schema = {
        Optional('legend'): str,
        'bridge_group': {
            Any(): {
                'bridge_domain': {
                    Any(): {
                        'id': int,
                        'state': str,
                        'shg_id': int,
                        Optional('mode'): str,
                        Optional('mst_i'): int,
                        Optional('mac_learning'): str,
                        Optional('mac_withdraw'): str,
                        Optional('flooding'): {
                            'broadcast_multicast': str,
                            'unknown_unicast': str
                        },
                        Optional('multicast_source'): str,
                        Optional('mac_aging_time'): int,
                        Optional('mac_aging_type'): str,
                        Optional('mac_limit'): int,
                        Optional('mac_limit_action'): str,
                        Optional('mac_limit_notification'): str,
                        Optional('mac_limit_reached'): str,
                        Optional('mac_port_down_flush'): str,
                        Optional('mac_withdraw_sent_on'): str,
                        Optional('mac_secure'): str,
                        Optional('mac_withdraw_relaying'): str,
                        Optional('mac_withdraw_for_access_pw'): str,
                        Optional('mac_secure_logging'): str,
                        Optional('dynamic_arp_inspection'): str,
                        Optional('dynamic_arp_logging'): str,
                        Optional('ip_source_logging'): str,
                        Optional('coupled_state'): str,
                        Optional('security'): str,
                        Optional('dhcp_v4_snooping'): str,
                        Optional('dhcp_v4_snooping_profile'): str,
                        Optional('igmp_snooping'): str,
                        Optional('igmp_snooping_profile'): str,
                        Optional('mld_snooping_profile'): str,
                        Optional('mac_limit_threshold'): str,
                        Optional('mid_cvpls_config_index'): str,
                        Optional('p2mp_pw'): str,
                        Optional('mtu'): int,
                        Optional('bridge_mtu'): str,
                        Optional('filter_mac_address'): int,
                        Optional('storm_control'): str,
                        Optional('ip_source_guard'): str,
                        Optional('create_time'): str,
                        Optional('split_horizon_group'): str,
                        Optional('vine_state'): str,
                        Optional('status_changed_since_creation'): str,
                        'ac': {
                            'num_ac': int,
                            'num_ac_up': int,
                            Optional('interfaces'): {
                                Any(): {
                                    'state': str,
                                    'type': str,
                                    Optional('vlan_num_ranges'): str,
                                    Optional('mac_aging_type'): str,
                                    Optional('mtu'): int,
                                    'xc_id': str,
                                    Optional('interworking'): str,
                                    Optional('mst_i'): int,
                                    Optional('mst_i_state'): str,
                                    Optional('mac_learning'): str,
                                    Optional('flooding'): {
                                        'broadcast_multicast': str,
                                        'unknown_unicast': str
                                    },
                                    Optional('error'): str,
                                    Optional('bvi_mac_address'): list,
                                    Optional('virtual_mac_address'): list,
                                    Optional('mac_aging_time'): int,
                                    Optional('mac_limit'): int,
                                    Optional('mac_limit_action'): str,
                                    Optional('mac_limit_notification'): str,
                                    Optional('mac_limit_reached'): str,
                                    Optional('security'): str,
                                    Optional('dhcp_v4_snooping'): str,
                                    Optional('dhcp_v4_snooping_profile'): str,
                                    Optional('igmp_snooping'): str,
                                    Optional('igmp_snooping_profile'): str,
                                    Optional('mld_snooping_profile'): str,
                                    Optional('mac_limit_threshold'): str,
                                    Optional('static_mac_address'): list,
                                    Optional('split_horizon_group'): str,
                                    Optional('statistics'): {
                                        'packet_totals': {
                                            'receive': int,
                                            'send': int,
                                        },
                                        'byte_totals': {
                                            'receive': int,
                                            'send': int,
                                        },
                                        Optional('mac_move'): str,
                                    },
                                    Optional('vlan_ranges'): list,
                                    Optional('rewrite_tags'): str,
                                    Optional('storm_control_drop_counters'): {
                                        'packets': {
                                            'broadcast': str,
                                            'multicast': str,
                                            'unknown_unicast': str,
                                        },
                                        'bytes': {
                                            'broadcast': str,
                                            'multicast': str,
                                            'unknown_unicast': str,
                                        },
                                    },
                                    Optional('dynamic_arp_inspection_drop_counters'): {
                                        'packets': str,
                                        'bytes': str,
                                    },
                                    Optional('ip_source_guard_drop_counters'): {
                                        'packets': str,
                                        'bytes': str,
                                    },
                                    Optional('pd_system_data'): {
                                        Any(): Any()
                                    }
                                }
                            }
                        },
                        Optional('vfi'): {
                            'num_vfi': int,
                            Any(): {
                                Optional('state'): str,
                                'neighbor': {
                                    Any(): {
                                        'pw_id': {
                                            Any(): {
                                                'state': str,
                                                'pw_class': str,
                                                Optional('xc_id'): str,
                                                'encapsulation': str,
                                                'protocol': str,
                                                'pw_type': str,
                                                'control_word': str,
                                                'interworking': str,
                                                Optional('pw_backup_disable_delay'): int,
                                                'sequencing': str,
                                                Optional('mpls'): {
                                                    Any(): {
                                                        'local': str,
                                                        'remote': str,
                                                        Optional('remote_type'): list,
                                                        Optional('local_type'): list
                                                    }
                                                },
                                                Optional('lsp'): {
                                                    'state': str,
                                                    Optional('pw'): {
                                                        'load_balance': {
                                                            'local': str,
                                                            'remote': str
                                                        },
                                                        'pw_status_tlv': {
                                                            'local': str,
                                                            'remote': str
                                                        }
                                                    },
                                                    Optional('mpls'): {
                                                        Any(): {
                                                            'local': str,
                                                            'remote': str,
                                                            Optional('remote_type'): list,
                                                            Optional('local_type'): list
                                                        }
                                                    }
                                                },
                                                Optional('status_code'): str,
                                                'create_time': str,
                                                'last_time_status_changed': str,
                                                Optional('mac_withdraw_message'): {
                                                    'send': int,
                                                    'receive': int,
                                                },
                                                Optional('static_mac_address'): list,
                                                Optional('statistics'): {
                                                    'packet_totals': {
                                                        'receive': int,
                                                        'send': int,
                                                    },
                                                    'byte_totals': {
                                                        'receive': int,
                                                        'send': int,
                                                    },
                                                    Optional('mac_move'): str,
                                                },
                                                Optional('dhcp_v4_snooping'): str,
                                                Optional('dhcp_v4_snooping_profile'): str,
                                                Optional('igmp_snooping'): str,
                                                Optional('igmp_snooping_profile'): str,
                                                Optional('mld_snooping_profile'): str,
                                                Optional('source_address'): str,
                                                Optional('forward_class'): str,
                                                Optional('storm_control'): str,
                                                Optional('storm_control_drop_counters'): {
                                                    'packets': {
                                                        'broadcast': str,
                                                        'multicast': str,
                                                        'unknown_unicast': str,
                                                    },
                                                    'bytes': {
                                                        'broadcast': str,
                                                        'multicast': str,
                                                        'unknown_unicast': str,
                                                    },
                                                },
                                                Optional('flooding'): {
                                                    'broadcast_multicast': str,
                                                    'unknown_unicast': str
                                                },
                                                Optional('mac_aging_time'): int,
                                                Optional('mac_aging_type'): str,
                                                Optional('mac_limit'): int,
                                                Optional('mac_limit_action'): str,
                                                Optional('mac_limit_notification'): str,
                                                Optional('mac_secure'): str,
                                                Optional('mac_learning'): str,
                                                Optional('mac_limit_reached'): str,
                                                Optional('mac_secure_logging'): str,
                                                Optional('mac_port_down_flush'): str,
                                                Optional('mac_limit_threshold'): str,
                                                Optional('split_horizon_group'): str,
                                            }
                                        }
                                    }
                                },
                                Optional('statistics'): {
                                    'drop': {
                                        'illegal_vlan': int,
                                        'illegal_length': int 
                                    },
                                },
                            }
                        },
                        Optional('access_pw'): {
                            Any(): {
                                'neighbor': {
                                    Any(): {
                                        'pw_id': {
                                            Any(): {
                                                'ac_id': str,
                                                'state': str,
                                                'xc_id': str,
                                                'encapsulation': str,
                                                'source_address': str,
                                                'encap_type': str,
                                                'control_word': str,
                                                'sequencing': str,
                                                Optional('lsp'): {
                                                    'state': str,
                                                    'evpn': {
                                                        Any(): {
                                                            'local': str,
                                                            'remote': str,
                                                            Optional('remote_type'): list,
                                                            Optional('local_type'): list
                                                        }
                                                    },
                                                    Optional('mpls'): {
                                                        Any(): {
                                                            'local': str,
                                                            'remote': str,
                                                            Optional('remote_type'): list,
                                                            Optional('local_type'): list
                                                        }
                                                    }
                                                },
                                                Optional('status_code'): str,
                                                'create_time': str,
                                                'last_time_status_changed': str,
                                                Optional('mac_withdraw_message'): {
                                                    'send': int,
                                                    'receive': int,
                                                },
                                                Optional('mac_learning'): str,
                                                Optional('flooding'): {
                                                    'broadcast_multicast': str,
                                                    'unknown_unicast': str
                                                },
                                                Optional('error'): str,
                                                Optional('bvi_mac_address'): list,
                                                Optional('mac_aging_type'): str,
                                                Optional('mac_aging_time'): int,
                                                Optional('mac_limit'): int,
                                                Optional('mac_limit_action'): str,
                                                Optional('mac_limit_notification'): str,
                                                Optional('mac_limit_reached'): str,
                                                Optional('mac_secure_logging'): str,
                                                Optional('mac_secure'): str,
                                                Optional('mac_port_down_flush'): str,
                                                Optional('dhcp_v4_snooping'): str,
                                                Optional('dhcp_v4_snooping_profile'): str,
                                                Optional('igmp_snooping'): str,
                                                Optional('igmp_snooping_profile'): str,
                                                Optional('mld_snooping_profile'): str,
                                                Optional('mac_limit_threshold'): str,
                                                Optional('static_mac_address'): list,
                                                Optional('statistics'): {
                                                    'packet_totals': {
                                                        'receive': int,
                                                        'send': int,
                                                    },
                                                    'byte_totals': {
                                                        'receive': int,
                                                        'send': int,
                                                    },
                                                    Optional('mac_move'): str,
                                                },
                                                Optional('dhcp_v4_snooping'): str,
                                                Optional('dhcp_v4_snooping_profile'): str,
                                                Optional('igmp_snooping'): str,
                                                Optional('igmp_snooping_profile'): str,
                                                Optional('mld_snooping_profile'): str,
                                                Optional('storm_control'): str,
                                                Optional('split_horizon_group'): str,
                                                Optional('forward_class'): str,
                                            }
                                        }
                                    }
                                }
                            }
                        },
                        'pw': {
                            'num_pw': int,
                            'num_pw_up': int,
                        },
                        Optional('pbb'): {
                            'num_pbb': int,
                            'num_pbb_up': int,
                        },
                        Optional('vni'): {
                            'num_vni': int,
                            'num_vni_up': int,
                        },
                        Optional('evpn'): {
                            Any(): {
                                'state': str,
                                'evi': str,
                                'xc_id': str,
                                Optional('statistics'): {
                                    'packet_totals': {
                                        'receive': int,
                                        'send': int,
                                    },
                                    'byte_totals': {
                                        'receive': int,
                                        'send': int,
                                    },
                                    Optional('mac_move'): str,
                                },
                            }
                        }
                    },
                }
            }
        }
    }


class ShowL2vpnBridgeDomainDetail(ShowL2vpnBridgeDomainDetailSchema):
    """Parser for show l2vpn bridge-domain detail"""

    cli_command = 'show l2vpn bridge-domain detail'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        
        ret_dict = {}
        vfi_obj_dict = {}
        interface_found = False
        label_found = False
        
        # Bridge group: g1, bridge-domain: bd1, id: 0, state: up, ShgId: 0, MSTi: 0
        # Bridge group: EVPN-Multicast, bridge-domain: EVPN-Multicast-BTV, id: 0, state: up, ShgId: 0, MSTi: 0
        p1 = re.compile(r'^Bridge +group: +(?P<bridge_group>\S+), +bridge\-domain: +'
                        r'(?P<bridge_domain>\S+), +id: +(?P<id>\d+), +state: +(?P<state>\w+), +'
                        r'ShgId: +(?P<shg_id>\d+)(, +MSTi: +(?P<mst_i>\d+))?$')
        
        # VPWS Mode
        p1_1 = re.compile(r'^(?P<mode>\S+) +Mode$')
        
        # MAC learning: enabled
        p2 = re.compile(r'^MAC +learning: +(?P<mac_learning>\S+)$')

        # MAC withdraw: disabled
        p3 = re.compile(r'^MAC +withdraw: +(?P<mac_withdraw>\S+)$')

        # Flooding:
        p4 = re.compile(r'^Flooding:$')

        # Broadcast & Multicast: enabled
        p5 = re.compile(r'^Broadcast +& +Multicast: +(?P<enabled>\S+)$')

        # Unknown unicast: enabled
        p6 = re.compile(r'^Unknown +unicast: +(?P<enabled>\S+)$')

        # MAC aging time: 300 s, Type: inactivity
        p7 = re.compile(r'^MAC +aging +time: +(?P<mac_aging_time>\d+) +s, +Type: +(?P<mac_aging_type>\S+)$')

        # MAC limit: 4000, Action: none, Notification: syslog
        p8 = re.compile(r'^MAC +limit: +(?P<mac_limit>\d+), +Action: +(?P<action>\S+),'
                        r' +Notification: +(?P<notification>\S+)$')

        # MAC limit reached: yes
        # MAC limit reached: no, threshold: 75%
        p9 = re.compile(r'^MAC +limit +reached: +(?P<mac_limit_reached>\S+)'
                        r'(, +threshold: +(?P<threshold>\S+))?$')

        # Security: disabled
        p10 = re.compile(r'^Security: +(?P<security>\S+)$')

        # DHCPv4 snooping: disabled
        # DHCPv4 Snooping: disabled
        p11 = re.compile(r'^DHCPv4 +(s|S)nooping: +(?P<dhcp_v4_snooping>\S+)$')

        # DHCPv4 Snooping profile: none
        p11_1 = re.compile(r'^DHCPv4 +(s|S)nooping profile: +(?P<dhcp_v4_snooping_profile>\S+)$')

        # IGMP Snooping: disabled
        p11_2 = re.compile(r'IGMP +(s|S)nooping: +(?P<igmp_snooping>\S+)$')

        # IGMP Snooping profile: none
        p11_3 = re.compile(r'^IGMP +(s|S)nooping profile: +(?P<igmp_snooping_profile>\S+)$')

        # MLD Snooping profile: none
        p11_4 = re.compile(r'^MLD +(s|S)nooping profile: +(?P<mld_snooping_profile>\S+)$')
        
        # MTU: 1500
        p12 = re.compile(r'^MTU: +(?P<mtu>\d+)$')

        # Filter MAC addresses:
        p13 = re.compile(r'^Filter +MAC +addresses:( +(?P<filter_mac_addresses>\d+))?$')

        # ACs: 1 (1 up), VFIs: 1, PWs: 1 (1 up)
        # ACs: 3 (2 up), VFIs: 0, PWs: 0 (0 up), PBBs: 0 (0 up), VNIs: 0 (0 up)
        p14 = re.compile(r'^ACs: +(?P<ac>\d+) +\((?P<ac_up>\d+) +up\), +VFIs: +(?P<vfi>\d+), +'
                         r'PWs: +(?P<pw>\d+) +\((?P<pw_up>\d+) +up\)(, +PBBs: +(?P<pbb>\d+) +\('
                         r'(?P<pbb_up>\d+) +up\))?(, +VNIs: +(?P<vni>\d+) +\((?P<vni_up>\d+) +up\))?$')

        # List of ACs:
        p15 = re.compile(r'^List +of +ACs:$')

        # AC: GigabitEthernet0/1/0/0, state is up
        # AC: GigabitEthernet0/5/1/4, state is admin down
        p16 = re.compile(r'^AC: +(?P<interface>\S+), +state +is +(?P<state>[\S ]+)$')

        # Type Ethernet
        # Type VLAN; Num Ranges: 1
        p17 = re.compile(r'^Type +(?P<type>\S+)(; +Num +Ranges: +(?P<num_ranges>\d+))?$')

        # MTU 1500; XC ID 0x2000001; interworking none; MSTi 0 (unprotected)
        # MTU 1514; XC ID 0x8000000b; interworking none
        # MTU 9202; XC ID 0xc0000002; interworking none; MSTi 5
        p18 = re.compile(r'^MTU +(?P<mtu>\d+); +XC +ID +(?P<xc_id>\S+); +interworking +'
                        r'(?P<interworking>\S+)(; +MSTi +(?P<mst_i>\d+))?( +\((?P<mst_i_state>\w+)\))?$')

        # Type Ethernet      MTU 1500; XC ID 1; interworking none
        p18_1 = re.compile(r'Type +(?P<pw_type>\S+) +MTU +(?P<mtu>\d+); +XC +ID +(?P<xc_id>\d+);'
                            r' +interworking +(?P<interworking>\S+)$')
        
        # 0000.0000.0000
        p19 = re.compile(r'(?P<static_mac_address>[a-zA-Z\d\.]+)$')

        # Statistics:
        p20 = re.compile(r'Statistics:')

        # packet totals: receive 3919680,send 9328
        # packets: received 0 (unicast 0), sent 0
        p21 = re.compile(r'packet(s)?( +totals)?: +receive(d)? +(?P<receive>\d+)( +\(( *multicast +'
                        r'(?P<multicast>\d+),?)?( *broadcast +(?P<broadcast>\d+),?)?( *unknown +'
                        r'unicast +(?P<unknown_unicast>\d+),?)? *unicast +(?P<unicast>\d+)\))?, '
                        r'*sen(d|t) +(?P<send>\d+)$')

        # byte totals: receive 305735040,send 15022146
        # bytes: received 0 (unicast 0), sent 0
        p22 = re.compile(r'byte(s)?( +totals)?: +receive(d)? +(?P<receive>\d+)( +\(( *multicast +'
                        r'(?P<multicast>\d+),?)?( *broadcast +(?P<broadcast>\d+),?)?( *unknown +'
                        r'unicast +(?P<unknown_unicast>\d+),?)? *unicast +(?P<unicast>\d+)\))?, '
                        r'*sen(d|t) +(?P<send>\d+)$')

        # List of Access PWs:
        p23 = re.compile(r'^List +of +Access +PWs:$')

        # List of VFIs:
        p24 = re.compile(r'^List +of +VFIs:$')

        # VFI 1
        # VFI vfi100 (up)
        p25 = re.compile(r'^VFI +(?P<vfi>\S+)( +\((?P<state>\w+)\))?$')

        # PW: neighbor 10.4.1.1, PW ID 1, state is up ( established )
        p26 = re.compile(r'^PW: +neighbor +(?P<neighbor>\S+), +PW +ID +(?P<pw_id>\d+), +state +'
                        r'is +(?P<state>[\S ]+)$')

        # PW class mpls, XC ID 0xff000001
        p27 = re.compile(r'^PW +class +(?P<pw_class>\w+), +XC +ID +(?P<xc_id>\S+)$')

        # PW class not set
        p27_1 = re.compile(r'^PW +class +(?P<pw_class>[\S ]+)$')

        # Encapsulation MPLS, protocol LDP
        p28 = re.compile(r'^Encapsulation +(?P<encapsulation>\S+)(, +protocol +(?P<protocol>\S+))?$')

        # PW type Ethernet, control word disabled, interworking none
        p29 = re.compile(r'^(?P<type>PW|Encap) +type +(?P<pw_type>\S+), +control +word +(?P<control_word>\S+)(, +interworking +(?P<interworking>\S+))?$')

        # PW backup disable delay 0 sec
        p30 = re.compile(r'PW +backup +disable +delay +(?P<delay>\d+) +sec$')

        # Sequencing not set
        p31 = re.compile(r'Sequencing +(?P<sequencing>[\S ]+)$')

        # MPLS         Local                          Remote
        # EVPN         Local                          Remote
        p32 = re.compile(r'^(?P<type>MPLS|EVPN) +Local +Remote$')

        # Label        30005                          unknown
        # Group ID     0x5000300                      0x0
        # VCCV CV type 0x2                            0x0
        # Avoid show commands: show l2vpn xconnect detail
        # Avoid Date and Time: Wed Sep 25 20:09:36.362 UTC
        p33 = re.compile(r'^(?P<mpls>.{1,12}\S) +(?P<local>.+\S) +(?P<remote>.+)$')

        # (control word)                 (control word)
        # (router alert label)           (router alert label)
        p33_1 = re.compile(r'^\((?P<local>.+)(\) +\()(?P<remote>.+)\)$')

        # ------------ ------------------------------ -----------------------------
        p34 = re.compile(r'^-+ +-+ +-+$')

        # Create time: 12/03/2008 14:03:00 (17:17:30 ago)
        p36 = re.compile(r'Create +time: +(?P<create_time>[\S ]+)$')

        # Last time status changed: 13/03/2008 05:57:58 (01:22:31 ago)
        p37 = re.compile(r'Last +time +status +changed: +(?P<last_time_status_changed>[\S ]+)$')

        # MAC withdraw message: send 0 receive 0
        p38 = re.compile(r'^MAC +withdraw +message(s)?: +sen(d|t) +(?P<send>\d+),? +receive(d)? +(?P<receive>\d+)$')

        # Static MAC addresses:
        p39 = re.compile(r'Static +MAC +addresses:$')

        # VFI Statistics:
        p40 = re.compile(r'VFI +Statistics:$')

        # drops: illegal VLAN 0, illegal length 0
        p41 = re.compile(r'drops: +(?P<drops>\S+) VLAN +(?P<vlan>\d+), +illegal +length '
                        r'+(?P<illegal_length>\d+)$')

        # (control word)                 (control word)  
        p42 = re.compile(r'^\([\S ]+\)$')

        # Mon Oct  7 16:18:59.168 EDT
        p43 = re.compile(r'^[Wed|Thu|Fri|Sat|Sun|Mon|Tue]+ +'
                        r'[Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec]+ +'
                        r'\d{1,2} +\d{1,2}:\d{1,2}:\d{1,2}[\.]\d{1,3} +[A-Z]{3}')

        # Legend: pp = Partially Programmed.
        p44 = re.compile(r'^Legend: +(?P<legend>[\S ]+)$')

        # Coupled state: disabled
        p45 = re.compile(r'^Coupled +state: +(?P<coupled_state>\S+)$')

        # VINE state: EVPN-IRB
        p46 = re.compile(r'^VINE +state: +(?P<vine_state>\S+)')

        # MAC withdraw for Access PW: enabled
        p47 = re.compile(r'^MAC +withdraw +for +Access +PW: +(?P<mac_withdraw_for_access_pw>\S+)$')

        # MAC withdraw sent on: bridge port up
        p48 = re.compile(r'^MAC +withdraw +sent +on: +(?P<mac_withdraw_sent_on>[\S ]+)$')

        # MAC withdraw relaying (access to access): disabled
        p49 = re.compile(r'^MAC +withdraw +relaying \(access +to +access\): +(?P<mac_withdraw_relaying>[\S ]+)$')

        # MAC port down flush: enabled
        p50 = re.compile(r'^MAC +port +down +flush: +(?P<mac_port_down_flush>\S+)$')

        #  MAC Secure: disabled, Logging: disabled
        p51 = re.compile(r'^MAC +Secure: +(?P<mac_secure>\w+), +Logging: +(?P<mac_secure_logging>\w+)$')

        # Split Horizon Group: none
        p52 = re.compile(r'^Split +Horizon +Group: +(?P<split_horizon_group>\S+)$')

        # Dynamic ARP Inspection: disabled, Logging: disabled
        p53 = re.compile(r'^Dynamic +ARP +Inspection: +(?P<dynamic_arp_inspection>\w+), +Logging'
                        r': +(?P<dynamic_arp_logging>\w+)$')

        # IP Source Guard: disabled, Logging: disabled
        p54 = re.compile(r'^IP +Source +Guard: +(?P<ip_source_guard>\w+), +Logging: +(?P<ip_source_logging>\w+)$')

        # Storm Control: disabled
        # Storm Control: bridge-domain policer
        p56 = re.compile(r'^Storm +Control: +(?P<storm_control>[\S ]+)$')

        # Bridge MTU: 1500
        p57 = re.compile(r'^Bridge +MTU: +(?P<bridge_mtu>\S+)$')

        # MIB cvplsConfigIndex: 1
        p58 = re.compile(r'^MIB +cvplsConfigIndex: (?P<mid_cvpls_config_index>\d+)$')

        # P2MP PW: disabled
        p59 = re.compile(r'^P2MP +PW: +(?P<p2mp_pw>\S+)$')

        # No status change since creation
        p60 = re.compile(r'^No +status +change +since +creation$')

        # List of EVPNs:
        p61 = re.compile(r'^List +of +EVPNs:$')

        # EVPN, state: up
        p62 = re.compile(r'^(?P<evpn>\S+), +state: +(?P<state>\S+)$')

        # evi: 1000
        p63 = re.compile(r'^evi: +(?P<evi>\d+)$')

        # XC ID 0x80000009
        p64 = re.compile(r'^XC +ID (?P<xc_id>\S+)$')

        # MAC move: 0
        p65 = re.compile(r'^MAC +move: +(?P<mac_move>\d+)$')

        # BVI MAC address:
        p66 = re.compile(r'^BVI +MAC +address:$')

        # 1000.10ff.1000
        p67 = re.compile(r'^(?P<bvi_mac_address>\w+\.\w+\.\w+)$')

        # Rewrite Tags: []
        p68 = re.compile(r'^Rewrite +Tags: +\[(?P<rewrite_tags>\S+)?\]$')

        # VLAN ranges: [100, 100]
        p69 = re.compile(r'^VLAN +ranges: +\[(?P<vlan_ranges>[\S ]+)?\]$')

        # Storm control drop counters:
        p70 = re.compile(r'^Storm +control +drop +counters:$')

        # packets: broadcast 0, multicast 0, unknown unicast 0
        p71 = re.compile(r'^packets: +broadcast +(?P<broadcast>\d+), +multicast +(?P<multicast>\d+)'
                        r', +unknown +unicast +(?P<unknown_unicast>\d+)$')

        # bytes: broadcast 0, multicast 0, unknown unicast 0
        p72 = re.compile(r'^bytes: +broadcast +(?P<broadcast>\d+), +multicast +(?P<multicast>\d+),'
                        r' +unknown +unicast +(?P<unknown_unicast>\d+)$')

        # Dynamic ARP inspection drop counters:
        p73 = re.compile(r'^Dynamic +ARP +inspection +drop +counters:$')

        # packets: 0, bytes: 0
        p74 = re.compile(r'^packets: +(?P<packets>\d+), +bytes: +(?P<bytes>\d+)$')

        # IP source guard drop counters:
        p75 = re.compile(r'^IP +source +guard +drop +counters:$')

        # List of Access VFIs:
        p76 = re.compile(r'^List +of +Access +VFIs:$')

        # Error: Need at least 1 bridge port up
        p77 = re.compile(r'^Error: +(?P<error>[\S ]+)$')

        # EVPN: neighbor 0.0.0.0, PW ID: evi 601, ac-id 1, state is down ( local ready ) (Transport LSP Down)
        p78 = re.compile(r'^(?P<type>EVPN): neighbor +(?P<neighbor>\S+), +PW +ID: +(?P<pw_id>evi +\d+), +ac-id +(?P<ac_id>\d+), +state +is +(?P<state>[\S ]+)$')

        # Source address 10.154.219.85
        p79 = re.compile(r'^Source +address +(?P<source_address>\S+)$')

        # LSP : Up
        p80 = re.compile(r'^LSP *: +(?P<lsp>\S+)$')

        # Forward-class: 0
        p81 = re.compile(r'^Forward-class: +(?P<forward_class>\d+)$')

        # Multicast Source: Not Set
        p82 = re.compile(r'^Multicast +Source: +(?P<multicast_source>[\S ]+)$')
        
        # PD System Data: AF-LIF-IPv4: 0x00000000  AF-LIF-IPv6: 0x00000000
        p83 = re.compile(r'^PD +System +Data: +(?P<key_1>\S+): +(?P<val_1>\S+) +(?P<key_2>\S+): +(?P<val_2>\S+)$')

        # Virtual MAC addresses:
        p84 = re.compile(r'^Virtual +MAC +addresses:$')

        # Incoming Status (PW Status TLV):
        p85 = re.compile(r'^Incoming Status \([\S ]+\):$')

        # Status code: 0x0 (Up) in Notification message
        p86 = re.compile(r'^Status code: +(?P<code>.+) in [\w ]+$')

        for line in out.splitlines():
            original_line = line
            line = line.strip()
            # Bridge group: g1, bridge-domain: bd1, id: 0, state: up, ShgId: 0, MSTi: 0
            # Bridge group: EVPN-Multicast, bridge-domain: EVPN-Multicast-BTV, id: 0, state: up, ShgId: 0, MSTi: 0
            m = p1.match(line)
            if m:
                dict_type = 'bridge_domain'
                group = m.groupdict()
                bridge_group = group['bridge_group']
                bridge_domain = group['bridge_domain']
                id = int(group['id'])
                state = group['state']
                shg_id = int(group['shg_id'])
                bridge_domain_dict = ret_dict.setdefault('bridge_group', {}). \
                    setdefault(bridge_group, {}). \
                    setdefault('bridge_domain', {}). \
                    setdefault(bridge_domain, {})
                bridge_domain_dict.update({'state': state})
                bridge_domain_dict.update({'id': id})
                bridge_domain_dict.update({'shg_id': shg_id})
                if group['mst_i']:
                    mst_i = int(group['mst_i'])
                    bridge_domain_dict.update({'mst_i': mst_i})
                continue
            
            # VPWS Mode
            m = p1_1.match(line)
            if m:
                group = m.groupdict()
                mode = group['mode']
                if dict_type == 'bridge_domain':
                    bridge_domain_dict.update({'mode': mode})
                else:
                    interface_dict.update({'mode': mode})
                continue

            # MAC learning: enabled
            m = p2.match(line)
            if m:
                group = m.groupdict()
                mac_learning = group['mac_learning']
                if dict_type == 'bridge_domain':
                    bridge_domain_dict.update({'mac_learning': mac_learning})
                elif dict_type == 'pw' or dict_type == 'access_pw':
                    pw_id_dict.update({'mac_learning': mac_learning})
                else:
                    interface_dict.update({'mac_learning': mac_learning})
                continue

            # MAC withdraw: disabled
            m = p3.match(line)
            if m:
                group = m.groupdict()
                mac_withdraw = group['mac_withdraw']
                if dict_type == 'bridge_domain':
                    bridge_domain_dict.update({'mac_withdraw': mac_withdraw})
                else:
                    interface_dict.update({'mac_learning': mac_learning})
                continue

            # Flooding:
            m = p4.match(line)
            if m:
                group = m.groupdict()
                if dict_type == 'bridge_domain':
                    flooding_dict = bridge_domain_dict.setdefault('flooding', {})
                elif dict_type == 'pw' or dict_type == 'access_pw':
                    flooding_dict = pw_id_dict.setdefault('flooding', {})
                else:
                    flooding_dict = interface_dict.setdefault('flooding', {})
                continue

            # Broadcast & Multicast: enabled
            m = p5.match(line)
            if m:
                group = m.groupdict()
                enabled = group['enabled']
                flooding_dict.update({'broadcast_multicast': enabled})
                continue

            # Unknown unicast: enabled
            m = p6.match(line)
            if m:
                group = m.groupdict()
                enabled = group['enabled']
                flooding_dict.update({'unknown_unicast': enabled})
                continue

            # MAC aging time: 300 s, Type: inactivity
            m = p7.match(line)
            if m:
                group = m.groupdict()
                mac_aging_time = int(group['mac_aging_time'])
                mac_aging_type = group['mac_aging_type']
                if dict_type == 'bridge_domain':
                    bridge_domain_dict.update({'mac_aging_time': mac_aging_time})
                    bridge_domain_dict.update({'mac_aging_type': mac_aging_type})
                elif dict_type == 'pw' or dict_type == 'access_pw':
                    pw_id_dict.update({'mac_aging_time': mac_aging_time})
                    pw_id_dict.update({'mac_aging_type': mac_aging_type})
                else:
                    interface_dict.update({'mac_aging_time': mac_aging_time})
                    interface_dict.update({'mac_aging_type': mac_aging_type})
                continue

            # MAC limit: 4000, Action: none, Notification: syslog
            m = p8.match(line)
            if m:
                group = m.groupdict()
                mac_limit = int(group['mac_limit'])
                action = group['action']
                notification = group['notification']
                
                if dict_type == 'bridge_domain':
                    bridge_domain_dict.update({'mac_limit': mac_limit})
                    bridge_domain_dict.update({'mac_limit_action': action})
                    bridge_domain_dict.update({'mac_limit_notification': notification})
                elif dict_type == 'pw' or dict_type == 'access_pw':
                    pw_id_dict.update({'mac_limit': mac_limit})
                    pw_id_dict.update({'mac_limit_action': action})
                    pw_id_dict.update({'mac_limit_notification': notification})
                else:
                    interface_dict.update({'mac_limit': mac_limit})
                    interface_dict.update({'mac_limit_action': action})
                    interface_dict.update({'mac_limit_notification': notification})
                continue

            # MAC limit reached: yes
            # MAC limit reached: no, threshold: 75%
            m = p9.match(line)
            if m:
                group = m.groupdict()
                mac_limit_reached = group['mac_limit_reached']
                bridge_domain_dict.update({'mac_limit_reached': mac_limit_reached})
                threshold = group['threshold']
                if dict_type == 'bridge_domain':
                    bridge_domain_dict.update({'mac_limit_reached': mac_limit_reached})
                    if threshold:
                        bridge_domain_dict.update({'mac_limit_threshold': threshold})
                elif dict_type == 'pw' or dict_type == 'access_pw':
                    pw_id_dict.update({'mac_limit_reached': mac_limit_reached})
                    if threshold:
                        pw_id_dict.update({'mac_limit_threshold': threshold})
                else:
                    interface_dict.update({'mac_limit_reached': mac_limit_reached})
                    if threshold:
                        interface_dict.update({'mac_limit_threshold': threshold})
                continue

            # Security: disabled
            m = p10.match(line)
            if m:
                group = m.groupdict()
                security = group['security']
                if dict_type == 'bridge_domain':
                    bridge_domain_dict.update({'security': security})
                else:
                    interface_dict.update({'security': security})
                continue

            # DHCPv4 snooping: disabled
            m = p11.match(line)
            if m:
                group = m.groupdict()
                dhcp_v4_snooping = group['dhcp_v4_snooping']
                if dict_type == 'bridge_domain':
                    bridge_domain_dict.update({'dhcp_v4_snooping': dhcp_v4_snooping})
                elif dict_type == 'pw' or dict_type == 'access_pw':
                    pw_id_dict.update({'dhcp_v4_snooping': dhcp_v4_snooping})
                else:
                    interface_dict.update({'dhcp_v4_snooping': dhcp_v4_snooping})
                continue

            # DHCPv4 Snooping profile: none
            m = p11_1.match(line)
            if m:
                group = m.groupdict()
                dhcp_v4_snooping_profile = group['dhcp_v4_snooping_profile']
                if dict_type == 'bridge_domain':
                    bridge_domain_dict.update({'dhcp_v4_snooping_profile': dhcp_v4_snooping_profile})
                elif dict_type == 'pw' or dict_type == 'access_pw':
                    pw_id_dict.update({'dhcp_v4_snooping_profile': dhcp_v4_snooping_profile})
                else:
                    interface_dict.update({'dhcp_v4_snooping_profile': dhcp_v4_snooping_profile})
                continue

            # IGMP Snooping: disabled
            m = p11_2.match(line)
            if m:
                group = m.groupdict()
                igmp_snooping = group['igmp_snooping']
                if dict_type == 'bridge_domain':
                    bridge_domain_dict.update({'igmp_snooping': igmp_snooping})
                elif dict_type == 'pw' or dict_type == 'access_pw':
                    pw_id_dict.update({'igmp_snooping': igmp_snooping})
                else:
                    interface_dict.update({'igmp_snooping': igmp_snooping})
                continue

            # IGMP Snooping profile: none
            m = p11_3.match(line)
            if m:
                group = m.groupdict()
                igmp_snooping_profile = group['igmp_snooping_profile']
                if dict_type == 'bridge_domain':
                    bridge_domain_dict.update({'igmp_snooping_profile': igmp_snooping_profile})
                elif dict_type == 'pw' or dict_type == 'access_pw':
                    pw_id_dict.update({'igmp_snooping_profile': igmp_snooping_profile})
                else:
                    interface_dict.update({'igmp_snooping_profile': igmp_snooping_profile})
                continue

            # MLD Snooping profile: none
            m = p11_4.match(line)
            if m:
                group = m.groupdict()
                mld_snooping_profile = group['mld_snooping_profile']
                if dict_type == 'bridge_domain':
                    bridge_domain_dict.update({'mld_snooping_profile': mld_snooping_profile})
                elif dict_type == 'pw' or dict_type == 'access_pw':
                    pw_id_dict.update({'mld_snooping_profile': mld_snooping_profile})
                else:
                    interface_dict.update({'mld_snooping_profile': mld_snooping_profile})
                continue

            # MTU: 1500
            m = p12.match(line)
            if m:
                group = m.groupdict()
                mtu = int(group['mtu'])
                bridge_domain_dict.update({'mtu': mtu})
                continue

            # Filter MAC addresses:
            m = p13.match(line)
            if m:
                group = m.groupdict()
                if group['filter_mac_addresses']:
                    filter_mac_addresses = int(group['filter_mac_addresses'])
                    bridge_domain_dict.update({'filter_mac_addresses': filter_mac_addresses})
                continue

            # ACs: 1 (1 up), VFIs: 1, PWs: 1 (1 up)
            m = p14.match(line)
            if m:
                group = m.groupdict()
                ac = int(group['ac'])
                ac_up = int(group['ac_up'])
                vfi = int(group['vfi'])
                pw = int(group['pw'])
                pw_up = int(group['pw_up'])
                
                ac_dict = bridge_domain_dict.setdefault('ac', {})
                ac_dict.update({'num_ac': ac})
                ac_dict.update({'num_ac_up': ac_up})

                vfi_dict = bridge_domain_dict.setdefault('vfi', {})
                vfi_dict.update({'num_vfi': vfi})

                pw_dict = bridge_domain_dict.setdefault('pw', {})
                pw_dict.update({'num_pw': pw})
                pw_dict.update({'num_pw_up': pw_up})

                pbb = group['pbb']
                pbb_up = group['pbb_up']
                if pbb:
                    pbb_dict = bridge_domain_dict.setdefault('pbb', {})
                    pbb_dict.update({'num_pbb': int(pbb)})
                    pbb_dict.update({'num_pbb_up': int(pbb_up)})

                vni = group['vni']
                vni_up = group['vni_up']
                if vni:
                    vni_dict = bridge_domain_dict.setdefault('vni', {})
                    vni_dict.update({'num_vni': int(vni)})
                    vni_dict.update({'num_vni_up': int(vni_up)})

                continue

            # List of ACs:
            m = p15.match(line)
            if m:
                dict_type = 'ac'
                label_found = False
                continue

            # AC: GigabitEthernet0/1/0/0, state is up
            m = p16.match(line)
            if m:
                dict_type = 'ac'
                group = m.groupdict()
                interface = Common.convert_intf_name(group['interface'])
                state = group['state']
                interface_dict = ac_dict.setdefault('interfaces', {}). \
                    setdefault(interface, {})
                interface_dict.update({'state': state})
                continue

            # Type Ethernet
            # Type VLAN; Num Ranges: 1
            m = p17.match(line)
            if m:
                group = m.groupdict()
                ac_type = group['type']
                num_ranges = group['num_ranges']
                interface_dict.update({'type': ac_type})
                if num_ranges:
                    interface_dict.update({'vlan_num_ranges': num_ranges})
                continue
            
            # MTU 1500; XC ID 0x2000001; interworking none; MSTi 0 (unprotected)
            # MTU 1514; XC ID 0x8000000b; interworking none
            # MTU 9202; XC ID 0xc0000002; interworking none; MSTi 5
            m = p18.match(line)
            if m:
                group = m.groupdict()
                mtu = int(group['mtu'])
                xc_id = group['xc_id']
                interworking = group['interworking']
                interface_dict.update({'mtu': mtu})
                interface_dict.update({'xc_id': xc_id})
                interface_dict.update({'interworking': interworking})
                mst_i = group['mst_i']
                if mst_i:
                    interface_dict.update({'mst_i': int(mst_i)})
                mst_i_state = group['mst_i_state']
                if mst_i_state:
                    interface_dict.update({'mst_i_state': mst_i_state})
                continue

            # Type Ethernet      MTU 1500; XC ID 1; interworking none
            m = p18_1.match(line)
            if m:
                group = m.groupdict()
                ac_type = group['pw_type']
                mtu = int(group['mtu'])
                xc_id = group['xc_id']
                interworking = group['interworking']
                interface_dict.update({'type': ac_type})
                interface_dict.update({'mtu': mtu})
                interface_dict.update({'xc_id': xc_id})
                interface_dict.update({'interworking': interworking})
                continue

            # 0000.0000.0000
            m = p19.match(line)
            if m:
                group = m.groupdict()
                static_mac_address = group['static_mac_address']
                if dict_type == 'ac':
                    static_mac_address_list = interface_dict.get(mac_address_type, [])
                else:
                    static_mac_address_list = vfi_obj_dict.get(mac_address_type, [])
                static_mac_address_list.append(static_mac_address)
                interface_dict.update({mac_address_type: static_mac_address_list})
                continue

            # Statistics:
            m = p20.match(line)
            if m:
                continue
            
            # packet totals: receive 3919680,send 9328
            m = p21.match(line)
            if m:
                group = m.groupdict()
                receive = int(group['receive'])
                send = int(group['send'])

                if dict_type == 'pw':
                    statistics_dict = pw_id_dict.setdefault('statistics', {})
                elif dict_type == 'evpn':
                    statistics_dict = evpn_dict.setdefault('statistics', {})
                elif dict_type == 'vfi':
                    statistics_dict = vfi_dict.setdefault('statistics', {})
                else:
                    statistics_dict = interface_dict.setdefault('statistics', {})
                packet_totals_dict = statistics_dict.setdefault('packet_totals', {})
                packet_totals_dict.update({'receive': receive})
                packet_totals_dict.update({'send': send})
                continue

            # byte totals: receive 305735040,send 15022146
            m = p22.match(line)
            if m:
                group = m.groupdict()
                receive = int(group['receive'])
                send = int(group['send'])

                if dict_type == 'pw':
                    statistics_dict = pw_id_dict.setdefault('statistics', {})
                elif dict_type == 'evpn':
                    statistics_dict = evpn_dict.setdefault('statistics', {})
                else:
                    statistics_dict = interface_dict.setdefault('statistics', {})
                packet_totals_dict = statistics_dict.setdefault('byte_totals', {})
                packet_totals_dict.update({'receive': receive})
                packet_totals_dict.update({'send': send})
                continue

            # List of Access PWs:
            m = p23.match(line)
            if m:
                dict_type = 'access_pw'
                label_found = False
                continue

            # List of VFIs:
            m = p24.match(line)
            if m:
                dict_type = 'vfi'
                label_found = False
                continue

            # PW: neighbor 10.4.1.1, PW ID 1, state is up ( established )
            m = p26.match(line)
            if m:
                dict_type = 'pw'
                group = m.groupdict()
                neighbor = group['neighbor']
                pw_id = group['pw_id']
                state = group['state']
                pw_id_dict = vfi_obj_dict.setdefault('neighbor', {}). \
                    setdefault(neighbor, {}). \
                    setdefault('pw_id', {}). \
                    setdefault(pw_id, {})
                pw_id_dict.update({'state': state})
                label_dict = pw_id_dict
                continue

            # PW class mpls, XC ID 0xff000001
            m = p27.match(line)
            if m:
                group = m.groupdict()
                pw_class = group['pw_class']
                xc_id = group['xc_id']
                pw_id_dict.update({'pw_class': pw_class})
                pw_id_dict.update({'xc_id': xc_id})
                continue

            # PW class mpls, XC ID 0xff000001
            m = p27_1.match(line)
            if m:
                group = m.groupdict()
                pw_class = group['pw_class']
                pw_id_dict.update({'pw_class': pw_class})
                continue

            # Encapsulation MPLS, protocol LDP
            m = p28.match(line)
            if m:
                group = m.groupdict()
                encapsulation = group['encapsulation']
                mpls = group['protocol']
                pw_id_dict.update({'encapsulation': encapsulation})
                if mpls:
                    pw_id_dict.update({'protocol': mpls})
                continue

            # PW type Ethernet, control word disabled, interworking none
            m = p29.match(line)
            if m:
                group = m.groupdict()
                type_found = group['type'].lower()
                pw_type = group['pw_type']
                control_word = group['control_word']
                interworking = group['interworking']
                pw_id_dict.update({'{}_type'.format(type_found) : pw_type})
                pw_id_dict.update({'control_word': control_word})
                if interworking:
                    pw_id_dict.update({'interworking': interworking})
                continue

            # PW backup disable delay 0 sec
            m = p30.match(line)
            if m:
                group = m.groupdict()
                pw_id_dict.update({'pw_backup_disable_delay': int(group['delay'])})
                continue

            # Sequencing not set
            m = p31.match(line)
            if m:
                group = m.groupdict()
                sequencing = group['sequencing']
                pw_id_dict.update({'sequencing': sequencing})
                continue

            # MPLS         Local                          Remote
            m = p32.match(line)
            if m:
                group = m.groupdict()
                label_found = True
                type_found = group['type'].lower()
                continue

            # ------------ ------------------------------ -----------------------------
            m = p34.match(line)
            if m:
                mpls_pairs = {}
                for m in re.finditer(r'-+', original_line):
                    mpls_pairs.update({m.start(): m.end()})
                continue

            # Create time: 12/03/2008 14:03:00 (17:17:30 ago)
            m = p36.match(line)
            if m:
                group = m.groupdict()
                create_time = group['create_time']
                if dict_type == 'bridge_domain':
                    bridge_domain_dict.update({'create_time': create_time})
                else:
                    pw_id_dict.update({'create_time': create_time})
                continue

            # Last time status changed: 13/03/2008 05:57:58 (01:22:31 ago)
            m = p37.match(line)
            if m:
                group = m.groupdict()
                last_time_status_changed = group['last_time_status_changed']
                pw_id_dict.update({'last_time_status_changed': last_time_status_changed})
                continue

            # MAC withdraw message: send 0 receive 0
            m = p38.match(line)
            if m:
                group = m.groupdict()
                send = int(group['send'])
                receive = int(group['receive'])
                mac_withdraw_message_dict = pw_id_dict.setdefault('mac_withdraw_message', {})
                mac_withdraw_message_dict.update({'send': send})
                mac_withdraw_message_dict.update({'receive': receive})
                continue

            # Static MAC addresses:
            m = p39.match(line)
            if m:
                mac_address_type = 'static_mac_address'
                continue

            # VFI Statistics:
            m = p40.match(line)
            if m:
                continue
            
            # Mon Oct  7 16:18:59.168 EDT
            m = p43.match(line)
            if m:
                continue

            # VFI 1
            m = p25.match(line)
            if m:
                group = m.groupdict()
                dict_type = 'vfi'
                vfi = group['vfi']
                vfi_obj_dict = vfi_dict.setdefault(vfi, {})
                state = group['state']
                if state:
                    vfi_obj_dict.update({'state': state})
                continue

            # drops: illegal VLAN 0, illegal length 0
            m = p41.match(line)
            if m:
                vfi_statistics_dict = vfi_obj_dict.setdefault('statistics', {})
                group = m.groupdict()
                drops = group['drops']
                vlan = int(group['vlan'])
                illegal_length = int(group['illegal_length'])
                drop_dict = vfi_statistics_dict.setdefault('drop', {})
                drop_dict.update({'illegal_vlan': vlan})
                drop_dict.update({'illegal_length': illegal_length})
                continue
            
            # Legend: pp = Partially Programmed.
            m = p44.match(line)
            if m:
                group = m.groupdict()
                legend = group['legend']
                ret_dict.update({'legend': legend})
                continue

            # Coupled state: disabled
            m = p45.match(line)
            if m:
                group = m.groupdict()
                coupled_state = group['coupled_state']
                bridge_domain_dict.update({'coupled_state': coupled_state})
                continue

            # VINE state: EVPN-IRB
            m = p46.match(line)
            if m:
                group = m.groupdict()
                vine_state = group['vine_state']
                bridge_domain_dict.update({'vine_state': vine_state})
                continue

            # MAC withdraw for Access PW: enabled
            m = p47.match(line)
            if m:
                group = m.groupdict()
                mac_withdraw_for_access_pw = group['mac_withdraw_for_access_pw']
                bridge_domain_dict.update({'mac_withdraw_for_access_pw': mac_withdraw_for_access_pw})
                continue

            # MAC withdraw sent on: bridge port up
            m = p48.match(line)
            if m:
                group = m.groupdict()
                mac_withdraw_sent_on = group['mac_withdraw_sent_on']
                bridge_domain_dict.update({'mac_withdraw_sent_on': mac_withdraw_sent_on})
                continue

            # MAC withdraw relaying (access to access): disabled
            m = p49.match(line)
            if m:
                group = m.groupdict()
                mac_withdraw_relaying = group['mac_withdraw_relaying']
                bridge_domain_dict.update({'mac_withdraw_relaying': mac_withdraw_relaying})
                continue

            # MAC port down flush: enabled
            m = p50.match(line)
            if m:
                group = m.groupdict()
                mac_port_down_flush = group['mac_port_down_flush']
                if dict_type == 'pw' or dict_type == 'access_pw':
                    pw_id_dict.update({'mac_port_down_flush': mac_port_down_flush})
                else:
                    bridge_domain_dict.update({'mac_port_down_flush': mac_port_down_flush})
                continue

            #  MAC Secure: disabled, Logging: disabled
            m = p51.match(line)
            if m:
                group = m.groupdict()
                mac_secure = group['mac_secure']
                mac_secure_logging = group['mac_secure_logging']
                if dict_type == 'pw' or dict_type == 'access_pw':
                    pw_id_dict.update({'mac_secure': mac_secure})
                    pw_id_dict.update({'mac_secure_logging': mac_secure_logging})
                else:
                    bridge_domain_dict.update({'mac_secure': mac_secure})
                    bridge_domain_dict.update({'mac_secure_logging': mac_secure_logging})
                continue

            # Split Horizon Group: none
            m = p52.match(line)
            if m:
                group = m.groupdict()
                split_horizon_group = group['split_horizon_group']
                if dict_type == 'pw' or dict_type == 'access_pw':
                    pw_id_dict.update({'split_horizon_group': split_horizon_group})
                elif dict_type == 'ac':
                    interface_dict.update({'split_horizon_group': split_horizon_group})
                else:
                    bridge_domain_dict.update({'split_horizon_group': split_horizon_group})
                continue

            # Dynamic ARP Inspection: disabled, Logging: disabled
            m = p53.match(line)
            if m:
                group = m.groupdict()
                dynamic_arp_inspection = group['dynamic_arp_inspection']
                dynamic_arp_logging = group['dynamic_arp_logging']
                bridge_domain_dict.update({'dynamic_arp_inspection': dynamic_arp_inspection})
                bridge_domain_dict.update({'dynamic_arp_logging': dynamic_arp_logging})
                continue

            # IP Source Guard: disabled, Logging: disabled
            m = p54.match(line)
            if m:
                group = m.groupdict()
                ip_source_guard = group['ip_source_guard']
                ip_source_logging = group['ip_source_logging']
                if dict_type == 'pw' or dict_type == 'access_pw':
                    pw_id_dict.update({'ip_source_guard': ip_source_guard})
                    pw_id_dict.update({'ip_source_logging': ip_source_logging})
                else:
                    bridge_domain_dict.update({'ip_source_guard': ip_source_guard})
                    bridge_domain_dict.update({'ip_source_logging': ip_source_logging})
                continue

            # Storm Control: disabled
            m = p56.match(line)
            if m:
                group = m.groupdict()
                storm_control = group['storm_control']
                if dict_type == 'pw' or dict_type == 'access_pw':
                    pw_id_dict.update({'storm_control': storm_control})
                else:
                    bridge_domain_dict.update({'storm_control': storm_control})
                continue

            # Bridge MTU: 1500
            m = p57.match(line)
            if m:
                group = m.groupdict()
                bridge_mtu = group['bridge_mtu']
                bridge_domain_dict.update({'bridge_mtu': bridge_mtu})
                continue

            # MIB cvplsConfigIndex: 1
            m = p58.match(line)
            if m:
                group = m.groupdict()
                mid_cvpls_config_index = group['mid_cvpls_config_index']
                bridge_domain_dict.update({'mid_cvpls_config_index': mid_cvpls_config_index})
                continue

            # P2MP PW: disabled
            m = p59.match(line)
            if m:
                group = m.groupdict()
                p2mp_pw = group['p2mp_pw']
                bridge_domain_dict.update({'p2mp_pw': p2mp_pw})
                continue

            # No status change since creation
            m = p60.match(line)
            if m:
                bridge_domain_dict.update({'status_changed_since_creation': 'No'})
                continue

            # List of EVPNs:
            m = p61.match(line)
            if m:
                dict_type = 'evpn'
                label_found = False
                continue

            # EVPN, state: up
            m = p62.match(line)
            if m:
                group = m.groupdict()
                evpn = group['evpn']
                evpn_state = group['state']
                evpn_dict = bridge_domain_dict.setdefault('evpn', {}) .\
                    setdefault(evpn, {})
                evpn_dict.update({'state': evpn_state})
                continue

            # evi: 1000
            m = p63.match(line)
            if m:
                group = m.groupdict()
                evi = group['evi']
                evpn_dict.update({'evi': evi})
                continue

            # XC ID 0x80000009
            m = p64.match(line)
            if m:
                group = m.groupdict()
                xc_id = group['xc_id']
                if dict_type == 'pw' or dict_type == 'access_pw':
                    pw_id_dict.update({'xc_id': xc_id})
                elif dict_type == 'evpn':
                    evpn_dict.update({'xc_id': xc_id})
                elif dict_type == 'vfi':
                    vfi_dict.update({'xc_id': xc_id})
                else:
                    interface_dict.update({'xc_id': xc_id})
                continue

            # MAC move: 0
            m = p65.match(line)
            if m:
                group = m.groupdict()
                mac_move = group['mac_move']
                statistics_dict.update({'mac_move': mac_move})
                continue

            # BVI MAC address:
            m = p66.match(line)
            if m:
                mac_address_type = 'bvi_mac_address'
                continue

            # 1000.10ff.1000
            m = p67.match(line)
            if m:
                group = m.groupdict()
                bvi_mac_address = group['bvi_mac_address']
                bvi_mac_address_list = interface_dict.get('bvi_mac_address', [])
                bvi_mac_address_list.append(bvi_mac_address)
                interface_dict.update({'bvi_mac_address': bvi_mac_address_list})
                continue

            # Rewrite Tags: []
            m = p68.match(line)
            if m:
                group = m.groupdict()
                rewrite_tags = group.get('rewrite_tags')
                interface_dict.update({'rewrite_tags': rewrite_tags if rewrite_tags else ''})
                continue

            # VLAN ranges: [100, 100]
            m = p69.match(line)
            if m:
                group = m.groupdict()
                vlan_ranges = group['vlan_ranges'].replace(' ', '')
                interface_dict.update({'vlan_ranges': vlan_ranges.split(',')})
                continue

            # Storm control drop counters:
            m = p70.match(line)
            if m:
                continue

            # packets: broadcast 0, multicast 0, unknown unicast 0
            m = p71.match(line)
            if m:
                group = m.groupdict()
                broadcast = group['broadcast']
                multicast = group['multicast']
                unknown_unicast = group['unknown_unicast']
                if dict_type == 'pw' or dict_type == 'access_pw':
                    packet_dict = pw_id_dict.setdefault('storm_control_drop_counters', {}). \
                        setdefault('packets', {})
                elif dict_type == 'ac':
                    packet_dict = interface_dict.setdefault('storm_control_drop_counters', {}). \
                        setdefault('packets', {})
                else:
                    packet_dict = bridge_domain_dict.setdefault('storm_control_drop_counters', {}). \
                        setdefault('packets', {})
                packet_dict.update({'broadcast': broadcast})
                packet_dict.update({'multicast': multicast})
                packet_dict.update({'unknown_unicast': unknown_unicast})
                continue

            # bytes: broadcast 0, multicast 0, unknown unicast 0
            m = p72.match(line)
            if m:
                group = m.groupdict()
                broadcast = group['broadcast']
                multicast = group['multicast']
                unknown_unicast = group['unknown_unicast']
                if dict_type == 'pw' or dict_type == 'access_pw':
                    byte_dict = pw_id_dict.setdefault('storm_control_drop_counters', {}). \
                        setdefault('bytes', {})
                elif dict_type == 'ac':
                    byte_dict = interface_dict.setdefault('storm_control_drop_counters', {}). \
                        setdefault('bytes', {})
                else:
                    byte_dict = bridge_domain_dict.setdefault('storm_control_drop_counters', {}). \
                        setdefault('bytes', {})
                byte_dict.update({'broadcast': broadcast})
                byte_dict.update({'multicast': multicast})
                byte_dict.update({'unknown_unicast': unknown_unicast})
                continue

            # Dynamic ARP inspection drop counters:
            m = p73.match(line)
            if m:
                byte_send_dict = interface_dict.setdefault('dynamic_arp_inspection_drop_counters', {})
                continue

            # packets: 0, bytes: 0
            m = p74.match(line)
            if m:
                group = m.groupdict()
                packets = group['packets']
                bytes = group['bytes']
                byte_send_dict.update({'packets': packets})
                byte_send_dict.update({'bytes': bytes})
                continue

            # IP source guard drop counters:
            m = p75.match(line)
            if m:
                byte_send_dict = interface_dict.setdefault('ip_source_guard_drop_counters', {})
                continue
            
            # List of Access VFIs:
            m = p76.match(line)
            if m:
                label_found = False
                continue

            # Error: Need at least 1 bridge port up
            m = p77.match(line)
            if m:
                group = m.groupdict()
                interface_dict.update({'error': group['error']})
                continue

            # EVPN: neighbor 0.0.0.0, PW ID: evi 601, ac-id 1, state is down ( local ready ) (Transport LSP Down)
            m = p78.match(line)
            if m:
                group = m.groupdict()
                type_found = group['type']
                neighbor = group['neighbor']
                pw_id = group['pw_id']
                ac_id = group['ac_id']
                state = group['state']
                pw_id_dict = bridge_domain_dict.setdefault('access_pw', {}). \
                    setdefault(type_found, {}). \
                    setdefault('neighbor', {}). \
                    setdefault(neighbor, {}). \
                    setdefault('pw_id', {}). \
                    setdefault(pw_id, {})
                pw_id_dict.update({'ac_id': ac_id})
                pw_id_dict.update({'state': state})
                label_dict = pw_id_dict
                continue
            
            # Source address 10.154.219.85
            m = p79.match(line)
            if m:
                group = m.groupdict()
                source_address = group['source_address']
                pw_id_dict.update({'source_address': source_address})
                continue

            # LSP : Up
            m = p80.match(line)
            if m:
                group = m.groupdict()
                lsp = group['lsp']
                label_dict = pw_id_dict.setdefault('lsp', {})
                label_dict.update({'state': lsp})
                continue

            # Forward-class: 0
            m = p81.match(line)
            if m:
                group = m.groupdict()
                forward_class = group['forward_class']
                pw_id_dict.update({'forward_class': forward_class})
                continue
            
            # Multicast Source: Not Set
            m = p82.match(line)
            if m:
                group = m.groupdict()
                multicast_source = group['multicast_source']
                bridge_domain_dict.update({'multicast_source': multicast_source})
                continue
            
            # PD System Data: AF-LIF-IPv4: 0x00000000  AF-LIF-IPv6: 0x00000000
            m = p83.match(line)
            if m:
                group = m.groupdict()
                key_1 = group['key_1'].lower().replace('-','_')
                val_1 = group['val_1']
                key_2 = group['key_2'].lower().replace('-','_')
                val_2 = group['val_2']
                pd_system_data = interface_dict.setdefault('pd_system_data', {})
                pd_system_data.update({key_1: val_1})
                pd_system_data.update({key_2: val_2})
                continue

            # Virtual MAC addresses:
            m = p84.match(line)
            if m:
                mac_address_type = 'virtual_mac_address'
                continue

            #     (LSP ping verification)               
            #                                    (none)
            #     (control word)                 (control word)
            #     (control word) 
            m = p42.match(line)
            if m:
                if label_found:
                    mpls_items = list(mpls_pairs.items()) 
                    local_value = (original_line[mpls_items[1][0]:mpls_items[1][1]].
                                    replace('(','').replace(')', '').strip()) 
                    remote_value = (original_line[mpls_items[2][0]:mpls_items[2][1]].
                                    replace('(','').replace(')', '').strip())
                    local_type = mpls_dict.get('local_type', [])
                    remote_type = mpls_dict.get('remote_type', [])
                    if local_value:
                        local_type.append(local_value)
                    if remote_value:
                        remote_type.append(remote_value)
                    mpls_dict.update({'local_type': local_type})
                    mpls_dict.update({'remote_type': remote_type})
                continue

            m = p85.match(line)
            if m:
                continue

            m = p86.match(line)
            if m:
                pw_id_dict.update({'status_code': m.groupdict()['code']})
                continue

            # Label        30005                          unknown
            # Group ID     0x5000300                      0x0
            # VCCV CV type 0x2                            0x0
            # Avoid show commands: show l2vpn xconnect detail
            # Avoid Date and Time: Wed Sep 25 20:09:36.362 UTC
            m = p33.match(line)
            if m:
                if label_found:
                    group = m.groupdict()
                    mpls = group['mpls'].strip().lower().replace(' ', '_')
                    local = group['local'].strip()
                    remote = group['remote']
                    if mpls == 'interface':
                        if interface_found:
                            mpls_dict = label_dict.setdefault(type_found, {}). \
                                setdefault('monitor_interface', {})
                            mpls_dict.update({'local': local})
                            mpls_dict.update({'remote': remote})
                        else:
                            interface_found = True
                            mpls_dict = label_dict.setdefault(type_found, {}). \
                                setdefault(mpls, {})
                            mpls_dict.update({'local': local})
                            mpls_dict.update({'remote': remote})
                    else:
                        mpls_dict = label_dict.setdefault(type_found, {}). \
                            setdefault(mpls, {})
                        mpls_dict.update({'local': local})
                        mpls_dict.update({'remote': remote})
                continue

            # (control word)                 (control word)
            # (router alert label)           (router alert label)
            m = p33_1.match(line)
            if m:
                if label_found and interface_found:
                    mpls_dict.update({'local': m.groupdict()['local']})
                    mpls_dict.update({'remote': m.groupdict()['remote']})

        return ret_dict
