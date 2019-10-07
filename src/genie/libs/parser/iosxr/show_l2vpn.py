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

    cli_command = 'show l2vpn mac-learning {mac_type} all location {location}'

    def cli(self, mac_type='', location='', output=None):
        if output is None:
            cmd = self.cli_command[0].format(
                mac_type=mac_type, location=location)
            out = self.device.execute(cmd)
        else:
            out = output

        # Topo ID  Producer  Next Hop(s)  Mac Address     IP Address

        # 6        0/0/CPU0   BV1        1000.0001.0001      10.1.1.11
        # 6        0/0/CPU0   BV1        0000.f65a.357c      fe80::200:f6ff:fe5a:357c
        # 1        0/0/CPU0   BE1.7      7777.7777.0002

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
        # 0001.0000.0002 dynamic Te0/0/1/0/3.3               N/A        0d 0h
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
            # 0001.0000.0002 dynamic Te0/0/1/0/3.3               N/A        0d
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
                                    'static_mac_address': int,
                                    'mst_i': int,
                                    'mst_i_state': str
                                }
                            }
                        },
                        Optional('vfi'): {
                            'num_vfi': int,
                            Any(): {
                                'neighbor': {
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
                        },
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
        # Bridge group: EVPN-Multicast, bridge-domain: EVPN-Multicast-BTV, id: 0, state: up, ShgId: 0, MSTi: 0
        p1 = re.compile(r'^Bridge +group: +(?P<bridge_group>\w+), +bridge\-domain: +'
            '(?P<bridge_domain>\S+), +id: +(?P<id>\d+), +state: +(?P<state>\w+), +'
            'ShgId: +(?P<shg_id>\d+), +MSTi: +(?P<mst_i>\d+)$')

        # Aging: 300 s, MAC limit: 4000, Action: none, Notification: syslog
        p2 = re.compile(r'^Aging: +(?P<mac_aging_time>\d+) s, +MAC +limit: +(?P<mac_limit>\d+), '
            '+Action: +(?P<mac_limit_action>\w+), +Notification: +(?P<mac_limit_notification>\w+)$')

        # Filter MAC addresses: 0
        p3 = re.compile(r'^Filter +MAC +addresses: +(?P<filter_mac_address>\d+)$')

        # ACs: 1 (1 up), VFIs: 1, PWs: 1 (1 up)
        p4 = re.compile(r'^ACs: +(?P<ac>\d+) +\((?P<ac_up>\d+) +up\), +VFIs: +'
            '(?P<vfi>\d+), +PWs: +(?P<pw>\d+) +\((?P<pw_up>\d+) +\w+\)$')

        # Gi0/1/0/0, state: up, Static MAC addresses: 2, MSTi: 0 (unprotected)
        p5 = re.compile(r'^(?P<interface>\S+), +state: +(?P<state>\w+), +Static +MAC +addresses: +'
            '(?P<static_mac_address>\d+), +MSTi: +(?P<mst_i>\d+) +\((?P<mst_i_state>\w+)\)$')
        
        # VFI 1
        p6 = re.compile(r'^VFI +(?P<vfi>\d+)$')

        # Neighbor 10.1.1.1 pw-id 1, state: up, Static MAC addresses: 0
        p7 = re.compile(r'Neighbor +(?P<neighbor>\S+) +pw-id +(?P<pw_id>\d+), +state: +'
            '(?P<state>\w+), +Static +MAC +addresses: +(?P<static_mac_address>\d+)$')

        # g1/bd1                           0     up         1/1            1/1 
        p8 = re.compile(r'^(?P<bridge_group>\S+)\/(?P<bridge_domain_name>\S+) +(?P<id>\d+) +'
            '(?P<state>\w+) +(?P<ac>\d+)\/(?P<ac_up>\d+) +(?P<pw>\d+)\/(?P<pw_up>\d+)$')
        
        for line in out.splitlines():
            line = line.strip()
            
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
                continue
            
            # Gi0/1/0/0, state: up, Static MAC addresses: 2, MSTi: 0 (unprotected)
            m = p5.match(line)
            if m:
                group = m.groupdict()
                interface = Common.convert_intf_name(group['interface'])
                state = group['state']
                static_mac_address = int(group['static_mac_address'])
                mst_i = int(group['mst_i'])
                mst_i_state = group['mst_i_state']

                interface_dict = ac_dict.setdefault('interfaces', {}). \
                    setdefault(interface, {})
                interface_dict.update({'state': state})
                interface_dict.update({'static_mac_address': static_mac_address})
                interface_dict.update({'mst_i': mst_i})
                interface_dict.update({'mst_i_state': mst_i_state})
                continue

            # VFI 1
            m = p6.match(line)
            if m:
                group = m.groupdict()
                vfi = int(group['vfi'])
                vfi_dict = bridge_domain_dict.setdefault('vfi', {}). \
                    setdefault(vfi, {})
                continue

            # Neighbor 10.1.1.1 pw-id 1, state: up, Static MAC addresses: 0
            m = p7.match(line)
            if m:
                group = m.groupdict()
                neighbor = group['neighbor']
                pw_id = int(group['pw_id'])
                state = group['state']
                static_mac_address = int(group['static_mac_address'])

                neighbor_dict = vfi_dict.setdefault('neighbor', {}). \
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
        return ret_dict

# =====================================================
# Parser for:
#   * 'show l2vpn bridge-domain brief'
# =====================================================

class ShowL2vpnBridgeDomainBrief(ShowL2vpnBridgeDomain):
    """Parser class for 'show l2vpn bridge-domain brief'"""

    cli_command = 'show l2vpn bridge-domain brief'
    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command)
        else:
            out = output
        return super().cli(output=out)


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
                        Optional('mac_aging_time'): int,
                        Optional('mac_aging_type'): str,
                        Optional('mac_limit'): int,
                        Optional('mac_limit_action'): str,
                        Optional('mac_limit_notification'): str,
                        Optional('mac_limit_reached'): str,
                        Optional('security'): str,
                        Optional('dhcp_v4_snooping'): str,
                        'mtu': int,
                        Optional('filter_mac_address'): int,
                        'ac': {
                            'num_ac': int,
                            'num_ac_up': int,
                            Optional('interfaces'): {
                                Any(): {
                                    'state': str,
                                    'type': str,
                                    Optional('mac_aging_type'): str,
                                    Optional('mtu'): int,
                                    'xc_id': str,
                                    'interworking': str,
                                    Optional('mst_i'): int,
                                    Optional('mst_i_state'): str,
                                    Optional('mac_learning'): str,
                                    Optional('flooding'): {
                                        'broadcast_multicast': str,
                                        'unknown_unicast': str
                                    },
                                    Optional('mac_aging_time'): int,
                                    Optional('mac_limit'): int,
                                    Optional('mac_limit_action'): str,
                                    Optional('mac_limit_notification'): str,
                                    Optional('mac_limit_reached'): str,
                                    Optional('security'): str,
                                    Optional('dhcp_v4_snooping'): str,
                                    Optional('static_mac_address'): list,
                                    'statistics': {
                                        'packet_totals': {
                                            'receive': int,
                                            'send': int,
                                        },
                                        'byte_totals': {
                                            'receive': int,
                                            'send': int,
                                        },
                                    }
                                }
                            }
                        },
                        Optional('vfi'): {
                            'num_vfi': int,
                            Any(): {
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
                                                'mpls': {
                                                    Any(): {
                                                        'local': str,
                                                        'remote': str,
                                                        Optional('remote_type'): list,
                                                        Optional('local_type'): list
                                                    }
                                                },
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
                                                },
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
                        'pw': {
                            'num_pw': int,
                            'num_pw_up': int,
                        },
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
        interface_found = False
        
        # Bridge group: g1, bridge-domain: bd1, id: 0, state: up, ShgId: 0, MSTi: 0
        # Bridge group: EVPN-Multicast, bridge-domain: EVPN-Multicast-BTV, id: 0, state: up, ShgId: 0, MSTi: 0
        p1 = re.compile(r'^Bridge +group: +(?P<bridge_group>\w+), +bridge\-domain: +'
            '(?P<bridge_domain>\S+), +id: +(?P<id>\d+), +state: +(?P<state>\w+), +'
            'ShgId: +(?P<shg_id>\d+)(, +MSTi: +(?P<mst_i>\d+))?$')
        
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
        p8 = re.compile(r'^MAC +limit: +(?P<mac_limit>\d+), +Action: +(?P<action>\S+), +Notification: +(?P<notification>\S+)$')

        # MAC limit reached: yes
        p9 = re.compile(r'^MAC +limit +reached: +(?P<mac_limit_reached>\S+)$')

        # Security: disabled
        p10 = re.compile(r'^Security: +(?P<security>\S+)$')

        # DHCPv4 snooping: disabled
        p11 = re.compile(r'DHCPv4 +snooping: +(?P<dhcp_v4_snooping>\S+)$')

        # MTU: 1500
        p12 = re.compile(r'MTU: +(?P<mtu>\d+)$')

        # Filter MAC addresses:
        p13 = re.compile(r'^Filter +MAC +addresses:( +(?P<filter_mac_addresses>\d+))?$')

        # ACs: 1 (1 up), VFIs: 1, PWs: 1 (1 up)
        p14 = re.compile(r'ACs: +(?P<ac>\d+) +\((?P<ac_up>\d+) +up\), +VFIs: +(?P<vfi>\d+), +PWs: +(?P<pw>\d+) +\((?P<pw_up>\d+) +up\)$')

        # List of ACs:
        p15 = re.compile(r'List +of +ACs:$')

        # AC: GigabitEthernet0/1/0/0, state is up
        # AC: GigabitEthernet0/5/1/4, state is admin down
        p16 = re.compile(r'AC: +(?P<interface>\S+), +state +is +(?P<state>[\S ]+)$')

        # Type Ethernet
        p17 = re.compile(r'Type +(?P<type>\S+)$')

        # MTU 1500; XC ID 0x2000001; interworking none; MSTi 0 (unprotected)
        p18 = re.compile(r'MTU +(?P<mtu>\d+); +XC +ID +(?P<xc_id>\S+); +interworking +(?P<interworking>\S+); +MSTi +(?P<mst_i>\d+) +\((?P<mst_i_state>\w+)\)$')

        # Type Ethernet      MTU 1500; XC ID 1; interworking none
        p18_1 = re.compile(r'Type +(?P<pw_type>\S+) +MTU +(?P<mtu>\d+); +XC +ID +(?P<xc_id>\d+); +interworking +(?P<interworking>\S+)$')
        
        # 0000.0000.0000
        p19 = re.compile(r'(?P<static_mac_address>[\d\.]+)$')

        # Statistics:
        p20 = re.compile(r'Statistics:')

        # packet totals: receive 3919680,send 9328
        p21 = re.compile(r'packet +totals: +receive +(?P<receive>\d+), *send +(?P<send>\d+)$')

        # byte totals: receive 305735040,send 15022146
        p22 = re.compile(r'byte +totals: +receive +(?P<receive>\d+), *send +(?P<send>\d+)$')

        # List of Access PWs:
        p23 = re.compile(r'List +of +Access +PWs:$')

        # List of VFIs:
        p24 = re.compile(r'List +of +VFIs:$')

        # VFI 1
        p25 = re.compile(r'VFI +(?P<vfi>\S+)$')

        # PW: neighbor 1.1.1.1, PW ID 1, state is up ( established )
        p26 = re.compile(r'PW: +neighbor +(?P<neighbor>\S+), +PW +ID +(?P<pw_id>\d+), +state +is +(?P<state>[\S ]+)$')

        # PW class mpls, XC ID 0xff000001
        p27 = re.compile(r'PW +class +(?P<pw_class>\w+), +XC +ID +(?P<xc_id>\S+)$')

        # PW class not set
        p27_1 = re.compile(r'PW +class +(?P<pw_class>[\S ]+)$')

        # Encapsulation MPLS, protocol LDP
        p28 = re.compile(r'Encapsulation +(?P<encapsulation>\S+), +protocol +(?P<protocol>\S+)$')

        # PW type Ethernet, control word disabled, interworking none
        p29 = re.compile(r'PW +type +(?P<pw_type>\S+), +control +word +(?P<control_word>\S+), +interworking +(?P<interworking>\S+)$')

        # PW backup disable delay 0 sec
        p30 = re.compile(r'PW +backup +disable +delay +(?P<delay>\d+) +sec$')

        # Sequencing not set
        p31 = re.compile(r'Sequencing +(?P<sequencing>[\S ]+)$')

        # MPLS         Local                          Remote
        p32 = re.compile(r'^MPLS +Local +Remote$')

        # Label        30005                          unknown
        # Group ID     0x5000300                      0x0
        # VCCV CV type 0x2                            0x0
        # Avoid show commands: show l2vpn xconnect detail
        # Avoid Date and Time: Wed Sep 25 20:09:36.362 UTC
        p33 = re.compile(r'^(?!(show +l2vpn))(?P<mpls>[\S ]+)\s+'
                '(?P<local>\S+)\s+(?P<remote>\S+)$')

        # ------------ ------------------------------ -----------------------------
        p34 = re.compile(r'^-+ +-+ +-+$')

        # Create time: 12/03/2008 14:03:00 (17:17:30 ago)
        p36 = re.compile(r'Create +time: +(?P<create_time>[\S ]+)$')

        # Last time status changed: 13/03/2008 05:57:58 (01:22:31 ago)
        p37 = re.compile(r'Last +time +status +changed: +(?P<last_time_status_changed>[\S ]+)$')

        # MAC withdraw message: send 0 receive 0
        p38 = re.compile(r'MAC +withdraw +message: +send +(?P<send>\d+) +receive +(?P<receive>\d+)$')

        # Static MAC addresses:
        p39 = re.compile(r'Static +MAC +addresses:$')

        # VFI Statistics:
        p40 = re.compile(r'VFI +Statistics:$')

        # drops: illegal VLAN 0, illegal length 0
        p41 = re.compile(r'drops: +(?P<drops>\S+) VLAN +(?P<vlan>\d+), +illegal +length +(?P<illegal_length>\d+)$')

        # (control word)                 (control word)  
        p42 = re.compile(r'^\([\S ]+\)$')

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
                else:
                    interface_dict.update({'mac_limit': mac_limit})
                    interface_dict.update({'mac_limit_action': action})
                    interface_dict.update({'mac_limit_notification': notification})
                continue

            # MAC limit reached: yes
            m = p9.match(line)
            if m:
                group = m.groupdict()
                mac_limit_reached = group['mac_limit_reached']
                bridge_domain_dict.update({'mac_limit_reached': mac_limit_reached})

                if dict_type == 'bridge_domain':
                    bridge_domain_dict.update({'mac_limit_reached': mac_limit_reached})
                else:
                    interface_dict.update({'mac_limit_reached': mac_limit_reached})
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
                else:
                    interface_dict.update({'dhcp_v4_snooping': dhcp_v4_snooping})
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
                continue

            # List of ACs:
            m = p15.match(line)
            if m:
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
            m = p17.match(line)
            if m:
                group = m.groupdict()
                ac_type = group['type']
                interface_dict.update({'type': ac_type})
                continue
            
            # MTU 1500; XC ID 0x2000001; interworking none; MSTi 0 (unprotected)
            m = p18.match(line)
            if m:
                group = m.groupdict()
                mtu = int(group['mtu'])
                xc_id = group['xc_id']
                interworking = group['interworking']
                mst_i = int(group['mst_i'])
                mst_i_state = group['mst_i_state']
                interface_dict.update({'mtu': mtu})
                interface_dict.update({'xc_id': xc_id})
                interface_dict.update({'interworking': interworking})
                interface_dict.update({'mst_i': mst_i})
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
                    static_mac_address_list = interface_dict.get('static_mac_address', [])
                else:
                    static_mac_address_list = vfi_obj_dict.get('static_mac_address', [])
                static_mac_address_list.append(static_mac_address)
                interface_dict.update({'static_mac_address': static_mac_address_list})
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

                if dict_type != 'ac':
                    statistics_dict = pw_id_dict.setdefault('statistics', {})
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

                if dict_type != 'ac':
                    statistics_dict = pw_id_dict.setdefault('statistics', {})
                else:
                    statistics_dict = interface_dict.setdefault('statistics', {})
                packet_totals_dict = statistics_dict.setdefault('byte_totals', {})
                packet_totals_dict.update({'receive': receive})
                packet_totals_dict.update({'send': send})
                continue

            # List of Access PWs:
            m = p23.match(line)
            if m:
                continue

            # List of VFIs:
            m = p24.match(line)
            if m:
                continue

            # PW: neighbor 1.1.1.1, PW ID 1, state is up ( established )
            m = p26.match(line)
            if m:
                group = m.groupdict()
                neighbor = group['neighbor']
                pw_id = group['pw_id']
                state = group['state']
                pw_id_dict = vfi_obj_dict.setdefault('neighbor', {}). \
                    setdefault(neighbor, {}). \
                    setdefault('pw_id', {}). \
                    setdefault(pw_id, {})
                pw_id_dict.update({'state': state})
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
                protocol = group['protocol']
                pw_id_dict.update({'encapsulation': encapsulation})
                pw_id_dict.update({'protocol': protocol})
                continue

            # PW type Ethernet, control word disabled, interworking none
            m = p29.match(line)
            if m:
                group = m.groupdict()
                pw_type = group['pw_type']
                control_word = group['control_word']
                interworking = group['interworking']
                pw_id_dict.update({'pw_type': pw_type})
                pw_id_dict.update({'control_word': control_word})
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
                continue

            # VFI Statistics:
            m = p40.match(line)
            if m:
                continue

            # VFI 1
            m = p25.match(line)
            if m:
                group = m.groupdict()
                dict_type = 'vfi'
                vfi = group['vfi']
                vfi_obj_dict = vfi_dict.setdefault(vfi, {})
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
            

            #     (LSP ping verification)               
            #                                    (none)
            #     (control word)                 (control word)
            #     (control word) 
            m = p42.match(line)
            if m:
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

            # Label        30005                          unknown
            # Group ID     0x5000300                      0x0
            # VCCV CV type 0x2                            0x0
            # Avoid show commands: show l2vpn xconnect detail
            # Avoid Date and Time: Wed Sep 25 20:09:36.362 UTC
            m = p33.match(line)
            if m:
                group = m.groupdict()
                mpls = group['mpls'].strip().lower().replace(' ','_')
                local = group['local'].strip()
                remote = group['remote']
                if mpls == 'interface':
                    if interface_found:
                        interface_dict = pw_id_dict.setdefault('mpls', {}). \
                            setdefault('monitor_interface', {})
                        interface_dict.update({'local': local})
                        interface_dict.update({'remote': remote})
                    else:
                        interface_found = True
                        mpls_dict = pw_id_dict.setdefault('mpls', {}). \
                            setdefault(mpls, {})
                        mpls_dict.update({'local': local})
                        mpls_dict.update({'remote': remote})
                else:
                    mpls_dict = pw_id_dict.setdefault('mpls', {}). \
                        setdefault(mpls, {})
                    mpls_dict.update({'local': local})
                    mpls_dict.update({'remote': remote})
                continue
        return ret_dict