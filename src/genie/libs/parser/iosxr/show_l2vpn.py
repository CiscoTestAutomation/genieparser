"""show_l2vpn.py

show l2vpn parser class

"""
# Python
import re
from ipaddress import ip_address

# Genie
from genie.metaparser import MetaParser
from genie.metaparser.util.schemaengine import Any
from genie.libs.parser.utils.common import Common

class ShowL2vpnMacLearning(MetaParser):
    """Parser for show l2vpn mac-learning <mac_type> all location <location>"""

    # TODO schema

    def __init__(self, mac_type='mac', location='local', **kwargs):
        self.location = location
        self.mac_type = mac_type
        super().__init__(**kwargs)

    cli_command = 'show l2vpn mac-learning {mac_type} all location {location}'

    def cli(self, output=None):
        if output is None:
            out = self.device.execute(self.cli_command.format(
                mac_type=self.mac_type,
                location=self.location))
        else:
            out = output

        result = {
            'entries': [],
        }


        for line in out.splitlines():
            line = line.rstrip()
            # Topo ID   Producer       Next Hop(s)       Mac Address       IP Address
            # -------   --------       -----------       --------------    ----------

            # 1         0/0/CPU0       BE1.7             7777.7777.0002
            # 0         0/0/CPU0       BV1               fc00.0001.0006    192.168.30.3
            m = re.match(r'^(?P<topo_id>\d+)'
                         r' +(?P<producer>\S+)'
                         r' +(?:none|(?P<next_hop>\S+))'
                         r' +(?P<mac>[A-Za-z0-9]+\.[A-Za-z0-9]+\.[A-Za-z0-9]+)'
                         r'(?: +(?P<ip_address>\d+\.\d+\.\d+\.\d+|[A-Za-z0-9:]+))?$', line)
            if m:
                entry = {
                    'topo_id': eval(m.group('topo_id')),
                    'producer': m.group('producer'),
                    'next_hop': m.group('next_hop'),
                    'mac': m.group('mac'),
                    'ip_address': m.group('ip_address') \
                    and ip_address(m.group('ip_address')),
                }
                result['entries'].append(entry)
                continue

        return result

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


class ShowL2vpnForwardingBridgeDomainMacAddress(ShowL2vpnForwardingBridgeDomainMacAddressSchema):
    """Parser for:
        show l2vpn forwarding bridge-domain mac-address location <location>
        show l2vpn forwarding bridge-domain <bridge_domain> mac-address location <location>
    """

    cli_command = ['show l2vpn forwarding bridge-domain mac-address location {location}',
                   'show l2vpn forwarding bridge-domain {bridge_domain} mac-address location {location}']

    def cli(self, location, bridge_domain=None, output=None):
        if output is None:
            if bridge_domain:
                cmd = self.cli_command[1].format(location=location, bridge_domain=bridge_domain)
            else:
                cmd = self.cli_command[0].format(location=location)

            out = self.device.execute(cmd)
        else:
            out = output

        # Mac Address Type Learned from/Filtered on LC learned Resync Age/Last Change Mapped to
        p1 = re.compile(r'^Mac +Address +Type +Learned +from\/Filtered +on +LC +learned +Resync Age\/Last +Change +Mapped +to$')

        # 1.01.1 EVPN    BD id: 0                    N/A        N/A                    N/A
        p2 = re.compile(r'^(?P<mac_address>\S+) +(?P<type>\S+) +BD +id: +(?P<bridge_domain>\d+)'
            ' +(?P<lc_learned>\S+) +(?P<resync_age>[\S\s]+) +(?P<mapped_to>\S+)$')

        # 3.3.5          dynamic BE1.2                       N/A        14 Mar 12:46:04        N/A
        # 0001.0000.0002 dynamic Te0/0/1/0/3.3               N/A        0d 0h 0m 14s           N/A
        p3 = re.compile(r'^(?P<mac_address>\S+) +(?P<type>\S+) +(?P<learned_from>[\w\/\.\d]+)'
            ' +(?P<lc_learned>\S+) +(?P<resync_age>[\S\s]+) +(?P<mapped_to>\S+)$')

        # 2.2.2          dynamic (10.25.40.40, 10007)        N/A        14 Mar 12:46:04        N/A
        p4 = re.compile(r'^(?P<mac_address>\S+) +(?P<type>\w+) +(?P<learned_from>[\d\(\)\.\,\s]+)'
            ' +(?P<lc_learned>\S+) +(?P<resync_age>[\S\s]+) +(?P<mapped_to>\S+)$')

        # Init dict
        ret_dict = {}

        # Init vars
        start_parsing = False

        for line in out.splitlines():
            line = line.strip()

            if '------' in line or not line:
                continue

            # Mac Address Type Learned from/Filtered on LC learned Resync Age/Last Change Mapped to
            m = p1.match(line)
            if m:
                start_parsing = True
                continue

            # 1.01.1 EVPN    BD id: 0                    N/A        N/A                    N/A
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
            # 0001.0000.0002 dynamic Te0/0/1/0/3.3               N/A        0d 0h 0m 14s           N/A
            m = p3.match(line)
            if m and start_parsing:
                group = m.groupdict()

                mac_address = group['mac_address']
                learned_from = group['learned_from']
                final_dict = ret_dict.setdefault('mac_table', {}).setdefault(
                    learned_from, {}).setdefault('mac_address', {}).setdefault(
                    mac_address, {})

                keys_list = ['type', 'learned_from', 'lc_learned', 'resync_age', 'mapped_to']
                for key in keys_list:
                    final_dict.update({key: group[key].strip()})
                continue

            # 2.2.2          dynamic (10.25.40.40, 10007)        N/A        14 Mar 12:46:04        N/A
            m = p4.match(line)
            if m and start_parsing:
                group = m.groupdict()

                mac_address = group['mac_address']
                learned_from = group['learned_from'].strip()
                final_dict = ret_dict.setdefault('mac_table', {}).setdefault(
                    learned_from, {}).setdefault('mac_address', {}).setdefault(
                    mac_address, {})

                keys_list = ['type', 'learned_from', 'lc_learned', 'resync_age', 'mapped_to']
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


class ShowL2vpnForwardingProtectionMainInterface(ShowL2vpnForwardingProtectionMainInterfaceSchema):
    """Parser for:
        show l2vpn forwarding protection main-interface location {location}
    """

    cli_command = ['show l2vpn forwarding protection main-interface location {location}']

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
        p2 = re.compile(r'^(?P<main_interface_id>\S+) +(?P<instance>\d+) +(?P<state>\S+)$')


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
                ret_dict.setdefault('main_interface_id', {}).setdefault(
                    main_interface_id, {}).setdefault('instance', {}).setdefault(
                    instance, {}).setdefault('state', state)
                continue

        return ret_dict


# vim: ft=python ts=8 sw=4 et

# ====================================
# Parser for 'show l2vpn bridge-domain'
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
                        'shg_id': int,
                        'mst_i': int,
                        'aging': int,
                        'mac_limit': int,
                        'action': str,
                        'notification': str,
                        'filter_mac_address': int,
                        'ac': {
                            'ac': int,
                            'ac_up': int,
                            'interfaces': {
                                Any(): {
                                    'state': str,
                                    'static_mac_address': int,
                                    'mst_i': int,
                                    'mst_i_state': str
                                }
                            }
                        },
                        'vfi': {
                            'vfi': int,
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
                            'pw': int,
                            'pw_up': int
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
        p2 = re.compile(r'^Aging: +(?P<aging>\d+) s, +MAC +limit: +(?P<mac_limit>\d+), '
            '+Action: +(?P<action>\w+), +Notification: +(?P<notification>\w+)$')

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
                ac_dict.update({'ac': ac})
                ac_dict.update({'ac_up': ac_up})

                vfi_dict = bridge_domain_dict.setdefault('vfi', {})
                vfi_dict.update({'vfi': vfi})

                pw_dict = bridge_domain_dict.setdefault('pw', {})
                pw_dict.update({'pw': pw})
                pw_dict.update({'pw_up': pw_up})
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

        return ret_dict